# Ultimate Cursor Prompts for Frictionless Multi-Phase Automation

## 1. Full Project Execution Prompt

> Please execute the entire [PROJECT/PROMPT NAME] as described in [PROMPT FILE PATH], including every phase, sub-step, and required output, without pausing, asking for input, or waiting for approval at any stage. 
> 
> **Checklist of required outputs:**
> - All pre-analysis documents for each SME persona
> - All individual SME interviews for each persona
> - Group synthesis/group interview transcript
> - Master requirements/roadmap file
> - Thesis-quality analysis/research paper
> - Any supporting diagrams, code examples, or logs
> 
> **Instructions:**
> - Do not stop or wait for my approval at any point. 
> - Loop through all personas, phases, and outputs as needed.
> - For each output, check if the file exists; if not, create it.
> - If an error or missing file is encountered, retry or handle autonomously.
> - Only stop when you have verified that every output in the checklist is present and complete.
> - At the end, generate a summary log of all actions taken and outputs created.
> - Do not ask me to review, adjust, or confirm anything unless I explicitly request it.

---

## 2. Recovery/Resume Prompt

> Please continue the [PROJECT/PROMPT NAME] process from where you left off, using [PROMPT FILE PATH] as the source of truth. 
> 
> **Instructions:**
> - Review the checklist of required outputs (see below) and compare against the current workspace.
> - For any missing or incomplete outputs, create or complete them as specified in the prompt.
> - If you encounter an error or missing file, handle it autonomously and retry as needed.
> - Do not pause, ask for input, or wait for approval unless explicitly instructed.
> - At the end, generate a summary log of all actions taken and outputs created or recovered.
> 
> **Checklist:**
> - All pre-analysis documents for each SME persona
> - All individual SME interviews for each persona
> - Group synthesis/group interview transcript
> - Master requirements/roadmap file
> - Thesis-quality analysis/research paper
> - Any supporting diagrams, code examples, or logs

---

## 3. Verification/Checklist Prompt

> Please verify that all required outputs for [PROJECT/PROMPT NAME] as described in [PROMPT FILE PATH] are present and complete in the workspace. 
> 
> **Instructions:**
> - Use the following checklist to verify each output:
>   - All pre-analysis documents for each SME persona
>   - All individual SME interviews for each persona
>   - Group synthesis/group interview transcript
>   - Master requirements/roadmap file
>   - Thesis-quality analysis/research paper
>   - Any supporting diagrams, code examples, or logs
> - For any missing or incomplete outputs, create or complete them as specified in the prompt.
> - At the end, generate a summary report listing all outputs and their status (present, missing, or incomplete).
> - Do not pause, ask for input, or wait for approval unless explicitly instructed. 