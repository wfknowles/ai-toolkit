# Requirements: Generalized Meeting of the Minds Engine V1

This document outlines the specifications for a generalized system capable of orchestrating simulated expert consultations (Meeting of the Minds) based on user requests.

## 1. Vision & Goals

*   **Vision:** To create a flexible and automated system that can analyze a user request, assemble a relevant virtual team of experts, simulate a structured multi-stage consultation process, and generate relevant project artifacts (strategies, requirements, roadmaps).
*   **Goals:**
    *   Improve efficiency and consistency of collaborative analysis and planning.
    *   Leverage diverse simulated expertise for complex problems.
    *   Provide structured, actionable outputs.
    *   Create a reusable and adaptable process framework.

## 2. Core Components & Definitions

### 2.1. Request Analyzer

*   **Purpose:** To parse and understand the initial user request to guide subsequent process steps.
*   **Inputs:** User request text, potential context documents/links.
*   **Outputs:** Structured data containing:
    *   Identified keywords and core concepts.
    *   Inferred domains of expertise required (e.g., "Data Architecture", "UI/UX", "Project Management").
    *   Estimated scope/complexity level (e.g., High-Level Strategy, Detailed Implementation Plan).
    *   Suggested relevant workflow template.
*   **Requirements:** Must utilize NLP/LLM capabilities for analysis. Must map request content to predefined domain taxonomies. Must handle diverse input formats.
*   **Acceptance Criteria:** Correctly identifies key domains for test requests. Output structure is consistent. Suggests appropriate workflow templates.
*   **Guidelines:** Use robust NLP techniques. Allow for potential user refinement of analysis results.

### 2.2. Persona Library

*   **Purpose:** To store definitions of expert personas available for simulation.
*   **Format:** Structured data (e.g., directory of YAML/JSON files).
*   **Schema per Persona:** `persona_id`, `role_name`, `domains_of_expertise` (list), `simulated_interview_style` (e.g., "Concise", "Detailed", "Skeptical"), `potential_biases` (optional), `typical_questions` (optional).
*   **Requirements:** Must be easily queryable and maintainable. Must contain a diverse range of relevant technical and business roles.
*   **Acceptance Criteria:** Library can be loaded and searched. Contains a minimum set of core personas (e.g., PM, PO, SSE, Arch, MLE, PE).
*   **Guidelines:** Regularly update and expand the library. Ensure expertise definitions are clear.

### 2.3. Persona Selector

*   **Purpose:** To choose the most relevant set of personas for a given request.
*   **Inputs:** Output from Request Analyzer, Persona Library.
*   **Outputs:** A list of 5-7 selected `persona_id`s/definitions.
*   **Requirements:** Must implement an algorithm to match required domains (from Analyzer) to persona expertise. Must aim for a balanced team composition based on request scope.
*   **Acceptance Criteria:** Selects relevant personas for test requests. Consistently selects the specified number of personas (e.g., 5-7).
*   **Guidelines:** Allow configuration of team size. Consider algorithm variations (e.g., prioritizing core roles, ensuring diversity).

### 2.4. Workflow Engine

*   **Purpose:** To orchestrate the sequence of steps in a Meeting of the Minds session.
*   **Inputs:** Selected workflow template (defining stages and steps), selected personas, initial request context.
*   **Outputs:** Coordinated execution of simulation steps, passing context between them.
*   **Workflow Templates:** Define sequences of steps (e.g., `Analyze Request -> Select Personas -> Simulate Interviews (Stage 1) -> Synthesize (Stage 1) -> Generate Report (Stage 1) -> Simulate Interviews (Stage 2) ...`). Examples: "Strategy Definition", "Requirements Gathering", "Roadmap Planning", "Full Project Simulation".
*   **Requirements:** Must load and interpret workflow templates. Must manage state and context between steps. Must trigger other components (Simulator, Synthesizer, Generator).
*   **Acceptance Criteria:** Executes steps defined in a template in the correct order. Passes necessary data between steps.
*   **Guidelines:** Design for modularity and extensibility to easily add new steps or workflow templates.

### 2.5. Interview Simulator

*   **Purpose:** To generate simulated responses from selected personas based on context and questions.
*   **Inputs:** List of active personas, context documents (previous reports, requirements), stage-specific goals/questions (from Workflow Engine).
*   **Outputs:** Simulated interview transcripts or structured notes per persona.
*   **Requirements:** Must use LLM prompting that incorporates persona definitions (role, style, expertise) and provided context. Must generate responses relevant to the questions asked.
*   **Acceptance Criteria:** Generates coherent, in-character responses relevant to the context. Responses reflect persona's defined expertise.
*   **Guidelines:** Develop robust prompt templates. Allow configuration of response length/detail. Consider techniques to simulate disagreement or diverse viewpoints based on persona definitions.

### 2.6. Insight Synthesizer

*   **Purpose:** To analyze simulated interview outputs and produce summarized findings.
*   **Inputs:** Interview transcripts/notes from multiple personas.
*   **Outputs:** Structured summary including: Key themes, points of agreement, points of disagreement/conflict, potential risks/blindspots identified, actionable recommendations/decisions.
*   **Requirements:** Must use NLP/LLM for summarization and theme extraction. Must implement strategies for comparing/contrasting persona inputs. Must identify and flag conflicts.
*   **Acceptance Criteria:** Accurately summarizes key points from test interview data. Identifies areas of agreement and disagreement. Output format is consistent.
*   **Guidelines:** Develop specific synthesis strategies (e.g., how to weight opinions, how to resolve simple conflicts vs. escalate complex ones). Allow for potential human review/refinement of synthesis.

### 2.7. Output Generator

*   **Purpose:** To create formatted output documents based on synthesized insights.
*   **Inputs:** Output from Insight Synthesizer, relevant report templates (e.g., `requirements_template.md`, `roadmap_template.md`), context from previous steps.
*   **Outputs:** Formatted Markdown documents.
*   **Report Templates:** Define structure, sections, and placeholders for different output types.
*   **Requirements:** Must populate templates with synthesized data. Must adhere to Markdown formatting standards.
*   **Acceptance Criteria:** Generates well-formatted reports based on templates and test synthesis data. All template placeholders are filled appropriately.
*   **Guidelines:** Use a standard templating engine. Ensure templates are customizable.

## 3. General Requirements & Guidelines

*   **R1: Modularity:** Design components to be as independent as possible.
*   **R2: Configurability:** Allow configuration of key parameters (team size, LLM models used, workflow selection).
*   **R3: Extensibility:** Easily add new personas, workflow steps, report templates, synthesis strategies.
*   **R4: Transparency:** Log key decisions made by automated components (e.g., why personas were selected, how conflicts were synthesized).
*   **G1: Technology Stack:** Define core technologies (e.g., Python, specific LLM APIs, libraries for NLP/workflow).
*   **G2: Persona Library Management:** Define process for adding, updating, and validating personas.
*   **G3: Workflow Template Management:** Define format and process for creating/managing workflow templates.
*   **G4: Testing:** Develop strategies for testing individual components (unit tests) and the end-to-end workflow (integration tests using sample requests).
*   **G5: Evaluation:** Define metrics to evaluate the quality and usefulness of the generated outputs and the overall process efficiency. 