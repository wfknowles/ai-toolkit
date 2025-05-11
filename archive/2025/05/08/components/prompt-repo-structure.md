# Centralized Prompt Library/Repository - Definition & Structure Guide

## 1. Overview and Purpose

This Git repository serves as the central, version-controlled library for all approved prompts, prompt templates, prompt chains, and associated exemplars used within Our Project's AI-assisted development ecosystem. Its purpose is to:
*   Promote reusability and consistency in prompt engineering.
*   Facilitate collaboration and knowledge sharing around effective prompt design.
*   Enable versioning and lifecycle management of prompts as critical assets.
*   Serve as the source of truth for the `Dockerized Prompt Backend Service`.
*   Support automated testing and CI/CD for prompts.

All contributions to this library must adhere to the [Our Project: Prompt Engineering Standards Document](link_to_component_1.md) and the [Prompt Contribution and Review Guidelines](link_to_component_13.md).

## 2. Repository Structure

The repository will follow a structured directory layout to ensure discoverability and organization:

*   `.github/`
    *   `workflows/`
        *   `prompts-ci.yml`      # GitHub Actions for Prompt CI/CD (Component #6)
*   `prompts/`
    *   `by_task/`                # Organized by general task type
        *   `code_generation/`
            *   `python/`
                *   `function_from_spec.md`
                *   `class_boilerplate.md`
            *   `javascript/`
                *   `component_template.md`
        *   `code_explanation/`
        *   `refactoring/`
        *   `testing/`
            *   `generate_unit_tests.md`
    *   `by_llm_model/`           # Optional: if prompts are highly model-specific
        *   `gpt-4/`
        *   `claude-3-opus/`
    *   `by_project_module/`      # For prompts very specific to internal project modules
        *   `auth_service/`
        *   `payment_gateway/`
    *   `common_elements/`        # Reusable prompt fragments or sub-prompts
        *   `security_considerations.md`
        *   `output_format_json.md`
*   `exemplars/`                  # Exemplar input/output pairs for testing (Component #4)
    *   `code_generation/`
        *   `python/`
            *   `function_from_spec_input.txt`
            *   `function_from_spec_expected_output.py`
    *   *(Additional exemplar structures mirroring prompts/)*
*   `templates/`                  # Parameterized prompt templates
    *   `general_code_gen_template.md`
    *   `data_analysis_template.md`
*   `tests/`                      # Jest/PyTest test files for prompts (Component #4)
    *   `test_code_generation_prompts.js`
    *   *(Additional test files)*
*   `.gitignore`
*   `.promptlintrc.js`            # Configuration for Prompt Linter (Component #3)
*   `README.md`                   # This file

**Key Directory Explanations:**

*   **`.github/workflows/`**: Contains GitHub Action definitions for CI/CD of prompts (linting, testing).
*   **`prompts/`**: The main directory for storing individual prompt files.
    *   **`by_task/`**: Primary organization. Prompts are categorized by the general task they perform. Sub-directories for specific languages or sub-tasks are encouraged.
    *   **`by_llm_model/`**: (Optional) Use if prompts are highly optimized for specific LLM versions.
    *   **`by_project_module/`**: For prompts tightly coupled with specific internal projects.
    *   **`common_elements/`**: Stores reusable snippets or sub-prompts.
*   **`exemplars/`**: Contains input examples and corresponding expected output criteria for testing prompts.
*   **`templates/`**: Stores parameterized prompt templates.
*   **`tests/`**: Contains the test scripts (e.g., Jest files) that use `exemplars/` to validate prompts.
*   **`.promptlintrc.js`**: Configuration file for the `Prompt Linter`.

## 3. Prompt File Format and Metadata

Each prompt file (typically a `.md` Markdown file) should adhere to a standard format using YAML frontmatter for metadata.

**(Example Prompt File Structure with YAML Frontmatter)**

```markdown
---
prompt_id: "python_function_from_spec_v1.2"
title: "Generate Python Function from Specification"
description: "Takes a natural language specification and generates a Python function."
version: "1.2.3"
author: "ai_prompt_code_architect_v1"
last_updated: "2023-10-26"
llm_compatibility: ["GPT-4", "Claude-3-Opus"]
tags: ["python", "code-generation", "functions", "backend"]
status: "production" # experimental, staging, production, deprecated
parameters:
  - name: "specification"
    type: "string"
    description: "Natural language description of the function."
    required: true
  - name: "function_name_suggestion"
    type: "string"
    description: "Optional suggested name for the function."
    required: false
test_cases: ["exemplars/code_generation/python/function_from_spec_*"]
known_limitations:
  - "May struggle with highly complex algorithmic specifications."
  - "Generated code requires security review for production use."
---

## Prompt Body

Act as an expert Python developer. Your task is to write a Python function based on the following specification.

**Specification:**
`{{ specification }}`

**Suggested Function Name (optional):**
`{{ function_name_suggestion }}`

**Requirements:**
- The function should be well-commented.
- Include type hints for all parameters and the return value.
- Adhere to PEP 8 styling guidelines.
- Implement robust error handling for invalid inputs.

**Output Format:**
Provide only the Python function code block. Do not include any explanatory text before or after the code block.
```

**Key Metadata Fields:**
(As previously defined: `prompt_id`, `title`, `description`, `version`, `author`, `last_updated`, `llm_compatibility`, `tags`, `status`, `parameters`, `test_cases`, `known_limitations`)

## 4. Branching Strategy

This repository will use the following branching strategy:
*   **`main`**: Production-ready prompts. Merges are restricted and require successful CI & approvals.
*   **`develop`**: Staging/integration branch for upcoming prompts.
*   **`feature/<feature-name>` or `prompt/<prompt-id>-dev`**: For new prompt development. PRs to `develop`.
*   **`experimental/<idea-name>`**: For early-stage, experimental prompts.

## 5. Contribution and Review Process

Refer to the [Prompt Contribution and Review Guidelines](link_to_component_13.md) for detailed instructions on how to contribute to this library.
