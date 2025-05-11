# Prompt Engineer - R3 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:**
*   `MotM-meta/round-2/sme-group-interview.md` (R2 Group Consensus)
*   `MotM-meta/round-2/req-analysis.md` (R2 Analysis Summary)
*   `MotM-meta/requirements.md` (MVP Requirements)

**Goal:** Define initial milestones, phases, steps for implementing the MVP prompts (Orchestrator, Step Prompts).

**Initial Thoughts & Analysis:**

From a prompt implementation perspective, the project breaks down naturally based on the core components identified in R2.

**Phase 1: Foundation & Setup (Milestone: Core Prompts Drafted)**
*   **Step 1.1:** Implement Initial Orchestrator Prompt Logic (Basic loop, step sequencing based on `MVP_WORKFLOW.md`, placeholder state read/write).
*   **Step 1.2:** Implement `step-prompt-template.md` as a physical file.
*   **Step 1.3:** Implement basic UX prompts (start message, status update template, error template, completion template).
*   **Step 1.4:** Implement first *very simple* Step Prompt (e.g., reads input from state, returns hardcoded success JSON) adhering to the template & interface contract.
*   **Step 1.5:** Test Orchestrator invoking the simple Step Prompt and updating state (conceptual E2E test 1).

**Phase 2: Step Prompt Implementation (Milestone: All MVP Step Prompts Implemented & Unit Tested)**
*   **Step 2.1:** Refactor/Implement Step Prompt for `Step 1` of `MVP_WORKFLOW.md`.
    *   Task: Implement prompt logic based on original MotM workflow.
    *   Task: Ensure adherence to template, input spec, output JSON format.
    *   Task: Implement logic for reading/writing auxiliary files if needed for this step.
    *   Task: Perform conceptual unit test (manual run with sample state).
*   **Step 2.2:** Refactor/Implement Step Prompt for `Step 2`...
*   **Step 2.n:** ...repeat for all steps in `MVP_WORKFLOW.md`.

**Phase 3: Integration & E2E Testing (Milestone: MVP Workflow Runs End-to-End Successfully)**
*   **Step 3.1:** Integrate all Step Prompts with the full Orchestrator logic.
*   **Step 3.2:** Implement Orchestrator's response parsing and validation logic.
*   **Step 3.3:** Implement Orchestrator's state update logic (overwriting `state.json`).
*   **Step 3.4:** Perform full E2E tests within Cursor using `/motm_mvp` command.
*   **Step 3.5:** Debug and refine prompts (Orchestrator & Steps) based on E2E test failures.
*   **Step 3.6:** Implement Checkpoint logic (summary generation in relevant step prompts, `continue` interaction in Orchestrator).
*   **Step 3.7:** Test Checkpoint functionality.
*   **Step 3.8:** Test Error Handling path (induce errors, verify halt & report).

**Phase 4: Finalization (Milestone: MVP Ready)**
*   **Step 4.1:** Code review (prompt review) for clarity, consistency, comments.
*   **Step 4.2:** Final validation against PO's acceptance criteria.
*   **Step 4.3:** Prepare final prompt files for "release".

**Potential Blindspots/Anti-Patterns:**
*   **Overly Complex Prompts:** Trying to put too much logic into a single Step Prompt instead of breaking it down further.
*   **Inconsistent Output:** Failing to rigorously enforce the JSON output format in *every* Step Prompt.
*   **Fragile Parsing:** Making the Orchestrator's JSON parsing logic too simplistic and easily broken by minor variations in the LLM response.
*   **Insufficient Testing:** Underestimating the effort needed for manual E2E testing and debugging. 