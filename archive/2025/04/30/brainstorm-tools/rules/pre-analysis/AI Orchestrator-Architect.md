# AI Orchestrator/Architect - Pre-Analysis & Concepts (Cursor Rules)

**Based on:** Maintaining architectural consistency, promoting design patterns, managing dependencies across a large codebase, and ensuring AI code generation aligns with architectural principles.

**Goal:** Propose Cursor rules that guide AI code generation towards architecturally sound patterns, enforce project structure conventions, and help manage system-wide dependencies.

**Initial Concepts (7 Rules):**

1.  **Rule: Enforce Preferred Architectural Patterns:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant, when generating new modules or features, to adhere to specific architectural patterns defined for the project (e.g., "Use dependency injection for services", "Follow CQRS pattern for read/write separation", "Implement new features using microservices communicating via event bus").
    *   **Rationale:** Ensures AI-generated code fits the established system architecture.
2.  **Rule: Guide Module/Directory Structure:**
    *   **Level:** Project
    *   **Description:** Define the standard directory structure for different types of components (e.g., controllers, models, services, utils). Instruct the AI assistant to place newly generated files in the correct location according to this structure.
    *   **Rationale:** Maintains consistency and navigability of the codebase.
3.  **Rule: Discourage Circular Dependencies:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant to analyze potential circular dependencies when adding imports or generating code that links modules. If a circular dependency might be created, warn the user or suggest alternative structures.
    *   **Rationale:** Helps prevent common architectural pitfalls that hinder maintainability.
4.  **Rule: Promote Use of Platform Libraries/SDKs:**
    *   **Level:** Project
    *   **Description:** When generating code for common tasks (e.g., logging, database access, API calls), instruct the AI assistant to prioritize using established internal platform libraries or SDKs (like the Secure Tool SDK or KB Client Lib from previous brainstorms) over implementing custom solutions or using external libraries directly.
    *   **Rationale:** Encourages code reuse, consistency, and leverages centrally managed/secured components.
5.  **Rule: Specify API Design Conventions:**
    *   **Level:** Project
    *   **Description:** Define project-specific API design conventions (e.g., RESTful principles, naming conventions, standard error formats, OpenAPI spec usage). Instruct the AI assistant to follow these conventions when generating API endpoints or client code.
    *   **Rationale:** Ensures consistency and interoperability of APIs within the system.
6.  **Rule: Identify Deprecated Component Usage:**
    *   **Level:** Project
    *   **Description:** Maintain a list or pattern for deprecated modules, classes, or functions. Instruct the AI assistant to warn the user if it generates code that uses deprecated components and suggest current alternatives.
    *   **Rationale:** Helps phase out old code and prevents technical debt accumulation.
7.  **Rule: Contextual Architecture Diagram Reference:**
    *   **Level:** Project
    *   **Description:** Allow linking high-level architecture diagrams or documentation (e.g., in `@docs/architecture.md`). Instruct the AI assistant to reference this documentation when asked architectural questions or when generating code that impacts core system interactions, potentially summarizing relevant sections.
    *   **Rationale:** Provides the AI with architectural context to generate more informed and consistent code. 