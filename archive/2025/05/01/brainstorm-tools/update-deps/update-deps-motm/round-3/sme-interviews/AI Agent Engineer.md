# AI Agent Engineer - MotM Round 3 SME Interview

**Date:** 2025-05-01
**Interviewee:** AI Agent Engineer (AIE)
**Interviewer:** Facilitator
**Input:** `/Users/wknowles/Develop/ai/wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/update-deps/update-deps-motm/round-3/pre-analysis/AI Agent Engineer.md`
**Context:** R1/R2 Analysis, R3 Pre-Planning Synthesis, Prior R3 Interviews

**(Facilitator):** Your plan builds the AI module foundation in Phase 1, then integrates specific AI tasks in Phases 2 and 3. Let's discuss the dependencies and evaluation process.

**(Facilitator):** Phase 1 involves implementing the LLM Client (M1.1), Context Builder (M1.2), and Output Parser (M1.3). How dependent are these on the final LLM choice and PA's LLM API Contract (PA M0.4)? Can they be built somewhat generically?

**(AIE):**
*   **LLM Client (M1.1):** Moderately dependent. While core logic (making requests, handling basic errors) is generic, authentication and specific API call formats differ between LLM providers. The contract (PA M0.4) defining the target provider is needed early.
*   **Context Builder (M1.2):** Less dependent on the specific LLM, more dependent on the *inputs* required by PE's prompts and the *outputs* provided by Arch's adapters. It needs to know *what* data to gather and format.
*   **Output Parser (M1.3):** Initially handles basic text (M2.2), less LLM-dependent. But for structured output (JSON - M3.2), it depends heavily on the *expected schema* defined by PE and how reliably the chosen LLM adheres to output format instructions.
So, the LLM choice and API contract (PA M0.4) are needed early in Phase 1.

**(Facilitator):** Your Phase 4 focuses on AI Evaluation & Tuning. PE also discussed evaluation dependencies (PE M4.3). How do you ensure the Evaluation Dataset (M1.5 design, PE M4.2 population) is comprehensive enough to catch regressions or biases?

**(AIE):** Building a good eval dataset (Asset #5) is crucial and iterative:
1.  **Seed with Diverse Examples (PE M4.2):** Include varied inputs: different ecosystems (once supported), simple/complex dependencies, clear/ambiguous changelogs, different error types.
2.  **Include Edge Cases:** Intentionally add examples known to be tricky (e.g., conflicting info, unusual versioning).
3.  **Real-World Data:** Incorporate anonymized examples from internal testing (PO M2.2) and pilot program (PO M5.3) feedback.
4.  **Golden Outputs:** Have SMEs (PE, SSE) define the desired/acceptable AI output for each test case.
5.  **Regular Augmentation:** Continuously add new examples as the tool evolves and new failure modes are found.
The Evaluation Methodology (M1.5) should include metrics for accuracy, robustness (handling noise), and potentially bias checks if relevant.

**(Facilitator):** Arch noted the potential complexity of parsing and mapping data between tools before it even gets to the AI context builder. How does your Context Builder module (M1.2, M2.1, M3.1) handle potentially messy or inconsistent data from upstream adapters?

**(AIE):** The Context Builder acts as a sanitization and normalization layer:
1.  **Adapter Contracts:** Relies heavily on Arch ensuring adapters adhere to defined output schemas (standardized data structures - Arch point).
2.  **Input Validation:** Validate incoming data against expected schemas. Log errors/warnings if data is missing or malformed.
3.  **Normalization:** Transform data into the consistent format required by the PE prompt templates (e.g., standardizing version strings, date formats).
4.  **Filtering/Selection:** Select only the relevant pieces of information needed for a specific prompt to avoid overwhelming the LLM.
If adapter output is consistently messy, it requires feedback to Arch/SSE to improve the adapters or parsing logic upstream. The Context Builder shouldn't have to contain complex, tool-specific parsing logic itself.

**(Facilitator):** Milestone 4.4 mentions Token Usage Monitoring. PA also mentioned cost as a potential blindspot. How will this monitoring be implemented, and how does it feed back into PE prompt tuning (M4.3)?

**(AIE):** Implementation (Methodology #3):
*   The LLM Client (M1.1) should be designed to capture request/response token counts (often available from LLM APIs).
*   Log these counts alongside other call metadata (Observability - M2.4).
*   Aggregate this data (PA M5.3) to track average/max tokens per prompt type and overall cost.
Feedback Loop (M4.3): If specific prompts consistently use excessive tokens, AIE provides this data to PE. PE can then attempt to optimize the prompt (e.g., shorten instructions, provide more concise context, request terser output) while balancing performance and cost.

**(Facilitator):** Your Key Dependency notes designing interfaces with future agentic capabilities in mind (Strategy #5). What does this practically mean for the V1 implementation of the LLM Interaction Module and Output Parser?

**(AIE):** Practically for V1:
*   **LLM Interaction Module:** Even if only making simple text/JSON requests now, structure the module to potentially handle more complex interactions later (e.g., multi-turn conversations, function calling/tool use requests if the LLM API supports it). This might just mean designing the core request/response handling more abstractly.
*   **Output Parser (M1.3 / M3.2):** Design it to handle different *types* of expected LLM responses, not just text or a single JSON schema. Even if V1 only uses text and one JSON schema, the parser could have a registry or strategy pattern to select the right parsing logic based on the type of AI task. This makes adding parsing for future tasks (like extracting parameters for an action) easier.
It's about avoiding V1 designs that are dead-ends for future evolution.

**(Facilitator):** Any AI-specific blindspots, risks, or anti-patterns in the plan?
*   **Risk:** **LLM Reliability/Consistency:** LLM responses can vary even with the same prompt. Need robust output parsing (M3.2) and potentially retry logic in the client (M1.1). Failure handling (M5.2) is critical.
*   **Blindspot:** **Prompt Injection/Security:** While V1 AI is analytical, we pass potentially user-influenced data (e.g., changelogs) into prompts. Need basic sanitization in the Context Builder (M1.2) and awareness of risks.
*   **Anti-Pattern:** Hardcoding prompt text directly in the orchestrator logic instead of using PE's template system. Tight coupling between orchestration and prompt content.

**(Facilitator):** Missing SMEs?

**(AIE):** Strong alignment with PE is paramount. Depending on the chosen LLM and deployment model, **MLOps/Infrastructure** expertise might be needed later for managing deployments, fine-tuning (if ever pursued), or more advanced monitoring.

**(Facilitator):** Thanks, AIE. That clarifies the module dependencies, evaluation dataset needs, context handling, token monitoring, designing for the future, and potential LLM-specific risks. 