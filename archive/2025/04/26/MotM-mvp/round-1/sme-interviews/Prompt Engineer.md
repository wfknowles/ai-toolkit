# Interview: Prompt Engineer

**Facilitator:** Thanks for joining. Based on your pre-analysis, you highlighted Gemini model selection, context management, tool prompting, and agentic workflows. Let's dive deeper.

**Facilitator:** You mentioned evaluating different Gemini models. For an MVP focused on reliable file I/O and basic code tasks within a local app, would a Pro model likely suffice, or are there specific agentic functions where Ultra's capabilities might be essential even early on?

**Prompt Engineer:** For the MVP, Gemini Pro should be sufficient. The core tasks – understanding user requests, triggering basic tools like `read_file`, and generating code snippets or edits based on provided context – fall well within its capabilities. Latency and cost are also favorable with Pro for a local application. We'd only *need* Ultra if the agent required significantly more complex reasoning, planning across many steps, or understanding extremely nuanced instructions right out of the gate, which seems beyond the MVP scope.

**Facilitator:** Context window management is key. Beyond standard summarization, what specific prompt strategies can we use to help Gemini effectively utilize large file contexts or conversation histories without exceeding limits or losing crucial information?

**Prompt Engineer:** Several strategies: 
1.  **Chunking & Selection:** Instead of feeding the whole file, use prompts to ask the LLM *what sections* of a file are relevant based on the user query, then feed only those chunks (using the `read_file` tool perhaps).
2.  **Summarization with Keywords:** Maintain a running summary of the conversation, but also extract key entities, filenames, or task goals mentioned, reinforcing them in subsequent prompts.
3.  **Structured Context:** Format the context provided in the prompt clearly, using markdown or XML tags to delineate conversation history, file snippets, tool outputs, etc. This helps the model parse it effectively.
4.  **Instruction Priming:** Explicitly instruct the model in the prompt on *how* to use the provided context (e.g., "Refer to the file `example.py` snippet provided below to answer the user's question.").

**Facilitator:** You emphasized robust tool definition prompts. What specific elements should we include in the prompts defining `read_file`, `edit_file`, and `terminal` to maximize reliability and minimize ambiguity for Gemini?

**Prompt Engineer:** Crucial elements include:
*   **Clear Description:** Explain exactly what the tool does and *when* it should be used. For `edit_file`, stress its purpose (e.g., applying specific changes, inserting code) and potential risks.
*   **Parameter Definition:** Precisely define each parameter (name, type, description, required/optional). For `edit_file`, parameters defining *what* change to make (e.g., line numbers, content to insert/replace, diff format) need extreme clarity.
*   **Input/Output Examples:** Provide few-shot examples within the prompt showing typical inputs and expected outputs or confirmation messages.
*   **Error Handling Guidance:** Instruct the model on what constitutes a successful execution versus an error, and potentially suggest how the model should react to errors (e.g., "If the file is not found, inform the user and ask for the correct path.").
*   **Security Caveats:** Especially for `edit_file` and `terminal`, include explicit warnings about potential side effects and perhaps instruct the model to always seek user confirmation via a specific mechanism before proposing its use.

**Facilitator:** Regarding `edit_file`'s reliability issues in Cursor – from a prompting perspective, do you think the failures stem more from the LLM misinterpreting the *request* or from the tool's execution logic itself? How can prompts mitigate the former?

**Prompt Engineer:** It's likely a combination, but prompts can definitely mitigate misinterpretation. Failures could stem from ambiguous user requests leading the LLM to formulate a poor edit instruction, or the LLM correctly understanding but formulating the tool call parameters incorrectly. Better prompts help by: 
1.  **Forcing Structure:** Prompt templates that require the LLM to break down the edit request into specific components (file, target lines, type of change, content) before constructing the tool call.
2.  **Requesting Confirmation:** Prompting the LLM to *first* explain the change it intends to make and *then* generate the tool call, allowing for an intermediate check.
3.  **Simplification:** Instructing the LLM to favor simpler, more atomic edits if possible, rather than complex multi-part changes in a single tool call.

**Facilitator:** You mentioned prompt chaining for workflows. For a simple workflow like "read file -> analyze -> suggest edit", how would you structure the prompts to pass information effectively between steps?

**Prompt Engineer:** The output of one step becomes context for the next. 
*   **Step 1 (User Request):** "Please read `config.yaml` and tell me how to change the port number to 8080."
*   **Step 2 (Agent Action):** LLM decides to use `read_file('config.yaml')`. Output is the file content.
*   **Step 3 (Agent Prompt - Internal):** "Context: User wants to change port to 8080. File `config.yaml` content: [content from read_file]. Analyze the content and determine the exact change needed. Then, formulate the parameters for the `edit_file` tool to make this change."
*   **Step 4 (Agent Action):** LLM responds with the analysis and the proposed `edit_file` parameters. This might be shown to the user for confirmation before execution.
Essentially, the prompt explicitly carries forward the goal and the relevant data gathered so far.

**Facilitator:** Any blindspots in the current concept from a prompt engineering perspective? Are we missing any key considerations?

**Prompt Engineer:** One potential blindspot is the **evaluation of prompt effectiveness**. We need a systematic way to test different prompt strategies for the tools and agent workflows, measuring not just task success but also reliability, tendency for hallucination, and efficiency. Another is **prompt security** – ensuring user inputs don't manipulate the agent's core instructions (prompt injection), especially relevant if we allow terminal access.

**Facilitator:** Based on this concept, are there any other SMEs you think should be involved in future rounds?

**Prompt Engineer:** Given the focus on reliability and potential complexity of `edit_file` and terminal interaction, perhaps a dedicated **Software Test Engineer** with experience in testing complex integrations and edge cases would be valuable. Also, if security becomes a major focus for the terminal, a **Security Engineer**.

**Facilitator:** Excellent points. Thank you for your insights. 