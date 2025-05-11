# Security Tool Configuration Baselines - Principles & Management v1.0

## 1. Purpose

This document outlines the principles and processes for defining, managing, and maintaining the configuration baselines for security scanning tools (SAST, SCA, Secrets Scanning, Linters with security rules) used within Our Project's CI/CD pipelines (as defined in GitHub Actions Workflows, Components #6 & #7).

The goal is to ensure these tools are configured effectively, consistently, and securely to provide maximum value in identifying risks while minimizing disruption to developers.

**Related Documents:**
*   [GitHub Actions Workflow for Prompts CI/CD](link_to_component_6.md)
*   [GitHub Actions Workflow for Codebase CI/CD](link_to_component_7.md)
*   [Secure Coding Standards & AI-Generated Code Checklist](link_to_component_8.md)

## 2. Core Principles

*   **Security First:** Configurations should prioritize the detection of significant security risks aligned with our standards (Component #8) and industry benchmarks (e.g., OWASP Top 10). Don't disable important checks without strong justification and documented risk acceptance.
*   **Optimize Signal-to-Noise:** Tune configurations to minimize false positives that waste developer time and erode trust in the tools. This involves understanding the project context, potentially tailoring rule sets, and using suppression mechanisms judiciously.
*   **Consistency:** Apply consistent baseline configurations across similar repositories or projects where applicable, while allowing for necessary project-specific adjustments.
*   **Configuration as Code:** All tool configurations (e.g., CodeQL config files, `.gitguardian.yml`, linter rule sets, workflow YAML snippets) MUST be stored in version control (typically within the repository they apply to or a central configuration repository).
*   **Secure Defaults:** Tool configurations should enforce secure defaults (e.g., failing builds on high-severity findings, not logging secrets).
*   **Transparency:** The rationale for key configuration choices (e.g., disabling a specific rule, setting severity thresholds) should be documented either in the configuration files themselves (via comments) or in this document.

## 3. Baseline Management Process

1.  **Initial Configuration:** The Application Security team (`ai_app_cloud_security_engineer_v1` persona) is responsible for defining the initial baseline configuration for each security tool, in consultation with development teams and the DevOps engineer (`ai_devops_automation_engineer_v1`).
2.  **Storage:** Baseline configurations are stored as version-controlled code (e.g., YAML, JSON, `.rc` files) within the relevant repository's `.github/` directory or a designated configuration path. Workflow files directly reference or utilize these configurations.
3.  **Review and Tuning:**
    *   On a regular basis (e.g., quarterly) or following significant tool updates or changes in the threat landscape, the Application Security team will review the effectiveness of the current baselines.
    *   Feedback from developers (via the `Developer Experience Specialist` - DTS) regarding excessive false positives or missed detections will be solicited and considered.
    *   Tuning involves adjusting rule severity, enabling/disabling specific checks, refining custom queries, or updating suppression lists.
4.  **Change Management:** Changes to baseline configurations must follow a standard code review process via Pull Requests. PRs modifying security tool configurations require approval from Application Security. The rationale for the change must be documented in the PR.
5.  **Documentation:** This document (`SECURITY_TOOL_BASELINES.md`) should be updated to reflect significant changes in principles, processes, or links to key configuration files. Specific tuning rationale may live closer to the configuration files themselves (e.g., in comments).

## 4. Specific Tool Considerations (Examples)

*   **SAST (e.g., CodeQL):**
    *   Start with standard security query suites (e.g., `security-and-quality`, `security-extended`).
    *   Develop custom queries for project-specific risks or to enforce custom secure coding standards.
    *   Use configuration files (`codeql-config.yml`) to precisely include/exclude paths and fine-tune analysis.
    *   Carefully manage suppression (`// codeql[js/some-rule]`) only for validated false positives or accepted risks, with clear justification comments.
*   **SCA (e.g., Dependency Review Action):**
    *   Define clear `allow-licenses` and `deny-licenses` lists based on company legal policy.
    *   Set an appropriate `fail-on-severity` level based on risk appetite (e.g., 'high' or 'critical').
    *   Establish a process for handling vulnerability exceptions (`allow-ghsas`) – these should be temporary and tracked.
*   **Secrets Scanning (e.g., GitGuardian Shield):**
    *   Use a robust set of detectors.
    *   Integrate with company-specific patterns if needed.
    *   Use `.gitguardian.yml` primarily to ignore specific *files* or *paths* that are known non-secrets (e.g., test data, examples), NOT to ignore specific secret patterns unless absolutely necessary and documented/approved. Avoid overly broad ignores.
    *   Ensure `exit_zero` is `false` in CI to enforce blocking.

## 5. Deployment

These configurations are deployed automatically whenever the corresponding GitHub Actions workflows (Component #6, #7) are executed, as the workflows read these version-controlled configuration files or parameters directly.
