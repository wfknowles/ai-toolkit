# Prompt Engineer - Pre-Analysis & Concepts (Cursor Rules)

**Based on:** Ensuring prompt clarity, consistency, effectiveness, and potentially enforcing security/privacy constraints through prompt structure or meta-instructions for the AI assistant within Cursor.

**Goal:** Propose Cursor rules that guide the user and/or the AI assistant towards constructing better, safer, and more effective prompts, potentially leveraging prompt templates or predefined instructions.

**Initial Concepts (7 Rules):**

1.  **Rule: Mandate Persona Usage in Prompts:**
    *   **Level:** User/Project
    *   **Description:** Require prompts (especially for complex tasks like code generation or refactoring) to include a specific `Persona:` tag (e.g., `Persona: Senior Python Developer`). Instruct the AI assistant to adopt this persona for its response style and technical depth.
    *   **Rationale:** Improves consistency and quality of AI responses by setting clear expectations.
2.  **Rule: Enforce Structured Prompt Formats:**
    *   **Level:** User/Project
    *   **Description:** Define a required structure for certain types of requests (e.g., bug fixing requests must include `## Problem`, `## Code Snippet`, `## Expected Behavior`, `## Actual Behavior`). Instruct the AI assistant to request missing sections if the structure isn't followed.
    *   **Rationale:** Ensures sufficient context is provided for effective AI assistance, reducing back-and-forth.
3.  **Rule: Contextual Prompt Templates:**
    *   **Level:** Project
    *   **Description:** Define project-specific prompt templates for recurring tasks (e.g., writing unit tests, generating documentation, refactoring according to project style). Allow users to invoke these templates easily (e.g., `@template/unit-test`).
    *   **Rationale:** Speeds up common tasks and ensures consistency with project standards.
4.  **Rule: Discourage Ambiguous Instructions:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, when encountering highly ambiguous user prompts (e.g., "fix this code", "make it better"), to actively ask clarifying questions about the desired outcome, constraints, or specific issues before proceeding.
    *   **Rationale:** Reduces wasted effort from the AI acting on unclear instructions and improves result quality.
5.  **Rule: Inject Project-Specific Constraints:**
    *   **Level:** Project
    *   **Description:** Automatically prepend or append project-specific constraints or guidelines to relevant AI prompts. Examples: "Always use functional components in React.", "Adhere to PEP 8.", "Do not use external libraries not listed in pyproject.toml."
    *   **Rationale:** Ensures AI-generated code aligns with project standards without requiring the user to repeat them.
6.  **Rule: Optimize Context Selection Strategy:**
    *   **Level:** User/Project
    *   **Description:** Define rules for how context (e.g., `@`-files, open tabs) is selected or prioritized for the AI prompt. E.g., "Prioritize files mentioned explicitly.", "Limit context to X tokens.", "Exclude `node_modules` unless explicitly added."
    *   **Rationale:** Improves relevance of context provided to the AI and manages token limits.
7.  **Rule: Privacy Filtering for Prompt Context:**
    *   **Level:** User/Project
    *   **Description:** Instruct the AI assistant (or a pre-processing step) to identify and potentially mask or remove PII (names, emails, specific IDs) detected within the user's prompt or selected context files *before* sending to the LLM, complementing CISO's rule on sensitive file exclusion.
    *   **Rationale:** Adds a layer of defense against accidental leakage of PII within prompts/context. 