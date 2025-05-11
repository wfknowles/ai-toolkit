# Interview (Round 2): Prompt Engineer

**Facilitator:** Welcome back. Your R2 pre-analysis defined key prompt assets (schemas, system prompt) and methodologies (versioning, evaluation, reliability workflows). Let's flesh these out.

**Facilitator:** For the Tool Prompt Schemas (YAML/JSON), besides name, description, params, what other fields might be useful for Gemini, especially for `insert_code_snippet`?

**Prompt Engineer:** We should definitely include concrete **Examples** within the schema if the API supports it. Showing Gemini an example of a valid `insert_code_snippet` call (with realistic path, line number, and snippet) can significantly improve its ability to generate correct parameters. Also, for parameters like `line_number`, reinforcing constraints in the description (e.g., \"Must be a positive integer within the file bounds\") is helpful.

**Facilitator:** The Core Agent System Prompt needs sections on Tool Usage, Error Handling, Context Usage, and Formatting. Can you elaborate on the *content* of the Error Handling Policy section? What specific instructions should it contain for MVP errors like `FileNotFoundError` or `InvalidLineNumberError`?

**Prompt Engineer:** The Error Handling Policy needs to be explicit:
*   **General:** \"If a tool call results in an error, do not proceed with the original task. Analyze the error message provided. Your primary goal is to inform the user clearly and help them resolve the issue if possible.\"
*   **Specific (`FileNotFoundError` on `read_file` or `insert_code_snippet`):** \"If the error indicates the file was not found, state this clearly to the user (e.g., \'I couldn\'t find the file specified at path [path].\') and ask them to verify the file path or provide the correct one.\"
*   **Specific (`InvalidLineNumberError` on `insert_code_snippet`):** \"If the error indicates an invalid line number was provided for insertion, inform the user (e.g., \'The insertion failed because line number [number] seems to be outside the valid range for file [path].\') and ask them to confirm or specify the correct line number for insertion.\"
*   **Specific (`PermissionError`):** \"If the error indicates a lack of permissions to read or write the file, inform the user about the permission issue for the specific file (e.g., \'I don\'t have permission to access or modify [path]. Please check the file permissions.\')\"
*   **General Failure:** \"If the error is generic or unclear, report that the operation failed and provide the error message received to the user for context (e.g., \'Sorry, I encountered an unexpected issue while trying to [action]. Error: [error message]\').\"
We need to map the errors documented by SSE to these kinds of instructions.

**Facilitator:** You proposed a Prompt Versioning & Evaluation methodology. For the MVP, how rigorous does evaluation need to be? Is manual review of test cases sufficient?

**Prompt Engineer:** For MVP, manual review is likely sufficient, but it needs structure. We need a defined set of \"golden\" test cases covering the key workflows (Q&A, insertion success, insertion failure due to bad line number, file not found). For each case, we manually run it with the current prompt version and check:
1.  Did the agent attempt the correct action (e.g., call `insert_code_snippet`)?
2.  Were the parameters generated correctly?
3.  Was the response to the user appropriate (especially for errors)?
We track pass/fail for each case against each prompt version. This provides a baseline measure of quality and prevents regressions as we refine prompts.

**Facilitator:** The workflow for `insert_code_snippet` involves the LLM identifying parameters and potentially explaining the change. How do we ensure the LLM reliably extracts the *correct* line number, which seems like a major challenge?

**Prompt Engineer:** This is tough. Strategies:
1.  **Explicit User Input:** Encourage the UX to allow users to explicitly specify the line number if possible, rather than relying solely on the LLM inferring it from ambiguous requests (e.g., \"put it after function X\").
2.  **Contextual Clues:** Provide the LLM with the file content (or relevant snippet) and explicitly ask it to identify the line number based on context (e.g., \"Find the line number corresponding to the end of function `foo` in the provided code\").
3.  **Structured Extraction:** Prompt the LLM to output its reasoning and the identified parameters in a structured format (like JSON) within its thought process, which might be easier to parse or validate.
4.  **Confirmation:** The UX preview showing the exact insertion location is the ultimate check. Prompting the LLM to *ask* for confirmation if it\'s uncertain about the line number could also help.
It likely requires a combination of these, plus robust backend validation.

**Facilitator:** Does the Round 1 analysis or the proposed R2 assets/strategies have any blindspots from your perspective now?

**Prompt Engineer:** A potential blindspot is managing conversational context length effectively. As history grows, just appending it might exceed limits or dilute the importance of recent information. We might need a more sophisticated strategy (summarization, windowing) sooner than anticipated, even with basic RAG. Also, ensuring consistency in the agent\'s persona and tone across different scenarios (casual chat, code generation, error reporting) requires ongoing attention in the system prompt.

**Facilitator:** Any other SMEs needed for this round or future rounds?

**Prompt Engineer:** Continued close collaboration with AE and SSE is vital for aligning prompts with backend logic. The Test Engineer is crucial for validating prompt effectiveness against the evaluation cases.

**Facilitator:** Very helpful details, thank you. 