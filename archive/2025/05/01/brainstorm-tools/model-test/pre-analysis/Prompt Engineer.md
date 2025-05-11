# Prompt Engineer - Pre-Analysis: AI Model Test Concepts

**Objective:** Identify tests focused on prompt understanding, instruction following, nuance handling, and output quality/controllability.

**Initial Concepts (9):**

1.  **Instruction Following Accuracy Test:** Provide complex, multi-step instructions (e.g., "Write a Python function that takes X, performs Y, formats output as Z, and includes error handling for A and B") and evaluate how accurately the model follows each constraint.
2.  **Persona Adoption Fidelity Test:** Instruct the model to adopt a specific persona (e.g., "You are a skeptical senior developer reviewing code", "You are a helpful teaching assistant") and evaluate the consistency and appropriateness of its tone, language, and focus.
3.  **Format Adherence Test:** Request output in specific formats (e.g., JSON, Markdown table with specific columns, YAML, numbered list, specific code style) and assess the model's ability to match the requested structure precisely.
4.  **Constraint Compliance Test:** Impose negative constraints (e.g., "Do not use library X," "Avoid passive voice," "Limit response to 100 words") and test if the model respects them.
5.  **Context Window Utilization Test:** Provide a large context (e.g., long document, code file) and ask questions that require synthesizing information from different parts of the context to evaluate its effective context length and recall ability.
6.  **Ambiguity Clarification Test:** Provide deliberately ambiguous or incomplete prompts and observe if the model asks clarifying questions or makes (and states) reasonable assumptions versus hallucinating or refusing.
7.  **Creative Generation & Style Transfer Test:** Request creative outputs (e.g., write a poem, generate marketing copy, suggest analogies) in different styles (e.g., formal, humorous, technical) to assess versatility and stylistic control.
8.  **Iterative Refinement Test:** Give the model feedback on its initial response (e.g., "Make it more concise," "Explain step 3 further," "Change the tone to be more empathetic") and evaluate its ability to incorporate the feedback accurately in subsequent turns.
9.  **Role & Goal Grounding Test:** Define a clear role and goal for the model within the prompt (e.g., "Your role is code reviewer, your goal is to find potential bugs") and see how well its responses stay grounded in that defined objective across multiple interactions. 