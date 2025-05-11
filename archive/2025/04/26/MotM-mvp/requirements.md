# MVP Requirements & Definitions (Round 2 Synthesis)

This document compiles the key definitions, requirements, acceptance criteria (ACs), and guidelines for the MVP as determined through the Meeting of the Minds Round 2 discussions.

---

## 1. Core Components & Features

### 1.1. Backend Service
*   **Definition:** Local backend service providing agentic capabilities via API.
*   **Technology:** Python 3.x, FastAPI framework.
*   **Deployment:** Docker container (local execution).
*   **Requirements:**
    *   REQ-BE-01: Must implement API endpoints defined in API Contract.
    *   REQ-BE-02: Must handle requests asynchronously.
    *   REQ-BE-03: Must integrate with Gemini Client Module.
    *   REQ-BE-04: Must integrate with Tool Execution Module.
    *   REQ-BE-05: Must implement core orchestration logic.
*   **Guidelines:**
    *   GUIDE-BE-01: Follow modular project structure (`api`, `core`, `tools`, etc.).
    *   GUIDE-BE-02: Use Dependency Injection for testability.

### 1.2. VSCode Extension (GUI)
*   **Definition:** Primary user interface for interacting with the agent.
*   **Technology:** VSCode Extension API, Webview UI (using React/Vue/Svelte recommended).
*   **Requirements:**
    *   REQ-GUI-01: Must provide a chat interface within a VSCode Webview.
    *   REQ-GUI-02: Must display conversation history (user prompts, agent responses).
    *   REQ-GUI-03: Must allow users to input text queries.
    *   REQ-GUI-04: Must communicate with the Backend Service via the defined API Contract.
    *   REQ-GUI-05: Must display active file context provided by the agent/backend.
    *   REQ-GUI-06: Must implement the UX for `insert_code_snippet` (preview, confirm).
    *   REQ-GUI-07: Must display agent status (idle, busy, error).
    *   REQ-GUI-08: Must provide clear setup instructions (README).
    *   REQ-GUI-09: Must have UI indicator for backend connection status.
*   **Guidelines:**
    *   GUIDE-GUI-01: Strive for responsive UI performance within the webview.
    *   GUIDE-GUI-02: Follow VSCode UI conventions where possible.
    *   GUIDE-GUI-03: Provide simple user feedback mechanism (e.g., thumbs up/down).

### 1.3. Tool: `read_file`
*   **Definition:** Tool to read the content of a specified file.
*   **Requirements:**
    *   REQ-TOOL-RF-01: Must accept `file_path` as input.
    *   REQ-TOOL-RF-02: Must perform workspace path validation on `file_path`.
    *   REQ-TOOL-RF-03: Must return file content as string on success.
    *   REQ-TOOL-RF-04: Must handle UTF-8 encoding; raise error for incompatible encoding.
    *   REQ-TOOL-RF-05: Must raise specific, documented errors (`FileNotFoundError`, `PermissionError`, `EncodingError`).
*   **Guidelines:**
    *   GUIDE-TOOL-RF-01: Implement using async file I/O (`aiofiles`).
    *   GUIDE-TOOL-RF-02: Log execution start, params (path), end, success/failure, duration.

### 1.4. Tool: `insert_code_snippet`
*   **Definition:** Tool to insert a provided code snippet into a file at a specified line number.
*   **Requirements:**
    *   REQ-TOOL-IC-01: Must accept `file_path`, `line_number` (integer > 0), `code_snippet` (string) as input.
    *   REQ-TOOL-IC-02: Must perform workspace path validation on `file_path`.
    *   REQ-TOOL-IC-03: Must validate `line_number` against file bounds (raise `InvalidLineNumberError`).
    *   REQ-TOOL-IC-04: Must create a backup file (`.bak`) before modifying the original file (overwrite previous `.bak`).
    *   REQ-TOOL-IC-05: Must insert the exact `code_snippet` before the specified `line_number`.
    *   REQ-TOOL-IC-06: Must not modify any other lines in the file.
    *   REQ-TOOL-IC-07: Must handle UTF-8 encoding; raise error for incompatible encoding.
    *   REQ-TOOL-IC-08: Must raise specific, documented errors (`FileNotFoundError`, `PermissionError`, `InvalidLineNumberError`, `EncodingError`, `BackupCreationError`, `WriteError`).
    *   REQ-TOOL-IC-09: Must return success status on successful insertion.
*   **Acceptance Criteria (from PO):**
    *   AC-TOOL-IC-01: Given valid inputs, code is inserted correctly without altering other lines.
    *   AC-TOOL-IC-02: Agent presents preview showing context and code before action (UX Req).
    *   AC-TOOL-IC-03: Agent requires explicit user confirmation (UX Req).
    *   AC-TOOL-IC-04: Agent provides clear success/failure feedback (UX Req).
    *   AC-TOOL-IC-05: Tool creates backup file.
    *   AC-TOOL-IC-06: (If Undo implemented) User can undo last insertion.
*   **Guidelines:**
    *   GUIDE-TOOL-IC-01: Implement using async file I/O (`aiofiles`).
    *   GUIDE-TOOL-IC-02: Log execution start, params (path, line, snippet length), end, success/failure, duration.
    *   GUIDE-TOOL-IC-03: Handle insertion into empty file (line 1).

### 1.5. Agent Logic
*   **Definition:** Core logic managing interaction flow using Gemini Pro.
*   **Technology:** ReAct-style flow using Gemini Function Calling.
*   **Requirements:**
    *   REQ-AGENT-01: Must parse user query, history, and context received from Orchestrator.
    *   REQ-AGENT-02: Must prepare tool schemas and prompt for Gemini API call.
    *   REQ-AGENT-03: Must correctly parse Gemini response (text or function call).
    *   REQ-AGENT-04: Must extract tool name and parameters from function call response.
    *   REQ-AGENT-05: Must request tool execution from Orchestrator.
    *   REQ-AGENT-06: Must handle `ToolResult` (success or error) received from Orchestrator.
    *   REQ-AGENT-07: Must format tool result appropriately for follow-up Gemini call.
    *   REQ-AGENT-08: Must adhere to error handling policies defined in System Prompt.
*   **Guidelines:**
    *   GUIDE-AGENT-01: Implement basic validation on LLM-provided parameters before tool execution.
    *   GUIDE-AGENT-02: Monitor and log API call latency and token usage.

### 1.6. RAG (Simplified MVP)
*   **Definition:** Provide basic workspace context to the agent.
*   **Requirements:**
    *   REQ-RAG-01: VSCode Extension must identify active editor file path and content/selection.
    *   REQ-RAG-02: Extension must pass this context to the Backend API.
    *   REQ-RAG-03: Backend (Orchestrator/Context Prepper) must format and include this context in the prompt to Gemini.
*   **Guidelines:**
    *   GUIDE-RAG-01: Define reasonable limits on context snippet size.

---

## 2. Strategies & Methodologies

### 2.1. API Contract
*   **Definition:** Interface between VSCode Extension and Backend.
*   **Asset:** OpenAPI Specification (auto-generated where possible).
*   **Requirements:**
    *   REQ-API-01: Must define `/chat` (or `/agent/invoke`) endpoint (POST) with request/response models (Pydantic).
    *   REQ-API-02: Request model must include `user_query`, `history`, and `context` (active file/selection).
    *   REQ-API-03: Must define `/health` endpoint (GET).
    *   REQ-API-04: Must be finalized in Sprint 0.
*   **Guidelines:**
    *   GUIDE-API-01: Use clear, consistent naming.
    *   GUIDE-API-02: Include descriptions for endpoints and models.

### 2.2. Tool Schemas
*   **Definition:** Structure defining tools for Gemini Function Calling.
*   **Asset:** Python code (`app/tools/schemas.py`) as single source of truth.
*   **Requirements:**
    *   REQ-SCHEMA-01: Must define schemas for `read_file` and `insert_code_snippet`.
    *   REQ-SCHEMA-02: Schemas must include name, description, parameters (name, type, description, required).
    *   REQ-SCHEMA-03: Parameter definitions must be precise and unambiguous.
*   **Guidelines:**
    *   GUIDE-SCHEMA-01: Include concrete Examples within schemas if supported/effective.
    *   GUIDE-SCHEMA-02: Auto-generate documentation format (e.g., Markdown) for PE reference.

### 2.3. System Prompt
*   **Definition:** Core instructions guiding the Gemini agent\'s behavior.
*   **Asset:** Text/Markdown file, version controlled.
*   **Requirements:**
    *   REQ-PROMPT-01: Must define agent persona and core objective.
    *   REQ-PROMPT-02: Must include Tool Usage Policy.
    *   REQ-PROMPT-03: Must include Context Usage Policy (how to use provided file snippets).
    *   REQ-PROMPT-04: Must include Error Handling Policy with specific instructions for documented tool errors (`FileNotFoundError`, `InvalidLineNumberError`, `PermissionError`).
*   **Guidelines:**
    *   GUIDE-PROMPT-01: Aim for clarity and conciseness.
    *   GUIDE-PROMPT-02: Structure prompt for reliability in function calling.
    *   GUIDE-PROMPT-03: Maintain consistent agent tone.

### 2.4. Error Handling Strategy
*   **Definition:** How errors from tools and APIs are processed and presented.
*   **Requirements:**
    *   REQ-ERR-01: Tool Executor must raise specific, documented exceptions.
    *   REQ-ERR-02: Orchestrator must catch tool exceptions and map them to a standardized `ToolResult` object (incl. `status`, `error_type`, `error_message`).
    *   REQ-ERR-03: Orchestrator must pass `ToolResult` back to Agent/LLM for handling based on System Prompt.
    *   REQ-ERR-04: Orchestrator/Gemini Client must handle Gemini API errors (retries for transient, user message for fatal).
    *   REQ-ERR-05: User-facing error messages (designed with UXE) must be clear, concise, and avoid jargon.
*   **Guidelines:**
    *   GUIDE-ERR-01: Agent should attempt recovery (e.g., ask for clarification) based on prompt instructions where feasible.

### 2.5. Testing Strategy
*   **Definition:** Approach to ensure code quality and reliability.
*   **Requirements:**
    *   REQ-TEST-01: Unit tests (using `pytest`, `pytest-asyncio`) must be implemented for critical backend logic, especially tool implementations.
    *   REQ-TEST-02: Unit tests must mock external dependencies (filesystem, API calls).
    *   REQ-TEST-03: Integration tests must verify end-to-end agent flows for key workflows (Q&A, Insert).
    *   REQ-TEST-04: Manual prompt evaluation against golden test cases must be performed.
    *   REQ-TEST-05: Informal usability testing must be conducted during development.
    *   REQ-TEST-06: All code requires review (via PR) before merging.
*   **Guidelines:**
    *   GUIDE-TEST-01: Aim for meaningful unit test coverage (>80% for tools).
    *   GUIDE-TEST-02: CI pipeline (GitHub Actions) runs tests automatically on PRs.

### 2.6. Configuration Management
*   **Definition:** Handling of configuration parameters.
*   **Requirements:**
    *   REQ-CONF-01: Must use Pydantic Settings loading from env vars / `.env` file.
    *   REQ-CONF-02: Gemini API Key must be configurable and handled securely (not checked into Git).
    *   REQ-CONF-03: Workspace root path must be configurable at backend startup.
*   **Guidelines:**
    *   GUIDE-CONF-01: Provide clear documentation (`README.md`) on required configuration.

### 2.7. Logging Strategy
*   **Definition:** Approach to application logging for monitoring and debugging.
*   **Requirements:**
    *   REQ-LOG-01: Must use standard Python `logging`.
    *   REQ-LOG-02: Logs must be structured JSON.
    *   REQ-LOG-03: Must include `correlation_id` for all logs related to a single API request.
    *   REQ-LOG-04: Must log key events (API req/res, tool call start/end/params(masked)/result, errors).
    *   REQ-LOG-05: Must use appropriate log levels (INFO, WARN, ERROR).
*   **Guidelines:**
    *   GUIDE-LOG-01: Avoid logging sensitive data (API keys, full code snippets) by default.

### 2.8. Security
*   **Definition:** Measures to ensure safe operation.
*   **Requirements:**
    *   REQ-SEC-01: Secure handling of Gemini API Key.
    *   REQ-SEC-02: Workspace path validation enforced in tools.
    *   REQ-SEC-03: Backend process runs with least privilege.
*   **Guidelines:**
    *   GUIDE-SEC-01: Conduct security review of design/implementation.
    *   GUIDE-SEC-02: Standardize on UTF-8 encoding, handle errors.

### 2.9. Agile Process
*   **Definition:** Development methodology.
*   **Requirements:**
    *   REQ-PROC-01: Use Agile (Scrum/Kanban) with short sprints (1-2 weeks).
    *   REQ-PROC-02: Implement defined DoD, including code review.
    *   REQ-PROC-03: Maintain project backlog (Jira/GitHub Projects).
    *   REQ-PROC-04: Conduct standard agile ceremonies.
*   **Guidelines:**
    *   GUIDE-PROC-01: Use spikes for research tasks.
    *   GUIDE-PROC-02: Refine estimates based on team velocity.
    *   GUIDE-PROC-03: Maintain Risk Log.

--- 