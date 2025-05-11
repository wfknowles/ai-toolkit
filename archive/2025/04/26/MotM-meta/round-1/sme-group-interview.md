# Meeting of the Minds: Meta-Workflow Design (Round 1)

**Date:** 2025-04-26
**Facilitator:** AI Assistant
**Attendees:** Prompt Engineer (PE), AI Orchestrator/Architect (Arch), Senior Software Engineer (SSE), Product Owner (PO), Project Manager (PM), AI UX Engineer (UXE), AI Agent Engineer (AE) (All Simulated)

**Facilitator:** Welcome everyone. We've all reviewed the initial concept of generalizing the MotM workflow and provided individual pre-analyses and interview feedback. The goal now is to synthesize our perspectives and agree on a concrete plan, particularly for an initial implementation.

**Facilitator:** There seems to be strong convergence on tackling an MVP first: replicating the *existing* MotM MVP workflow (requirements/roadmap generation for a specific concept) but using the new chained architecture to improve UX by removing interruptions. Generalization comes later. Any objections to this initial scope?

**(General agreement)**

**PO:** Makes sense. De-risk the core technical challenges first and deliver user value quickly via the smoother UX.
**PM:** Agree. This limits scope and allows us to focus on the high-risk technical feasibility aspects.

**Facilitator:** Great. Architecturally, the consensus points towards a **fixed chain sequence** orchestrated by a central **meta-prompt**, using a single **`state.json` file** for state management. SSE, Arch, any major concerns with that foundation for the MVP?

**Arch:** No, that's the most pragmatic approach given the constraints. Fixed chain minimizes complex logic in the orchestrator.
**SSE:** Agreed. JSON is the right choice for state, assuming the LLM can handle parsing/updating it reliably via prompts and the `edit_file` tool.

**Facilitator:** Okay, let's detail that interaction. Agent Engineer, Prompt Engineer, how should the Orchestrator and the Step Prompts (Agents) interact via the state file and prompt instructions?

**AE:** The Orchestrator reads `state.json`. It identifies the next step. It constructs the prompt for that step, injecting only the *necessary* data from the state (e.g., `state.concept`, `state.data.step_n_output`). The Step Prompt executes its task.
**PE:** Crucially, the Step Prompt must be instructed to return its results *and* a status (e.g., `success` or `error`) formatted within a specific JSON block in its response. Like:
```json
{
  "status": "success",
  "output_data": { ...results... }
}
```
**AE:** Exactly. The Orchestrator then parses this JSON block from the response. It validates – did it get JSON? Is status `success`? If yes, it updates the `state.json` file with the `output_data` and advances `current_step`. If no, it sets `state.status` to `error`, records the error, and halts.
**SSE:** This reliance on the LLM perfectly formatting JSON output is still a weak point, but it's the best we can do here. The Orchestrator's validation step is critical.

**Facilitator:** What specific fields should be in the `state.json` schema for the MVP?

**Arch:** Based on interviews: `workflow_id`, `schema_version`, `concept_input`, `current_step`, `status` (`running`, `completed`, `error`), `error_message`, and a `data` object keyed by step name to store outputs.

**Facilitator:** Moving to UX and artifacts. The "glass box" idea seemed popular: automated flow, status updates, optional checkpoints with summaries linking to hidden artifacts. UXE, PO, how does that sound?

**UXE:** Yes, that balances flow with transparency. Status updates should be lightweight ("*Status: Step X complete*"). Checkpoints after major phases – let's define those for the MVP workflow. Maybe after all initial SME analyses are simulated, and again after the simulated group discussion?
**PO:** I agree with those checkpoint locations. Summaries are key. Generate the full files (like the individual analyses or group discussion transcript) but link them optionally. The primary flow shouldn't require reading them.
**SSE:** From an engineering view, generating them is fine, maybe even useful for debugging. Hiding them by default is the right UX compromise.

**Facilitator:** Finally, let's acknowledge limitations. We're simulating agents, relying heavily on prompt adherence and tool reliability. Error recovery is minimal for MVP (halt and report). We're aiming for *better* UX, but robustness might still be lower than a dedicated application. Everyone aligned on managing expectations?

**PM:** Yes, clear communication about the limitations and the experimental nature of this prompt-driven workflow is key.
**AE:** It's a simulation constrained by the environment. We build the most robust version possible within those constraints.

**Facilitator:** Excellent. So, the plan is: Build an MVP chain replicating the existing MotM process using a fixed sequence, JSON state file, orchestrator prompt managing simple transitions and error checking, with UX featuring status updates and optional checkpoints linking to generated-but-hidden artifacts. Generalization is deferred.

**(General agreement and conclusion of meeting)** 