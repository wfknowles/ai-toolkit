# Interview R3: AI Agent Engineer

**Date:** 2025-04-26
**Facilitator:** AI Assistant
**Interviewee:** AI Agent Engineer (Simulated)

**Facilitator:** Thanks for phasing the agent system implementation. Your Phase 1 focuses on foundation/standards like the template and contract. Any challenges defining the `INTERFACE_CONTRACT.md` comprehensively for *all* steps upfront?

**AI Agent Engineer:** The challenge is anticipating the precise data needs of *every* step before implementing them. We can define the major inputs/outputs based on the `MVP_WORKFLOW.md`, but details might emerge during Step Prompt implementation (Phase 3). Mitigation: Treat the contract as a living document (PA's point), but enforce that any *changes* needed during implementation are formally updated in the contract and reviewed, not just hacked into the prompts.

**Facilitator:** Your Phase 2 involves implementing and testing the Orchestrator logic using dummy steps. How complex should these dummy steps be?

**AI Agent Engineer:** Very simple. Their only purpose is to test the Orchestrator. Dummy Step A might just return `{ "status": "success", "output_data": {"path": "dummy-A-output.md"} }`. Dummy Step B might return `{ "status": "error", "output_data": {"message": "Simulated error"} }`. This allows testing the Orchestrator's sequencing, parsing, validation, state update, and error handling logic without depending on the actual complex Step Prompt implementations.

**Facilitator:** If you were planning the integration testing (Phase 4), how would you structure debugging when the full Orchestrator interacts with real Step Prompts?

**AI Agent Engineer:** Debugging integration:
1.  **Verify Interfaces:** If Step S3 fails, first check: Did Orchestrator provide the correct input to S3 per the contract? Did S3 produce output matching the contract? (Check raw LLM response if needed).
2.  **Isolate Component:** If the interface seems correct, test the failed Step Prompt S3 in isolation (unit test) with the exact input it received. If it fails there, the issue is S3's internal logic/prompting.
3.  **Check Orchestrator Logic:** If S3 works in isolation but fails in the chain, the issue might be the Orchestrator's state handling *before* S3, its parsing of S3's response, or how it updates state *after* S3.
4.  **Examine State/Files:** Check `state.json` and auxiliary files at each stage to trace the data flow and pinpoint where inconsistency occurred.

**Facilitator:** Any R1/R2 decisions/blindspots related to the agent interactions? Any shortcuts risking scalability?

**AI Agent Engineer:** A potential R1/R2 blindspot was not explicitly discussing how prompts should handle *tool errors* (e.g., `edit_file` itself fails). Step Prompts need instructions to catch this (if possible via the tool's response?) and report it via their `status: "error"` output. A shortcut would be assuming tools always work. For scalability, relying heavily on complex data transformations *within* prompts (instead of just data passing) makes generalization harder, as that logic might need to change significantly for different concepts.

**Facilitator:** Biggest unknown before starting implementation?

**AI Agent Engineer:** The LLM's consistency in complex prompt following, especially the Orchestrator's multi-part logic (parse, validate, update state, call tool). And the reliability/latency of the tool calls.

**Facilitator:** Any agent-specific "smells" to forbid?

**AI Agent Engineer:**
*   Step Prompts that don't clearly declare their inputs/outputs.
*   Step Prompts that don't return the standard JSON status block.
*   Orchestrator prompts that are monolithic instead of having clear logical sections for each part of the control loop.
*   Prompts that fail silently on tool errors instead of reporting failure in their status.

**Facilitator:** Missing SMEs?

**AI Agent Engineer:** No, team is good.

**Facilitator:** Thank you. The structured debugging approach and handling tool errors are key takeaways. 