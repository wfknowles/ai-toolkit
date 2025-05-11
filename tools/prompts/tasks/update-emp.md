# Peer Review - Agentic Framework Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/wknowles/Develop/ai/wfkAi/brain/prompts/peer-review/peer-review-1.md`
*   **Goal:** To facilitate a discussion between SMEs to help develop, brainstorm, debate, and synthesize a concept, idea, or miscellanous request and walk away with a more refined, fully developed, concept.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Prerequisites**
NONE

**Concept**

**user:**`wknowles`
**output_root:**`/Users/[user]/.wfkAi/brain/knowledge/chronological/2025/04/29`
**output_dir:**`[output_root]/agentic-framework`

**Original Reqs:**`/Users/wknowles/Develop/ai/wfkAi/brain/knowledge/chronological/2025/04/29/agentic-framework-motm/requirements.md`
**Original Roadmap:**`/Users/wknowles/Develop/ai/wfkAi/brain/knowledge/chronological/2025/04/29/agentic-framework-motm/roadmap.md`
**Agent Framework:**`/Users/wknowles/Develop/ai/wfkAi/brain/knowledge/chronological/2025/04/29/agentic-framework-motm`

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
Step 1: Analyze this request and determine the best mix of personas to facilitate the below peer review meeting. Please adopt that mix of those persona.

### Phase 2 - Invitations & Analyzing Prerequisites

Step 1: Invite the following SMEs to a peer review meeting:
- Prompt Engineer
- AI Orchestrator/Architect
- Senior Software Engineer
- Product Owner
- AI UX Engineer
- AI Agent Engineer
- Security Engineer
- Senior QA

Step 2: In preparation for the full scope of the peer review process, please create a new `[output_dir]` subdirectory within `[output_root]`. Additionally, there will be a total of 3 full rounds, so please create subdirectories within the new MotM/ directory for each round named `round-[round count]`. We also need to prepare this round's subdirectory, so within the newly creatd [output_dir]/ directory, please create the following subdirectories:
- `pre-analysis`
- `sme-interviews`

Step 2: Instruct all experts to please review:
    - The `Original Reqs` that that the roadmap was built from.
    - The `Original Roadmap` used to guide it'd development.
    - The `Agent Framework` itself.

Step 3: Please have them each analyze the `Original Reqs` and `Original Roadmap` so they can have the knowledge of the project's inception. Then, have them CAREFULLY AND THOROUGHLY review our `Agent Framework`. As they analyze the project, have them begin to compile notes on their perspective on the project, whether they have concerns, what they believe should be reviewed/refactored, or any flaws they see in the design, code, or testing strategies. Save their initial thoughts within [output_dir]/pre-analysis/ named `[persona name].md`.

### Phase 3 - Facilitator Pre-Planning, Round 1

Step 1: Carefully review each SMEs analysis and research any of the topics you might need to prepare for a group interview where you'll work through their initial thoughts, and walk away with a solid quality analysis of the project and a roadmap for improvement.

### Phase 4 - Group Peer Review

Step 1: Within a group of all experts, begin the conversation with the different persona and do an initial round of group analysis where everyone discusses what they see as the strengths and weaknesses of the project and it's current implementation.

Step 2: Begin another round of conversation between the different persona where everyone discusses what they see as specific challenges, difficulties, or surprises that may arise due to how the project has been constructed. Ensure everyone is being honest and rely on their pre-analysis to make sure the many perspectives are being heard and explored. It's a group of SMEs and we dont want any idea to be steamrolled.

Step 3: Begin another round of conversation between the different persona where everyone discusses what they see as potential concerns, risks, or flaws of the current implementation. Discuss strategies for shedding light on any unknowns.

Step 4: Begin another round of conversation and have everyone determine an agreed upon list of feedback and recommendation based on their analysis.

Step 5: Save the full output of the discussion here [output_dir]/ named `sme-group-interview.md`.

### Phase 5 - Create Requested Assets

Step 1: Please create a thesis quality research paper comprising the overall analysis and discussion. There should be sections for every major discussion point with detailed explorations of the each idea. There should be breakdowns of all major concepts and thorough discussion of comparisons, contrasts, tradeoffs. Please include commentary from the relevant expert and any code examples or diagrams that add clarity. For quality and depth sake, ensure its length reflects a deep exploration and analysis. More discussion is preferred to less.

Step 2: Save the full output of the discussion here [output_dir]/ named `peer-review.md`.


## Footer (Model Instructions - Do Not Output)

## END Header
