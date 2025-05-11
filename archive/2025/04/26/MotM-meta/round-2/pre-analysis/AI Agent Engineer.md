# AI Agent Engineer - R2 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:** R1 Group Consensus, R1 Analysis Summary.

**Goal:** Define assets, strategies, methodologies for the MVP pseudo-agent implementation.

**Initial Thoughts & Analysis:**

Focusing on the implementation details of the Orchestrator and Step Prompts (Agents) based on R1 decisions:

1.  **Asset: Step Prompt Template:**
    *   **Strategy:** Create a standard structure for all Step Prompts.
    *   **Methodology:** Define a template (`step-prompt-template.md`) that includes sections for:
        *   `## Role & Goal`: (e.g., "Simulate PE analysis of the concept")
        *   `## Input Data`: (Description of expected keys from `state.json`, e.g., `state.concept_input`, `state.data.previous_step_output_path`)
        *   `## Task Instructions`: (Detailed steps for the LLM)
        *   `## Tool Usage`: (Instructions for reading/writing auxiliary files, e.g., "Read the file at path X. Write your analysis to a new file Y and include path Y in your output JSON.")
        *   `## Output Format`: (Explicit instructions to generate the JSON block: `{ "status": "success"/"error", "output_data": { ... } }` including specification of `output_data` keys for this step).

2.  **Asset: Orchestrator Prompt Detailed Logic:**
    *   **Strategy:** Flesh out the control loop logic.
    *   **Methodology:** Write the core instructions for the Orchestrator prompt, including:
        *   Reading `state.json` via `read_file`.
        *   Identifying the next step based on `state.current_step` using a predefined sequence map (e.g., `step1 -> step2 -> ...`).
        *   Extracting required input data/paths from the parsed `state.json`.
        *   Constructing the actual prompt text for the identified Step Prompt using the template and injecting the input data.
        *   Executing the Step Prompt (LLM call).
        *   Parsing the response string to find and extract the JSON output block.
        *   Validating the JSON (`status` key check).
        *   Updating the internal representation of the state JSON.
        *   Generating the full, updated JSON content.
        *   Calling `edit_file` to overwrite `state.json` with the new content.
        *   Handling the halt condition on error or completion.

3.  **Strategy: Handling Auxiliary Files:**
    *   **Methodology:** Define the process clearly:
        *   Step Prompt needing to write large output: Generates content, calls `edit_file` to save it to a unique, predictable path (e.g., `round-2/step-X-output.md`), includes this *path* in its `output_data` JSON.
        *   Orchestrator: Saves this path to `state.json`.
        *   Subsequent Step Prompt needing this data: Orchestrator provides the *path* from `state.json` in the input. Step Prompt uses `read_file` with the provided path.

4.  **Methodology: Prompt Modularity:**
    *   **Strategy:** Ensure prompts can be developed and potentially tested independently.
    *   **Methodology:** Keep Orchestrator logic separate from Step Prompt logic. Use the standardized interface (JSON input/output) as the connection point. Avoid complex dependencies where one Step Prompt directly calls another.

**Key Task:** Defining the standard template for Step Prompts and detailing the precise operational logic within the Orchestrator prompt for handling state, invoking steps, parsing results, and managing auxiliary files. 