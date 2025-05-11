# Prompt Engineer - Initial Analysis

**Core Concept:** Build a local, Gemini-powered agentic application, starting small and focusing on reliability, especially regarding custom tools like file I/O.

**Initial Thoughts:**

1.  **Gemini Interaction:**
    *   Need to evaluate different Gemini models (e.g., Pro vs. Ultra variants) for capability vs. cost/latency trade-offs, especially for complex agentic tasks.
    *   Context window management will be crucial for maintaining conversation history and providing relevant file context to the model. Strategies for summarizing or selecting relevant context snippets will be needed.
    *   Prompt templating and versioning are essential for managing the complexity of prompts for different tasks (e.g., code generation, RAG, tool use).

2.  **Tool Definition & Usage:**
    *   The reliability issues mentioned with Cursor's tools highlight the importance of extremely clear and robust tool definition prompts for Gemini.
    *   Prompts instructing the model *how* and *when* to use custom tools (`read_file`, `edit_file`, terminal interaction) need careful design and testing. This includes specifying expected input/output formats and error handling.
    *   Need strategies for handling potential tool execution failures within the prompt flow – can the agent recover or ask for clarification?

3.  **Agentic Workflows:**
    *   Consider prompt chaining or multi-turn prompt strategies to implement basic agentic workflows (e.g., read file -> analyze -> suggest edit -> apply edit).
    *   How will prompts guide the model in planning sequences of actions?

4.  **Evaluation:**
    *   Need methods to evaluate the quality and reliability of the model's responses and tool usage based on different prompt designs.

**Key Questions:**
*   What specific limitations of Gemini models (latency, context, tool use reliability) might impact the design?
*   How can we design prompts that make tool use as deterministic and reliable as possible?
*   What level of detail is required in prompts to ensure safe and effective file system and terminal interaction? 