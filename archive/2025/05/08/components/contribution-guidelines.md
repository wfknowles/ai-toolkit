# Prompt Contribution and Review Guidelines - v1.0

## 1. Purpose

These guidelines outline the process for contributing new prompts, prompt templates, or improvements to existing ones to the `Centralized Prompt Library/Repository`. Following this process ensures that all prompts in the library are high-quality, tested, secure, documented, and adhere to our project's standards.

**Related Documents:**
*   [Centralized Prompt Library/Repository - Definition & Structure Guide](link_to_component_2.md)
*   [Our Project: Prompt Engineering Standards Document](link_to_component_1.md)
*   [Prompt Output Evaluation Framework - README](link_to_component_4_readme.md)

## 2. Contribution Workflow

1.  **Create an Issue (Optional but Recommended):** Before starting significant work on a new prompt or major revision, consider creating an issue in the Prompt Library repository to discuss the idea, need, and approach.
2.  **Ensure Up-to-Date `develop` Branch:** Pull the latest changes for the `develop` branch of the Prompt Library repository to your local machine.
3.  **Create a Feature Branch:** Create a new branch off `develop` for your work. Use a descriptive naming convention:
    *   For new prompts: `feature/prompt-<task-name>` (e.g., `feature/prompt-python-docstring-generator`)
    *   For improvements: `feature/improve-<prompt-id>` (e.g., `feature/improve-python_function_from_spec_v1.2`)
4.  **Develop the Prompt/Template:**
    *   Create or modify the prompt file(s) in the appropriate directory (see Component #2 for structure).
    *   Ensure the prompt adheres strictly to the `Prompt Engineering Standards` (Component #1).
    *   Include complete and accurate metadata (YAML frontmatter) as defined in Component #2.
5.  **Develop Tests and Exemplars:**
    *   Create corresponding test cases in the `tests/` directory using our `Prompt Output Evaluation Framework` (Component #4).
    *   Create necessary input and expected output exemplar files in the `exemplars/` directory.
    *   Ensure your tests cover the primary functionality and key edge cases of the prompt.
6.  **Run Linter and Tests Locally:**
    *   Run the `Prompt Linter` (Component #3) against your changed files (`npm run lint:prompts` or equivalent). Fix any errors.
    *   Run the automated tests (`npm test` or equivalent). Ensure all tests associated with your changes pass.
7.  **Commit Changes:** Use clear and descriptive commit messages. Reference the issue number if applicable.
8.  **Push Branch and Create Pull Request (PR):**
    *   Push your feature branch to the remote repository.
    *   Create a Pull Request targeting the `develop` branch.
    *   Use the provided PR template (see Section 3). Fill in all required details.

## 3. Pull Request (PR) Template Requirements

Your PR description MUST include:

*   **Link to Issue (if applicable):**
*   **Purpose:** Briefly explain the goal of the new prompt or the reason for the modification.
*   **Prompt(s) Affected:** List the path(s) to the prompt file(s) added or changed.
*   **Key Features/Changes:** Detail the functionality or improvements introduced.
*   **Metadata Checklist:** Confirm all required metadata fields are present and accurate.
*   **Testing:**
    *   Confirm that new/updated tests have been added in the `tests/` directory.
    *   Confirm that all local tests (linting and evaluation) pass. (CI will verify this).
*   **Rationale/Design Choices:** Briefly explain any significant design decisions made for the prompt structure or testing approach.
*   **Known Limitations/Risks:** Note any known limitations or potential risks associated with the prompt.

## 4. Review Process

1.  **Automated Checks (CI):** The `GitHub Actions Workflow for Prompts CI/CD` (Component #6) will automatically run on the PR. This includes linting and automated tests. These checks MUST pass before a manual review can proceed.
2.  **Assign Reviewers:** The PR author should request reviews from:
    *   At least one **Peer Reviewer** (another developer familiar with prompt engineering).
    *   The designated **Prompt Architect Lead** (`ai_prompt_code_architect_v1` or delegate).
    *   *(Optional)* A **Security Reviewer** (`ai_app_cloud_security_engineer_v1`) if the prompt deals with sensitive data generation, security tasks, or processes untrusted input in a novel way.
3.  **Reviewer Responsibilities:**
    *   **Peer Reviewer:** Focuses on clarity, usability, adherence to standards, documentation quality, and the effectiveness of the prompt based on its description and test cases.
    *   **Prompt Architect Lead:** Focuses on architectural consistency, advanced prompt techniques, alignment with overall ecosystem goals, test coverage adequacy, and adherence to core standards.
    *   **Security Reviewer:** Focuses on potential security implications, data handling, ethical considerations, and avoidance of harmful outputs (Standards #5, #6, #9).
4.  **Review Feedback and Iteration:** Reviewers will provide feedback via PR comments. The PR author is responsible for addressing comments, making necessary changes (on their feature branch), and pushing updates.
5.  **Approval:** The PR requires at least one approval from the Peer Reviewer category AND approval from the Prompt Architect Lead (and Security Reviewer, if assigned) before it can be merged.

## 5. Merging

*   Once all checks have passed and required approvals are received, a repository maintainer (typically the Prompt Architect Lead or a designated team member) will merge the PR into the `develop` branch.
*   The preferred merge strategy is generally **Squash and Merge** to keep the commit history on `develop` clean, unless multiple distinct commits within the PR provide significant value. Ensure the squashed commit message is informative.

## 6. Release to `main`

Prompts merged into `develop` will be included in the next "release" to the `main` branch. This process is typically managed by the Prompt Architect Lead or DevOps team, potentially involving further integration testing or a scheduled release cadence. Only code from `main` (or designated release tags) should be considered "production-ready" for consumption by the `Dockerized Prompt Backend Service` in production environments (if applicable) or general use.
