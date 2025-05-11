# Master Requirements List: AI Tool Integration Framework (MVP)

**Date:** 2024-07-23
**Source:** MotM Rounds 1 & 2 (Orchestrator)

This document outlines the requirements, acceptance criteria, and guidelines for the Minimum Viable Product (MVP) of the AI Tool Integration Framework for `read_file` and `edit_file` tools.

---

## 1. Orchestrator Component (MVP)

*   **Definition:** Central logic managing AI model interaction, tool calls, and the `edit_file` confirmation workflow.
*   **Asset(s):**
    *   Orchestrator Service Codebase
    *   State Management Schema (for pending edits)
    *   API Contract (Orchestrator <-> Exec Env)
    *   API Contract (Orchestrator <-> UI Layer)
*   **Requirements:**
    *   REQ-ORC-001: Must receive user prompts and forward them to the AI Model with appropriate Tool Definitions.
    *   REQ-ORC-002: Must parse AI Model responses to detect tool call requests (`read_file`, `edit_file`).
    *   REQ-ORC-003: For `read_file` requests, must validate parameters and trigger Execution Env via defined API.
    *   REQ-ORC-004: For `edit_file` requests, must validate parameters and initiate the User Confirmation Workflow instead of directly calling Execution Env.
    *   REQ-ORC-005: User Confirmation Workflow: Must store pending edit details (request ID, path, content, user, timestamp) using defined State Management Schema.
    *   REQ-ORC-006: User Confirmation Workflow: Must trigger the UI Layer via defined API to display confirmation prompt, passing necessary details (request ID, path, content/diff).
    *   REQ-ORC-007: User Confirmation Workflow: Must receive Approve/Reject response from UI Layer via defined API, correlating via request ID.
    *   REQ-ORC-008: User Confirmation Workflow: If approved, must trigger Execution Env via defined API to execute the `edit_file_tool` function with approved content.
    *   REQ-ORC-009: User Confirmation Workflow: If rejected or timed out, must NOT trigger Execution Env.
    *   REQ-ORC-010: Must receive results (success/failure/content/error code) from Execution Env.
    *   REQ-ORC-011: Must forward tool execution results (or rejection status like `USER_REJECTED_EDIT`) back to the AI Model.
    *   REQ-ORC-012: Must handle timeouts for pending confirmations.
*   **Acceptance Criteria:**
    *   AC-ORC-001: `read_file` request from AI triggers correct call to Execution Env.
    *   AC-ORC-002: `edit_file` request from AI triggers call to UI Layer for confirmation.
    *   AC-ORC-003: User rejection via UI results in notification to AI Model, no call to Execution Env.
    *   AC-ORC-004: User approval via UI results in correct call to Execution Env with approved content.
    *   AC-ORC-005: Execution Env results (success/error) are correctly relayed to AI Model.
*   **Guidelines:**
    *   GUIDE-ORC-001: State management for confirmations should be resilient (DB/Cache preferred over in-memory).
    *   GUIDE-ORC-002: Communication with Execution Env should be decoupled (Queue preferred).

---

## 2. Execution Environment (MVP)

*   **Definition:** Secure, sandboxed environment for running `file_io.py` functions.
*   **Asset(s):**
    *   Execution Environment Service Codebase / Build Spec (e.g., Dockerfile)
    *   Configuration Schema (for allow-lists)
    *   Deployed `file_io.py` script
*   **Requirements:**
    *   REQ-EXE-001: Must listen for requests from Orchestrator (e.g., via queue or API endpoint).
    *   REQ-EXE-002: Must securely load and parse allow-list configuration.
    *   REQ-EXE-003: Must invoke the correct function (`read_file_tool` or `edit_file_tool`) from `file_io.py` based on request.
    *   REQ-EXE-004: Must perform robust input sanitization on `file_path` and `approved_content` before passing to `file_io.py` functions (defense in depth).
    *   REQ-EXE-005: Must capture return values (`success`, `content`, `error`) from `file_io.py`.
    *   REQ-EXE-006: Must return results to Orchestrator via defined API/protocol, including standardized error codes.
    *   REQ-EXE-007: (If Diff Generation here) Must be able to read current file content (respecting READ_ALLOW_LIST) and generate a diff on edit proposals.
*   **Acceptance Criteria:**
    *   AC-EXE-001: Receives `read_file` request, calls `read_file_tool`, returns correct result/error.
    *   AC-EXE-002: Receives `edit_file` request (post-confirmation), calls `edit_file_tool`, returns correct result/error.
    *   AC-EXE-003: Correctly denies requests based on loaded allow-lists.
    *   AC-EXE-004: Logs execution details securely.
*   **Guidelines:**
    *   GUIDE-EXE-001: Environment must be strongly sandboxed (minimal privileges, network restrictions).
    *   GUIDE-EXE-002: Configuration injection must be secure.

---

## 3. Tool Definitions (MVP)

*   **Definition:** Structured descriptions (JSON Schema) for AI Model consumption.
*   **Asset(s):** `read_file.json`, `edit_file.json` (Schema files)
*   **Requirements:**
    *   REQ-DEF-001: Must accurately describe tool purpose, parameters (name, type, required, description), and return values.
    *   REQ-DEF-002: `edit_file` description must explicitly state the mandatory user confirmation workflow initiated by calling the tool.
*   **Acceptance Criteria:**
    *   AC-DEF-001: Schema validates correctly.
    *   AC-DEF-002: Model can successfully parse schemas and generate valid tool call requests.

---

## 4. UI Layer Component (MVP - Confirmation Flow)

*   **Definition:** Component responsible for rendering the edit confirmation prompt.
*   **Asset(s):**
    *   Confirmation UI Codebase Component
    *   Wireframes/Mockups
*   **Requirements:**
    *   REQ-UI-001: Must receive confirmation trigger from Orchestrator via defined API.
    *   REQ-UI-002: Must display file path and content diff (with option for full content) clearly.
    *   REQ-UI-003: Must present clear Approve/Reject actions.
    *   REQ-UI-004: Must send user decision (Approve/Reject) back to Orchestrator via defined API, correlating via request ID.
*   **Acceptance Criteria:**
    *   AC-UI-001: Correct information is displayed on confirmation trigger.
    *   AC-UI-002: User Approve action sends "Approved" status to Orchestrator.
    *   AC-UI-003: User Reject action sends "Rejected" status to Orchestrator.
*   **Guidelines:**
    *   GUIDE-UI-001: Design should minimize friction while ensuring clarity.
    *   GUIDE-UI-002: Provide appropriate feedback during/after action.

---

## 5. Configuration Management (MVP)

*   **Definition:** Process and mechanism for managing allow-lists.
*   **Asset(s):**
    *   Allow-list configuration files (e.g., `allow_list.yaml`)
    *   Secrets Management tooling/process
*   **Requirements:**
    *   REQ-CFG-001: Must provide a secure way to store allow-list definitions.
    *   REQ-CFG-002: Must provide a secure mechanism to deploy/inject configuration into the Execution Environment at runtime/startup.
*   **Acceptance Criteria:**
    *   AC-CFG-001: Execution Environment successfully loads the correct allow-lists on startup.
*   **Guidelines:**
    *   GUIDE-CFG-001: Use infrastructure secrets management where possible.
    *   GUIDE-CFG-002: Implement change control and auditing for allow-list modifications. 