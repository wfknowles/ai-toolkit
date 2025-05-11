# Product Owner - Pre-Analysis & Concepts (Cursor Rules)

**Based on:** Ensuring AI assistance aligns with product goals, user stories, acceptance criteria, and overall product vision. Maintaining focus on delivering user value and adhering to feature requirements.

**Goal:** Propose Cursor rules that help align AI-generated code and suggestions with specific product requirements, user stories, and feature goals.

**Initial Concepts (7 Rules):**

1.  **Rule: Link to User Story/Ticket Context:**
    *   **Level:** User/Project
    *   **Description:** Encourage or require users to link their AI requests (especially for new features or bug fixes) to a specific user story or ticket ID (e.g., `For RW-4394:`). Instruct the AI assistant to reference the linked ticket (if accessible via a tool/API) to understand requirements, acceptance criteria, and context.
    *   **Rationale:** Ensures AI assistance is grounded in specific requirements and project tracking.
2.  **Rule: Prioritize Acceptance Criteria Adherence:**
    *   **Level:** Project
    *   **Description:** Instruct the AI assistant, when generating code for a feature linked to a user story (see Rule 1), to explicitly review the acceptance criteria (if available in the context or linked ticket) and prioritize generating code that meets those criteria.
    *   **Rationale:** Helps ensure AI-generated features meet the defined requirements for completion.
3.  **Rule: Validate Against Feature Requirements:**
    *   **Level:** Project/User
    *   **Description:** Instruct the AI assistant, after generating a feature or modification, to perform a self-check: "Does this code meet the core requirements outlined in the prompt/linked ticket [Ticket ID]? Specifically, does it achieve [Requirement 1], [Requirement 2]?"
    *   **Rationale:** Encourages the AI to verify its output against the product goals.
4.  **Rule: Suggest User-Facing Documentation Updates:**
    *   **Level:** Project/User
    *   **Description:** When the AI assistant generates changes that impact user-facing functionality or APIs, instruct it to remind the user to update relevant user documentation, help guides, or API specs, potentially suggesting draft text based on the changes.
    *   **Rationale:** Helps keep documentation synchronized with product changes.
5.  **Rule: Align with Target User Persona:**
    *   **Level:** Project
    *   **Description:** Define the target user persona(s) for the project. Instruct the AI assistant, when making suggestions about UI/UX or generating user-facing text, to consider the needs and technical expertise of this persona (complementing PE's persona rule).
    *   **Rationale:** Ensures AI contributions align with the intended user experience.
6.  **Rule: Discourage Scope Creep:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, if a user's request seems to significantly expand beyond the scope of the current task or linked ticket (Rule 1), to gently point this out and ask the user to confirm if they want to proceed or suggest creating a new ticket/task.
    *   **Rationale:** Helps keep development focused on agreed-upon scope.
7.  **Rule: Check for Feature Flag Consistency:**
    *   **Level:** Project
    *   **Description:** If the project uses feature flags, instruct the AI assistant to check if newly generated code needs to be placed behind an existing or new feature flag, based on project conventions or linked ticket information.
    *   **Rationale:** Ensures new features are deployed safely and consistently with release strategy. 