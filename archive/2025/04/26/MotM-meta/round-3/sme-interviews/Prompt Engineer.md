# Interview R3: Prompt Engineer

**Date:** 2025-04-26
**Facilitator:** AI Assistant
**Interviewee:** Prompt Engineer (Simulated)

**Facilitator:** Thanks for outlining the implementation phases from a prompt perspective. You identified anti-patterns like overly complex prompts and fragile parsing. How can we proactively mitigate these during the Step Prompt Implementation phase (your Phase 2)?

**Prompt Engineer:** Mitigation involves discipline and clear standards:
1.  **Strict Adherence to Template/Contract:** Every Step Prompt *must* use the standard template and conform to the I/O contract. No exceptions.
2.  **Single Responsibility Principle:** Each Step Prompt should do *one thing*. If logic seems too complex, break it into two sequential Step Prompts.
3.  **Peer Reviews:** Before integrating a Step Prompt, another engineer (PE/AE/SSE) should review it for clarity, adherence to standards, and potential complexity issues.
4.  **Standardized Instructions:** Use the documented "common instruction patterns" (SSE's R3 point) for file I/O, JSON handling etc., don't reinvent them in each prompt.

**Facilitator:** Regarding the Orchestrator parsing JSON responses - how confident are you this can be made reliable enough? What's the fallback if it proves highly inconsistent?

**Prompt Engineer:** Confidence is moderate. We can improve reliability with very explicit instructions (find fenced block, validate keys). The fallback if it remains highly inconsistent is... painful. It might require adding a wrapper script *if* custom tools were possible (they aren't), or simplifying the Step Prompt outputs further (e.g., returning simpler strings instead of JSON, making state updates harder), or potentially accepting a higher failure rate and relying on the user to manually retry/debug using the state file.

**Facilitator:** If you were planning the project (your Phase 3/4), what would your ideal testing strategy look like for the prompts themselves?

**Prompt Engineer:** Ideal within constraints:
*   **Unit Tests:** For each Step Prompt, create sample `state.json` inputs representing different scenarios (happy path, edge cases, potential errors). Run the prompt manually with these inputs. Verify the output JSON `status` and `output_data` (including generated file paths) are exactly as expected.
*   **Orchestrator Response Handling Tests:** Craft sample LLM responses (some with correct JSON, some malformed, some with `status: error`). Feed these (conceptually) to the Orchestrator prompt logic and verify it correctly parses, validates, updates state, or flags errors.
*   **E2E Tests:** Execute the full workflow, paying close attention to the transitions between steps handled by prompts and the intermediate state/files.

**Facilitator:** Any R1/R2 decisions or analyses that seem like blindspots now? Are there prompt-related shortcuts taken that might hurt scalability?

**Prompt Engineer:** The main potential shortcut is simplifying the logic refactored from the monoliths too much, potentially losing nuance needed for quality output, just to fit it into discrete steps. We need to balance simplicity with functional equivalence. Relying *solely* on prompt templating for JSON output without robust Orchestrator validation could also be a shortcut that bites us.

**Facilitator:** What are the biggest unknowns for you before starting Phase 1 (Foundation Setup)?

**Prompt Engineer:** The biggest unknown is the *real-world* consistency of the chosen LLM within Cursor in following complex, structured instructions involving tool use and specific output formatting over a multi-step sequence. We have designs and requirements, but practical reliability is unproven.

**Facilitator:** Any "prompt smells" we should explicitly forbid?

**Prompt Engineer:** Yes: 
*   Prompts that try to combine multiple logical steps.
*   Prompts with ambiguous instructions for tool use or output format.
*   Prompts that rely on implicit knowledge from previous steps instead of explicit input data.
*   Lack of comments explaining the prompt's purpose and logic.

**Facilitator:** Missing SMEs for the implementation phase?

**Prompt Engineer:** No, the defined team (PE/AE/SSE focus on implementation, others on design/docs/testing) seems correct.

**Facilitator:** Thank you, the focus on standards and testing is critical. 