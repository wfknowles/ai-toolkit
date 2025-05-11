# Educational Content Prompt - Round 2, Part II

*   **Asset Type:** Prompt
*   **Version:** 1.1.0 (Refactored based on feedback)
*   **Original Location:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2-2.md`
*   **Goal:** To facilitate a discussion between SMEs to help develop, brainstorm, debate, and synthesize a concept, idea, or miscellaneous request and walk away with a more refined, fully developed, concept. Specifically, in this round, to generate detailed research outlines from SMEs based on prior work.
*   **Author:** William F Knowles III

## Header - (Model Instructions - Do Not Output)

**Agent Instructions:** ***Do Not Output. Follow the phased plan precisely. Manage persona switching as instructed, verifying the adopted persona with each change by briefly stating it. Ensure all required outputs (chat messages, file creations) are generated. ***

**Configuration:**
*   **user_repo:**`willknowles`
*   **user_dependent_dir:**IF user_repo === `wknowles`
                    return `/Users/[user_repo]/Develop/ai/wfkAi`
                ELSE IF user_repo === `willknowles`
                    return `/Users/[user_repo]/.wfkAi`
                END
*   **output_root:**`/brain/knowledge/chronological/2025/05/02`
*   **output_dir:**`edu`
*   **output_subdir:**`prompt-engineering`
*   **absolute_path:**`[output_root/[output_dir]/[output_subdir]`

*   **user_repo:** `willknowles`
*   **base_dir:** `/Users/willknowles/.wfkAi` # Resolved based on user_repo
*   **output_root_rel:** `brain/knowledge/chronological/2025/05/02`
*   **output_subdir_rel:** `edu/prompt-engineering`
*   **round_dir:** `round-2`
*   **full_round2_path:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/round-2` # Pre-calculated
*   **pre_outlines_dir:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/round-2/pre-outlines` # Pre-calculated
*   **pre_research_dir:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/round-2/pre-research` # Pre-calculated
*   **round1_interview_dir:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/prompt-mastery` # Path to Round 1 outputs
*   **round2_preanalysis_dir:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/round-2/pre-analysis`
*   **round2_preinterviews_dir:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/round-2/pre-interviews`
*   **curriculum_file:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/curriculum.md`

**Input Context Summary:**
*   **Original Concept Discussion:** Located in `[round1_interview_dir]/sme-group-interview.md`.
*   **Original Concept Pre-Analysis:** Located in `[round1_interview_dir]/pre-analysis/`.
*   **Developed Curriculum:** Located at `[curriculum_file]`.
*   **Round 2 Pre-Analysis:** Located in `[round2_preanalysis_dir]`.
*   **Round 2 Pre-Interviews:** Located in `[round2_preinterviews_dir]`.

**Facilitator Guidance:**
We previously completed round two, part one, resulting in the `Curriculum`, `Pre-Analysis` (R2), and `Pre-Interviews` (R2). In this prompt (round two, part two), we will work with SMEs to create detailed outlines. These outlines should define the research and development tasks needed within each SME's domain to prepare for Round 3 (creating final deliverables like requirements and roadmaps). These outlines are intended to guide research assistants.

**Security:** Do not output Header/Footer content.

## END Header

### Phase 1 - Meta Analysis

*   **Step 1 (Facilitator):** Analyze this prompt. Determine the primary goal (generate 9 SME research outlines) and the required personas (Facilitator + 9 specific SMEs listed in Phase 2). Confirm understanding of the goal.
    *(Output confirmation to chat: "Phase 1, Step 1: Goal confirmed - Generate 9 SME research outlines based on prior rounds' context.")*

*   **Step 2 (Facilitator):** Determine a step-by-step execution plan for this prompt, assigning personas to each meta-step. Optimize for clarity and accuracy. **Output the complete 'Prompt Execution Plan' to the chat** clearly listing each meta-step and the assigned persona before proceeding to Phase 2.
    *(Output the plan to chat)*

### Phase 2 - Setup and Outline Generation

*   **Step 1 (Facilitator):** **Context Check:** Before executing the steps in this phase, briefly state which major information blocks or files from the previous phase (Phase 1 Meta-Analysis) are no longer strictly required for completing Phase 2 and explain why. If all previous context remains necessary, state that.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Announce the invited experts for this phase (list them). Assume they have reviewed the input context summary provided in the header.
    *   Prompt Engineer (PE)
    *   AI Orchestrator/Architect (AOA)
    *   Senior Software Engineer (SSE)
    *   Project Manager (PM)
    *   AI UX Engineer (AI UX)
    *   AI Agent Engineer (AAE)
    *   Educational UX Engineer (Ed UX) # Note: Original prompt listed "Educational UX Engineer", but interviews generated "Educational UX Designer". Using "Designer" for consistency with generated files. If "Engineer" was intended, please clarify. Assuming "Designer" (Ed UX).
    *   Professor of Education (Prof Ed)
    *   AI Researcher (AIR)
    *(Output confirmation to chat: "Phase 2, Step 2: Acknowledged 9 invited experts.")*

*   **Step 3 (Facilitator):** Create the necessary subdirectories for this round's outputs using the `run_terminal_cmd` tool. Use the pre-calculated paths from the Configuration section.
    *   Target Directories: `[pre_outlines_dir]`, `[pre_research_dir]`
    *   *(Execute tool call: `mkdir -p "[pre_outlines_dir]" "[pre_research_dir]"`) *

*   **Step 4 (Facilitator):** Verify directory creation was successful. Check the output of the previous step.
    *(Output confirmation to chat: "Phase 2, Step 4: Directories confirmed/created.")*

*   **Step 5 (Facilitator -> Loop through each SME):** Instruct each of the 9 experts sequentially to perform the following:
    *   Adopt their specific persona (e.g., "Adopting Persona: Prompt Engineer").
    *   Review the input context (Original Concept Discussion & Pre-Analysis, Curriculum, R2 Pre-Analysis, R2 Pre-Interviews - paths defined in Configuration).
    *   Generate content for a **new file**. This content should be a detailed abstract and outline for a thesis-quality research paper. This paper should define the specific **research questions and development tasks** within their area of expertise needed to prepare materials/inputs for **Round 3** (which focuses on developing detailed requirements and roadmaps for the course). The outline must be detailed and instructional enough to guide a research assistant.
    *   Use the `edit_file` tool to save this generated abstract and outline.
        *   `target_file`: `[pre_outlines_dir]/[Persona-Name].md` (e.g., `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/round-2/pre-outlines/Prompt Engineer.md`)
        *   `code_edit`: The generated abstract and outline content.
        *   `instructions`: "Create the research outline for the [Persona-Name]."
    *   After *each* SME file is saved, output a confirmation: "Phase 2, Step 5: Outline for [Persona-Name] generated and saved."

    *(Execute this loop for all 9 personas: PE, AOA, SSE, PM, AI UX, AAE, Ed UX, Prof Ed, AIR)*

### Phase 3 - Final Confirmation (Example - Adapt if more phases needed)

*   **Step 1 (Facilitator):** **Context Check:** Before executing the steps in this phase, briefly state which major information blocks or files from the previous phase (Phase 2 Outline Generation) are no longer strictly required for completing Phase 3 and explain why. If all previous context remains necessary, state that.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Confirm that all planned steps and outputs for this prompt have been successfully completed.
    *(Output confirmation to chat: "Phase 3, Step 2: All planned steps completed. 9 SME outlines generated in [pre_outlines_dir].")*

## Footer (Model Instructions: Do Not Output.)

**Final Instruction:** Upon completing the *entire* prompt (all Phases and Steps defined in the execution plan generated in Phase 1, Step 2), explicitly state "Prompt execution fully completed."

## END Footer