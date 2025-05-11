# Senior Software Engineer - R3 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:** R2 Group Consensus, R2 Analysis Summary, MVP Requirements.

**Goal:** Define initial milestones, phases, steps for the technical implementation of MVP components.

**Initial Thoughts & Analysis:**

Breaking down the implementation work based on the R2 requirements from an engineering perspective:

**Phase 1: Setup & Core Utilities (Milestone: Dev Environment Ready)**
*   **Step 1.1:** Establish prompt file structure/organization in the repo.
*   **Step 1.2:** Create initial `state.json` example file based on schema.
*   **Step 1.3:** Develop/Document robust prompt instructions for common tasks:
    *   Reliably reading specific keys from input JSON (state).
    *   Reliably generating the full updated state JSON for overwrite.
    *   Reliably constructing auxiliary file paths.
    *   Reliably instructing `edit_file` to save/overwrite files.
    *   Reliably instructing `read_file`.
    *   Reliably formatting the output JSON block.
*   **Step 1.4:** "Unit test" these common instruction patterns manually in Cursor.

**Phase 2: Component Implementation (Milestone: Components Built)**
*   **Step 2.1 (Parallel):** Implement Orchestrator Prompt (Arch/AE focus).
*   **Step 2.2 (Parallel):** Implement individual Step Prompts (PE/SSE/AE focus), including auxiliary file handling logic where needed.
*   **Step 2.3 (Parallel):** Implement UX prompt templates (UXE/PE focus).
*   **Step 2.4:** Perform manual "unit tests" on each prompt as developed.

**Phase 3: Integration & Debugging (Milestone: E2E Flow Working)**
*   **Step 3.1:** Assemble the full chain by configuring the Orchestrator with the sequence of implemented Step Prompts.
*   **Step 3.2:** Run initial E2E tests.
*   **Step 3.3:** Debug failures – likely involving analysing `state.json`, auxiliary files, and refining prompt instructions in Orchestrator or Step Prompts iteratively.
*   **Step 3.4:** Implement and test checkpoint logic integration.
*   **Step 3.5:** Implement and test error handling integration.

**Phase 4: Testing & Refinement (Milestone: MVP Stable)**
*   **Step 4.1:** Execute comprehensive E2E test cases covering success paths, error paths, and checkpoint interactions.
*   **Step 4.2:** Validate final outputs against acceptance criteria.
*   **Step 4.3:** Refine prompts for robustness, clarity, and potentially performance (if latency is an issue).
*   **Step 4.4:** Perform prompt reviews (code reviews).

**Potential Blindspots/Anti-Patterns:**
*   **"Prompt Hacking":** Using overly clever tricks in prompts that work inconsistently or are hard to understand/maintain.
*   **Ignoring Edge Cases:** Failing to consider how prompts handle empty inputs, unexpected data types in state, or tool errors during testing.
*   **Poor Debugging Trail:** Not ensuring `state.json` and auxiliary files provide enough info to trace failures.
*   **Scalability of Prompts:** Writing prompts that are so long (due to logic, examples, injected state) that they hit context limits or become unreliable.

**Key Consideration:** The debugging phase (3.3) is likely to be the most time-consuming and unpredictable, requiring significant patience and iterative refinement of potentially complex prompt interactions. 