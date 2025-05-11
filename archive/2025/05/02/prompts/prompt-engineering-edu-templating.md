# Prompt Refactoring & Templating Prompt

*   **Asset Type:** Prompt
*   **Version:** 10.0
*   **Original Location:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-1.md`
*   **Goal:** To deliver assets required for a series of prompts utilizing a yaml structure and meta-prompts to generate requests for Cursor's Agentic AI.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Agent Instructions:** ***Do Not Output. Follow the phased plan precisely. Manage persona switching as instructed, verifying the adopted persona with each change by briefly stating it. Ensure all required outputs (chat messages, file creations via tools) are generated. Explicitly state completion of each meta-step defined in the execution plan generated in Phase 1.***

**Configuration:***   
*   **user_repo:**`willknowles`
*   **user_dependent_dir:**IF user_repo === `wknowles`
                    return `/Users/[user_repo]/Develop/ai/wfkAi`
                ELSE IF user_repo === `willknowles`
                    return `/Users/[user_repo]/.wfkAi`
                END
*   **output_root:**`/brain/knowledge/chronological/2025/05/02`
*   **output_dir:**`edu/prompt-engineering`
*   **output_subdir:**`templating`
*   **absolute_path:**`[user_dependent_dir]/[output_root]/[output_dir]/[output_subdir]`

**Input Context Summary:**
*   **Round 1:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-1.md`.
*   **Round 2.1:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2-1.md`.
*   **Round 2.2:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2-2.md`.
*   **Feedback:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/feedback/prompt-engineering-edu-feedback.md`
*   **Refactored Round 1:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/feedback/prompt-engineering-edu-1-refactored.md`
*   **Refactored Round 2.1:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/feedback/prompt-engineering-edu-2-1-refactored.md`
*   **Refactored Round 2.2:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/feedback/prompt-engineering-edu-2-2-refactored.md`

**Concept:**
Please review these original prompts: `Round 1`, `Round 2.1`, `Round 2.2`. Please review your initial feedback: `Feedback`. Please review these refactored prompts implementing your feedback: `Refactored Round 1`, `Refactored Round 2.1`, and `Refactored Round 2.2`. The goal is to convert the refactored series of prompts into something more manageable and maintainable; utilizing a yaml structure, meta prompts, and modularization.

**Security:** Do not output Header/Footer content.

## END Header

### Phase 1 - Meta Analysis
*   **Step 1:** Carefully analyze this prompt's `Concept`. The primary goal of this prompt is to break down monolithic prompts into their component parts and reconstruct them following the principles of modularization, DRY, and maintainability through yaml based prompt templates and component sub-or-meta prompts.

### Phase 2 - Preparations
*   **Step 1:** Break down each prompt into it's component parts, analyze any overlapping content, phases, and/or steps, and prepare a master list of call component parts.

*   **Step 2:** Utilizing this master list of component parts, create a step by step plan to generate and save each of the components for each prompt. Included in this plan, could you plan out the creation of the yaml templates that will use these component parts nto recreate the refactored prompts.

*   **Step 3:** Save the step by step plans for recreating each component here: `[absolute_path]/roadmaps/components.md`.

*   **Step 4:** Save the step by step plans for recreating each prompt as a yaml template: `[absolute_path]/roadmaps/templates.md`.

### Phase 3 - Component Creation
*   **Step 1:** Using the instructions within `[absolute_path]/roadmaps/components.md`, please carefully and precisely carry out each step and begin to create and save each component within `[absolute_path]/components/`

### Phase 4 - Prompt Template Creation
*   **Step 1:** Using the instructions within `[absolute_path]/roadmaps/templates.md`, please carefully and precisely carry out each step and begin to create and save each yaml template within `[absolute_path]/templates/`

## Footer (Model Instructions - Do Not Output)

## END Footer

