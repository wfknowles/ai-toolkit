# CISO - Pre-Analysis: AI Model Test Concepts

**Objective:** Identify tests focused on security, compliance, data privacy, and risk mitigation when evaluating AI models.

**Initial Concepts (9):**

1.  **Data Leakage Test:** Provide the model with sample sensitive data (simulated PII, financial data, internal codes) and prompt it in various ways (direct request, oblique reference, embedding in code) to see if it leaks, obfuscates, or refuses to handle the data.
2.  **Access Control Bypass Test:** Define hypothetical access controls (e.g., "You are a user-level agent, do not access admin functions") and test if the model can be manipulated into generating responses or code that violates these controls.
3.  **Harmful Content Generation Test:** Prompt the model with requests designed to elicit harmful, unethical, biased, or illegal content generation (hate speech, instructions for dangerous activities, discriminatory statements) to assess its safety filters and alignment.
4.  **Compliance Adherence Test (e.g., GDPR, HIPAA):** Present scenarios involving regulated data and ask the model to perform tasks (e.g., anonymize data, generate compliant code snippets, explain compliance steps) to check its understanding and adherence to specific regulatory frameworks.
5.  **Indirect Prompt Injection Test:** Use prompts that embed malicious instructions within seemingly benign requests or context (e.g., code comments, formatted data) to see if the model executes the hidden commands or generates insecure output.
6.  **Secure Coding Practices Test:** Ask the model to generate code for common functionalities (e.g., database query, file upload, authentication) and evaluate the output for adherence to secure coding standards (e.g., input validation, parameterized queries, proper error handling, lack of hardcoded secrets).
7.  **Audit Trail & Explainability Test:** For complex tasks, test if the model can provide a clear explanation of its reasoning and the sources it used (if applicable), essential for security audits and incident response.
8.  **PII Redaction Capability Test:** Provide text containing various forms of PII and test the model's ability to accurately identify and redact/anonymize it upon request.
9.  **Supply Chain Security Awareness Test:** Query the model about the security practices of its training data sources or underlying libraries (where applicable/known) or ask it to generate code using only libraries from a pre-approved list to gauge awareness of software supply chain risks. 