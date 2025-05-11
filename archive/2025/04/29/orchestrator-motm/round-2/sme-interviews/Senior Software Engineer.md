# Senior Software Engineer - Round 2 Interview (Orchestrator Framework)

**Facilitator:** Define the structure for the allow-list configuration file (e.g., YAML format).

**Senior Software Engineer:** (Placeholder providing YAML example: `read_allow: ["/abs/path/to/data", "relative/docs"]
edit_allow: ["/abs/path/to/data/editable"]`).

**Facilitator:** Outline the steps for the Execution Environment to generate a diff for the confirmation.

**Senior Software Engineer:** (Placeholder describing process: Receive edit proposal -> Securely read current file content using `read_file_tool` logic -> Use a diff library (e.g., `difflib` in Python) to compare current vs proposed -> Return diff as part of response to Orchestrator.)

... 