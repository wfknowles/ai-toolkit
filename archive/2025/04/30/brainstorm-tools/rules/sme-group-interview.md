# SME Group Interview: Brainstorming Cursor Rules

**Date:** 2025-04-30

**Attendees (Personas):** Facilitator, CISO, Prompt Engineer (PE), AI Orchestrator/Architect (Arch), Senior Software Engineer (SSE), Product Owner (PO), Project Manager (PM), AI UX Engineer (UXE), AI Agent Engineer (AIE), Security Engineer (SE)

**Output File:** `brain/knowledge/chronological/2025/04/30/brainstorm-tools/rules/sme-group-interview.md`

**Goal:** Brainstorm practical, useful, and potentially complex user and project rules for Cursor, discuss feasibility and tradeoffs, select top concepts, and refine them.

**(Facilitator):** Alright team, our final brainstorm session today focuses on defining valuable rules for Cursor itself, building on our experiences. The goal is practical, useful rules – user or project level – covering everything from security to code style to workflow. Let's start by identifying rules with potentially high impact.

--- 

### Round 1: High Impact Rules

**(Facilitator):** Looking at the 63 rule ideas, which ones jump out as offering the most significant benefits if implemented effectively?

**(CISO):** The security rules are paramount for enterprise adoption. **Prohibit Sensitive File Inclusion (CISO-1)** and **Check for Secrets in Changes (SE-7)** are basic hygiene to prevent catastrophic leaks. **Mandating Security Linter Integration (CISO-2)** and **Dependency Vulnerability Checks (SE-1)** embed security scanning directly in the workflow.

**(SSE):** I agree on the security basics. From a quality perspective, **Enforce Code Style & Formatting (SSE-1)** is huge for consistency between human and AI code. **Mandate Unit Test Generation (SSE-2)**, even if imperfect, shifts the culture towards testability. And **Require Docstrings (SSE-3)** makes AI code usable long-term.

**(Arch):** Maintaining architectural integrity is key. **Enforce Preferred Architectural Patterns (ARCH-1)** and **Promote Use of Platform Libraries/SDKs (ARCH-4)** prevent the AI from creating architectural chaos or reinventing wheels. **Guide Module/Directory Structure (ARCH-2)** keeps the project organized.

**(PM):** Traceability is vital. **Require Task Association for Edits (PM-1)** and **Generate Standard Commit Messages (PM-6)**, especially if linked to the PO's **Link to User Story/Ticket Context (PO-1)**, make AI contributions trackable and align them with project management.

**(PE):** Guiding the interaction is crucial for efficiency. **Inject Project-Specific Constraints (PE-5)** saves users from repeating instructions. **Enforce Structured Prompt Formats (PE-2)** ensures the AI gets needed context, and **Discourage Ambiguous Instructions (PE-4)** prevents wasted cycles.

**(AIE):** Making the AI more robust and explainable is high impact. **Chain-of-Thought for Complex Problems (AIE-2)** and **Explicitly State AI Assumptions (AIE-1)** build trust and allow intervention. **Contextual KB Querying (AIE-7)** makes the AI smarter about the specific project.

**(PO):** Aligning with requirements via **Prioritize Acceptance Criteria (PO-2)** and self-validation (**Validate Against Feature Requirements (PO-3)**) ensures the AI builds the *right* thing.

**(UXE):** Rules improving the interaction flow, like **Summarize Large Code Changes (UXE-4)** and **Offer Incremental Changes (UXE-5)**, are critical for user acceptance and control over powerful AI actions.

**(Facilitator):** Great points covering security fundamentals, code/arch quality, process integration, prompt effectiveness, AI reasoning, and user control. Now, let's talk about how feasible these are.

--- 

### Round 2: Feasibility & Implementation

**(Facilitator):** How could these rules actually be implemented in Cursor? What are the challenges?

**(SSE):** Many code quality rules – formatting (SSE-1), imports (SSE-6), maybe docstrings (SSE-3) – seem feasible via prompt instruction, telling the AI to adhere to standards or run formatters. Mandating test generation (SSE-2) is harder; the AI might generate poor tests, but reminding the user is easy.

**(Arch):** Enforcing architectural patterns (ARCH-1) or directory structure (ARCH-2) via prompts is possible but potentially brittle. The AI might misunderstand or ignore complex constraints. Injecting constraints (PE-5) seems more reliable for simple rules. Referencing diagrams (ARCH-7) relies on the AI's ability to read/interpret them.

**(SE):** Running external tools like linters (CISO-2, SE-6), vulnerability scanners (SE-1), or secret scanners (SE-7) directly via a rule seems challenging *unless* Cursor builds specific integrations or allows rules to execute shell commands (which has security implications itself, CISO-3). Instructing the AI to *remind* the user to run these tools is trivial via prompts, but not true enforcement.

**(CISO):** Agreed. True enforcement for things like **Prohibit Sensitive File Inclusion (CISO-1)** or **Network Restrictions (CISO-3)** likely needs built-in Cursor functionality beyond prompt instructions. Prompt-based PII filtering (PE-7) is possible but imperfect.

**(PE):** Prompt structure rules (PE-2), persona usage (PE-1), asking for clarification (PE-4), context selection (PE-6) – these are all very achievable through instructing the AI assistant within the rule definition. Prompt templates (PE-3) would likely require specific Cursor support.

**(AIE):** Rules guiding the AI's reasoning, like stating assumptions (AIE-1), Chain-of-Thought (AIE-2), requesting feedback (AIE-3), self-correction (AIE-5), are perfect candidates for prompt-based rules. Limiting edit scope (AIE-4) might need IDE-level integration for robust enforcement.

**(PM):** Task association (PM-1, PO-1) could work via prompts asking the user, but ideally, it integrates with the project management tool. Generating commit messages (PM-6) is easy via prompts. Complexity estimation (PM-2) is possible but likely very inaccurate.

**(UXE):** Most UX rules – proactiveness level (UXE-1), clarification style (UXE-2), tone (UXE-3), summarization (UXE-4), incremental changes (UXE-5), managing expectations (UXE-6) – are about instructing the AI's *behavior* and communication style, making them well-suited for prompt-based implementation.

**(Facilitator):** It seems many rules guiding AI behavior, code style, and prompting are feasible via prompt instructions within rules. However, rules requiring true enforcement, external tool execution, or deep IDE integration present challenges and might rely on future Cursor features. Let's discuss user vs. project level.

--- 

### Round 3: User vs. Project Level & Friction

**(Facilitator):** Which rules make sense as project-wide mandates versus individual user preferences? How do we avoid making the AI too restrictive?

**(PM):** Project standards like code formatting (SSE-1), commit messages (PM-6), directory structure (ARCH-2), API conventions (ARCH-5), required task association (PM-1), documentation standards (PM-3) should absolutely be **Project** level to ensure consistency.

**(Arch):** Agreed. Core architectural patterns (ARCH-1), use of platform libraries (ARCH-4), and handling of dependencies (ARCH-3, ARCH-6) must be **Project** level.

**(CISO):** Foundational security rules – sensitive file exclusion (CISO-1), linter integration (CISO-2), dependency checks (SE-1), blocking hardcoded secrets (CISO-5), secure library enforcement (SE-2), IaC validation (CISO-7) – need to be **Project** mandates.

**(SE):** Also Input validation patterns (SE-4), secure file handling (SE-5), insecure TLS (SE-3). Running the linter (SE-6) and checking for secrets (SE-7) should probably default to On at the project level, maybe user-configurable Off.

**(SSE):** Mandating test generation (SSE-2) or docstrings (SSE-3) could be **Project** level, but might cause friction if the AI struggles. Maybe start as User/Project optional and make them mandatory later? Complexity suggestions (SSE-4) and cross-referencing (SSE-7) feel more like **User** preferences.

**(PE):** Project constraints (PE-5) and prompt templates (PE-3) are inherently **Project**. Persona usage (PE-1) and structured prompts (PE-2) could be Project standards. Context selection (PE-6) and PII filtering (PE-7) could be Project defaults with **User** overrides.

**(AIE):** AI reasoning rules like stating assumptions (AIE-1), CoT (AIE-2), requesting feedback (AIE-3), self-correction (AIE-5) feel like generally good practices, potentially **User** configurable defaults. Tool usage strategy (AIE-6) might have Project-level security aspects (CISO-3) but also User preferences. Limiting edit scope (AIE-4) could be a Project safety default with User override.

**(UXE):** Interaction rules – proactiveness (UXE-1), clarification style (UXE-2), tone (UXE-3), summarization (UXE-4), incremental changes (UXE-5), managing expectations (UXE-6) – seem best as **User** preferences to match individual workflows. UI/Text consistency (UXE-7) would be **Project**.

**(PO):** Linking to tickets (PO-1) should be encouraged at the **Project** level. Prioritizing AC (PO-2), validating requirements (PO-3), suggesting doc updates (PO-4), feature flags (PO-7) align with project process, so likely **Project**. Discouraging scope creep (PO-6) is a helpful **User** nudge.

**(Facilitator):** Good breakdown. Clear consensus on project standards (formatting, architecture, security mandates) being Project level, while AI interaction style and helper features (summaries, complexity) lean towards User level. The key is providing value without excessive friction. Let's pick our Top 10.

--- 

### Round 4: Top 10 Selection (Cursor Rules)

**(Facilitator):** Let's select ~10 rules that offer a strong blend of impact (security, quality, consistency, productivity) and feasibility (leaning towards prompt-achievable initially).

*(Discussion, consensus building, and voting occurs...)*

**(Facilitator):** Okay, the group agrees on this Top 10:

1.  **Inject Project-Specific Constraints (PE-5):** (Project) Auto-apply project standards (style, libraries, patterns) to prompts.
2.  **Enforce Code Style & Formatting (SSE-1):** (Project) Instruct AI to use configured formatters/linters.
3.  **Prohibit Sensitive File Inclusion & Check Secrets (CISO-1 & SE-7):** (Project Default/User) Prevent context inclusion, check diffs for secrets (prompt-based best effort initially).
4.  **Generate Standard Commit Messages (PM-6):** (Project/User) Instruct AI to follow format and include ticket ID (from PO-1).
5.  **Mandate/Encourage Unit Test & Docstring Generation (SSE-2 & SSE-3):** (Project/User) Instruct AI to generate tests/docs or remind user.
6.  **Link to User Story/Ticket Context (PO-1):** (Project/User) Encourage/require prompts to link to work items.
7.  **Chain-of-Thought & State Assumptions (AIE-2 & AIE-1):** (User) Instruct AI to show reasoning for complex tasks and state assumptions.
8.  **Guide Module/Directory Structure (ARCH-2):** (Project) Instruct AI on project structure for new files.
9.  **Summarize/Offer Incremental Changes (UXE-4 & UXE-5):** (User) Instruct AI to summarize large changes and offer smaller steps.
10. **Mandate Security Linter Checks (CISO-2 & SE-6):** (Project) Instruct AI to run linters post-change or remind user (best effort via prompt).

**(Facilitator):** This list covers core project standards, security hygiene, AI reasoning transparency, workflow integration, and user control. Let's quickly refine them.

--- 

### Round 5: Refinement (Cursor Rules)

**(Facilitator):** Refinements for the Top 10 Rules:

1.  **Inject Project Constraints (PE-5):** Level=Project. Mechanism=Prompt Injection. Need easy way to define these constraints (e.g., in `.cursor/rules.md`).
2.  **Enforce Style/Format (SSE-1):** Level=Project. Mechanism=Prompt Instruction. Relies on configured formatters being available.
3.  **Sensitive Files/Secrets Check (CISO-1/SE-7):** Level=Project Default (User Opt-out?). Mechanism=Prompt for CISO-1 (file patterns), Prompt+Regex/Tool for SE-7 (feasibility depends on Cursor allowing checks). Emphasize best-effort nature via prompts.
4.  **Standard Commit Msgs (PM-6):** Level=Project Default (User Edit). Mechanism=Prompt Instruction. Requires extracting Ticket ID (from PO-1).
5.  **Test/Docstring Generation (SSE-2/SSE-3):** Level=Project Optional/User. Mechanism=Prompt Instruction. Quality will vary; focus on reminder/attempt.
6.  **Link Ticket Context (PO-1):** Level=Project Encouraged/User. Mechanism=Prompt Structure/User Action. AI instruction to reference if available.
7.  **CoT & State Assumptions (AIE-2/AIE-1):** Level=User Default (Opt-out?). Mechanism=Prompt Instruction. User can toggle for brevity.
8.  **Guide Directory Structure (ARCH-2):** Level=Project. Mechanism=Prompt Instruction. Needs clear definition of structure rules.
9.  **Summarize/Incremental Changes (UXE-4/UXE-5):** Level=User Default (Opt-out?). Mechanism=Prompt Instruction. Trigger based on change size/complexity.
10. **Security Linter Checks (CISO-2/SE-6):** Level=Project Default (User Opt-out?). Mechanism=Prompt Instruction (remind user) or IDE Task/Future Integration for auto-run.

**(Facilitator):** Clearer levels and mechanisms. Many rely heavily on good prompt instructions within the rule definition. Dependencies on external tools or deeper IDE integration noted where applicable.

--- 

### Wrap-up

**(Facilitator):** Excellent work. We've brainstormed a wide range of potential Cursor rules and narrowed it down to a practical Top 10 list focusing on achievable instructions that provide significant value across security, quality, process, and usability. The next step is the detailed analysis document. Any final thoughts?

*(No further comments)*

**(Facilitator):** Great, thank you all. Meeting adjourned. 