# Interview R3: Senior Software Engineer

**Date:** 2025-04-26
**Facilitator:** AI Assistant
**Interviewee:** Senior Software Engineer (Simulated)

**Facilitator:** Thanks for breaking down the implementation work and highlighting the need for robust common prompt instructions. Your Phase 1 focuses on setup and utilities. Any challenges defining or testing those common instructions for file I/O and JSON handling?

**Senior Software Engineer:** The challenge is the lack of a true testing harness. We have to manually test these prompt patterns in Cursor, trying different inputs and edge cases (e.g., empty files, malformed JSON input, large data) to see if the LLM consistently follows the instructions. Documenting the *exact* wording that proves most reliable for each common task (state read, state write, aux file write, output format) is key output from this phase.

**Facilitator:** You identified "Prompt Hacking" and ignoring edge cases as anti-patterns. How would your ideal project plan mitigate these during component implementation (your Phase 2)?

**Senior Software Engineer:** Mitigation strategies:
1.  **Code/Prompt Reviews:** Mandatory reviews of all prompts (Orchestrator, Steps) by another engineer before integration. Look specifically for overly complex logic, unclear instructions, or lack of error handling (e.g., assuming a file read will always succeed).
2.  **Standardization:** Enforce use of the documented common instruction patterns from Phase 1. Discourage bespoke solutions for standard tasks.
3.  **Test Case Definition:** Explicitly define test cases (even if executed manually) that cover not just the happy path but also edge cases (e.g., first step, last step, steps with/without auxiliary files, error conditions).

**Facilitator:** If you were planning the debugging phase (your Phase 3.3), how would you structure that potentially time-consuming work?

**Senior Software Engineer:** Structure it methodically:
1.  **Isolate the Failure:** Use `state.json` (`current_step`, `status`, `error_message`) and auxiliary files to pinpoint which step failed.
2.  **Reproduce Manually:** Try running the failed Step Prompt manually with the state data it received (logged by Orchestrator or retrieved from the state file just before the failed step).
3.  **Analyze Prompt/Response:** Examine the exact prompt sent to the LLM for that step and the raw response received. Did the LLM misunderstand? Was the input data wrong? Did the output format deviate?
4.  **Refine Prompt:** Adjust the instructions in the failing prompt (or potentially the Orchestrator if it provided bad input).
5.  **Retest:** Rerun the manual unit test, then reintegrate and retry the E2E test.
6.  **Iterate:** Repeat as needed. Log findings and solutions.

**Facilitator:** Any R1/R2 decisions or analyses that seem like blindspots now? Are there technical shortcuts taken (like the overwrite state strategy) that might hurt scalability?

**Senior Software Engineer:** The state overwrite strategy *is* a potential scalability bottleneck if `state.json` becomes enormous, but the auxiliary file approach mitigates the worst of it for MVP. The main blindspot might be underestimating the performance hit of *many* sequential tool calls (read state, read aux, run LLM, write aux, write state per step). This could make the UX poor even without interruptions. We should consider if *any* steps can be combined *without* sacrificing modularity, but likely not for MVP.

**Facilitator:** Biggest unknown before starting implementation?

**Senior Software Engineer:** The true reliability/latency profile of the `edit_file` and `read_file` tools under repeated sequential use within a single logical workflow.

**Facilitator:** Any engineering "smells" (anti-patterns) specific to this prompt-based approach to forbid?

**Senior Software Engineer:**
*   Prompts asking the LLM to perform complex calculations or data transformations better suited to code.
*   Relying on the LLM remembering context across *tool calls* within a single step (it likely won't).
*   Prompts that don't explicitly handle potential tool errors (e.g., what to output if `read_file` fails).
*   Lack of detailed comments explaining *why* a prompt instruction is phrased a certain way, especially if it looks non-obvious (often needed for reliability).

**Facilitator:** Missing SMEs?

**Senior Software Engineer:** No, implementation team seems right.

**Facilitator:** Great, thank you for the practical implementation and debugging insights. 