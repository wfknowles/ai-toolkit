# Template Creation Plan

This plan outlines the steps to generate YAML prompt templates that reconstruct the refactored prompts using the modular components.

1.  **`template_edu_r1.yaml`:**
    *   **Goal:** Recreate the Refactored Round 1 prompt using components.
    *   **Structure:**
        ```yaml
        metadata:
          <<: !include ../components/component_metadata.md # Use YAML merge key for metadata
          Version: '1.1.0-template'
          Original_Location: '/path/to/prompt-engineering-edu-1.md'
          Goal: 'Define high-level course outline via simulated SME interaction'

        header_instructions: !include ../components/component_agent_instructions.md

        configuration:
          base: !include ../components/component_configuration_base.md
          paths: !include ../components/component_configuration_paths_r1.md
          # Add specific path values if needed, resolved here or by execution engine

        input_context:
          summary: !include ../components/component_input_context_summary.md
          items:
            - name: Concept Discussion (Brainstorm)
              path: '{{round1_brainstorm_dir}}/sme-group-interview.md' # Variables from config
            - name: Concept Pre-Analysis (Brainstorm)
              path: '{{round1_brainstorm_dir}}/pre-analysis/'

        concept:
          header: !include ../components/component_concept_block.md
          description: |
            Review the previous brainstorming discussion ({{input_context.items[0].path}}) 
            and the initial SME concepts ({{input_context.items[1].path}}). 
            The goal is to synthesize these ideas and define a high-level outline 
            (major sections/units) for an educational course on mastering prompt engineering.

        security_footer: !include ../components/component_security_footer.md

        phases:
          - phase_name: 'Phase 1 - Meta Analysis'
            steps: !include ../components/component_phase_meta_analysis.md
            # Add specific values for placeholders like {{Meta_Analysis_Goal_Description}}
            variables:
               Meta_Analysis_Goal_Description: 'Define high-level course outline via simulated SME interaction'
               SME_Count: 11

          - phase_name: 'Phase 2 - Setup and SME Pre-Analysis Generation'
            steps: !include ../components/component_phase_setup_sme_preanalysis_r1.md
            variables:
               SME_Count_R1: 11
               # Paths will be resolved from configuration block

          - phase_name: 'Phase 3 - Facilitator Pre-Planning (Round 1 - Prep for Interviews)'
            steps: !include ../components/component_phase_facilitator_planning_pre_interview_r1.md

          - phase_name: 'Phase 4 - Individual SME Interviews (Simulated)'
            steps: !include ../components/component_phase_individual_interviews_simulated_r1.md
            variables:
               SME_Count_R1: 11

          - phase_name: 'Phase 5 - Facilitator Pre-Planning (Round 2 - Prep for Group Session)'
            steps: !include ../components/component_phase_facilitator_planning_pre_groupsession_r1.md

          - phase_name: 'Phase 6 - Meeting of the Minds (Simulated Group Session)'
            steps: !include ../components/component_phase_group_session_r1.md

          - phase_name: 'Phase 7 - Analysis Paper Generation (Simplified from Original)'
            steps: !include ../components/component_phase_analysis_paper_r1.md

        final_instruction: !include ../components/component_final_instruction.md
        ```
    *   **Action:** Save structure to `[templates_dir]/template_edu_r1.yaml`.

2.  **`template_edu_r2_1.yaml`:**
    *   **Goal:** Recreate the Refactored Round 2.1 prompt using components.
    *   **Structure:** (Similar YAML structure as R1, but including/referencing R2.1 specific components)
        ```yaml
        metadata:
          <<: !include ../components/component_metadata.md
          Version: '1.1.0-template'
          Original_Location: '/path/to/prompt-engineering-edu-2-1.md'
          Goal: 'Generate R2 SME lesson ideas/abstracts and conduct simulated interviews'

        header_instructions: !include ../components/component_agent_instructions.md

        configuration:
          base: !include ../components/component_configuration_base.md
          paths: !include ../components/component_configuration_paths_r2_1.md

        input_context:
          summary: !include ../components/component_input_context_summary.md
          items:
            - name: Round 1 Group Interview
              path: '{{prior_group_interview_file}}'
            - name: Round 1 Pre-Analysis
              path: '{{prior_pre_analysis_dir}}'
            - name: Agreed Curriculum Outline
              path: '{{curriculum_file}}'

        concept:
          header: !include ../components/component_concept_block.md
          description: |
            Review the Round 1 outputs ({{input_context.items[0].path}}, {{input_context.items[1].path}}) 
            and the agreed Curriculum Outline ({{input_context.items[2].path}}). 
            The goal of this prompt (Round 2, Part 1) is to prepare for Round 3... 
            (Include full concept description)

        security_footer: !include ../components/component_security_footer.md

        phases:
          - phase_name: 'Phase 1 - Meta Analysis'
            steps: !include ../components/component_phase_meta_analysis.md
            variables:
               Meta_Analysis_Goal_Description: 'Generate R2 SME lesson ideas/abstracts and conduct simulated interviews'
               SME_Count: 10 # Or 9 depending on decision

          - phase_name: 'Phase 2 - Setup and R2 Pre-Analysis Generation'
            steps: !include ../components/component_phase_setup_sme_preanalysis_r2.md
            variables:
               SME_Count_R2: 10 # Or 9
               # Paths resolved from config

          - phase_name: 'Phase 3 - Facilitator Pre- Planning (Prep for R2 Interviews)'
            steps: !include ../components/component_phase_facilitator_planning_pre_interview_r2.md

          - phase_name: 'Phase 4 - Individual SME Interviews (Simulated, R2)'
            steps: !include ../components/component_phase_individual_interviews_simulated_r2.md
            variables:
               SME_Count_R2: 10 # Or 9
               # Paths resolved from config

        final_instruction: !include ../components/component_final_instruction.md
        ```
    *   **Action:** Save structure to `[templates_dir]/template_edu_r2_1.yaml`.

3.  **`template_edu_r2_2.yaml`:**
    *   **Goal:** Recreate the *original* Round 2.2 prompt's functionality (generating research outlines) using components and refactored structure.
    *   **Structure:** (Similar YAML structure, referencing R2.2 components)
        ```yaml
        metadata:
          <<: !include ../components/component_metadata.md
          Version: '1.1.0-template' # Based on refactoring principles applied
          Original_Location: '/path/to/prompt-engineering-edu-2-2.md'
          Goal: 'Generate detailed research outlines from SMEs based on prior work'

        header_instructions: !include ../components/component_agent_instructions.md

        configuration:
          base: !include ../components/component_configuration_base.md
          paths: !include ../components/component_configuration_paths_r2_2.md

        input_context:
          summary: !include ../components/component_input_context_summary.md
          items:
             # List inputs needed for R2.2 based on config component
             - name: Curriculum
               path: '{{curriculum_file}}'
             - name: R2 Pre-Analysis
               path: '{{round2_preanalysis_dir}}'
             - name: R2 Pre-Interviews
               path: '{{round2_preinterviews_dir}}'
             # Potentially add R1 interview/pre-analysis if needed by concept
             - name: R1 Group Interview Dir
               path: '{{round1_interview_dir}}'

        concept: # Concept Description for R2.2
          header: !include ../components/component_concept_block.md
          description: |
            Review the agreed upon Curriculum ({{input_context.items[0].path}}), the R2 Pre-Analysis 
            ({{input_context.items[1].path}}), and R2 Pre-Interviews ({{input_context.items[2].path}}). 
            The goal is to work with SMEs to create detailed outlines for pre-researching 
            material needed for Round 3's creation of final deliverables (requirements/roadmaps). 
            You will be guiding research assistants through this pre-research phase via these outlines.

        security_footer: !include ../components/component_security_footer.md

        phases:
          - phase_name: 'Phase 1 - Meta Analysis'
            steps: !include ../components/component_phase_meta_analysis.md
            variables:
               Meta_Analysis_Goal_Description: 'Generate detailed research outlines from SMEs based on prior work'
               SME_Count: 9 # From original R2.2 prompt

          - phase_name: 'Phase 2 - Setup and Outline Generation'
            steps: !include ../components/component_phase_setup_sme_outlines_r2_2.md
            variables:
               SME_Count_R2_2: 9 
               # Paths resolved from config

          # Add other phases from original R2.2 if they were intended, e.g., Facilitator Planning? Asset Creation?
          # The original R2.2 prompt seemed incomplete/confusing in later phases.
          # Adding a simple confirmation phase here based on refactored structure.
          - phase_name: 'Phase 3 - Final Confirmation' 
            steps: |
                *   **Step 1 (Facilitator):** **Context Check:** ... (Standard Context Check) ...
                    *(Output context check summary to chat)*

                *   **Step 2 (Facilitator):** Confirm that all planned steps and outputs for this prompt have been successfully completed.
                    *(Output confirmation to chat: "Phase 3, Step 2: All planned steps completed. 9 SME research outlines generated in {{pre_outlines_dir}}.")*

        final_instruction: !include ../components/component_final_instruction.md
        ```
    *   **Action:** Save structure to `[templates_dir]/template_edu_r2_2.yaml`.

*Note: The `!include` tag is a common convention in YAML for including external file content, but actual support depends on the YAML parser/execution engine. Placeholders like `{{variable}}` would need to be processed by a templating engine (like Jinja2) that loads the YAML.* 