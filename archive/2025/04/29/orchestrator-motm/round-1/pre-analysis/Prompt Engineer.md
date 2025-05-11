# Prompt Engineer - Pre-Analysis (Orchestrator Framework)

**Concept:** AI Tool Integration Framework for File I/O.

**Initial Thoughts:**
*   **Tool Definitions:** How detailed do the JSON Schema/OpenAPI definitions need to be for the model to understand the confirmation workflow of `edit_file`? Need to clearly document the two-stage nature (propose -> confirm -> execute).
*   **Error Handling Prompts:** How should the orchestrator instruct the model when a tool call fails (e.g., access denied, execution error, user rejection)? Model needs clear signals to generate appropriate user messages.
*   **Clarity of Confirmation:** How can prompts clearly explain to the user *why* confirmation is needed for `edit_file`? 