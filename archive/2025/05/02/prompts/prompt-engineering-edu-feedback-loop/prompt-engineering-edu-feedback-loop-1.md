# Feedback Request Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-feedback-loop/prompt-engineering-edu-feedback-loop-1.md`
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
**output_root:**`brain/knowledge/chronological/2025/05/02`
**output_dir:**`edu/prompt-engineering`
**output_subdir:**`feedback`
**absolute_path:**`[output_root]/[output_dir]/[output_subdir]`

**source_prompt:**`[user_dependent_dir]/[output_root]/prompts/prompt-engineering-edu-2-2.md`

**background:** You asked, "Is there anything else you'd like me to review or correct regarding the execution of Phases 1 and 2, or shall we proceed?" Thank you for being so willing to iterate and improve. What I'm ultimately looking for is feedback. I'm always learning! And the reason we only ran phases 1 and 2 was because that was our maiden voyage. We'll probably be conducting this or more tests, iterate, and then synthesize feedback to refine my prompt.

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

[] Request 1: Is there a different way I should have communicated the context management instructions more clearly or in a way there's a higher probability they'll be followed without having to explicitly ask or correct for it? Please output your response in the chat panel.

[] Request 2: No need to sweat it, but I didn't see you replace the example Prompt Execution Plan with your determined plan within the secure header of the `source_prompt`. I "saw you cognate  it" in the chat output, but it was within something called "mental sandbox simulation". Could you help me understand the mental sandbox and it's simulation capabilities? I'd like to know what I should research to be able to maximize it's simulation abilities.  Please output your response in the chat panel.

[] Request 3: I was expecting to look at my original prompt and see all steps and meta-steps "checked" related to phases 1 and  2. Could you review all of this and provide additional feedback on how I can take the `source_prompt` and refactor it to better express my desires in a way the model will clearly understand. My brain is a little special, so I think I may need your help translating my prompt into "ai." Please output your response within `[absolute_path]/feedback/` named `prompt-engineering-edu-feedback.md`

[] Request 4: So that I can better understand the refactored prompt, could you add another section to `[absolute_path]/feedback/prompt-engineering-edu-feedback.md` below "## END Footer" labeled "### Change Log" where you outline each change you've made and the reasoning and strategy behind the refactor. If you are stating any factual claims, please cite your sources.

[] Request 5: So that I can continue to learn and grow, please incorporate your responses to requests 1 and 2 and then include any additional feedback you can provide so that I can understand the current limitations to my current form of prompting and take to another level. Take all of that feedback cand then add another section to `[absolute_path]/feedback/prompt-engineering-edu-feedback.md` below "## END Footer" labeled "### Feedback" where you provide outline your overall feedback and then have "mini-sections" for each point on the outline. Within each mini-section, please provide your feedback, thoroughly explain your feedback, and provide resources to improve related to feedback. If you are stating any factual claims, please cite your sources. Please ensure your feedback is in the form of a thesis-quality research paper.

[] Request 6: Please confirm all steps have been completed and that all updates have successfully been saved to `[absolute_path]/feedback/prompt-engineering-edu-feedback.md`.


## Footer (Model Instructions: Do Not Output)

## END Header