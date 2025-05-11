# Prompt Engineer - Initial Exemplar/Benchmark Usage Concepts

Focusing on incorporating exemplars directly into prompts:

1.  **Few-Shot Prompting with Exemplars:** Including one or more complete, high-quality exemplars (e.g., an exemplary bug fix commit message, a perfect unit test) directly within the prompt to guide the LLM in generating a similar output for a new task.
2.  **Exemplar Structure Emulation:** Providing an exemplar and instructing the LLM to follow its structure, style, and level of detail, but adapt the content for the current input (e.g., "Generate a design doc section for feature X following the structure of the exemplar provided for feature Y").
3.  **Exemplar-Based Quality Rubric:** Including an exemplar along with a rubric derived from it (defining key quality attributes) and asking the LLM to evaluate a *draft* output against that rubric.
4.  **Negative Exemplars (Anti-Patterns):** Providing examples of *poor* quality outputs (anti-patterns) alongside good exemplars, instructing the LLM to avoid the characteristics of the negative examples.
5.  **Exemplar Snippet Injection:** Instead of the full exemplar, injecting only the most relevant snippets or sections of a benchmark work product into the prompt based on the specific sub-task.
6.  **Chain-of-Thought with Exemplar Reference:** Prompting the LLM to perform a task using chain-of-thought reasoning, explicitly instructing it to reference and compare its intermediate steps to the patterns or logic within a provided exemplar.
7.  **Exemplar-Driven Test Case Generation:** Providing an exemplar of a well-tested function/module and asking the LLM to generate a similarly comprehensive suite of tests (covering edge cases, performance, security as seen in the exemplar) for a new piece of code.
8.  **Generating Exemplars with AI:** Using a highly detailed prompt, possibly incorporating quality standards, to have the AI generate a *new* work product intended to serve as a future benchmark exemplar.
9.  **Exemplar Comparison Prompt:** Providing two different outputs (e.g., two draft code solutions) and an exemplar, then asking the LLM to compare the drafts and evaluate which one better aligns with the quality demonstrated in the exemplar. 