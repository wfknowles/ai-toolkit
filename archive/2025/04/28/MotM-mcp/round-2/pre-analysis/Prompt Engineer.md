# Prompt Engineer Pre-Analysis (Round 2)

## Initial Thoughts on Assets, Strategies, and Workflows for MCP MVP

### Key Assets Needed
- Modular, composable prompt templates for each workflow step (analysis, synthesis, review, etc.)
- A state schema (JSON) for passing context and results between steps
- System prompt(s) defining agent persona, tool usage, and error handling

### Strategies
- Use prompt chaining with explicit state handoff between steps
- Design prompts to generate summaries and checkpoints for user review
- Modularize prompts for extensibility and future workflows

### Methodologies
- Iterative prompt development and testing
- User-in-the-loop for confirmation at key steps
- Error handling and recovery prompts for failed tool calls or context loss

### Workflows
- Stepwise chain: concept analysis → SME simulation → group synthesis → requirements/roadmap generation
- Each step writes to state, which is validated before proceeding
- User checkpoints after major steps

### Open Questions
- How to best modularize prompts for new workflows?
- What is the minimum viable set of prompt templates for the MVP?
- How to ensure state integrity across chained steps? 