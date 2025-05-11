# Feedback Request Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/04/prompts/prompt-engineering-edu-feedback-loop-2.md`
*   **Goal:** To provide feedback that I can feed into a loop.
*   **Author:** William F Knowles III

## Header - (Model Instructions - Do Not Output)

**Agent Instructions:** ***Do Not Output. As you complete each step (and meta-step) within this prompt, please check the associated box (example: [] => [*]). Verify each check mark after completing checking each step. Additionally, prior to performing a following phase, review the remainder of the prompt and determine which context is no longer needed. Once completed, please offload the context that is no longer needed. Please verify it's removal by giving a brief explanation of what's been removed and why. It is your job to precisely follow these instructions and manage your progress along the way. It is also your job to manage switching out the different persona. Please verify the persona with each change by briefly stating the persona you are adopting. ***

**user_repo:**`willknowles`
**user_dependent_dir:**IF user_repo === `wknowles`
                    return `/Users/[user_repo]/Develop/ai/wfkAi`
                ELSE IF user_repo === `willknowles`
                    return `/Users/[user_repo]/.wfkAi`
                END
**output_root:**`brain/knowledge/chronological/2025/05/04`
**output_dir:**`edu/prompt-engineering`
**output_subdir:**`feedback`
**absolute_path:**`[output_root]/[output_dir]/[output_subdir]`

**source_prompt:**`[user_dependent_dir]/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-templating.md`

**source_prompt_result_dir:**`[user_dependent_dir]/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/templating`

**original_prompts:**
- `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-1.md`
- `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2-1.md`
- `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2-2.md`

**background:** We recently took some monolithic prompts and broke them into a templating strategy. I reviewed what was created here: `source_prompt_result_dir`, and was disappointed with the quality of work. In my prompt here: `source_prompt`, I didn't realize i needed to request complete, production-ready, work. As an assistant, understand concepts of a strategy to recreate my original prompts here: `original_prompts`, IS NOT the same thing as being asked to recreate my original prompts. Can you help me understand where I may have confused you? Or, is there something in your processing that made you think an incomplete work would suffice?

**Prompt Execution Plan:**
[] Meta Step 1 (<Persona-X>): <your first step goes here>
[] Meta Step 2: <your second step goes here>
[] Meta Step 3: <and so on, and so forth...>

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
[] Step 1: Determine a step by step plan to carry this prompt out with extreme efficiency and optimization in mind. Consider slow is okay, but tolerance for errors is low and my expectations of UX are sky high. After determining your plan, please use the current `Prompt Execution Plan` as an example, and replace it within the secure header. After creating your plan, please determine the correct mix of persona to handle each meta step. Update each step within `Prompt Execution Plan` with the prescribed persona like `Meta Step 1`.

[] Step 2: Please consider the `background` and `source_prompt` that these questions are being born out of.

### Phase 2 - Questions

[] Request 1: Is there a different way I should have communicated the desire for complete, production0-ready, work more clearly or in a way there's a higher probability it'll be followed without having to explicitly ask or correct for it? Please output your response in the chat panel.

[] Request 2: I was expecting to look at the template prompts and see everything ready to be ran and tested. It was unacceptable to see notes that you deferred creating the requested assets and notated next steps. I was fully expecting you to carry out my request and return a complete and functioning set of templates and components. Could you review everything and provide additional feedback on how I can take the `source_prompt` and refactor it to better express my desires in a way the model will clearly understand. My brain is a little special, so I think I may need your help translating my prompt into "ai." Please output your response within `[absolute_path]/feedback/` named `prompt-engineering-edu-feedback-1.md`

[] Request 3: So that I can better understand the refactored prompt, could you add another section to `[absolute_path]/feedback/prompt-engineering-edu-feedback-1.md` below "## END Footer" labeled "### Change Log" where you outline each change you've made and the reasoning and strategy behind the refactor. If you are stating any factual claims, please cite your sources.

[] Request 4: So that I can continue to learn and grow, please incorporate your responses to requests 1 and 2 and then include any additional feedback you can provide so that I can understand the current limitations to my current form of prompting and take it to another level. Take all of that feedback and then add another section to `[absolute_path]/feedback/prompt-engineering-edu-feedback-1.md` below "## END Footer" labeled "### Feedback" where you provide outline your overall feedback and then have "mini-sections" for each point on the outline. Within each mini-section, please provide your feedback, thoroughly explain your feedback, and provide resources to improve related to feedback. If you are stating any factual claims, please cite your sources. Please ensure your feedback is in the form of a thesis-quality research paper.

[] Request 5: Please confirm all steps have been completed and that all updates have successfully been saved to `[absolute_path]/feedback/prompt-engineering-edu-feedback-1.md`.


## Footer (Model Instructions: Do Not Output)

## END Header