# MotM MVP Project Roadmap & Tasks

## Overview

This document outlines the milestones, phases, user stories, and tasks required to deliver the Minimum Viable Product (MVP) for the AI Coding Assistant VSCode Extension. The MVP focuses on providing reliable code Q&A and code insertion capabilities using `read_file` and `insert_code_snippet` tools, integrated within a VSCode chat interface.

**Primary Goal:** Deliver a usable and reliable AI coding assistant MVP within VSCode that can answer questions about the active file and safely insert generated code snippets via a user-confirmed process.

**Key Technologies:** Python (FastAPI backend), Gemini Pro (LLM), VSCode Extension (Webview with React/Vue/Svelte), Docker.

**Core Tools:**
*   `read_file`: Reads content from a file within the allowed workspace.
*   `insert_code_snippet`: Inserts a code snippet into a file at a specified location within the allowed workspace, with backup and user confirmation via preview.

## High-Level Phasing & Milestones

*(Based on PO/PM analysis, refined through discussion)*

1.  **Phase 1: Foundational Setup & Reliability (Sprints 0-2)**
    *   **Goal:** Establish project infrastructure, implement core reliable tools (`read_file`, `insert_code_snippet`) with testing, define core interfaces.
    *   **Milestones:**
        *   [S0] Project Setup Complete (Repo, Structure, CI, Docker, Config/Logging).
        *   [S0/1] API Contract v1.0 & Tool Interface v1.0 Signed Off.
        *   [S1] `read_file` Tool Implemented & Unit Tested.
        *   [S1/2] Workspace Path Validation Implemented & Tested.
        *   [S2] `insert_code_snippet` Tool Implemented & Unit Tested (incl. backup).
        *   [S2] Basic Orchestrator/Agent Loop & Tool Executor Structure In Place.

2.  **Phase 2: Core Workflow Integration & UX (Sprints 2-4)**
    *   **Goal:** Integrate backend components, connect API, implement core agent logic (function calling), implement core VSCode Extension UI and workflows.
    *   **Milestones:**
        *   [S2/3] Tools Integrated with Orchestrator via Interface.
        *   [S3] Agent Makes Successful Function Calls for Tools.
        *   [S3] `/chat` API Endpoint Functional (calling Orchestrator).
        *   [S3] Basic Tool Error Handling Implemented (Backend & Agent).
        *   [S3/4] VSCode Extension Chat UI Implemented (displaying messages).
        *   [S4] Code Q&A Workflow Demonstrable End-to-End.
        *   [S4] `insert_code_snippet` Preview/Confirm UX Implemented in UI.
        *   [S4] Code Insertion Workflow Demonstrable End-to-End.

3.  **Phase 3: MVP Release & Polish (Sprint 5)**
    *   **Goal:** Stabilize MVP, fix critical bugs, document, and prepare for internal release/testing.
    *   **Milestones:**
        *   [S5] Basic User Feedback Mechanism Implemented (UI & Backend Logging).
        *   [S5] Key Observability Metrics Logging Implemented (Tool Success Rate, Latency).
        *   [S5] Usability Testing Conducted & Major Issues Addressed.
        *   [S5] Key Bugs Fixed (meets PO criteria).
        *   [S5] Setup/Installation Documented & Tested (`README.md`).
        *   [S5] MVP Meets Definition of Done.
        *   [S5] Internal Demo Completed.

## User Stories & Tasks (MVP)

*(Stories are high-level; tasks provide more implementation detail)*

---

### **Epic: Project Foundation & Setup**

**User Story 1 (Setup):** As a Developer (SSE/AOA), I want the basic project structure, repository, CI/CD pipeline, Docker setup, and core configuration/logging established, so that development can begin efficiently and consistently.

*   **Requirements:** Standard Python project layout, runnable FastAPI app, basic tests pass in CI, runnable via Docker, secure config loading, structured logging.
*   **AC:**
    *   Git repo initialized.
    *   Directory structure (`/app`, `/tests`) created.
    *   `pyproject.toml`/`requirements.txt` includes FastAPI, Pydantic, `aiofiles`, `pytest`, `pytest-asyncio`.
    *   `Dockerfile` allows building and running the app.
    *   Basic FastAPI app (`app/main.py`) exists with `/health` endpoint returning 200 OK.
    *   `pytest` configured; basic passing test exists.
    *   Basic CI (e.g., GitHub Action) runs `pytest` on push/PR.
    *   Pydantic Settings implemented for configuration (e.g., `API_KEY`, `WORKSPACE_ROOT`).
    *   `.env` file support for local development.
    *   Structured logging (e.g., JSON) configured with basic request/correlation ID logging (middleware).
*   **Tasks (Sprint 0):**
    *   `[SSE]` Setup Git repository.
    *   `[SSE]` Create initial project structure (`/app`, `/tests`, `/scripts`, `/config`).
    *   `[SSE]` Initialize `pyproject.toml` (using Poetry or similar) or `requirements.txt`.
    *   `[SSE]` Create initial `Dockerfile` and `docker-compose.yml` for local dev.
    *   `[SSE]` Implement basic FastAPI app (`app/main.py`) with `/health` endpoint.
    *   `[SSE]` Setup `pytest` and `pytest-asyncio`. Add a simple test for `/health`.
    *   `[SSE]` Setup basic GitHub Action for CI (linting, testing).
    *   `[SSE]` Implement Pydantic Settings (`app/config.py`) for API Key, Workspace Root.
    *   `[SSE]` Add `.env` handling using `python-dotenv`.
    *   `[SSE]` Configure basic structured logging (e.g., using `structlog` or standard logging with JSONFormatter).
    *   `[SSE]` Implement FastAPI middleware to inject correlation ID into logs.
    *   `[PA/AOA/SSE/AE/UXE]` **(Working Session)** Define API Contract v1.0 (Pydantic models, OpenAPI spec).
    *   `[PA/AOA/SSE]` **(Working Session)** Define Tool Interface v1.0 (Python Protocol/ABC) & `ToolResult` model.
    *   `[PM]` Groom Sprint 1 backlog based on finalized S0 outputs.

---

### **Epic: Core Tool Implementation**

**User Story 2 (Read File):** As an AI Agent, I want to reliably read the contents of a specified file within the user's workspace, so that I can answer questions about it or use its content for generation.

*   **Requirements:** Tool reads specified file path relative to configured workspace root. Handles errors gracefully. Async implementation. Path validation enforced.
*   **AC:**
    *   `read_file_async(file_path: str)` function implemented.
    *   Calls `validate_path_in_workspace` utility.
    *   Uses `aiofiles` for async reading.
    *   Returns file content as string on success.
    *   Raises specific documented exceptions (`FileNotFoundError`, `PermissionError`, custom `PathValidationError`, potentially `EncodingError`) on failure.
    *   Comprehensive unit tests pass, mocking `aiofiles` and filesystem, covering success, errors, and path validation edge cases.
*   **Tasks (Sprint 1):**
    *   `[SSE]` Implement `validate_path_in_workspace(user_path: str, workspace_root: Path)` utility function in `app/utils/security.py` using `pathlib` as discussed.
    *   `[SSE]` Write unit tests for `validate_path_in_workspace` covering normal cases, `..` traversal, symlinks, absolute paths, etc.
    *   `[SSE]` Implement `read_file_async(file_path: str)` in `app/tools/file_io.py` using `aiofiles` and calling validation util.
    *   `[SSE]` Implement specific error handling/raising within `read_file_async`.
    *   `[SSE]` Write comprehensive unit tests for `read_file_async` using `pytest-mock` / `asynctest` to mock `aiofiles`.

**User Story 3 (Insert Code Snippet):** As an AI Agent, I want to reliably insert a given code snippet into a specified file at a target location (line number or marker like 'EOF') within the user's workspace, ensuring a backup is made and the user confirms the change via a preview, so that I can safely modify code based on user requests.

*   **Requirements:** Tool inserts snippet at target location. Handles errors gracefully. Async. Path validation. Backup creation. Relies on external confirmation step (via separate API call) before execution. Provides context snippet for preview.
*   **AC:**
    *   `get_context_snippet_async(file_path: str, line_number: int)` implemented (returns N lines before/after). Unit tested.
    *   `insert_code_snippet_async(file_path: str, code_snippet: str, line_number: int)` implemented.
    *   Calls `validate_path_in_workspace`.
    *   Uses `aiofiles`.
    *   Creates backup (`.bak`) before attempting modification.
    *   Correctly inserts code at the specified line number (handling edge cases like line 0, EOF).
    *   Raises specific documented exceptions (`FileNotFoundError`, `PermissionError`, `InvalidLineNumberError`, `PathValidationError`, custom `BackupCreationError`, `WriteError`).
    *   Restores from backup if insertion fails after backup creation.
    *   Comprehensive unit tests pass, mocking `aiofiles` and filesystem, covering success, various error conditions (backup fails, write fails, invalid line), path validation, and atomicity concerns.
    *   *(Note: The actual execution is triggered by `/confirm_insertion`, not directly by the agent call)*
*   **Tasks (Sprint 1-2):**
    *   `[SSE]` Implement `get_context_snippet_async` in `app/tools/file_io.py`. (S1)
    *   `[SSE]` Write unit tests for `get_context_snippet_async`. (S1)
    *   `[SSE]` Implement `insert_code_snippet_async` structure in `app/tools/file_io.py`, including path validation call. (S1)
    *   `[SSE]` Implement backup creation logic (`.bak` file) within `insert_code_snippet_async`. (S1/S2)
    *   `[SSE]` Implement core insertion logic (reading file, inserting at line, writing back) using `aiofiles`. (S2)
    *   `[SSE]` Implement specific error handling/raising and restore-from-backup logic. (S2)
    *   `[SSE]` Write comprehensive unit tests for `insert_code_snippet_async`. (S2)
    *   `[TestEng]` (From S2/S3) Review and take ownership of tool unit tests.

---

### **Epic: Backend Service Integration**

**User Story 4 (Tool Execution):** As an AI Orchestrator, I want to execute validated tool calls requested by the AI Agent using a defined interface, handling success and failure results consistently, so that agent requests can be reliably fulfilled.

*   **Requirements:** Executor maps tool names to functions. Uses Tool Interface. Validates params against Pydantic schemas. Catches tool exceptions. Returns standardized `ToolResult`. DI used.
*   **AC:**
    *   `ToolResult` Pydantic model defined (can represent success with data or error with type/message).
    *   Tool Interface (Protocol/ABC) defined.
    *   `ToolExecutor` service/class implemented.
    *   Executor receives tool name, parameters, and tool implementations (via DI or registration).
    *   Executor validates received parameters against the registered tool's Pydantic schema.
    *   Executor calls the correct tool function using `try...except`.
    *   Maps successful return values to `ToolResult(success=True, data=...)`.
    *   Maps specific, documented tool exceptions to `ToolResult(success=False, error_type=..., error_message=...)`.
    *   Logs execution start, parameters (potentially masked), result/error, and latency.
    *   Unit tests pass, mocking tool functions and schemas.
*   **Tasks (Sprint 2):**
    *   `[AOA/PA/SSE]` Finalize `ToolResult` model and Tool Interface definition (from S0/1 working session output).
    *   `[AOA/SSE]` Implement `ToolExecutor` class/module (`app/services/tool_executor.py`).
    *   `[AOA/SSE]` Implement Pydantic schema validation within the executor.
    *   `[AOA/SSE]` Implement tool function mapping/calling logic.
    *   `[AOA/SSE]` Implement `try...except` block mapping tool exceptions to `ToolResult(error=...)`.
    *   `[AOA/SSE]` Add logging for execution details and latency.
    *   `[AOA/SSE]` Write unit tests for `ToolExecutor` using mocked tools and results.

**User Story 5 (Orchestration & Agent Logic):** As an AI Orchestrator, I want to manage the core loop of receiving user input, preparing context/prompts, calling the LLM (Gemini), parsing responses (including function calls), invoking the Tool Executor, formatting results, and managing basic state (history), so that a conversational AI agent interaction can occur.

*   **Requirements:** Basic ReAct loop via function calling. Integrates Gemini client. Integrates Tool Executor. Uses DI. Basic history management.
*   **AC:**
    *   Basic `GeminiClient` service implemented (connects, calls `generate_content` with prompt/tools).
    *   `Orchestrator` service/class implemented (`app/services/orchestrator.py`).
    *   Receives dependencies (LLM Client, Tool Executor, State Manager?) via DI.
    *   `handle_chat` method takes user message, conversation ID/history.
    *   Prepares prompt using System Prompt (from PE), history, and user message.
    *   Prepares tool schemas for Gemini API call.
    *   Calls `GeminiClient`.
    *   Parses `function_call` from LLM response.
    *   Calls `ToolExecutor` with extracted tool name/params.
    *   Receives `ToolResult` from executor.
    *   Formats `ToolResult` (success or error) into function response for follow-up LLM call.
    *   Includes basic state management (passing conversation history between turns).
    *   Logs key steps (LLM call, function call parsed, tool result received, final response).
    *   Unit/integration tests pass, mocking dependencies (LLM Client, Executor, State).
*   **Tasks (Sprints 1-3):**
    *   `[AE/AOA]` Define Python representations of tool Pydantic schemas (`app/tools/schemas.py`) (S0/1 - from working session).
    *   `[AOA/SSE]` Implement basic `GeminiClient` (`app/services/gemini_client.py`) capable of making API calls with tool definitions. (S1/S2)
    *   `[AOA]` Implement basic `Orchestrator` skeleton, integrating with DI framework. (S1)
    *   `[AE/AOA]` Implement logic to prepare prompts and tool schemas for Gemini call. (S2)
    *   `[AE/AOA]` Implement logic to parse `function_call` from Gemini response. (S2/S3)
    *   `[AE/AOA]` Implement logic to format successful `ToolResult` into function response for Gemini. (S3)
    *   `[AE/AOA]` Implement logic to format error `ToolResult` into function response for Gemini. (S3)
    *   `[AOA]` Integrate `ToolExecutor` call within Orchestrator. (S2/S3)
    *   `[AOA]` Implement basic history passing mechanism. (S2/S3)
    *   `[AOA/AE]` Add core logging points. (S3)
    *   `[AOA/AE/TestEng]` Write unit/integration tests for Orchestrator flow using mocks. (S3)
    *   `[PE]` Provide System Prompt v1.0 including tool usage instructions and basic error handling policies. (S1/S2)

**User Story 6 (API Endpoints):** As a VSCode Extension Frontend, I want to communicate with the backend via defined API endpoints (`/chat`, `/confirm_insertion`, `/health`) to send user requests, receive agent responses (potentially streamed), and manage the code insertion flow.

*   **Requirements:** FastAPI endpoints implemented according to API Contract v1.0. Uses Pydantic models. Calls Orchestrator service. Basic error handling.
*   **AC:**
    *   `/health` endpoint implemented (returns 200 OK). (Done in S0)
    *   `/chat` endpoint implemented (`app/api/endpoints/chat.py`).
        *   Accepts request body matching Pydantic model from API Contract (user message, history/context).
        *   Calls `Orchestrator.handle_chat`.
        *   Returns response body matching Pydantic model (agent message, tool calls?). (Streaming TBD)
        *   Handles potential Orchestrator errors gracefully (returns appropriate HTTP status code).
    *   `/confirm_insertion` endpoint implemented.
        *   Accepts request body with necessary confirmation details (e.g., original request ID).
        *   Calls specific Orchestrator/Executor method to trigger the validated `insert_code_snippet_async`.
        *   Returns success/failure response.
    *   Endpoints integrated with Orchestrator service via DI.
    *   Basic integration tests pass (calling endpoints, mocking Orchestrator).
*   **Tasks (Sprint 3-4):**
    *   `[SSE/AOA]` Implement `/chat` endpoint structure, request/response models (using finalized Pydantic schemas). (S3)
    *   `[SSE/AOA]` Integrate `/chat` endpoint with `Orchestrator.handle_chat` call. (S3)
    *   `[SSE/AOA]` Implement `/confirm_insertion` endpoint structure and request model. (S3/S4)
    *   `[SSE/AOA]` Integrate `/confirm_insertion` endpoint with logic to trigger tool execution via Orchestrator/Executor. (S4)
    *   `[SSE/TestEng]` Write integration tests for API endpoints using `FastAPI.TestClient`, mocking the Orchestrator service. (S3/S4)
    *   `[SSE/AOA]` (TBD/Optional for MVP) Implement streaming response logic for `/chat` if required by UX. (S4?)

---

### **Epic: VSCode Extension Frontend & UX**

**User Story 7 (Core Chat UI):** As a User, I want a VSCode extension with a chat interface where I can type messages to an AI agent, see the conversation history, and view agent responses, so that I can interact with the coding assistant.

*   **Requirements:** VSCode extension activates. Opens webview panel. Basic chat input. History display. Agent status indicator. Context display (active file). API communication layer.
*   **AC:**
    *   Basic VSCode extension structure created (manifest, activation).
    *   Webview panel opens with chosen framework (React/Vue/Svelte) app loaded.
    *   Chat input component allows typing and sending messages.
    *   Chat history component displays user messages and agent text responses.
    *   Basic agent status indicator (e.g., "Thinking...", "Idle").
    *   Displays current active file as context hint.
    *   Frontend API client can call backend `/health` and `/chat` endpoints.
    *   Basic state management for conversation history in UI.
*   **Tasks (Sprints 1-3):**
    *   `[UXE]` Create detailed mockups for chat UI, context display. (S0/1)
    *   `[UXE]` Research/Recommend/Decide on frontend framework. (S0/1)
    *   `[UXE]` Setup basic VSCode Extension project (`package.json`, entry point). (S1)
    *   `[UXE]` Setup Webview panel and load chosen framework boilerplate. (S1)
    *   `[UXE]` Implement chat history display component. (S2)
    *   `[UXE]` Implement user input component. (S2)
    *   `[UXE]` Implement frontend API client layer (e.g., using `fetch`) to call backend. (S2)
    *   `[UXE]` Integrate API client to send messages to `/chat` and display text responses. (S3)
    *   `[UXE]` Implement basic agent status indicator UI. (S3)
    *   `[UXE]` Implement context display UI element (showing active file). (S3)

**User Story 8 (Insertion Preview & Confirmation):** As a User, when the AI agent suggests inserting code, I want to see a preview (diff) of the exact changes in the target file and explicitly confirm or reject them before any modification occurs, so that I can confidently allow the agent to modify my code.

*   **Requirements:** Triggered by agent response indicating code insertion. Fetches context snippet. Displays diff preview. Provides Confirm/Reject buttons. Communicates confirmation back to backend. Handles backend errors during insertion.
*   **AC:**
    *   UI detects agent response requiring insertion confirmation.
    *   Calls backend to get context snippet (using `get_context_snippet` via orchestrator).
    *   Displays diff preview component showing proposed changes clearly.
    *   Displays target filename/location.
    *   Confirm/Reject buttons are functional.
    *   Clicking Confirm calls backend `/confirm_insertion` endpoint.
    *   UI updates based on success/failure response from `/confirm_insertion`.
    *   Displays user-friendly error messages mapped from backend error types.
*   **Tasks (Sprint 3-4):**
    *   `[UXE]` Create detailed mockups for insertion preview/confirmation flow. (S1/S2)
    *   `[UXE]` Implement frontend logic to detect insertion requests. (S3)
    *   `[UXE]` Implement frontend call to get context snippet from backend. (S3/S4)
    *   `[UXE]` Implement diff preview component (using a JS diff library). (S4)
    *   `[UXE]` Implement Confirm/Reject buttons and associated state management. (S4)
    *   `[UXE]` Implement frontend call to `/confirm_insertion` endpoint. (S4)
    *   `[UXE]` Implement UI updates based on insertion success/failure. (S4)
    *   `[UXE/PE]` Design user-facing error messages for insertion failures. (S3)
    *   `[UXE]` Implement error message display logic. (S4)

---

### **Epic: Polish & Release**

**User Story 9 (User Feedback):** As a User, I want a simple way to provide feedback (e.g., thumbs up/down) on the agent's responses, so that I can help improve the assistant. As a Product Owner, I want this feedback logged for analysis.

*   **Requirements:** Simple UI element per response. Logs feedback event to backend.
*   **AC:**
    *   Thumbs up/down UI elements appear on agent messages.
    *   Clicking sends feedback event (response ID, rating, optional text) to a backend logging mechanism (could be simple `/log_feedback` endpoint or integrated with existing logging).
    *   Feedback is logged on the backend with associated conversation/turn identifiers.
*   **Tasks (Sprint 5):**
    *   `[UXE]` Implement feedback UI components.
    *   `[UXE]` Implement frontend logic to send feedback.
    *   `[SSE/AOA]` Implement simple backend mechanism/endpoint to receive and log feedback data.

**User Story 10 (Observability):** As a Maintainer (PA/AOA/SSE), I want key operational metrics (tool success/failure rate, E2E latency) logged, so that I can monitor the health and performance of the service.

*   **Requirements:** Metrics defined by PA logged during relevant operations.
*   **AC:**
    *   Tool Executor logs success/failure status per tool call.
    *   API layer logs request start/end timestamps to calculate E2E latency.
    *   Logs include correlation IDs and relevant context (tool name, endpoint).
*   **Tasks (Sprint 5):**
    *   `[AOA/SSE]` Implement logging for tool success/failure rate in Tool Executor (ensure code from S2/S3 does this).
    *   `[SSE/AOA]` Implement logging for E2E latency in API layer/middleware (ensure code from S3/S4 does this).
    *   `[PA]` Review logging implementation for metrics coverage.

**User Story 11 (Documentation & Release Prep):** As a Developer (Team), I want clear setup and usage instructions, and the MVP to meet its Definition of Done, so that it can be prepared for internal release and testing.

*   **Requirements:** README with setup/run instructions. All MVP ACs met. Critical bugs fixed. Usability tested. Final demo.
*   **AC:**
    *   `README.md` created/updated with clear local setup instructions (env vars, docker-compose up, etc.) and basic usage guide.
    *   All user stories for MVP meet their ACs.
    *   Critical/Major bug list (from S4/S5 testing) is empty or approved by PO.
    *   Usability testing feedback incorporated (critical issues).
    *   MVP meets Definition of Done checklist (PM/PO sign-off).
    *   Successful internal demo conducted.
*   **Tasks (Sprint 5):**
    *   `[UXE/TestEng]` Conduct usability testing.
    *   `[ALL]` Focused bug fixing based on integration and usability testing.
    *   `[SSE/UXE]` Write/Finalize `README.md`.
    *   `[TestEng]` Perform final regression testing.
    *   `[PM/PO]` Verify DoD checklist completion.
    *   `[ALL]` Prepare and conduct internal demo. 