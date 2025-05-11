# AI Agent Engineer - MotM Round 3 Pre-Analysis

**Date:** 2025-05-01
**Focus:** Initial Milestones, Phases, Steps for V1 CLI (AI Module Implementation & Evaluation Perspective)

Phasing the implementation and evaluation of the V1 AI components, while keeping future agentic capabilities in view:

**Proposed Phases & Milestones (AI Integration Focus):**

1.  **Phase 1: AI Module Foundation & Contracts** (Aligns with Arch/PA Phase 1)
    *   *Dependency:* PA defines LLM API Contract (PA M0.4).
    *   **AIE Milestone 1.1:** Implement LLM API Client Library (Asset #1) handling auth, basic calls, errors.
    *   **AIE Milestone 1.2:** Implement initial Context Builder Module (Asset #2) structure.
    *   **AIE Milestone 1.3:** Implement initial Output Parser Module (Asset #3) structure (handling text initially).
    *   **AIE Milestone 1.4:** Define structure for Tool Schema Definitions (Input for AI) (Asset #4).
    *   **AIE Milestone 1.5:** Design initial Evaluation Dataset structure (Asset #5) and LLM Task Evaluation Methodology (Methodology #1).
2.  **Phase 2: Scan Summary AI Integration** (Aligns with Arch Phase 4.1, PE Phase 3.1)
    *   *Dependency:* Core `scan` workflow functional (Arch M3.1); Vuln/License adapters provide data; PE defines `prompt_template_scan_summary`.
    *   **AIE Milestone 2.1:** Context Builder populates context for scan summary prompt.
    *   **AIE Milestone 2.2:** Output Parser handles basic text summarization output.
    *   **AIE Milestone 2.3:** Basic `scan` AI summary integrated and testable.
    *   **AIE Milestone 2.4:** Implement initial Observability hooks (logging) for AI calls (Strategy #4).
3.  **Phase 3: Update Workflow AI Integration (Core Analysis)** (Aligns with Arch Phase 4.2, PE Phase 3.2-3.4)
    *   *Dependency:* Core `update` workflow functional (Arch M3.2); PE defines breaking change, test fail, conflict prompts & schemas.
    *   **AIE Milestone 3.1:** Context Builder populates context for breaking change, test failure, conflict prompts.
    *   **AIE Milestone 3.2:** Output Parser implements robust JSON parsing (with fallback) for breaking change schema (PE Asset #3).
    *   **AIE Milestone 3.3:** Integrate breaking change, test failure, conflict AI analysis into `update` workflow.
4.  **Phase 4: AI Evaluation & Tuning** (Aligns with PE Phase 4, AIE Method #1)
    *   *Dependency:* AI features integrated; Evaluation corpus (PE Asset #4) populated.
    *   **AIE Milestone 4.1:** Implement tooling/scripts to run evaluations against the dataset.
    *   **AIE Milestone 4.2:** Conduct first full evaluation run for integrated AI tasks.
    *   **AIE Milestone 4.3:** Analyze results, provide feedback to PE for prompt tuning (Methodology #2).
    *   **AIE Milestone 4.4:** Implement Token Usage Monitoring (Methodology #3).
5.  **Phase 5: Pre-Release AI Validation** (Aligns with Pilot phases)
    *   *Dependency:* Pilot program feedback (PO M5.3).
    *   **AIE Milestone 5.1:** Re-evaluate AI performance based on pilot feedback and any prompt updates.
    *   **AIE Milestone 5.2:** Ensure AI failure handling (Strategy #3) is robust based on real-world testing.
    *   **AIE Milestone 5.3:** Verify observability data (logs, metrics) is being captured correctly.

**Key Dependencies/Steps:**
*   Building the AI interaction modules (Client, Context Builder, Parser) is foundational (Phase 1) before specific prompts can be integrated.
*   Integration depends heavily on stable outputs from Tool Adapters and well-defined prompts/schemas from PE.
*   The evaluation methodology and dataset (Phase 1 definition, Phase 4 implementation) are critical for measuring and improving AI performance.
*   Designing interfaces with future agentic capabilities in mind (Strategy #5), particularly in the LLM Interaction Module and Output Parser (handling potential action requests), should happen in Phase 1, even if unused in V1.
*   Observability (Strategy #4) needs to be built in from the start of integration (Phase 2). 