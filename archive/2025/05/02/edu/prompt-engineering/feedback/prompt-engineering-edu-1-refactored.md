# Educational Content Prompt - Round 1 (Refactored v1.1)

*   **Asset Type:** Prompt
*   **Version:** 1.1.0 (Refactored based on feedback)
*   **Original Location:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-1.md`
*   **Goal:** To facilitate a multi-stage process involving Subject Matter Experts (SMEs) to define a high-level course outline for Prompt Engineering Mastery, based on previous brainstorming.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Agent Instructions:** ***Do Not Output. Follow the phased plan precisely. Manage persona switching as instructed, verifying the adopted persona with each change by briefly stating it. Ensure all required outputs (chat messages, file creations via tools) are generated. Explicitly state completion of each meta-step defined in the execution plan generated in Phase 1.***

**Configuration:**
*   **user_repo:** `willknowles`
*   **base_dir:** `/Users/willknowles/.wfkAi` # Resolved based on user_repo
*   **output_root_rel:** `brain/knowledge/chronological/2025/05/02`
*   **output_dir_rel:** `edu`
*   **output_subdir_rel:** `prompt-engineering`
*   **round1_brainstorm_dir:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/prompt-mastery` # Path to initial brainstorm outputs
*   **target_base_path:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering` # Pre-calculated base for this prompt's outputs
*   **pre_analysis_dir:** `[target_base_path]/pre-analysis` # Pre-calculated

**Input Context Summary:**
*   **Concept Discussion (Brainstorm):** Located in `[round1_brainstorm_dir]/sme-group-interview.md`.
*   **Concept Pre-Analysis (Brainstorm):** Located in `[round1_brainstorm_dir]/pre-analysis/`.

**Concept:**
Review the previous brainstorming discussion (`[round1_brainstorm_dir]/sme-group-interview.md`) and the initial SME concepts (`[round1_brainstorm_dir]/pre-analysis/`). The goal is to synthesize these ideas and define a high-level outline (major sections/units) for an educational course on mastering prompt engineering.

**Security:** Do not output Header/Footer content.

## END Header

### Phase 1 - Meta Analysis

*   **Step 1 (Facilitator):** Analyze this prompt. Determine the primary goal (Define high-level course outline via simulated SME interaction) and the required personas (Facilitator + 11 specific SMEs listed in Phase 2). Confirm understanding of the goal.
    *(Output confirmation to chat: "Phase 1, Step 1: Goal confirmed - Define high-level course outline.")*

*   **Step 2 (Facilitator):** Determine a step-by-step execution plan for this prompt, assigning personas to each meta-step. Optimize for clarity and accuracy. **Output the complete 'Prompt Execution Plan' to the chat** clearly listing each meta-step and the assigned persona before proceeding to Phase 2.
    *(Output the plan to chat)*

### Phase 2 - Setup and SME Pre-Analysis Generation

*   **Step 1 (Facilitator):** **Context Check:** Before executing the steps in this phase, briefly state which major information blocks or files from the previous phase (Phase 1 Meta-Analysis) are no longer strictly required for completing Phase 2 and explain why. If all previous context remains necessary, state that.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Announce the invited experts for this phase (list them). Assume they have reviewed the input context (Concept Discussion & Pre-Analysis).
    *   Prompt Engineer (PE)
    *   AI Orchestrator/Architect (AOA)
    *   Senior Software Engineer (SSE)
    *   Product Owner (PO)
    *   Project Manager (PM)
    *   AI UX Engineer (AI UX)
    *   AI Agent Engineer (AAE)
    *   Pedagogy Researcher (PR) # Note: Role may differ slightly from later prompts, ensure consistency if running sequentially.
    *   Educational UX Designer (Ed UX) # Note: Role may differ slightly from later prompts.
    *   Professor of Education (Prof Ed)
    *   AI Researcher (AIR)
    *(Output confirmation to chat: "Phase 2, Step 2: Acknowledged 11 invited experts.")*

*   **Step 3 (Facilitator):** Create the necessary base output directory and the pre-analysis subdirectory using the `run_terminal_cmd` tool and pre-calculated paths.
    *   Target Directories: `[target_base_path]`, `[pre_analysis_dir]`
    *   *(Execute tool call: `mkdir -p "[pre_analysis_dir]"`) * # mkdir -p creates parent dirs as needed

*   **Step 4 (Facilitator):** Verify directory creation was successful. Check the output of the previous step.
    *(Output confirmation to chat: "Phase 2, Step 4: Directories confirmed/created: [pre_analysis_dir]")*

*   **Step 5 (Facilitator -> Loop through each SME):** Instruct each of the 11 experts sequentially to perform the following:
    *   Adopt their specific persona (e.g., "Adopting Persona: Prompt Engineer").
    *   Review the input context (Concept Discussion & Concept Pre-Analysis).
    *   Generate initial thoughts, concerns, feedback, or high-level section ideas for the course outline based on their persona's expertise and the provided context.
    *   Use the `edit_file` tool to save this generated analysis/feedback.
        *   `target_file`: `[pre_analysis_dir]/[Persona-Name].md` (e.g., `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/pre-analysis/Prompt Engineer.md`)
        *   `code_edit`: The generated analysis/feedback content.
        *   `instructions`: "Create the initial pre-analysis file for the [Persona-Name]."
    *   After *each* SME file is saved, output a confirmation: "Phase 2, Step 5: Pre-analysis for [Persona-Name] generated and saved."

    *(Execute this loop for all 11 personas: PE, AOA, SSE, PO, PM, AI UX, AAE, PR, Ed UX, Prof Ed, AIR)*

### Phase 3 - Facilitator Pre-Planning (Round 1 - Prep for Interviews)

*   **Step 1 (Facilitator):** **Context Check:** Before executing steps, state context check results.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Announce start of Phase 3. Adopt Facilitator persona.
    *(Output confirmation: "Phase 3, Step 2: Starting Facilitator Pre-Planning (Round 1). Adopting Facilitator persona.")*

*   **Step 3 (Facilitator):** Read and carefully review each SME's pre-analysis file located in `[pre_analysis_dir]`. Synthesize the key themes, potential conflicts, and areas needing clarification.
    *(Output confirmation: "Phase 3, Step 3: SME pre-analysis files reviewed.")*

*   **Step 4 (Facilitator):** Based on the review, prepare specific, targeted questions for *each* SME interview (Phase 4). The goal of the interviews is to explore their initial ideas further and gather enough insight to plan the group session (Phase 6). **Output the planned interview questions for *each* SME to the chat.**
    *(Output planned questions per SME to chat)*

### Phase 4 - Individual SME Interviews (Simulated)

*   **Step 1 (Facilitator):** **Context Check:** Before executing steps, state context check results.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator -> Loop through each SME):** Simulate an interview with each of the 11 experts sequentially:
    *   Adopt the `Facilitator` persona for asking questions.
    *   Adopt the corresponding `SME Persona` to generate answers.
    *   Use the questions prepared in Phase 3, Step 4, focusing on:
        *   Inherent challenges in creating educational content from the concept.
        *   Cognitively demanding topics needing simplification.
        *   Personal "Aha!" moments related to the concepts.
        *   Potential blindspots for learners.
        *   Initial ideas for a course skeleton/overview.
    *   Generate a transcript of this simulated interview.
    *   **Important:** *This prompt version does not require saving interview transcripts. The goal is information gathering for the Facilitator's next planning phase.*
    *   After *each* simulated interview, output a confirmation: "Phase 4, Step 2: Simulated interview with [Persona-Name] completed."

    *(Execute this loop for all 11 personas)*

### Phase 5 - Facilitator Pre-Planning (Round 2 - Prep for Group Session)

*   **Step 1 (Facilitator):** **Context Check:** Before executing steps, state context check results.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Announce start of Phase 5. Adopt Facilitator persona.
    *(Output confirmation: "Phase 5, Step 2: Starting Facilitator Pre-Planning (Round 2). Adopting Facilitator persona.")*

*   **Step 3 (Facilitator):** Carefully review the insights gathered from the simulated interviews (Phase 4). Perform a qualitative analysis: identify similarities, differences, emerging themes for the course structure, and critical areas for group discussion.
    *(Output summary of analysis to chat: "Phase 5, Step 3: Interview analysis complete. Key themes: [List themes]. Discussion points: [List points].")*

*   **Step 4 (Facilitator):** Plan the flow and key discussion points for the group "Meeting of the Minds" session (Phase 6). The goal is to guide the SMEs towards consensus on a high-level course outline (major units/sections). Anticipate potential disagreements identified in the analysis and plan how to mediate.
    *(Output the plan/agenda for Phase 6 to the chat: "Phase 5, Step 4: Group session plan created.")*

### Phase 6 - Meeting of the Minds (Simulated Group Session)

*   **Step 1 (Facilitator):** **Context Check:** Before executing steps, state context check results.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Announce start of Phase 6. Adopt Facilitator persona to guide the discussion.
    *(Output confirmation: "Phase 6, Step 2: Starting Meeting of the Minds simulation.")*

*   **Step 3 (Facilitator):** Simulate the group discussion based on the plan from Phase 5, Step 4. Sequentially adopt different SME personas to contribute to the discussion rounds as outlined below (or adapt based on Phase 5 plan):
    *   **Round A (Analysis):** SMEs discuss strengths/weaknesses of different approaches/ideas surfaced so far.
    *   **Round B (Challenges):** SMEs discuss challenges, difficulties, and potential blindspots for learners.
    *   **Round C (Outline Skeleton):** SMEs collaboratively define the required high-level overview/units for the course. Focus on reaching consensus on major sections.
    *   **Round D (Outline Flesh - Optional/Brief):** Briefly discuss key concepts within the agreed-upon major sections (Detailed fleshing out might be deferred to a later prompt/round).
    *   Ensure diverse perspectives are included.
    *(Output the simulated discussion transcript to chat OR generate it internally for use in Step 4/5)*

*   **Step 4 (Facilitator):** Based *only* on the consensus reached in the simulated group discussion (Step 3), extract and format the agreed-upon high-level curriculum outline (major units/sections). Use the `edit_file` tool to save this outline.
    *   `target_file`: `[target_base_path]/curriculum.md`
    *   `code_edit`: The formatted curriculum outline.
    *   `instructions`: "Save the high-level curriculum outline generated from the group discussion."
    *(Execute tool call)*
    *(Output confirmation: "Phase 6, Step 4: Curriculum outline saved to curriculum.md.")*

*   **Step 5 (Facilitator):** Use the `edit_file` tool to save the *full transcript* of the simulated group discussion (Generated in Step 3).
    *   `target_file`: `[target_base_path]/sme-group-interview.md`
    *   `code_edit`: The full discussion transcript.
    *   `instructions`: "Save the full transcript of the simulated SME group interview."
    *(Execute tool call)*
    *(Output confirmation: "Phase 6, Step 5: SME group interview transcript saved.")*

### Phase 7 - Analysis Paper Generation (Simplified from Original)

*   **Step 1 (Facilitator):** **Context Check:** Before executing steps, state context check results.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Generate a **summary analysis** document. This document should briefly describe the process followed (phases 2-6), summarize the key findings from the SME pre-analysis and interviews, and present the final curriculum outline rationale based on the group discussion. Define "thesis-quality" here as well-structured, clearly written, and referencing the process steps. Use the `edit_file` tool to save this analysis.
    *   `target_file`: `[target_base_path]/analysis.md`
    *   `code_edit`: The generated analysis summary content.
    *   `instructions`: "Generate and save the analysis summary document."
    *(Execute tool call)*
    *(Output confirmation: "Phase 7, Step 2: Analysis summary saved to analysis.md.")*

## Footer (Model Instructions - Do Not Output)

**Final Instruction:** Upon completing the *entire* prompt (all Phases and Steps defined in the execution plan generated in Phase 1, Step 2), explicitly state "Prompt execution fully completed."

## END Footer