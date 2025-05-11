project-prompt-library/
|
+-- .github/
|   +-- workflows/
|       +-- prompts-ci.yml         (Component #6)
|
+-- prompts/                       (Component #2 Core)
|   +-- by_task/
|   |   +-- code_generation/
|   |   |   +-- python/
|   |   |   +-- javascript/
|   |   +-- code_explanation/
|   |   +-- refactoring/
|   |   +-- testing/
|   +-- by_llm_model/ (Optional)
|   +-- by_project_module/ (Optional)
|   +-- common_elements/
|
+-- exemplars/                     (Component #4 Support)
|   +-- (Mirrors prompts/ structure where applicable)
|
+-- templates/                     (Component #2 Support)
|   +-- general_code_gen_template.md
|   +-- ...
|
+-- tests/                         (Component #4 Core)
|   +-- (Mirrors prompts/ structure where applicable)
|   +-- llm_service_mock.js (Example helper)
|   +-- prompt_loader.js (Example helper)
|
+-- .gitignore
+-- .promptlintrc.js               (Component #3 Config)
+-- README.md                      (Component #2 Guide)
+-- PROMPT_LINTER_RULES.md         (Component #3 Rules Doc)
+-- PROMPT_CONTRIBUTION_GUIDELINES.md (Component #13)