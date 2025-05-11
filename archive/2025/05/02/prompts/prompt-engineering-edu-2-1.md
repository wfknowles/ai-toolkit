# Educational Content Prompt - Round 2, Part I

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/prompts/prompt-engineering-edu-2.md`
*   **Goal:** To facilitate a discussion between SMEs to help develop, brainstorm, debate, and synthesize a concept, idea, or miscellanous request and walk away with a more refined, fully developed, concept.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Prerequisites**
NONE

**Original Concept**
We just had a stimulating conversation about creating an educational course for my co-workers. Please review that discussion: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/prompt-mastery/sme-group-interview.md`. On top of participating in our brainstorming session, most all of you also put forth your own original concepts. Make yourselves familiar with everyone's initial concepts within here: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/prompt-mastery/pre-analysis`. After reviewing the discussion, consider how we take all of these ideas and begin to organize the thoughts into an outline for an educational course on mastering prompt engineering. Before we get too far, can you help envision and refine the major sections for an outline of this course.

**Concept**
We just had a stimulating conversation about creating an educational course for my co-workers. Please review that discussion: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/sme-group-interview.md`. Make yourselves familiar with everyone's initial outlines and thoughts: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/pre-analysis`. Additionally, please review the agreed upon curriculum based on all analysis and group discussion: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/02/edu/prompt-engineering/curriculum.md`. After reviewing all materials and the discussion, consider that I think we need to create some materials to help guide the overall development of the educational course. I think we need to compile some research to serve as the foundation of the curriculum. I think we need to create two sets of roadmaps and requirements. One to guide the research phase of developing the curriculum, and another to guide the development of the actual course content. These are large undertakings and we need to be strategic in how we design our course on prompt engineering. It's an emerging field and the goal is to be the most comprehensive curriculum on prompt engineering mastery (focused on software engineering). 

**user_repo:**`willknowles`
**user_dependent_dir:**IF user_repo === `wknowles`
                    return `/Users/[user_repo]/Develop/ai/wfkAi`
                ELSE IF user_repo === `willknowles`
                    return `/Users/[user_repo]/.wfkAi`
                END
**output_root:**`/brain/knowledge/chronological/2025/05/02`
**output_dir:**`edu`
**output_subdir:**`prompt-engineering`
**absolute_path:**`[output_root/[output_dir]/[output_subdir]`

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
Step 1: Analyze this request and determine the best mix of personas to facilitate the below discussion on converting the `Concept` into a fully developed plan for researching and developing and educational course on the `Original Concept`. Please adopt the relevant persona at the appropriate steps.

### Phase 2 - Invitations & Analyzing Prerequisites - (Model Instructions: Review the rest of the prompt and determine which context is no longer needed. Once completed, remove the unneeded context. Please verify it's removal.)

[] Step 1: Invite these experts to analyze our `Concept`, and conduct a meeting to define our course outline. Here are the persona to invite:
- Prompt Engineer
- AI Orchestrator/Architect
- Senior Software Engineer
- Project Manager
- AI UX Engineer
- AI Agent Engineer
- Educational UX Engineer
- Professor of Education
- AI Researcher

[] Step 2: We need to prepare this round's subdirectory, so within `[absolute_path]/round-2` directory, please create the following subdirectories:
- `pre-analysis`
- `pre-interviews`

[] Step 3: Verify we are prepared for our session, please confirm our prepared directory `[absolute_path]/round-2/pre-analysis/`.

[] Step 2: Instruct all experts to please review the `Concept` and become familiar with it so that they might be prepared for a session where they'll help thoroughly review the `Concept` and then convert it into a detailed set of requirements and roadmaps to help guide the research and development phases for the educational course. Please have them analyze the different modules and units and begin to develop and outline initial ideas for lessons and then "abstracts" that we could use to shape the modules and units. Feel free to include examples or diagrams to help improve your analysis. Save their initial thoughts within `[absolute_path]/round-2/pre-analysis/` named `[persona-name].md`.

### Phase 3 - Facilitator Pre-Planning, Round 1 - (Model Instructions: Review the rest of the prompt and determine which context is no longer needed. Once completed, remove the unneeded context. Please verify it's removal.)

[] Step 1: Carefully review each SMEs analysis and research any topics you might need to prepare for an interview where you'll work through their initial outline and thoughts, and walk away with enough insight to plan the group interview phase of this session.

### Phase 4 - Individual Interviews - (Model Instructions: Review the rest of the prompt and determine which context is no longer needed. Once completed, remove the unneeded context. Please verify it's removal.)

Overview: Begin an interview with the individual SME and explore their pre-analysis. They need to be asked a series of questions utilizing your pre-planning.

[] Step 1: Do you see any inherent challenges to adding more detail to each module and unit, or determing lessons?

[] Step 2: Do you see any modules or units within the curriculum that might need to be reviewed?

[] Step 3: Do you feel like the curriculum is geared toward a working software engineer? Is there anything at risk of being too basic? Engineers are fairly technical and bright. Is there anything in the curriculum that might be paced or broken apart that might cause an engineer to feel the course is boring or beneath them?

[] Step 4: Based on your initial lesson concepts, what do you see as strengths, weaknesses, challenges, or potential blockers?

[] Step 5: Within the research phase, do you feel like there are any modules, units, or lessons where you feel especially qualified to lead the research, analysis, and/or documentation?

[] Step 6: Within developing requirements and roadmaps, do you feel like there are any modules, units, or lessons where you may be the relevant SME to defer to?

[] Step 7: Are there any SME that you think should be invited for the group phase of the session?

[] Step 8: What have I not asked that you feel is important to consider, analyze, or weigh in on?

[] Step 8:Save the interview within `[absolute_path]/round-2/pre-interviews/` named `[persona-name].md`.


## Footer (Model Instructions: Do Not Output. Please determine which context has accumalated related to this prompt. Once completed, remove the unneeded context. Please verify it's removal.)

## END Header
