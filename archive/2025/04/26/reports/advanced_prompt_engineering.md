# Advanced Prompt Engineering Report: Capabilities, Conventions, and Patterns

**Date:** 2025-04-26
**Context:** Exploring techniques beyond basic instructions, inspired by observations during the MotM Workflow MVP development.
**Contributing Perspectives:** Prompt Engineer, AI Orchestrator/Architect, Senior Software Engineer, Principal Architect, AI UX Engineer, AI Agent Engineer.

## 1. Introduction: Beyond Simple Instructions

The MotM workflow demonstrated that prompts can go beyond simple Q&A or text generation. They can act as instruction sets for complex, multi-step processes involving state management, tool use, and structured data handling. The observation about instructing an action *like* `json.loads` hints at a broader capability: using natural language within prompts to direct the execution environment and the LLM's reasoning capabilities to perform tasks analogous to programming functions or control flow structures. This report explores these "unknown unknowns," conventions, accessible capabilities, and advanced patterns.

## 2. The Nature of Prompt "Execution" (Senior Software Engineer Perspective)

It's crucial to understand that a `.prompt` file doesn't *execute* code in the traditional sense. Instead:

1.  **The Prompt Instructs:** The prompt provides detailed instructions (often in natural language, structured with Markdown) to an **Execution Environment**.
2.  **The Environment Acts:** This environment (e.g., the backend infrastructure of Cursor, running Python, Node.js, Go, etc.) is responsible for:
    *   Parsing the prompt instructions.
    *   Calling the appropriate LLM with the relevant parts of the prompt and context.
    *   Providing **Tools** (like `read_file`, `edit_file`, `web_search`) as callable functions/APIs.
    *   Providing underlying **Capabilities** (like the ability to parse JSON, manipulate strings, perform basic logic based on LLM output).
3.  **The LLM Reasons & Responds:** The LLM processes the instructions and context, performs reasoning, generates text, and importantly, formulates requests to use the available Tools or signals data/status back to the Environment based on the prompt's instructions.

Therefore, when we talk about "invoking JSON parsing" or "looping" within a prompt, we're instructing the *Environment* and the *LLM's reasoning process* to achieve that outcome, leveraging the Environment's underlying capabilities.

## 3. Prompting Conventions Beyond Basic Instructions (Prompt Engineer Perspective)

Beyond simple requests, several conventions enhance clarity and capability:

*   **Invoking Conceptual Functions:** As seen with the `json.loads` example, you can instruct the LLM/Environment to perform standard data operations.
    *   **JSON/Data Parsing:** "Parse the following string, which should be valid JSON: [string]. Extract the value of the 'status' field."
    *   **List/String Manipulation:** "Take the following list of filenames: [list]. Filter out any filename that does not end with '.md'." or "Read the text from [file]. Convert it all to lowercase."
    *   **Text Analysis:** "Analyze the sentiment of the following text: [text]. Respond with 'positive', 'negative', or 'neutral'."
    *   **Example:**
        ```prompt
        # Goal: Extract error messages from a list of step results

        # Input: A JSON string representing partial state.step_results
        step_results_json_string = """
        {
          "step-01": {"status": "success", "error_message": ""},
          "step-02": {"status": "error", "error_message": "File not found."},
          "step-03": {"status": "success", "error_message": ""}
        }
        """

        # Instructions:
        1. Parse the step_results_json_string into a structured object.
        2. Iterate through each step result in the object.
        3. If a step's status is "error", extract its "error_message".
        4. Collect all extracted error messages into a list.
        5. Respond ONLY with a JSON object containing a single key "error_list" holding the collected list of error messages.

        # Expected Output Format Example:
        # { "error_list": ["File not found."] }
        ```
*   **Structured Input/Output:** Clearly define input variables within the prompt (using placeholders or examples) and demand specific output structures (often JSON or Markdown tables) using explicit instructions and examples. This makes prompt chaining reliable.
*   **Role/Persona Adoption:** Crucial for focusing the LLM's expertise. `Act as a Senior Software Engineer...`
*   **Using Delimiters:** Use Markdown fences (```), XML tags (`<input>`, `<instructions>`), or other clear delimiters to separate instructions, input data, examples, and expected output formats within the prompt. This helps the LLM parse the request accurately.
*   **Chain-of-Thought (CoT):** Instruct the LLM to "think step-by-step" or "show its reasoning" before providing the final answer, especially for complex problems. This often improves accuracy.

## 4. Accessible Capabilities via Prompt Instructions (Senior Software Engineer & Prompt Engineer Perspectives)

Through carefully crafted prompts, you can instruct the LLM/Environment to leverage capabilities analogous to programming libraries or functions:

*   **Text Analysis & Manipulation:** Summarization, extraction (named entity recognition, keyword extraction), translation, reformatting (e.g., text to bullet points), sentiment analysis. These rely heavily on the LLM's core language understanding.
*   **Data Structuring & Transformation:** Instructing the LLM to convert unstructured text into structured formats like JSON or Markdown tables, based on rules provided in the prompt.
*   **Logical Reasoning & Problem Solving:** Leveraging the LLM's ability to perform logical deduction, constraint satisfaction, and basic mathematical reasoning (though complex math often requires a specific tool).
*   **Code Generation & Analysis:** Instructing the LLM to write code snippets, explain code, identify bugs (within its capabilities), or translate code between languages.
*   **Tool Usage:** This is critical. Instructing the prompt's *execution environment* (via the LLM formulating the request) to use available tools (`read_file`, `edit_file`, `web_search`, `run_terminal_cmd`, etc.). The prompt needs to specify *when* to use a tool, *what inputs* to provide (e.g., filename, search query), and *how to handle* the tool's output.

**Important Note:** You are not directly calling Python libraries *from* the prompt text. You are writing natural language instructions that the LLM interprets, causing the execution environment to use its *own* underlying implementations (which might be Python libraries, internal APIs, etc.) to fulfill the request or call the specified external tools.

## 5. Advanced Orchestration Patterns (AI Orchestrator/Architect & Principal Architect Perspectives)

Beyond the simple sequential `STEP_ORDER` in our MotM MVP, more advanced orchestration can be defined within an Orchestrator Prompt:

*   **Conditional Branching:** Instruct the orchestrator to choose the `next_step_id` based on the `status` or specific `output_data` from the previous step.
    *   **Example Instruction:** "If the status of the previous step ('code_review') was 'success', the next_step_id is 'deploy_staging'. If the status was 'error', the next_step_id is 'notify_developer' and update overall_status to 'error'."
*   **Looping / Iteration:** Explicitly instruct the orchestrator to repeat a specific step or sequence of steps based on a condition or for each item in a list retrieved from state.
    *   **Example Instruction:** "Retrieve the `sme_list` from `shared_data`. For each `sme_persona` in `sme_list`: set `shared_data.current_sme_persona = sme_persona`, set `next_step_id = 'step-04-r1-sme-interviews.prompt'`, execute the step, and store the result before proceeding to the next SME. Only after iterating through all SMEs, set `next_step_id = 'step-05-r1-facilitator-plan-group.prompt'." (This requires more complex state tracking within the orchestrator logic).
*   **State Machines:** Define the workflow as a set of states and transitions within the orchestrator prompt. The orchestrator's main job becomes determining the current state and executing the transition logic (which might involve calling a step).
*   **Error Handling & Retry Logic:** Define specific instructions for different error types. "If `step-09` fails with status 'error' and error_message contains 'timeout', retry the step up to 2 times. If it fails otherwise, set overall_status to 'error' and proceed to Finalization."
*   **Dynamic Context Injection:** Instead of passing all `shared_data` or `step_results`, instruct the orchestrator to intelligently select *only* the necessary pieces of context required by the *specific* next step, based on predefined needs for that step.
*   **Meta-Prompts / Self-Modification (Highly Advanced):** Prompts that generate or refine *other* prompts within the workflow, potentially adapting the workflow based on intermediate results.

## 6. Agentic Patterns via Prompts (AI Agent Engineer & Principal Architect Perspectives)

These patterns often involve shorter loops where the LLM decides the next action, potentially involving tool use:

*   **ReAct (Reason + Act):** Structure the prompt to instruct the LLM to follow a cycle:
    1.  **Observation:** Receive current state/goal/previous action result.
    2.  **Thought/Reasoning:** Analyze the observation and determine the best next action to achieve the goal (e.g., "I need the content of file X to answer the user's question").
    3.  **Action:** Formulate a request to use a specific tool (e.g., `read_file(target_file='fileX.txt')`) or generate a response.
    4.  The environment executes the action (calls the tool) and provides the result back as the next Observation.
    *   **Example Prompt Snippet:** "Given the Goal and current Observation, first output your Thought process for the next action. Then, output the Action itself, which must be either calling one of the available tools [Tool list] with correct parameters, or providing the final answer to the user. Format the action as required by the tool."
*   **Plan-and-Execute:**
    1.  **Planning Prompt:** An initial prompt takes the overall goal and instructs the LLM to generate a step-by-step plan (potentially using specific tools).
    2.  **Execution Orchestrator:** A separate orchestrator (or the same one in a different mode) takes the generated plan and executes each step, potentially calling other prompts or tools.
*   **Reflection/Self-Correction:** After a step or tool use, instruct the LLM to evaluate the result against the original goal or criteria. "Review the generated summary. Does it address all key points from the input document? If not, identify the missing points and regenerate the summary."

## 7. Understanding "Tools" (`read_file`, etc.) (Senior Software Engineer & AI Orchestrator/Architect Perspectives)

This was a source of confusion and is critical:

*   **Environment Capability:** Tools like `read_file`, `edit_file`, `web_search`, `run_terminal_cmd` are **capabilities provided by the execution environment** (e.g., the Cursor platform). They are functions or APIs made available *to* the LLM agent running within that environment.
*   **LLM's Role:** The LLM itself (Gemini, Claude, GPT-4, etc.) does **not** inherently possess the ability to directly read files or browse the web. Its role is to *understand the prompt's instructions* and the current context, and then *decide when to ask the environment* to use one of its available tools. It formulates a *request* for tool use, usually in a specific format the environment understands (often JSON).
*   **Platform Dependency:** The specific tools available, their reliability, and their exact behavior are **features of the platform (Cursor)**, not the underlying LLM model selected.
*   **Model vs. Platform QA:**
    *   If a tool like `edit_file` fails consistently (as observed), it points towards an issue with:
        1.  The **platform's implementation** of that tool.
        2.  The **assistant's internal logic** failing to correctly *invoke* the tool (as hypothesized in the incident report).
        3.  The **LLM failing to correctly *format the request*** for the tool (less likely if it worked previously and the prompt structure was consistent).
    *   Switching the underlying LLM (e.g., from Claude 3.7 to Gemini 2.5 Pro) *might* help if the failure was due to the specific LLM consistently misinterpreting the prompt and failing to generate the correct tool request (point 3 above), or if one model is better at managing complex state leading to the invocation failure (point 2). However, it *won't* fix underlying bugs in the platform's tool implementation (point 1).
    *   Therefore, the `edit_file` issues we encountered are **most likely platform/tooling issues or assistant execution logic issues**, not something fundamentally tied to the choice of LLM model itself, although model choice *can* sometimes influence the likelihood of triggering such issues.

## 8. Conclusion

Prompt engineering for complex workflows moves beyond simple instructions into the realm of architectural design. By leveraging conventions like structured I/O, conceptual function invocation, and applying patterns like modularity, state management, conditional logic, looping, and agentic reasoning (ReAct, Plan-and-Execute), prompts can define sophisticated, automated processes. Understanding the distinct roles of the prompt (instructions), the LLM (reasoning and tool request formulation), and the execution environment (providing capabilities and tools) is key to both designing robust systems and effectively troubleshooting failures. Mastery involves applying these software engineering principles within the prompt-based paradigm.
