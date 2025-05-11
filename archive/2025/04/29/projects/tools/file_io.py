import os
import logging
from typing import List, Dict, Any, Tuple

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration ---
# Allow lists are now passed directly to the functions.
# Removed hardcoded READ_ALLOW_LIST, EDIT_ALLOW_LIST, and PROJECT_ROOT

# --- Helper Functions ---

def _is_path_allowed(file_path: str, allowed_paths: List[str]) -> Tuple[bool, str]:
    """
    Checks if the normalized absolute path is within one of the allowed paths.
    Prevents directory traversal.

    Args:
        file_path (str): The path to the file to check.
        allowed_paths (List[str]): A list of absolute base paths that are allowed.

    Returns:
        Tuple[bool, str]: (is_allowed, normalized_absolute_path)
                         Returns False, '' if path is invalid or not allowed.
    """
    try:
        # Ensure the path is absolute and normalized to resolve '..' etc.
        abs_path = os.path.abspath(file_path)
        normalized_path = os.path.normpath(abs_path)

        # Security: Check if the normalized path still points within the intended root
        # This helps prevent certain types of traversal if PROJECT_ROOT is used in allow list.
        # If allow list contains absolute paths outside project root, this check needs adjustment.
        # if not normalized_path.startswith(PROJECT_ROOT):
        #     logging.warning(f"Path traversal attempt detected outside project root: {file_path}")
        #     return False, "" # Or handle more specifically based on allow_paths structure

        for allowed_base in allowed_paths:
            # Ensure the allowed_base is also absolute and normalized for comparison
            norm_allowed_base = os.path.normpath(os.path.abspath(allowed_base))
            # Check if the normalized path starts with the normalized allowed base directory
            if normalized_path.startswith(norm_allowed_base + os.sep) or normalized_path == norm_allowed_base:
                 # Security: Double-check against relative path components just in case normpath misses something subtle
                 # Although normpath should handle '..', an extra check adds defense in depth.
                 # This check prevents accessing PROJECT_ROOT/data/../other_dir if allowed_base is PROJECT_ROOT/data
                 common_path = os.path.commonpath([norm_allowed_base, normalized_path])
                 if common_path == norm_allowed_base:
                     logging.info(f"Path '{normalized_path}' allowed under '{norm_allowed_base}'.")
                     return True, normalized_path
                 else:
                      # This case should ideally not be hit if normpath works correctly, but log if it does.
                      logging.warning(f"Path traversal detected after normalization check: {file_path} vs {allowed_base}")
                      return False, ""


        logging.warning(f"Path '{normalized_path}' is not within any allowed directories: {allowed_paths}")
        return False, ""
    except Exception as e:
        logging.error(f"Error during path validation for '{file_path}': {e}")
        return False, ""

# --- Tool Implementations ---

def read_file_tool(file_path: str, read_allow_list: List[str], user_id: str = "unknown_user") -> Dict[str, Any]:
    """
    Reads the content of a file if the path is allowed.

    Args:
        file_path (str): The path to the file to read.
        read_allow_list (List[str]): List of allowed absolute base paths for reading.
        user_id (str): Identifier for the user/agent initiating the action.

    Returns:
        Dict[str, Any]: A dictionary containing:
            - 'success' (bool): True if successful, False otherwise.
            - 'content' (str | None): The file content if successful, None otherwise.
            - 'error' (str | None): An error message if unsuccessful, None otherwise.
    """
    log_prefix = f"[read_file_tool][User:{user_id}]"
    logging.info(f"{log_prefix} Requested path: '{file_path}'")

    # Task RF-T-01: Implement path validation using the provided allow list
    is_allowed, normalized_path = _is_path_allowed(file_path, read_allow_list)
    if not is_allowed:
        logging.warning(f"{log_prefix} Access denied for path: '{file_path}'")
        # Task RF-T-04: Implement basic logging (already done via logging calls)
        # Task RF-T-03: Implement error handling
        return {"success": False, "content": None, "error": "Access Denied: Path is not allowed."}

    # Task RF-T-02: Implement file read logic
    try:
        if not os.path.exists(normalized_path):
             logging.warning(f"{log_prefix} File not found: '{normalized_path}'")
             # Task RF-T-03: Implement error handling
             return {"success": False, "content": None, "error": "File Not Found."}
        if not os.path.isfile(normalized_path):
             logging.warning(f"{log_prefix} Path is not a file: '{normalized_path}'")
             # Task RF-T-03: Implement error handling
             return {"success": False, "content": None, "error": "Invalid Path: Not a file."}

        with open(normalized_path, 'r', encoding='utf-8') as f:
            content = f.read()
        logging.info(f"{log_prefix} Successfully read file: '{normalized_path}'")
        # Task RF-T-04: Implement basic logging (already done via logging calls)
        return {"success": True, "content": content, "error": None}

    except Exception as e:
        logging.error(f"{log_prefix} Failed to read file '{normalized_path}': {e}")
        # Task RF-T-03: Implement error handling
        return {"success": False, "content": None, "error": f"Failed to read file: {e}"}

# --- edit_file_tool Implementation ---
# Note: This function assumes user confirmation has already happened
# and the provided `content` is the final approved content to be written.
# The triggering of the confirmation workflow (REQ-EF-003, REQ-EF-004)
# belongs in the calling layer (agent/orchestrator).

def edit_file_tool(file_path: str, approved_content: str, edit_allow_list: List[str], user_id: str = "unknown_user") -> Dict[str, Any]:
    """
    Edits/Overwrites a file with approved content if the path is allowed.
    ASSUMES USER CONFIRMATION HAS ALREADY OCCURRED.

    Args:
        file_path (str): The path to the file to edit/overwrite.
        approved_content (str): The full content approved by the user to write.
        edit_allow_list (List[str]): List of allowed absolute base paths for editing.
        user_id (str): Identifier for the user/agent initiating the action.

    Returns:
        Dict[str, Any]: A dictionary containing:
            - 'success' (bool): True if edit was successful, False otherwise.
            - 'error' (str | None): An error message if unsuccessful, None otherwise.
    """
    log_prefix = f"[edit_file_tool][User:{user_id}]"
    logging.info(f"{log_prefix} Edit approved for path: '{file_path}'")

    # Task EF-T-01: Implement path validation using the provided allow list
    is_allowed, normalized_path = _is_path_allowed(file_path, edit_allow_list)
    if not is_allowed:
        logging.warning(f"{log_prefix} Access denied for edit path: '{file_path}'")
        # Task EF-T-06: Implement detailed logging (already done)
        # Task EF-T-05: Implement error handling
        return {"success": False, "error": "Access Denied: Path is not allowed for editing."}

    # Task EF-T-04: Implement approved edit application logic
    try:
        # Security: Check if path exists and *is* a file before writing
        # Avoid overwriting directories or special files if validation somehow missed it.
        if os.path.exists(normalized_path) and not os.path.isfile(normalized_path):
             logging.warning(f"{log_prefix} Cannot edit path, it is not a file: '{normalized_path}'")
             # Task EF-T-05: Implement error handling
             return {"success": False, "error": "Invalid Path: Cannot edit, not a file."}

        # Consider backup mechanism here (Post-MVP)
        # Simple approach: rename existing file?
        # More complex: versioning system?

        with open(normalized_path, 'w', encoding='utf-8') as f:
            f.write(approved_content)

        logging.info(f"{log_prefix} Successfully wrote approved content to: '{normalized_path}'")
        # Task EF-T-06: Implement detailed logging (already done)
        return {"success": True, "error": None}

    except Exception as e:
        logging.error(f"{log_prefix} Failed to write file '{normalized_path}': {e}")
        # Task EF-T-05: Implement error handling
        return {"success": False, "error": f"Failed to write file: {e}"} 