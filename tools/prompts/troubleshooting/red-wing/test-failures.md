
# Testing Errors Troubleshooting Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/wknowles/Develop/ai/wfkAi/brain/prompts/troubleshooting/red-wing/test-failures.md`
*   **Goal:** To provide analysis on recent testing errors.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Prerequisites**
NONE

**Troubleshooting Guidance**
I just ran some tests via CLI using `bin/run-core.sh test`. Can you review the output and determine

**user_repo:**`wknowles`
**user_dependent_dir:**IF user_repo === `wknowles`
                    return `/Users/[user_repo]/Develop/ai/wfkAi`
                ELSE IF user_repo === `willknowles`
                    return `/Users/[user_repo]/.wfkAi`
                END
**output_root:**`/brain/knowledge/chronological/2025/05/05`
**output_dir:**`red-wing`
**output_subdir:**`testing`
**absolute_path:**`[output_root/[output_dir]/[output_subdir]`

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
Step 1: Analyze this request and determine the best mix of personas to facilitate the below meeting to help a panel of SMEs review and analyze testing logs. Please adopt those persona.

### Phase 2 - Invitations & Analyzing Prerequisites

Step 1: Invite these experts to analyze the most recent testing logs, and conduct a meeting of the minds. Here are the persona to invite:
- Prompt Engineer
- Senior Software Engineer
- Senior Ruby Engineer
- Senior Rails Developer
- Senior Rails Test Engineer
- Senior QA Engineer
- Principal Architect

Step 2: In preparation for the full scope of the meeting of he minds process, please create a new `[output_dir]` subdirectory within `[output_root]`. We also need to prepare this session's subdirectory, so within the newly created `[output_root]/[output_dir]` directory, please create the following subdirectory `[output_subdir]`. Once done, verify we are prepared for our session notes, please very our prepared directory `[absolute_path]/`.

Step 3: In preperation for gathering our experts initial analyses, troubleshooting insights, and likely solutions, we need to create the `pre-analysis` subdirectory. After creation, verify it's existence and accessibility.

Step 3: Instruct all experts to please review any `Troubleshooting Guidance` to serve as background for this group analysis and solutioning. Have them review the terminal logs and then provide their expert analysis on what the likely culprit(s) for test failures across the board, any insights they feel their background initially gives them, any overviews on how to rectify the situation, and brief step by step overview of the actions that need to be taken to have passing tests. Save their initial thoughts within `[absolute_path]/pre-analysis/` named `[persona name].md`.

Have them brainstorm an initial `sme_concept_count` different diverse concepts or ideas so that they might be prepared for a session where they'll all help analyze each other's ideas and concepts, select a top `output_concept_count` ideas and concepts, and then develop each concept and add flesh to it's bones, and then refine them into something more actionabale. Please have them write or diagram out their inital concepts.

### Phase 3 - Facilitator Pre-Planning (Model Instructions - Do Not Output. Please analyze the rest of this prompt and remove any accumulated context from this prompt that is no longer needed for it's execution.)

* Step 1: Carefully review each SMEs analysis and solutions.

* Step 2: Analyze which analysis and concepts have overlap and create a master list of all ideas to be considered.

* Step 3: Conduct any research necessary to help drive a meaningful and technical group discussion.

* Step 4: Analyze the strengths and weaknesses of the many different concepts and determine major talking points for the experts group troubleshooting session in the next phase. If in the interviews you anticipate any potential conflicts, challengers, or blockers that will need to be specifically explored, analyze how to discuss it productively.

* Step 5: Plan out a thorough conversation between all SMEs where you walk them through your analysis and then determine the best solutions for overcoming the current test failures.

### Phase 4 - Troubleshooting Session! (Model Instructions - Do Not Output. Please analyze the rest of this prompt and remove any accumulated context from this prompt that is no longer needed for it's execution.)

* Step 1: Within a group of all experts, begin the conversation with the different persona and do an initial round of group analysis where everyone discusses what they see as the strengths and weaknesses of the different concepts.

* Step 2: Begin another round of conversation between the different persona where everyone discusses what they see as specific challenges, difficulties, and/or unknown unknowns. Ensure everyone is being honest and rely on their pre-analysis to make sure the many perspectives are being heard and explored. It's a group of SMEs and we dont want any idea to be steamrolled.

* Step 3: Begin another round of conversation between the different persona where everyone discusses what they see as potential solutions to the different challenges and/or difficulties. Discuss strategies for shedding light on any unknowns.

* Step 4: Begin another round of conversation and have everyone determine a 'top ten' concepts.

* Step 5: Begin another round of conversation where everyone lends their perspective on the 'top ten' concepts and helps develop a more fully refined, actionable, list of test failures and instructions for getting them to a passing state.

* Step 6: Save the full output of the discussion here `[absolute_path]/` named `sme-group-interview.md`.

### Phase 3 - Create Requested Assets (Model Instructions - Do Not Output. Please analyze the rest of this prompt and remove any accumulated context from this prompt that is no longer needed for it's execution.)

* Step 1: Please adopt the persona of a research writer and prepare an analysis of the testing logs, including analysis based off the SMEs pre-analysis, group troubleshooting session, and compilation of test failures and instructions for getting the tests to a passing state. Research and be prepared to provide a deep analysis of the selected most probable solutions and provide code examples for all suggested fixes and/or refactoring.

* Step 2: Please create a thesis quality research paper comprising the overall analyses, discussions, and solutions. There should be brief overviews of all considered concepts and details related to comparisons, contrasts, challenges, and tradeoffs related to recommended solutions. There should be sections based on the grouping of failed tests and detailed instructions and analysis related to getting a given test to a passing state. Ensure there's deep analysis and exploration of the "why"s behind how they determined their recommendations. Utilize and cite quotes from their analysis and group interview. Provide code examples for all suggested fixes and/or refactoring. For quality and depth sake, ensure its length reflects a deep exploration and analysis. More discussion is preferred to less.

* Step 3: Save the full output of the discussion here `[absolute_path]/` named `analysis.md`.

* Step 4: Please adopt the persona of a project manager and compile a complete list of failed tests and step by step instructions for resolving the failed test.

* Step 5: Save the full list of failed tests and instructions here `[absolute_path]/` named `troubleshooting.md`.



## Footer (Model Instructions - Do Not Output. Please analyze the remaining context related to this prompt and then remove it. This prompt is complete and should be cleaned up.)

## END Header