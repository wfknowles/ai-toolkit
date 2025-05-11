# UI Main Script (using Flask)

import logging
import json
import os
from flask import Flask, request, jsonify, render_template, abort

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__) # Default template folder is 'templates'

# --- In-Memory Store for UI Data (Temporary) ---
# Stores data passed from Orchestrator needed to render the confirmation page.
# Key: request_id, Value: {'file_path': str, 'diff_content': str}
UI_PENDING_CONFIRMATIONS = {}

# --- Orchestrator Interaction (Placeholder Functions) --- 
# These functions are not used in the UI service itself for *receiving* commands,
# but kept for context from the original file. The UI *sends* decisions back.
# def display_confirmation_dialog(...) - Replaced by Flask rendering
# def receive_confirmation_request(...) - Replaced by /display endpoint
# def send_user_decision(...) - Happens via HTML form submission in template

# --- Flask Endpoints --- 

@app.route('/display', methods=['POST'])
def display_confirmation_request():
    """Receives confirmation details from the Orchestrator.
    
    Stores the details needed to render the confirmation page later.
    Expected JSON body: {'request_id': str, 'file_path': str, 'diff_content': str}
    """
    data = request.json
    request_id = data.get('request_id')
    file_path = data.get('file_path')
    diff_content = data.get('diff_content')
    log_prefix = f"[UI][Req:{request_id}]"

    logger.info(f"{log_prefix} Received confirmation request from Orchestrator via /display.")

    if not all([request_id, file_path, diff_content]):
        logger.error(f"{log_prefix} Invalid request data received on /display.")
        return jsonify({"success": False, "error": "Missing required data (request_id, file_path, diff_content)"}), 400

    # Store data for later retrieval by the confirmation page
    UI_PENDING_CONFIRMATIONS[request_id] = {
        "file_path": file_path,
        "diff_content": diff_content
    }
    logger.info(f"{log_prefix} Stored confirmation details. User should navigate to /confirm/{request_id}")
    logger.debug(f"{log_prefix} Current UI pending state: {UI_PENDING_CONFIRMATIONS}")
    
    # Respond to Orchestrator (just acknowledging receipt)
    return jsonify({"success": True, "message": f"Confirmation details received. User should visit /confirm/{request_id}"}), 200

@app.route('/confirm/<string:request_id>', methods=['GET'])
def show_confirmation_page(request_id: str):
    """Renders the HTML confirmation page for the user.
    
    Retrieves data stored by the /display endpoint.
    """
    log_prefix = f"[UI][Req:{request_id}]"
    logger.info(f"{log_prefix} User accessed /confirm page.")

    confirmation_data = UI_PENDING_CONFIRMATIONS.get(request_id)

    if not confirmation_data:
        logger.error(f"{log_prefix} No pending confirmation data found for this request ID.")
        abort(404, description="Confirmation request not found or already processed.")

    # Render the template, passing the necessary data
    return render_template(
        'confirmation.html',
        request_id=request_id,
        file_path=confirmation_data['file_path'],
        diff_content=confirmation_data['diff_content']
    )

# --- Example Simulation (Removed - Replaced by Flask app) --- 
# if __name__ == "__main__": ...

if __name__ == "__main__":
    # Run Flask app (adjust host/port as needed)
    # Use 0.0.0.0 to be accessible outside the container/network
    port = int(os.environ.get("UI_PORT", 5000))
    logger.info(f"Starting UI Confirmation Server on port {port}...")
    # Note: Use development server only. For production, use Gunicorn/Waitress etc.
    app.run(host='0.0.0.0', port=port, debug=False) 