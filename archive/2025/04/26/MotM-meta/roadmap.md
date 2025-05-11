# MotM Chained Workflow MVP: Roadmap & Backlog

**Version:** 1.0 (Derived from MotM-meta Round 3 Discussion)
**Date:** 2025-04-26

## 1. Project Goal Recap

Implement an MVP of the chained MotM workflow, replicating the existing MotM process for its original concept, focusing on UX improvement (automation) and basic robustness within Cursor AI.

## 2. High-Level Phases & Milestones

*   **Phase 1: Design Finalization & Documentation**
    *   *Milestone:* Implementation Blueprint Ready
*   **Phase 2: Core Framework Implementation**
    *   *Milestone:* Basic Orchestration Loop Functional
*   **Phase 3: Step Prompt Implementation**
    *   *Milestone:* All MVP Step Prompts Implemented & Unit Tested
*   **Phase 4: Integration, Testing & Refinement**
    *   *Milestone:* MVP Functionally Complete & Stable
*   **Phase 5: Release Preparation**
    *   *Milestone:* MVP Ready for Use

## 3. Initial Product Backlog (User Stories & Tasks)

*(Note: Estimates/Owners TBD. Context links point to conceptual documents defined in R2/R3)*

--- 

**EPIC: FOUNDATION & DOCUMENTATION (Phase 1)**

*   **Story 1:** Define State Management Foundation
    *   *Goal:* Establish the structure and rules for state persistence.
    *   **Task 1.1:** Finalize and commit `state.schema.json`. (Owner: Arch/AE)
        *   *Context:* R2 discussion, `req-analysis.md` Sec 3.
    *   **Task 1.2:** Document auxiliary file strategy & naming convention in `TECHNICAL_DESIGN.md`. (Owner: PA/Arch)
        *   *Context:* R2 discussion, `requirements.md` REQ-STATE-002, REQ-STATE-003.

*   **Story 2:** Define Step Interfaces
    *   *Goal:* Ensure clear contracts between Orchestrator and Steps.
    *   **Task 2.1:** Draft and commit `INTERFACE_CONTRACT.md`, defining I/O JSON & aux files for each step in `MVP_WORKFLOW.md`. (Owner: Arch/AE)
        *   *Context:* R2/R3 discussion, `requirements.md` REQ-STEP-005.
    *   **Task 2.2:** Create and commit `step-prompt-template.md`. (Owner: PE)
        *   *Context:* R2/R3 discussion, `requirements.md` REQ-STEP-002.

*   **Story 3:** Define MVP Workflow Sequence
    *   *Goal:* Provide a clear blueprint of the steps to implement.
    *   **Task 3.1:** Analyze original MotM prompts & R1/R2 outputs to define the linear step sequence.
    *   **Task 3.2:** Create and commit `MVP_WORKFLOW.md` (list/diagram). (Owner: PA)
        *   *Context:* R2/R3 discussion, `requirements.md` REQ-ARCH-001.

*   **Story 4:** Define Project Parameters
    *   *Goal:* Align on execution plan and success criteria.
    *   **Task 4.1:** Create and commit `TECHNICAL_DESIGN.md` consolidating all decisions. (Owner: PA)
    *   **Task 4.2:** Create and commit `MVP_ACCEPTANCE.md` with detailed testable criteria. (Owner: PO)
    *   **Task 4.3:** Create `PROJECT_PLAN.md` with WBS, task list, roles, check-in plan. (Owner: PM)

*   **Story 5:** Define Core Prompting Utilities
    *   *Goal:* Establish reliable low-level prompt instructions.
    *   **Task 5.1:** Develop & document standard prompt instruction patterns for JSON read/write, file I/O, aux path construction. (Owner: SSE/PE/AE)
        *   *Context:* R3 SSE Interview. *Example (Conceptual)*: "Instruction Pattern for State Overwrite: Read current state -> Modify internal representation -> Generate COMPLETE new state JSON -> Instruct `edit_file` to OVERWRITE `state.json` with this content."

--- 

**EPIC: CORE FRAMEWORK IMPLEMENTATION (Phase 2)**

*   **Story 6:** Implement Orchestrator Core Logic
    *   *Goal:* Build the basic engine that drives the workflow.
    *   **Task 6.1:** Implement Orchestrator: State read/write logic (using common pattern). (Owner: AE/PE)
        *   *Context:* `Orchestrator.prompt`, `state.json`, `requirements.md` REQ-ORCH-001, 009.
    *   **Task 6.2:** Implement Orchestrator: Fixed step sequencing based on `MVP_WORKFLOW.md`. (Owner: AE/PE)
        *   *Context:* `Orchestrator.prompt`, `MVP_WORKFLOW.md`, REQ-ORCH-002.
    *   **Task 6.3:** Implement Orchestrator: Basic invocation of Step Prompts. (Owner: AE/PE)
    *   **Task 6.4:** Implement Orchestrator: Basic response parsing shell (find JSON block). (Owner: AE/PE)
        *   *Context:* R3 AE Interview logic. REQ-ORCH-005.
    *   **Task 6.5:** Test basic loop with 1-2 dummy Step Prompts.

--- 

**EPIC: STEP PROMPT IMPLEMENTATION (Phase 3)**

*   **Story 7:** Implement Step Prompt: [Step 1 Name from `MVP_WORKFLOW.md`]
    *   *Goal:* Implement the logic for the first step in the chain.
    *   **Task 7.1:** Draft prompt using template, implementing logic based on original MotM & contract. (Owner: TBD - PE/SSE/AE)
        *   *Context:* `step-1.prompt`, `step-prompt-template.md`, `INTERFACE_CONTRACT.md`, `MVP_WORKFLOW.md`.
    *   **Task 7.2:** Implement necessary auxiliary file reads/writes (using common patterns & naming convention). (Owner: TBD)
    *   **Task 7.3:** Implement correct output JSON generation (`status`, `output_data`). (Owner: TBD)
        *   *Context:* `INTERFACE_CONTRACT.md`, REQ-STEP-004, 005, 006.
    *   **Task 7.4:** Perform manual unit test.

*   **(Stories 8...N for remaining Step Prompts in `MVP_WORKFLOW.md`)**

--- 

**EPIC: INTEGRATION, TESTING & UX FEATURES (Phase 4)**

*   **Story N+1:** Implement Orchestrator Validation & State Updates
    *   *Goal:* Make the Orchestrator robustly handle Step responses.
    *   **Task N+1.1:** Implement Orchestrator: Full JSON response parsing & validation logic. (Owner: AE/PE)
        *   *Context:* R3 AE Interview logic, REQ-ORCH-006.
    *   **Task N+1.2:** Implement Orchestrator: Logic to update state based on `output_data`, including auxiliary file paths. (Owner: AE/PE)
        *   *Context:* REQ-ORCH-007.

*   **Story N+2:** Implement Error Handling
    *   *Goal:* Ensure graceful failure.
    *   **Task N+2.1:** Implement Orchestrator: Logic to detect/handle errors (parse failure, `status: "error"`). (Owner: AE/PE)
    *   **Task N+2.2:** Implement Orchestrator: Set state to `error` and halt. (Owner: AE/PE)
        *   *Context:* REQ-ORCH-010.
    *   **Task N+2.3:** Integrate Orchestrator with error message UX template. (Owner: AE/PE + UXE)
        *   *Context:* REQ-UX-004.

*   **Story N+3:** Implement UX Status Updates
    *   *Goal:* Provide user visibility.
    *   **Task N+3.1:** Integrate status update UX templates into Orchestrator loop. (Owner: AE/PE + UXE)
        *   *Context:* REQ-UX-003.

*   **Story N+4:** Implement UX Checkpoints
    *   *Goal:* Allow optional user review.
    *   **Task N+4.1:** Implement checkpoint logic in relevant Step Prompts (summary generation). (Owner: PE/SSE)
    *   **Task N+4.2:** Implement checkpoint logic in Orchestrator (detect step, show message, wait for 'continue'). (Owner: AE/PE + UXE)
        *   *Context:* REQ-UX-006, 007, 008.

*   **Story N+5:** Perform End-to-End Testing
    *   *Goal:* Validate the full integrated workflow.
    *   **Task N+5.1:** Define E2E test scenarios based on `MVP_ACCEPTANCE.md`. (Owner: PO/UXE)
    *   **Task N+5.2:** Execute E2E tests manually in Cursor. (Owner: Team)
    *   **Task N+5.3:** Log results and bugs (`TESTING_RESULTS.md`). (Owner: Team)
    *   **Task N+5.4:** Debug and refine prompts based on test results (Iterative). (Owner: PE/AE/SSE)

--- 

**EPIC: RELEASE PREPARATION (Phase 5)**

*   **Story N+6:** Final Validation & Review
    *   *Goal:* Ensure MVP meets quality standards and DoD.
    *   **Task N+6.1:** Perform final acceptance testing against `MVP_ACCEPTANCE.md` (esp. output artifact quality). (Owner: PO)
    *   **Task N+6.2:** Perform final prompt reviews (architectural, code style). (Owner: PA/Team)
    *   **Task N+6.3:** Update all documentation (`TECHNICAL_DESIGN.md`, etc.) to reflect final state. (Owner: Assigned Doc Owners)

*   **Story N+7:** Prepare Release
    *   *Goal:* Make the MVP usable.
    *   **Task N+7.1:** Finalize user documentation. (Owner: PO/UXE)
    *   **Task N+7.2:** Package/organize final prompt files. 