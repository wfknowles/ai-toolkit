# Prompt Linter Rules Definition - v1.0

This document outlines the rules enforced by our project's Prompt Linter. Each rule is designed to support adherence to the [Our Project: Prompt Engineering Standards Document](link_to_component_1.md).

## Rule Categories and Specific Rules

The linter rules are configured in `.promptlintrc.js` (or equivalent). Below is a descriptive list:

### 1. Intent, Task, and Output Definition (Ref: Standard #1)
*   **`require-llm-persona` (Error):** Ensures every prompt explicitly defines a persona for the LLM to adopt (e.g., "Act as a...").
    *   *Rationale:* Improves output relevance and quality.
*   **`require-task-definition` (Error):** Ensures every prompt contains a clear and specific definition of the task the LLM should perform.
    *   *Rationale:* Reduces ambiguity and LLM "hallucinations."
*   **`require-output-format` (Warning):** Recommends that prompts specify the desired structure or format of the LLM's output.
    *   *Rationale:* Increases predictability and usability of LLM responses.
*   **`no-vague-phrases` (Warning):** Flags common vague phrases (e.g., "do something," "make it better") and suggests more specific language.
    *   *Rationale:* Enhances clarity and actionable instructions for the LLM.

### 2. Context Provision and Security (Ref: Standard #2, #6)
*   **`check-context-placeholder-format` (Error):** Enforces a consistent format (e.g., `{{variable_name}}`) for placeholders where dynamic context will be injected.
    *   *Rationale:* Supports automated templating and reduces errors.
*   **`detect-pii-in-prompt-context` (Error):** Scans prompt text (excluding designated user input sections if possible) for patterns resembling Personally Identifiable Information (e.g., email addresses, phone numbers, SSNs). Uses a configurable list of patterns.
    *   *Rationale:* Prevents accidental leakage of PII to LLMs, especially third-party services.
*   **`detect-secrets-in-prompt-context` (Error):** Scans prompt text for patterns resembling common secrets formats (e.g., API keys, password assignments). Uses a configurable list of patterns.
    *   *Rationale:* Prevents accidental leakage of credentials.

### 3. Parameterization and Templating (Ref: Standard #4)
*   **`enforce-parameter-documentation` (Error):** For prompts identified as templates (e.g., by filename convention or metadata), ensures that all expected parameters are documented in the prompt's metadata section.
    *   *Rationale:* Improves usability and maintainability of templated prompts.

### 4. Security - Prompt Injection Defense (Ref: Standard #5)
*   **`require-input-demarcation` (Warning):** When a prompt structure indicates it will combine predefined instructions with dynamic user input, this rule checks if the user input section is clearly demarcated (e.g., using specific tags like `<user_input>...</user_input>`) and if there are instructions to the LLM to treat demarcated input as data only.
    *   *Rationale:* Basic mitigation against prompt injection attacks.

### 5. Metadata and Documentation (Ref: Standard #7, #8)
*   **`require-prompt-metadata` (Error):** Verifies that all prompt files contain a valid metadata block (e.g., YAML frontmatter) with a minimum set of required fields (`prompt_id`, `title`, `version`, `status`, `author`).
    *   *Rationale:* Ensures all prompts are properly cataloged, versioned, and discoverable.
*   **`encourage-few-shot-example-section` (Info):** Suggests adding a dedicated section for few-shot examples in prompts designed for complex tasks where such examples significantly improve performance.
    *   *Rationale:* Promotes a powerful prompt engineering technique.

### 6. Ethical and Bias Considerations (Ref: Standard #9)
*   **`detect-harmful-content-generation-requests` (Error):** Scans the instructional part of the prompt for patterns or keywords that request the generation of known harmful, unethical, or policy-violating content. Uses a configurable pattern list.
    *   *Rationale:* Proactive defense against misuse of LLMs.
*   **`encourage-bias-mitigation-statements` (Info):** For prompts where output diversity or fairness is a concern (e.g., generating user personas, sample narratives), suggests including explicit instructions to the LLM to avoid stereotypes and consider diversity.
    *   *Rationale:* Promotes responsible and fair AI outputs.

### 7. General Style and Quality
*   **`no-excessive-capitalization` (Warning):** Flags excessive use of ALL CAPS in prompts, which can be hard to read.
*   **`check-grammar-spelling` (Info):** (Placeholder for potential future integration) Suggests integrating a grammar and spell checker for the natural language parts of the prompt.
    *   *Rationale:* Improves clarity and professionalism of prompts.

## Configuration

The linter rules, their severity (error, warning, info), and any specific parameters (like pattern files or length limits) are configured in the project's `.promptlintrc.js` file (or equivalent).

## Contribution

Additions or modifications to these rules should be proposed via a Pull Request and reviewed by the AI Prompt Engineering Committee.