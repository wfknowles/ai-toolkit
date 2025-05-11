# Prompt Output Evaluation Framework - README

This directory contains the automated tests for validating the prompts stored in the `../prompts/` and `../templates/` directories of this library. The framework uses [Jest](https://jestjs.io/) (or a similar testing framework like PyTest if prompts are primarily Python-focused) to execute these tests.

## Purpose

The primary purposes of this evaluation framework are to:
1.  **Verify Prompt Effectiveness:** Ensure that prompts generate outputs that meet defined quality criteria when run against target Large Language Models (LLMs).
2.  **Prevent Regressions:** Detect when changes to a prompt, its template, or the underlying LLM (if a specific version is targeted) cause a degradation in output quality for known use cases.
3.  **Automate Quality Assurance:** Integrate with the `GitHub Actions Workflow for Prompts CI/CD` (Component #6) to provide automated quality gates.
4.  **Document Expected Behavior:** The tests and their associated exemplar files serve as living documentation of how each prompt is expected to perform.

## Test Structure

Each prompt or prompt template should ideally have a corresponding test file in this directory, mirroring the structure of the `../prompts/` directory. For example, a prompt located at `../prompts/by_task/code_generation/python/function_from_spec.md` might have its tests in `tests/by_task/code_generation/python/function_from_spec.test.js`.

Each test file will typically contain one or more test suites/cases that:
1.  Load the target prompt or template.
2.  Prepare input data, often sourced from `../exemplars/`.
3.  (If a template) Populate the prompt template with exemplar input data.
4.  Execute the prompt against a configured LLM endpoint (this might be a real LLM for integration tests or a mock/stubbed LLM for unit tests of prompt construction logic).
5.  Evaluate the LLM's output against expected criteria, which might involve:
    *   Comparing against an 'expected output' file from `../exemplars/`.
    *   Running linters or validators on the output (e.g., checking if generated code is valid).
    *   Asserting the presence/absence of specific keywords or patterns.
    *   Checking structural correctness (e.g., for JSON, XML).

## Exemplar Files (`../exemplars/`)

Exemplar files store the input data and expected output characteristics for test cases.
*   **Input Exemplars:** (e.g., `_input.txt`, `_input.json`) Provide the specific input data to be used with a prompt template or as context for a static prompt.
*   **Output Exemplars:** (e.g., `_expected_output.py`, `_expected_output.json`, `_expected_output.md`) Provide the "golden" output or criteria against which the LLM's actual output will be compared. This might be an exact match, a superset, a structurally similar file, or a list of validation rules.

## Running Tests

Tests can be run locally using the command:
`npm test` (if Jest is used with Node.js)
or
`pytest` (if PyTest is used with Python)

They are also run automatically as part of the CI/CD pipeline for this repository.

## Contributing New Tests

When contributing a new prompt or modifying an existing one, corresponding tests and exemplar files **must** be added or updated. Refer to the [Prompt Contribution and Review Guidelines](link_to_component_13.md) and existing test files for examples.

**Key Test Dependencies (Illustrative for Jest):**
*   `jest`: The testing framework.
*   An LLM client library (e.g., `openai`, `@anthropic-ai/sdk`) or a custom module for interacting with the target LLM(s).
*   Helper functions for loading prompts and exemplar files.
*   Linters or validators used for output checking (e.g., ESLint, Pylint programmatically).