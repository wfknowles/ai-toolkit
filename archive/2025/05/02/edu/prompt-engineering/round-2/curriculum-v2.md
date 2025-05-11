# Prompt Mastery Course Curriculum Outline

**Version:** 2.0 (Draft - Reflecting Hybrid Delivery)
**Date:** 2025-05-04
**Target Audience:** Software Engineers (~200)
**Primary Tool:** Cursor IDE
**Delivery Model:** Hybrid (Web Application for Unit 1, VSCode Extension in Cursor IDE for Units 2-5)

**Overall Goal:** To equip software engineers with the knowledge and skills to effectively leverage LLMs and prompt engineering techniques within their daily workflows using Cursor, progressing from foundational understanding to practical application and mastery of advanced concepts.

**Platform Note:** This course utilizes a hybrid delivery model. Unit 1 and supporting materials will be delivered via a dedicated web application. Units 2-5, focusing on practical application, will be delivered through an integrated VSCode Extension within the Cursor IDE. Accessibility (WCAG AA) and a seamless user experience between platforms are core requirements.

---

**Unit 1: Foundations: Understanding AI & Your Cursor Copilot (Delivered via Web App)**
*   **Goal:** Establish baseline understanding of AI/LLMs, prompting value prop, ethical considerations, and basic Cursor interaction concepts.
*   **Modules:**
    *   **1.1: The AI Advantage for Engineers:** What are LLMs? Why Prompting? Value Proposition (Productivity, Quality). Conceptual Intro to Cursor. (PO)
    *   **1.2: Anatomy of a Prompt:** Core components (Role, Instruction, Context, Format). Clarity & Specificity. (PE)
    *   **1.3: Conceptual Cursor Interaction:** Understanding Chat, Providing Context (selections, files), Interpreting Diffs (concepts illustrated via examples/videos). (AI UX, SSE)
    *   **1.4: Responsible AI Use:** Intro to Hallucinations, Bias, Data Privacy, and Ethical Considerations. (AIR, AI UX)
*   **Key Activities:** Analyze good/bad prompts; Conceptual exercises; Basic quiz.
*   **Cognitive Level (Bloom):** Remembering, Understanding.
*   **Assessment:** Online quizzes, analysis tasks (within web app).

**Unit 2: Core Prompt Craft: Techniques for Everyday Tasks (Delivered via Cursor Extension)**
*   **Goal:** Develop practical skills in core prompting techniques and iterative refinement for common SE tasks directly within the Cursor IDE.
*   **Modules:**
    *   **2.1: Zero-Shot vs. Few-Shot Prompting in Cursor:** When & how; Crafting effective examples for code tasks using inline edits (Cmd+K) and Chat (Cmd+L). (PE)
    *   **2.2: Context Engineering I:** Providing effective code context within Cursor; Using `@`-files, `@Symbol`, selections; Understanding Tokenization impact on context limits. (SSE, PE, AIR)
    *   **2.3: Output Formatting & Control:** Controlling basic output (Markdown, JSON), specifying code style via prompt instructions. (PE)
    *   **2.4: Iterative Refinement & Prompt Debugging I:** The Test-Analyze-Refine loop within Cursor; Introduction to systematic prompt debugging methodology; Troubleshooting common prompt failures (vague instructions, context issues). (PE, PR, SSE)
*   **Key Activities:** Scaffolded interactive exercises within Cursor (generate tests, docs, refactor simple functions); Debugging failing prompts in the IDE; Peer review of prompts (potentially via shared code snippets/comments).
*   **Cognitive Level (Bloom):** Applying.
*   **Assessment:** Successful completion of interactive exercises in Cursor; Peer feedback; Practical prompt debugging tasks. Rubrics defined for IDE-based tasks.

**Unit 3: Building Complexity: Reasoning & Workflows in Cursor (Delivered via Cursor Extension)**
*   **Goal:** Apply techniques for more complex reasoning, handle larger contexts using Cursor's features, build simple prompt chains, and evaluate AI outputs critically within the IDE.
*   **Modules:**
    *   **3.1: Chain-of-Thought (CoT) in Action:** Using "step-by-step" for debugging, code analysis, complex explanations within Cursor chat/edits. (PE, SSE)
    *   **3.2: Context Engineering II & RAG in Cursor:** Strategies for larger context (`@Codebase`); Prompting with documentation (`@Docs`) and codebase context (RAG pattern simulation). (AOA, AIR, PE)
    *   **3.3: Prompt Chaining I:** Designing simple multi-step workflows within Cursor chat; Passing state/context between prompts manually. Introduction to cost/latency/security considerations in chains. (AOA, PE)
    *   **3.4: Evaluating AI Outputs & Code Review:** Heuristics for AI code quality; Best practices for reviewing AI-generated code (logic, edge cases, security); Identifying potential issues. (SSE, AIR)
*   **Key Activities:** Debug complex code using CoT prompts in Cursor; Use `@Codebase`/`@Docs` to solve context-dependent tasks; Design 2-3 step prompt chains in chat; Review and critique AI-generated code within the IDE.
*   **Cognitive Level (Bloom):** Analyzing, Evaluating.
*   **Assessment:** Multi-step problem-solving exercises in Cursor; Code review tasks based on provided rubrics; Practical RAG-based exercises.

**Unit 4: Advanced Techniques & Agentic Concepts (Delivered via Cursor Extension)**
*   **Goal:** Introduce advanced prompting techniques, concepts of agentic AI, prompting for tool use, and robust evaluation strategies, all applied within the Cursor context.
*   **Modules:**
    *   **4.1: Advanced Prompting Toolbox:** Self-Consistency (improving reliability); Meta-Prompting (dynamic prompts); Conceptual overview of ToT/Reflexion applied to complex SE problems. (PE, AOA, AIR)
    *   **4.2: Agentic Concepts Primer:** Observe-Think-Act loops, Planning, Memory types (theory applied to structuring complex prompts for Cursor's AI). (AAE, AOA)
    *   **4.3: Prompting for Tool Use (Simulation):** Instructing AI to use simulated tools via prompts; Handling tool output/errors via prompt structure within Cursor chat/edits. (AAE, PE)
    *   **4.4: Evaluating Outputs II & Security:** Advanced evaluation techniques; Security checks for AI code; Prompt injection awareness and mitigation strategies within workflows. (AIR, SSE, PE, AOA)
*   **Key Activities:** Apply Self-Consistency to a reasoning task within Cursor; Design prompts simulating tool use; Analyze a complex prompt chain for failure points and security risks; Evaluate code for security issues.
*   **Cognitive Level (Bloom):** Evaluating, Creating (preparation).
*   **Assessment:** Analysis tasks; Design challenges for complex prompts/workflows; Security review exercises.

**Unit 5: Capstone Application & Continuous Learning (Delivered via Cursor Extension & Web)**
*   **Goal:** Synthesize and apply learned skills to an authentic SE project within Cursor, demonstrate mastery, and engage with ongoing learning resources.
*   **Modules:**
    *   **5.1: Capstone Project (IDE-Based):** Develop a solution for an authentic SE task (e.g., AI-assisted refactoring, workflow automation helper) using multiple prompting techniques within Cursor. (Individual or Pairs) (SSE, Prof Ed)
    *   **5.2: Showcase & Feedback (Web/IDE):** Present/demonstrate capstone project (potentially via screen sharing/recording); Provide/receive peer feedback using defined rubrics (potentially via web platform or shared docs). (PO, Ed UX)
    *   **5.3: Lifelong Learning & Community (Web):** Resources for staying current; Engaging with the internal Community of Practice via web platform/channels. (PR, PM)
*   **Key Activities:** Capstone project development within Cursor; Presentation/Demo; Contributing effective prompts/workflows to internal library.
*   **Cognitive Level (Bloom):** Creating, Synthesis.
*   **Assessment:** Capstone project evaluated via rubric (assessing prompt quality, output quality, process, application of techniques); Peer feedback score.

**Cross-Cutting Themes (Integrated Throughout):**
*   **Ethical Considerations & Responsible AI:** Bias, fairness, transparency, privacy.
*   **Security Awareness:** Prompt injection, evaluating generated code security.
*   **Critical Evaluation:** Continuously assessing the quality, correctness, and utility of AI outputs.
*   **Iterative Refinement & Prompt Debugging:** Emphasizing the systematic process of improving prompts.
*   **Cursor Integration:** Constant grounding of techniques within the primary tool.
*   **Cost/Latency Awareness:** Discussing implications of complex prompts/chains.
*   **Accessibility:** Ensuring course interactions meet WCAG AA standards.
*   **Differentiation:** Optional challenges/resources for varying skill levels.

**Supporting Elements (Course Infrastructure):**
*   Web Application Platform (for Unit 1, resources, community) (Ed UX)
*   VSCode Extension integrated with Cursor (for Units 2-5) (VSCode SE/PA, AIUXE)
*   Web-Extension API & State Management (AOA, VSCode PA/SE)
*   Authentic Assessment Strategy (Formative & Summative/PBL) (Prof Ed, PR)
*   Clear Feedback Mechanisms (IDE and Web) (AI UX, Ed UX)
*   Community of Practice Facilitation (Web/Channels) (PR, PM)
*   Content Maintenance Plan (PM, PO)
*   Success Metrics & Tracking (Kirkpatrick/LTEM based) (PM, PO, PR)

--- 