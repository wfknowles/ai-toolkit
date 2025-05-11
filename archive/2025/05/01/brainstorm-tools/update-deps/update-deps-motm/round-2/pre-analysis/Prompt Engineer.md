# Prompt Engineer - MotM Round 2 Pre-Analysis

**Date:** 2025-05-01
**Focus:** Assets, Strategies, Methodologies, Workflows for V1 CLI (Prompting Perspective)

Based on the refined V1 CLI concept from Round 1, here are the key elements needed from a Prompt Engineering perspective:

**1. Assets:**

*   **Modular Prompt Templates:** A set of version-controlled text templates for each distinct LLM interaction point identified in R1 (Analysis Summary, Conflict Explanation, Breaking Change Analysis, Test Failure Explanation, Optional CoT). These templates should include placeholders for dynamic context injection.
    *   `prompt_template_scan_summary.txt`
    *   `prompt_template_conflict_resolution.txt`
    *   `prompt_template_breaking_change.txt`
    *   `prompt_template_test_failure.txt`
    *   `prompt_template_cot_explanation.txt`
*   **Persona Definition File:** A configuration file (`persona_jr_dev_assistant.yaml`?) defining the target AI persona (helpful, cautious, clear, concise) to ensure consistency across modules.
*   **Expected Output Schemas (JSON):** Define the desired structured output format (e.g., JSON schema) for prompts where structured data extraction is needed (e.g., identifying specific breaking changes, risk scores). This helps reliable parsing by the orchestrator.
    *   `schema_breaking_change_output.json`
    *   `schema_risk_assessment_output.json`
*   **Example Interaction Corpus:** A collection of input/output examples for each prompt template to be used for testing, fine-tuning (if applicable later), and documentation.

**2. Strategies:**

*   **Context Injection Strategy:** Define precisely *what* context (prior state, user config, tool outputs, conversation history snippets) needs to be injected into each modular prompt template by the orchestrator.
*   **Instruction Following Strategy:** Utilize clear delimiters, role prompting (System/User/Assistant), few-shot examples (within the prompt), and explicit instructions (e.g., "Explain potential breaking changes based *only* on the provided changelog snippets and code references.") to maximize reliable instruction following.
*   **Output Parsing Strategy:** Primarily rely on the orchestrator parsing LLM outputs. For critical structured data, instruct the LLM to output JSON matching the predefined schemas. Include fallback logic for parsing failures (e.g., treat output as unstructured text, log error).
*   **Error Handling Prompt Strategy:** Design specific prompts or instructions for the LLM on how to respond when *its own analysis* is uncertain or hits limitations (e.g., "If the changelog is unclear, state that the breaking change risk cannot be determined accurately and recommend manual review.").

**3. Methodologies:**

*   **Prompt Template Versioning:** Use Git for version control of all prompt assets.
*   **Prompt Evaluation Methodology:** Establish a methodology for testing prompts against a benchmark dataset (using the Example Interaction Corpus). Metrics should include: clarity of output, accuracy of analysis (vs. human baseline), adherence to persona, successful parsing (for structured outputs).
*   **Cross-LLM Compatibility Testing:** Test core prompts against multiple potential backend LLMs (if applicable) to assess portability and performance differences.

**4. Workflows:**

*   **Prompt Execution Workflow (Orchestrator -> LLM):**
    1.  Orchestrator identifies current state/required AI task.
    2.  Orchestrator selects appropriate Prompt Template.
    3.  Orchestrator gathers required Context Data.
    4.  Orchestrator injects Context into Template.
    5.  Orchestrator sends final prompt to LLM API.
    6.  Orchestrator receives LLM response.
    7.  Orchestrator parses response (using Expected Output Schema if applicable).
    8.  Orchestrator uses parsed data or presents text to user.
*   **Conflict Explanation Workflow (User Interaction):**
    1.  Orchestrator detects conflict.
    2.  Orchestrator triggers `prompt_template_conflict_resolution` with conflict details.
    3.  AI explains conflict and potential resolution options.
    4.  Orchestrator presents options to user.
    5.  User selects option.
    6.  Orchestrator proceeds based on selection. 