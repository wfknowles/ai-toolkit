# Usage Report: MotM Workflow MVP

**Date:** 2025-04-26

**Project:** Meeting of the Minds (MotM) Workflow MVP

## 1. Overview

This report details how the currently built MotM Workflow MVP architecture is intended to be used, specifically addressing how to provide input concepts and where output is generated.

## 2. Current Setup Analysis

The workflow is designed to be executed by invoking the main orchestrator prompt file: `brain/workflows/orchestrators/MotM/Orchestrator.prompt` within a suitable execution environment (e.g., Cursor) that provides the necessary helper functions (file I/O, prompt invocation, time/UUID generation, potential user interaction).

Key aspects of the current setup:

*   **Orchestration:** The logic defined within `Orchestrator.prompt` controls the workflow execution.
*   **State Management:** Workflow state is maintained in `brain/workflows/orchestrators/MotM/state.json`.
*   **Steps:** Individual steps are defined in `step-*.prompt` files within the same directory.
*   **Auxiliary Outputs:** All intermediate and final file outputs (transcripts, analyses, requirements, roadmap) are stored within the `brain/workflows/orchestrators/MotM/_aux_files/` directory, organized by round.

## 3. Providing Input Concepts

*   **Current Implementation:** In the current MVP (`Orchestrator.prompt`, Phase: Initialization, Step 1), the `INITIAL_CONCEPT` is **hardcoded**:
    ```
    INITIAL_CONCEPT = "Analyze the feasibility of building a local AI agent for reliable file editing."
    ```
    When the orchestrator initializes a new state (if `state.json` doesn't exist or is invalid), it uses this hardcoded string.
*   **How to Change:** To run the workflow with a *different* concept, you currently need to **manually edit** the `Orchestrator.prompt` file and change the value assigned to the `INITIAL_CONCEPT` variable before starting the execution.

## 4. Specifying Output Directory

*   **Current Implementation:** The root directory for auxiliary file outputs (`_aux_files/`) is **hardcoded** relative to the location of the orchestrator and step prompts. Steps construct their output paths based on this assumption (e.g., `_aux_files/round-1/analysis.md`). This is defined implicitly by the step prompts and formalized in `AUXILIARY_FILES.md`.
*   **How to Change:** There is currently **no mechanism** to specify a different output directory dynamically. Changing the output location would require modifying:
    1.  Each Step Prompt (`step-*.prompt`) that writes an auxiliary file to use a different base path.
    2.  The `Orchestrator.prompt` if it needed to pass a dynamic output path to the steps.
    3.  The `AUXILIARY_FILES.md` documentation to reflect the new structure.

## 5. How to Run

1.  **(Optional) Modify Concept:** Edit the `INITIAL_CONCEPT` variable within `Orchestrator.prompt` if you want to use a different input concept.
2.  **Ensure Clean State:** Make sure `state.json` and the `_aux_files` directory do not exist in the `brain/workflows/orchestrators/MotM/` directory (the `rm` commands from Task 7.3.2 achieve this).
3.  **Invoke Orchestrator:** Execute the `Orchestrator.prompt` in the target environment (e.g., within Cursor). The prompt contains detailed instructions for the AI driving the execution.
4.  **Interact if Needed:** If the workflow pauses at a checkpoint (like after Step 7), provide the input `continue` when prompted.
5.  **Monitor Output:** Observe the `[Orchestrator]` messages for step progress and final status.
6.  **Review Results:** Upon completion (or error), check the final `state.json` and the generated files within the `_aux_files` directory.

## 6. Recommendations for Future Use

For more flexible use:

*   **Parameterize `INITIAL_CONCEPT`:** Modify the `Orchestrator.prompt` to accept the initial concept as an input parameter from the execution environment instead of being hardcoded.
*   **Parameterize Output Directory:** Similarly, modify the orchestrator and step prompts to accept a base output directory path as an input parameter, allowing users to specify where `_aux_files` (or a differently named directory) should be created. 