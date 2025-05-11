---
persona: Prompt Engineer
date: 2025-04-26
analysis_type: initial_thoughts
concept: Automating the multi-round MotM process within Cursor IDE constraints
---

## Prompt Engineer - Initial Thoughts

**Core Challenge:** Replicating a multi-round, human-driven collaborative process using primarily prompt chaining and file I/O, without direct API access for complex state management or LLM calls within the automated flow. The key constraint is the "manual bridge" where the user copies/pastes prompts/outputs between the automation script and the LLM interface (e.g., Cursor chat).

**Initial Strategy Ideas:**

1.  **Master Orchestration Prompt:** Define a top-level prompt (like the `meeting-of-the-minds-round-1.md` we are currently processing) that outlines the entire N-round process. This prompt would instruct the LLM (acting as facilitator/SMEs) on which phase/step it's currently in.
2.  **State Management via Files:** Use the file system to store the state and outputs of each step/round.
    *   Each round's output (SME analyses, synthesized findings, generated requirements/roadmap drafts) gets saved to a dedicated file within the round's directory (`MotM/round-X/`).
    *   The Master Orchestration Prompt for the *next* round would need to instruct the LLM to *load* the relevant output files from the *previous* round to provide context.
3.  **Leveraging RAG for Internal Knowledge:** The existing RAG system (`answer_query_with_rag`) could be used *within* the automated process if we allow the script running the automation to call it (even if it can't call an external LLM). This could allow simulated SMEs to "look up" details from the project's `brain/knowledge` before formulating their responses.
    *   *Constraint Check:* This depends on whether the automation script itself *can* run the RAG agent's Python code, even if it can't make external API calls. The `rag_agent.py` currently relies on components loading at module level; this might need adjustment if called programmatically.
4.  **Explicit Step Handoffs:** Prompts must be very clear about:
    *   What input files/context to consider for the current step.
    *   What task to perform (analysis, synthesis, drafting).
    *   What specific output file(s) to generate.
    *   Signaling the *end* of the current step/round so the user knows when to run the next part of the automation (or the next round's master prompt).

**Potential Issues & Questions:**

*   **Context Window Limits:** Loading multiple prior outputs into subsequent round prompts could easily exceed context limits. Strategies needed:
    *   Summarization prompts between rounds.
    *   Instructing the LLM to focus only on *specific sections* of previous outputs.
*   **Prompt Complexity:** The Master Orchestration Prompt for each round will become increasingly complex as it needs to manage more state and context loading instructions.
*   **Maintaining Persona Consistency:** Ensuring the LLM maintains distinct, consistent personas across multiple rounds and manual copy/paste steps will be difficult. Explicit re-instruction might be needed in each prompt.
*   **Error Handling:** How does the process handle LLM failures, refusals, or malformed file outputs during a round? Manual intervention seems likely.
*   **User Experience (UX):** The manual copy/paste between the script's output (e.g., "Run Round 2 Prompt") and the LLM interface, then potentially copying the LLM's output back to a file, could be cumbersome. How can this be streamlined? Can the script at least *generate* the *next* master prompt file automatically?

**Diagram Idea:**

```mermaid
graph LR
    A[User Input: Concept] --> B(Automation Script: Round 1);
    B -- Generates --> C{Master Prompt 1 (File)};
    C -- User Copies --> D{LLM Interface};
    D -- LLM Generates --> E[Round 1 Outputs (Files)];
    E -- Automation Script Reads --> F(Automation Script: Round 2);
    F -- Generates --> G{Master Prompt 2 (File)};
    G -- User Copies --> D;
    D -- LLM Generates --> H[Round 2 Outputs (Files)];
    H --> I(...);
    I --> J[Final Assets: Reqs, Roadmap];
```

**Focus:** Design prompts that are robust to the manual copy/paste steps and clearly manage state via file inputs/outputs. Explore using the internal RAG for persona knowledge retrieval if feasible within constraints.
