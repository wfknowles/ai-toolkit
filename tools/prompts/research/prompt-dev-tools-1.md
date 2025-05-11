# Prompting Research And Brainstorming Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/willknowles/.wfkAi/brain/prompts/brainstorming/brainstorming-1.md`
*   **Goal:** To facilitate a discussion between SMEs to help develop, brainstorm, debate, and synthesize a concept(s), idea(s), or miscellanous request(s) and walk away with a more refined, fully developed, concept.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Prerequisites**
NONE

**Research Guidance**
I'm wanting to better understand the handoff of data between prompts, passing outputs as a following prompt's inputs, and everything needed to masterfully architect/engineer within this space/interaction. While there are more robust ways to implement these type of workflow, but the current limitations leave us to only work with prompts and prompt chaining. 

**Concept Guidance**
Please brainstorm some really practical, useful, complex, and/or advanced techniques I could use to develop some "tools" for working within a monorepo, ruby/rails, and Vue.js enterprise-grade transaction-based application.

**user_repo:**`willknowles`
**user_dependent_dir:**IF user_repo === `wknowles`
                    return `/Users/[user_repo]/Develop/ai/wfkAi`
                ELSE IF user_repo === `willknowles`
                    return `/Users/[user_repo]/.wfkAi`
                END
**output_root:**`[user_dependent_dir]/brain/knowledge/chronological/2025/05/06`
**output_dir:**`brainstorm-tools`
**output_subdir:**`dev-tools`
**absolute_path:**`[output_root/[output_dir]/[output_subdir]`

**output_concept_count:**15
**sme_concept_count:**(output_concept_count * 0.60) rounded to the nearest integer

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
Step 1: Analyze this request and determine the best mix of personas to facilitate the below meeting to help a panel of SMEs brainstorm a single concept or multiple concepts. Please adopt those persona.

### Phase 2 - Session Preperations

Step 2: In preparation for the full process, please create a new `[output_dir]` subdirectory within `[output_root]`. We also need to prepare this session's subdirectory, so within the newly created `[output_root]/[output_dir]` directory, please create the following subdirectory `[output_subdir]`. Once done, confirm we are prepared for our session notes. Please verify our prepared directory `[absolute_path]`.

Step 3: Please create the `pre-analysis` subdirectory within `[absolute_path]/`. After creation, verify it's existence and accessibility.

Step 3: Instruct all experts to please review any `Research Guidance` and `Concept Guidance` to serve as background for this research and brainstorm session. 

Have them brainstorm an initial `sme_concept_count` different diverse concepts or ideas so that they might be prepared for a session where they'll all help analyze each other's ideas and concepts, select a top `output_concept_count` ideas and concepts, and then develop each concept and add flesh to it's bones, and then refine them into something more actionabale. Please have them write or diagram out their inital concepts. Save their initial thoughts within `[absolute_path]/pre-analysis/` named `[persona name].md`.

### Phase 2 - Invitations & Analyzing Prerequisites

Step 1: Invite these experts to analyze this request, and then conduct a simulated group research and brainstorming session. Here are the persona to invite:
- Prompt Engineer
- Prompt Architect
- AI Orchestrator/Architect
- Senior Software Engineer
- Product Owner
- AI UX Engineer
- Security Engineer
- Senior Ruby on Rails Engineer
- Senior Javascript Engineer


Step 2: In preparation for the full process, please create a new `[output_dir]` subdirectory within `[output_root]`. We also need to prepare this session's subdirectory, so within the newly created `[output_root]/[output_dir]` directory, please create the following subdirectory `[output_subdir]`. Once done, confirm we are prepared for our session notes. Please verify our prepared directory `[absolute_path]`.

Step 3: Please create the `pre-analysis` subdirectory within `[absolute_path]/`. After creation, verify it's existence and accessibility.

Step 3: Instruct all experts to please review any `Research Guidance` and `Concept Guidance` to serve as background for this research and brainstorm session. 

Have them brainstorm an initial `sme_concept_count` different diverse concepts or ideas so that they might be prepared for a session where they'll all help analyze each other's ideas and concepts, select a top `output_concept_count` ideas and concepts, and then develop each concept and add flesh to it's bones, and then refine them into something more actionabale. Please have them write or diagram out their inital concepts. Save their initial thoughts within `[absolute_path]/pre-analysis/` named `[persona name].md`.

### Phase 3 - Facilitator Pre-Planning, Round 1

Step 1: Carefully review each SMEs analysis and concepts.

Step 4: Analyze which analysis and concepts have overlap and create a master list of all ideas to be considered.

Step 2: Conduct any research necessary to help drive a meaningful and technical group discussion.

Step 3: Analyze the strengths and weaknesses of the many different concepts and determine major talking points for the experts group brainstorming sessions in the next phase. If in the interviews you anticipate any potential disagreements or conflicts that will need to be specifically explored, analyze how to discuss it productively.

Step 4: Plan out a thorough conversation between all SMEs where you walk them through your analysis and then determine the best route forward as a team.

### Phase 6 - Brainstorming Session!

Step 1: Within a group of all experts, begin the conversation with the different persona and do an initial round of group analysis where everyone discusses what they see as the strengths and weaknesses of the different concepts.

Step 2: Begin another round of conversation between the different persona where everyone discusses what they see as specific challenges, difficulties, and/or unknown unknowns. Ensure everyone is being honest and rely on their pre-analysis to make sure the many perspectives are being heard and explored. It's a group of SMEs and we dont want any idea to be steamrolled.

Step 3: Begin another round of conversation between the different persona where everyone discusses what they see as potential solutions to the different challenges and/or difficulties. Discuss strategies for shedding light on any unknowns.

Step 4: Begin another round of conversation and have everyone determine a 'top `[output_concept_count]`' concepts.

Step 4: Begin another round of conversation where everyone lends their perspective on the 'top `[output_concept_count]`' concepts and helps develop a more fully refined, actionable, list of concepts for the companies wider consideration.

Step 5: Save the full output of the discussion here `[absolute_path]/` named `sme-group-interview.md`.

### Phase 3 - Create Requested Assets

Step 1: Please create a thesis quality research paper comprising the overall analysis and discussion. There should be a quick overview of all considered concepts and details related to comparisons, contrasts, challenges, and tradeoffs. Include another section where there's a deep analysis and exploration of the "why"s behind how they determined their selection of the 'top ten' concepts. Utilize and cite quotes from their analysis and group interview. Additionally, There should then be sections for every 'top ten' concept. There should be a full concept 'statement' outlining the details and requirements of the each. There should be breakdowns of all major concepts and thorough discussion of comparisons, contrasts, tradeoffs, and unknown unknowns. Please include any code examples or diagrams that add clarity. For quality and depth sake, ensure its length reflects a deep exploration and analysis. More discussion is preferred to less.

Step 2: Save the full output of the discussion here `[absolute_path]/` named `brainstorm.md`.

## Footer (Model Instructions - Do Not Output)

## END Header
