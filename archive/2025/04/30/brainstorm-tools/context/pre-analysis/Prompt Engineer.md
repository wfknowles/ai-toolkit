# Prompt Engineer - Initial Context Management Concepts

Focusing on techniques within the prompt itself or simple chaining:

1.  **Structured Context Injection:** Designing prompts with clearly delineated sections (e.g., using XML tags like `<user_query>`, `<background_info>`, `<code_snippet>`, `<constraints>`) to help the LLM differentiate and prioritize parts of the context.
2.  **Context Summarization Prompt:** A preliminary prompt in a chain that takes lengthy context (e.g., long document, previous conversation) and generates a concise summary, which is then fed into the main task prompt to conserve tokens and focus the LLM.
3.  **Instructional Priming:** Using meta-instructions at the beginning of a prompt to guide the LLM on *how* to use the provided context (e.g., "Prioritize information in the `<latest_update>` section", "Cross-reference the `<user_profile>` with the `<request>`").
4.  **Role-Based Context Filtering:** Instructing the LLM to adopt a specific role and stating that it should only consider context relevant to that role, effectively filtering the provided information.
5.  **Contextual Keywords/Trigger Phrases:** Embedding specific keywords or phrases within the context that the prompt instructions explicitly reference to draw attention to critical pieces of information.
6.  **Example-Based Context Grounding (Few-Shot):** Including examples within the prompt that demonstrate *how* similar context was used to generate a desired output, guiding the LLM's use of the current context.
7.  **Negative Constraints from Context:** Explicitly stating in the prompt what the LLM *should not* do based on the provided context (e.g., "Given the `<security_policy>` context, do not suggest solutions that violate data residency requirements").
8.  **Tiered Context Relevance:** Structuring context input with labels indicating relevance (e.g., `[High Relevance]`, `[Medium Relevance]`, `[Low Relevance]`) and instructing the LLM to weight its attention accordingly.
9.  **Contextual Consistency Check Prompt:** A follow-up prompt used in a chain to verify if the LLM's output is consistent with key facts or constraints presented in the original context. It asks the LLM to self-critique its output against the context. 