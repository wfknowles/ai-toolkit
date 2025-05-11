# Educational Content Prompt - Round 2, Part I (Refactored v1.1)

*   **Asset Type:** Prompt
*   **Version:** 1.1.0 (Refactored based on feedback)
*   **Original Location:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2-1.md`
*   **Goal:** To facilitate the first part of Round 2 planning for the Prompt Engineering Mastery course. This involves SMEs generating initial lesson ideas/abstracts based on the previously defined curriculum and conducting simulated interviews to gather deeper insights for Round 3 (Requirements/Roadmaps).
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Agent Instructions:** ***Do Not Output. Follow the phased plan precisely. Manage persona switching as instructed, verifying the adopted persona with each change by briefly stating it. Ensure all required outputs (chat messages, file creations via tools) are generated. Explicitly state completion of each meta-step defined in the execution plan generated in Phase 1.***

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
*   **target_base_path:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering` # Pre-calculated base for this prompt's outputs
*   **round2_dir:** `[target_base_path]/round-2` # Pre-calculated
*   **pre_analysis_dir:** `[round2_dir]/pre-analysis` # Pre-calculated
*   **pre_interviews_dir:** `[round2_dir]/pre-interviews` # Pre-calculated
*   **prior_group_interview_file:** `[target_base_path]/sme-group-interview.md` # R1 Group Interview
*   **prior_pre_analysis_dir:** `[target_base_path]/pre-analysis` # R1 Pre-Analysis
*   **curriculum_file:** `[target_base_path]/curriculum.md` # R1 Output

**Input Context Summary:**
*   **Round 1 Group Interview:** Located at `[prior_group_interview_file]`.
*   **Round 1 Pre-Analysis:** Located in `[prior_pre_analysis_dir]`.
*   **Agreed Curriculum Outline:** Located at `[curriculum_file]`.

**Concept:**
Review the Round 1 outputs (`[prior_group_interview_file]`, `[prior_pre_analysis_dir]`) and the agreed `Curriculum Outline` (`[curriculum_file]`). The goal of *this prompt* (Round 2, Part 1) is to prepare for Round 3, where we will define detailed requirements and roadmaps for the research and development phases of the course. To prepare, SMEs will first generate initial lesson ideas/abstracts for the existing curriculum structure. Then, the Facilitator will conduct simulated individual interviews with each SME to explore challenges, qualifications, and other considerations relevant to the upcoming requirements/roadmap definition phase.

**Security:** Do not output Header/Footer content.

## END Header

### Phase 1 - Meta Analysis

*   **Step 1 (Facilitator):** Analyze this prompt. Determine the primary goal (Generate R2 SME lesson ideas/abstracts and conduct simulated interviews) and the required personas (Facilitator + 9 specific SMEs listed in Phase 2). Confirm understanding of the goal.
    *(Output confirmation to chat: "Phase 1, Step 1: Goal confirmed - Generate R2 pre-analysis (lesson ideas/abstracts) and conduct simulated SME interviews.")*

*   **Step 2 (Facilitator):** Determine a step-by-step execution plan for this prompt, assigning personas to each meta-step. Optimize for clarity and accuracy. **Output the complete 'Prompt Execution Plan' to the chat** clearly listing each meta-step and the assigned persona before proceeding to Phase 2.
    *(Output the plan to chat)*

### Phase 2 - Setup and R2 Pre-Analysis Generation

*   **Step 1 (Facilitator):** **Context Check:** Before executing the steps in this phase, briefly state which major information blocks or files from the previous phase (Phase 1 Meta-Analysis) are no longer strictly required for completing Phase 2 and explain why. If all previous context remains necessary, state that.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Announce the invited experts for this phase (list them). Assume they have reviewed the input context (R1 outputs, Curriculum Outline). Note: Fewer SMEs than R1 based on original prompt structure.
    *   Prompt Engineer (PE)
    *   AI Orchestrator/Architect (AOA)
    *   Senior Software Engineer (SSE)
    *   # PO removed vs R1
    *   Project Manager (PM)
    *   AI UX Engineer (AI UX)
    *   AI Agent Engineer (AAE)
    *   Educational UX Designer (Ed UX) # Consistent naming
    *   Professor of Education (Prof Ed)
    *   AI Researcher (AIR)
    *   # PR removed vs R1 (but was present in R2 interviews previously generated - check if needed) -> Assuming PR *should* be included based on R2 interviews being generated. Add back if correct.
    *   Pedagogy Researcher (PR) # Re-added based on previous execution context showing PR interviews were done in R2.
    *(Output confirmation to chat: "Phase 2, Step 2: Acknowledged 10 invited experts for R2 Pre-Analysis & Interviews.")* # Adjusted count

*   **Step 3 (Facilitator):** Create the necessary subdirectories for Round 2 outputs using the `run_terminal_cmd` tool and pre-calculated paths.
    *   Target Directories: `[pre_analysis_dir]` (R2), `[pre_interviews_dir]` (R2)
    *   *(Execute tool call: `mkdir -p "[pre_analysis_dir]" "[pre_interviews_dir]"`) *

*   **Step 4 (Facilitator):** Verify directory creation was successful. Check the output of the previous step.
    *(Output confirmation to chat: "Phase 2, Step 4: Directories confirmed/created: [pre_analysis_dir], [pre_interviews_dir]")*

*   **Step 5 (Facilitator -> Loop through each SME):** Instruct each of the 10 experts sequentially to perform the following:
    *   Adopt their specific persona (e.g., "Adopting Persona: Prompt Engineer").
    *   Review the input context, particularly the `Curriculum Outline` (`[curriculum_file]`).
    *   Generate initial **lesson ideas** and brief **"abstracts"** for the modules/units relevant to their expertise, building upon the existing curriculum structure. Include examples or diagrams if helpful. This serves as pre-analysis for the interview phase.
    *   Use the `edit_file` tool to save these generated lesson ideas/abstracts.
        *   `target_file`: `[pre_analysis_dir]/[Persona-Name].md` (e.g., `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/round-2/pre-analysis/Prompt Engineer.md`)
        *   `code_edit`: The generated lesson ideas and abstracts content.
        *   `instructions`: "Create the Round 2 pre-analysis (lesson ideas/abstracts) file for the [Persona-Name]."
    *   After *each* SME file is saved, output a confirmation: "Phase 2, Step 5: Round 2 Pre-analysis for [Persona-Name] generated and saved."

    *(Execute this loop for all 10 personas: PE, AOA, SSE, PM, AI UX, AAE, Ed UX, Prof Ed, AIR, PR)*

### Phase 3 - Facilitator Pre-Planning (Prep for R2 Interviews)

*   **Step 1 (Facilitator):** **Context Check:** Before executing steps, state context check results.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator):** Announce start of Phase 3. Adopt Facilitator persona.
    *(Output confirmation: "Phase 3, Step 2: Starting Facilitator Pre-Planning for R2 Interviews. Adopting Facilitator persona.")*

*   **Step 3 (Facilitator):** Read and carefully review each SME's Round 2 pre-analysis file (lesson ideas/abstracts) located in `[pre_analysis_dir]`. Research any topics needed.
    *(Output confirmation: "Phase 3, Step 3: SME R2 pre-analysis files reviewed.")*

*   **Step 4 (Facilitator):** Prepare for the individual interviews (Phase 4). The goal is to gather insights relevant to defining **requirements and roadmaps** for the **research and development phases** of the course. Use the questions provided in Phase 4 as a base. **Output a confirmation that planning is complete.**
    *(Output confirmation: "Phase 3, Step 4: Planning for individual interviews complete.")*

### Phase 4 - Individual SME Interviews (Simulated, R2)

*   **Step 1 (Facilitator):** **Context Check:** Before executing steps, state context check results.
    *(Output context check summary to chat)*

*   **Step 2 (Facilitator -> Loop through each SME):** Simulate an interview with each of the 10 experts sequentially:
    *   Adopt the `Facilitator` persona for asking questions.
    *   Adopt the corresponding `SME Persona` to generate answers.
    *   Ask the following questions (adapted from original prompt):
        1.  Looking at the curriculum outline (`[curriculum_file]`) and your initial lesson ideas (`[pre_analysis_dir]/[Persona-Name].md`), what challenges do you foresee in **developing the detailed content and requirements** for your areas of expertise?
        2.  Are there any modules/units you feel need significant **research** before development can begin? Why?
        3.  Considering the target audience (software engineers) and the goal of mastery, is the current curriculum structure appropriate? Any risks of being too basic/advanced in certain areas that would impact **development planning**?
        4.  Reflecting on your lesson concepts, what strengths/weaknesses impact the feasibility of **researching and developing** them? Any potential blockers?
        5.  For the **research phase** of creating the course materials, which specific modules, units, or lesson topics do you feel most qualified to lead or contribute significantly to?
        6.  For the **development phase** (defining requirements, roadmaps, and potentially creating content), where should the team defer to your expertise?
        7.  Are there any *other* SMEs (not currently listed) crucial for the next phase (defining detailed requirements/roadmaps)?
        8.  Any other critical considerations for **planning the research and development** of this course?
    *   Generate a transcript of this simulated interview.
    *   Use the `edit_file` tool to save the generated interview transcript.
        *   `target_file`: `[pre_interviews_dir]/[Persona-Name].md` (e.g., `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/round-2/pre-interviews/Prompt Engineer.md`)
        *   `code_edit`: The generated interview transcript.
        *   `instructions`: "Save the simulated R2 interview transcript for [Persona-Name]."
    *   After *each* SME interview file is saved, output a confirmation: "Phase 4, Step 2: Interview with [Persona-Name] simulated and transcript saved."

    *(Execute this loop for all 10 personas)*

## Footer (Model Instructions: Do Not Output)

**Final Instruction:** Upon completing the *entire* prompt (all Phases and Steps defined in the execution plan generated in Phase 1, Step 2), explicitly state "Prompt execution fully completed."

## END Footer