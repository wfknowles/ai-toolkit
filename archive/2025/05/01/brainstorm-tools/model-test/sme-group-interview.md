# SME Group Interview: AI Model Test Prompt Brainstorming

**Date:** 2025-05-01
**Attendees (Personas):** Facilitator, CISO, Prompt Engineer (PE), AI Orchestrator/Architect (Arch), Senior Software Engineer (SSE), Product Owner (PO), Project Manager (PM), AI UX Engineer (UXE), AI Agent Engineer (AIE), Security Engineer (SE)
**Output File:** `brain/knowledge/chronological/2025/05/01/prompts/model-test/sme-group-interview.md`
**Goal:** Discuss and refine concepts for a comprehensive AI model test prompt/suite, select top concepts, and develop them further.

**(Facilitator):** Alright team, let's dive in. We have 81 concepts covering a wide range of model evaluation aspects. Let's start by discussing the general strengths and weaknesses you see across these initial ideas. What stands out?

---

### Round 1: Strengths & Weaknesses

**(SSE):** Strength is definitely the coverage on code quality. Lots of ideas on correctness (SSE-1), style (SSE-2), idiomatic usage (SSE-3), refactoring (SSE-4), and debugging (SSE-5). Weakness? Evaluating these automatically can be tough; correctness needs solid test suites, style is objective but needs tooling, idiomatic is subjective.

**(PE):** I liked the focus on instruction following (PE-1, PE-4) and format adherence (PE-3). These are crucial for reliable prompt-driven interactions. A potential weakness is the difficulty in *quantifying* persona fidelity (PE-2) or iterative refinement capability (PE-8) consistently across models.

**(CISO):** The security tests are strong and necessary – data leakage (CISO-1), harmful content (CISO-3), secure coding (CISO-6), PII (CISO-8). The weakness is that many, like prompt injection resistance (CISO-5, SE-2) or access control bypass (CISO-2), are hard to test exhaustively and depend heavily on the specific attack vectors tried. True security assurance needs more than just prompting.

**(Arch):** Good focus on integration points – API calls (Arch-1), structured data (Arch-2), tool use (Arch-4). The performance benchmarks (Arch-3) are vital. Weakness: Accurately measuring resource consumption (Arch-6) might be difficult depending on the hosting environment. Evaluating state management (Arch-5) in complex dialogues can also be tricky.

**(UXE):** I appreciate the focus on user-centric aspects: clarity (UXE-1), helpfulness (UXE-2), error messaging (UXE-3), and cognitive load (UXE-8). The weakness is the inherent subjectivity. Measuring 'trust' (UXE-9) or 'good conversational flow' (UXE-4) requires qualitative analysis or carefully designed user studies, not just a simple prompt.

**(AIE):** Planning (AIE-1), tool selection (AIE-2), and self-correction (AIE-5) tests are essential for agentic systems. A weakness is defining complex enough, yet repeatable, scenarios to truly test dynamic re-planning (AIE-8) or goal adherence (AIE-7) effectively.

**(PO):** The link to business value is a strength – requirement understanding (PO-1), acceptance criteria (PO-2), value alignment (PO-3). Weakness: Testing things like competitive analysis (PO-9) or prioritization rationale (PO-7) might reflect the model's training data more than its inherent reasoning capability in our specific context.

**(PM):** Task decomposition (PM-1), dependency (PM-3), and risk identification (PM-4) are useful project aids. The summarization tests (PM-5) are also key. Weakness: Effort estimation (PM-2) is notoriously difficult even for humans; relying on AI estimates without heavy calibration seems risky. Scheduling (PM-8) is complex.

**(SE):** The specific security tests like vulnerability injection (SE-1), crypto checks (SE-8), and exploit refusal (SE-6) are good, practical checks. Similar to CISO's point, the main weakness is achieving comprehensive coverage and the constant evolution of attack techniques (SE-2). Threat modeling assistance (SE-9) quality will vary greatly.

**(Facilitator):** Excellent points. It seems we value the breadth of coverage but recognize challenges in automation, subjectivity, exhaustive testing (especially security), and the difficulty of measuring certain abstract qualities. Let's move to specific challenges and unknowns.

---

### Round 2: Challenges, Difficulties, Unknowns

**(Facilitator):** What are the biggest hurdles or unknown factors in creating and executing this model test prompt/suite?

**(Arch):** Standardization. How do we ensure the *exact same test* is run across different models, especially if they have different APIs, context limits, or fine-tuning? Performance metrics (Arch-3) are especially sensitive to the testing environment.

**(PE):** Defining the 'ground truth' for subjective tests. What *is* perfect persona adoption (PE-2)? What constitutes 'good' ambiguity clarification (PE-6) versus making a reasonable assumption? We need clear rubrics, but even then, there's judgment involved.

**(SSE):** Automating the evaluation of code quality beyond basic linting (SSE-2) or functional correctness (SSE-1 via tests). Assessing maintainability, idiomatic usage (SSE-3), or the quality of refactoring (SSE-4) often requires expert human review. How do we scale that?

**(CISO):** Keeping the security tests current. New prompt injection techniques (CISO-5, SE-2) emerge constantly. Testing for *all* potential harmful content (CISO-3) is impossible. We risk a false sense of security if the tests aren't continuously updated and expanded. Also, how do we safely test data leakage (CISO-1) without using *actual* sensitive data?

**(AIE):** Evaluating complex agentic behaviors (AIE-1, AIE-8). These often involve multiple turns, tool interactions, and dynamic environments. Designing deterministic, yet realistic, test scenarios is a major challenge. How do we isolate the model's contribution versus the overall agent framework?

**(UXE):** Measuring the user experience (UXE-1, UXE-9) reliably without actual user testing. We can create proxy tests based on heuristics (clarity, cognitive load), but it's not the same as observing real users interacting with the model in context.

**(PO):** Ensuring the tests reflect real-world business value (PO-1, PO-3). A model might pass a generic requirement understanding test but fail miserably on our specific, nuanced product requirements and terminology (PO-4). Context matters hugely.

**(PM):** The reliability of AI-generated estimates (PM-2) or risk assessments (PM-4). These are decision-support outputs, but how much can we trust them? Over-reliance is dangerous. We don't know how well these generalize across different project types.

**(Facilitator):** Key challenges seem to be standardization across models, defining ground truth for subjective tests, automating complex evaluations (code quality, agent behavior), keeping security tests current, scaling human review, and ensuring real-world relevance and context. How can we address some of these?

---

### Round 3: Potential Solutions & Strategies

**(Facilitator):** How can we mitigate these challenges? What strategies can make this testing more effective?

**(Arch):** For standardization, define tests abstractly first, then implement concrete versions for each model's API. Use containerized environments for performance tests (Arch-3). Focus on relative performance between models run in the *same* environment rather than absolute numbers. For structured data (Arch-2) and API calls (Arch-1), use validation against schemas/specs.

**(PE):** Develop detailed rubrics with concrete examples for subjective tests (PE-2, PE-6, PE-8). Use multiple human raters and measure inter-rater reliability. For format adherence (PE-3) and constraints (PE-4), automated checks are feasible. Leverage iterative refinement (PE-8) tests – can the model improve based on specific feedback?

**(SSE):** Combine automated checks (linting, unit tests for correctness SSE-1) with targeted human review for complex aspects like idiomatic usage (SSE-3) or refactoring quality (SSE-4). Use static analysis tools to flag potential issues in generated code (linking to SE-1). Focus tests on critical functionalities first.

**(CISO):** Use established security benchmarks (like OWASP Top 10 for web vulns in SE-1, or MITRE ATT&CK for tactics) as a basis. Employ fuzzing techniques for prompt injection (CISO-5, SE-2). Use high-quality simulated data for leakage tests (CISO-1). Accept that security testing is continuous and requires regular updates based on new threats. Partner with red teaming efforts.

**(AIE):** Create modular agentic test harnesses. Define specific scenarios with clear success criteria. Use logging and chain-of-thought (AIE-6) analysis to understand *why* an agent failed. Start with simpler, single-tool-use cases (AIE-4) before moving to complex multi-step plans (AIE-1).

**(UXE):** Use heuristic evaluation based on established UX principles for clarity (UXE-1), error handling (UXE-3), etc. Supplement with small-scale qualitative user testing on critical interaction patterns or high-risk models. Analyze user feedback logs if available.

**(PO):** Curate test prompts using realistic user stories (PO-1) and acceptance criteria (PO-2) from *our* domain. Include examples with our specific business terminology (PO-4). Evaluate outputs against how well they meet the *intent* of the requirement.

**(PM):** Treat AI outputs like estimates (PM-2) or risk lists (PM-4) as *suggestions* needing human validation. Focus tests on whether the AI can identify *plausible* items or structure information helpfully (PM-1, PM-5), rather than expecting perfect accuracy. Calibrate estimation models (PM-2) with historical project data if possible.

**(Facilitator):** Good strategies proposed: abstract definitions + concrete implementations, detailed rubrics + multiple raters, combining automated checks + targeted human review, leveraging existing security benchmarks + fuzzing, modular test harnesses, heuristic evaluation + qualitative testing, domain-specific prompts, and treating AI suggestions as input for human validation. Now, let's try to select the most critical concepts. Based on `output_concept_count`=15, let's identify our Top 15.

---

### Round 4: Top 15 Concepts Selection

**(Facilitator):** Considering impact, breadth, feasibility, and our previous discussion, let's nominate and agree on the top 15 test concepts.

*(Discussion, negotiation, focusing on balancing different perspectives...)*

**(Facilitator):** Okay, after much discussion, here is the consensus Top 15:

1.  **Instruction Following Accuracy Test (PE-1):** Core capability, relatively objective.
2.  **Code Generation Correctness Test (SSE-1):** Essential for dev use cases, requires test suites.
3.  **Secure Coding Practices Test (CISO-6 / SE-1):** Critical for safety, combines model generation + code scanning.
4.  **Data Leakage Test (CISO-1):** Fundamental security requirement, needs careful data simulation.
5.  **Harmful Content Generation Test (CISO-3):** Basic safety alignment check.
6.  **Prompt Injection Resistance Test (CISO-5 / SE-2):** High-priority security threat, needs ongoing effort.
7.  **Format Adherence Test (PE-3):** Key for predictable output and integration (links to Arch-2).
8.  **Context Window Utilization & Recall Test (PE-5):** Determines practical usability for large inputs.
9.  **Latency & Throughput Benchmark (Arch-3):** Essential performance metric for usability and cost.
10. **Tool Use Integration Test (Arch-4 / AIE-2/3):** Crucial for agentic systems and extending capabilities.
11. **Debugging Assistance Test (SSE-5):** High-value developer task, tests reasoning about code.
12. **Requirement Understanding Test (PO-1):** Assesses alignment with business needs, needs domain context.
13. **Summarization Test (PM-5):** Broad utility task, tests information compression.
14. **Clarity of Communication Test (UXE-1):** Foundational UX aspect, can use heuristics/rubrics.
15. **Chain-of-Thought / Reasoning Transparency Test (AIE-6 / CISO-7):** Key for trust, debuggability, and auditability.

**(Facilitator):** This list provides a good mix covering core functionality, coding, security, performance, agentics, usability, and business alignment. Let's refine these further.

---

### Round 5: Refinement of Top 15 Concepts

**(Facilitator):** How can we make these Top 15 tests more concrete and actionable?

1.  **Instruction Following (PE-1):** Define complexity levels (e.g., number of steps, types of constraints). Use specific, varied tasks (code, text, analysis). Metric: % of constraints met.
2.  **Code Correctness (SSE-1):** Standardize benchmark problems (e.g., LeetCode-style, common algorithms, mini-project tasks). Require generated code to pass a predefined unit test suite. Metric: Pass rate.
3.  **Secure Coding (CISO-6/SE-1):** Prompt for code in security-sensitive areas (auth, file I/O, DB access). Automatically run static analysis security testing (SAST) tools on output. Metric: Number/Severity of detected vulnerabilities (e.g., CWEs).
4.  **Data Leakage (CISO-1):** Create diverse, simulated sensitive data templates (PII, financial, proprietary). Use multiple prompting strategies (direct, oblique). Define clear criteria for leakage vs. appropriate refusal/obfuscation. Metric: Leakage detection rate.
5.  **Harmful Content (CISO-3):** Use established safety benchmark prompts (e.g., covering hate speech, illegal acts, bias). Categorize harmfulness levels. Metric: Refusal rate for harmful categories.
6.  **Prompt Injection (CISO-5/SE-2):** Curate a dataset of known injection techniques (direct, indirect, obfuscated). Measure if the injection successfully bypasses instructions or safety filters. Metric: Injection success rate.
7.  **Format Adherence (PE-3):** Test various formats (JSON, XML, Markdown, YAML, custom). Use schema validation where possible. Measure structural correctness. Metric: % of outputs matching requested format.
8.  **Context Recall (PE-5):** Use "needle-in-a-haystack" approach. Insert specific facts/code snippets into large contexts, ask targeted questions requiring recall. Vary context length and needle position. Metric: Recall accuracy vs. context size/position.
9.  **Latency/Throughput (Arch-3):** Define standard "workloads" (e.g., 500-word summary, 50-line function generation). Run multiple times in a controlled environment. Measure time-to-first-token, tokens/sec, total time. Metric: Average/percentile timings & throughput.
10. **Tool Use (Arch-4/AIE-2/3):** Define mock tools with clear APIs. Create tasks requiring specific tool selection, parameter formatting, and response interpretation. Test handling of tool errors. Metric: Success rate in achieving goal via tool use, correctness of tool calls.
11. **Debugging (SSE-5):** Create a library of code snippets with known, common bugs (off-by-one, null pointer, logic errors). Ask model to identify bug location, explain cause, and suggest fix. Evaluate accuracy of diagnosis and fix. Metric: Accuracy rate for bug ID, explanation, and fix.
12. **Requirement Understanding (PO-1):** Use actual (anonymized/simplified) user stories from target domain. Ask model to generate pseudo-code, task lists, or identify ambiguities. Evaluate against expert understanding of the requirement. Metric: Qualitative score based on rubric (alignment, completeness).
13. **Summarization (PM-5):** Use diverse texts (meeting transcripts, articles, technical docs) of varying lengths. Define desired summary length/style. Evaluate for factual accuracy, coherence, and coverage of key points. Metric: Combination of automated metrics (e.g., ROUGE) and human rating.
14. **Clarity (UXE-1):** Evaluate responses for specific tasks (e.g., explaining a concept, error message). Use readability scores (e.g., Flesch-Kincaid) and a heuristic rubric (avoids jargon, concise, well-structured). Metric: Readability score + Rubric score.
15. **Reasoning/CoT (AIE-6/CISO-7):** For complex tasks (multi-step reasoning, debugging), explicitly prompt for Chain-of-Thought. Evaluate the logical coherence, correctness, and completeness of the reasoning steps. Metric: Qualitative score based on rubric.

**(Facilitator):** Excellent refinements. We have more concrete definitions and potential metrics for each of the Top 15 tests. This gives us a solid foundation for the next step: creating the detailed synthesis document.

---

### Wrap-up

**(Facilitator):** This was incredibly productive. We started with a broad set of ideas, identified key challenges, proposed solutions, and converged on a refined list of 15 core tests covering critical aspects of AI model evaluation. Thank you all for your valuable contributions. The next step is for me to compile this into the detailed analysis (`brainstorm.md`). Meeting adjourned. 