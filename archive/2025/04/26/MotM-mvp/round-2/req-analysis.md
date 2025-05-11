# MVP Build Plan Analysis (Round 2)

**Date:** 2025-04-26

**Version:** 1.0

**Authors:** Prompt Engineer, AI Orchestrator/Architect, Senior Software Engineer, Principal Architect, Product Owner, Project Manager, AI UX Engineer, AI Agent Engineer

**Facilitator:** AI Assistant

**Prerequisites:** Round 1 Analysis (`/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/04/26/MotM/round-1/analysis.md`)

## 1. Introduction

Following the initial concept refinement and MVP definition in Round 1, this document details the outcome of Round 2 of the Meeting of the Minds process. The objective of Round 2 was to move from the *what* (the MVP scope) to the *how* – defining the specific assets, strategies, methodologies, and workflows required to successfully develop and deliver the Minimum Viable Product (MVP) of the local agentic AI application.

The MVP, as defined in Round 1, consists of a Python/FastAPI backend using Gemini Pro via function calling, a simple ReAct agent, reliable `read_file` and insertion-only `edit_file` tools, basic active-file context awareness, and a VSCode extension UI, all prioritizing reliability as the core value proposition.

This round focused on translating that scope into actionable definitions and plans across all relevant disciplines (prompt engineering, architecture, software engineering, product management, UX design, agent engineering).

## 2. Methodology

Round 2 followed a similar methodology to Round 1:

1.  **Prerequisite Review:** All SME personas reviewed the outputs of Round 1 (`analysis.md`, `sme-group-interview.md`).
2.  **Individual Pre-Analysis (R2):** Each persona identified the key assets, strategies, methodologies, and workflows needed from their perspective to build the MVP. Saved in `MotM/round-2/pre-analysis/`.
3.  **Facilitator Pre-Planning (R2):** The facilitator synthesized the R2 pre-analyses to identify areas needing further definition and prepare for interviews.
4.  **Individual Interviews (R2):** The facilitator conducted interviews with each persona to add detail and rigor to the proposed assets and strategies. Saved in `MotM/round-2/sme-interviews/`.
5.  **Facilitator Pre-Planning (R2 - Part 2):** The facilitator synthesized R2 interview findings, identified consensus points, and pinpointed remaining open questions/decisions.
6.  **Meeting of the Minds (R2 Group Discussion):** A group meeting finalized key decisions, refined definitions, and gathered requirements/ACs/guidelines for the MVP build. Saved in `MotM/round-2/sme-group-interview.md`.
7.  **Asset Creation (R2):** Compilation of requirements (`requirements.md`) and this analysis paper (`req-analysis.md`).

## 3. Defined Assets for MVP Development

The following key assets were identified and defined as necessary for MVP development:

*   **Tool Prompt Schemas (YAML/JSON or Python Source):** (PE/AE) Formal definitions for `read_file` and `insert_code_snippet` for Gemini function calling, including descriptions, parameters, types, and potentially examples. Defined in Python code (`app/tools/schemas.py`) as the single source of truth.
*   **Core Agent System Prompt (Text/Markdown):** (PE) Defines agent persona, objectives, constraints, and policies for tool usage, error handling, context usage, and response formatting. Must include specific instructions for handling documented tool errors.
*   **Orchestration Flow Diagram:** (AOA) Visualizes the ReAct loop, data flow, tool calls, and error paths within the orchestrator.
*   **Tool Interface Definition (Code - ABC/Protocol):** (AOA/SSE) Defines the standard interface (`execute`, `ToolResult`) used by the orchestrator to interact with tool implementations.
*   **`requirements.txt` / `pyproject.toml`:** (SSE) Lists pinned versions of all backend dependencies (FastAPI, Google SDK, `aiofiles`, `pytest-asyncio`, etc.).
*   **`Dockerfile`:** (SSE) Multi-stage Dockerfile for building the backend service container image.
*   **Tool Implementation Code (`tools/file_io.py`):** (SSE) Concrete Python implementation of `read_file_async` and `insert_code_snippet_async`, including backup logic, specific error raising, path validation, and async I/O.
*   **API Endpoint Definition (Code - `api/endpoints.py`):** (SSE) FastAPI code defining `/chat`, `/health` endpoints and their Pydantic request/response models.
*   **API Contract Definition (OpenAPI Spec):** (PA/SSE) Formal OpenAPI specification for the backend API, auto-generated from FastAPI code where possible.
*   **Basic Project Structure (Directories):** (SSE/PA) Defined initial directory layout for backend code (`/app`, `/tests`) following common conventions.
*   **MVP Feature List & Acceptance Criteria:** (PO) Formal list of MVP features with clear, testable ACs, particularly detailed for `insert_code_snippet` reliability.
*   **Key User Workflows (MVP Document):** (PO/UXE) Step-by-step descriptions of the primary user workflows (Code Q&A, Code Gen & Insert) from the user perspective.
*   **Wireframes/Mockups (VSCode Extension UI):** (UXE) Visual designs for the chat webview, including the critical `insert_code_snippet` preview and confirmation flow.
*   **Prioritized Post-MVP Feature List (Draft):** (PO) Living document outlining potential future features/improvements.
*   **Project Backlog (Initial Draft):** (PM) Epics, User Stories, and initial Tasks derived from the MVP features/ACs, managed in a tool (Jira/GitHub Projects).
*   **Sprint 0 Plan:** (PM) Goals and tasks for the initial setup sprint (API contract, repo setup, CI, etc.).
*   **Risk Management Log (Updated):** (PM) Tracking identified risks (technical, resource, schedule) and mitigation strategies.

## 4. Defined Strategies for MVP Development

Key strategic approaches were agreed upon:

*   **Context Management Strategy (MVP):** (AOA) Context derived from active VSCode file/selection, passed via API, formatted by `Context Prepper` in backend, included directly in LLM prompt.
*   **Error Handling Strategy (Orchestrator & Agent):** (AOA/PE/AE) Tools raise specific errors -> Orchestrator catches, standardizes into `ToolResult`, passes to Agent -> Agent (guided by System Prompt) analyzes error, informs user, attempts recovery (e.g., asks clarification).
*   **Interface Definitions Strategy:** (PA/AOA) Use explicit Python Protocols/ABCs for internal interfaces (Orchestrator <-> Tools/LLM Client) to enforce contracts and aid testing.
*   **Logging Standards:** (PA) Standardize on Python `logging`, structured JSON format, include correlation ID per request, log key events, avoid sensitive data by default.
*   **Security Standards (MVP):** (PA/SSE) Secure API Key handling, workspace path validation via startup config, least privilege execution, plan for security review.
*   **Configuration Management Approach:** (SSE/PA) Use Pydantic Settings loading from env vars / `.env` file for backend config.
*   **Reliability Metrics Definition:** (PO) Track key metrics like `insert_code_snippet` success rate; use for debugging and guiding refinement.
*   **Tool Parameter Parsing & Validation Strategy:** (AE) Orchestrator performs basic type/sanity checks on LLM parameters; tool implementation performs definitive validation.
*   **Backup File Strategy:** (SSE/PO) Create `.bak` file before `insert_code_snippet`; keep the *last* `.bak` file per modified file (overwrite previous on next edit).
*   **API Authentication Strategy (MVP):** (PA/PO) No authentication between local extension and local backend for MVP.
*   **Backend Discovery Strategy:** (SSE/PA) Use a default fixed port (e.g., 8000) for the backend service.

## 5. Defined Methodologies for MVP Development

Core development processes and methodologies were established:

*   **Prompt Versioning & Evaluation:** (PE) Simple filename versioning; manual review of prompt performance against golden test cases for MVP.
*   **Modular Design Implementation:** (AOA) Structure backend code into distinct modules with clear responsibilities and DI.
*   **Unit Testing Strategy:** (SSE) Use `pytest` + `pytest-asyncio`. Focus on tool logic. Mock external dependencies (filesystem, APIs). Test success, errors, edge cases. Aim for >80% coverage on critical code.
*   **Integration Testing Strategy:** (AE/Test Eng) Verify end-to-end agent flows (tool choice, parameter correctness, response quality) for key workflows.
*   **Agile Methodology:** (PM) Scrum/Kanban with 1-2 week sprints, standard ceremonies (Standup, Planning, Review, Retro).
*   **Agile Estimation:** (PM) Story points at user story level; break down stories into tasks for sprint planning.
*   **Definition of Done (DoD):** (PM) Checklist including code implemented, tests pass, reviewed, meets ACs, locally runnable.
*   **Code Review Process:** (PM) Mandatory PRs with at least one reviewer approval.
*   **User Feedback Collection Plan (Initial):** (PO/UXE) Simple in-app mechanism (thumbs up/down), informal internal usability testing during development.
*   **Tech Debt Management:** (PA) Acknowledge MVP simplifications (RAG, agent logic) as tech debt; track via `TODO`s or backlog items.
*   **Communication Plan:** (PM) Defined channels (Chat, Standups, Syncs, Demos, Backlog Tool).
*   **CI/CD Pipeline (Basic):** (PM/SSE) Setup in Sprint 0 (e.g., GitHub Actions) to automatically run tests on PRs.
*   **State Management (MVP):** (AOA/AE) Pass conversation history explicitly via API request/prompt; log token counts and implement simple truncation if needed.

## 6. Defined Workflows for MVP Development

Critical operational workflows were detailed:

*   **Prompt Design for Tool Reliability:** (PE) Focus on structured parameter generation, potentially requesting explanation before action.
*   **Error Handling Prompting:** (PE) Define agent response based on specific documented tool errors.
*   **Orchestration Flow (ReAct):** (AOA/AE) Detailed flow from user request through context prep, LLM calls (potentially multiple for tool use), tool execution, and response generation.
*   **Handling Tool Execution Results:** (AE/AOA) Orchestrator formats `ToolResult` into function response for Gemini.
*   **UX Design for `insert_code_snippet`:** (UXE) Specific workflow from trigger (button click) through preview, confirmation, backend execution, feedback, and potential Undo.
*   **Setup/Configuration Workflow:** (UXE/SSE) Define simple steps for user installation, API key entry, and verifying backend connection.
*   **Sprint 0 Workflow:** (PM) Finalize API, setup repo, CI, structure, Docker, dependencies, groom Sprint 1 backlog.

## 7. Outstanding Questions & Next Steps from Round 2

While Round 2 significantly detailed the build plan, a few minor items remain or require immediate follow-up:

*   **VSCode Undo API Investigation:** Task assigned to SSE/Extension Dev to confirm feasibility.
*   **Tool Error Documentation:** SSE to formally document specific errors raised by tools.
*   **Error Handling Prompt Implementation:** PE/AE to implement prompt logic based on documented errors.
*   **Detailed Backlog Refinement:** PM to break down defined assets/strategies into Sprint 1 tasks.
*   **Test Engineer Onboarding:** PM to prioritize bringing Test Engineer onto the team.
*   **Security Review Scheduling:** PM to schedule review once initial components are drafted.
*   **Metric Implementation:** Decide *how* metrics (e.g., success rate) will be logged/tracked.

## 8. Conclusion

Round 2 successfully transitioned the project from a defined MVP scope to a concrete, actionable build plan. Key assets, strategies, methodologies, and workflows have been defined across all disciplines. Critical decisions regarding implementation details, error handling, testing, and process were made collaboratively. While minor implementation details and investigations remain, the team has established a shared, detailed understanding of *how* the MVP will be constructed, focusing on the core principles of reliability and user trust. The outputs of this round, particularly the `requirements.md` compilation, provide the necessary foundation for commencing Sprint 0 and initiating development work. 