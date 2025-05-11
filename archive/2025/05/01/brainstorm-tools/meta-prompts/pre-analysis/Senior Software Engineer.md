# Senior Software Engineer - Brainstorming Pre-Analysis: Meta-Prompts & Modularity

**Focus:** Practical Application & Developer Experience of Advanced Prompts

**Concepts Brainstormed (9):**

1.  **"Explain This Error" Contextual Prompt:** When a build or test fails, trigger a prompt automatically populated with the error log, relevant code snippets (from stack trace?), and recent git changes. Meta-instruction: "Explain the likely cause of this error in simple terms and suggest debugging steps."
2.  **Refactoring Suggestion Prompt with Live Code Context:** Allow devs to select a code block and trigger a prompt: "Suggest refactoring options for the selected code to improve [readability/performance/maintainability] based on [Project Coding Standards Doc]." Dynamically injects selection & standards.
3.  **Test Generation Prompt based on Code Changes:** After code changes, prompt: "Based on the recent diff [inject diff], generate [unit/integration] test cases covering the modified logic." Needs careful diff parsing and understanding of existing tests.
4.  **Documentation Update Prompt:** Triggered on commit or PR, prompt: "Review the code changes [inject diff] and the existing documentation [inject relevant doc sections]. Suggest updates or new sections needed for the documentation."
5.  **Onboarding Buddy Prompt:** A prompt accessible to new team members: "Explain how [feature X] works, referencing the relevant code in [module Y] and the design doc [link]. Use simplified language suitable for onboarding."
6.  **Code Review Automation (Specific Checks):** Prompts focused on specific, automatable code review tasks: "Check the following code [snippet] for adherence to [Security Checklist Item #3]. Explain any violations found." Easier than a full open-ended review.
7.  **Dynamic `TODO` / Tech Debt Generation:** Prompt analyzing code: "Identify potential areas of tech debt or sections needing future improvement in this code [snippet/file]. Generate `TODO` comments with brief explanations."
8.  **Cross-Cutting Concern Analysis Prompt:** "Analyze how [authentication/logging/error handling] is implemented across these files [list]. Identify any inconsistencies or areas for standardization."
9.  **Commit Message Generation Prompt:** Based on the staged changes (diff), prompt: "Generate a conventional commit message summarizing these changes." 