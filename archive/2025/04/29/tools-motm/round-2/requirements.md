# Master Requirements List: Custom File I/O Tools (MVP)

**Date:** 2024-07-23
**Source:** MotM Rounds 1 & 2

This document outlines the requirements, acceptance criteria, and guidelines for the Minimum Viable Product (MVP) of the custom `read_file` and `edit_file` tools.

---

## 1. Tool: `read_file` (MVP)

*   **Definition:** A tool that allows the AI agent to read the contents of a specified file path within allowed directories.
*   **Asset(s):**
    *   API Endpoint (`/readFile`)
    *   Core Implementation Code
    *   Standardized Tool Description (for prompts)
*   **Requirements:**
    *   REQ-RF-001: Must accept a file path string as input.
    *   REQ-RF-002: Must validate the file path against a pre-defined allow-list of accessible directories/patterns.
    *   REQ-RF-003: Must return the full content of the specified file if access is allowed and the file exists.
    *   REQ-RF-004: Must return a structured error response if the path is disallowed, the file doesn't exist, or a read error occurs.
    *   REQ-RF-005: Must log basic usage information (timestamp, file path requested, success/failure status, calling agent/user ID) to a defined metrics schema.
*   **Acceptance Criteria:**
    *   AC-RF-001: Given a valid path in the allow-list, the tool returns the complete file content.
    *   AC-RF-002: Given an invalid path outside the allow-list, the tool returns a specific 'Access Denied' error.
    *   AC-RF-003: Given a path to a non-existent file (within the allow-list), the tool returns a specific 'File Not Found' error.
    *   AC-RF-004: Basic usage logs are generated correctly for successful and failed calls.
*   **Guidelines:**
    *   GUIDE-RF-001: Implementation should prioritize security and handle potential exceptions gracefully.
    *   GUIDE-RF-002: Tool description for the agent should clearly state its purpose, required parameters, and potential errors.

---

## 2. Tool: `edit_file` (MVP)

*   **Definition:** A tool that allows the AI agent to propose modifications to a specified file path, requiring user confirmation before applying the changes.
*   **Asset(s):**
    *   API Endpoint (`/editFile`)
    *   Core Implementation Code (including user confirmation hook)
    *   Standardized Tool Description (for prompts)
    *   User Confirmation UI Mockup/Description
*   **Requirements:**
    *   REQ-EF-001: Must accept a file path string and the proposed content/edit instructions as input.
    *   REQ-EF-002: Must validate the file path against a pre-defined allow-list (potentially more restrictive than `read_file`).
    *   REQ-EF-003: Must NOT apply changes directly. Instead, it must trigger a user confirmation workflow.
    *   REQ-EF-004: The user confirmation workflow must present the file path, proposed change (e.g., a diff), and clear approve/reject options.
    *   REQ-EF-005: Only upon user approval should the tool attempt to apply the change to the file.
    *   REQ-EF-006: Must return a structured response indicating whether the edit was proposed, approved, applied successfully, rejected, or failed (with error details).
    *   REQ-EF-007: Must log detailed usage information (timestamp, file path, proposed change summary, approval status, success/failure, calling agent/user ID).
*   **Acceptance Criteria:**
    *   AC-EF-001: Given a valid path and content, the tool triggers the user confirmation workflow with correct details.
    *   AC-EF-002: If the user approves, the tool correctly applies the change to the target file.
    *   AC-EF-003: If the user rejects, the tool does not modify the file and reports rejection.
    *   AC-EF-004: Given an invalid path, the tool returns an 'Access Denied' error without triggering confirmation.
    *   AC-EF-005: Detailed usage logs are generated correctly for all stages (proposal, approval/rejection, success/failure).
*   **Guidelines:**
    *   GUIDE-EF-001: User confirmation step is critical and must be robust.
    *   GUIDE-EF-002: Consider file locking or other mechanisms to prevent race conditions if concurrent edits are possible (though likely deferred post-MVP).
    *   GUIDE-EF-003: Tool description must emphasize the user confirmation step and the potential impact of edits.

---

## 3. System Components (MVP)

*   **Asset:** API Specification (covering both tools)
*   **Asset:** Metrics/Logging Schema
*   **Asset:** Basic Allow/Deny List Configuration
*   **Methodology:** Unit & Integration Test Plan
*   **Methodology:** UAT Criteria
*   **Strategy:** Agent Guardrails (path restrictions)

*   **(Placeholder for further definitions of shared components, strategies, etc. emerging from group discussion)** 