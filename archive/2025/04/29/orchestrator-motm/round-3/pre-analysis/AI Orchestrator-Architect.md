# AI Orchestrator/Architect - Round 3 Pre-Analysis (Orchestrator Framework)

**Based on:** Framework Requirements (`requirements.md`)

**Initial Milestones/Phases/Steps for MVP Framework:**
*   **Phase: Design & Setup**
    *   Milestone: Finalize API Contracts
        *   Step: Formalize Orchestrator <-> Exec Env API (message queue format) (REQ-ORC-003, REQ-ORC-008).
        *   Step: Formalize Orchestrator <-> UI API (trigger/response) (REQ-ORC-006, REQ-ORC-007).
    *   Milestone: Setup State Management
        *   Step: Choose & setup DB/Cache for pending edits (GUIDE-ORC-001).
        *   Step: Implement schema (REQ-ORC-005).
*   **Phase: Orchestrator Implementation**
    *   Milestone: Implement Core Logic
        *   Step: Implement AI model interaction (prompt+schema -> request) (REQ-ORC-001, REQ-ORC-002).
        *   Step: Implement `read_file` flow (trigger Exec Env, relay result) (REQ-ORC-003, REQ-ORC-010, REQ-ORC-011).
    *   Milestone: Implement Confirmation Workflow
        *   Step: Implement state storage/retrieval (REQ-ORC-005).
        *   Step: Implement UI trigger logic (REQ-ORC-006).
        *   Step: Implement UI response handling (approve/reject/timeout) (REQ-ORC-007, REQ-ORC-009, REQ-ORC-012).
        *   Step: Implement Exec Env trigger on approval (REQ-ORC-008).
        *   Step: Implement result relay to model (incl. rejection) (REQ-ORC-011).
*   **Phase: Integration Testing**
    *   Milestone: Test Orchestrator Flows
        *   Step: Write tests for `read_file` end-to-end flow.
        *   Step: Write tests for `edit_file` confirmation flow (happy path, rejection, timeout). 