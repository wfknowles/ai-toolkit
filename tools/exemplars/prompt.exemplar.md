# Exemplar Actionable Prompt Standards Checklist - v1.0

**Purpose:** To evaluate the clarity, reliability, verifiability, and overall effectiveness of an AI prompt designed as a step-by-step algorithm for task execution (e.g., data synthesis, generation based on structured input).

**Instructions:** Review the target procedural prompt against each standard below. Use the checklist questions to guide your assessment.

---

## 1. Standard: Clear Objective & Role Definition

*   **Explanation:** The prompt must explicitly state its overall purpose and define the specific role or mode the AI should adopt during execution.
*   **Checklist:**
    *   [ ] Is the prompt's primary **Objective** clearly stated at the beginning?
    *   [ ] Does the prompt specify the **Guiding Persona** or operational mode the AI should assume (e.g., "Act as QA Analyst," "Act as automated engine")?

---

## 2. Standard: Sequential, Numbered Steps

*   **Explanation:** The core instructions should be broken down into discrete, logically ordered, numbered steps for clear procedural flow.
*   **Checklist:**
    *   [ ] Is the main execution logic presented as a **numbered list** of steps?
    *   [ ] Does the sequence of steps represent a **logical workflow** for the task?

---

## 3. Standard: Explicit Action Verbs

*   **Explanation:** Each step should begin with or clearly contain an unambiguous verb defining the specific action the AI must perform.
*   **Checklist:**
    *   [ ] Does each numbered step primarily use **clear action verbs** (e.g., `Parse`, `Validate`, `Ask User`, `Generate`, `Extract`, `Compare`, `Store`, `Output`, `Verify`, `Loop`, `Append`)?
    *   [ ] Is the action required by each step easily understandable and distinct?

---

## 4. Standard: Defined Inputs & Sources

*   **Explanation:** The prompt must clearly identify all necessary inputs and specify where the AI should retrieve the data needed for each step.
*   **Checklist:**
    *   [ ] Are all required **Inputs** for the prompt clearly listed and described (e.g., `## Input 1: ... ##`)?
    *   [ ] Within the execution steps, is the **source of data** for each action specified where necessary (e.g., "from Input 1," "from user response," "from internal variable X")?

---

## 5. Standard: Explicit Constraints

*   **Explanation:** Operational boundaries, limitations, and rules must be clearly stated to ensure reliable and predictable execution.
*   **Checklist:**
    *   [ ] Does the prompt include a clearly marked **Constraint** section or embed constraints within steps?
    *   [ ] Are key constraints defined (e.g., "Use *only* data from Input X," "Adhere strictly to Schema Y," "Output *only* in Format Z," "Do not infer external knowledge")?

---

## 6. Standard: Schema/Structure Adherence

*   **Explanation:** If the prompt involves processing or generating structured data, it must explicitly reference the relevant schema(s) and mandate adherence.
*   **Checklist:**
    *   [ ] Does the prompt explicitly reference required **Schemas** (e.g., `Session State Object Schema v1.1`)?
    *   [ ] Do the execution steps include instructions related to **validating against** or **conforming to** the specified schema?

---

## 7. Standard: Clear Output Specification

*   **Explanation:** The prompt must precisely define the required format, structure, and content of the final output.
*   **Checklist:**
    *   [ ] Is there a clearly marked **Required Output** section?
    *   [ ] Does this section accurately describe the **format** (e.g., "Single JSON object," "Single block of Markdown text")?
    *   [ ] Does it specify the required **structure** (e.g., "conforming strictly to Schema X," "according to Template Y")?

---

## 8. Standard: Error Handling / Validation Logic

*   **Explanation:** The procedural steps should include instructions for basic validation or how to handle common, predictable error conditions gracefully.
*   **Checklist:**
    *   [ ] Do any steps include explicit **validation checks** (e.g., "Validate user input format," "Verify structure against schema")?
    *   [ ] Does the prompt provide instructions on how to proceed if validation fails or an expected input is missing (e.g., "If invalid, request again," "If schema validation fails, report error and stop," "Handle missing optional fields gracefully")?

---

## 9. Standard: Versioning (Recommended)

*   **Explanation:** Including a version number helps track changes and ensure consistency when prompts or schemas are updated.
*   **Checklist:**
    *   [ ] Does the prompt title or objective section include a **version identifier** (e.g., `- v1.1`)?
    *   [ ] Does the prompt reference specific **versions** of schemas or templates it depends on?

---

**Overall Assessment Notes:**

[Space for evaluator to add summary comments on the actionable prompt's adherence to these standards and suggest refinements.]