# Interview: AI Agent Engineer

**Facilitator:** Welcome. Your analysis covered agent design patterns (ReAct), tool integration via function calling, interaction with the orchestrator, RAG, and reliability. Let's refine this for the MVP.

**Facilitator:** You recommended a ReAct agent for the MVP. Concretely, how does Gemini's function calling fit into this? Does the LLM directly output the function call, or does it output a "Reasoning" step first?

**AI Agent Engineer:** With Gemini's function calling, the typical ReAct flow adapts slightly. 
1.  **Prompt:** The orchestrator sends the user query, conversation history, RAG context (if any), and the schemas of available tools (`read_file`, simplified `edit_file`, maybe `query_rag`) to Gemini.
2.  **Reason/Act (Combined):** Instead of explicitly outputting a "Reason: I need to read the file. Action: call `read_file`...", Gemini's response might directly include a function call request if it determines a tool is needed. The reasoning is implicit in its choice to call the function.
3.  **Orchestrator Action:** The orchestrator receives the response. If it contains a function call request, it executes the corresponding tool (e.g., our backend's `read_file` implementation).
4.  **Observation/Response:** The orchestrator sends the tool's output back to Gemini in a subsequent turn (as a function response). Gemini then uses this output to generate the final response to the user.
So, the LLM's "Act" is requesting the function call; the orchestrator performs the actual execution.

**Facilitator:** How crucial are well-defined tool schemas for reliable function calling, especially for the simplified `edit_file` (insertion)? What details must be included?

**AI Agent Engineer:** Absolutely crucial. The schema *is* the primary way the LLM understands the tool. For `edit_file` (insertion MVP):
*   **Function Name:** Clear and descriptive (e.g., `insert_code_snippet`).
*   **Function Description:** Explain its exact purpose: "Inserts a given block of code into a specified file at a specific line number. Use only for inserting new code, not for replacing existing code."
*   **Parameters:**
    *   `file_path` (string, required): Description: "The relative or absolute path to the file to modify."
    *   `line_number` (integer, required): Description: "The line number *before* which the code should be inserted."
    *   `code_snippet` (string, required): Description: "The exact block of code to insert. Include necessary indentation."
*   **Type Hinting:** Use accurate types (string, integer, boolean). Provide enums if there are fixed choices.
Accuracy and clarity here directly impact whether the LLM can generate valid parameters and call the function correctly.

**Facilitator:** What strategies should the agent (or the orchestrator guiding it) use to handle failed tool executions, like `edit_file` failing because the line number is invalid?

**AI Agent Engineer:** The orchestrator receives the error from the tool. It should then:
1.  **Format Error:** Package the error message clearly (e.g., "Tool execution failed: `edit_file` reported error: Invalid line number specified.").
2.  **Send to Agent:** Pass this error message back to the Gemini model as the function response/observation.
3.  **Prompt for Recovery:** The prompt guiding the LLM should instruct it on how to handle errors. Examples:
    *   "If a tool call fails, analyze the error message. If it's resolvable (e.g., invalid path), inform the user and ask for correction. If it's a more complex failure, inform the user about the error."
    *   "If `edit_file` fails due to an invalid line number, inform the user and perhaps ask them to confirm the insertion point."
The goal is to let the LLM attempt to recover gracefully or, failing that, clearly report the issue to the user, rather than just stopping silently.

**Facilitator:** Regarding RAG integration, how does the agent decide *when* to query RAG versus using conversation history? For the MVP's basic RAG, how might this work?

**AI Agent Engineer:** For a basic MVP:
*   **Implicit Context:** The orchestrator might automatically retrieve context from the currently open/active file(s) and include it in the prompt sent to the agent/LLM alongside the user query. The agent doesn't explicitly decide to query RAG; it just uses the context provided.
*   **Explicit Query (Optional MVP+):** We could have a simple `query_workspace` tool. The agent (prompted appropriately) could decide to call this tool if the user asks a question that seems likely answerable from the workspace files and isn't in the immediate conversation history. The prompt would need guidance like: "If the user asks about code in their project not present in the history, consider using `query_workspace`."
For MVP, the implicit context approach is simpler and likely sufficient.

**Facilitator:** What are the simplest agentic workflows to target for the MVP, focusing on the reliable tools (`read_file`, simple `edit_file`)?

**AI Agent Engineer:** Aligning with the Product Owner:
1.  **File Q&A:** User asks question -> Agent uses provided context (implicitly via `read_file`/RAG) -> Agent answers.
2.  **Code Generation & Insertion:** User asks for code -> Agent generates code -> User confirms -> Agent calls `insert_code_snippet` -> Orchestrator executes -> Agent confirms success.
3.  **Explain Code:** User selects code -> Agent uses context -> Agent explains.
These involve primarily `read_file` (implicitly or explicitly) and the simplified `insert_code_snippet`, testing the core reliable components.

**Facilitator:** Any blindspots from an agent implementation perspective?

**AI Agent Engineer:** A potential blindspot is **managing the state** between turns effectively, especially if tool calls fail or require clarification. Ensuring the LLM receives the correct history, context, and error messages to make informed decisions in the next turn is critical and easy to get wrong. Another is **overly complex prompts** – trying to make the agent handle too many edge cases in a single prompt can become brittle. Iterative prompt refinement based on testing will be key.

**Facilitator:** Other SMEs needed?

**AI Agent Engineer:** Strong agreement on needing a **Test Engineer**. The interaction between the LLM's function calling requests, the orchestrator's interpretation, the tool's execution, and the response sent back to the LLM is a complex flow that needs rigorous testing beyond simple unit tests.

**Facilitator:** That gives a clear picture of the agent implementation. Thanks. 