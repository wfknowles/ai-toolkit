# Project Manager - Pre-Analysis & Concepts (Cursor Rules)

**Based on:** Ensuring development aligns with project plans, tracking work items, managing scope and dependencies, facilitating team communication, and adhering to project processes.

**Goal:** Propose Cursor rules that integrate AI assistance with project management practices, enforce process adherence, and improve visibility into AI-driven development activities.

**Initial Concepts (7 Rules):**

1.  **Rule: Require Task Association for Edits:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant, before applying significant code changes (e.g., >N lines, adding new files), to prompt the user to associate the change with a task/ticket ID (linking to PO-1), if not already provided in the initial request.
    *   **Rationale:** Ensures code changes are traceable back to specific work items.
2.  **Rule: Estimate Complexity/Effort for AI Tasks:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, when asked to generate a new feature or perform a complex refactoring, to provide a *rough, qualitative* estimate of the complexity (e.g., Simple, Moderate, Complex) or potential time involved, based on the request and context. Remind the user this is a rough estimate.
    *   **Rationale:** Helps users gauge the potential scope of AI-generated work for planning purposes.
3.  **Rule: Reference Project Documentation Standards:**
    *   **Level:** Project
    *   **Description:** Define project documentation standards (e.g., location of READMEs, ADR format, code commenting standards - linking to SSE-3). Instruct the AI assistant to follow these standards when generating documentation or reminding users to update docs (PO-4).
    *   **Rationale:** Maintains consistency in project documentation.
4.  **Rule: Identify Cross-Team Dependencies:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant, when modifying code related to APIs or shared libraries defined by another team (requires project structure/ownership info), to flag the potential cross-team dependency and remind the user to coordinate with the relevant team.
    *   **Rationale:** Improves awareness and management of inter-team dependencies.
5.  **Rule: Align AI Suggestions with Sprint Goals:**
    *   **Level:** Project/User
    *   **Description:** Allow defining current sprint goals or focus areas (e.g., "Focus on bug fixes in module X", "Implement feature Y"). Instruct the AI assistant to prioritize suggestions or refactorings that align with these goals and potentially deprioritize unrelated major changes.
    *   **Rationale:** Helps keep AI assistance focused on current project priorities.
6.  **Rule: Generate Standard Commit Messages:**
    *   **Level:** Project/User
    *   **Description:** Instruct the AI assistant, when suggesting commit messages for generated changes, to follow a predefined project format (e.g., Conventional Commits) and automatically include the associated ticket ID (from Rule 1 or PO-1).
    *   **Rationale:** Ensures consistent and informative version control history.
7.  **Rule: Check for Environment Configuration Consistency:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant, when generating code that relies on environment variables or configuration files, to check against a defined project template (e.g., `.env.example`, `config/defaults.yml`) and remind the user if necessary configuration seems missing or inconsistent.
    *   **Rationale:** Helps prevent environment-specific issues during development and deployment. 