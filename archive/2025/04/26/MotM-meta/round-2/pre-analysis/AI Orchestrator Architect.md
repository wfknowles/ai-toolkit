# AI Orchestrator/Architect - R2 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:** R1 Group Consensus, R1 Analysis Summary.

**Goal:** Define assets, strategies, methodologies for the MVP (Fixed chain, JSON state, Orchestrator).

**Initial Thoughts & Analysis:**

Focusing on the architecture and orchestration elements decided in R1:

1.  **Asset: Orchestration Logic Definition:**
    *   **Strategy:** Implement the core control loop within the Orchestrator Meta-Prompt.
    *   **Methodology:** Define the exact sequence of steps for the fixed chain (mapping the original MotM MVP workflow). Define the state transitions: Read state -> Identify step -> Prepare input -> Invoke step -> Process output -> Write state. Specify the exact validation checks on the step prompt's response JSON (presence/value of `status` key, basic structure of `output_data`). Detail the error handling path (update status to `error`, log message, halt).
    *   **Workflow:** This defines the backbone of the execution flow.

2.  **Asset: State Management (`state.json`) Implementation Detail:**
    *   **Strategy:** Formalize the JSON schema.
    *   **Methodology:** Provide a concrete `state.schema.json` (or equivalent documentation). Specify how large data (like simulated interview transcripts) should be handled – store directly in the JSON? Store in separate files referenced by the JSON? *Recommendation: Store large text blobs in separate files (e.g., `step-N-output.md`) and put only the *path* to that file in `state.json` to keep the state file itself manageable and reduce parsing/update complexity.* This requires step prompts to know how to read/write these auxiliary files.
    *   **Workflow:** Ensures consistent data handling.

3.  **Asset: Step Interface Definition:**
    *   **Strategy:** Define the contract between the Orchestrator and Step Prompts.
    *   **Methodology:** Document the standard input structure the Orchestrator will provide (e.g., relevant parts of `state.json`) and the standard output structure Step Prompts *must* return (the JSON block with `status` and `output_data`). Provide examples.
    *   **Workflow:** Critical for modularity and ensuring components integrate correctly.

4.  **Methodology: Testing Strategy:**
    *   **Strategy:** Define how to test this fragile system.
    *   **Methodology:**
        *   *Unit Tests (Conceptual):* Test individual Step Prompts with sample inputs to see if they produce the correct output format.
        *   *Integration Tests (Conceptual):* Test the Orchestrator's ability to correctly sequence steps, pass data, and handle expected success/failure responses from mocked Step Prompts.
        *   *End-to-End Tests:* Run the full chain within Cursor AI, monitoring `state.json` and tool interactions.
    *   **Workflow:** Essential for verifying functionality and finding bugs.

**Refined Workflow (Architecture Focus):**

```mermaid
graph TD
    subgraph Orchestrator Control Loop
        direction LR
        O1(Read state.json) --> O2{Identify Next Step S_n};
        O2 --> O3(Load data D_n from state.json);
        O3 --> O4(Construct Prompt P_n for S_n with D_n);
        O4 --> O5(Invoke P_n);
        O5 --> O6{Parse/Validate Response R_n};
        O6 -- Success --> O7(Extract Output O_n);
        O7 --> O8(Update state.json with O_n, advance step);
        O8 --> O9(Write state.json);
        O9 --> O1;
        O6 -- Error/Invalid --> O10(Update state.json: status=error);
        O10 --> O11(Write state.json);
        O11 --> O12[Halt & Report Error];
    end

    subgraph Step Execution (Agent P_n)
        P_n --> T1(Tool: Read Aux Files if needed);
        T1 --> LLM(LLM Processing);
        LLM --> T2(Tool: Write Aux Files if needed);
        T2 --> R_n(Format JSON Response);
    end

    Start --> O1;
    O2 -- No More Steps --> End;
```

**Key Task:** Detailing the state schema, the exact sequence for the fixed chain, and the input/output contract for each step. 