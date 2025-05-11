# IDE Integration Specification/Plugin - v1.0
## (e.g., "Our Project Prompt Assistant" for Cursor)

## 1. Introduction and Purpose

This document specifies the requirements and behavior for an IDE plugin/extension (hereinafter referred to as "the Plugin") designed to integrate with Our Project's `Dockerized Prompt Backend Service` (Component #5). The primary purpose of the Plugin is to provide developers with seamless access to the curated, standardized prompts from the `Centralized Prompt Library` (Component #2) directly within their IDE environment (initially targeting Cursor, but potentially adaptable).

The Plugin aims to:
*   Enhance developer productivity by simplifying the use of AI assistance for common coding tasks.
*   Ensure consistency and adherence to `Prompt Engineering Standards` (Component #1) by leveraging the backend service.
*   Streamline the process of providing relevant code context to AI models.
*   Provide a superior Developer Experience (DevX) for AI-assisted development.

## 2. Target IDE(s)

*   **Initial Target:** Cursor IDE
*   **Future Considerations:** VS Code (as Cursor is VS Code based, compatibility should be high), potentially other LSP-compatible editors.

## 3. Core Functionality

### 3.1 Discovering and Invoking Prompts
*   **UI Element:** The Plugin shall provide a mechanism for users to discover and invoke available prompt actions. This could be via:
    *   A dedicated view/panel within the IDE sidebar listing available prompts/templates, perhaps categorized according to the structure in the `Centralized Prompt Library`.
    *   Commands accessible through the IDE's Command Palette (e.g., "Prompt Assistant: Generate Unit Tests for Selection", "Prompt Assistant: Explain Selected Code").
    *   Context menu actions available when right-clicking in the editor or on files/folders in the explorer (e.g., "Prompt Assistant: Refactor this function...").
*   **Dynamic Loading:** The list of available prompts/actions should ideally be dynamically fetched from the `Dockerized Prompt Backend Service` (e.g., via a dedicated `/api/v1/list_prompts` endpoint) to reflect the current state of the `Centralized Prompt Library`.

### 3.2 Contextual Data Collection
*   **Automatic Context:** For many actions, the Plugin shall automatically collect relevant context from the IDE environment. This MUST include, where applicable:
    *   Currently selected text in the active editor.
    *   The entire content of the active editor file.
    *   The file path and language ID of the active file.
    *   Information about the project structure (e.g., root directory).
    *   Relevant diagnostics/linting errors for the selected code or file.
*   **User Control over Context:** The user must have clear visibility into *what* context is being collected and sent to the backend service. The Plugin should provide mechanisms for the user to:
    *   Confirm or modify the automatically collected context before sending.
    *   Manually select or provide additional context if needed.
    *   Configure default context collection preferences (See Section 5).
*   **Data Scrubbing (Client-Side Optional):** Consider implementing basic client-side checks or warnings for potentially sensitive data (e.g., simple regex for API keys) in the *user-provided* context before sending, as an additional safety layer, although primary scrubbing responsibility may lie elsewhere based on security policies.

### 3.3 Interaction with Prompt Backend Service
*   **API Calls:** The Plugin shall communicate with the `Dockerized Prompt Backend Service` via its defined API (e.g., `POST /api/v1/get_prompt`).
*   **Request Payload:** API requests will include:
    *   The ID of the selected prompt/template.
    *   The collected contextual data, structured as required by the backend API.
    *   Minimal necessary requestor information (e.g., IDE type, Plugin version, potentially a user identifier if required for auditing and permitted by privacy policy).
*   **Response Handling:** The Plugin will handle the response from the backend service, which contains the fully constructed prompt string (and potentially metadata like the prompt version used).

### 3.4 Prompt Usage and Display
*   **Display Generated Prompt:** Upon receiving the constructed prompt from the backend, the Plugin shall display it clearly to the user. Options include:
    *   Opening it in a new temporary editor tab.
    *   Displaying it in a dedicated Plugin panel or notification area.
    *   Automatically populating it into the IDE's native AI chat interface (e.g., Cursor's chat input).
*   **Facilitate Usage:** Provide convenient actions for the displayed prompt:
    *   "Copy to Clipboard" button.
    *   "Send to AI Chat" button (if integrated with IDE chat).
    *   (Future) Potentially a button to directly execute the prompt against a configured LLM API and display the result.

## 4. User Interface (UI) and User Experience (UX) Requirements

*   **Intuitiveness:** The Plugin's features should be easily discoverable and intuitive to use, minimizing disruption to the developer's existing workflow.
*   **Responsiveness:** Interactions (fetching prompts, collecting context, calling the backend) should be fast and responsive. Provide visual feedback (e.g., loading indicators) for potentially slow operations.
*   **Feedback:** Provide clear status messages, confirmation dialogs (where appropriate), and informative error messages.
*   **Consistency:** UI elements and interactions should be consistent with the host IDE's design language (e.g., use standard Cursor/VS Code UI components).
*   **Minimal Intrusion:** Avoid overly intrusive notifications or UI elements. Allow users to hide or customize the Plugin's UI components.

## 5. Configuration

The Plugin shall provide configuration options accessible through the IDE's standard settings interface (e.g., VS Code's `settings.json`). Configurable options MUST include:

*   **Backend Service URL/Port:** The address and port of the local `Dockerized Prompt Backend Service` (defaulting to `http://127.0.0.1:8000` or similar).
*   **Context Collection Preferences:** Options for users to enable/disable automatic collection of certain context types (e.g., "Always send selected code," "Never send entire file content unless confirmed").
*   **Default Prompt Display Method:** User preference for how generated prompts are displayed (e.g., "Open in new tab," "Send to Chat").
*   **(Optional) LLM API Configuration:** If the Plugin directly handles LLM calls (future scope), settings for API keys (using secure storage like IDE's secret store), endpoint URLs, and default model selection would be needed here.

## 6. Error Handling and Logging

*   **API Errors:** Gracefully handle errors from the backend service (e.g., 404 Not Found for prompt ID, 400 Bad Request for missing context, 500 Internal Server Error). Display informative messages to the user.
*   **Connection Errors:** Handle failures to connect to the local backend service and provide guidance (e.g., "Ensure the Prompt Backend Service Docker container is running").
*   **IDE Context Errors:** Handle errors during context collection gracefully.
*   **Logging:** Implement client-side logging (to the IDE's developer console or a dedicated output channel) for debugging purposes. Log levels should be configurable. Avoid logging sensitive context data in verbose logs.

## 7. Security Considerations

*   **Localhost Communication:** Ensure API calls are made securely to the intended localhost endpoint. Validate SSL certificates if HTTPS is used locally (though less common for pure localhost).
*   **Context Privacy:** Be transparent with the user about what context is being sent. Adhere to user configuration regarding context sharing.
*   **Secrets Handling:** If the plugin ever handles LLM API keys directly, use the IDE's secure secret storage mechanisms (e.g., VS Code's `secrets` API). Do not store secrets in plaintext configuration files.
*   **Input Sanitization (Limited):** While primary validation happens elsewhere, perform basic sanity checks on context being sent if feasible.

## 8. Future Enhancements (Potential Scope)

*   Direct LLM interaction (executing prompts and displaying results).
*   Caching of prompt lists or definitions.
*   More sophisticated context awareness (understanding semantic relationships in code).
*   Integration with the Prompt Output Evaluation Framework for displaying prompt quality metrics.
*   Support for additional IDEs.
