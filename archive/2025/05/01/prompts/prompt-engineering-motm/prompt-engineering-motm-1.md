# Meeting of the Minds - Round 1 Meta Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/wknowles/Develop/ai/wfkAi/brain/knowledge/chronological/2025/05/01/prompts/dependency-manager-motm/dependency-manager-motm-1.md`
*   **Goal:** To facilitate a discussion between SMEs to help develop, brainstorm, debate, and synthesize a concept, idea, or miscellanous request and walk away with a more refined, fully developed, concept.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Prerequisites**
NONE

**Concept**
We just had a stimulating conversation about creating an educational course. After reviewing the analysis and recommendations within `/Users/wknowles/Develop/ai/wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/update-deps/brainstorm.md`, please review the group interview `/Users/wknowles/Develop/ai/wfkAi/brain/knowledge/chronological/2025/05/01/brainstorm-tools/update-deps/sme-group-interview.md` so that you can understand their decision making. Please also review any of the SMEs initial ideas for whether they should be implemented within this overall concept. Add flesh to these bones and then create the concept to workshop within this process.

**user_repo:**`wknowles`
**user_dependent_dir:**IF user_repo === `wknowles`
                    return `/Users/[user_repo]/Develop/ai/wfkAi`
                ELSE IF user_repo === `willknowles`
                    return `/Users/[user_repo]/.wfkAi`
                END
**output_root:**`/brain/knowledge/chronological/2025/05/01`
**output_dir:**`brainstorm-tools/prompt-mastery`
**output_subdir:**`prompt-mastery-motm`
**absolute_path:**`[output_root/[output_dir]/[output_subdir]`

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
Step 1: Analyze this request and determine the best mix of personas to facilitate the below meeting of the minds. Please adopt those persona.

### Phase 2 - Invitations & Analyzing Prerequisites

Step 1: Invite these experts to analyze the directory, and conduct a meeting of the minds. Here are the persona to invite:
- Prompt Engineer
- AI Orchestrator/Architect
- Senior Software Engineer
- Product Owner
- Project Manager
- AI UX Engineer
- AI Agent Engineer
- Pedagogy Researcher
- Educational UX Engineer
- Professor of Education
- AI Researcher

Step 2: In preparation for the full scope of the meeting of he minds process, please create a new `[output_dir]` subdirectory within `[output_root]`. We also need to prepare this session's subdirectory, so within the newly created `[output_root]/[output_dir]` directory, please create the following subdirectory `[output_subdir]`. Additionally, there will be a total of 3 full rounds in this series, so please create subdirectories within the new `[absolute_path]` directory for each round named `round-[round count]`. We also need to prepare this round's subdirectory, so within the newly created `[absolute_path]/round-1/` directory, please create the following subdirectories:
- `pre-analysis`
- `sme-interviews`

Step 3: Verify we are prepared for our session notes, please confirm our prepared directory `[absolute_path]`.

Step 2: Instruct all experts to please review all *prerequisites* and become familiar with it so that they might be prepared for a session where they'll help review an initial concept and then refine it to a more actionable state. Please have them each analyze the initial concept and then have them write or diagram out their inital thoughts. Save their initial thoughts within `[absolute_path]/round-1/pre-analysis/` named `[persona-name].md`.

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

Step 2: Save your full interview here `[absolute_path]/round-1/sme-interviews/` named `[persona-name].md`.

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

Step 5: Save the full output of the discussion here `[absolute_path]/round-1/` named `sme-group-interview.md`.

### Phase 3 - Create Requested Assets

Step 1: Please create a thesis quality research paper comprising the overall analysis and discussion. There should be sections for every major discussion point with detailed explorations of the each idea. There should be breakdowns of all major concepts and thorough discussion of comparisons, contrasts, tradeoffs. Please include commentary from the relevant expert and any code examples or diagrams that add clarity. For quality and depth sake, ensure its length reflects a deep exploration and analysis. More discussion is preferred to less.

Step 2: Save the full output of the discussion here `[absolute_path]/round-1/` named `analysis.md`.

## Footer (Model Instructions - Do Not Output)

## END Header
