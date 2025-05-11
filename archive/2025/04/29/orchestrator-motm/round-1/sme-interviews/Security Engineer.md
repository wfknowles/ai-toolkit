# Security Engineer - Interview (Orchestrator Framework)

**Facilitator:** Regarding the execution environment, what level of sandboxing is appropriate for this use case?

**Security Engineer:** (Placeholder recommending strong sandboxing (e.g., Docker with minimal base image, no network access unless essential, read-only root filesystem where possible, run as non-root user) to contain potential exploits.)

**Facilitator:** Where is the most critical point for input sanitization in this flow?

**Security Engineer:** (Placeholder identifying the boundary points: Orchestrator receiving model output (less critical if model is trusted), and crucially, the Execution Environment receiving parameters (`file_path`, `content`) before acting on them.)

... 