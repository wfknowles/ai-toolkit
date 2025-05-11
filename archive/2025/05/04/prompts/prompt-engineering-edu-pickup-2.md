# Prompt Refactoring & Templating Prompt

*   **Asset Type:** Prompt
*   **Version:** 10.0
*   **Original Location:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/04/prompts/prompt-engineering-edu-pickup.md`
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
*   **Originating Prompt:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-1.md`
*   **Previous Prompt:**`/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2-2.md`
*   **Pre-Analysis:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/pre-analysis`
*   **Next Step:** Located in `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2-2.md`

**Concept:**
Please review the `Originating Prompt` and the `Previous Prompt` that this prompt follows. The previous prompt's output is within here: `Pre-Analysis`. Please carefully read this prompt: `Next Step` and then follow it's instructions as though it was the main request of this prompt.

**Security:** Do not output Header/Footer content.

## END Header

## Footer (Model Instructions - Do Not Output)

## END Footer