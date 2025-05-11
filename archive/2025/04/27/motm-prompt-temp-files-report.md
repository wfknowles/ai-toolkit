# Report: MotM User Interface Prompt & Temporary File Strategy

**Date:** 2025-04-27
**Project:** Meeting of the Minds (MotM) Workflow MVP Enhancements
**Authors:** Prompt Engineer AI, Technical Writer AI

## 1. Introduction

Following the development of the MotM Workflow MVP, two key areas for usability improvement were identified:
1.  Providing a user-friendly way to input the initial concept without manually editing the main orchestrator prompt.
2.  Managing the persistence of intermediate auxiliary files (`_aux_files`), which primarily serve as inputs to later steps but may not be needed after the final outputs (requirements, roadmap) are generated.

This report details proposed solutions and strategies for addressing these points within the context of the existing prompt-based architecture.

## 2. User Interface Prompt (`motm_user_interface.prompt`)

### 2.1. Requirement

The current MotM MVP hardcodes the `INITIAL_CONCEPT` within the `Orchestrator.prompt`. To run the workflow on different ideas, a user must manually edit this file, which is error-prone and inconvenient. A dedicated interface prompt is needed to allow users to specify the concept easily. Ideally, this would also allow specifying an output directory, but the current architecture makes this complex.

### 2.2. Proposed Solution

A new prompt, `motm_user_interface.prompt`, is proposed to act as a configuration and initiation layer *before* the main `Orchestrator.prompt` is run.

**Functionality:**

1.  **User Input:** The prompt defines clear placeholders for the user to input their desired `USER_CONCEPT` and specify the location of the target `Orchestrator.prompt` and its directory.
2.  **Orchestrator Modification:** It instructs the AI execution environment (e.g., Cursor) to read the `Orchestrator.prompt`, programmatically replace the hardcoded `INITIAL_CONCEPT` value with the `USER_CONCEPT`, and save the modified orchestrator file using the `edit_file` tool.
3.  **State Reset:** It explicitly instructs the environment to delete the existing `state.json` and `_aux_files` directory using `run_terminal_cmd` to ensure a clean run.
4.  **Execution Trigger:** Finally, it instructs the environment to invoke the now-modified `Orchestrator.prompt`, starting the actual MotM workflow execution.

**(The full content of `motm_user_interface.prompt` should be referred to separately.)**

### 2.3. Limitations (Output Directory)

Parameterizing the output directory (currently hardcoded as `_aux_files`) presents a significant challenge with this approach. It would require:
*   Modifying the UI prompt to accept a desired output path.
*   Modifying the `Orchestrator.prompt` to potentially receive this path and store it in `shared_data`.
*   Crucially, **modifying every single Step Prompt** that writes an auxiliary file (`step-01`, `step-02`, `step-03`, etc.) to read this path from the input context and use it instead of the hardcoded relative path.

This level of modification across numerous files is complex and brittle to manage purely through prompt instructions. Therefore, the proposed UI prompt focuses *only* on parameterizing the concept for simplicity and reliability within the current MVP structure. Handling dynamic output paths would likely require a more significant refactoring, potentially favouring a hybrid code-based orchestrator approach.

## 3. Strategies for Temporary Auxiliary Files

### 3.1. Requirement

The `_aux_files` directory accumulates numerous intermediate files (pre-analyses, interview plans, individual transcripts, group transcripts) that are primarily used as inputs for subsequent steps (e.g., `analysis.md`, `requirements.md`, `roadmap.md`). Once the final, key outputs are generated and verified, these intermediate files often add clutter and may not need to be persisted long-term. A strategy is needed to clean them up automatically or semi-automatically.

### 3.2. Proposed Strategies

**Strategy 1: Post-Workflow Cleanup Prompt/Script (Recommended)**

*   **Description:** After the main `Orchestrator.prompt` completes successfully (`overall_status: "completed"`), a *separate* prompt or script is executed.
*   **Logic:**
    1.  Reads the final `state.json`.
    2.  Identifies the paths to the key final outputs (e.g., `roadmap_file_path` from `shared_data` or step results).
    3.  *(Optional but Recommended)* Prompts the user to confirm the final outputs are satisfactory.
    4.  Identifies all *other* files/directories within `_aux_files` (or specific intermediate paths recorded in `state.json`).
    5.  Uses `run_terminal_cmd` (`rm`) or multiple `delete_file` tool calls to remove the identified intermediate files/directories, leaving only the desired final outputs.
*   **Pros:**
    *   Simple to implement.
    *   Decouples cleanup logic from the main workflow, keeping the core orchestrator focused.
    *   Allows for optional user verification before deletion.
*   **Cons:**
    *   Requires an extra manual step to trigger the cleanup.
    *   Relies on successful completion of the main workflow.

**Strategy 2: Integrated Cleanup Step**

*   **Description:** Add a new final step (e.g., `step-15-cleanup.prompt`) to the `STEP_ORDER` in `Orchestrator.prompt`.
*   **Logic:**
    1.  This step runs automatically after `step-14-completion` succeeds.
    2.  It reads `state.json` to get paths of intermediate files (requires careful tracking throughout the workflow).
    3.  Uses `delete_file` tool calls to remove them.
*   **Pros:**
    *   Fully automated as part of the workflow.
*   **Cons:**
    *   Increases complexity of the main `Orchestrator.prompt` and workflow.
    *   Requires careful state management to track all intermediate files accurately.
    *   No opportunity for user verification before deletion.
    *   Cleanup won't run if the main workflow fails before reaching this step.
    *   Potential for errors during the cleanup step itself.

**Strategy 3: Dedicated Temporary Directory**

*   **Description:** Modify all Step Prompts to write intermediate files to a globally unique temporary location (e.g., `/tmp/motm_run_[UUID]/round-N/...`). Steps producing final outputs (`analysis.md`, `requirements.md`, `roadmap.md`) would explicitly copy these final files to the persistent `_aux_files` directory. A post-workflow step (or system process) could then simply delete the entire temporary directory.
*   **Pros:**
    *   Clean separation of temporary vs. persistent files.
    *   Easy cleanup (delete one temporary directory).
*   **Cons:**
    *   Requires significant refactoring of *all* Step Prompts.
    *   Adds complexity with file copying operations.
    *   Relies on the execution environment having a suitable temporary location accessible by the tools.

### 3.3. Recommendation

For the current MVP architecture, **Strategy 1 (Post-Workflow Cleanup Prompt/Script)** is recommended. It provides the desired cleanup capability with the least modification to the existing, complex workflow structure and allows for user oversight before deletion.

## 4. Conclusion

The proposed `motm_user_interface.prompt` offers a practical way to parameterize the initial concept for the MotM workflow within the current architecture's constraints. For managing auxiliary files, a separate post-workflow cleanup process is the most straightforward approach, balancing effectiveness with minimal disruption to the core workflow logic. Future iterations aiming for more dynamic output paths or fully integrated cleanup might benefit from adopting a hybrid code-based orchestration model.