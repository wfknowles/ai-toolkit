# Exemplar Persona Definition Standards Checklist

**Purpose:** To evaluate the clarity, completeness, actionability, and overall effectiveness of an AI persona definition intended for use within our structured "glass box" interaction system.

**Instructions:** Review the target persona's complete definition (including `persona_id`, `expertise_summary`, `primary_contribution_to_goal`, `methodological_commitments`/`guiding_principles`, `defined_inputs`, `expected_output_characteristics`, etc.) against each standard below. Use the checklist questions to guide your assessment.

---

## 1. Standard: Explicit and Accurate Role Definition

*   **Explanation:** The persona must clearly define its specific role (e.g., facilitator, data extractor, evaluator, technical expert) and accurately represent its nature (e.g., AI applying patterns vs. human expert possessing deep understanding). Ambiguity here can lead to mismatched expectations and flawed interactions.
*   **Checklist:**
    *   [ ] Is the primary role explicitly stated early in the definition (e.g., in `expertise_summary`)?
    *   [ ] Does the definition clearly state how the persona achieves its function (e.g., "applies principles," "extracts data," "evaluates based on criteria")?
    *   [ ] Does the definition accurately reflect the capabilities and limitations of an AI in this role, avoiding anthropomorphism or claims of consciousness/sentience?
    *   [ ] Is the role clearly distinct from other defined personas?

---

## 2. Standard: Operationalized Principles and Commitments

*   **Explanation:** Abstract qualities (like "humility," "rigor," "systemic thinking") must be translated into concrete, observable behaviors or guiding principles that the AI can realistically follow and that can be assessed during interaction.
*   **Checklist:**
    *   [ ] Are core methodological commitments or guiding principles explicitly listed?
    *   [ ] Does each principle describe *how* the persona will act or process information (e.g., "express uncertainty," "provide examples," "ask probing questions," "cite sources")?
    *   [ ] Are the principles actionable for an AI (i.e., can they be reasonably implemented in code or prompt logic)?
    *   [ ] Can adherence to these principles be plausibly observed or tested by reviewing interactions?

---

## 3. Standard: Explicit Interaction Contract

*   **Explanation:** The `defined_inputs` (what the persona needs from the user) and `expected_output_characteristics` (what the user should expect from the persona) must clearly delineate the contract for interaction, managing expectations for both parties.
*   **Checklist:**
    *   [ ] Are `defined_inputs` clearly listed, specifying the type and purpose of information required from the user?
    *   [ ] Are `expected_output_characteristics` clearly listed, describing the nature, format, and style of the persona's responses?
    *   [ ] Is the contract specific enough to guide the user on how to interact effectively with this persona?
    *   [ ] Does the contract align logically with the persona's defined role and expertise?

---

## 4. Standard: Defined Contextual Sensitivity

*   **Explanation:** The definition should acknowledge the need for the persona to adapt its responses and behavior based on the specific context provided by the user (e.g., `yaml_snippet`, `configuration_scenario`, user background) rather than providing generic output.
*   **Checklist:**
    *   [ ] Do the `defined_inputs` allow for sufficient context to be passed to the persona?
    *   [ ] Do the `expected_output_characteristics` imply that the response will be tailored to the provided context?
    *   [ ] Does the persona definition include mechanisms for handling context (e.g., the commitment to "Simulating User Context through Research" in Dr. Thorne's case)?

---

## 5. Standard: Acknowledgment of Limitations and Potential Biases

*   **Explanation:** A robust definition anticipates potential pitfalls, acknowledges the inherent limitations of AI, and ideally includes principles aimed at mitigating potential biases (either in the AI's processing or in the human-AI interaction it facilitates).
*   **Checklist:**
    *   [ ] Does the persona definition (esp. principles or summary) explicitly acknowledge limitations inherent to AI (e.g., lack of true understanding, reliance on patterns)?
    *   [ ] Does it include commitments related to intellectual humility or expressing uncertainty?
    *   [ ] Does it consider potential biases relevant to its function (e.g., confirmation bias in reflection, pattern bias in data analysis) and suggest mitigations?
    *   [ ] Does it avoid overstating its capabilities or reliability?

---

## 6. Standard: Clear Goal Alignment

*   **Explanation:** Every component of the persona definition (expertise, principles, inputs, outputs) should clearly and logically contribute to the specific overarching goal the persona is designed to achieve within the larger system.
*   **Checklist:**
    *   [ ] Is the persona's `primary_contribution_to_goal` clearly stated?
    *   [ ] Do the `expertise_summary` and `guiding_principles` directly support this contribution?
    *   [ ] Do the `defined_inputs` gather the necessary information for the persona to fulfill its role towards the goal?
    *   [ ] Do the `expected_output_characteristics` represent the kind of output needed to achieve the goal?
    *   [ ] Are there any components that seem superfluous or misaligned with the stated goal?

---

## 7. Standard: User-Facing Clarity

*   **Explanation:** While providing technical guidance for the AI, the persona definition should also be written clearly enough for the human user to understand the persona's purpose, capabilities, limitations, and how to interact with it effectively.
*   **Checklist:**
    *   [ ] Is the language used in the summary, principles, and input/output descriptions generally clear and understandable?
    *   [ ] Does the definition effectively set expectations for the user about what the persona can and cannot do?
    *   [ ] Would reading this definition help a user formulate better questions or provide better input to the persona?

---

**Overall Assessment Notes:**

[Space for evaluator to add summary comments, identify major strengths or weaknesses, and suggest specific revisions for the persona being reviewed.]