# AI Agent Engineer - R3 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:** R2 Group Consensus, R2 Analysis Summary, MVP Requirements.

**Goal:** Define initial milestones, phases, steps for implementing the pseudo-agent system (Orchestrator & Step Prompts).

**Initial Thoughts & Analysis:**

Structuring the implementation of the agentic components defined in R2.

**Phase 1: Foundation & Standards (Milestone: Core Agent Infrastructure Defined)**
*   **Step 1.1:** Implement and commit `step-prompt-template.md`.
*   **Step 1.2:** Implement and commit `state.schema.json`.
*   **Step 1.3:** Implement and commit initial `INTERFACE_CONTRACT.md` (defining I/O for all steps in `MVP_WORKFLOW.md`).
*   **Step 1.4:** Define detailed prompt instructions for the Orchestrator's JSON parsing/validation logic.
*   **Step 1.5:** Define detailed prompt instructions for Step Prompts regarding auxiliary file path construction and inclusion in output JSON.

**Phase 2: Orchestrator Implementation & Test (Milestone: Orchestrator Logic Complete)**
*   **Step 2.1:** Implement Orchestrator prompt: core loop, state read/write, fixed step sequencing.
*   **Step 2.2:** Implement Orchestrator prompt: Step Prompt input injection.
*   **Step 2.3:** Implement Orchestrator prompt: Response JSON parsing and validation logic.
*   **Step 2.4:** Implement Orchestrator prompt: State update logic (including auxiliary file paths).
*   **Step 2.5:** Implement Orchestrator prompt: Error handling logic (halt & set error state).
*   **Step 2.6:** Test Orchestrator logic using dummy Step Prompts that return predictable success/error JSON responses.

**Phase 3: Step Prompt Implementation & Test (Milestone: Step Prompts Functioning Individually)**
*   **Step 3.1:** Implement Step Prompt S1 based on template, contract, and refactored logic.
*   **Step 3.2:** Ensure S1 correctly handles inputs, auxiliary files (if any), and produces valid output JSON.
*   **Step 3.3:** Manually unit test S1.
*   **Step 3.4...n:** Repeat for all Step Prompts S2...Sn in the MVP workflow.

**Phase 4: Integration & System Test (Milestone: Full Agent System Integrated & Tested)**
*   **Step 4.1:** Configure Orchestrator to invoke the real implemented Step Prompts.
*   **Step 4.2:** Execute E2E tests focusing on the agent interactions: data passing via state/aux files, correct sequencing, response parsing, state updates.
*   **Step 4.3:** Debug issues arising from LLM inconsistencies in prompt adherence (output format, tool usage).
*   **Step 4.4:** Refine Orchestrator parsing/validation or Step Prompt output instructions as needed.

**Potential Blindspots/Anti-Patterns:**
*   **Implicit Dependencies:** Step Prompts accidentally relying on state left by previous steps but not explicitly defined in the interface contract.
*   **Non-Standard Output:** Step Prompts failing to return the exact JSON structure, breaking Orchestrator parsing.
*   **Context Window Issues:** The Orchestrator prompt + injected state + Step Prompt instructions exceeding context limits, causing unpredictable failures.
*   **Tool Call Failures:** Not adequately instructing prompts on how to report errors if an underlying `edit_file` or `read_file` call fails.

**Key Consideration:** Rigorous adherence to the defined Interface Contract and standardized prompt template is paramount for the pseudo-agent system to function. Debugging will likely involve examining the exact prompts sent to the LLM and the raw responses received. 