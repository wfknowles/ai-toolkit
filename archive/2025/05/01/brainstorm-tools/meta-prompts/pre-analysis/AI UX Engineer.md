# AI UX Engineer - Brainstorming Pre-Analysis: Meta-Prompts & Modularity

**Focus:** User Experience of Interacting With & Consuming AI Outputs

**Concepts Brainstormed (9):**

1.  **Progressive Disclosure Prompt Pattern:** Design prompts to initially provide a concise summary. Include a meta-instruction like: "Offer the user options to request more details, such as [explain reasoning, show code examples, list alternatives]." The orchestrator parses this to present follow-up actions.
2.  **Confidence Score Visualization Prompt:** Instruct the AI to output not just analysis, but also a confidence score (e.g., High/Medium/Low or 0-1). Prompt includes format requirement: "Output analysis and confidence score in JSON: `{'analysis': '...', 'confidence': 'Medium'}`." UX then visualizes this score appropriately.
3.  **Source Attribution Prompting:** Meta-instruction: "For every key statement or suggestion made, cite the primary source document or code file used from the provided context." Requires careful context labeling by orchestrator.
4.  **Customizable Output Format Prompt:** Allow users to specify output format preference (via config or flag). Meta-prompt: "User prefers output format [verbose_text/json_summary/bullet_points]. Generate the response accordingly."
5.  **Glossary Generation for Explanations:** For prompts explaining complex concepts (SSE concept #5), add meta-instruction: "If technical terms are used, provide a brief definition for each in a separate glossary section."
6.  **Interactive Refinement Prompt:** Instead of one-shot generation (e.g., commit message), use a prompt that suggests options: "Based on the diff, here are 3 possible commit messages. Which one is best, or would you like to refine one?" Allows user guidance.
7.  **Accessibility Check Prompt for Generated Content:** For AI generating user-facing text (docs, UI copy): "Review this generated text [text] for clarity, conciseness, and use of potentially ambiguous jargon. Ensure it meets WCAG AA readability guidelines."
8.  **User Persona Simulation for Testing UX:** Use the Persona-Driven Meta-Prompt (PE concept #4) *during development* to simulate how different user types might perceive or misunderstand AI outputs. Helps anticipate UX issues.
9.  **Feedback Tone Analysis Prompt:** Analyze user feedback (PO concept #8) not just for themes, but also for sentiment/tone: "Categorize the sentiment of this user feedback (Positive/Negative/Neutral) and identify emotionally charged language." 