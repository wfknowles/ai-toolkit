# Our Project: Git Repository Structure & Branching Strategy - v1.0

## 1. Purpose

This document outlines the standard structure for organizing Our Project's source code, AI assets (prompts, tests, exemplars), infrastructure code, documentation, and related artifacts within Git repositories. It also defines the branching strategies and access control mechanisms to be used, aiming for clarity, consistency, security, and efficient integration with our CI/CD workflows.

Adherence to this strategy is crucial for maintaining code quality, facilitating collaboration, enabling effective automation, ensuring auditability, and managing access control effectively.

**Related Documents:**
*   [Centralized Prompt Library/Repository - Definition & Structure Guide](link_to_component_2.md)
*   [Prompt Contribution and Review Guidelines](link_to_component_13.md)
*   [GitHub Actions Workflow for Prompts CI/CD](link_to_component_6.md)
*   [GitHub Actions Workflow for Codebase CI/CD](link_to_component_7.md)

## 2. Repository Organization Strategy

We will adopt a **Multi-Repository Strategy** to maintain a clear separation of concerns between different types of assets with potentially different lifecycles, access control needs, and CI/CD requirements.

**Core Repositories:**

1.  **`project-main-app`** (or similar names for distinct application services):
    *   **Contents:** Source code for the primary application(s), including backend, frontend, unit/integration tests, application-specific documentation.
    *   **CI/CD:** Uses `GitHub Actions Workflow for Codebase CI/CD` (Component #7).
2.  **`project-prompt-library`**:
    *   **Contents:** The `Centralized Prompt Library` including prompts, templates, exemplars, prompt tests, linter configs. (As defined in Component #2).
    *   **CI/CD:** Uses `GitHub Actions Workflow for Prompts CI/CD` (Component #6).
3.  **`project-infrastructure`**:
    *   **Contents:** Infrastructure as Code (IaC) definitions (e.g., Terraform, Ansible, Helm charts) for deploying application services and potentially the prompt backend service.
    *   **CI/CD:** Dedicated IaC deployment workflows (potentially leveraging Component #7 principles for scanning).
4.  **`project-docs`**:
    *   **Contents:** Centralized project documentation, including user guides, onboarding materials (like Component #12), architectural diagrams, standards documents (Components #1, #8, #10, #13, #14, #15, #16). Could use a Docs-as-Code approach (e.g., MkDocs, Docusaurus).
    *   **CI/CD:** Workflow to build and deploy the documentation site.
5.  **`project-prompt-backend-service`**:
    *   **Contents:** Source code, `Dockerfile`, `docker-compose.yml` for the `Dockerized Prompt Backend Service` (Component #5).
    *   **CI/CD:** Workflow similar to Component #7, focused on building, testing, and potentially publishing the Docker image for this service.
6.  **`project-ide-plugin`**:
    *   **Contents:** Source code for the `IDE Integration Plugin` (Component #11).
    *   **CI/CD:** Workflow for building, testing, and packaging the plugin (`.vsix` file).

*(Adjust repository names and number based on actual project architecture.)*

## 3. Branching Model: GitFlow Variant (Common Standard)

Unless a specific repository requires a different model (which must be documented in its `README.md`), all core repositories will adhere to a variant of the GitFlow branching model:

*   **`main` Branch:**
    *   Represents production-ready code/assets. Only stable, tagged releases exist here.
    *   **Protected:** Direct pushes are **forbidden**. Merges only occur from `release` branches (or `hotfix` branches) via PRs with strict approvals. Commits should correspond to release versions.
*   **`develop` Branch:**
    *   Represents the main integration branch for ongoing development, reflecting the latest delivered development changes for the next release.
    *   **Protected:** Direct pushes are generally discouraged (allowed for core maintainers with caution, perhaps). Merges primarily occur from `feature` branches via PRs. CI checks (linting, testing, security scans) MUST pass for PRs targeting `develop`.
*   **`feature/<descriptive-name>` Branches:**
    *   Created from `develop` for developing new features or making significant changes (e.g., `feature/add-user-auth`, `feature/prompt-summarization-v2`).
    *   Developers work here. Multiple commits are expected.
    *   Pull Requests are created from `feature/*` branches back to `develop`.
    *   CI checks run on these PRs.
    *   Should be relatively short-lived and deleted after merging.
*   **`release/<version-number>` Branches (Optional but Recommended):**
    *   Branched from `develop` when preparing for a production release (e.g., `release/v1.2.0`).
    *   Used for final testing, bug fixing (only release-critical fixes), and documentation updates specific to the release.
    *   Once stable, merged into `main` (and tagged) and also back into `develop` (to incorporate any release-specific fixes).
    *   Protected similar to `main`.
*   **`hotfix/<issue-or-version>` Branches:**
    *   Branched directly from `main` to address critical bugs in production.
    *   Minimal changes allowed.
    *   Once fixed and tested, merged directly into `main` (and tagged) and also back into `develop` to ensure the fix is included in ongoing development.
    *   Protected similar to `main`.
*   **Repository-Specific Branches (e.g., for Prompt Library):**
    *   The `project-prompt-library` may have additional conventions like `experimental/*` branches as outlined in its specific structure guide (Component #2).

**Branch Naming Conventions:** Use lowercase, kebab-case (`feature/add-new-widget`), and reference issue tracker IDs where applicable (`feature/PROJ-123-user-profile`).

## 4. Access Control Strategy (GitHub)

Access control will be managed using a combination of GitHub Team permissions, Branch Protection Rules, and `CODEOWNERS` files.

*   **Teams:** Define GitHub teams corresponding to roles (e.g., `developers`, `security-team`, `devops-eng`, `prompt-architects`, `release-managers`). Assign repository access levels (Read, Triage, Write, Maintain, Admin) to teams appropriately.
*   **Branch Protection Rules:**
    *   **`main` & `release/*`:** Require PRs, require passing status checks (CI, Security Scans), require review approvals from designated teams/CODEOWNERS (e.g., `release-managers`, `security-team`), restrict who can push, prevent force pushes.
    *   **`develop`:** Require PRs (strongly recommended, might allow direct push for maintainers in specific cases), require passing status checks. Require at least one approving review.
    *   **`feature/*` & `hotfix/*`:** Generally do not require strict protections beyond standard repository permissions, but PRs targeting `develop` or `main` *from* these branches trigger the protections on the target branch.
*   **`CODEOWNERS` Files:**
    *   Use `CODEOWNERS` files (in `.github/` directory) to automatically request reviews from specific teams or individuals when changes occur in particular files or directories.
    *   *Example:* Changes in `prompts/` directory automatically requests review from `@organization/prompt-architects`. Changes in `.github/workflows/` requests review from `@organization/devops-eng`. Security-sensitive files request review from `@organization/security-team`.
    *   Branch protection rules can be configured to require approval from CODEOWNERS.

## 5. Integration with CI/CD Workflows

*   The GitHub Actions workflows (Component #6, #7, and others) are configured to trigger based on events related to this branching strategy (e.g., pushes to `develop`, PRs targeting `main` or `develop`).
*   The pass/fail status of these workflows directly acts as a gate for merging PRs into protected branches, enforcing quality and security standards before integration.

## 6. Developer Guidance

*   **Always Branch from `develop`:** Start new feature work by creating a branch from the latest `develop`.
*   **Keep Branches Short-Lived:** Aim to integrate feature branches back into `develop` frequently via PRs to minimize merge conflicts and ensure continuous integration.
*   **Pull Frequently:** Regularly pull changes from the remote `develop` branch into your feature branch (`git pull origin develop`) to stay up-to-date.
*   **Descriptive PRs:** Use the project's PR template and write clear descriptions explaining the 'what' and 'why' of your changes.
*   **Address CI Failures:** If CI checks fail on your PR, investigate the logs and fix the issues promptly. Merging will be blocked until checks pass.
*   **Respect CODEOWNERS:** Ensure requested reviews from CODEOWNERS are obtained.

## 7. Review and Updates

This strategy document will be reviewed annually or when significant changes occur in project structure, team organization, or tooling. Updates require consultation between DevOps, Security, and Development leadership.
