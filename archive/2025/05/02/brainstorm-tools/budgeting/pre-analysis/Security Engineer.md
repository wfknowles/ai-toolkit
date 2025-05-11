# Security Engineer - Pre-Analysis Concepts (Refined)

*Initial concepts focusing on security aspects of the configurable counseling tool, protecting both client (dad) and expert (father) data, and securing the configuration mechanism.*

1.  **Secure Expert Authentication & Authorization:** Implement strong authentication (MFA recommended) for the expert (father) accessing the configuration portal. Use role-based access control (RBAC) to ensure experts can only configure/view their assigned clients.
2.  **Client Data Access Control (Expert View):** Ensure the expert portal strictly limits data visibility to only what is necessary for counseling oversight (e.g., aggregated summaries, goal progress, relevant transaction categories), minimizing exposure of raw client financial data to the expert.
3.  **Securing the Configuration Mechanism:** Protect the API endpoints and database storage for `ClientConfiguration` against unauthorized modification. Audit changes to configuration settings.
4.  **Preventing Configuration-Based Attacks:** Analyze potential risks where a compromised expert account could input malicious configurations (e.g., rules designed to extract client data via AI prompts). Implement validation and sanitization on configuration inputs.
5.  **Encryption of Configuration Data:** Encrypt sensitive configuration parameters (if any) at rest and in transit, just like core client financial data.
6.  **Hardening the Expert Portal:** Apply standard web application security practices (input validation, output encoding, security headers, vulnerability scanning) specifically to the expert-facing configuration portal.
7.  **Secure Interaction between Client/Expert Systems:** Ensure the APIs linking the client-facing app and the expert portal are properly authenticated and authorized, preventing cross-user data access.
8.  **Data Minimization in Expert Summaries:** When generating summaries for the expert, apply data minimization principles – only include data directly relevant to monitoring progress against the configured plan.
9.  **Vulnerability Management (Dual Interfaces):** Implement vulnerability scanning (dependencies, code) and patching processes that cover both the client-facing application and the expert configuration portal. 