# AI Orchestrator/Architect - R3 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:** R2 Group Consensus, R2 Analysis Summary, MVP Requirements.

**Goal:** Define initial milestones, phases, steps for implementing the MVP architecture (Orchestration, State).

**Initial Thoughts & Analysis:**

Focusing on the architectural build-out based on R2 requirements.

**Phase 1: Core Infrastructure Setup (Milestone: Basic Orchestration Loop Functional)**
*   **Step 1.1:** Define & Create `state.schema.json` file.
*   **Step 1.2:** Define & Create `INTERFACE_CONTRACT.md` document (outline).
*   **Step 1.3:** Implement Orchestrator Prompt: Initial version handling only state read, determining first step, invoking a dummy step, basic overwrite of `state.json`.
*   **Step 1.4:** Define `workflow_id` generation logic (e.g., timestamp-based).
*   **Step 1.5:** Test basic state initialization and persistence across one dummy step.

**Phase 2: Orchestration Logic Implementation (Milestone: Orchestrator Handles Full Sequence & Basic Validation)**
*   **Step 2.1:** Implement fixed sequence logic in Orchestrator based on `MVP_WORKFLOW.md` (PA asset).
*   **Step 2.2:** Implement Orchestrator logic for injecting correct input data/paths into Step Prompts based on `INTERFACE_CONTRACT.md`.
*   **Step 2.3:** Implement Orchestrator logic for parsing the expected JSON block from Step Prompt responses.
*   **Step 2.4:** Implement Orchestrator logic for basic validation (`status` key check).
*   **Step 2.5:** Implement Orchestrator logic for updating `state.json` based on `output_data` (handle adding paths for auxiliary files).
*   **Step 2.6:** Test Orchestrator sequencing and data passing using dummy/simple Step Prompts.

**Phase 3: Error Handling & UX Integration (Milestone: Orchestrator Handles Errors & Checkpoints)**
*   **Step 3.1:** Implement Orchestrator logic for error handling path (detecting non-'success' status or parse failures, setting `state.status`='error', halting).
*   **Step 3.2:** Integrate Orchestrator with UX templates for status updates.
*   **Step 3.3:** Implement Orchestrator logic for checkpoints: identifying checkpoint steps, triggering the checkpoint message (using UX template), waiting for 'continue' reply.
*   **Step 3.4:** Integrate Orchestrator with UX template for error reporting.
*   **Step 3.5:** Test error paths and checkpoint interactions.

**Phase 4: Integration & System Testing (Milestone: Stable MVP Architecture)**
*   **Step 4.1:** Integrate the fully implemented Orchestrator with the fully implemented Step Prompts (from PE/AE/SSE workstream).
*   **Step 4.2:** Perform E2E testing focusing on architectural integrity (state consistency, correct sequencing, data flow, error handling).
*   **Step 4.3:** Performance testing (manual timing) of full workflow runs.
*   **Step 4.4:** Refine Orchestrator prompt based on testing results.

**Potential Blindspots/Anti-Patterns:**
*   **Tight Coupling:** Orchestrator logic becoming too dependent on the specific internal workings of Step Prompts, rather than relying solely on the interface contract.
*   **State Bloat:** Allowing `state.json` itself to become too large if the auxiliary file strategy isn't strictly enforced by Step Prompts.
*   **Inadequate Validation:** The Orchestrator's validation of the Step Prompt response being too weak, allowing bad data into the state.
*   **Race Conditions (Conceptual):** While unlikely in serial chat, ensuring prompts don't generate instructions leading to unintended parallel tool calls if the environment ever changed. 