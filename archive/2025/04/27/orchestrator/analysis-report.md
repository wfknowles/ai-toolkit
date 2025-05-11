# MotM Orchestrator Refactor: Analysis Report

## 1. Understanding of the Request

The goal is to refactor the MotM Orchestrator to:
- Remove hardcoded values (especially the initial concept) from `Orchestrator.prompt` and replace them with explicit inputs and interface contracts.
- Add an `output_dir` input to control where `requirements.md` and `roadmap.md` are created, passing this through the state and relevant steps.
- Create a new main interface prompt for passing these values to the orchestrator, using outputs and interface contracts.
- Ensure _aux_files are created in the orchestrator directory but are removed as a last step (after verifying final outputs).
- Insert a verification step for `requirements.md` and `roadmap.md` before cleanup.
- Create a new main MotM interface prompt in the prompt directory, with defined outputs for `output_dir` and `concept`.
- All work must conform to existing conventions, reflect the spirit of prior MotM rounds, and be production ready.

## 2. Model Considerations and Their Impact

- **Patterns & Conventions:** The orchestrator and step prompts use strict naming, directory, and interface conventions. State is managed via a JSON schema. Steps communicate via structured JSON outputs. Auxiliary files are organized in `_aux_files/round-X/`.
- **Origins:** The MotM process is rooted in iterative, multi-round SME analysis and synthesis, as seen in the V1 rounds and their outputs. The orchestrator is an MVP, but its structure is robust and should be preserved.
- **Reasoning:** The refactor is motivated by UX and safety: hardcoding is brittle, and the current workflow leaves artifacts and is not user-friendly for non-experts.
- **Production Readiness:** All changes must be precise, non-breaking, and maintain the orchestrator's reliability and traceability.

## 3. Potential Conflicts and Resolutions

- **State Schema Compatibility:** Adding `output_dir` must not break the schema; it should be added to `shared_data`.
- **Auxiliary File Cleanup:** Cleanup must only occur after successful verification of final outputs to avoid data loss.
- **Interface Contracts:** New prompts and steps must strictly follow the interface contract for step outputs.
- **Backward Compatibility:** The refactor should not disrupt the existing step logic or file structure.

## 4. Optimizations and Suggestions

- Add explicit validation for `output_dir` (existence, permissions) in the new interface prompt and orchestrator.
- Improve error messages and logging around file operations and state transitions.
- Modularize the orchestrator to make future step additions/removals easier.
- Document the new workflow and interface for future maintainers.

## 5. Determined Solution

- **New Main Interface Prompt:** In the MotM prompt directory, create a prompt that collects `output_dir` and `concept` as outputs, with clear instructions and validation.
- **Refactor Orchestrator.prompt:**
  - Accept `output_dir` and `concept` as inputs.
  - Remove hardcoded concept.
  - Pass `output_dir` through state and to relevant steps.
  - Update `STEP_ORDER` to add two new steps: verification and cleanup.
- **New Steps:**
  - `step-14-verify-outputs.prompt`: Verifies existence and content of `requirements.md` and `roadmap.md` in `output_dir`.
  - `step-15-cleanup.prompt`: Removes `_aux_files` after verification.
- **Documentation:** Update or create documentation for the new interface and workflow.

## 6. Step-by-Step Plan

**Phase 1: Analysis & Planning**
- [x] Analyze current orchestrator, state schema, and step contracts
- [x] Draft refactor plan (this report)

**Phase 2: Interface & Input Refactor**
- [ ] Create new main interface prompt in MotM prompt directory
- [ ] Refactor Orchestrator.prompt to accept inputs, update state, and remove hardcoding

**Phase 3: Workflow Extension**
- [ ] Create `step-14-verify-outputs.prompt` for output verification
- [ ] Create `step-15-cleanup.prompt` for auxiliary file cleanup
- [ ] Update orchestrator step order and logic

**Phase 4: Documentation & Testing**
- [ ] Update documentation for new workflow and interface
- [ ] Test the full workflow with various inputs and edge cases

**Phase 5: Output Delivery**
- [ ] Place all new/modified artifacts in Today's Orchestrator Directory for review

---

This plan ensures a safe, production-ready refactor that meets all requirements and preserves the MotM orchestrator's integrity and extensibility. 