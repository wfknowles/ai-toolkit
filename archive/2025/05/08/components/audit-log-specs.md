# AI Interaction Audit Log Specification - v1.0

## 1. Purpose

This document specifies the requirements for logging interactions with AI systems, particularly Large Language Models (LLMs), accessed via Our Project's `Dockerized Prompt Backend Service` (Component #5) or potentially other integrated AI services.

The purpose of these audit logs is to provide a reliable and secure record of AI interactions to support:
*   **Debugging and Troubleshooting:** Understanding the inputs and parameters that led to specific AI outputs.
*   **Security Incident Investigation:** Analyzing interactions in case of security breaches, prompt injection attempts, or data leakage incidents.
*   **Compliance and Auditing:** Demonstrating adherence to internal policies (e.g., `Prompt Engineering Standards`, `Ethical AI Usage Protocol`) and external regulations.
*   **Performance Monitoring:** Analyzing usage patterns, response times, and error rates (though detailed performance metrics might reside elsewhere).
*   **Usage Analysis:** Understanding how AI tools are being used to identify popular prompts or areas needing better support (while respecting privacy).
*   **Traceability:** Fulfilling Standard #10 of the `Prompt Engineering Standards`.

## 2. Scope

This specification applies to interactions initiated through the `Dockerized Prompt Backend Service` when it constructs prompts and potentially when it (or an integrated component like the IDE Plugin) interacts with an underlying LLM API.

## 3. Log Event Definition

A distinct log event should be generated for each significant interaction cycle, typically corresponding to a single request to the `/api/v1/get_prompt` endpoint of the backend service and the subsequent interaction with the LLM (if handled by the service or trackable).

## 4. Log Data Fields

Each log event MUST contain the following fields, where applicable and available. Fields marked "(Conditional)" depend on the specific interaction context. Fields marked "(PII Risk)" require careful handling as defined in Section 6.

*   **`eventId` (String):** A unique identifier for the log event (e.g., UUID).
*   **`timestamp` (String - ISO 8601 format):** Timestamp of when the event occurred (UTC recommended).
*   **`serviceName` (String):** Name of the service generating the log (e.g., "PromptBackendService").
*   **`eventType` (String):** Category of the event (e.g., "PromptRequestReceived", "PromptConstructed", "LlmCallAttempt", "LlmCallSuccess", "LlmCallFailure", "ServiceError").
*   **`correlationId` (String, Optional):** An ID to correlate related log events within a single user request or workflow.
*   **`requestorInfo` (Object, Conditional, PII Risk):** Information about the entity initiating the request.
    *   `userId` (String, Optional, PII Risk): Identifier of the authenticated user (use anonymized ID if possible).
    *   `sourceIp` (String, Optional, PII Risk): Source IP address (use with caution, may not be relevant for localhost service).
    *   `clientType` (String, Optional): e.g., "CursorPluginV1.2", "CLIToolV0.9".
*   **`promptInfo` (Object, Conditional):** Details about the requested prompt.
    *   `promptIdRequested` (String): The ID of the prompt/template requested by the client.
    *   `promptVersionUsed` (String, Optional): The specific version of the prompt template actually used.
*   **`contextInfo` (Object, Conditional, PII Risk):** Information about the context provided for prompt templating.
    *   `contextKeysProvided` (List[String]): List of keys provided in the context dictionary (logging keys only is safer than logging values).
    *   `contextSizeBytes` (Integer, Optional): Size of the provided context data.
    *   `sensitiveContextFlag` (Boolean, Optional): A flag indicating if the requestor marked the context as potentially sensitive.
*   **`llmInteraction` (Object, Conditional):** Details about the interaction with the downstream LLM API.
    *   `llmProvider` (String, Optional): e.g., "OpenAI", "Anthropic", "LocalLlama".
    *   `llmModelUsed` (String, Optional): Specific model version (e.g., "gpt-4-turbo-2024-04-09").
    *   `llmParameters` (Object, Optional): Key parameters used for the LLM call (e.g., `{"temperature": 0.5, "max_tokens": 500}`).
    *   `fullPromptHash` (String, Optional): A cryptographic hash (e.g., SHA-256) of the *final* prompt sent to the LLM. **Avoid logging the full prompt text unless absolutely necessary and secured.**
    *   `responseSummaryHash` (String, Optional): A hash of the LLM's response content.
    *   `responseSizeBytes` (Integer, Optional): Size of the LLM response.
    *   `latencyMs` (Integer, Optional): Time taken for the LLM call.
*   **`outcome` (Object):** Information about the result of the event.
    *   `status` (String): e.g., "SUCCESS", "FAILURE", "WARNING".
    *   `errorCode` (String, Optional): A specific error code if the status is FAILURE.
    *   `errorMessage` (String, Optional): A descriptive error message (avoid sensitive details).
*   **(Optional) `metadata` (Object):** Any other relevant key-value pairs for context.

## 5. Log Format

*   Logs MUST be generated in a structured format, preferably **JSON**, to facilitate automated parsing, searching, and analysis.
*   Each log event should be a single line in the output stream or log file.

**Example JSON Log Event:**
```json
{
  "eventId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "timestamp": "2023-10-26T10:30:05.123Z",
  "serviceName": "PromptBackendService",
  "eventType": "PromptConstructed",
  "correlationId": "req-xyz789",
  "requestorInfo": {
    "userId": "user-hash-123", // Anonymized ID
    "clientType": "CursorPluginV1.2"
  },
  "promptInfo": {
    "promptIdRequested": "python_function_from_spec_v1.2",
    "promptVersionUsed": "1.2.3"
  },
  "contextInfo": {
    "contextKeysProvided": ["specification", "function_name_suggestion"],
    "contextSizeBytes": 256,
    "sensitiveContextFlag": false
  },
  "llmInteraction": {
    "fullPromptHash": "sha256:abc123def456..." // Hashed prompt
  },
  "outcome": {
    "status": "SUCCESS"
  }
}
```

## 6. Security and Privacy Considerations

*   **PII/Sensitive Data Handling:** Fields marked "(PII Risk)" (e.g., `userId`, `sourceIp`, `contextInfo`, potentially parts of prompts/responses if not hashed) must be handled according to company data privacy policies and relevant regulations (GDPR, CCPA, etc.).
    *   **Prefer Anonymization/Hashing:** Use anonymized user identifiers. Hash full prompts and responses instead of logging them directly, unless essential for specific, approved debugging or security use cases.
    *   **Redaction:** Implement mechanisms to redact sensitive patterns within logged fields if direct logging is unavoidable and contains residual risk.
    *   **Access Control:** Log access must be strictly controlled (See Section 7).
*   **Log Injection:** Sanitize any data incorporated into log messages (especially free-text fields like error messages) to prevent log injection vulnerabilities (e.g., attackers inserting fake log entries or manipulating log formats via malicious input).

## 7. Log Storage, Retention, and Access Control

*   **Storage:** Logs should be stored in a secure, centralized logging system (e.g., Elasticsearch/OpenSearch, Splunk, Datadog, AWS CloudWatch Logs, Azure Monitor Logs). Avoid storing logs directly on application servers or in insecure locations.
*   **Retention:** Define a log retention policy based on compliance requirements, operational needs, and storage costs (e.g., retain active logs for 90 days, archive for 1 year).
*   **Access Control:** Access to logs must be strictly controlled based on the principle of least privilege. Role-based access control (RBAC) should be used. Grant access only to personnel with a legitimate need (e.g., Security Operations, SREs for debugging, specific Auditors). Audit all access to log data.
*   **Integrity:** Implement measures to protect log integrity (e.g., using append-only storage, cryptographic signing of log batches if feasible).

## 8. SIEM Integration

*   The structured log format (JSON) facilitates easy ingestion into Security Information and Event Management (SIEM) systems.
*   Define specific alert rules within the SIEM based on these logs to detect potential security incidents (e.g., high rate of errors, detection of secrets scanning patterns in context, anomalies in user activity).

## 9. Review and Updates

This specification must be reviewed and updated periodically (e.g., annually) or when significant changes occur to the AI interaction workflows, tooling, or regulatory landscape. Reviews should involve Security, Legal/Compliance, and Engineering stakeholders.
