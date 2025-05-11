# Interview: AI Agent Engineer

**Date:** 2025-04-26
**Facilitator:** AI Assistant
**Interviewee:** AI Agent Engineer (Simulated)

**Facilitator:** Thanks for framing this in terms of a simulated agent system. You emphasized the orchestrator and standardized state. Given the reliability concerns others raised, how would you design the agents (prompts) themselves to be as robust as possible?

**AI Agent Engineer:** Robustness in this context means predictability and clear interfaces. 
1.  **Explicit Instructions:** Prompts need extremely clear instructions on reading specific keys from the JSON state, performing a single logical task, and generating output for specific keys in the state JSON. Use formatting (like XML tags or Markdown headings) within the prompt to clearly delineate input data, task instructions, and output format requirements.
2.  **Input Validation (Minimal):** The agent prompt could include a basic instruction like "If the required input key X is missing or empty in the provided state, output an error status for key Y instead of proceeding."
3.  **Output Formatting:** Instruct the agent to output its results *and* status (success/error) within a designated JSON structure in its response. This makes parsing by the orchestrator much more reliable than freeform text.
4.  **Idempotency (Desirable but Hard):** Ideally, if an agent step were accidentally run twice, it wouldn't corrupt the state. This is difficult to achieve purely via prompts but designing steps to be as self-contained as possible helps.

**Facilitator:** How critical is the choice of state format (JSON vs. MD) from an agent interaction perspective?

**AI Agent Engineer:** JSON is strongly preferred for agent interaction. LLMs are generally better at parsing and generating structured JSON via prompting than arbitrary markdown. It reduces ambiguity. While MD might be user-readable, the agents (LLM instances) are the primary consumers of the state file during the chain execution. We optimize for machine readability and processing reliability.

**Facilitator:** If you were building the orchestrator prompt, how would it handle agent invocation and response processing?

**AI Agent Engineer:** The orchestrator loop would be:
1.  Read `state.json`.
2.  Determine `next_step` based on `state.current_step` (and potentially `state.status`).
3.  Construct the prompt for `next_step`, injecting necessary data from `state.json`.
4.  Execute the agent prompt.
5.  Attempt to parse the agent's response (expecting a JSON block).
6.  *Crucially:* Validate the response. Did the agent report success? Is the output JSON valid? Does it contain expected keys?
7.  If valid & success: Update `state.json` with the results and set `current_step` to `next_step`.
8.  If invalid or error reported by agent: Update `state.json` with `status: error`, `error_message: ...`, and halt.
9.  Write `state.json` back to disk.
10. If more steps, loop. If complete, run final synthesis.

**Facilitator:** What are the biggest unknowns for you in implementing this pseudo-agent system?

**AI Agent Engineer:**
*   The LLM's consistency in adhering to the strict JSON output format across different steps and potentially complex data.
*   The true limits of the orchestrator prompt's complexity – can it reliably manage the state logic, agent invocation, and error checking purely through text instructions?
*   Scalability: While the initial chain might be simple, how fragile does this become if we add more steps or more complex inter-step dependencies?

**Facilitator:** Any blindspots?

**AI Agent Engineer:** A potential blindspot is the lack of true agent memory or learning. Each step is essentially stateless except for what's explicitly passed via the file. This limits the ability to handle nuanced context or evolve strategy mid-chain in a sophisticated way. We are simulating agents, not deploying them.

**Facilitator:** Missing SMEs?

**AI Agent Engineer:** No, this group covers the design aspects well. The proof will be in the implementation and testing.

**Facilitator:** Thank you for the agent-based perspective and design details. 