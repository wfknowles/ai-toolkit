# Research Outline: Educational UX Designer (Ed UX)

**Thesis Title:** Designing Engaging and Effective Learning Journeys: An Educational UX Research Plan for the Prompt Engineering Mastery Course

**Abstract:** This paper outlines a research plan from the Educational User Experience (Ed UX) perspective, focusing on optimizing the overall learning journey for the Prompt Engineering Mastery course (`curriculum.md`). Complementing the in-IDE focus of AI UX, this plan synthesizes Ed UX insights from SME discussions (`pre-analysis/`, `pre-interviews/`) to define research questions and tasks for RAs. Key areas include investigating best practices for visualizing abstract concepts (Units 1, 3, 4), designing activities that foster active learning and reflection across all units, strategies for managing cognitive load and scaffolding complex topics (Units 3, 4), accommodating diverse learner preferences, and ensuring the overall course flow is engaging and motivating for software engineers. This research aims to inform the development of a pedagogically sound, learner-centered, and highly effective educational experience.

---

**Detailed Outline:**

**1. Introduction**
    1.1. Problem Statement: Designing a learning experience for a complex technical skill that is engaging, effective, and scalable for ~200 engineers.
    1.2. Course Context: Overview of the 5-Unit `curriculum.md` from a learning journey perspective.
    1.3. Synthesis of Prior Work: Key Ed UX contributions regarding active learning, visualization, cognitive load, scaffolding, feedback, engagement, learning preferences, and accessibility (`prompt-mastery/...`, `round-2/...`).
    1.4. Thesis Goal: Define R&D tasks to ensure the overall course design maximizes learning effectiveness and engagement based on educational UX principles.
    1.5. Outline Structure.

**2. Visualization Strategies for Abstract Concepts**
    2.1. Research Question: What types of visualizations (static diagrams, interactive simulations, animations) are most effective for explaining abstract concepts like tokenization (1.1.1, 2.2.1), LLM internals (1.1), prompt chaining flows (3.3), RAG processes (3.2), and agent loops (4.2)? (Ref: Ed UX, AI UX, AOA, AIR interviews)
    2.2. Research Tasks (for RAs):
        2.2.1. Review literature on multimedia learning principles and effective visualization design for technical concepts.
        2.2.2. Survey existing visualizations used in AI/CS education.
        2.2.3. Analyze the specific conceptual hurdles in the curriculum and identify where visualizations would be most impactful.
        2.2.4. Collaborate with AI UX on feasibility and integration options (in-IDE vs. external).
    2.3. Development Tasks:
        2.3.1. Design and develop specific visualizations for key abstract concepts across the curriculum (Coord with AI UX, Technical SMEs).
        2.3.2. Ensure visualizations are clear, accurate, accessible, and aligned with learning objectives.
        2.3.3. Test effectiveness of visualizations with target users (if possible).

**3. Designing for Active Learning and Reflection**
    3.1. Research Question: What types of activities (beyond hands-on coding) can be integrated throughout the course to promote active learning, critical thinking, and metacognitive reflection on prompt engineering strategies? (Ref: Ed UX, Prof Ed, PR interviews)
    3.2. Research Tasks (for RAs):
        3.2.1. Research active learning strategies suitable for online/blended technical training (e.g., case studies, peer review, debates, concept mapping).
        3.2.2. Investigate methods for embedding metacognitive prompts or reflective exercises within lessons.
        3.2.3. Explore platforms or techniques for facilitating peer interaction and collaborative learning at scale.
    3.3. Development Tasks:
        3.3.1. Design specific non-coding activities for each unit to reinforce concepts and encourage deeper thinking (e.g., analyzing prompt failures, critiquing AI outputs, designing prompt strategies).
        3.3.2. Develop rubrics or guidelines for peer review activities (Coord with Prof Ed).
        3.3.3. Integrate reflective prompts into lesson structures or exercises.

**4. Managing Cognitive Load and Scaffolding Complexity**
    4.1. Research Question: How should the learning content and activities, particularly in Units 3 and 4, be structured and sequenced to effectively manage cognitive load and scaffold learners from basic techniques to complex workflows and agentic concepts? (Ref: Ed UX, Prof Ed, PR, AOA interviews)
    4.2. Research Tasks (for RAs):
        4.2.1. Apply Cognitive Load Theory principles to analyze the demands of each module.
        4.2.2. Research instructional design strategies for scaffolding complex skills (e.g., worked examples, fading support, chunking).
        4.2.3. Analyze dependencies between lessons and identify optimal learning pathways.
    4.3. Development Tasks:
        4.3.1. Structure content within modules using clear chunking and logical sequencing.
        4.3.2. Design introductory examples and gradually increase complexity within units.
        4.3.3. Ensure clear signposting and connections between related concepts across different units.
        4.3.4. Develop worked examples for complex techniques or workflows (Coord with Technical SMEs).

**5. Accommodating Learner Diversity and Motivation**
    5.1. Research Question: How can the course design offer flexibility and variety in presentation and activities to accommodate diverse learning preferences (visual, textual, interactive) and maintain motivation throughout the ~5 Units? (Ref: Ed UX, Prof Ed interviews)
    5.2. Research Tasks (for RAs):
        5.2.1. Research models of learning preferences (e.g., VARK) and their application to online learning.
        5.2.2. Investigate gamification techniques or elements of choice that can enhance engagement in technical training.
        5.2.3. Analyze strategies for providing differentiated pathways or optional advanced content.
    5.3. Development Tasks:
        5.3.1. Incorporate a mix of content formats (text, visuals, video snippets, interactive elements) where feasible.
        5.3.2. Design a variety of practice activities (labs, quizzes, reflective questions, optional challenges).
        5.3.3. Clearly label optional or advanced content.
        5.3.4. Ensure a clear narrative and connection to practical SE benefits throughout the course to maintain relevance (Coord with SSE).

**6. Conclusion & Next Steps**
    6.1. Summary of Research Questions and Development Tasks for Educational UX.
    6.2. Dependencies (AI UX for IDE integration, Prof Ed/PR for pedagogy, Technical SMEs for content, PM for overall structure).
    6.3. Call for feedback on learning journey design priorities.

**7. Bibliography / References**
    7.1. Curriculum Document (`curriculum.md`)
    7.2. Round 1 Pre-Analysis & Interview (`prompt-mastery/...`)
    7.3. Round 2 Pre-Analysis & Interviews (`round-2/...`)
    7.4. (RA Task) Relevant external literature on Instructional Design, Educational Psychology, Multimedia Learning, Active Learning, Cognitive Load Theory, UX Design. 