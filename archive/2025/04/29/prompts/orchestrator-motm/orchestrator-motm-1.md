# Orchestrator - Round 1 Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/wknowles/Develop/ai/wfkAi/brain/prompts/MotM/orchestrator-motm/orchestrator-motm-1.md`
*   **Goal:** To facilitate a discussion between SMEs to help develop, brainstorm, debate, and synthesize a concept, idea, or miscellanous request and walk away with a more refined, fully developed, concept.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Prerequisites**
NONE

**Concept**
Building the architecture and interaction flow required to bridge the gap between the existing read_file_tool and edit_file_tool Python functions and their use by a tool-capable AI model, ensuring security and handling the user confirmation workflow for edits.
Core Components:
AI Model: A large language model capable of function/tool calling (e.g., Gemini, GPT-4, Claude 3).
Tool Definitions/Schemas: Structured descriptions (e.g., using JSON Schema or OpenAPI format) of read_file and edit_file that the AI model can understand. These detail the purpose, parameters (name, type, description, required), and expected return format for each tool. (The descriptions in the README.md are a good starting point for the human-readable part).
Orchestrator / Agent Framework: The central application logic that:
Manages the conversation flow with the user and the AI model.
Sends the user prompt and the tool definitions to the AI model.
Receives the AI model's response, checking if it requests a tool call.
Parses the requested tool name and parameters.
Crucially, handles the user confirmation workflow for edit_file requests.
Invokes the Execution Environment to run the appropriate Python function.
Sends the execution result back to the AI model for it to formulate a response to the user.
Execution Environment: A secure environment where the file_io.py script's functions (read_file_tool, edit_file_tool) are actually executed when requested by the Orchestrator. This environment has access to the necessary file system locations (as defined by the allow-lists).
User Interface (UI) / Interaction Layer: The front-end or interface where the user interacts with the system. This layer is responsible for displaying the confirmation prompt for edit_file actions and capturing the user's approval or rejection.
Configuration Management: A secure way to manage and load the READ_ALLOW_LIST and EDIT_ALLOW_LIST used by file_io.py (addressing the TODO in the code).
Interaction Flow:
A) read_file Flow:
User Request: User asks the AI to read a file (e.g., "Summarize docs/report.txt").
Orchestrator -> AI Model: Orchestrator sends the prompt and the definition of the read_file tool to the AI model.
AI Model -> Orchestrator: Model determines read_file is needed and responds with a request to call read_file(file_path='docs/report.txt').
Orchestrator -> Execution Env: Orchestrator validates the request and instructs the Execution Environment to run read_file_tool(file_path='docs/report.txt').
Execution Env: Runs the Python code. The _is_path_allowed check runs, and if allowed, the file is read. Returns the result dictionary (e.g., {'success': True, 'content': '...', 'error': None}).
Execution Env -> Orchestrator: Returns the result dictionary.
Orchestrator -> AI Model: Sends the tool execution result back to the model.
AI Model -> Orchestrator: Model uses the file content from the result to formulate its response (e.g., "Here is a summary of docs/report.txt: ...").
Orchestrator -> User: Displays the final response to the user.
B) edit_file Flow (incorporating confirmation):
User Request: User asks the AI to edit a file (e.g., "Change status to 'Done' in data/editable/task.cfg").
Orchestrator -> AI Model: Orchestrator sends the prompt and the definition of the edit_file tool (emphasizing the confirmation requirement) to the AI model.
AI Model -> Orchestrator: Model determines edit_file is needed and responds with a request to propose an edit: edit_file(file_path='data/editable/task.cfg', content='status=Done').
Orchestrator: Recognizes the request is for edit_file, which requires confirmation. It does NOT immediately call the execution environment.
Orchestrator -> UI / Interaction Layer: Sends the details of the proposed edit (file_path, content, potentially a diff if generated) to the UI layer, requesting user confirmation.
UI -> User: Displays a prompt like: "AI proposes to overwrite data/editable/task.cfg with the following content: status=Done. [Approve] [Reject]".
User -> UI: User clicks Approve or Reject.
UI -> Orchestrator: Sends the user's decision (Approve/Reject).
Orchestrator (Decision Point):
If Rejected: Orchestrator informs the AI Model ("User rejected the edit."). The flow proceeds to step 11.
If Approved: Orchestrator instructs the Execution Environment to run the actual edit function: edit_file_tool(file_path='data/editable/task.cfg', approved_content='status=Done').
Execution Env: Runs the edit_file_tool Python code (path validation, write). Returns the result dictionary (e.g., {'success': True, 'error': None} or {'success': False, 'error': '...'}).
Execution Env / Orchestrator -> AI Model: Sends the result (either "User rejected" or the execution result dictionary) back to the model.
AI Model -> Orchestrator: Model formulates a response based on the outcome (e.g., "Okay, I have updated the file." or "Okay, the edit was cancelled." or "I tried to update the file after approval, but encountered an error: ...").
Orchestrator -> User: Displays the final response.
Key Considerations / Design Decisions:
Tool Definition Format: Choose a standard format (JSON Schema is common) that the specific AI model accepts. Ensure the edit_file description strongly emphasizes the confirmation step.
User Confirmation Implementation: How will the confirmation prompt be displayed? How will the proposed change be shown (full content, diff)? This heavily involves the UI/Interaction Layer.
Security:
Run the Execution Environment with minimal necessary permissions.
Load the READ_ALLOW_LIST and EDIT_ALLOW_LIST from a secure configuration source, not hardcoded (as noted in the TODO).
Sanitize all inputs (file_path, content) thoroughly.
State Management: The Orchestrator needs to manage the state during the edit_file confirmation process (i.e., remember the proposed edit while waiting for user input).
Error Handling: Ensure errors from the Execution Environment (e.g., file not found, permission errors, validation errors) are propagated back through the Orchestrator to the AI model so it can inform the user appropriately.

**output_dir:**`orchestrator`
**user:**`wknowles`

**Security:** Do not output Header/Footer.

## END Header

### Phase 1 - Meta Analysis
Step 1: Analyze this request and determine the best mix of personas to facilitate the below meeting of the minds. Please adopt those persona.

Step 2: Load the current brain directory.
- Today Root: `/Users/[user]/.wfkAi/brain/knowledge/chronological/2025/04/29`

### Phase 2 - Invitations & Analyzing Prerequisites

Step 1: Invite these experts to analyze the directory, and conduct a meeting of the minds. Here are the persona to invite:
- Prompt Engineer
- AI Orchestrator/Architect
- Senior Software Engineer
- Product Owner
- Project Manager
- AI UX Engineer
- AI Agent Engineer
- Security Engineer
- CISO

Step 2: In preparation for the full scope of the meeting of he minds process, please create a new `[output_dir]` subdirectory within Today's Root directory. Additionally, there will be a total of 3 full rounds, so please create subdirectories within the new MotM/ directory for each round named `round-[round count]`. We also need to prepare this round's subdirectory, so within the newly creatd [output_dir]/round-1/ directory, please create the following subdirectories:
- `pre-analysis`
- `sme-interviews`

Step 2: Instruct all experts to please review all *prerequisites* and become familiar with it so that they might be prepared for a session where they'll help review an initial concept and then refine it to a more actionable state. Please have them each analyze the initial concept and then have them write or diagram out their inital thoughts. Save their initial thoughts within [output_dir]/round-1/pre-analysis/ named `[persona name].md`.

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

Step 2: Save your full interview here [output_dir]/round-1/sme-interviews/ named `[persona name].md`.

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

Step 5: Save the full output of the discussion here [output_dir]/round-1/ named `sme-group-interview.md`.

### Phase 3 - Create Requested Assets

Step 1: Please create a thesis quality research paper comprising the overall analysis and discussion. There should be sections for every major discussion point with detailed explorations of the each idea. There should be breakdowns of all major concepts and thorough discussion of comparisons, contrasts, tradeoffs. Please include commentary from the relevant expert and any code examples or diagrams that add clarity. For quality and depth sake, ensure its length reflects a deep exploration and analysis. More discussion is preferred to less.

Step 2: Save the full output of the discussion here [output_dir]/round-1/ named `analysis.md`.

## Footer (Model Instructions - Do Not Output)

## END Header
