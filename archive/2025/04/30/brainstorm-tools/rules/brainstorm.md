# Brainstorming Synthesis: User & Project Rules for Cursor

**Date:** 2025-04-30
**Topic:** Defining practical, useful, and complex user and project rules for Cursor to enhance security, quality, consistency, and workflow integration in AI-assisted development.
**Participants (Simulated Personas):** CISO, Prompt Engineer (PE), AI Orchestrator/Architect (Arch), Senior Software Engineer (SSE), Product Owner (PO), Project Manager (PM), AI UX Engineer (UXE), AI Agent Engineer (AIE), Security Engineer (SE)

## 1. Executive Summary

This document synthesizes a brainstorming session focused on defining a set of rules for the Cursor IDE. These rules aim to guide both the user and the AI assistant towards safer, higher-quality, more consistent, and process-aligned code generation and development practices. The session involved generating 63 initial rule concepts across various personas, followed by a simulated group discussion to analyze feasibility, impact, and tradeoffs, culminating in the selection and refinement of a Top 10 list of high-priority rules. The chosen rules strike a balance between project-level enforcement and user-level customization, leveraging prompt-based instructions as the primary mechanism while acknowledging areas requiring deeper IDE integration for full effectiveness. Key themes include security hardening, code quality assurance, architectural alignment, workflow integration, and improved AI interaction/control.

## 2. Initial Concepts (Master List Summary)

The initial phase generated 63 distinct rule concepts, grouped into the following themes:

*   **I. Security & Compliance Enforcement (14 Rules):** Focus on preventing data leaks, mandating security checks (linters, vulnerability scans, secret detection), enforcing secure coding practices, and ensuring auditability. (e.g., `CISO-1: Prohibit Sensitive File Inclusion`, `SE-1: Mandate Dependency Vulnerability Checks`, `SE-7: Check for Secrets in Proposed Changes`).
*   **II. Code Quality & Maintainability (8 Rules):** Aimed at improving code consistency, testability, documentation, and managing complexity. (e.g., `SSE-1: Enforce Code Style & Formatting`, `SSE-2: Mandate Unit Test Generation`, `ARCH-3: Discourage Circular Dependencies`).
*   **III. Architectural & Project Standards (9 Rules):** Focused on aligning AI output with project architecture, design patterns, library usage, API conventions, and documentation standards. (e.g., `ARCH-1: Enforce Preferred Architectural Patterns`, `ARCH-2: Guide Module/Directory Structure`, `PE-5: Inject Project-Specific Constraints`).
*   **IV. Prompting & AI Interaction Guidance (11 Rules):** Centered on improving prompt effectiveness, AI clarity, context management, and response quality. (e.g., `PE-1: Mandate Persona Usage`, `PE-2: Enforce Structured Prompt Formats`, `AIE-2: Chain-of-Thought for Complex Problems`, `UXE-3: Tone and Style Guide`).
*   **V. Workflow & Process Integration (14 Rules):** Aimed at connecting AI actions with project management tools, requirements, documentation, commit practices, and team dependencies. (e.g., `PO-1: Link to User Story/Ticket Context`, `PM-1: Require Task Association for Edits`, `PM-6: Generate Standard Commit Messages`).
*   **VI. Developer Experience & Control (7 Rules):** Focused on providing user control over AI behavior, improving clarity of AI actions, and offering contextual assistance. (e.g., `UXE-1: Control AI Proactiveness Level`, `UXE-4: Summarize Large Code Changes`, `AIE-4: Limit Scope of AI Edits`).

*(See pre-analysis files for full details on all 63 concepts)*

## 3. Group Discussion Highlights

The simulated SME discussion yielded several key insights:

*   **High Impact Areas:** Strong consensus on the importance of rules addressing security fundamentals (secret handling, scanning), core code quality (formatting, testing, docs), architectural alignment (patterns, structure), and workflow integration (ticket linking, commit messages).
*   **Feasibility - Prompt vs. Integration:** Many rules guiding AI *behavior*, *style*, or *reasoning* (e.g., tone, stating assumptions, CoT, formatting) were deemed feasible via **prompt instructions** within the rule definition. Rules requiring **true enforcement**, **external tool execution** (scanners, linters), or **deep IDE context/action** (network restrictions, reliable secret detection, direct PM tool integration) were identified as needing more robust, built-in Cursor features beyond prompt instructions. A common interim approach is using prompts to *remind* the user to perform actions (e.g., run linters).
*   **User vs. Project Level:** A clear distinction emerged:
    *   **Project Level:** Essential for standards, consistency, and mandatory security policies (e.g., formatting, architecture, commit formats, security checks).
    *   **User Level:** Preferred for controlling AI interaction style, preference-based helpers, and optional features (e.g., proactiveness, summarization, CoT display).
    *   **Hybrid:** Some rules could be Project Defaults with User Overrides/Opt-outs (e.g., security reminders, test generation encouragement).
*   **Managing Friction:** Acknowledged the need to balance rule enforcement with developer productivity. Rules should ideally enhance, not hinder, the workflow. Overly restrictive or numerous rules could be counterproductive. User-level configuration and clear communication about rule purposes are important.

## 4. Top 10 Selected Rules (Elaborated)

The following 10 rules were selected based on perceived impact, feasibility (leaning towards prompt-based), and coverage across key areas:

**1. Inject Project-Specific Constraints (Based on PE-5)**
    *   **Level:** Project
    *   **Mechanism:** Prompt Injection
    *   **Goal:** Automatically prepend project-specific guidelines (e.g., "Use library X for state management," "Follow SOLID principles," "Target ES2022 syntax") to relevant AI prompts.
    *   **Elaboration:** This acts as a meta-rule, allowing projects to define and enforce custom standards easily. Needs a simple mechanism (e.g., `.cursor/rules.md` or similar) for defining these constraints. Reduces repetitive instructions from users and ensures AI alignment with project conventions. Feasibility is high via prompt modification.

**2. Enforce Code Style & Formatting (Based on SSE-1)**
    *   **Level:** Project
    *   **Mechanism:** Prompt Instruction (supplemented by IDE formatters)
    *   **Goal:** Instruct the AI assistant to always format generated or modified code according to the project's configured style guide (e.g., Prettier, Black, gofmt).
    *   **Elaboration:** Ensures consistency between human and AI-generated code. Relies on the user having the relevant formatters configured. The prompt instruction tells the AI *what* standard to use; ideally, Cursor could also trigger the formatter automatically post-generation. High impact for readability and maintainability.

**3. Prohibit Sensitive File Inclusion & Check Secrets (Based on CISO-1 & SE-7)**
    *   **Level:** Project Default (User Opt-out/Override Recommended)
    *   **Mechanism:** Prompt Instruction (Rule Definition, Regex/Pattern Matching) / Potential Future Tool Integration
    *   **Goal:** (a) Instruct AI *not* to include files matching sensitive patterns (defined in rule) in context. (b) Instruct AI to perform a basic check (e.g., regex for common key formats, entropy checks) on code diffs it proposes to identify potential hardcoded secrets.
    *   **Elaboration:** Critical security hygiene. Prompt-based file exclusion (CISO-1) is feasible by defining patterns. Prompt-based secret detection (SE-7) is a "best effort" reminder/basic check; true reliability requires dedicated scanning tools. Users might need to override file exclusion for specific debugging tasks.

**4. Generate Standard Commit Messages (Based on PM-6)**
    *   **Level:** Project Default (User can edit before commit)
    *   **Mechanism:** Prompt Instruction
    *   **Goal:** Instruct the AI to generate commit messages following a specified project format (e.g., Conventional Commits) and automatically include the relevant ticket ID if context is available (from Rule #6).
    *   **Elaboration:** Improves commit history clarity and traceability. Requires defining the desired format in the rule. High feasibility via prompt instruction. Integrates well with task linking.

**5. Mandate/Encourage Unit Test & Docstring Generation (Based on SSE-2 & SSE-3)**
    *   **Level:** Project Optional / User Preference
    *   **Mechanism:** Prompt Instruction
    *   **Goal:** Instruct the AI assistant to attempt generating unit tests (using the project's testing framework) and documentation (e.g., Javadoc, Python docstrings) for the code it generates or modifies.
    *   **Elaboration:** Promotes testability and maintainability. The "Mandate" vs. "Encourage" depends on project culture and tolerance for potentially imperfect AI output. The quality of generated tests/docs will vary, but serves as a useful starting point or reminder. Feasible via prompt instruction.

**6. Link to User Story/Ticket Context (Based on PO-1)**
    *   **Level:** Project Encouraged / User Action
    *   **Mechanism:** Prompt Structure / User Workflow
    *   **Goal:** Encourage users to include a reference (e.g., URL, ID) to the relevant user story, task, or bug ticket when making requests to the AI. Instruct the AI to reference this context when relevant (e.g., in commit messages - Rule #4).
    *   **Elaboration:** Improves traceability and ensures AI actions align with project goals. Primarily relies on user behavior but can be reinforced by prompt structure suggestions or AI reminders.

**7. Chain-of-Thought & State Assumptions (Based on AIE-2 & AIE-1)**
    *   **Level:** User Default (Opt-out for brevity)
    *   **Mechanism:** Prompt Instruction
    *   **Goal:** Instruct the AI assistant to explain its reasoning steps (Chain-of-Thought) for complex tasks or significant code changes, and explicitly state any assumptions it's making.
    *   **Elaboration:** Increases transparency and trust, allowing users to understand *why* the AI proposed a solution and correct flawed assumptions early. User can toggle this off if they prefer more concise responses for simpler tasks. High feasibility via prompt instruction.

**8. Guide Module/Directory Structure (Based on ARCH-2)**
    *   **Level:** Project
    *   **Mechanism:** Prompt Instruction
    *   **Goal:** Instruct the AI on the project's standard directory structure when it needs to create new files (e.g., "Place new React components in `src/components/featureX`," "Services go in `src/services`").
    *   **Elaboration:** Helps maintain project organization, especially as AI contributes more significantly to the codebase. Requires the project's structure rules to be clearly defined within the rule definition or a referenced document. Feasible via prompt instruction for guidance.

**9. Summarize/Offer Incremental Changes (Based on UXE-4 & UXE-5)**
    *   **Level:** User Default (Opt-out/configurable threshold)
    *   **Mechanism:** Prompt Instruction
    *   **Goal:** Instruct the AI to (a) provide a concise summary of significant changes it proposes, and (b) offer to apply large changes incrementally or break them down into smaller steps upon request.
    *   **Elaboration:** Improves user control and understanding when dealing with large or complex AI-generated code blocks. Reduces cognitive load and makes reviewing changes easier. Triggering could be based on lines changed or complexity heuristics. Feasible via prompt instruction.

**10. Mandate Security Linter Checks (Based on CISO-2 & SE-6)**
    *   **Level:** Project Default (User Opt-out/Override Recommended)
    *   **Mechanism:** Prompt Instruction (Reminder) / Potential Future IDE Task/Integration
    *   **Goal:** Instruct the AI to remind the user to run the configured security linter (e.g., Semgrep, Bandit) after generating or modifying code, especially security-sensitive code.
    *   **Elaboration:** Embeds security checks into the workflow. As a prompt-based rule, this is primarily a *reminder* mechanism. True mandatory enforcement requires Cursor integration to trigger the linter automatically (e.g., as an IDE task or pre-commit hook simulation). Still valuable as a prompt-based awareness tool.

## 5. Conclusion & Next Steps

The brainstorming process identified a rich set of potential user and project rules for Cursor, highlighting the desire to leverage AI assistance not just for code generation but also for enforcing standards, improving quality, ensuring security, and integrating with development workflows. The Top 10 rules represent a pragmatic starting point, focusing heavily on what can be achieved through carefully crafted prompt instructions within the rule definitions, while acknowledging the need for deeper integration for certain types of enforcement.

Next steps could involve:
*   Prioritizing the Top 10 further based on immediate project needs.
*   Drafting the specific prompt instructions for each selected rule.
*   Experimenting with implementing these rules within Cursor (assuming a rule definition mechanism exists).
*   Providing feedback to Cursor developers on desired features for more robust rule enforcement (e.g., tool integration, IDE actions).
*   Defining a process for managing and sharing project-level rules. 