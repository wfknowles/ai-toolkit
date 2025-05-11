---
persona: Senior Software Engineer
date: 2025-04-26
analysis_type: initial_thoughts
concept: Automating the multi-round MotM process within Cursor IDE constraints
---

## Senior Software Engineer - Initial Thoughts

**Core Task:** Implement the orchestration script (`motm_engine.py`) and supporting Python modules, focusing on code quality, robustness, and maintainability within the specified constraints.

**Implementation Details & Considerations:**

1.  **Orchestration Script (`motm_engine.py`):**
    *   **Language:** Python 3.
    *   **Libraries:** `argparse` (for CLI), `pathlib` (for path manipulation), `json`/`yaml` (for config/state), `logging`, `shutil` (potentially for file ops), `subprocess` (if calling RAG agent as separate process).
    *   **Structure:** Likely class-based (`MotmOrchestrator`?) to manage state (current round, concept, paths) or function-based with clear parameter passing.
    *   **CLI:** Needs arguments for `--concept-file` (or `--concept-text`), `--start-round`, `--end-round`, `--step` (to potentially resume), `--output-dir`. Example: `python -m motm_engine --concept-file concept.md --output-dir brain/knowledge/chronological/2025/04/26/MotM`.
2.  **Round/Step Definitions:** Loading round definitions from external files (YAML suggested by Architect) is good. Define a clear schema for these files.
3.  **State Management (Files):**
    *   Use `pathlib` for all path operations to handle OS differences.
    *   Implement robust checks for expected input files before proceeding with a step. Log clear errors if files are missing.
    *   Use consistent naming conventions (as proposed by Architect).
    *   Consider a simple `state.json` file within the main MotM output directory to track the last successfully completed round/step, aiding resumability.
4.  **Prompt Generation:**
    *   Create a dedicated `prompt_generator.py` module.
    *   Function `generate_llm_prompt(round_num, step_name, template_path, context_files: dict)`.
    *   This function reads the template file.
    *   It then iterates through `context_files` (mapping placeholder names to file paths), reads the content of each file.
    *   Injects the read content into the template using `string.Template.safe_substitute`.
    *   Returns the complete prompt string.
5.  **RAG Integration:**
    *   If the orchestrator needs to call the RAG agent (`agent_core/rag_agent.py`), importing its `answer_query_with_rag` function is cleaner than using `subprocess`, *if* the dependency/path issues are resolved (running the orchestrator with `python -m` should help).
    *   Need error handling around the RAG call.
6.  **User Handoff:**
    *   When the script needs manual LLM interaction, it should print:
        *   Clear instructions: "Please copy the following prompt and submit it to your LLM."
        *   The generated prompt itself (well-formatted).
        *   Clear instructions on where to save the LLM response: "Save the complete response from the LLM to: [specific_output_file_path]"
        *   The exact command to run next to continue the process: "Once saved, run: [next_command_to_run]"
    *   This makes the manual step as foolproof as possible.
7.  **Output Parsing (Post-LLM):**
    *   The script step *after* the manual LLM interaction needs to read the file the user saved.
    *   If the prompt asked the LLM to structure its output (e.g., specific sections, code blocks), this script step needs to parse that structure reliably. This can be brittle. Simpler might be to treat the LLM output as mostly monolithic text for subsequent steps.
    *   Consider adding marker lines (e.g., `# START REQUIREMENTS`, `# END REQUIREMENTS`) in the prompts to make parsing the LLM output file easier for the script.
8.  **Error Handling:** Wrap file I/O, RAG calls, and potentially template substitution in `try...except` blocks. Log errors clearly. Provide informative messages to the user if the script has to abort.
9.  **Testing:** Unit tests for prompt generation logic, file path manipulation, and state handling. Integration tests are harder due to the manual LLM step, but we could test the script's flow up to the point of generating the prompt and after reading a *mock* LLM output file.

**Potential Refinements:**

*   Could the script *watch* for the LLM output file to appear instead of requiring the user to run the next command manually? (Adds complexity - requires file system watching libraries).
*   Could the script offer to *open* the generated prompt file in the editor automatically?

**Focus:** Clean, modular Python code. Robust file handling and path management. Clear, explicit instructions for the user during the manual handoff phases. Make resuming a partially completed run possible (via state file or CLI args).
