# Interview R3: Project Manager

**Date:** 2025-04-26
**Facilitator:** AI Assistant
**Interviewee:** Project Manager (Simulated)

**Facilitator:** Thanks for laying out the MVP project execution phases. Your Phase 1 focuses on planning and kickoff. Any challenges anticipating the task breakdown or estimation (Step 1.1, 1.3), given the novelty of prompt engineering?

**Project Manager:** Absolutely. Estimating prompt implementation (WBS 2.2) is the biggest challenge. Unlike traditional coding, it's highly iterative and success depends heavily on LLM behavior. Mitigation is to use timeboxing initially for prompt tasks rather than precise estimates, and build buffer into the testing/debugging phase (WBS 3.3/3.5), as SSE noted it will be time-consuming.

**Facilitator:** The manual testing strategy (your Phase 3) seems laborious. How can we ensure it's effective and provides sufficient coverage from a project management perspective?

**Project Manager:** Effectiveness comes from:
1.  **Clear Test Cases:** PO/UXE/QA (if we had one) need to define specific E2E scenarios based on acceptance criteria, covering happy paths and key error conditions.
2.  **Structured Execution:** Testers need to methodically execute these scenarios, logging results, state file contents, and any errors encountered.
3.  **Bug Tracking:** Use a simple system (even just a shared document) to track identified issues, assign owners, and monitor resolution.
Coverage is harder to guarantee than with automated tests, but focusing on the defined acceptance criteria provides the baseline.

**Facilitator:** If you were managing this project, how would you structure check-ins and reporting (Step 1.4, 3.4)?

**Project Manager:** 
*   **Check-ins:** Short daily syncs for the core implementation team (PE/AE/SSE) to discuss progress, blockers. Weekly demos for the wider team (including PO, UXE, PA) to show progress on the E2E flow or key features.
*   **Reporting:** Simple weekly status updates summarizing progress against milestones, key risks/issues, and any changes to timelines.

**Facilitator:** What are the biggest project execution unknowns now?

**Project Manager:**
*   The actual velocity of prompt development and debugging – how quickly can the team iterate and stabilize the prompts?
*   Will we encounter unexpected Cursor platform or tool limitations (rate limits, stability issues like we are seeing now!) that significantly impact the plan?
*   Resource contention if PE/AE/SSE are needed simultaneously for different interdependent prompts.

**Facilitator:** Any R1/R2 blindspots? Are there project management shortcuts (like inadequate tracking) that risk scalability/maintainability?

**Project Manager:** The R1/R2 focus was heavily on *design*. A potential R2 blindspot was not creating the detailed WBS/task list *then*, pushing it to R3/Phase 1 now. For scalability, the main shortcut risk is insufficient time allocated for prompt reviews and refactoring (PA's point) – leading to "prompt debt" that makes future changes costly.

**Facilitator:** Any project management "smells" to avoid?

**Project Manager:**
*   Tasks staying "In Progress" for too long without clear updates or blockers identified.
*   Lack of visibility into testing progress and results.
*   Team members working in silos without coordinating on interfaces (Orchestrator/Step Prompts).
*   Ignoring risks identified in R1/R2 during implementation.

**Facilitator:** Missing SMEs for implementation?

**Project Manager:** No, the team defined seems right for the build.

**Facilitator:** Thank you. The focus on realistic estimation and managing the testing process is key. 