# MotM Chained Workflow MVP: Requirements & Definitions

**Version:** 1.0 (Derived from MotM-meta Round 2 Discussion)
**Date:** 2025-04-26

## 1. Overall MVP Goal

Implement a chained, prompt-driven workflow within Cursor AI that replicates the functionality of the existing 3-round monolithic MotM process for its original MVP concept (generating `requirements.md` and `roadmap.md`). The primary goal is to improve User Experience (UX) by eliminating mandatory user interruptions (`"Please continue"` prompts) while ensuring functional correctness and providing basic error handling.

## 2. Core Architecture Requirements

*   **REQ-ARCH-001:** The workflow MUST follow a **fixed, linear sequence** of steps, explicitly documented in `MVP_WORKFLOW.md` (Owner: PA).
*   **REQ-ARCH-002:** A single **Orchestrator Meta-Prompt** MUST manage the overall workflow execution, state transitions, step invocation, and response processing.
*   **REQ-ARCH-003:** Workflow state MUST be persisted between steps using a single **`state.json`** file.

## 3. State Management Requirements

*   **REQ-STATE-001:** The `state.json` file MUST adhere to the defined **`state.schema.json`** (Owner: Arch/AE). Key top-level fields include: `workflow_id`, `schema_version`, `concept_input`, `current_step`, `status`, `error_message`, `data`.
*   **REQ-STATE-002:** Large data outputs (e.g., text analyses, transcripts) MUST be stored in **auxiliary `.md` files**. The `state.json` file MUST only store the **relative path** to these files within the `data` object.
*   **REQ-STATE-003:** Auxiliary files MUST use the naming convention: **`[workflow_id]-[step_name]-[output_type].md`**.
*   **REQ-STATE-004:** The Orchestrator MUST generate a unique `workflow_id` at the start of each run.
*   **REQ-STATE-005:** Updates to `state.json` by the Orchestrator SHOULD **overwrite the entire file** with the complete, updated JSON content to minimize partial write risks (using `edit_file`).
*   **REQ-STATE-006:** The `state.json` file MUST contain sufficient information for debugging (e.g., `current_step`, `status`, `error_message`, paths to outputs).

## 4. Step Prompt (Agent) Requirements

*   **REQ-STEP-001:** Each logical step from the documented `MVP_WORKFLOW.md` MUST be implemented as a separate **Step Prompt** file.
*   **REQ-STEP-002:** All Step Prompts MUST adhere to the standard **`step-prompt-template.md`** structure (Owner: PE), including sections for Role/Goal, Input Data, Task Instructions, Tool Usage, and Output Format.
*   **REQ-STEP-003:** Step Prompts MUST expect their input data (including paths to needed auxiliary files) to be injected by the Orchestrator based on `state.json`.
*   **REQ-STEP-004:** Step Prompts MUST output their results **within the chat response** formatted as a single **JSON code block** (` ```json ... ``` `).
*   **REQ-STEP-005:** The output JSON block MUST contain a `status` key (`"success"` or `"error"`) and an `output_data` object, as defined in `INTERFACE_CONTRACT.md` (Owner: Arch/AE).
*   **REQ-STEP-006:** If a Step Prompt generates an auxiliary file, it MUST save it using the standard naming convention and include the **relative path** to the file in its `output_data`.
*   **REQ-STEP-007:** Step Prompts MUST be designed to be as modular and self-contained as possible.

## 5. Orchestrator Prompt Requirements

*   **REQ-ORCH-001:** MUST read `state.json` at the beginning of each processing cycle.
*   **REQ-ORCH-002:** MUST determine the next step based on `state.current_step` and the fixed sequence in `MVP_WORKFLOW.md`.
*   **REQ-ORCH-003:** MUST construct the prompt for the next step, injecting required data/paths from `state.json`.
*   **REQ-ORCH-004:** MUST invoke the Step Prompt (LLM call).
*   **REQ-ORCH-005:** MUST parse the Step Prompt's response to find and extract the expected JSON output block.
*   **REQ-ORCH-006:** MUST validate the parsed JSON (is valid JSON? does `status` key exist?).
*   **REQ-ORCH-007:** If validation passes and `status` is `"success"`, MUST update its internal representation of the state with the `output_data` and advance `current_step`.
*   **REQ-ORCH-008:** MUST generate the complete, updated JSON content for the state.
*   **REQ-ORCH-009:** MUST use `edit_file` to overwrite `state.json` with the complete updated content.
*   **REQ-ORCH-010:** If validation fails or `status` is `"error"`, MUST set `state.status` to `"error"`, record details in `state.error_message`, save the error state to `state.json`, halt execution, and report the error to the user (See REQ-UX-004).
*   **REQ-ORCH-011:** MUST handle the final step completion by setting `state.status` to `"completed"` and presenting final artifacts (See REQ-UX-005).

## 6. User Experience (UX) Requirements

*   **REQ-UX-001:** The workflow MUST be initiated by a single user command/prompt (e.g., `/motm_mvp`).
*   **REQ-UX-002:** The workflow MUST run automatically between steps **without requiring mandatory user continuation prompts**.
*   **REQ-UX-003:** Brief, consistent **status update messages** MUST be displayed in the chat during execution (e.g., "*Status: Running step [Step Name]...*"). Use templates defined by UXE.
*   **REQ-UX-004:** Upon halting due to an error, a **clear, user-friendly error message** MUST be displayed, indicating the step of failure and that the process stopped. Use templates defined by UXE.
*   **REQ-UX-005:** Upon successful completion, a **confirmation message** MUST be displayed, including **links** to the final generated artifacts (`requirements.md`, `roadmap.md` for the MVP concept).
*   **REQ-UX-006:** **Optional checkpoints** MUST be presented after the R1 analysis simulation step and the R1 group discussion simulation step.
*   **REQ-UX-007:** Checkpoint messages MUST include a **concise summary** of the completed phase and a **link** to view detailed artifact(s).
*   **REQ-UX-008:** Checkpoint messages MUST explicitly prompt the user to reply **`continue`** to proceed. The Orchestrator MUST wait for this reply before invoking the next step.

## 7. Acceptance Criteria (High-Level Summary - See `MVP_ACCEPTANCE.md` for detail)

*   MVP workflow completes end-to-end successfully for the predefined concept.
*   All REQ-UX requirements related to automation, status, checkpoints, and final output delivery are met.
*   Generated `requirements.md` and `roadmap.md` content is correct and complete for the predefined MVP concept.
*   Introduced errors lead to graceful halt and correct error reporting per REQ-ORCH-010 and REQ-UX-004.

## 8. Guidelines & Non-Functional Requirements

*   **GUIDE-001:** Emphasize **modularity** in Step Prompt design.
*   **GUIDE-002:** Use **clear, consistent naming conventions** for prompts, state keys, and auxiliary files.
*   **GUIDE-003:** Include **comments** within prompts explaining complex logic.
*   **GUIDE-004:** Prioritize **simplicity** in prompt logic and state structures for the MVP.
*   **NFR-001:** The system MUST operate entirely within the Cursor AI environment using available tools.
*   **NFR-002:** The system MUST be testable via manual E2E runs and conceptual unit/integration checks. 