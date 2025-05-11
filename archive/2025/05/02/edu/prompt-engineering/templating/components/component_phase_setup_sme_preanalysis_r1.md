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