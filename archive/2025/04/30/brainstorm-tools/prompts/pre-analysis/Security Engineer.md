# Security Engineer - Initial Concepts

Focusing on security aspects throughout the maintenance lifecycle:

1.  **Secure Code Review Prompt:** A prompt specifically trained/designed to analyze code changes (diffs) for common security vulnerabilities (e.g., OWASP Top 10) relevant to the language/framework being used.
2.  **Dependency Vulnerability Analysis Prompt:** A prompt that takes results from a dependency scanner (e.g., `npm audit`, Snyk) and analyzes the codebase to determine if and how the vulnerable functions are actually used, assessing exploitability and impact in context.
3.  **Security Test Case Generation:** A prompt that, given a description of a feature or fix, generates security-focused test cases, including tests for injection flaws, broken authentication/authorization, XSS, insecure direct object references, etc.
4.  **Threat Modeling Assistant for Changes:** A prompt to assist in threat modeling a proposed change during maintenance. It takes the change description and architecture context and suggests potential threats, attack vectors, and required security controls based on frameworks like STRIDE.
5.  **Infrastructure-as-Code Security Scan Prompt:** A prompt that analyzes IaC templates (Terraform, CloudFormation, Kubernetes manifests) for security misconfigurations (e.g., overly permissive IAM roles, unencrypted storage, exposed ports) before they are applied during maintenance.
6.  **Secret Detection Prompt:** A prompt designed to scan code changes or configuration files specifically for hardcoded secrets (API keys, passwords, certificates) that might be accidentally introduced during maintenance.
7.  **Security Incident Response Playbook Generation:** A prompt that helps generate or update incident response playbooks for specific types of security events potentially triggered by maintenance activities (e.g., credential compromise, data leakage).
8.  **Log Analysis for Security Events:** A prompt optimized for security analysts to query application and system logs for indicators of compromise (IoCs) or suspicious activity, potentially correlating events across different log sources during or after maintenance.
9.  **Compliance Check Automation Prompt:** A prompt that checks code changes or configurations against specific compliance requirements (e.g., PCI-DSS, HIPAA, GDPR), identifying potential violations introduced during maintenance. 