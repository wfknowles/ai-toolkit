# CISO - Brainstorming Pre-Analysis: Meta-Prompts & Modularity

**Focus:** Governance, Risk, Compliance (GRC) & Strategic Security Value

**Concepts Brainstormed (9):**

1.  **Auditable Prompt Execution Logs:** Ensure the orchestration system (Arch concept #1) logs every prompt execution, including the exact prompt sent (potentially redacted for sensitive data), the context provided (hashes/references), the LLM response, and metadata (user, timestamp, decision). Essential for audit trails.
2.  **Risk-Based Prompt Approval Workflow:** For high-risk AI actions (e.g., auto-applying code changes, generating sensitive configurations), implement an approval workflow. The initial AI output triggers a request requiring human review/approval (potentially tiered based on sensitivity) before execution.
3.  **Compliance Mapping Prompt:** Prompt: "Analyze this technical control description [text] or code snippet [text]. Map it to relevant compliance requirements from [SOC2/PCI-DSS/HIPAA control list]. Identify any potential gaps."
4.  **Policy Generation Assistance Prompt:** Prompt: "Draft a corporate policy regarding [Acceptable Use of AI Tools], based on [NIST AI RMF / organizational principles]."
5.  **Security Awareness Content Generation:** Prompt: "Generate a short security awareness message for developers about the risks of [Prompt Injection], including examples and prevention tips."
6.  **Supply Chain Risk Analysis Prompt:** Prompt: "Analyze this list of software dependencies [list]. Identify any known high-risk components based on [age, maintainer activity, known breaches, geopolitical factors - requires external data feed]."
7.  **Red Team Scenario Generation Prompt:** Prompt: "Generate potential attack scenarios targeting our [web application], considering common vulnerabilities [OWASP Top 10] and our tech stack [details]."
8.  **GRC Reporting Data Aggregation Prompt:** Prompt: "Aggregate the results from recent [security scans, compliance checks, policy exceptions] across these projects [list]. Summarize key risk indicators and trends for a CISO dashboard report."
9.  **Guardrails for AI Capabilities (Meta-Prompt):** A high-level meta-prompt or configuration that restricts the *types* of actions or *domains* the AI system is allowed to operate in, regardless of specific task prompts. E.g., "Under no circumstances should the AI attempt to modify production infrastructure configurations." 