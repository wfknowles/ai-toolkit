# Project Roadmap & User Stories: Custom File I/O Tools (MVP)

**Date:** 2024-07-23
**Source:** MotM Rounds 1, 2 & 3

This document outlines the project plan (phases, milestones, steps) and associated user stories/tasks for the MVP.

---

## Phase 1: Planning & Design

*   **Milestone 1.1:** Finalize API & Schemas
    *   *Step 1.1.1:* Define `/readFile` request/response schema (Orchestrator)
    *   *Step 1.1.2:* Define `/editFile` request/response schema (Orchestrator)
    *   *Step 1.1.3:* Define User Confirmation interaction schema (Orchestrator)
    *   *Step 1.1.4:* Define Logging Schemas (REQ-RF-005, REQ-EF-007) (Orchestrator)
    *   *Step 1.1.5:* Architectural Review of API/Schemas (Principal Architect)
*   **Milestone 1.2:** Finalize Tool Descriptions & Guidelines
    *   *Step 1.2.1:* Draft/Refine `read_file` description (Prompt Engineer)
    *   *Step 1.2.2:* Draft/Refine `edit_file` description (Prompt Engineer)
    *   *Step 1.2.3:* Document Agent Tool Selection Guidelines (Prompt Engineer, Agent Engineer)
*   **Milestone 1.3:** Define User Stories & Backlog
    *   *Step 1.3.1:* Define `read_file` User Stories (Product Owner, Team)
    *   *Step 1.3.2:* Define `edit_file` User Stories (incl. confirmation) (Product Owner, Team)
    *   *Step 1.3.3:* Prioritize Backlog (Product Owner)
*   **Milestone 1.4:** Define UX Flows
    *   *Step 1.4.1:* Design User Confirmation Flow & Mockups (AI UX Engineer)
    *   *Step 1.4.2:* Design Tool Feedback Display (AI UX Engineer)

---

## Phase 2: Core Development

*   **Milestone 2.1:** Implement `read_file`
    *   *User Story:* RF-US-01: As an Agent, I need to read a file securely, so that I can access its content.
        *   Task RF-T-01: Implement path validation (REQ-RF-002) (SSE)
        *   Task RF-T-02: Implement file read logic (REQ-RF-003) (SSE)
        *   Task RF-T-03: Implement error handling (REQ-RF-004) (SSE)
        *   Task RF-T-04: Implement basic logging (REQ-RF-005) (SSE)
        *   Task RF-T-05: Write Unit Tests (SSE)
*   **Milestone 2.2:** Implement `edit_file` (Proposal & Execution)
    *   *User Story:* EF-US-01: As an Agent, I need to propose an edit to a file, so that a user can review it.
    *   *User Story:* EF-US-02: As a System, I need to apply an approved file edit, so that the user's request is fulfilled.
        *   Task EF-T-01: Implement path validation (REQ-EF-002) (SSE)
        *   Task EF-T-02: Implement edit proposal reception (REQ-EF-001) (SSE)
        *   Task EF-T-03: Implement user confirmation hook/trigger (REQ-EF-003) (SSE)
        *   Task EF-T-04: Implement approved edit application logic (REQ-EF-005) (SSE)
        *   Task EF-T-05: Implement error handling (REQ-EF-006) (SSE)
        *   Task EF-T-06: Implement detailed logging (REQ-EF-007) (SSE)
        *   Task EF-T-07: Write Unit Tests (SSE)

---

## Phase 3: Integration & Testing

*   **Milestone 3.1:** Deploy Tool Service (Staging)
    *   *Step 3.1.1:* Package Tool Service (Orchestrator, SSE)
    *   *Step 3.1.2:* Deploy to Staging Env (Orchestrator)
*   **Milestone 3.2:** Integrate with Agent Framework
    *   *User Story:* INT-US-01: As an Agent, I need to correctly call the `read_file` API and handle responses.
    *   *User Story:* INT-US-02: As an Agent, I need to correctly call the `edit_file` API and handle the user confirmation workflow.
        *   Task INT-T-01: Implement API calls from Orchestrator (Orchestrator)
        *   Task INT-T-02: Implement agent logic for tool selection (Agent Engineer)
        *   Task INT-T-03: Implement agent response/error handling (Agent Engineer)
        *   Task INT-T-04: Implement agent handling of confirmation flow (Agent Engineer)
        *   Task INT-T-05: Implement agent guardrails (Agent Engineer)
*   **Milestone 3.3:** Implement User Confirmation UI
    *   *User Story:* UX-US-01: As a User, I need to see proposed file edits clearly and be able to approve or reject them easily.
        *   Task UX-T-01: Develop UI based on mockups (AI UX Engineer, Frontend Dev?)
        *   Task UX-T-02: Integrate UI with confirmation hook/callback (AI UX Engineer, Orchestrator)
*   **Milestone 3.4:** Integration Testing
    *   *Step 3.4.1:* Write End-to-End test cases (Team)
    *   *Step 3.4.2:* Execute Integration Tests (Team)
    *   *Step 3.4.3:* Architectural Review of Integration (Principal Architect)

---

## Phase 4: UAT & Release

*   **Milestone 4.1:** User Acceptance Testing
    *   *Step 4.1.1:* Execute UAT Plan (Product Owner, AI UX Engineer, Testers)
    *   *Step 4.1.2:* Gather Feedback
*   **Milestone 4.2:** Bug Fixing & Polish
    *   *Step 4.2.1:* Address UAT bugs/feedback (Team)
*   **Milestone 4.3:** Production Release
    *   *Step 4.3.1:* Final Deployment Checks (Orchestrator, SSE)
    *   *Step 4.3.2:* Release to Production

---

## Appendix: Code Examples / Diagrams (Illustrative)

*   **(Placeholder for API request/response examples)**
*   **(Placeholder for logging schema example)**
*   **(Placeholder for basic sequence diagram of edit confirmation flow)**

```python
# Example: Basic Path Validation Concept (Python)
def is_path_allowed(file_path: str, allowed_prefixes: list[str]) -> bool:
    """Checks if the normalized absolute path starts with an allowed prefix."""
    try:
        abs_path = os.path.abspath(file_path)
        # Basic normalization (resolve symlinks, etc. might be needed)
        normalized_path = os.path.normpath(abs_path)

        for prefix in allowed_prefixes:
            norm_prefix = os.path.normpath(os.path.abspath(prefix))
            if normalized_path.startswith(norm_prefix):
                # Potentially add checks for '..' components after prefix match
                return True
        return False
    except Exception:
        return False # Error during path processing
``` 