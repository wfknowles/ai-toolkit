# Prompt Engineer - Pre-Analysis: AI Dependency Update Assistant Concepts

**Objective:** Identify concepts for structuring the prompt and interaction to effectively guide the AI and the user through the dependency update process.

**Initial Concepts (9):**

1.  **Structured Input Fields:** Design the prompt to accept structured inputs: list of dependencies to update/check, specific versions to pin, dependencies to omit, target stability level (stable, latest, patch-only).
2.  **Contextual Code Analysis Trigger:** Prompt the AI to analyze relevant code sections that *use* a dependency before suggesting an update, especially for major version changes, to anticipate potential breaking changes.
3.  **Change Explanation Generation:** Instruct the AI to clearly explain *why* an update is recommended (e.g., security fix, performance improvement, new features) and summarize breaking changes based on changelogs or code analysis.
4.  **Interactive Conflict Resolution Prompt:** If conflicts arise, prompt the AI to present clear options to the user (e.g., "Keep version A of LibX (needed by LibY) or Update to version B (needed by LibZ)? Explain trade-offs.") rather than failing silently.
5.  **Safety/Confidence Score Prompting:** Instruct the AI to provide a confidence score or risk assessment for each proposed update based on factors like test coverage, known issues, age of release, and security scan results.
6.  **User Control Integration:** Ensure prompt structure allows users to easily override suggestions, pin specific versions (e.g., `--pin libX==1.2.3`), or exclude dependencies (`--omit libY`).
7.  **Dependency Manager Inference Prompt:** Instruct the AI to attempt inferring the package manager (npm, pip, bundler, cargo, etc.) and dependency file (`package.json`, `requirements.txt`, `Gemfile`) from the project structure, but prompt user for confirmation.
8.  **Command Generation Preview:** Before execution, prompt the AI to show the exact package manager commands it plans to run (e.g., `npm update libX`, `bundle update gemY`) for user review and approval.
9.  **Persona-Driven Explanation (Jr. Dev Focus):** Instruct the AI to adopt a helpful, explanatory persona, especially when detailing complex conflicts or breaking changes, tailoring the language for a junior developer audience. 