# Prompt Engineer - MotM Round 3 Pre-Analysis

**Date:** 2025-05-01
**Focus:** Initial Milestones, Phases, Steps for V1 CLI (Prompting Integration Perspective)

Based on the V1 definition from Round 2, integrating the AI/prompting components requires careful phasing relative to the core orchestration and tool adapters.

**Proposed Phases & Milestones (Prompting Focus):**

1.  **Phase 1: Foundation & Core Orchestration Setup**
    *   *Dependency:* Arch/SSE define CLI skeleton, basic config, state machine basics.
    *   **PE Milestone 1.1:** Define initial V1 prompt templates (Asset #1) structure and content (placeholders identified).
    *   **PE Milestone 1.2:** Define V1 persona (Asset #2) and output schemas (Asset #3).
2.  **Phase 2: Tool Adapter Implementation (Initial Ecosystem)**
    *   *Dependency:* Arch/SSE implement core adapters (Git, Test Runner, Vuln Scan, License Scan, *First* Pkg Manager).
    *   **PE Milestone 2.1:** Refine `prompt_template_scan_summary` based on *actual* parsed outputs from Vuln/License adapters.
    *   **PE Milestone 2.2:** Develop initial evaluation examples (Asset #4) for scan summary prompt.
3.  **Phase 3: AI Integration Layer Development**
    *   *Dependency:* Arch/AIE implement LLM Interaction Module, Context Builder, Output Parser.
    *   **PE Milestone 3.1:** Integrate `prompt_template_scan_summary` with the AI module; test basic end-to-end flow for the `scan` command's AI portion.
    *   **PE Milestone 3.2:** Develop initial `prompt_template_breaking_change` (conservative version).
    *   **PE Milestone 3.3:** Develop initial `prompt_template_test_failure`.
    *   **PE Milestone 3.4:** Develop initial `prompt_template_conflict_resolution`.
4.  **Phase 4: MVP Workflow Integration & Testing**
    *   *Dependency:* Core `update` workflow orchestration is functional (without AI analysis initially, per PA strategy).
    *   **PE Milestone 4.1:** Integrate breaking change, test failure, and conflict prompts into the `update` workflow.
    *   **PE Milestone 4.2:** Build out evaluation corpus (Asset #4) with examples covering different scenarios (conflicts, breaks, test fails).
    *   **PE Milestone 4.3:** Conduct initial prompt evaluation (Methodology #2) using the corpus and potentially SME review (SSE, UXE).
5.  **Phase 5: Tuning, Refinement & Documentation**
    *   *Dependency:* Initial feedback from internal testing / early users (PO Strategy #2).
    *   **PE Milestone 5.1:** Refine prompt templates based on evaluation results and user feedback (AIE Method #2).
    *   **PE Milestone 5.2:** Finalize prompt assets and contribute relevant sections to user documentation (SSE Asset #2) explaining AI features and limitations.

**Key Dependencies/Steps:**
*   Prompt development is highly dependent on the *actual data* coming from the Tool Adapters. We can draft templates early, but refinement requires seeing real parsed outputs.
*   The AI Interaction Module (AIE/Arch) needs to be built before prompts can be truly integrated and tested end-to-end.
*   Prompt evaluation needs a defined methodology (AIE Method #1) and representative test cases/corpus (PE Asset #4).
*   Refinement relies on establishing the feedback loop (PO/SSE Method #1). 