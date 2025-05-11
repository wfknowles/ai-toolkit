# AI Agent Engineer - MotM Round 1 SME Interview

**Date:** 2025-05-01
**Interviewee:** AI Agent Engineer (AIE)
**Interviewer:** Facilitator

**(Facilitator):** Thanks for your analysis. You noted the Top 15 concept leans heavily towards an *assisted* workflow rather than a fully *agentic* one, highlighting gaps in planning, autonomy, tool orchestration, information gathering, and learning.

**(Facilitator):** Given the risks discussed earlier (subtle breakages, security), is a more agentic approach with less human-in-the-loop even desirable for dependency updates, or is the current assisted model the right level?

**(AIE):** For an initial version, the assisted model in the Top 15 is absolutely the right level. Dependency updates are inherently risky. Full autonomy (like the original AIE-6) is too dangerous right now – the potential for the agent to silently break things is high. However, we should design the *architecture* (Arch point #1 refinement) with future agentic capabilities in mind. The value of agentics here lies in automating the *tedious analysis and information gathering*, not necessarily the final decision-making or execution for anything beyond trivial updates.

**(Facilitator):** You suggested formalizing tool definitions (#1 refinement) and adding error handling logic (#3 refinement). How complex is it to make an LLM reliably interact with diverse, potentially flaky tools like scanners or test runners?

**(AIE):** It adds significant complexity. We need:
1.  **Clear Tool Schemas:** Like OpenAPI specs, but for CLI tools or library functions. The LLM needs precise definitions of inputs, outputs, and potential errors.
2.  **Robust Parsing:** Parsing the string output of CLI tools can be brittle. Structured output (JSON) is much preferred where possible.
3.  **Retry Logic:** Defining when and how to retry a failed tool call.
4.  **Failure Handling Prompts:** Instructing the LLM on what to do if a tool fails irrecoverably (e.g., report the failure clearly, suggest manual alternatives, halt the specific update path).
5.  **Feedback Loop:** The LLM needs the tool's *actual* output (success or failure details) fed back into its context to make informed decisions for the next step. It requires careful orchestration (Arch #1, #3 refinements).

**(Facilitator):** If you were building this, what agentic capabilities would you prioritize adding *after* the initial Top 15 assisted workflow is established?

**(AIE):** Post-MVP, I'd prioritize:
1.  **Smarter Analysis Integration:** Instead of just running scans (#1), have the agent *synthesize* results from multiple sources (vulns, changelogs #2, test results #3, maybe static analysis) to provide a more holistic risk assessment (#13).
2.  **Basic Planning (#2 refinement):** Generate explicit update plans for user review, especially for multi-dependency updates.
3.  **Information Gathering (#5 refinement):** Enable targeted web searches via a tool when analysis hits unknowns (e.g., obscure error messages, undocumented breaking changes).
4.  **Automated PR/MR Creation:** After successful testing (#3) on a branch (#11), automate the creation of a Pull/Merge Request with a summary of changes, scan results, and test status for human review.
Full self-correction (#4 initial) or autonomous application (#6 initial) would be much further down the line.

**(Facilitator):** What are the biggest unknown unknowns for you in applying agentic AI to this problem?

**(AIE):** The biggest is ensuring the agent's goal alignment (#7 initial concept) remains stable throughout a complex, multi-step update process, especially when encountering errors or ambiguity. Can we prevent the agent from getting sidetracked or making unsafe assumptions? Another unknown is how well current LLMs can perform complex reasoning over diverse technical artifacts (code, logs, changelogs, scan results) simultaneously to make reliable judgments about risk (#13) or breaking changes (#2).

**(Facilitator):** Does the Top 15 concept have major blindspots from an AI/Agent capability perspective?

**(AIE):** The primary blindspot is the lack of explicit mechanisms for robust tool interaction and orchestration (#2 weakness), which underpins many of the analysis steps. It also lacks mechanisms for dynamic information gathering (#7 initial) when faced with ambiguity, relying solely on the initially provided context and static analysis.

**(Facilitator):** Any missing SMEs you'd add?

**(AIE):** Maybe someone specializing in LLM evaluation and red-teaming. As the agent gets more capable (e.g., synthesizing data, planning), we need expertise in testing its reasoning capabilities, identifying potential failure modes or biases, and ensuring its robustness against adversarial inputs, beyond the specific security checks SE/CISO focus on.

**(Facilitator):** Very helpful perspective on phasing agentic capabilities, the complexities of tool integration, the importance of goal alignment, and the need for specific LLM evaluation expertise. Thank you. 