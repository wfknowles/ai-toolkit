# Phase 6 (Round 2): Meeting of the Minds - Defining the MVP Build Plan

**Attendees:** Facilitator, Prompt Engineer (PE), AI Orchestrator/Architect (AOA), Senior Software Engineer (SSE), Principal Architect (PA), Product Owner (PO), Project Manager (PM), AI UX Engineer (UXE), AI Agent Engineer (AE)

**Facilitator:** Welcome back, team. Round 1 defined the MVP scope. Round 2 pre-analysis and interviews focused on *how* we build it – the specific assets, strategies, and workflows. Let\'s synthesize this, make key decisions, and define the necessary components to start development.

**(Part 1: Review & Confirm Refined Definitions)**

**Facilitator:** Interviews added detail to many areas. Let\'s quickly confirm understanding on key refinements:
*   Tool Schemas: Python code as single source, include Examples for Gemini.
*   System Prompt: Explicit error handling instructions per error type.
*   Prompt Evaluation: Manual review of golden test cases for MVP.
*   Orchestration: Simple context formatter, standardized `ToolResult` object, orchestrator reports errors but agent recovers, pass history for state.
*   Implementation: Pinned deps, multi-stage Dockerfile, specific exceptions in tools, standard project structure, async testing patterns, path validation via workspace root config.
*   API: Core `/chat`, `/health` endpoints, OpenAPI spec, Pydantic models for requests (incl. history, context).
*   UX: Detailed insertion preview, recommend UI framework (React/Vue), investigate native Undo, implicit context display, clear error messages, simple setup UX.
*   Agent: Use Python tool schemas, parse function calls robustly, handle latency concerns, test tool choice/params.
*   Process: API spec in Sprint 0, lightweight code review, updated risk log, CI pipeline in Sprint 0, need Test Eng/Security review.

*(Pause for brief confirmations/clarifications from team - Assume general agreement)*

**Facilitator:** Okay, excellent alignment on the detailed definitions.

**(Part 2: Key Decisions)**

**Facilitator:** Let\'s address the open decision points from the interviews.

**Facilitator:** First, **Backup File Cleanup** for `insert_code_snippet`. SSE suggested keeping the last `.bak` file for a slightly longer safety net. PO, UXE, any concerns? Or delete immediately on success?

**UXE:** Keeping the last `.bak` feels safer initially, especially if Undo isn\'t native. It supports a potential manual recovery if needed.
**PO:** Agreed. The small risk of disk space filling (unlikely locally) is outweighed by the user trust benefit of having that last backup. Let\'s keep the last `.bak` per file for MVP.
**SSE:** Okay, we can implement logic to overwrite the previous `.bak` on the next successful edit to the same file.
**Facilitator:** Decision: Keep last `.bak` file per modified file.

**Facilitator:** Next, **History Management**. AE noted potential context window limits. For MVP, we agreed to pass history. Do we set a simple truncation limit now? E.g., last N turns?

**AE:** Starting without a hard limit but *logging* token counts per call seems reasonable. If logs show we\'re hitting limits frequently during testing, we implement simple truncation (e.g., last 10-15 turns) then.
**AOA:** Agree. Avoid premature optimization. Log token counts first, implement truncation if proven necessary.
**PM:** Okay, plan is log first, implement truncation (e.g., last 10-15 turns) if needed based on logs. Add logging task to backlog.
**Facilitator:** Decision: Log token counts; implement simple turn-based truncation if needed.

**Facilitator:** **MVP API Authentication.** AOA raised potentially adding a simple API key passed from extension to backend, even if local. Thoughts?

**PA:** Minimal security benefit locally if both run as the same user, adds slight complexity to setup/config.
**SSE:** Agree, probably unnecessary for MVP if communication is purely localhost.
**PO:** Let\'s keep it simple for MVP. No API auth between local extension and local backend.
**Facilitator:** Decision: No API authentication for MVP.

**Facilitator:** **Backend Discovery.** PA asked how the extension finds the backend. Fixed port?

**SSE:** Easiest for MVP is assuming a fixed default port (e.g., `localhost:8000`) for the backend service.
**UXE:** We need clear instructions for the user if the port is configurable or if they need to ensure it\'s available.
**PA:** Default fixed port is fine. Make it configurable via env var eventually, but default works for MVP.
**Facilitator:** Decision: Use a default fixed port (e.g., 8000) for backend service.

**(Part 3: Defining Key Components & Requirements)**

**Facilitator:** Now let\'s add flesh to the bones, defining the component parts and their requirements, ACs, guidelines as per Phase 6, Step 5 & 6.

*(Iterative discussion follows, gathering details for each key asset/strategy/workflow identified in R2 Pre-Analysis & Interviews. Example snippets below)*

**Facilitator:** Okay, **Tool: `insert_code_snippet`**. We have ACs from PO. SSE, any specific implementation guidelines beyond backup/error handling?

**SSE:** Guideline: Must handle UTF-8 encoding. Guideline: Workspace path validation must be strictly enforced. Guideline: Log parameters (file path, line num, snippet length - not content), success/failure, and duration.

**Facilitator:** **Strategy: Logging Standards**. PA mentioned JSON, correlation ID. Specific requirements?

**PA:** Requirement: All logs must be valid JSON. Requirement: Every log entry associated with an API request must include the unique `correlation_id` generated for that request. Requirement: Log levels (INFO, WARN, ERROR) must be used appropriately. Guideline: Avoid logging sensitive data (API keys, full code snippets) by default.

**Facilitator:** **Methodology: Unit Testing**. We have scope/tools. Acceptance Criteria?

**SSE:** AC: Unit tests must cover success paths for core tool logic. AC: Unit tests must cover documented error conditions (e.g., file not found, invalid line). AC: Mocks must be used for external dependencies (filesystem, Gemini API). Guideline: Aim for reasonable code coverage (e.g., >80%) for critical modules like `tools`.

**Facilitator:** **Asset: API Contract (OpenAPI Spec)**. Requirements?

**PA:** Requirement: Spec must define request/response models for `/chat` and `/health`. Requirement: Models must align with Pydantic definitions used in FastAPI. Guideline: Include clear descriptions for endpoints and models. AC: Spec should be auto-generated from code where possible and kept up-to-date.

**Facilitator:** **UX Design: Insertion Preview**. Requirements?

**UXE:** Requirement: Preview must show filename, target line number, code snippet, and surrounding context lines. Requirement: Preview must require explicit user action (button click) to proceed with insertion. AC: Preview should be rendered accurately and quickly.

*(Continue this process for other key components: System Prompt structure, Orchestration Flow, Config Management, CI Pipeline goals, Error Handling definitions, Key User Workflows, etc., gathering requirements, ACs, and guidelines for each)*

**(Part 4: Final Review & Next Steps)**

**Facilitator:** We\'ve defined the core components, strategies, and standards for building the MVP in detail, including requirements and guidelines. Does everyone feel we have a clear enough definition to proceed with Sprint 0/1?

**PM:** Yes, this provides the necessary clarity for detailed backlog refinement and starting implementation.
**PO:** Agreed, the ACs and workflow definitions capture the MVP goals.
**PA/SSE/AOA/AE/PE/UXE:** *(General agreement)*

**Facilitator:** Excellent. I will compile these definitions, requirements, ACs, and guidelines into the `requirements.md` master list as per Phase 7. The next step is for the PM to finalize the Sprint 0 plan and detailed backlog based on this discussion. 