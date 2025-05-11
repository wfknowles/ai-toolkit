# Senior Software Engineer - Pre-Analysis & Concepts (Cursor Rules)

**Based on:** Promoting code quality, maintainability, testability, adherence to coding standards, and efficient debugging practices, especially when leveraging AI assistance.

**Goal:** Propose Cursor rules that help maintain high code quality standards, encourage best practices in testing and documentation, and ensure AI-generated code is clean, readable, and maintainable.

**Initial Concepts (7 Rules):**

1.  **Rule: Enforce Code Style & Formatting:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant to always format generated or modified code according to the project's configured formatter (e.g., Black, Prettier) and adhere to linting rules (e.g., PEP 8, ESLint rules defined in the project).
    *   **Rationale:** Maintains consistent code style across human and AI contributions.
2.  **Rule: Mandate Unit Test Generation:**
    *   **Level:** Project/User
    *   **Description:** When the AI assistant generates new functions or significant logic changes, instruct it to also generate corresponding unit tests (using the project's preferred testing framework) or remind the user to do so.
    *   **Rationale:** Encourages test coverage and ensures AI-generated code is testable.
3.  **Rule: Require Docstrings/Comments for Generated Code:**
    *   **Level:** Project/User
    *   **Description:** Instruct the AI assistant to include clear docstrings (following project standards, e.g., Google style, NumPy style) for any new functions or classes it generates, and add comments for complex or non-obvious logic.
    *   **Rationale:** Improves code readability and maintainability.
4.  **Rule: Complexity Analysis & Refactoring Suggestions:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, when analyzing or modifying code, to identify overly complex functions or modules (e.g., based on cyclomatic complexity heuristics) and proactively suggest refactoring approaches to simplify them.
    *   **Rationale:** Helps manage technical debt and improve code quality.
5.  **Rule: Guide Error Handling Practices:**
    *   **Level:** Project
    *   **Description:** Define project standards for error handling (e.g., specific exception types, logging requirements for errors, avoiding empty catch blocks). Instruct the AI assistant to follow these standards when generating code that involves error handling.
    *   **Rationale:** Ensures consistent and robust error handling.
6.  **Rule: Optimize Imports:**
    *   **Level:** Project/User
    *   **Description:** Instruct the AI assistant to automatically clean up imports in modified files (e.g., remove unused imports, sort imports according to project standards like isort) after applying changes.
    *   **Rationale:** Keeps code clean and avoids import-related issues.
7.  **Rule: Cross-Reference Related Code/Tests:**
    *   **Level:** User
    *   **Description:** When the user is working on a specific function or module, instruct the AI assistant to proactively identify and offer to add related files to the context, such as corresponding unit tests, usage examples elsewhere in the codebase, or relevant interface definitions.
    *   **Rationale:** Improves developer context awareness and aids navigation. 