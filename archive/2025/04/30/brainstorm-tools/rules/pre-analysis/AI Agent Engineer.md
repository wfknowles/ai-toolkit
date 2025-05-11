# AI Agent Engineer - Pre-Analysis & Concepts (Cursor Rules)

**Based on:** Understanding AI/LLM limitations, promoting effective AI collaboration patterns, ensuring AI actions are explainable and controllable, and leveraging AI for complex reasoning tasks.

**Goal:** Propose Cursor rules that optimize the AI assistant's reasoning process, improve its ability to handle complex tasks, and ensure its behavior is predictable and understandable to the developer.

**Initial Concepts (7 Rules):**

1.  **Rule: Explicitly State AI Assumptions:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, when making significant assumptions to fulfill a request (e.g., about intended functionality, library choices, implicit requirements), to explicitly state these assumptions in its response.
    *   **Rationale:** Makes the AI's reasoning transparent and allows the user to correct invalid assumptions early.
2.  **Rule: Chain-of-Thought for Complex Problems:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, when faced with a complex problem (e.g., debugging a multi-component issue, designing a new algorithm), to explicitly outline its step-by-step reasoning process (Chain-of-Thought) before presenting the final solution.
    *   **Rationale:** Improves the reliability of complex problem-solving and allows the user to follow the AI's logic.
3.  **Rule: Request Feedback on Ambiguous Choices:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, if it identifies multiple valid approaches or solutions to a problem with different tradeoffs, to present the options and briefly explain the tradeoffs, asking the user for their preference before proceeding.
    *   **Rationale:** Engages the user in the decision-making process for subjective choices, leading to better outcomes.
4.  **Rule: Limit Scope of AI Edits:**
    *   **Level:** User/Project
    *   **Description:** Define rules to limit the scope of AI-generated edits by default (e.g., "Only edit the selected code region", "Only edit the current file unless explicitly asked"). Require user confirmation for edits spanning multiple files or large sections.
    *   **Rationale:** Prevents unintended widespread changes and gives the user more control over AI modifications.
5.  **Rule: Self-Correction Instruction:**
    *   **Level:** User
    *   **Description:** Instruct the AI assistant, if the user indicates a previous response was incorrect or unsatisfactory (e.g., via feedback or explicit statement), to analyze the previous turn, acknowledge the error, and attempt to correct its approach or understanding before trying again.
    *   **Rationale:** Encourages the AI to learn from feedback within the conversation context.
6.  **Rule: Specify Tool Usage Strategy:**
    *   **Level:** Project/User
    *   **Description:** Define preferred strategies for tool usage, if the AI has access to tools (e.g., "Prefer using the knowledge base search tool before web search", "Always ask for confirmation before using file system tools").
    *   **Rationale:** Guides the AI's agentic behavior involving external tools towards desired patterns.
7.  **Rule: Contextual Knowledge Base Querying:**
    *   **Level:** Project/User
    *   **Description:** Instruct the AI assistant to automatically query a project-specific knowledge base (if configured, see previous brainstorm) when encountering project-specific terms, acronyms, or components it doesn't recognize, before asking the user for clarification.
    *   **Rationale:** Leverages project knowledge proactively to improve AI understanding and reduce user interruptions. 