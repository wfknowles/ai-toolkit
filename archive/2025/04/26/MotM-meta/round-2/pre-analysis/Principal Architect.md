# Principal Architect - R2 Pre-Analysis

**Date:** 2025-04-26

**Prerequisites Reviewed:** R1 Group Consensus, R1 Analysis Summary.

**Goal:** Define assets, strategies, methodologies for the MVP, considering broader architectural implications.

**Initial Thoughts & Analysis:**

Reviewing the R1 MVP decision (fixed chain, JSON state, orchestrator replicating existing workflow) from a higher level:

1.  **Asset: Formalized MVP Workflow Definition:**
    *   **Strategy:** Explicitly document the sequence of steps in the fixed chain for the MVP.
    *   **Methodology:** Create a sequence diagram or flowchart mapping the discrete steps derived from the original `round-1`, `round-2`, `round-3` prompts. Identify inputs/outputs for each step, referencing the `state.json` schema and auxiliary files (agreeing with SSE/Arch on using file paths in JSON for large blobs). This provides a clear blueprint for the PE/AE to implement the Step Prompts and the Orchestrator logic.

2.  **Strategy: Scalability & Maintainability Considerations (Even for MVP):**
    *   **Methodology:** While the MVP chain is fixed, design the Orchestrator and Step Prompts with modularity in mind. Use clear naming conventions. Ensure prompts are well-documented (comments within the prompt explaining logic). Design the `state.json` schema anticipating potential future additions (even if not used in MVP). Avoid hardcoding values that might change; fetch from `state.json` where possible. This makes future refactoring (e.g., towards generalization) less painful.

3.  **Asset: Technical Design Document (Conceptual):**
    *   **Strategy:** Consolidate the key decisions and definitions into a single reference document.
    *   **Methodology:** Draft a document outlining:
        *   MVP Scope & Goals.
        *   Core Architecture (Orchestrator, Fixed Chain, JSON State).
        *   `state.json` Schema.
        *   Auxiliary File Strategy (paths in JSON, separate files).
        *   Step Prompt Interface Contract (Input/Output JSON format).
        *   MVP Fixed Workflow Sequence (diagram/list).
        *   Error Handling Strategy (Halt & Report).
        *   Testing Strategy.
        *   Known Limitations & Risks.

4.  **Methodology: Technology Choices (Implicit):**
    *   **Strategy:** Acknowledge the constraints and dependencies.
    *   **Methodology:** We are locked into: Cursor AI environment, available LLM, specific tools (`edit_file`, `read_file`). The architecture must function within these boundaries. The primary implementation "language" is prompt engineering.

5.  **Strategy: Future-Proofing (Minimal Viable):**
    *   **Methodology:** The main way to future-proof the MVP slightly is through clean design: modular prompts, clear state schema, avoiding hardcoding. Explicitly note areas where future generalization (post-MVP) would require significant changes (e.g., Orchestrator logic moving from fixed sequence to dynamic selection).

**Key Task:** Ensure the MVP design, while simple and fixed, is documented clearly and built with enough internal structure (modular prompts, defined interfaces) to serve as a stable foundation for potential future enhancements, rather than becoming an immediate dead-end due to poor internal design. 