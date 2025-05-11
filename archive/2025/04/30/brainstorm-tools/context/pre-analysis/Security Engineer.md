# Security Engineer - Initial Context Management Concepts

Focusing on security implications of context handling:

1.  **Context Sanitization/Filtering:** Implementing mechanisms to automatically detect and remove or mask sensitive information (PII, secrets, proprietary code) from context before it's sent to an LLM, especially third-party models.
2.  **Least Privilege Context Access (RAG Security):** Ensuring that Retrieval-Augmented Generation systems only retrieve context that the user/agent is authorized to access, enforcing access controls on the underlying knowledge sources.
3.  **Detecting Context Injection Attacks:** Developing prompts or techniques to identify if malicious instructions have been hidden within the data provided as context (e.g., in a document being summarized).
4.  **Auditing Context Usage:** Logging precisely what context was provided to an LLM for a given request and what context was retrieved (e.g., in RAG) to enable security auditing and incident investigation.
5.  **Secure Context Storage:** Ensuring that any stored context (e.g., conversation history, agent memory) is encrypted at rest and in transit, with appropriate access controls.
6.  **Contextual Access Control for Agents:** Designing fine-grained permissions for AI agents that restrict what contextual information they can access or request based on their specific task and role.
7.  **Preventing Context Leakage Across Sessions/Users:** Implementing strict boundaries to ensure that context from one user's session or task cannot inadvertently leak into another user's session or influence their results.
8.  **Vulnerability Scanning of Context Sources:** Regularly scanning knowledge bases or document repositories used for RAG to ensure they don't contain known vulnerabilities or malicious content that could be injected into prompts.
9.  **Context Provenance Tracking:** Maintaining metadata about the origin and trustworthiness of different pieces of context, allowing the LLM or orchestrator to potentially weigh context from trusted sources more heavily. 