# Research Outline: AI Agent Engineer (AAE)

**Thesis Title:** Prompting for Agency: A Research Plan for Introducing AI Agent Concepts and Techniques in Engineering Education

**Abstract:** This paper outlines the research and development plan for the Agent Architectures module (Unit 4.2) of the Prompt Engineering Mastery curriculum (`curriculum.md`). Based on AAE perspectives from SME inputs (`pre-analysis/`, `pre-interviews/`), it focuses on defining research required to effectively teach introductory AI agent concepts (e.g., planning, tool use, simple loops like ReAct) and the associated prompt engineering skills to software engineers. Research tasks for RAs include investigating pedagogical strategies for the agent mindset shift, identifying suitable simple agent patterns and SE demonstration tasks, exploring effective prompting techniques for agent guidance (planning, tool description, correction), and analyzing how to present agent limitations and risks. Development tasks will involve creating clear conceptual explanations, designing contained exercises runnable in Cursor/scripts, and providing robust prompt examples, ensuring learners grasp the fundamentals of prompting for agentic behavior.

---

**Detailed Outline:**

**1. Introduction**
    1.1. Problem Statement: The challenge of introducing the concepts and prompting techniques for AI agents to engineers accustomed to deterministic systems.
    1.2. Course Context: Focus on Unit 4.2 (Agent Architectures) within the 5-Unit `curriculum.md`.
    1.3. Synthesis of Prior Work: Key AAE contributions regarding mindset shift, conceptual focus (vs. frameworks), core loops (ReAct), planning prompts, tool use, limitations, and risks (`prompt-mastery/...`, `round-2/...`).
    1.4. Thesis Goal: Define R&D tasks for Unit 4.2 to ensure effective teaching of foundational agent concepts and prompting skills.
    1.5. Outline Structure.

**2. Pedagogical Strategies for Agent Concepts**
    2.1. Research Question: What are the most effective pedagogical methods (e.g., analogies, visualizations, conceptual models) for explaining the core concepts of agent loops (Plan-Act-Observe, ReAct), planning, and tool use to engineers? (Ref: AAE, AOA, AIR interviews)
    2.2. Research Tasks (for RAs):
        2.2.1. Research conceptual models for explaining basic agent architectures suitable for novices.
        2.2.2. Investigate analogies that bridge from traditional programming concepts to agent behavior.
        2.2.3. Survey visualization techniques applicable to agent decision-making loops (Ref: Ed UX interview).
        2.2.4. Analyze literature on teaching complex systems thinking.
    2.3. Development Tasks:
        2.3.1. Develop clear, concise explanations of the target agent concepts (ReAct, simple loops).
        2.3.2. Create visualizations and analogies for the agent module (Lesson 4.2.1) (Coord with Ed UX).

**3. Designing Introductory Agent Exercises**
    3.1. Research Question: What types of simple, constrained exercises, runnable within Cursor or basic scripts, can effectively demonstrate agentic patterns and allow engineers to practice the associated prompting techniques? (Ref: AAE, AOA, SSE interviews)
    3.2. Research Tasks (for RAs):
        3.2.1. Identify minimal SE tasks suitable for demonstrating planning, tool use, and iteration within a simple agent loop (e.g., multi-step code generation, API query based on analysis).
        3.2.2. Research simple execution environments (e.g., Python scripts) or ways to simulate agent steps within Cursor chat.
        3.2.3. Analyze how to scaffold exercises from observing an agent to actively prompting its steps.
    3.3. Development Tasks:
        3.3.1. Design 2-3 specific exercises for Lesson 4.2.1 demonstrating core agent concepts.
        3.3.2. Develop necessary scaffolding code or simulation setup for the exercises.
        3.3.3. Create clear instructions and expected outcomes for agent exercises.

**4. Researching Effective Prompting Techniques for Agents**
    4.1. Research Question: What specific prompt structures and content are most effective for guiding basic agent behaviors like planning, tool selection/use, and simple self-correction in the context of introductory exercises? (Ref: AAE, PE interviews)
    4.2. Research Tasks (for RAs):
        4.2.1. Survey literature and examples (e.g., from LangChain, DSPy) for effective planning prompts.
        4.2.2. Research best practices for writing clear and effective tool descriptions for LLMs.
        4.2.3. Investigate basic prompting strategies for encouraging reflection or correction in agent outputs.
    4.3. Development Tasks:
        4.3.1. Develop example prompts for planning, tool use, and correction tailored to the course exercises.
        4.3.2. Create guidelines or templates for writing effective agent-guiding prompts.
        4.3.3. Ensure prompt examples are robust enough for the constrained exercise environment.

**5. Addressing Agent Limitations and Risks**
    5.1. Research Question: How can the curriculum effectively communicate the inherent limitations (e.g., brittleness, predictability issues), failure modes (e.g., looping, hallucination), and potential risks (e.g., misuse of tools, security) of agentic systems? (Ref: AAE interview emphasis)
    5.2. Research Tasks (for RAs):
        5.2.1. Catalog common failure modes observed in simple agent systems.
        5.2.2. Research ethical considerations and safety best practices related to autonomous agents.
        5.2.3. Identify strategies for human oversight and intervention in agent workflows.
    5.3. Development Tasks:
        5.3.1. Integrate discussion of limitations, risks, and safety into Lesson 4.2.1 and potentially the Responsible AI module (5.2).
        5.3.2. Include examples or warnings of potential agent failures in exercises or demonstrations.
        5.3.3. Develop guidelines on responsible agent prompting and monitoring.

**6. Conclusion & Next Steps**
    6.1. Summary of Research Questions and Development Tasks for the Agent Module.
    6.2. Dependencies (AOA for architecture, PE for core prompts, Ed UX for visuals, AIR for theory).
    6.3. Call for feedback on scope and approach for teaching agent concepts.

**7. Bibliography / References**
    7.1. Curriculum Document (`curriculum.md`)
    7.2. Round 1 Pre-Analysis & Interview (`prompt-mastery/...`)
    7.3. Round 2 Pre-Analysis & Interviews (`round-2/...`)
    7.4. (RA Task) Relevant external literature on AI agents, cognitive architectures (e.g., ReAct), prompt engineering for agents, AI safety. 