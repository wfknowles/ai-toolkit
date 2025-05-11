# Interview Transcript: Prompt Engineer

**Date:** 2025-05-02
**Persona:** Prompt Engineer (PE)
**Interviewer:** Facilitator

**Facilitator:** Thanks for sharing your lesson ideas, focusing heavily on practical techniques. Looking at the proposed curriculum, what challenges do you foresee in teaching concepts like CoT or RAG to engineers who might be new to structured prompting?

**PE:** The biggest hurdle is moving beyond "just asking the LLM." Engineers need to see the *value* in structured approaches. CoT seems magical until you show side-by-side comparisons of complex task failures without it vs. success with it. For RAG, the challenge is explaining *how* it overcomes context limits without getting bogged down in vector DB specifics – focus on the *prompt augmentation* aspect. Live demos in Cursor showing these techniques solving real SE problems are crucial.

**Facilitator:** Which modules do you think will be most cognitively demanding?

**PE:** Unit 3, definitely. Combining techniques like chaining prompts or integrating RAG requires understanding how outputs from one step feed into the next. Unit 4's advanced topics like Self-Consistency or Agentic patterns also require a mental shift. We need hands-on labs where they build these workflows piece by piece.

**Facilitator:** What were your own "Aha!" moments when learning this?

**PE:** Realizing that the LLM *doesn't know what it doesn't know*. That shifted my focus to providing *all* necessary context explicitly. Another was seeing how few-shot prompting dramatically improves performance on specific formats or tasks. And finally, understanding tokenization and how it impacts code generation or complex instructions.

**Facilitator:** What blindspots might engineers have?

**PE:** Over-reliance on default settings or simple Q&A prompts. Not iterating enough – prompt engineering *is* iterative. Also, not considering the 'negative space' – what the prompt *doesn't* say, which can implicitly guide the model incorrectly. Many might also underestimate the importance of clear formatting and delimiters.

**Facilitator:** How do your lesson ideas contribute? Strengths/Weaknesses?

**PE:** Strength is the focus on practical application and specific techniques engineers can use immediately in Cursor. Weakness might be slightly under-emphasizing the 'why' – need to link closely with AIR's theoretical points. The hands-on labs are key.

**Facilitator:** For the curriculum research phase, where are you best placed?

**PE:** Defining the core prompting techniques (Lesson 1.2.1, 2.1.1, 2.3.1), developing practical examples for CoT/RAG/Chaining (3.1.1, 3.2.1, 3.3.1), crafting the hands-on labs, contributing to the Cursor integration examples (2.4.1, etc.), and providing input on evaluation from a practitioner's perspective (3.4.1).

**Facilitator:** And for development?

**PE:** Writing the practical exercise instructions, creating demo prompts and expected outputs, refining the technical content for clarity and accuracy, ensuring the Cursor examples are realistic and effective.

**Facilitator:** Any other SMEs crucial for the roadmap phase?

**PE:** SSE is vital to ensure the examples and labs resonate with actual SE workflows. AI UX is needed to ensure the Cursor integration examples are smooth and intuitive.

**Facilitator:** Anything else important?

**PE:** Emphasize the *debugging* aspect. When a prompt fails, how do you systematically figure out why? We need to teach diagnostic techniques, like simplifying the prompt, checking tokenization, or tweaking parameters. This is a critical skill.

**Facilitator:** Excellent point. Thank you, PE. 