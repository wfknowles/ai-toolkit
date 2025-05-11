# Meeting of the Minds: Meta-Workflow MVP Definition (Round 2)

**Date:** 2025-04-26
**Facilitator:** AI Assistant
**Attendees:** Prompt Engineer (PE), AI Orchestrator/Architect (Arch), Senior Software Engineer (SSE), Principal Architect (PA), Product Owner (PO), Project Manager (PM), AI UX Engineer (UXE), AI Agent Engineer (AE) (All Simulated)

**Facilitator:** Welcome to Round 2. We have detailed pre-analyses focusing on the assets and methodologies for building the MVP defined in Round 1. The goal today is to finalize these definitions so implementation can begin.

**Facilitator:** Topic 1: `state.json` and Auxiliary Files. We converged on JSON state, but need to finalize the schema and handling of large outputs.

**Arch:** I propose the schema includes: `workflow_id` (string, unique per run), `schema_version` (string, e.g., "1.0"), `concept_input` (string), `current_step` (string, name of last completed step), `status` (enum: "running", "completed", "error"), `error_message` (string, null if no error), `data` (object, holds step outputs keyed by step name).
**SSE:** Agree. For large outputs (transcripts, etc.), store them in auxiliary files (`.md`) and put the *path* to the file within the corresponding step's output in `state.json`. E.g., `state.data.step_analysis_pe.output_path = "./run123-step_analysis_pe-output.md"`.
**Arch:** We need a naming convention. How about `[workflow_id]-[step_name]-[output_type].md`?
**AE:** That works. The Orchestrator needs to generate the `workflow_id` initially and pass it to steps. Steps construct filenames using this ID and their own name.
**Facilitator:** Any objections to this schema and auxiliary file strategy (paths in JSON, convention `[id]-[step]-[type].md`)?
**(General agreement)**

**Facilitator:** Topic 2: MVP Workflow Sequence. We need to explicitly define the linear sequence derived from the original MotM prompts.
**PA:** I volunteer to document this based on the R1/R2 discussions and the original prompts. I'll create an `MVP_WORKFLOW.md` with a list or diagram showing Step 1 -> Step 2 -> ... -> Step N, clearly naming each step.
**PM:** Excellent. This will be the blueprint for WBS 2.2 (implementing step prompts).
**Facilitator:** Agreed. PA will draft `MVP_WORKFLOW.md`.

**Facilitator:** Topic 3: Step I/O Contract and Orchestrator Logic. We agreed Step Prompts output a JSON block (`status`, `output_data`) and the Orchestrator parses/validates it.
**PE:** Yes, the Step Prompt Template (AE's asset) needs to enforce this. Output needs to be *only* the JSON block if possible, or clearly fenced.
**AE:** The Orchestrator prompt logic needs the explicit parsing steps I outlined: find JSON block -> parse -> check `status` key -> extract `output_data` on success -> handle errors gracefully.
**SSE:** And the Orchestrator prompt, after updating its internal state representation, generates the *full* new JSON to overwrite `state.json` via `edit_file`.
**Facilitator:** Consensus on this Orchestrator <-> Step interaction model and state update strategy?
**(General agreement)**
**Arch/AE:** We will draft the detailed `INTERFACE_CONTRACT.md` and `state.schema.json` based on this.

**Facilitator:** Topic 4: Checkpoint Interaction.
**UXE:** Proposal was: Show summary + link, explicitly wait for user to type 'continue' before proceeding. View-only for MVP.
**PO:** Acceptable for MVP. Addresses the control concern without adding feedback complexity yet.
**Facilitator:** Okay, we'll proceed with the explicit 'continue' prompt for checkpoints in the MVP.

**Facilitator:** Topic 5: Documentation Ownership.
**PM:** Let's confirm: PA owns `TECHNICAL_DESIGN.md` and `MVP_WORKFLOW.md`. Arch/AE own `INTERFACE_CONTRACT.md` and `state.schema.json`. PO owns `MVP_ACCEPTANCE.md`. PE owns `step-prompt-template.md`. Does that work?
**(General agreement)**

**Facilitator:** Excellent. We now have concrete definitions for the core assets and methodologies. These form the requirements for the MVP build. The next step (Phase 7/Make A List) will be to compile these into a formal requirements list.

**(Conclusion of meeting)** 