# Agentic Framework PoC - Peer Review Group Interview (Round 1)

**Attendees:**
*   Facilitator (Lead Architect Persona)
*   Prompt Engineer (PE)
*   AI Orchestrator/Architect (OArch) - Reviewer Role
*   Senior Software Engineer (SWE)
*   Product Owner (PO)
*   AI UX Engineer (UXE)
*   AI Agent Engineer (AE)
*   Security Engineer (SE)
*   Senior QA (QA)

**Date:** 2025-04-29

**(Facilitator):** Alright team, thanks for reviewing the Agentic Framework PoC. We've all submitted our pre-analysis notes. The goal today is to discuss our findings, identify key strengths, weaknesses, risks, and agree on recommendations for the next iteration.

---

**Part 1: Strengths & Weaknesses**

**(Facilitator):** Let's start high-level. What's working well, what are the biggest weaknesses right now?

**(OArch):** Strength is definitely the architecture. Separating Orchestrator and Execution Environment is the right move for security and scalability. Using Redis for state and having the Connection Manager addresses core async needs.

**(SWE):** Agreed. The codebase is generally clean for a PoC, uses FastAPI well, and the Docker setup makes it easy to run. The common library is good practice.

**(PO):** Strength is that it meets the basic requirement: an agent that can use `read_file` and `edit_file` with a confirmation safeguard. It proves the concept.

**(Facilitator):** Good points. Weaknesses?

**(PE):** Biggest weakness is the mock LLM. It hides all the real challenges of prompt engineering, tool schema design for LLM consumption, and handling unpredictable LLM output. We can't really validate the core agent loop properly yet.

**(AE):** Echoing that. The agent logic in `handle_prompt` is very linear. Real agents need more complex reasoning, possibly multi-step calls, which isn't here. Context window management is also just basic trimming.

**(SE):** From my perspective, the biggest weakness is the lack of robust sandboxing in the Execution Environment. The path allowlisting is a start, but it's insufficient, especially if we add riskier tools like shell execution. Prompt injection is also a major latent risk.

**(UXE):** The confirmation UX is a conceptual weakness. Relying on a separate REST call after a WebSocket prompt isn't ideal. We also lack UI indicators for what the agent is doing (e.g., pending tool calls).

**(QA):** The testing strategy is weak. Too much mocking at critical integration points (Orchestrator <-> Exec Env, Redis interaction). No automated E2E tests.

**(Facilitator):** Okay, common themes seem to be the limitations of the mock LLM, the need for better security/sandboxing, testing gaps, and UX refinements around the confirmation flow.

---

**Part 2: Challenges, Difficulties, Surprises**

**(Facilitator):** What specific challenges or difficulties do we foresee based on the current implementation?

**(AE):** Handling LLM flakiness. What happens when the LLM generates malformed JSON for arguments? Or hallucinates parameters? The current `handle_prompt` has basic error handling, but a real system might need retry logic or even ask the LLM to correct itself.

**(PE):** Crafting the meta-prompt will be challenging. It needs to instruct the LLM on tool usage, argument formatting, *when* to ask for confirmation, *how* to generate the confirmation reasoning, and how to interpret tool errors, all while staying within token limits and avoiding confusing the LLM.

**(SWE):** Managing state consistency, especially around confirmations. The `retrieve_pending_confirmation` uses `GETDEL` which is atomic, that's good. But ensuring the WebSocket push post-confirmation reliably reaches the client, especially if the client disconnects and reconnects, could be tricky without more sophisticated session management.

**(OArch):** Scaling Redis if the number of users or conversation history length grows significantly. Also, managing potential schema evolution for the data stored in Redis (the serialized Pydantic models) could become difficult.

**(SE):** The biggest surprise might be how easily prompt injection can bypass safeguards if not carefully considered at every step – from the initial prompt, to argument generation, to how arguments are used in the Execution Environment.

**(UXE):** The difficulty will be making the asynchronous nature of tool calls and confirmations feel seamless to the user. They need clear feedback on what the agent is doing and why it might be waiting.

**(Facilitator):** So, LLM unreliability, robust prompting, state/session management, schema evolution, prompt injection defense, and async UX are key challenges.

---

**Part 3: Concerns, Risks, Flaws & Unknowns**

**(Facilitator):** Let's focus on risks and potential flaws. What keeps you up at night?

**(SE):** Unsandboxed execution, number one. Adding `run_shell` in its current state would be a critical vulnerability. Number two is insecure argument handling – an LLM providing `../../../etc/passwd` as a `file_path` or injecting shell commands into `content` arguments that later get processed unsafely.

**(PO):** The risk that the confirmation fatigue sets in. If the user has to confirm too often, or doesn't understand *what* they're confirming (needs diff!), they might just click approve blindly, negating the safety benefit.

**(QA):** The risk of regressions due to the lack of integration and E2E tests. A change in the Exec Env API contract might break the Orchestrator, and we wouldn't catch it until runtime.

**(OArch):** The risk of the current global instances (`redis_client`, `ws_manager`) causing issues in more complex deployment scenarios (e.g., multiple workers). While FastAPI handles dependencies well, explicit management might be safer.

**(PE):** The risk that the chosen LLM just isn't good enough at reliable tool use or following the structured format we need, requiring significant prompt iteration or even a model change.

**(AE):** The risk that the simple single-turn agent loop proves insufficient for complex tasks, requiring a major redesign of the Orchestrator logic to support planning or multi-step execution.

**(Facilitator):** Key risks: security vulnerabilities (sandboxing, injection, args), confirmation fatigue/ineffectiveness, regressions due to test gaps, LLM suitability/reliability, and architectural limitations for complex tasks. How do we shed light on unknowns?

**(QA):** More testing. Integration tests will expose issues between services. E2E tests will validate the user flow. Exploratory testing with a real LLM is needed.

**(SE):** Penetration testing, specifically targeting prompt injection and argument manipulation once a real LLM is integrated.

**(PO):** User testing with a prototype UI to get feedback on the confirmation flow and overall usability.

---

**Part 4: Agreed Feedback & Recommendations**

**(Facilitator):** Okay, let's synthesize this into concrete recommendations for the next steps.

**(All - General Agreement after Discussion):**

1.  **LLM Integration (Highest Priority):**
    *   Replace `llm_client.py` mock with a real LLM client (e.g., OpenAI). Securely manage API keys via configuration.
    *   Develop v1 Meta-Prompt: Define tool usage protocol, response formats (esp. confirmation reasoning), error handling, and security constraints.
    *   Implement robust argument validation and JSON parsing in `handle_prompt`.
    *   Ensure `send_result_to_ai_model` sends structured `ToolError` data.

2.  **Security Hardening:**
    *   **ABSOLUTELY NO `run_shell` tool** until robust sandboxing (e.g., Firecracker, nsjail, dedicated container execution) is designed and implemented.
    *   Thoroughly review and test `_is_path_allowed` for edge cases.
    *   Implement input sanitization/validation on tool arguments received from the LLM *before* they are used in Redis keys or passed to the Execution Environment.
    *   Implement AuthN/AuthZ: Define user sessions, authenticate WebSocket connections, authorize tool usage, and implement dynamic `allowed_paths_root` based on user context.

3.  **Confirmation Workflow & UX:**
    *   Implement Diff Generation: Execution Environment `/generate-diff` must return an actual diff for `edit_file`.
    *   Enhance Confirmation Request: The `WSConfirmationRequest` should include the generated diff (or summary).
    *   Prototype Client UI: Build a simple web client to visualize the flow, display confirmations (with diffs), and handle WebSocket messages.
    *   (Optional - Evaluate Later) Consider moving confirmation response (Approve/Reject) to WebSocket.

4.  **Testing Enhancements:**
    *   Implement Integration Tests: Test Orchestrator <-> Execution Environment HTTP API interactions.
    *   Implement Redis Integration Tests: Use `fakeredis-py` or test containers.
    *   Develop E2E Tests: Simulate client interaction via WebSocket.
    *   Expand edge case test coverage.

5.  **Architecture & Code Quality:**
    *   Split `Settings` in `common/config.py` into service-specific classes.
    *   Load `AVAILABLE_TOOLS` from an external configuration file.
    *   Integrate Linters/Formatters (e.g., Ruff/Black).
    *   Expand `ExecutionContext` model.
    *   Review state serialization in Redis for potential future issues.

**(Facilitator):** This looks like a solid set of recommendations covering our key discussion points. We have clear priorities around LLM integration, security, the confirmation UX, and testing. We'll use this to inform the next phase of development.

--- End Transcript --- 