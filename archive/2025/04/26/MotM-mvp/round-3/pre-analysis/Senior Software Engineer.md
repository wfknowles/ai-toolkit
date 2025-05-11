# Senior Software Engineer - Round 3 Pre-Analysis

**Based on Round 2 Analysis & Requirements:** Have definitions for core assets (`requirements.txt`, `Dockerfile`, project structure), tool implementation strategy (async, errors, backup), API endpoints, testing, and config. Need to structure implementation into sprints/phases.

**Initial Milestones/Phases/Steps (Backend Implementation Focus):**

1.  **Phase 1: Project Setup & Core Infrastructure (Sprint 0)**
    *   **Milestone:** Basic FastAPI app running in Docker, basic project structure committed, CI running `pytest`.
    *   **Steps:**
        *   Task: Setup Git repository.
        *   Task: Create initial project structure (`/app`, `/tests`).
        *   Task: Initialize `requirements.txt`/`pyproject.toml` with core dependencies.
        *   Task: Create initial `Dockerfile`.
        *   Task: Implement basic FastAPI app (`main.py`) with `/health` endpoint.
        *   Task: Setup `pytest` and `pytest-asyncio`.
        *   Task: Setup basic CI pipeline (e.g., GitHub Action) to run `pytest`.
        *   Task: Define and commit initial API Contract (OpenAPI Spec - PA collab).
        *   Task: Implement Pydantic Settings for config (API key).
        *   Task: Setup `.env` handling for local dev.

2.  **Phase 2: Tool Implementation & Unit Testing (Sprints 1-2)**
    *   **Milestone:** `read_file_async` implemented with error handling and passing unit tests.
    *   **Milestone:** `insert_code_snippet_async` implemented with backup, error handling, path validation, and passing unit tests.
    *   **Steps:**
        *   Task: Implement `read_file_async` in `tools/file_io.py` using `aiofiles`.
        *   Task: Implement workspace path validation logic.
        *   Task: Implement documented error handling (`FileNotFound`, `Permission`, `Encoding`) for `read_file`.
        *   Task: Write comprehensive unit tests for `read_file` (success, errors, edge cases) using mocks.
        *   Task: Implement `insert_code_snippet_async` in `tools/file_io.py` using `aiofiles`.
        *   Task: Implement backup logic (`.bak` file creation, overwrite strategy).
        *   Task: Implement documented error handling (`InvalidLineNumber`, `BackupCreation`, `WriteError`, etc.) for `insert_code_snippet`.
        *   Task: Write comprehensive unit tests for `insert_code_snippet`.

3.  **Phase 3: Service Integration & API Implementation (Sprints 2-4)**
    *   **Milestone:** Tools integrated with Orchestrator via defined interface.
    *   **Milestone:** `/chat` API endpoint implemented, calling Orchestrator.
    *   **Milestone:** Basic Gemini client connected and making calls.
    *   **Steps:**
        *   Task: Implement `Tool Executor` module that uses the Tool Interface (AOA collab).
        *   Task: Implement basic `Gemini Client` service module.
        *   Task: Implement core Orchestration service logic skeleton (AOA collab).
        *   Task: Implement `/chat` endpoint in `api/endpoints.py` using Pydantic models from API contract.
        *   Task: Integrate API endpoint with Orchestration service.
        *   Task: Write integration tests for API -> Orchestrator -> Mocked Tool flow.
        *   Task: Implement logging with correlation IDs throughout services.

4.  **Phase 4: End-to-End Integration & Polish (Sprints 4-5)**
    *   **Milestone:** Backend fully functional for MVP workflows.
    *   **Steps:**
        *   Task: Integrate real tool implementations with Orchestrator.
        *   Task: Work with VSCode Extension dev on resolving API integration issues.
        *   Task: Implement required metrics logging.
        *   Task: Refine error handling based on integration testing.
        *   Task: Create/update `README.md` with setup and run instructions.

**Initial Thoughts/Concerns:**
*   Ensuring adequate time for writing *good* unit tests for the file I/O tools, covering edge cases.
*   Workspace path validation logic needs to be robust and well-tested early on.
*   Smooth integration with the VSCode extension requires the API contract to be stable and well-understood by both sides. 