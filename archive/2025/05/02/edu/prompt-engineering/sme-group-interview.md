# SME Group Interview: Prompt Mastery Course Outline & Curriculum

**Date:** 2025-05-02
**Attendees:** Facilitator, Prompt Engineer (PE), AI Orchestrator/Architect (AOA), Senior Software Engineer (SSE), Product Owner (PO), Project Manager (PM), AI UX Engineer (AI UX), AI Agent Engineer (AAE), Pedagogy Researcher (PR), Educational UX Engineer (Ed UX), Professor of Education (Prof Ed), AI Researcher (AIR)

**Goal:** Refine and finalize the high-level outline and module structure for the Prompt Mastery educational course based on previous brainstorming, pre-analysis, and individual interviews.

---

**Facilitator:** Welcome back, everyone. We've done extensive individual prep work reviewing the initial course concept, previous discussions, and formulating outline ideas. The individual interviews revealed strong convergence on a roughly 5-part structure: Foundations, Core Craft, Building Complexity, Advanced Workflows, and Application/Capstone. Let's use that as our starting point and refine it. Any initial thoughts on these major groupings?

**Prof Ed:** I strongly support aligning these parts with cognitive progression, perhaps using Bloom's Taxonomy as a guide: Understanding/Remembering (Foundations), Applying (Core Craft), Analyzing/Evaluating (Complexity), and Creating/Synthesizing (Advanced/Capstone). This provides a sound pedagogical flow.

**PO:** That aligns well with value delivery too. Foundations & Core Craft represent the MVP, delivering immediate practical skills. Complexity and Advanced Workflows add deeper capabilities, leading to the mastery demonstrated in the Capstone.

**PM:** Structurally, this makes sense for planning content development and potential phased rollout.

**(General agreement on the 5-part structure. Tentative names: Unit 1: Foundations, Unit 2: Core Prompt Craft, Unit 3: Building Complexity & Workflows, Unit 4: Advanced Techniques & Concepts, Unit 5: Capstone & Continuous Learning)**

**Facilitator:** Excellent. Let's dive into the MVP - Units 1 and 2. Unit 1: Foundations - AI/LLM Intro, Prompt Basics, Cursor Intro, Ethics. Unit 2: Core Craft - Zero/Few-Shot, Context Eng I, Output Formatting I, Iteration/Debug I, maybe linking Tokenization basics. What are the essential hands-on activities here?

**SSE:** Absolutely need hands-on in Cursor from day one. Unit 1 needs a basic 'generate a docstring' or 'explain this code' exercise. Unit 2 needs exercises like: provide context using @-mentions and selections, generate unit tests, try few-shot prompting for a specific code style, debug a prompt that gives incorrect output for a simple function.

**Ed UX:** We need an integrated playground/simulation for Unit 2 activities. Guided tutorials for the Unit 1 Cursor basics. The playground should show token counts and allow easy comparison of different prompt attempts.

**AI UX:** The activities should emphasize the *interaction*. How to phrase requests clearly? How to provide minimal effective context? How to react when Cursor misunderstands? Debugging prompts *is* a core UX skill here.

**PR:** These hands-on activities embody situated learning. Frame the debugging exercises (Iterative Refinement) as problem-solving, not just syntax correction. Error analysis is key.

**Facilitator:** Solid plan for the MVP units. Now Unit 3: Building Complexity - CoT, RAG concepts + Context Eng II, Prompt Chaining I, Evaluation I. How do we make CoT practical? What activities?

**PE:** CoT exercises should focus on debugging complex logic or explaining non-trivial algorithms using "step-by-step" prompts within Cursor. For Prompt Chaining, a simple workflow like: 1. Analyze requirements -> 2. Draft function signature -> 3. Implement function skeleton. Keep it within the chat interface initially.

**AOA:** For RAG, simulate it. Give learners relevant documentation snippets *as context* and ask them to write prompts that use that context to answer questions about a related code example. Focus on the *prompting pattern* of incorporating external info.

**SSE:** Evaluating AI output is crucial here. Activity: Review AI-generated unit tests – did they cover edge cases? Review AI-refactored code – did it introduce bugs?

**AIR:** Link CoT exercises to the concept of model reasoning. Link RAG exercises to grounding and reducing hallucinations. Explain context window limitations as the motivation for RAG/advanced context engineering.

**Facilitator:** Good, practical activities for Unit 3. Now, Unit 4: Advanced Techniques. We agreed to focus on concepts and prompting patterns, not deep agent building. What's essential here?

**AAE:** Demonstrate prompting for *simulated* tool use. E.g., "Run the linter (simulated) on this code and summarize the critical issues." Explain agent loops conceptually using diagrams (Ed UX support needed!). Introduce Self-Consistency with an example – run a complex reasoning prompt 3 times, show divergent answers, explain taking the majority.

**AOA:** Meta-prompting example: Prompt that takes high-level test requirements and generates detailed test case prompts. Explain the *pattern*. Briefly cover performance/cost implications of complex chains.

**PE:** Advanced debugging needs case studies: Why did this complex chain fail? How to isolate the faulty prompt? Also, cover prompt templates and sharing best practices.

**AIR:** Discuss security/robustness (prompt injection basics). Briefly introduce ToT/Reflexion as concepts for further exploration.

**Facilitator:** Okay, a conceptual overview of agentics, practical prompting for simulated tools, self-consistency, meta-prompting basics, advanced debugging, evaluation, and security. Now, the Capstone for Unit 5?

**Prof Ed:** Needs to be an authentic SE task allowing application of multiple techniques from Units 2-4. Project-based, assessed on the process and outcome.

**SSE:** I like the idea of refactoring a non-trivial module *using* AI assistance throughout, documenting the prompts used and evaluating the results. Or building a practical workflow helper – like a smart documentation/commit message generator that uses CoT and maybe simple RAG.

**PO:** Scope needs to be manageable. Maybe offer a few project options? Individual or pairs seems good. Showcase is vital – short demos or write-ups.

**PM:** Need clear rubrics and allocated time/support. Pairs might reduce marking load and encourage collaboration.

**Facilitator:** Capstone defined: Authentic SE task, applying multiple techniques, potentially offering choices, individual/pairs, clear rubric, showcase element. Lastly, cross-cutting themes: Ethics, security, evaluation, differentiation?

**AIR:** Ethics/Security shouldn't be just Unit 1. Revisit when discussing evaluation, agent safety, data privacy with RAG/tool use.

**Prof Ed:** Differentiation can be handled via optional advanced exercises within modules, or varying the complexity of the capstone project options. Provide clear pathways for those needing more support vs. those ready for deeper dives.

**AI UX:** Evaluation of AI output needs to be a constant theme – how does the engineer *know* the AI is helping effectively and correctly?

**Facilitator:** Excellent. We have a much more refined structure, clear module goals, concrete activity ideas, and a plan for the capstone. This gives us the detailed skeleton we need.

--- 