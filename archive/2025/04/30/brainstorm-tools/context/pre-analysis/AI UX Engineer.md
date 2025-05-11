# AI UX Engineer - Initial Context Management Concepts

Focusing on the user's interaction context and managing context within the AI interface:

1.  **Implicit Context Capture:** Designing AI interfaces that automatically capture relevant context from the user's actions within the application (e.g., current screen, selected data, recent operations) to pre-fill prompts or suggest relevant actions.
2.  **Conversation History Summarization for UI:** Displaying a concise, AI-generated summary of the ongoing conversation or task context within the UI, helping users maintain orientation during multi-turn interactions.
3.  **Context Clarification Prompts:** Designing prompts that the AI uses to proactively ask the user clarifying questions when the provided context is ambiguous or insufficient, rather than making assumptions.
4.  **User-Editable Context Panel:** Providing a UI panel where users can explicitly view, add, remove, or edit the context being used by the AI for the current task, giving them transparency and control.
5.  **Visualizing Context Sources:** If context is pulled from multiple places (e.g., RAG from documents, database info), visually indicating the source of information used in the AI's response to build trust and aid verification.
6.  **Context Persistence Strategies:** Defining how context is persisted across sessions or related tasks (e.g., short-term memory for current task, long-term memory for user preferences/history) and making this behaviour clear to the user.
7.  **Contextual Affordances:** Designing UI elements (e.g., buttons, suggestions) that appear dynamically based on the current context, guiding users towards relevant AI-powered actions.
8.  **Graceful Handling of Missing Context:** Designing AI responses and UI feedback for situations where necessary context is unavailable or couldn't be retrieved, guiding the user on how to provide it.
9.  **Feedback Mechanisms for Context Relevance:** Including UI elements allowing users to easily provide feedback on whether the context used by the AI (especially retrieved context like RAG) was relevant and helpful for the generated response. 