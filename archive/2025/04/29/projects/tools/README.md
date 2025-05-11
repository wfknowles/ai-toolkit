# File I/O Tools (`file_io.py`)

This module provides basic, security-conscious file reading and writing tools intended for use by AI agents within a controlled environment.

**Security Note:** Access is restricted by predefined allow-lists (`READ_ALLOW_LIST`, `EDIT_ALLOW_LIST`) within the `file_io.py` script. These lists determine which directories the tools can interact with. Edits require explicit user confirmation before being applied.

## Tools Provided

### 1. `read_file_tool`

*   **Purpose:** Reads the entire content of a file located within the `READ_ALLOW_LIST`.
*   **Function Signature (Conceptual):** `read_file(file_path: str) -> {success: bool, content: str | None, error: str | None}`
*   **Parameters:**
    *   `file_path` (string): Path to the file to read (relative or absolute).
*   **Returns:** A dictionary indicating success status, the file content if successful, or an error message if failed (e.g., access denied, file not found).
*   **Security:** Only allows reading from paths configured in `READ_ALLOW_LIST`.

### 2. `edit_file_tool`

*   **Purpose:** Edits/overwrites a file with new content, **but only after explicit user confirmation**.
*   **Function Signature (Conceptual - Represents the post-confirmation action):** `edit_file(file_path: str, approved_content: str) -> {success: bool, error: str | None}`
*   **Parameters:**
    *   `file_path` (string): Path to the file to edit (relative or absolute).
    *   `approved_content` (string): The full, user-approved content to write to the file.
*   **Returns:** A dictionary indicating success or failure of the write operation *after approval*.
*   **Security:** Only allows editing files within the more restrictive `EDIT_ALLOW_LIST`. The core security relies on the **mandatory user confirmation step** that must occur *before* this tool's underlying write action is performed.
*   **Workflow:** Using this tool involves proposing the edit content, waiting for user approval via a separate mechanism, and then this function executes the write if approved.

## Usage Examples (Conceptual Prompts & Interactions)

Here are 10 examples illustrating how these tools might be used in an AI assistant/agent context:

1.  **Simple Read:**
    *   *User:* "What are the contents of `docs/project-summary.txt`?"
    *   *AI Action:* `read_file(file_path='docs/project-summary.txt')`
    *   *AI Response (if successful):* "The contents are: [Content of file]"

2.  **Read from Data Directory:**
    *   *User:* "Load the configuration from `data/config.json`."
    *   *AI Action:* `read_file(file_path='data/config.json')`
    *   *AI Response (if successful):* "Okay, I have loaded the configuration: { [JSON content] }"

3.  **Read Non-Existent File:**
    *   *User:* "Read `data/old_config.txt`."
    *   *AI Action:* `read_file(file_path='data/old_config.txt')`
    *   *AI Response:* "I couldn't find the file `data/old_config.txt`. (Error: File Not Found.)"

4.  **Read Disallowed Path:**
    *   *User:* "Read my system password file at `/etc/shadow`."
    *   *AI Action:* `read_file(file_path='/etc/shadow')`
    *   *AI Response:* "I'm sorry, I cannot access that file. Access is restricted to specific project directories. (Error: Access Denied: Path is not allowed.)"

5.  **Propose a Simple Edit (Requires Confirmation):**
    *   *User:* "Update the status in `data/editable/status.txt` to 'Completed'."
    *   *AI Action (Internal):* Propose calling `edit_file(file_path='data/editable/status.txt', content='Completed')`
    *   *AI Response to User:* "Okay, I can update the status in `data/editable/status.txt` to 'Completed'. Please confirm this change." [Confirmation UI/step appears]
    *   *(If User Confirms)* -> *System Action:* `edit_file_tool('data/editable/status.txt', 'Completed')`
    *   *AI Response (after successful system action):* "I have updated the file `data/editable/status.txt`."

6.  **Propose Edit to Create a New File (Requires Confirmation):**
    *   *User:* "Create a new file `data/editable/notes.txt` with the content 'Initial note.'"
    *   *AI Action (Internal):* Propose `edit_file(file_path='data/editable/notes.txt', content='Initial note.')`
    *   *AI Response to User:* "Okay, I can create the file `data/editable/notes.txt` with the content 'Initial note.'. Please confirm." [Confirmation UI/step appears]
    *   *(If User Confirms)* -> *System Action:* `edit_file_tool('data/editable/notes.txt', 'Initial note.')`
    *   *AI Response (after successful system action):* "I have created the file `data/editable/notes.txt`."

7.  **Propose Edit - User Rejects:**
    *   *User:* "Change the value in `data/editable/config.ini` to `debug=true`."
    *   *AI Action (Internal):* Propose `edit_file(file_path='data/editable/config.ini', content='debug=true')`
    *   *AI Response to User:* "Okay, I can change the value in `data/editable/config.ini` to `debug=true`. Please confirm." [Confirmation UI/step appears]
    *   *(User Rejects)* -> *System Action:* No write operation occurs.
    *   *AI Response:* "Okay, I have cancelled the file edit."

8.  **Attempt Edit on Read-Only Allowed Path:**
    *   *User:* "Add 'Revision 2' to `docs/project-summary.txt`."
    *   *AI Action (Internal):* Propose `edit_file(file_path='docs/project-summary.txt', content='[Original Content] Revision 2')`
    *   *AI Response to User:* "I cannot edit files in the `docs/` directory, only in `data/editable/`. (Error: Access Denied: Path is not allowed for editing.)"
    *   *(Note: Access denied happens before confirmation is even sought)*

9.  **Read then Propose Edit (Requires Confirmation):**
    *   *User:* "Read `data/editable/checklist.md`, add '- Item 3' to the end, and save it back."
    *   *AI Action 1:* `read_file(file_path='data/editable/checklist.md')` -> Gets content, e.g., "- Item 1\n- Item 2"
    *   *AI Action 2 (Internal):* Construct new content: "- Item 1\n- Item 2\n- Item 3". Propose `edit_file(file_path='data/editable/checklist.md', content='- Item 1\n- Item 2\n- Item 3')`
    *   *AI Response to User:* "Okay, I can add '- Item 3' to `data/editable/checklist.md`. The new content will be:\n```markdown\n- Item 1\n- Item 2\n- Item 3\n```\nPlease confirm." [Confirmation UI/step appears]
    *   *(If User Confirms)* -> *System Action:* `edit_file_tool('data/editable/checklist.md', '- Item 1\n- Item 2\n- Item 3')`
    *   *AI Response (after successful system action):* "I have updated the checklist."

10. **Handling Edit Failure (Post-Confirmation):**
    *   *User:* "Save 'Data' to `data/editable/output.txt`."
    *   *AI Action (Internal):* Propose `edit_file(file_path='data/editable/output.txt', content='Data')`
    *   *AI Response to User:* "Okay, I can save 'Data' to `data/editable/output.txt`. Please confirm." [Confirmation UI/step appears]
    *   *(User Confirms)* -> *System Action:* `edit_file_tool('data/editable/output.txt', 'Data')` -> *Fails due to disk full / permissions error*
    *   *AI Response:* "I tried to save the file after you confirmed, but encountered an error: Failed to write file: [Specific OS Error]." 