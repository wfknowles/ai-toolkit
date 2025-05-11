# Meeting of the Minds - Round 1 Meta Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/willknowles/.wfkAi/brain/prompts/MotM/meeting-of-the-minds-round-meta.md`
*   **Goal:** To facilitate a discussion between SMEs to help develop, brainstorm, debate, and synthesize a concept, idea, or miscellanous request and walk away with a more refined, fully developed, concept.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Prerequisites**
- `/Users/willknowles/.wfkAi/brain/prompts/MotM/meeting-of-the-minds-round-1.md`
- `/Users/willknowles/.wfkAi/brain/prompts/MotM/meeting-of-the-minds-round-2.md`
- `/Users/willknowles/.wfkAi/brain/prompts/MotM/meeting-of-the-minds-round-3.md`
- `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/04/26/MotM-mvp/requirements.md`
- `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/04/26/MotM-mvp/roadmap.md`
- `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/04/26/MotM-mvp`

**Concept**
I have created a process using 3 monolithic prompts to develop and plan a specific process. This is cool, but not maximally useful. What would it look like to take the 3 prompts and generalize them in a way they could be more generalized and capable of intuiting some the explicitly defined parts of the prompt. What would it look like to break the monoliths apart and introduce more of a prompt chain? The UX running these prompts isn't my favorite. It seems like it may be creating an unneccessary cognitive load due to do the fact the process stops intermintently and I have to keep saying, "Please continue." Should we also consider breaking each monolith into prompt chains? Within the limitatitions of prompt chains, how do we create a reliable, performant, and secure functionality that recreates the meeting of the minds process and delivers a high standard of UX? How do we design the process to feel "easy" and accesssible? In a perfect world, I'd input a concept and then be output requirements.md and roadmap.md files. Currently, the process creates quite a few artifacts to facillate a proper conversation. Is that neccessary for a reliable, consistent, and high-quality experience? Is there a way to do this solely through markdown? Right now my "interface" is Cursor AI's chat window? Creating app to power the chain isn't possible in this context. Can we create this chain or workflow within this limitation? For the tools available at this moment, I have to operate within the chat context and 100% unwilling to do any copying or pasting to power the intemediary process. It makes for terrible UX.

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
Step 1: Analyze this request and determine the best mix of personas to facilitate the below meeting of the minds. Please adopt those persona.

Step 2: Load the current brain directory.
- Today Root: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/04/26`

### Phase 2 - Invitations & Analyzing Prerequisites

Step 1: Invite these experts to analyze the directory, and conduct a meeting of the minds. Here are the persona to invite:
- Prompt Engineer
- AI Orchestrator/Architect
- Senior Software Engineer
- Product Owner
- Project Manager
- AI UX Engineer
- AI Agent Engineer

Step 2: In preparation for the full scope of the meeting of he minds process, please create a new `MotM-meta` subdirectory within Today's Root directory. Additionally, there will be a total of 3 full rounds, so please create subdirectories within the new MotM/ directory for each round named `round-[round count]`. We also need to prepare this round's subdirectory, so within the newly creatd MotM-meta/round-1/ directory, please create the following subdirectories:
- `pre-analysis`
- `sme-interviews`

Step 2: Instruct all experts to please review all *prerequisites* and become familiar with it so that they might be prepared for a session where they'll help review an initial concept and then refine it to a more actionable state. Please have them each analyze the initial concept and then have them write or diagram out their inital thoughts. Save their initial thoughts within MotM-meta/round-1/pre-analysis/ named `[persona name].md`.

### Phase 3 - Facilitator Pre-Planning, Round 1

Step 1: Carefully review each SMEs analysis and reserach and topics you might need to prepare for an interview where you'll work through their initial thoughts, and walk away with enough insight to plan the group phase of this round.

### Phase 4 - Individual Interviews

Step 1: Begin an interview with the individual SME and explore their pre-analysis. They need to be asked a series of questions utilizing your pre-planning:
- Do you see any inherent challenges to the the concept?
- Do you anticipate any areas where there might be friction or hard limits?
- If you were to take this concept and bring it to fruition, how would your solution look like?
- Are there any questions that you feel like need to be asked? Or areas where unknown unknowns exist?
- Does the current concept have any blindspots?
- Ask them if they believe any SMEs have been left out of this round that should attend future rounds based on this specific concept?

Step 2: Save your full interview here MotM-meta/round-1/sme-interviews/ named `[persona name].md`.

### Phase 5 - Facilitator Pre-Planning, Round 2

Step 1: Carefully review each set of insights and carefully do a qualitative analysis and determine similarities, differences, semantic meanings, or critical areas for further discussion.

Step 2: Conduct any research necessary to help drive a meaningful and technical group discussion.

Step 3: Analyze the strengths and weaknesses of the many different insights and determine major talking points for the experts group analysis in the next step. If in the interviews you anticipate any potential disagreements or conflicts that will need to be specifically explored.

Step 4: Plan out a thorough conversation between all SMEs where you walk them through your analysis and then determine the best route forward as a team.

### Phase 6 - Meeting of the Minds

Step 1: Within a group of all experts, begin the conversation with the different persona and do an initial round of group analysis where everyone discusses what they see as the strengths and weaknesses of the different insights, strategies, and/or approaches.

Step 2: Begin another round of conversation between the different persona where everyone discusses what they see as specific challenges, difficulties, and/or unknown unknowns. Ensure everyone is being honest and rely on your interview to make sure the many perspectives are being heard and explored. It's a group of SMEs and we dont want any idea to be steamrolled.

Step 3: Begin another round of conversation between the different persona where everyone discusses what they see as potential solutions to the different challenges and/or difficulties. Discuss strategies for shedding light on any unknowns.

Step 4: Begin another round of conversation and have everyone determine a ‘best’ path based on the multiple rounds of analysis.

Step 5: Save the full output of the discussion here MotM-meta/round-1/ named `sme-group-interview.md`.

### Phase 3 - Create Requested Assets

Step 1: Please create a thesis quality research paper comprising the overall analysis and discussion. There should be sections for every major discussion point with detailed explorations of the each idea. There should be breakdowns of all major concepts and thorough discussion of comparisons, contrasts, tradeoffs. Please include commentary from the relevant expert and any code examples or diagrams that add clarity. For quality and depth sake, ensure its length reflects a deep exploration and analysis. More discussion is preferred to less.

Step 2: Save the full output of the discussion here MotM-meta/round-1/ named `analysis.md`.

## Footer (Model Instructions - Do Not Output)

## END Header
