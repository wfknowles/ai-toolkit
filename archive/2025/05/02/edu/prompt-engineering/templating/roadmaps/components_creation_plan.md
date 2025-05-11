# Component Creation Plan

This plan outlines the steps to generate modular components based on the analysis of the refactored prompts. Each component will be saved as a separate file in the `components` directory.

1.  **`component_metadata.md`:**
    *   **Content:** Markdown block containing standard metadata fields with placeholders.
        ```markdown
        *   **Asset Type:** Prompt
        *   **Version:** {{Version}}
        *   **Original Location:** {{Original_Location}}
        *   **Goal:** {{Goal}}
        *   **Author:** William F Knowles III
        ```
    *   **Action:** Save content to `[components_dir]/component_metadata.md`.

2.  **`component_agent_instructions.md`:**
    *   **Content:** Standardized agent instructions for header.
        ```markdown
        **Agent Instructions:** ***Do Not Output. Follow the phased plan precisely. Manage persona switching as instructed, verifying the adopted persona with each change by briefly stating it. Ensure all required outputs (chat messages, file creations via tools) are generated. Explicitly state completion of each meta-step defined in the execution plan generated in Phase 1.***
        ```
    *   **Action:** Save content to `[components_dir]/component_agent_instructions.md`.

3.  **`component_configuration_base.md`:**
    *   **Content:** Base configuration variables.
        ```markdown
        **Configuration:**
        *   **user_repo:** `willknowles`
        *   **base_dir:** `/Users/willknowles/.wfkAi` # Resolved based on user_repo
        ```
    *   **Action:** Save content to `[components_dir]/component_configuration_base.md`.

4.  **`component_configuration_paths_r1.md`:**
    *   **Content:** Path definitions specific to Round 1 (initial outline generation).
        ```markdown
        *   **output_root_rel:** `brain/knowledge/chronological/2025/05/02`
        *   **output_dir_rel:** `edu`
        *   **output_subdir_rel:** `prompt-engineering`
        *   **round1_brainstorm_dir:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/prompt-mastery` # Path to initial brainstorm outputs
        *   **target_base_path:** `{{base_dir}}/{{output_root_rel}}/{{output_dir_rel}}/{{output_subdir_rel}}` # Example calculation
        *   **pre_analysis_dir:** `{{target_base_path}}/pre-analysis`
        ```
    *   **Action:** Save content to `[components_dir]/component_configuration_paths_r1.md`.

5.  **`component_configuration_paths_r2_1.md`:**
    *   **Content:** Path definitions specific to Round 2.1 (lesson ideas/interviews).
        ```markdown
        *   **output_root_rel:** `brain/knowledge/chronological/2025/05/02`
        *   **output_dir_rel:** `edu`
        *   **output_subdir_rel:** `prompt-engineering`
        *   **target_base_path:** `{{base_dir}}/{{output_root_rel}}/{{output_dir_rel}}/{{output_subdir_rel}}`
        *   **round2_dir:** `{{target_base_path}}/round-2`
        *   **pre_analysis_dir:** `{{round2_dir}}/pre-analysis`
        *   **pre_interviews_dir:** `{{round2_dir}}/pre-interviews`
        *   **prior_group_interview_file:** `{{target_base_path}}/sme-group-interview.md` # R1 Group Interview
        *   **prior_pre_analysis_dir:** `{{target_base_path}}/pre-analysis` # R1 Pre-Analysis
        *   **curriculum_file:** `{{target_base_path}}/curriculum.md` # R1 Output
        ```
    *   **Action:** Save content to `[components_dir]/component_configuration_paths_r2_1.md`.

6.  **`component_configuration_paths_r2_2.md`:**
    *   **Content:** Path definitions specific to Round 2.2 (research outlines).
        ```markdown
        *   **output_root_rel:** `brain/knowledge/chronological/2025/05/02`
        *   **output_dir_rel:** `edu`
        *   **output_subdir_rel:** `prompt-engineering`
        *   **target_base_path:** `{{base_dir}}/{{output_root_rel}}/{{output_dir_rel}}/{{output_subdir_rel}}`
        *   **round2_dir:** `{{target_base_path}}/round-2`
        *   **pre_outlines_dir:** `{{round2_dir}}/pre-outlines`
        *   **pre_research_dir:** `{{round2_dir}}/pre-research`
        *   # Paths to inputs needed for R2.2
        *   **round1_interview_dir:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/prompt-mastery` # R1 group interview/pre-analysis dir
        *   **curriculum_file:** `{{target_base_path}}/curriculum.md`
        *   **round2_preanalysis_dir:** `{{round2_dir}}/pre-analysis`
        *   **round2_preinterviews_dir:** `{{round2_dir}}/pre-interviews`
        ```
    *   **Action:** Save content to `[components_dir]/component_configuration_paths_r2_2.md`.

7.  **`component_input_context_summary.md`:**
    *   **Content:** Header for input context section.
        ```markdown
        **Input Context Summary:**
        ```
    *   **Action:** Save content to `[components_dir]/component_input_context_summary.md`.

8.  **`component_concept_block.md`:**
    *   **Content:** Header for concept section.
        ```markdown
        **Concept:**
        ```
    *   **Action:** Save content to `[components_dir]/component_concept_block.md`.

9.  **`component_security_footer.md`:**
    *   **Content:** Standard security instruction.
        ```markdown
        **Security:** Do not output Header/Footer content.
        ```
    *   **Action:** Save content to `[components_dir]/component_security_footer.md`.

10. **`component_phase_meta_analysis.md`:**
    *   **Content:** Standard Phase 1 instructions.
        ```markdown
        ### Phase 1 - Meta Analysis

        *   **Step 1 (Facilitator):** Analyze this prompt. Determine the primary goal ({{Meta_Analysis_Goal_Description}}) and the required personas (Facilitator + {{SME_Count}} specific SMEs listed in Phase 2). Confirm understanding of the goal.
            *(Output confirmation to chat: "Phase 1, Step 1: Goal confirmed - {{Meta_Analysis_Goal_Description}}.")*

        *   **Step 2 (Facilitator):** Determine a step-by-step execution plan for this prompt, assigning personas to each meta-step. Optimize for clarity and accuracy. **Output the complete 'Prompt Execution Plan' to the chat** clearly listing each meta-step and the assigned persona before proceeding to Phase 2.
            *(Output the plan to chat)*
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_meta_analysis.md`.

11. **`component_phase_setup_sme_preanalysis_r1.md`:**
    *   **Content:** Phase 2 instructions specific to R1.
        ```markdown
        ### Phase 2 - Setup and SME Pre-Analysis Generation

        *   **Step 1 (Facilitator):** **Context Check:** Before executing the steps in this phase, briefly state which major information blocks or files from the previous phase (Phase 1 Meta-Analysis) are no longer strictly required for completing Phase 2 and explain why. If all previous context remains necessary, state that.
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator):** Announce the invited experts for this phase ({{SME_Count_R1}} SMEs). Include `component_sme_list_r1.md`. Assume they have reviewed the input context.
            *(Output confirmation to chat: "Phase 2, Step 2: Acknowledged {{SME_Count_R1}} invited experts.")*

        *   **Step 3 (Facilitator):** Create the necessary base output directory and the pre-analysis subdirectory using the `run_terminal_cmd` tool and pre-calculated paths.
            *   Target Directories: `{{target_base_path}}`, `{{pre_analysis_dir}}`
            *   *(Execute tool call: `mkdir -p "{{pre_analysis_dir}}"`) *

        *   **Step 4 (Facilitator):** Verify directory creation was successful. Check the output of the previous step.
            *(Output confirmation to chat: "Phase 2, Step 4: Directories confirmed/created: {{pre_analysis_dir}}")*

        *   **Step 5 (Facilitator -> Loop through each SME):** Instruct each of the {{SME_Count_R1}} experts sequentially (from `component_sme_list_r1.md`):
            *   Adopt their specific persona.
            *   Review the input context (Concept Discussion & Concept Pre-Analysis).
            *   Generate initial thoughts, concerns, feedback, or high-level section ideas for the course outline.
            *   Use the `edit_file` tool to save this generated analysis/feedback.
                *   `target_file`: `{{pre_analysis_dir}}/[Persona-Name].md`
                *   `code_edit`: The generated analysis/feedback content.
                *   `instructions`: "Create the initial pre-analysis file for the [Persona-Name]."
            *   After *each* SME file is saved, output a confirmation: "Phase 2, Step 5: Pre-analysis for [Persona-Name] generated and saved."
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_setup_sme_preanalysis_r1.md`.

12. **`component_phase_setup_sme_preanalysis_r2.md`:**
    *   **Content:** Phase 2 instructions specific to R2.1.
        ```markdown
        ### Phase 2 - Setup and R2 Pre-Analysis Generation

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator):** Announce invited experts ({{SME_Count_R2}} SMEs). Include `component_sme_list_r2.md`. Assume review of R1 outputs & Curriculum.
            *(Output confirmation to chat: "Phase 2, Step 2: Acknowledged {{SME_Count_R2}} invited experts for R2 Pre-Analysis & Interviews.")*

        *   **Step 3 (Facilitator):** Create R2 subdirectories.
            *   Target Directories: `{{pre_analysis_dir}}` (R2), `{{pre_interviews_dir}}` (R2)
            *   *(Execute tool call: `mkdir -p "{{pre_analysis_dir}}" "{{pre_interviews_dir}}"`) *

        *   **Step 4 (Facilitator):** Verify directory creation.
            *(Output confirmation to chat: "Phase 2, Step 4: Directories confirmed/created: {{pre_analysis_dir}}, {{pre_interviews_dir}}")*

        *   **Step 5 (Facilitator -> Loop through each SME):** Instruct each of the {{SME_Count_R2}} experts sequentially (from `component_sme_list_r2.md`):
            *   Adopt persona.
            *   Review input context (esp. Curriculum Outline).
            *   Generate initial lesson ideas and abstracts for relevant modules/units.
            *   Use `edit_file` to save.
                *   `target_file`: `{{pre_analysis_dir}}/[Persona-Name].md`
                *   `code_edit`: Generated lesson ideas/abstracts.
                *   `instructions`: "Create the Round 2 pre-analysis (lesson ideas/abstracts) file for the [Persona-Name]."
            *   Output confirmation: "Phase 2, Step 5: Round 2 Pre-analysis for [Persona-Name] generated and saved."
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_setup_sme_preanalysis_r2.md`.

13. **`component_phase_setup_sme_outlines_r2_2.md`:**
    *   **Content:** Phase 2 instructions specific to R2.2.
        ```markdown
        ### Phase 2 - Setup and Outline Generation

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator):** Announce invited experts ({{SME_Count_R2_2}} SMEs - likely 9). Include `component_sme_list_r2_2.md`. Assume review of R1/R2 inputs & Curriculum.
            *(Output confirmation to chat: "Phase 2, Step 2: Acknowledged {{SME_Count_R2_2}} invited experts.")*

        *   **Step 3 (Facilitator):** Create R2 outline/research subdirectories.
            *   Target Directories: `{{pre_outlines_dir}}`, `{{pre_research_dir}}`
            *   *(Execute tool call: `mkdir -p "{{pre_outlines_dir}}" "{{pre_research_dir}}"`) *

        *   **Step 4 (Facilitator):** Verify directory creation.
            *(Output confirmation to chat: "Phase 2, Step 4: Directories confirmed/created: {{pre_outlines_dir}}, {{pre_research_dir}}")*

        *   **Step 5 (Facilitator -> Loop through each SME):** Instruct each of the {{SME_Count_R2_2}} experts sequentially (from `component_sme_list_r2_2.md`):
            *   Adopt persona.
            *   Review input context (Concept, Curriculum, R2 Pre-Analysis, R2 Pre-Interviews).
            *   Generate detailed abstract and outline for a thesis-quality research paper defining R&D tasks for Round 3 (requirements/roadmaps).
            *   Use `edit_file` to save.
                *   `target_file`: `{{pre_outlines_dir}}/[Persona-Name].md`
                *   `code_edit`: Generated abstract and outline.
                *   `instructions`: "Create the research outline for the [Persona-Name]."
            *   Output confirmation: "Phase 2, Step 5: Outline for [Persona-Name] generated and saved."
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_setup_sme_outlines_r2_2.md`.

14. **`component_sme_list_r1.md`:**
    *   **Content:** List of 11 SMEs.
        ```markdown
        *   Prompt Engineer (PE)
        *   AI Orchestrator/Architect (AOA)
        *   Senior Software Engineer (SSE)
        *   Product Owner (PO)
        *   Project Manager (PM)
        *   AI UX Engineer (AI UX)
        *   AI Agent Engineer (AAE)
        *   Pedagogy Researcher (PR)
        *   Educational UX Designer (Ed UX)
        *   Professor of Education (Prof Ed)
        *   AI Researcher (AIR)
        ```
    *   **Action:** Save content to `[components_dir]/component_sme_list_r1.md`.

15. **`component_sme_list_r2.md`:**
    *   **Content:** List of 10 SMEs for R2.1/R2.2 (Standardized).
        ```markdown
        *   Prompt Engineer (PE)
        *   AI Orchestrator/Architect (AOA)
        *   Senior Software Engineer (SSE)
        *   Project Manager (PM)
        *   AI UX Engineer (AI UX)
        *   AI Agent Engineer (AAE)
        *   Educational UX Designer (Ed UX)
        *   Professor of Education (Prof Ed)
        *   AI Researcher (AIR)
        *   Pedagogy Researcher (PR)
        ```
    *   **Action:** Save content to `[components_dir]/component_sme_list_r2.md`.

16. **`component_phase_facilitator_planning_pre_interview_r1.md`:**
    *   **Content:** Phase 3 instructions for R1.
        ```markdown
        ### Phase 3 - Facilitator Pre-Planning (Round 1 - Prep for Interviews)

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator):** Announce start of Phase 3. Adopt Facilitator persona.
            *(Output confirmation: "Phase 3, Step 2: Starting Facilitator Pre-Planning (Round 1). Adopting Facilitator persona.")*

        *   **Step 3 (Facilitator):** Read and carefully review each SME's pre-analysis file located in `{{pre_analysis_dir}}`. Synthesize key themes, potential conflicts, and areas needing clarification.
            *(Output confirmation: "Phase 3, Step 3: SME pre-analysis files reviewed.")*

        *   **Step 4 (Facilitator):** Based on the review, prepare specific, targeted questions for *each* SME interview (Phase 4). Output the planned interview questions for *each* SME to the chat.
            *(Output planned questions per SME to chat)*
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_facilitator_planning_pre_interview_r1.md`.

17. **`component_phase_facilitator_planning_pre_groupsession_r1.md`:**
    *   **Content:** Phase 5 instructions for R1.
        ```markdown
        ### Phase 5 - Facilitator Pre-Planning (Round 2 - Prep for Group Session)

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator):** Announce start of Phase 5. Adopt Facilitator persona.
            *(Output confirmation: "Phase 5, Step 2: Starting Facilitator Pre-Planning (Round 2). Adopting Facilitator persona.")*

        *   **Step 3 (Facilitator):** Carefully review insights gathered from simulated interviews (Phase 4). Perform qualitative analysis: identify themes, differences, discussion points for group session.
            *(Output summary of analysis to chat: "Phase 5, Step 3: Interview analysis complete. Key themes: [List themes]. Discussion points: [List points].")*

        *   **Step 4 (Facilitator):** Plan the flow and key discussion points for the Phase 6 group session. Output the plan/agenda for Phase 6 to the chat.
            *(Output the plan/agenda for Phase 6 to the chat: "Phase 5, Step 4: Group session plan created.")*
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_facilitator_planning_pre_groupsession_r1.md`.

18. **`component_phase_facilitator_planning_pre_interview_r2.md`:**
    *   **Content:** Phase 3 instructions for R2.1.
        ```markdown
        ### Phase 3 - Facilitator Pre-Planning (Prep for R2 Interviews)

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator):** Announce start of Phase 3. Adopt Facilitator persona.
            *(Output confirmation: "Phase 3, Step 2: Starting Facilitator Pre-Planning for R2 Interviews. Adopting Facilitator persona.")*

        *   **Step 3 (Facilitator):** Read and carefully review each SME's Round 2 pre-analysis file (lesson ideas/abstracts) located in `{{pre_analysis_dir}}`. Research any topics needed.
            *(Output confirmation: "Phase 3, Step 3: SME R2 pre-analysis files reviewed.")*

        *   **Step 4 (Facilitator):** Prepare for the individual interviews (Phase 4). Goal: gather insights for requirements/roadmaps. Use Phase 4 questions as base. Output confirmation.
            *(Output confirmation: "Phase 3, Step 4: Planning for individual interviews complete.")*
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_facilitator_planning_pre_interview_r2.md`.

19. **`component_phase_individual_interviews_simulated_r1.md`:**
    *   **Content:** Phase 4 instructions for R1 (no saving).
        ```markdown
        ### Phase 4 - Individual SME Interviews (Simulated)

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator -> Loop through each SME):** Simulate an interview with each of the {{SME_Count_R1}} experts sequentially:
            *   Adopt Facilitator/SME personas.
            *   Use questions prepared in Phase 3 (challenges, cognitive load, aha moments, blindspots, skeleton ideas).
            *   Generate transcript internally (no saving required by this component).
            *   Output confirmation: "Phase 4, Step 2: Simulated interview with [Persona-Name] completed."
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_individual_interviews_simulated_r1.md`.

20. **`component_phase_individual_interviews_simulated_r2.md`:**
    *   **Content:** Phase 4 instructions for R2.1 (with saving).
        ```markdown
        ### Phase 4 - Individual SME Interviews (Simulated, R2)

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator -> Loop through each SME):** Simulate an interview with each of the {{SME_Count_R2}} experts sequentially:
            *   Adopt Facilitator/SME personas.
            *   Ask the R2 interview questions focusing on R&D planning (challenges, research needs, audience fit, feasibility, qualifications, other SMEs, critical considerations).
            *   Generate transcript.
            *   Use `edit_file` tool to save transcript.
                *   `target_file`: `{{pre_interviews_dir}}/[Persona-Name].md`
                *   `code_edit`: Generated interview transcript.
                *   `instructions`: "Save the simulated R2 interview transcript for [Persona-Name]."
            *   Output confirmation: "Phase 4, Step 2: Interview with [Persona-Name] simulated and transcript saved."
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_individual_interviews_simulated_r2.md`.

21. **`component_phase_group_session_r1.md`:**
    *   **Content:** Phase 6 instructions for R1.
        ```markdown
        ### Phase 6 - Meeting of the Minds (Simulated Group Session)

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator):** Announce start Phase 6. Adopt Facilitator persona.
            *(Output confirmation: "Phase 6, Step 2: Starting Meeting of the Minds simulation.")*

        *   **Step 3 (Facilitator):** Simulate group discussion based on Phase 5 plan (Analysis, Challenges, Outline Skeleton, Outline Flesh). Output transcript to chat or generate internally.

        *   **Step 4 (Facilitator):** Based on discussion consensus, extract and format the high-level curriculum outline. Use `edit_file` to save.
            *   `target_file`: `{{target_base_path}}/curriculum.md`
            *   `code_edit`: Formatted curriculum outline.
            *   `instructions`: "Save the high-level curriculum outline generated from the group discussion."
            *(Execute tool call)*
            *(Output confirmation: "Phase 6, Step 4: Curriculum outline saved to curriculum.md.")*

        *   **Step 5 (Facilitator):** Use `edit_file` to save the full simulated group discussion transcript.
            *   `target_file`: `{{target_base_path}}/sme-group-interview.md`
            *   `code_edit`: Full discussion transcript.
            *   `instructions`: "Save the full transcript of the simulated SME group interview."
            *(Execute tool call)*
            *(Output confirmation: "Phase 6, Step 5: SME group interview transcript saved.")*
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_group_session_r1.md`.

22. **`component_phase_analysis_paper_r1.md`:**
    *   **Content:** Phase 7 instructions for R1.
        ```markdown
        ### Phase 7 - Analysis Paper Generation (Simplified from Original)

        *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
            *(Output context check summary to chat)*

        *   **Step 2 (Facilitator):** Generate a summary analysis document (process, findings, rationale for outline). Define "thesis-quality" as well-structured, clear, referencing process steps. Use `edit_file` to save.
            *   `target_file`: `{{target_base_path}}/analysis.md`
            *   `code_edit`: Generated analysis summary content.
            *   `instructions`: "Generate and save the analysis summary document."
            *(Execute tool call)*
            *(Output confirmation: "Phase 7, Step 2: Analysis summary saved to analysis.md.")*
        ```
    *   **Action:** Save content to `[components_dir]/component_phase_analysis_paper_r1.md`.

23. **`component_final_instruction.md`:**
    *   **Content:** Standard final instruction block.
        ```markdown
        ## Footer (Model Instructions: Do Not Output)

        **Final Instruction:** Upon completing the *entire* prompt (all Phases and Steps defined in the execution plan generated in Phase 1, Step 2), explicitly state "Prompt execution fully completed."

        ## END Footer
        ```
    *   **Action:** Save content to `[components_dir]/component_final_instruction.md`. 