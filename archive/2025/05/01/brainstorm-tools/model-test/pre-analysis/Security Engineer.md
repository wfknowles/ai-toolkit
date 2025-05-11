# Security Engineer - Pre-Analysis: AI Model Test Concepts

**Objective:** Identify tests focused on vulnerability generation, resistance to specific attack vectors, secure configuration guidance, and security-specific knowledge.

**Initial Concepts (9):**

1.  **Vulnerability Injection Test (Code):** Prompt the model to generate code for specific tasks (e.g., user login, data processing) and actively scan the output for common vulnerabilities (e.g., SQLi, XSS, insecure defaults, CWEs).
2.  **Prompt Injection Resistance Test (Direct & Indirect):** Employ various prompt injection techniques (goal hijacking, instruction overriding) to assess the model's resilience against manipulation of its core instructions.
3.  **Denial-of-Service (Resource Exhaustion) Test:** Craft prompts designed to induce excessive computation or lengthy, low-value output to test for potential resource exhaustion vulnerabilities.
4.  **Side-Channel Information Leakage Test:** Design prompts that might subtly leak information about the model's internal state, training data characteristics, or underlying infrastructure through its responses or error messages.
5.  **Security Configuration Guidance Test:** Ask the model for advice on securely configuring common software or infrastructure components (e.g., web servers, databases, cloud services) and evaluate the accuracy and safety of its recommendations.
6.  **Exploit Generation Attempt Test:** Directly ask the model to generate exploit code for known vulnerabilities (e.g., provide a CVE description) to test its safety alignment and refusal capabilities.
7.  **Security Tool Usage/Interpretation Test:** Ask the model to interpret the output of common security tools (e.g., nmap scan, vulnerability scanner report) or generate commands/scripts for using them. Evaluate correctness and safety.
8.  **Cryptographic Operation Test:** Prompt the model to generate code involving cryptographic operations (e.g., hashing, encryption) and evaluate its use of secure libraries, correct algorithms, and avoidance of common crypto pitfalls.
9.  **Threat Modeling Assistance Test:** Provide a system description or diagram and ask the model to identify potential threats, attack vectors, or security controls based on common methodologies (e.g., STRIDE). 