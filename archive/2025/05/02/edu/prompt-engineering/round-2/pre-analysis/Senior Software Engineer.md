# Senior Software Engineer - Round 2 Pre-Analysis: Lesson Ideas

**Date:** 2025-05-02
**Persona:** Senior Software Engineer (SSE)

**Review:** The 5-unit structure makes sense, progressing from basics to complex workflows. Need to ensure every lesson has concrete code examples relevant to our daily work.

**Initial Lesson Ideas/Abstracts (Focus on SE Tasks & Code):**

*   **Unit 1: Foundations**
    *   *Lesson 1.3.1: Cursor for Code Explanation:* Abstract: Use Cursor chat to explain complex or unfamiliar code snippets. Practice prompts for different levels of detail.
    *   *Lesson 1.3.2: Cursor for Basic Code Generation:* Abstract: Generate boilerplate code, simple functions based on descriptions. Evaluate initial output.
*   **Unit 2: Core Prompt Craft**
    *   *Lesson 2.1.1: Few-Shot for Code Style:* Abstract: Use few-shot examples to guide Cursor in generating code matching team style guides.
    *   *Lesson 2.2.1: Providing Context for Debugging:* Abstract: Practice selecting minimal but sufficient code context (@-mentions, functions) when asking Cursor for debugging help.
    *   *Lesson 2.4.1: Debugging AI's Bad Code:* Abstract: Iterate on prompts when Cursor generates buggy or inefficient code. Techniques for asking for fixes.
*   **Unit 3: Building Complexity & Workflows**
    *   *Lesson 3.1.1: CoT for Root Cause Analysis:* Abstract: Use step-by-step prompting to trace complex bugs or understand intricate logic flows.
    *   *Lesson 3.3.1: Workflow: Feature > Tests > Docs:* Abstract: Chain prompts to generate a function, then unit tests for it, then basic documentation.
    *   *Lesson 3.4.1: Evaluating AI Refactoring:* Abstract: Critically review code refactored by AI. Check for correctness, maintainability, performance impacts.
*   **Unit 4: Advanced Techniques & Concepts**
    *   *Lesson 4.1.X: Advanced Code Gen (APIs/Schemas):* Abstract: Use meta-prompting or detailed prompts to generate more complex artifacts like API client boilerplate or DB schema suggestions.
    *   *Lesson 4.3.1: Prompting Linters/Formatters:* Abstract: (Simulated) Use prompts to invoke code quality tools and summarize their output.
    *   *Lesson 4.4.1: Security Review of AI Code:* Abstract: Heuristics and prompts for identifying potential security vulnerabilities (e.g., injection flaws, insecure defaults) in AI-generated code.
*   **Unit 5: Capstone**
    *   *Lesson 5.1.1: Capstone Project Options:* Abstract: Examples: AI-assisted refactoring of a tricky module; Building a workflow for generating integration tests; Automating documentation updates based on code changes.

**Diagram Idea:** Flowchart showing the prompt chain for the Feature->Tests->Docs workflow.

**Concerns:** Keeping examples relevant across different teams/tech stacks used by the 200 engineers. Ensuring the simulated environment/playground can handle realistic code complexity. Providing clear guidance on when *not* to trust AI code (security, complex logic). 