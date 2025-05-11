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