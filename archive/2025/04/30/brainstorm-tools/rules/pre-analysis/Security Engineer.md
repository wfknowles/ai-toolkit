# Security Engineer - Pre-Analysis & Concepts (Cursor Rules)

**Based on:** Implementing technical security controls, validating security posture, automating security checks within the development workflow, and ensuring AI tools don't introduce new vulnerabilities.

**Goal:** Propose Cursor rules that directly enforce technical security controls, integrate security testing tools, and guide AI code generation to avoid common vulnerabilities.

**Initial Concepts (7 Rules):**

1.  **Rule: Mandate Dependency Vulnerability Checks:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant, when adding or updating dependencies, to automatically run a vulnerability scan (e.g., `pip-audit`, `npm audit`, Snyk CLI) on the updated dependencies and report high/critical severity vulnerabilities to the user.
    *   **Rationale:** Integrates supply chain security checks directly into the AI-assisted workflow.
2.  **Rule: Enforce Use of Secure Coding Libraries:**
    *   **Level:** Project
    *   **Description:** Define project-approved secure libraries for common vulnerable operations (e.g., XML parsing, SQL querying, encryption). Instruct the AI assistant to always use these approved libraries instead of potentially insecure alternatives when generating relevant code.
    *   **Rationale:** Guides AI towards using vetted, secure components for high-risk operations.
3.  **Rule: Disallow Insecure TLS/SSL Configurations:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant to avoid generating code that configures TLS/SSL connections with known weak protocols (e.g., SSLv3, TLS 1.0/1.1) or ciphers. It should default to strong, current standards.
    *   **Rationale:** Prevents introduction of weak encryption configurations.
4.  **Rule: Input Validation Pattern Enforcement:**
    *   **Level:** Project
    *   **Description:** Define project-specific patterns or approved libraries for input validation (e.g., using a specific regex library, standard validation functions). Instruct the AI assistant to use these approved patterns when generating code that handles external input.
    *   **Rationale:** Enforces consistent and robust input validation practices, reducing injection risks.
5.  **Rule: Secure File Handling Practices:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant, when generating code that performs file I/O, to follow secure practices like validating file paths (preventing path traversal), checking permissions, and handling file exceptions properly.
    *   **Rationale:** Prevents common file handling vulnerabilities.
6.  **Rule: Run Security Linter on Generated Code:**
    *   **Level:** User/Project
    *   **Description:** After generating or modifying code, instruct the AI assistant to automatically run the configured security linter (CISO-2) on the affected code block or file and report any new findings.
    *   **Rationale:** Provides immediate feedback on potential security issues introduced by the AI.
7.  **Rule: Check for Secrets in Proposed Changes:**
    *   **Level:** User/Project
    *   **Description:** Before applying code changes, instruct the AI assistant to perform a quick scan (e.g., using regex patterns or tools like `gitleaks`) on the diff to check for accidentally introduced secrets (API keys, passwords, tokens) and warn the user if any are found (complementing CISO-5 on generation).
    *   **Rationale:** Acts as a safety net to catch secrets accidentally pasted or generated in code edits. 