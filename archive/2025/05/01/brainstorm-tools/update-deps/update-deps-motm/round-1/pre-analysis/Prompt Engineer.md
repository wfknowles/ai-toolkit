# Prompt Engineer - MotM Round 1 Pre-Analysis: AI Dependency Update Assistant

**Objective:** Analyze the refined Top 15 concept list, focusing on the prompt structure, interaction flow, clarity of instructions to the AI, and how well it supports the Jr. Dev persona.

**Analysis of Concept (Top 15 from `brainstorm.md`):**

The Top 15 list effectively incorporates key prompt engineering principles:

*   **Clarity & Control:** Command Preview/Confirmation (#5), User Control (#7), Manager Inference/Confirmation (#9), and Rollback (#8) provide essential control points.
*   **Structured Interaction:** The implied workflow (Check -> Review -> Test -> Apply) benefits from Clear Summary/Filtering (#10) and Interactive Conflict Resolution (#4).
*   **Explanation Focus:** Breaking Change Explanation (#2) and Reasoning/CoT (#14) are crucial for transparency and the target Jr. Dev audience.

**Potential Weaknesses/Gaps from PE Perspective:**

*   **Prompt Complexity:** Orchestrating all these steps (scanning, analysis, testing, branching, user interaction) via a single prompt seems unrealistic. It likely requires a multi-turn conversation or a more structured tool interface driven by prompts at specific stages.
*   **AI Instruction Nuance:** How do we effectively instruct the AI to *balance* competing goals? E.g., "Update to fix security issue (#1) but minimize breaking changes (#2) and respect user pins (#7)." This requires sophisticated instruction design.
*   **Parsing Reliability:** Several concepts rely on parsing external data (changelogs for #2, resolver errors for #4, test results for #3). The prompt needs to guide the AI on how to handle parsing failures or ambiguous data.
*   **Persona Consistency:** Ensuring the helpful Jr. Dev persona (PE-9 from initial brainstorm) is maintained throughout complex technical explanations (#2, #4, #14) needs explicit instruction.

**Initial Thoughts/Refinements:**

1.  **Modular Prompting:** Define distinct prompt templates/sub-prompts for each phase (e.g., Initial Check & Summary, Conflict Resolution, Code Mod Suggestion, Final Confirmation).
2.  **Goal Prioritization Instruction:** Explicitly instruct the AI on how to prioritize conflicting goals (e.g., "Prioritize applying security patches unless a high-confidence breaking change is detected in critical code paths"). Make this configurable.
3.  **Error Handling Prompts:** Design specific prompts for the AI to use when it encounters errors (e.g., failed scans, broken tests, unparseable data), guiding it to report clearly and suggest next steps.
4.  **Refine Explanation Prompts:** Craft specific instructions for #2 (Breaking Changes) and #14 (CoT) emphasizing analogy, simple terms, and focusing on the *impact* for the developer.
5.  **Input Validation:** Prompt the AI to validate user inputs (#7) for syntax and potential conflicts early in the process. 