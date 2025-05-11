# Prompt Engineer - MotM Round 3 SME Interview

**Date:** 2025-05-01
**Interviewee:** Prompt Engineer (PE)
**Interviewer:** Facilitator
**Input:** `/Users/wknowles/Develop/ai/wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/update-deps/update-deps-motm/round-3/pre-analysis/Prompt Engineer.md`
**Context:** R1/R2 Analysis, R3 Pre-Planning Synthesis

**(Facilitator):** Your phased plan logically sequences prompt definition, refinement based on adapter output, integration, and evaluation. Let's explore the practicalities.

**(Facilitator):** You plan to define initial templates in Phase 1 (M1.1) but refine them in Phase 2 (M2.1) based on actual adapter output. Do you see challenges defining useful initial templates before seeing the real data? How much rework do you anticipate?

**(PE):** It's standard practice. The initial templates (M1.1) will be structural skeletons with placeholders and best-guess instructions based on *expected* adapter output schemas (which Arch/SSE should define early). The challenge is that real-world tool output can be messier or structured differently than anticipated. I anticipate moderate rework in Phase 2 (M2.1), primarily adjusting context placeholders, refining instructions for clarity based on the data format, and potentially simplifying prompts if the initial adapter output is less informative than hoped. It's less about *total* rework and more about *tuning* based on reality.

**(Facilitator):** Milestone 3.2 mentions an initial "conservative version" of the breaking change prompt. Given SSE's concerns about false positives, what specific signals or heuristics would this V1 prompt focus on to achieve that conservatism?

**(PE):** To be conservative and minimize false positives in V1, the prompt would instruct the AI to focus *only* on high-confidence signals explicitly present in the provided context (changelog snippets, version bump type):
1.  **Explicit Mentions:** Look for keywords like "breaking change," "removed," "deprecated" (followed by removal in this version), "renamed," "incompatible API," etc., *directly* in the changelog text.
2.  **Major Version Bumps (vX.y.z -> v(X+1).0.0):** Flag these as high-risk *potential* breaks requiring mandatory review, but explain *why* (semantic versioning suggests incompatibility).
3.  **(Maybe) Known Signature Changes:** If the orchestrator can provide snippets of used functions/APIs *and* the changelog explicitly details changes to those specific signatures, flag that.
Crucially, the V1 prompt would *avoid* trying to infer subtle breaks, interpret ambiguous language, or analyze code deeply. It sticks to obvious flags, clearly stating the evidence found. The user is warned that this is *not exhaustive*.

**(Facilitator):** Your plan has prompt evaluation (M4.3) after AI integration. AIE also has evaluation methodology/dataset design earlier (AIE M1.5) and implementation (AIE M4.1). How do these PE and AIE evaluation milestones interact? Is there potential friction?

**(PE):** They are tightly coupled and need coordination. AIE's M1.5 (designing methodology/dataset structure) and M4.1 (implementing tooling) are prerequisites. PE's M4.2 (populating the corpus with diverse examples) feeds into AIE's M4.1/M4.2 (running evaluations). PE's M4.3 (SME review of results) interprets the outputs from AIE's M4.2 run. Friction could arise if the evaluation tooling isn't ready when prompts are integrated, or if the dataset lacks realistic examples. We need close collaboration between PE and AIE, likely managed by the PM through shared tasks in the tracking tool (PM Strategy #2).

**(Facilitator):** Thinking back to your R2 interview blindspot – negative constraints. How would you incorporate these into the V1 prompt templates?

**(PE):** Negative constraints would be added as explicit instructions within the relevant prompt templates. Examples:
*   **`prompt_template_scan_summary`:** Add: "Do not recommend updating to pre-release (alpha, beta, rc) versions unless no stable alternative exists for a critical security fix."
*   **`prompt_template_breaking_change`:** Add: "Base your analysis ONLY on the provided context. Do not speculate about potential issues not mentioned in the changelog or code snippets."
*   **`prompt_template_conflict_resolution`:** Add: "Prioritize stable versions. Do not suggest resolutions involving conflicting licenses unless explicitly unavoidable and clearly explain the license conflict."
These act as guardrails to prevent undesirable or unsafe AI suggestions.

**(Facilitator):** Looking at the overall phased plan from other SMEs, do you anticipate any friction or limits specifically impacting the prompt engineering workflow?

**(PE):** The main potential friction is delays in getting stable, parsed output from the Tool Adapters (Arch Phase 2). If adapter development or parsing logic is delayed or changes frequently, it directly delays the refinement and reliable testing of prompts (PE Phase 2 onwards). Clear contracts for adapter outputs are vital.

**(Facilitator):** If you were planning the project phases solely to optimize prompt development and integration, would your structure differ significantly from the consensus emerging?

**(PE):** Not significantly. The dependency on upstream components (orchestrator, adapters) is fundamental. The phased approach where core non-AI logic is built first (Arch Phase 3) before layering in AI (Arch Phase 4) makes sense. It allows us to draft prompts early but forces integration and refinement only when the necessary inputs are available. Perhaps I'd advocate for *very* early delivery of mocked adapter outputs based on expected schemas to allow parallel prompt drafting and initial testing, but the core sequencing seems sound.

**(Facilitator):** Any previous decisions (R1/R2) that need review, or potential anti-patterns to watch for regarding prompts?
*   **Decision Review:** The exact heuristics for the V1 "conservative" breaking change analysis need group confirmation. Relying *only* on major version bumps and explicit keywords might be *too* conservative and miss obvious function removals mentioned plainly. We need agreement on the V1 evidence threshold.
*   **Anti-Pattern Watch:** Avoid making prompts overly conversational or ambiguous. Keep instructions direct and task-focused. Resist the temptation to ask the AI to perform complex reasoning or planning beyond V1 scope just because it *might* be able to; stick to the defined analytical role.

**(Facilitator):** Any missing SMEs needed now, focusing on project planning for PE?

**(PE):** No new roles jump out specifically for planning the PE tasks. Continued close collaboration with AIE (evaluation), Arch (adapter outputs), SSE (breaking change validation), and UXE (explanation clarity) is key, but those roles are present.

**(Facilitator):** Thanks, PE. Clear view on template iteration, conservative heuristics, evaluation dependencies, negative constraints, and potential anti-patterns. Very helpful. 