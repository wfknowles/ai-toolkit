# Prompt Engineer - Round 3 Pre-Analysis

**Based on Round 2 Analysis & Requirements:** We have detailed definitions for assets (schemas, system prompt), strategies (error handling), and methodologies (evaluation). The next step is integrating prompt development and tuning into the project plan.

**Initial Milestones/Phases/Steps (Prompt Engineering Focus):**

1.  **Phase 1: Setup & Foundational Prompts (Aligns with Sprint 0-1)**
    *   **Milestone:** Core System Prompt v1.0 Defined.
    *   **Steps:**
        *   Task: Draft initial Core Agent System Prompt (persona, objectives, core policies based on R2 discussions).
        *   Task: Define initial Python code schemas for `read_file` and `insert_code_snippet` (collaborate w/ AE).
        *   Task: Incorporate tool schemas and basic usage/error handling policies into System Prompt v1.0.
        *   Task: Establish prompt versioning convention.
        *   Task: Define initial set of golden test cases for manual evaluation (Q&A, Insert Success/Fail).

2.  **Phase 2: Tool Integration & Reliability Tuning (Aligns with Sprints 1-3)**
    *   **Milestone:** Prompts reliably generate correct function calls for `read_file` and `insert_code_snippet` in golden test cases.
    *   **Milestone:** Agent handles documented tool errors gracefully based on prompt instructions.
    *   **Steps:**
        *   Task: Refine tool schemas/descriptions with Examples based on initial testing.
        *   Task: Tune System Prompt and tool descriptions to improve `insert_code_snippet` parameter accuracy (esp. line number inference/handling).
        *   Task: Implement and test specific error handling prompt instructions for `FileNotFoundError`, `InvalidLineNumberError`, `PermissionError` (coordinate w/ SSE/AE error implementation).
        *   Task: Run prompts against golden test cases regularly (manual eval); iterate based on failures.

3.  **Phase 3: Workflow & UX Alignment Tuning (Aligns with Sprints 3-5)**
    *   **Milestone:** Agent responses and error messages align with UX design and user workflows.
    *   **Steps:**
        *   Task: Refine agent persona and tone in System Prompt based on UX feedback.
        *   Task: Adjust prompts to ensure agent clearly states intent before `insert_code_snippet`.
        *   Task: Tune context usage instructions if initial implicit context proves insufficient.
        *   Task: Refine user-facing error message wording in prompts based on UX review.

**Initial Thoughts/Concerns:**
*   Tight feedback loop needed between prompt changes, backend implementation (AE/SSE), and UX testing (UXE/Test Eng).
*   Allocating sufficient time for prompt iteration and evaluation within sprints is crucial, as LLM behavior can be unpredictable.
*   Need clarity on *how* prompt evaluation results will be tracked and communicated. 