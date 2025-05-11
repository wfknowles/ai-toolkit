# Senior Software Engineer - Round 2 Pre-Analysis

**Based on Round 1 Analysis:** Agreed on Python/FastAPI backend, Docker, SQLite (if needed), focus on reliable `read_file` / `insert_code_snippet` (insertion only), DI for testing, async handling. `terminal` deferred.

**Initial Assets/Strategies/Methodologies/Workflows Needed:**

1.  **Asset: `requirements.txt` / `pyproject.toml`:**
    *   Initial list of core dependencies (FastAPI, Uvicorn, Pydantic, Google AI Python SDK, `aiofiles`, potentially `python-dotenv`).
    *   *Strategy:* Pin dependency versions for reproducible builds.

2.  **Asset: `Dockerfile`:**
    *   Defines the container image build process.
    *   *Strategy:* Use official Python base image, copy requirements, install dependencies, copy application code, define entry point (e.g., `uvicorn main:app`). Multi-stage build for smaller final image.

3.  **Asset: Tool Implementation Code (`tools/file_io.py`):**
    *   Initial implementation of `read_file_async` and `insert_code_snippet_async`.
    *   *Strategy:* Use `aiofiles` for async file access. Implement robust error handling (try/except blocks for `FileNotFoundError`, `PermissionError`, `IOError`, custom `InvalidLineNumberError`). Implement backup mechanism for `insert_code_snippet`. Focus on clear return values/exceptions.

4.  **Asset: API Endpoint Definition (Code - `api/endpoints.py`):**
    *   Define FastAPI endpoints (e.g., `/chat`, `/agent/invoke`).
    *   *Strategy:* Use Pydantic models for request/response validation. Define clear API contracts for interaction with the VSCode extension (including how context is passed).
    *   *Workflow:* Endpoint receives request -> Calls orchestration service -> Returns response.

5.  **Methodology: Unit Testing Strategy:**
    *   *Strategy:* Use `pytest`. Focus unit tests on tool logic (`tools/`), utility functions, and potentially orchestrator logic components.
    *   *Methodology:* Mock external dependencies (filesystem using `pyfakefs` or similar, Gemini API calls using `unittest.mock`). Test success paths, expected error handling paths, edge cases (empty files, end-of-file insertion).

6.  **Methodology: Configuration Management:**
    *   *Strategy:* Use Pydantic Settings to load config (e.g., Gemini API Key) from environment variables or a `.env` file.
    *   *Workflow:* Access configuration via injected Settings object.

7.  **Asset: Basic Project Structure (Directories):**
    *   Define initial directory layout (e.g., `/app`, `/app/api`, `/app/core` (orchestration), `/app/services` (llm client), `/app/tools`, `/app/models` (pydantic), `/tests`).

**Initial Thoughts/Concerns:**
*   Need the exact API contract defined quickly to unblock VSCode extension development.
*   Handling file paths reliably (relative vs. absolute, ensuring they stay within workspace boundaries for security) needs careful implementation in tools.
*   Ensuring async/await is used correctly throughout the FastAPI stack to avoid blocking.
*   Setting up secure handling for the Gemini API key. 