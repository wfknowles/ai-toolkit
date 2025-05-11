# Interview Transcript: AI UX Engineer

**Date:** 2025-05-02
**Persona:** AI UX Engineer (AI UX)
**Interviewer:** Facilitator

**Facilitator:** Thanks for bringing the user experience perspective, especially within Cursor. What challenges do you see in designing learning experiences around prompting directly within the IDE environment?

**AI UX:** The key challenge is balancing instruction with workflow. The learning shouldn't feel like a disruptive overlay on their coding environment. It needs to be contextual and integrated. How do we present examples, allow experimentation, and provide feedback directly within Cursor without cluttering the UI or breaking their flow? Another challenge is showcasing the *interaction* – prompt/response/refinement – which is core to effective use, but can be hard to demonstrate passively.

**Facilitator:** Which modules seem most demanding from a UX/cognitive load perspective, specifically within the Cursor tool?

**AI UX:** Anything involving complex context management or multi-turn interactions (Units 3 & 4). Showing engineers how to effectively manage context (`@`-files, symbol search, chat history) within Cursor is crucial but adds UI complexity. Visualizing prompt chains or agent loops (AOA's focus) within the IDE will be a significant UX challenge. Keeping the core prompting techniques (Unit 2) clear and discoverable within the Cursor interface is also vital.

**Facilitator:** What were your "Aha!" moments regarding the UX of AI developer tools?

**AI UX:** Realizing how critical clear feedback and explainability are. When the AI does something unexpected, the user needs *some* insight into why. Also, the power of context awareness – tools that seamlessly understand the code the user is working on feel magical. Finally, seeing how important iteration and refinement are – the UX must make it easy to tweak prompts and retry.

**Facilitator:** Potential blindspots for engineers regarding the UX aspects?

**AI UX:** Focusing only on the prompt text and ignoring the surrounding UI and interaction patterns. Not utilizing the tool's context features effectively. Frustration when the AI doesn't "get it" immediately, without considering how the UI might facilitate better prompting or feedback.

**Facilitator:** How do your lesson ideas address these UX challenges?

**AI UX:** Strength: Emphasizing the practicalities of using AI within Cursor (Lesson 2.4.1), including context management and iterative refinement. Ideas around visualizing complex workflows (collab with Ed UX) are key. Weakness: Designing these integrated learning experiences within Cursor requires technical feasibility checks and likely collaboration with the Cursor team itself or deep knowledge of its extension capabilities.

**Facilitator:** Where can you best contribute during curriculum research?

**AI UX:** Defining best practices for interacting with AI in Cursor (2.4.1), contributing user-centric perspectives on evaluating prompt effectiveness (3.4.1), designing the user flow for exercises and the capstone project within the IDE, researching optimal ways to present feedback and explanations.

**Facilitator:** And during development?

**AI UX:** Designing mockups or prototypes for any in-IDE learning elements, ensuring clarity and usability of instructions and examples, usability testing of the course materials/exercises within Cursor, collaborating with Ed UX on visualizations.

**Facilitator:** Other SMEs needed for roadmapping?

**AI UX:** Ed UX is a natural partner. SSE ensures the workflows we design match reality. PE ensures the underlying prompting concepts are sound.

**Facilitator:** Anything else crucial?

**AI UX:** Accessibility. We need to ensure the learning materials and any custom UI elements within Cursor are usable by engineers with diverse needs. Also, consider the UX of *debugging* prompts within the tool – how can the interface help users diagnose issues?

**Facilitator:** Great points. Thank you, AI UX. 