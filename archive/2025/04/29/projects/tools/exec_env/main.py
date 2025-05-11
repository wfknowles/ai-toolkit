# Placeholder for Execution Environment main script (main.py)

import os
import sys
import logging
import json
import yaml # Requires PyYAML
import difflib
from flask import Flask, request, jsonify # Added Flask imports

# Adjust import path assuming file_io.py is in the parent directory within container
# If file_io.py is copied to the same dir, change to: from file_io import ...
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    # Assuming file_io.py is copied to the same directory in the container
    from file_io import read_file_tool, edit_file_tool, _is_path_allowed # Need access to helper for diff
except ImportError:
    logging.error("Failed to import file_io tools. Ensure file_io.py is accessible.")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Configuration Loading (Task EXE-T-02) ---
CONFIG_PATH = os.environ.get('ALLOW_LIST_CONFIG_PATH', '/etc/fileio/allow_list.yaml')
READ_ALLOW_LIST_EXEC = []
EDIT_ALLOW_LIST_EXEC = []

def load_configuration():
    global READ_ALLOW_LIST_EXEC, EDIT_ALLOW_LIST_EXEC
    logger.info(f"Attempting to load allow-list configuration from: {CONFIG_PATH}")
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = yaml.safe_load(f)
        # Ensure lists contain absolute paths
        read_paths_raw = config.get('read_allow', [])
        edit_paths_raw = config.get('edit_allow', [])
        READ_ALLOW_LIST_EXEC = [os.path.abspath(p) for p in read_paths_raw]
        EDIT_ALLOW_LIST_EXEC = [os.path.abspath(p) for p in edit_paths_raw]
        logger.info(f"Configuration loaded. Read paths: {READ_ALLOW_LIST_EXEC}, Edit paths: {EDIT_ALLOW_LIST_EXEC}")
        # Removed TODO about replacing lists as they are now passed as args
    except FileNotFoundError:
        logger.error(f"Configuration file not found at {CONFIG_PATH}. Using empty allow lists.")
        READ_ALLOW_LIST_EXEC = []
        EDIT_ALLOW_LIST_EXEC = []
    except Exception as e:
        logger.error(f"Error loading configuration from {CONFIG_PATH}: {e}. Using empty allow lists.")
        READ_ALLOW_LIST_EXEC = []
        EDIT_ALLOW_LIST_EXEC = []

# --- Input Sanitization (Task EXE-T-05 Placeholder) ---
def sanitize_filepath(path: str) -> str:
    # Basic sanitization - real implementation might need more robustness
    # (e.g., check for null bytes, unexpected characters, path length)
    if not isinstance(path, str):
        raise ValueError("File path must be a string")
    # normpath helps, but absolute path resolution is key
    return os.path.normpath(path)

def sanitize_content(content: str) -> str:
    # Placeholder - depends on expected content types
    # (e.g., check encoding, potentially limit size, strip dangerous sequences)
    if not isinstance(content, str):
        raise ValueError("Content must be a string")
    return content

# --- Diff Generation (Task EXE-T-08 Placeholder) ---
def generate_diff(file_path: str, proposed_content: str) -> str | None:
    """Generates a diff between current file content and proposed content."""
    logger.info(f"Generating diff for: {file_path}")
    try:
        # Need to read the file securely first!
        # Use the *read* allow list here, passed from the global config.
        read_allowed, norm_path = _is_path_allowed(file_path, READ_ALLOW_LIST_EXEC) # Use loaded list
        if not read_allowed:
            logger.warning(f"Diff generation failed: Read access denied for {file_path}")
            return "Error: Cannot read original file to generate diff (Access Denied)."

        current_content = ""
        if os.path.exists(norm_path) and os.path.isfile(norm_path):
            with open(norm_path, 'r', encoding='utf-8') as f:
                current_content = f.read()

        diff = difflib.unified_diff(
            current_content.splitlines(keepends=True),
            proposed_content.splitlines(keepends=True),
            fromfile=f"a/{os.path.basename(file_path)}",
            tofile=f"b/{os.path.basename(file_path)}",
            lineterm='\n'
        )
        return '\n'.join(diff)
    except Exception as e:
        logger.error(f"Error generating diff for {file_path}: {e}")
        return f"Error generating diff: {e}"

# --- Request Processing (Task EXE-T-04, T-06, T-07) ---
def process_request(request_data: dict) -> dict:
    """Processes a tool execution request."""
    request_id = request_data.get('request_id', 'no-request-id') # Get request_id early for logging
    log_prefix_initial = f"[ExecEnv][Req:{request_id}]" # Log prefix usable even if other fields missing
    try:
        tool_name = request_data.get('tool_name')
        file_path_raw = request_data.get('file_path')
        content_raw = request_data.get('approved_content') # Assuming edit calls provide approved content
        user_id = request_data.get('user_id', 'exec_env_user')

        log_prefix = f"[ExecEnv][Req:{request_id}][User:{user_id}]"
        logger.info(f"{log_prefix} Received request for tool: {tool_name}")

        if not tool_name or not file_path_raw:
            raise ValueError("Missing required fields: tool_name, file_path")

        # Sanitization (Task EXE-T-05)
        file_path = sanitize_filepath(file_path_raw)

        # Invocation (Task EXE-T-06)
        if tool_name == 'read_file':
            # NOTE: Passing user_id - requires file_io.py modification potentially
            # Pass the loaded allow list
            result = read_file_tool(file_path=file_path, read_allow_list=READ_ALLOW_LIST_EXEC, user_id=user_id)
        elif tool_name == 'edit_file':
            if content_raw is None:
                 raise ValueError("Missing required field for edit_file: approved_content")
            content = sanitize_content(content_raw)
            # NOTE: Passing user_id
            # Pass the loaded allow list
            result = edit_file_tool(file_path=file_path, approved_content=content, edit_allow_list=EDIT_ALLOW_LIST_EXEC, user_id=user_id)
        # Add elif here if diff generation is requested as a separate tool/action
        # elif tool_name == 'generate_diff': ...
        else:
            raise ValueError(f"Unsupported tool: {tool_name}")

        # Result Handling (Task EXE-T-07)
        logger.info(f"{log_prefix} Tool '{tool_name}' execution finished. Success: {result.get('success')}")
        response = {"request_id": request_id, **result} # Add request ID back for correlation
        return response

    except Exception as e:
        logger.error(f"{log_prefix} Error processing request {request_data}: {e}")
        return {
            "request_id": request_id,
            "success": False,
            "content": None,
            "error": f"Execution Environment Error: {e}"
        }

# --- Communication Listener (Replaced with Flask API) ---

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_tool():
    """API Endpoint to execute a tool request."""
    request_data = request.json
    request_id = request_data.get('request_id', 'no-request-id')
    log_prefix = f"[ExecEnv][Req:{request_id}]"
    logger.info(f"{log_prefix} Received API request on /execute")

    if not request_data:
        logger.error(f"{log_prefix} Invalid request: No JSON body found.")
        return jsonify({"success": False, "error": "Invalid Request: No JSON body.", "request_id": request_id}), 400

    result = process_request(request_data)

    # Determine status code based on success
    status_code = 200 if result.get('success', False) else 500
    if "Access Denied" in result.get("error", "") or "Invalid Path" in result.get("error", ""):
        status_code = 403 # Forbidden
    elif "Not Found" in result.get("error", ""):
        status_code = 404 # Not Found
    elif "Execution Environment Error" in result.get("error", ""):
        # Keep 500 for internal errors
        pass

    logger.info(f"{log_prefix} Sending response (Status: {status_code}): {json.dumps(result)}")
    return jsonify(result), status_code

@app.route('/generate-diff', methods=['POST'])
def generate_diff_endpoint():
    """API Endpoint to generate a diff for a proposed file change."""
    request_data = request.json
    # Use a generic request ID or extract if provided separately for diff requests
    request_id = request_data.get('request_id', 'diff-request') 
    log_prefix = f"[ExecEnv][Req:{request_id}]"
    logger.info(f"{log_prefix} Received API request on /generate-diff")

    if not request_data:
        logger.error(f"{log_prefix} Invalid request: No JSON body found.")
        return jsonify({"success": False, "error": "Invalid Request: No JSON body.", "diff": None}), 400

    file_path_raw = request_data.get('file_path')
    proposed_content_raw = request_data.get('proposed_content')

    if not file_path_raw or proposed_content_raw is None:
        logger.error(f"{log_prefix} Invalid request: Missing file_path or proposed_content.")
        return jsonify({"success": False, "error": "Invalid Request: Missing file_path or proposed_content.", "diff": None}), 400

    try:
        # Sanitization might be less critical for content here if just generating diff, but good practice
        file_path = sanitize_filepath(file_path_raw)
        proposed_content = sanitize_content(proposed_content_raw)

        diff_result = generate_diff(file_path, proposed_content)

        if diff_result is None or diff_result.startswith("Error:"):
            logger.error(f"{log_prefix} Diff generation failed: {diff_result}")
            # Determine appropriate status code
            status = 403 if "Access Denied" in diff_result else 500
            return jsonify({"success": False, "error": diff_result, "diff": None}), status
        else:
            logger.info(f"{log_prefix} Successfully generated diff for {file_path}")
            return jsonify({"success": True, "error": None, "diff": diff_result}), 200

    except Exception as e:
        logger.error(f"{log_prefix} Unexpected error during diff generation: {e}")
        return jsonify({"success": False, "error": f"Internal Server Error: {e}", "diff": None}), 500

# --- Removed run_listener() function --- 

if __name__ == "__main__":
    load_configuration()
    # Run Flask app (adjust host/port as needed for container environment)
    # Use 0.0.0.0 to be accessible outside the container
    port = int(os.environ.get("EXEC_ENV_PORT", 5001))
    logger.info(f"Starting Execution Environment API server on port {port}...")
    app.run(host='0.0.0.0', port=port) 