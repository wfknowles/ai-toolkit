# AI Orchestrator/Architect - Round 3 Pre-Analysis

**Based on Round 2 Analysis & Requirements:** Detailed definitions for orchestration flow, tool interface, context/error handling, modular design. Need to map these to project phases.

**Initial Milestones/Phases/Steps (Orchestration/Architecture Focus):**

1.  **Phase 1: Core Service & Interface Setup (Aligns with Sprint 0-1)**
    *   **Milestone:** Backend service runnable locally via Docker.
    *   **Milestone:** Core Orchestration loop structure implemented.
    *   **Milestone:** Tool Interface Protocol/ABC defined and integrated.
    *   **Steps:**
        *   Task: Implement basic FastAPI app structure (SSE collab).
        *   Task: Implement `Dockerfile` (SSE collab).
        *   Task: Define and implement `ToolResult` model.
        *   Task: Define Tool Interface (Protocol/ABC).
        *   Task: Implement basic Orchestrator class/module skeleton.
        *   Task: Implement basic Gemini Client module (connect, simple call).
        *   Task: Setup Dependency Injection framework.

2.  **Phase 2: Tool & Agent Integration (Aligns with Sprints 1-3)**
    *   **Milestone:** Orchestrator correctly invokes `read_file` and `insert_code_snippet` tools via interface.
    *   **Milestone:** Orchestrator handles successful tool execution results and passes them back to Gemini.
    *   **Milestone:** Orchestrator correctly passes tool schemas to Gemini.
    *   **Milestone:** Orchestrator correctly parses function call requests from Gemini.
    *   **Milestone:** Basic context handling (from API to prompt) implemented.
    *   **Steps:**
        *   Task: Integrate `Tool Executor` module with Orchestrator using Tool Interface.
        *   Task: Implement logic to prepare tool schemas for Gemini API call.
        *   Task: Implement logic to parse `function_call` from Gemini response (AE collab).
        *   Task: Implement logic to format `ToolResult` into function response for Gemini (AE collab).
        *   Task: Implement `Context Prepper` logic for MVP context strategy.
        *   Task: Implement basic conversation history management (passing).

3.  **Phase 3: Error Handling & Robustness (Aligns with Sprints 2-4)**
    *   **Milestone:** Orchestrator correctly catches documented tool errors and passes standardized `ToolResult` (Error) back to agent.
    *   **Milestone:** Orchestrator/Gemini Client implements basic retry logic for transient API errors.
    *   **Steps:**
        *   Task: Implement `try...except` blocks around tool execution calls, mapping specific exceptions (from SSE) to `ToolResult`.
        *   Task: Implement retry logic in Gemini Client module.
        *   Task: Implement handling for fatal Gemini API errors (e.g., content filter) -> format user message.
        *   Task: Add logging points throughout orchestration flow (using correlation ID).

4.  **Phase 4: API Integration & Polish (Aligns with Sprints 4-5)**
    *   **Milestone:** Backend fully integrated with VSCode extension via defined API contract.
    *   **Steps:**
        *   Task: Ensure API layer correctly calls orchestration service and handles responses/errors.
        *   Task: Implement `/health` endpoint.
        *   Task: Add necessary metrics tracking (tool success rate, latency).

**Initial Thoughts/Concerns:**
*   Need to ensure the separation of concerns between the orchestrator (flow control), agent (reasoning via LLM), and tools (execution) remains clean during implementation.
*   The state management (history passing) might need refinement if long conversations become common.
*   Defining the Tool Interface precisely early on is critical for parallel work. 