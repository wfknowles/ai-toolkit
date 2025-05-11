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