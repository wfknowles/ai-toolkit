# Placeholder for Orchestrator main script (main.py)

import logging
import json
import time
import uuid
import os # Added for path operations
import requests # Added for HTTP requests
from typing import Tuple, List, Dict, Any
from flask import Flask, request, jsonify # Added Flask imports
import threading # Added for running Flask in background
# --- Gemini Imports ---
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold, Tool, FunctionDeclaration, FunctionResponse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Directory containing tool JSON definitions (adjust path as needed)
TOOL_DEFINITION_DIR = os.path.join(os.path.dirname(__file__), '..', 'tool_definitions')
# Execution Environment API endpoint
EXEC_ENV_URL = os.environ.get("EXEC_ENV_URL", "http://localhost:5001") # Base URL
EXEC_TOOL_ENDPOINT = f"{EXEC_ENV_URL}/execute"
DIFF_TOOL_ENDPOINT = f"{EXEC_ENV_URL}/generate-diff"
# UI Interaction Endpoint
UI_DISPLAY_ENDPOINT = os.environ.get("UI_DISPLAY_ENDPOINT", "http://localhost:5000/display")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    logger.warning("GEMINI_API_KEY environment variable not set. AI calls will fail.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Safety settings for Gemini - Adjust as needed
SAFETY_SETTINGS = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# --- In-Memory State for Pending Confirmations ---
# NOTE: This is for demonstration. In production, use a persistent store (DB, Cache).
PENDING_CONFIRMATIONS = {}

# Initialize the Gemini model (choose appropriate model)
# Using 1.5 Flash as it's fast and supports tool calling well
ai_model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    safety_settings=SAFETY_SETTINGS
)

# --- Orchestrator Flask App --- 
app = Flask(__name__)

@app.route('/confirm/<string:request_id>', methods=['POST'])
def handle_confirmation_callback(request_id: str):
    """Receives the user's decision from the UI form submission."""
    log_prefix = f"[Orchestrator][Req:{request_id}]"
    logger.info(f"{log_prefix} Received confirmation callback from UI.")
    
    decision = request.form.get('decision') # Get decision from form data
    logger.info(f"{log_prefix} User decision: {decision}")

    retrieved_details = get_pending_confirmation(request_id)

    if not retrieved_details:
         logger.error(f"{log_prefix} State lost for pending confirmation during callback!")
         # Simplified: Cannot easily call send_result_to_ai_model without history here
         # In a real system, history might be stored with the pending state.
         return "Error: Confirmation state lost.", 500 # Respond to UI callback
    
    tool_result = {}
    if decision == "Approved":
        logger.info(f"{log_prefix} Edit approved by user. Triggering execution.")
        exec_request = {
            "request_id": request_id,
            "user_id": retrieved_details['user_id'],
            "tool_name": "edit_file", # Assuming confirmation only happens for edit_file
            "file_path": retrieved_details['file_path'],
            "approved_content": retrieved_details['content']
        }
        # Execute the tool
        tool_result = trigger_execution_env(exec_request)
        
    elif decision == "Rejected":
        logger.info(f"{log_prefix} Edit rejected by user.")
        tool_result = {"request_id": request_id, "success": False, "error": "USER_REJECTED_EDIT"}
    else:
        logger.error(f"{log_prefix} Invalid decision received: {decision}")
        tool_result = {"request_id": request_id, "success": False, "error": "INVALID_DECISION_RECEIVED"}

    # --- Simplified AI call for callback ---
    # Ideally, we'd retrieve the conversation history associated with request_id
    # and call send_result_to_ai_model(history, tool_result)
    # For now, just log the tool result. A separate system would handle notifying the user.
    logger.info(f"{log_prefix} Final tool result after UI interaction: {tool_result}")
    # final_ai_response = send_result_to_ai_model(??history??, tool_result) # Need history!
    final_response_content = f"Processed decision '{decision}'. Final result logged."
    # --- End Simplified Section ---

    delete_pending_confirmation(request_id)
    
    # Respond to the UI callback POST request
    # Show a simple message to the user in the browser after they click approve/reject
    return f"Action {decision}. Request ID: {request_id}. Result logged.", 200

def run_orchestrator_server():
    """Runs the Flask server in a separate thread."""
    port = int(os.environ.get("ORCHESTRATOR_PORT", 5002))
    logger.info(f"Starting Orchestrator callback server on port {port}...")
    # Use development server only. For production, use Gunicorn/Waitress etc.
    # Run in a thread to not block the main handle_prompt logic (if run as a script)
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False), daemon=True).start()

# --- AI Interaction Functions --- 

def convert_schema_to_gemini_tool(schemas: List[Dict[str, Any]]) -> Tool | None:
    """Converts loaded JSON schemas to Gemini Tool object."""
    function_declarations = []
    for schema in schemas:
        try:
            # Basic validation
            name = schema.get("name")
            description = schema.get("description")
            parameters = schema.get("parameters")
            if not all([name, description, parameters]):
                 logger.warning(f"Skipping invalid schema (missing name, description, or parameters): {schema.get('name', 'N/A')}")
                 continue
                 
            # Parameters should be in OpenAPI format
            fd = FunctionDeclaration(name=name, description=description, parameters=parameters)
            function_declarations.append(fd)
        except Exception as e:
            logger.error(f"Error converting schema '{schema.get('name', 'N/A')}' to FunctionDeclaration: {e}")
            
    if not function_declarations:
        return None
        
    return Tool(function_declarations=function_declarations)

def call_ai_model(prompt: str, gemini_tools: Tool | None) -> dict:
    """Calls the configured Gemini model with the prompt and tools."""
    logger.info("Calling Gemini model...")
    if not GEMINI_API_KEY:
        return {"type": "error", "content": "Gemini API key not configured."}
        
    try:
        # Start conversation with the user prompt
        conversation_history = [{'role': 'user', 'parts': [prompt]}]
        
        response = ai_model.generate_content(
            conversation_history,
            tools=[gemini_tools] if gemini_tools else None,
        )
        
        response_part = response.candidates[0].content.parts[0]

        if hasattr(response_part, 'function_call') and response_part.function_call:
            fc = response_part.function_call
            # Convert Struct args to dict
            params = {key: value for key, value in fc.args.items()}
            logger.info(f"Gemini requested tool call: {fc.name} with params: {params}")
            # Include the function call in history for the next turn
            conversation_history.append({'role': 'model', 'parts': [response_part]})
            return {
                "type": "tool_call", 
                "tool_name": fc.name, 
                "parameters": params,
                "conversation_history": conversation_history # Pass history along
            }
        elif hasattr(response_part, 'text'):
             logger.info(f"Gemini returned text response: {response_part.text}")
             return {"type": "text", "content": response_part.text}
        else:
             logger.error(f"Gemini returned unexpected response part: {response_part}")
             return {"type": "error", "content": "Unexpected response format from AI."}

    except Exception as e:
        logger.error(f"Error calling Gemini API: {e}", exc_info=True)
        # Check for specific GenAI exceptions if needed
        return {"type": "error", "content": f"Error calling AI model: {e}"}

def send_result_to_ai_model(conversation_history: list, tool_result: dict) -> dict:
    """Sends the tool execution result back to the Gemini model."""
    log_prefix = f"[Orchestrator][Req:{tool_result.get('request_id', 'N/A')}]"
    logger.info(f"{log_prefix} Sending tool result back to Gemini: {tool_result}")
    
    if not GEMINI_API_KEY:
        return {"type": "error", "content": "Gemini API key not configured."}
        
    # --- Find the original function call in history to get the tool name ---
    # The history should end with model's function call request
    last_model_part = None
    if conversation_history and conversation_history[-1]['role'] == 'model':
        last_model_part = conversation_history[-1]['parts'][0]
        
    if not (last_model_part and hasattr(last_model_part, 'function_call')):
         logger.error(f"{log_prefix} Could not find previous function call in history to send result for.")
         return {"type": "error", "content": "Internal Error: Invalid conversation history state."}
         
    tool_name = last_model_part.function_call.name
    # --- End Find ---
    
    try:
        # Format the tool result as FunctionResponse
        function_response = FunctionResponse(
             name=tool_name,
             response=tool_result # Send the whole dict (success, content/error)
        )
        
        # Append the function response to the history
        conversation_history.append({'role': 'function', 'parts': [function_response]})

        # Call Gemini again with the updated history
        response = ai_model.generate_content(conversation_history) # No tools needed now
        
        final_text = response.candidates[0].content.parts[0].text
        logger.info(f"{log_prefix} Received final text response from Gemini: {final_text}")
        return {"type": "text", "content": final_text}

    except Exception as e:
        logger.error(f"{log_prefix} Error sending tool result to Gemini API: {e}", exc_info=True)
        return {"type": "error", "content": f"Error processing tool result with AI: {e}"}

# --- Core Logic Functions (Exec Env, Diff, UI Notify, State) ---
# (trigger_execution_env, trigger_exec_env_diff, notify_ui_of_confirmation) 
# (store_pending_confirmation, get_pending_confirmation, delete_pending_confirmation) 
def trigger_execution_env(request_data: dict) -> dict:
    """Sends a request to the execution environment API (/execute) and returns the result."""
    request_id = request_data['request_id']
    log_prefix = f"[Orchestrator][Req:{request_id}]"
    logger.info(f"{log_prefix} Triggering Execution Environment via API (/execute) for tool: {request_data['tool_name']}")
    
    try:
        response = requests.post(EXEC_TOOL_ENDPOINT, json=request_data, timeout=60) # Use specific endpoint
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        result = response.json()
        logger.info(f"{log_prefix} Received response from Execution Environment (/execute): {result}")
        return result
    except requests.exceptions.ConnectionError as e:
        error_msg = f"Connection Error: Could not connect to Execution Environment at {EXEC_TOOL_ENDPOINT}. {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"request_id": request_id, "success": False, "error": error_msg}
    except requests.exceptions.Timeout as e:
        error_msg = f"Timeout Error: Request to Execution Environment (/execute) timed out. {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"request_id": request_id, "success": False, "error": error_msg}
    except requests.exceptions.RequestException as e:
        error_msg = f"Request Error: Failed to get valid response from Execution Environment (/execute). Status: {e.response.status_code if e.response else 'N/A'}. Response: {e.response.text if e.response else 'N/A'}. Error: {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"request_id": request_id, "success": False, "error": error_msg}
    except json.JSONDecodeError as e:
        error_msg = f"JSON Decode Error: Invalid JSON response from Execution Environment (/execute). {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"request_id": request_id, "success": False, "error": error_msg}

def trigger_exec_env_diff(request_id: str, file_path: str, proposed_content: str) -> dict:
    """Requests a diff from the execution environment API (/generate-diff)."""
    log_prefix = f"[Orchestrator][Req:{request_id}]"
    logger.info(f"{log_prefix} Requesting diff from Execution Environment for: {file_path}")
    request_data = {
        "request_id": request_id, # Pass along the original request ID
        "file_path": file_path,
        "proposed_content": proposed_content
    }
    try:
        response = requests.post(DIFF_TOOL_ENDPOINT, json=request_data, timeout=30) # Shorter timeout for diff
        response.raise_for_status()
        result = response.json()
        logger.info(f"{log_prefix} Received response from Execution Environment (/generate-diff): {result}")
        return result # Expected format: {"success": bool, "error": str|None, "diff": str|None}
    except requests.exceptions.ConnectionError as e:
        error_msg = f"Connection Error: Could not connect to Execution Environment at {DIFF_TOOL_ENDPOINT}. {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"success": False, "error": error_msg, "diff": None}
    except requests.exceptions.Timeout as e:
        error_msg = f"Timeout Error: Request to Execution Environment (/generate-diff) timed out. {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"success": False, "error": error_msg, "diff": None}
    except requests.exceptions.RequestException as e:
        error_msg = f"Request Error: Failed to get valid response from Execution Environment (/generate-diff). Status: {e.response.status_code if e.response else 'N/A'}. Response: {e.response.text if e.response else 'N/A'}. Error: {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"success": False, "error": error_msg, "diff": None}
    except json.JSONDecodeError as e:
        error_msg = f"JSON Decode Error: Invalid JSON response from Execution Environment (/generate-diff). {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"success": False, "error": error_msg, "diff": None}

def notify_ui_of_confirmation(request_id: str, file_path: str, diff_content: str) -> dict:
    """Notifies the UI service about a pending confirmation request.
    
    Sends data to the UI's /display endpoint.
    """
    log_prefix = f"[Orchestrator][Req:{request_id}]"
    logger.info(f"{log_prefix} Notifying UI service at {UI_DISPLAY_ENDPOINT} about pending confirmation.")
    ui_request_data = {
        "request_id": request_id,
        "file_path": file_path,
        "diff_content": diff_content
    }
    try:
        response = requests.post(UI_DISPLAY_ENDPOINT, json=ui_request_data, timeout=10)
        response.raise_for_status()
        ui_response = response.json()
        logger.info(f"{log_prefix} Received response from UI service (/display): {ui_response}")
        # Return success/failure based on UI acknowledging receipt
        return {"success": True, "message": ui_response.get("message", "UI acknowledged.")}
    except requests.exceptions.ConnectionError as e:
        error_msg = f"Connection Error: Could not connect to UI service at {UI_DISPLAY_ENDPOINT}. {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"success": False, "error": error_msg}
    except requests.exceptions.RequestException as e:
        error_msg = f"Request Error: Failed to notify UI service. Status: {e.response.status_code if e.response else 'N/A'}. Response: {e.response.text if e.response else 'N/A'}. Error: {e}"
        logger.error(f"{log_prefix} {error_msg}")
        return {"success": False, "error": error_msg}

def store_pending_confirmation(request_id: str, details: dict):
    """Stores pending confirmation state in the in-memory dictionary."""
    log_prefix = f"[Orchestrator][Req:{request_id}]"
    logger.info(f"{log_prefix} Storing pending confirmation state.")
    PENDING_CONFIRMATIONS[request_id] = {**details, "timestamp": time.time()}
    logger.debug(f"{log_prefix} Current pending state: {PENDING_CONFIRMATIONS}")
    # Real implementation interacts with state store
    # pass

def get_pending_confirmation(request_id: str) -> dict | None:
    """Retrieves pending confirmation state from the in-memory dictionary."""
    log_prefix = f"[Orchestrator][Req:{request_id}]"
    logger.info(f"{log_prefix} Retrieving pending confirmation state.")
    details = PENDING_CONFIRMATIONS.get(request_id)
    if details:
        logger.debug(f"{log_prefix} Found pending state: {details}")
    else:
        logger.warning(f"{log_prefix} No pending state found for request ID.")
    # Real implementation interacts with state store
    # Simulate finding it for now
    # return {"file_path": "data/editable/task.cfg", "content": "status=Done", "user_id": "sim_user"}
    return details

def delete_pending_confirmation(request_id: str):
     """Deletes state from the in-memory dictionary after completion/timeout."""
     log_prefix = f"[Orchestrator][Req:{request_id}]"
     logger.info(f"{log_prefix} Deleting pending confirmation state.")
     removed_item = PENDING_CONFIRMATIONS.pop(request_id, None)
     if removed_item:
         logger.debug(f"{log_prefix} Removed state for request ID.")
     else:
         logger.warning(f"{log_prefix} Attempted to delete state, but request ID not found.")
     logger.debug(f"{log_prefix} Remaining pending state: {PENDING_CONFIRMATIONS}")
     # pass

# DEPRECATED trigger_ui_confirmation - should be removed eventually
def trigger_ui_confirmation(request_id: str, file_path: str, content_or_diff: str):
     """DEPRECATED: Replaced by notify_ui_of_confirmation and the /confirm callback."""
     logger.warning("DEPRECATED function trigger_ui_confirmation called.")
     return "Approved" # Simulate old behavior if called somehow

# --- Helper Function to Load Schemas ---
def load_tool_schemas(directory: str) -> list:
    """Loads all .json tool schemas from the specified directory."""
    schemas = []
    logger.info(f"Loading tool schemas from: {directory}")
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                file_path = os.path.join(directory, filename)
                try:
                    with open(file_path, 'r') as f:
                        schema = json.load(f)
                        schemas.append(schema)
                        logger.info(f"Loaded schema: {filename}")
                except json.JSONDecodeError:
                    logger.error(f"Error decoding JSON from {file_path}")
                except Exception as e:
                    logger.error(f"Error loading schema from {file_path}: {e}")
    except FileNotFoundError:
        logger.error(f"Tool definition directory not found: {directory}")
    except Exception as e:
        logger.error(f"Error listing tool directory {directory}: {e}")
    
    if not schemas:
        logger.warning("No tool schemas were loaded.")
    return schemas

# --- Helper Function to Validate Parameters ---
def validate_parameters(tool_name: str, parameters: dict, tool_schemas: list) -> Tuple[bool, str | None]:
    """Validates received parameters against the tool's schema.

    Args:
        tool_name (str): The name of the tool requested.
        parameters (dict): The parameters received from the AI.
        tool_schemas (list): The list of loaded tool schemas.

    Returns:
        Tuple[bool, str | None]: (is_valid, error_message)
                                 error_message is None if valid.
    """
    schema = next((s for s in tool_schemas if s.get('name') == tool_name), None)
    if not schema:
        # This should ideally not happen if AI only calls tools from the provided list,
        # but check just in case.
        return False, f"Schema not found for tool: {tool_name}"

    schema_params = schema.get('parameters', {})
    schema_props = schema_params.get('properties', {})
    required_params = schema_params.get('required', [])

    missing_params = [p for p in required_params if p not in parameters]
    if missing_params:
        return False, f"Missing required parameters: {', '.join(missing_params)}"

    # Basic type check (optional, can be expanded)
    # for param_name, param_details in schema_props.items():
    #     if param_name in parameters:
    #         expected_type = param_details.get('type')
    #         actual_value = parameters[param_name]
    #         # Add type checking logic here (e.g., isinstance checks)
    #         pass 

    # Check for unexpected parameters (optional, could be strict)
    # unexpected_params = [p for p in parameters if p not in schema_props]
    # if unexpected_params:
    #     return False, f"Unexpected parameters provided: {', '.join(unexpected_params)}"

    return True, None

# --- Main Orchestration Logic --- 
def handle_prompt(user_prompt: str, user_id: str):
    """Handles a user prompt, interacts with AI, tools, and UI."""
    log_prefix = f"[Orchestrator][User:{user_id}]"
    logger.info(f"{log_prefix} --- Handling prompt: '{user_prompt}' ---")
    
    # --- 1. Load Tool Definitions ---
    tool_schemas_json = load_tool_schemas(TOOL_DEFINITION_DIR)
    if not tool_schemas_json: 
         error_msg = "Internal Error: Could not load tool definitions."
         logger.error(f"{log_prefix} {error_msg}")
         return error_msg 
         
    gemini_tools = convert_schema_to_gemini_tool(tool_schemas_json)
    if not gemini_tools:
        logger.warning(f"{log_prefix} No valid Gemini tools could be created from schemas.")
        # Decide if processing should continue without tools

    # --- 2. Initial AI Call ---
    ai_response = call_ai_model(user_prompt, gemini_tools)
    conversation_history = ai_response.pop("conversation_history", [{'role': 'user', 'parts': [user_prompt]}]) # Store history if AI returns it

    final_ai_response = None # Variable to hold the final outcome

    # --- 3. Process AI Response ---
    if ai_response['type'] == 'tool_call':
        tool_name = ai_response['tool_name']
        parameters = ai_response['parameters']
        request_id = str(uuid.uuid4()) # Generate unique ID for this tool request flow
        log_prefix_req = f"[Orchestrator][Req:{request_id}]"
        logger.info(f"{log_prefix_req} AI requested tool '{tool_name}' with params: {parameters}")

        # --- 3a. Validate Parameters ---
        is_valid, validation_error = validate_parameters(tool_name, parameters, tool_schemas_json)
        if not is_valid:
            logger.error(f"{log_prefix_req} Parameter validation failed: {validation_error}")
            error_result = {"request_id": request_id, "success": False, "error": f"Parameter Validation Failed: {validation_error}"}
            final_ai_response = send_result_to_ai_model(conversation_history, error_result)
        else:
            # Parameters valid, proceed by tool type
            # --- 3b. Handle Read File ---
            if tool_name == 'read_file':
                logger.info(f"{log_prefix_req} Handling direct execution for: {tool_name}")
                exec_request = {"request_id": request_id, "user_id": user_id, "tool_name": tool_name, **parameters}
                tool_result = trigger_execution_env(exec_request)
                # Send result back to AI
                final_ai_response = send_result_to_ai_model(conversation_history, tool_result)

            # --- 3c. Handle Edit File (Requires Confirmation) ---
            elif tool_name == 'edit_file':
                logger.info(f"{log_prefix_req} Handling confirmation flow for: {tool_name}")
                file_path = parameters['file_path']
                content = parameters['content']
                
                # Generate Diff
                diff_response = trigger_exec_env_diff(request_id, file_path, content)
                
                if not diff_response.get("success"):
                    logger.error(f"{log_prefix_req} Failed to generate diff: {diff_response.get('error')}")
                    error_result = {"request_id": request_id, "success": False, "error": f"Failed to generate diff: {diff_response.get('error')}"}
                    final_ai_response = send_result_to_ai_model(conversation_history, error_result)
                else:
                    # Diff succeeded, proceed with confirmation
                    diff_for_ui = diff_response.get("diff", "Error: Diff content missing.")
                    
                    # Store pending state (including conversation history for potential resume later)
                    # NOTE: Storing history here is crucial for proper resume in callback, but complex for in-memory
                    pending_details = {**parameters, "user_id": user_id, "conversation_history": conversation_history}
                    store_pending_confirmation(request_id, pending_details)

                    # Notify UI
                    ui_notification_result = notify_ui_of_confirmation(request_id, file_path, diff_for_ui)

                    if ui_notification_result.get("success"):
                        # Return pending message - workflow continues in /confirm callback
                        final_response_content = f"Confirmation required for request {request_id}. Please approve or reject via the UI."
                        final_ai_response = {"type": "text", "content": final_response_content} 
                    else:
                        # Failed to notify UI
                        error_msg = f"Failed to notify UI for confirmation: {ui_notification_result.get('error')}"
                        logger.error(f"{log_prefix_req} {error_msg}")
                        delete_pending_confirmation(request_id) # Clean up state
                        error_result = {"request_id": request_id, "success": False, "error": error_msg}
                        final_ai_response = send_result_to_ai_model(conversation_history, error_result)
            
            # --- 3d. Handle Unknown Validated Tool (Shouldn't happen if schema loading is correct) ---
            else: 
                logger.warning(f"{log_prefix_req} Unknown tool requested (post-validation): {tool_name}")
                error_result = {"request_id": request_id, "success": False, "error": f"Unknown tool: {tool_name}"}
                final_ai_response = send_result_to_ai_model(conversation_history, error_result)

    # --- 4. Handle Simple Text Response ---
    elif ai_response['type'] == 'text':
        final_ai_response = ai_response # Just use the direct text response
    
    # --- 5. Handle AI Call Error ---
    elif ai_response['type'] == 'error':
        logger.error(f"{log_prefix} Error received directly from AI call: {ai_response['content']}")
        final_ai_response = {"type": "text", "content": f"Sorry, there was an error communicating with the AI: {ai_response['content']}"}

    # --- 6. Handle Unexpected AI Response Format ---
    else:
        logger.error(f"{log_prefix} Unknown AI response type: {ai_response.get('type')}")
        final_ai_response = {"type": "text", "content": "Sorry, an internal error occurred processing the AI response."}

    # --- 7. Log and Return Final Response ---
    if final_ai_response and 'content' in final_ai_response:
        logger.info(f"{log_prefix} --- Final response for prompt: {final_ai_response['content']} ---")
        return final_ai_response['content']
    else:
        # Should not happen if all paths set final_ai_response correctly
        logger.error(f"{log_prefix} --- Failed to determine final response ---")
        return "Error: Could not determine final response."

if __name__ == "__main__":
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set. Exiting.")
        exit()
        
    # Start the Flask server in the background
    run_orchestrator_server()
    time.sleep(1) 

    # --- Example Usage --- 
    print("--- Test Case 1: Read File (Requires Gemini API Key) ---")
    response1 = handle_prompt("Summarize docs/report.txt", "user_gemini_a")
    print(f"Response: {response1}")
    print("\n---")
    
    print("--- Test Case 2: Edit File (Requires Gemini API Key & UI Interaction) ---")
    response2 = handle_prompt("Update status to 'Done' in data/editable/task.cfg", "user_gemini_b")
    print(f"Initial response: {response2}")
    print("\n--- Please manually navigate to the UI confirmation page if prompted --- ")
    print("--- Waiting for potential UI callback (e.g., 30 seconds)... ---")
    time.sleep(30) 
    print("\n--- Test script finished. Check logs for callback results. ---") 