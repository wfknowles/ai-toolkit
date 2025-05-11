# Senior Software Engineer - R2 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:** R1 Group Consensus, R1 Analysis Summary.

**Goal:** Define assets, strategies, methodologies for the MVP implementation.

**Initial Thoughts & Analysis:**

From an engineering implementation standpoint, focusing on the agreed MVP:

1.  **Asset: `state.json` File & Schema:**
    *   **Strategy:** Implement the defined JSON schema. Crucially, decide on handling large data blobs.
    *   **Methodology:** Agree with Arch: Use pointers (paths) in `state.json` for large text outputs (e.g., transcripts, analyses) stored in separate `.md` files within the round directory. This keeps `state.json` concise and performant for reads/updates. Define a clear naming convention for these auxiliary files (e.g., `step-<step_name>-output.md`). Ensure the `edit_file` instructions for updating `state.json` are precise to avoid accidental corruption (e.g., target specific keys).

2.  **Asset: Step Prompt Implementation:**
    *   **Strategy:** Refactor existing MotM logic into discrete, testable units.
    *   **Methodology:** Each step prompt needs:
        *   Input section clearly defining expected data keys (read from `state.json` data passed by Orchestrator).
        *   Task section defining the single operation.
        *   Output section defining the JSON structure (`status`, `output_data`) to be returned *in the chat response*.
        *   Instructions for reading/writing auxiliary files if needed, using predictable paths relative to the current round directory.
        *   *Crucially:* Emphasize error reporting within the output JSON's `status` field if the step itself detects an issue.

3.  **Asset: Orchestrator Prompt Implementation:**
    *   **Strategy:** Build the state machine logic.
    *   **Methodology:** Implement the loop: read `state.json`, check `status`, determine next step from the *fixed* sequence, prepare input data (including paths to auxiliary files if needed), invoke step prompt, *robustly parse* the expected JSON block from the response, validate `status`, update `state.json` (including any new auxiliary file paths), write `state.json`. Include the basic error handling (halt on parse failure or `error` status).

4.  **Methodology: Robust `edit_file` Usage:**
    *   **Strategy:** Minimize risk of file corruption during state updates.
    *   **Methodology:** When updating `state.json`, the prompt instructing `edit_file` should ideally provide the *entire* new JSON content to overwrite the file, rather than attempting complex partial edits. This is simpler and less prone to errors if the LLM can reliably generate the full, correct updated state. Read the *current* state first, update the necessary fields in the LLM's internal representation, then generate the *full* new JSON for the `edit_file` command.

5.  **Strategy: Debugging Aids:**
    *   **Methodology:** Ensure `state.json` includes timestamps for step completion or a log array. Store the generated (but hidden) intermediate artifacts with clear names. This provides essential trace information if the chain fails.

**Key Task:** Ensuring the prompt logic for both the Orchestrator and Step Prompts correctly and reliably interacts with the `state.json` file and any auxiliary files via the available tools, particularly the `edit_file` tool. 