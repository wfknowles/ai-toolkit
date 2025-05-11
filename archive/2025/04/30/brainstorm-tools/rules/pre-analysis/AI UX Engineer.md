# AI UX Engineer - Pre-Analysis & Concepts (Cursor Rules)

**Based on:** Ensuring AI interactions are intuitive, efficient, trustworthy, and consistent with good UX principles. Managing user expectations and preventing AI-induced friction in the development workflow.

**Goal:** Propose Cursor rules that shape the AI assistant's interaction patterns, communication style, and generated outputs to align with best practices for user experience and developer productivity.

**Initial Concepts (7 Rules):**

1.  **Rule: Control AI Proactiveness Level:**
    *   **Level:** User
    *   **Description:** Allow the user to configure how proactive the AI assistant is with suggestions (e.g., "Minimal", "Balanced", "Proactive"). For instance, limit unsolicited refactoring suggestions (SSE-4) or context gathering (SSE-7) if the user prefers less interruption.
    *   **Rationale:** Tailors AI interaction frequency and style to user preference, reducing potential annoyance.
2.  **Rule: Standardize AI Clarification Prompts:**
    *   **Level:** User/Project
    *   **Description:** Define standard, concise phrasing for when the AI needs to ask clarifying questions (PE-4). Ensure questions are specific and provide clear options if possible, avoiding overly verbose or open-ended requests.
    *   **Rationale:** Makes AI requests for clarification efficient and easy for the user to respond to.
3.  **Rule: Tone and Style Guide for AI Responses:**
    *   **Level:** User/Project
    *   **Description:** Define a preferred tone and style for the AI assistant's chat responses (e.g., "Concise and technical", "Slightly conversational", "Formal"). Instruct the AI to adhere to this style guide.
    *   **Rationale:** Creates a more consistent and potentially more pleasant user interaction experience.
4.  **Rule: Summarize Large Code Changes:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, before applying a large or complex code change, to provide a brief, bulleted summary of the intended modifications in the chat for user review.
    *   **Rationale:** Improves user understanding and confidence before accepting significant AI-generated changes.
5.  **Rule: Offer Incremental Changes:**
    *   **Level:** User
    *   **Description:** For complex refactoring or feature generation tasks, instruct the AI assistant to offer breaking down the changes into smaller, incremental steps that the user can review and apply sequentially.
    *   **Rationale:** Makes large changes less overwhelming and easier to validate.
6.  **Rule: Manage Expectations on AI Capabilities:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, when asked to perform tasks known to be outside its capabilities or prone to error (e.g., predicting runtime performance perfectly, guaranteeing bug-free complex logic), to gently preface its response by stating its limitations regarding that specific task.
    *   **Rationale:** Helps manage user expectations and prevents over-reliance on AI for tasks it cannot reliably perform.
7.  **Rule: Consistency Check for UI/Text Generation:**
    *   **Level:** Project
    *   **Description:** If the project has defined UI component names, text styles, or terminology (e.g., in a design system reference file), instruct the AI assistant to reference these standards when generating UI code or user-facing text to ensure consistency.
    *   **Rationale:** Maintains consistency in the application's look, feel, and language. 