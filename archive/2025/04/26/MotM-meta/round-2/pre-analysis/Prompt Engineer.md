# Prompt Engineer - R2 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:**
*   `meeting-of-the-minds-round-meta.md` (Original Concept)
*   `MotM-meta/round-1/sme-group-interview.md` (R1 Group Consensus)
*   `MotM-meta/round-1/analysis.md` (R1 Analysis Summary)

**Goal:** Define initial assets, strategies, methodologies for the MVP (Fixed chain, JSON state, Orchestrator, replicating existing MotM workflow).

**Initial Thoughts & Analysis:**

Based on the R1 consensus for a fixed-chain MVP replicating the existing workflow, the core assets we need to define from a *prompt* perspective are:

1.  **Asset: Orchestrator Meta-Prompt:**
    *   **Strategy:** Must handle the core loop: read state -> determine next fixed step -> load data -> invoke step prompt -> parse response -> validate -> update state -> loop/halt.
    *   **Methodology:** Use clear markers/instructions for state reading (specific JSON keys), step invocation (which sub-prompt to use), response parsing (expecting a JSON block), basic validation (presence of status key, value is 'success'), and state updating (writing back to specific keys). Needs explicit error handling instructions (set status='error', log message, halt).
    *   **Workflow Integration:** This is the entry point and controller.

2.  **Asset: Step-Specific Prompts (Agent Prompts):** These need to be refactored from the original monolithic MotM prompts.
    *   **Strategy:** Each prompt must perform one discrete logical step from the original workflow (e.g., "Simulate Persona X Pre-Analysis", "Facilitate Group Discussion Step Y", "Synthesize Requirements").
    *   **Methodology:**
        *   Standard Input: Define how each prompt receives necessary context (e.g., concept details, previous step outputs) via data injected by the Orchestrator (from `state.json`).
        *   Clear Task Instruction: Explicitly state the single goal of the prompt.
        *   Standard Output: Define the required JSON output block (`{ "status": "success"/"error", "output_data": {...} }`). The `output_data` structure will vary by step but needs to be predictable.
        *   Tool Usage: Specify if a step needs to read other files (beyond the state injected) or write intermediate (hidden) artifacts.
    *   **Workflow Integration:** These are the workers invoked by the Orchestrator.

3.  **Asset: `state.json` Schema Definition:**
    *   **Strategy:** Define the exact structure agreed upon in R1.
    *   **Methodology:** Create a template/example `state.json` documenting all keys (`workflow_id`, `schema_version`, `concept_input`, `current_step`, `status`, `error_message`, `data: { step1_output: {}, step2_output: {} ... }`).
    *   **Workflow Integration:** The central data exchange mechanism.

4.  **Asset: UX Interaction Prompts:** (Minor, but needed)
    *   **Strategy:** Prompts for the Orchestrator to output status updates and optional checkpoint messages.
    *   **Methodology:** Simple, templated messages (e.g., "*Status: Running [Step Name]...*", "Phase X complete. [Summary]. View details [link]? (Continue/Feedback)").
    *   **Workflow Integration:** Handles user-facing communication.

**Initial Workflow Sketch (Prompt Focus):**

```mermaid
graph TD
    A[Orchestrator: Start] --> B(Read state.json);
    B --> C{Determine Next Step};
    C --> D(Load Step Data from state.json);
    D --> E(Construct Step Prompt);
    E --> F(Invoke Step Prompt / LLM Call);
    F --> G{Parse Response JSON};
    G -- Valid & Success --> H(Update state.json);
    H --> B; # Loop
    G -- Invalid or Error --> I(Set state.json status='error');
    I --> J[Orchestrator: Halt & Report];
    C -- All Steps Done --> K[Orchestrator: Final Output];
```

**Key Task:** The immediate work is **refactoring** the logic from the existing `meeting-of-the-minds-round-1.md`, `round-2.md`, `round-3.md` prompts into discrete Step-Specific Prompts that conform to the input/output standards required by the Orchestrator and `state.json`. 