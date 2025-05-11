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
I've been iterating a ton and have finally landed on what might be the solution for integrating my work into Cursor IDE... prompt servers. Can you flesh out how to create a MCP and then finish out the development of this concept so that the MCP has our brain functionality. There's a lot here I dont know. What are the components of an MCP? How we do we do this elegantly, simply, securely? What's the big picture for an MCP? What should the MVP be? Experts... I'm really leaning on you here. Could we do it with simply prompts and state like here: /Users/willknowles/.wfkAi/brain/workflows/orchestrators/MotM? Or is there a better practice that respects the limitations of not being able to connect directly to a model api AND doesnt include copy/paste. Im driving for the highest quality UX and copy/paste is truly the worst. Let's see what you've got.

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
Step 1: Analyze this request and determine the best mix of personas to facilitate the below meeting of the minds. Please adopt those persona.

Step 2: Load the current brain directory.
- Today Root: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/04/28`

### Phase 2 - Invitations & Analyzing Prerequisites

Step 1: Invite these experts to analyze the directory, and conduct a meeting of the minds. Here are the persona to invite:
- Prompt Engineer
- AI Orchestrator/Architect
- Senior Software Engineer
- Product Owner
- Project Manager
- AI UX Engineer
- AI Agent Engineer

Step 2: In preparation for the full scope of the meeting of he minds process, please create a new `MotM-mcp` subdirectory within Today's Root directory. Additionally, there will be a total of 3 full rounds, so please create subdirectories within the new MotM/ directory for each round named `round-[round count]`. We also need to prepare this round's subdirectory, so within the newly creatd MotM-meta/round-1/ directory, please create the following subdirectories:
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
