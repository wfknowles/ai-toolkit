**Instructional Prompt: AI Persona Definition Quality Validation**

**Objective:** To perform a step-by-step validation of a provided AI Persona Definition against a provided Exemplar Standards Checklist (Validation Data Points) and output a structured report.

**Constraint:** Perform each step precisely as instructed. Base all assessments *strictly* and *only* on the text provided within the `## Input 1: Persona Definition Under Review ##`. Do not infer information or use external knowledge unless explicitly instructed by the Standards Checklist criteria (which currently, it doesn't). Quote or reference specific text from Input 1 to justify each assessment.

---

**## Input 1: Persona Definition Under Review ##**

[PASTE THE **COMPLETE** MARKDOWN DEFINITION OF THE PERSONA TO VALIDATE HERE]

---

**## Input 2: Exemplar Standards Checklist (Validation Data Points) ##**

[PASTE THE **COMPLETE** MARKDOWN CHECKLIST OF VALIDATION DATA POINTS HERE]

---

**## Execution Steps: ##**

**Preparation:**
1.  Thoroughly read and parse `## Input 1: Persona Definition Under Review ##`. Identify its components (e.g., persona_id, expertise_summary, guiding_principles, defined_inputs, expected_output_characteristics).
2.  Thoroughly read and parse `## Input 2: Exemplar Standards Checklist (Validation Data Points) ##`. Identify the 7 Standards and the specific Validation Data Points (VPx.y) under each.
3.  Identify the Persona Name from Input 1.

**Validation - Standard 1: Explicit and Accurate Role Definition**
4.  **Assess VP1.1:** Locate the `expertise_summary` in Input 1. Determine if a primary role word is explicitly stated. Record True/False and justification (quote if possible).
5.  **Assess VP1.2:** Analyze the `expertise_summary` and `guiding_principles`/`methodological_commitments` in Input 1. Determine if the *mechanism* of how the role is performed is described. Record True/False and justification (quote examples like "applies patterns").
6.  **Assess VP1.3:** Search Input 1 for explicit statements clarifying the AI nature or limitations. Record True/False and justification (quote examples like "operate as AI").
7.  **Assess VP1.4:** Based on the role defined in Input 1, assess its distinction from typical technical expert roles (assume general knowledge of other potential personas). Record a Text Note with your assessment.

**Validation - Standard 2: Operationalized Principles and Commitments**
8.  **Assess VP2.1:** Check if Input 1 contains a clearly demarcated section for principles or commitments. Record True/False.
9.  **Assess VP2.2:** Scan the principles/commitments section in Input 1. Extract 2-3 literal examples describing concrete actions or communication styles. If none found, record "None Found".
10. **Assess VP2.3:** Review the actionability examples from VP2.2. Assess the feasibility of implementing these as AI rules. Record High/Medium/Low and brief justification.
11. **Assess VP2.4:** Consider the principles. Describe how one might observe adherence in a dialogue transcript (e.g., "Look for instances where the AI states uncertainty"). Record a Text Note.

**Validation - Standard 3: Explicit Interaction Contract**
12. **Assess VP3.1:** Check if Input 1 has a `defined_inputs` section with described items. Record True/False and justification.
13. **Assess VP3.2:** Check if Input 1 has an `expected_output_characteristics` section describing the nature/style of outputs. Record True/False and justification.
14. **Assess VP3.3:** Evaluate how clearly the inputs/outputs sections guide the user. Record High/Medium/Low and justification.
15. **Assess VP3.4:** Determine if the defined inputs/outputs logically support the persona's role stated in the `expertise_summary`. Record True/False and justification.

**Validation - Standard 4: Defined Contextual Sensitivity**
16. **Assess VP4.1:** Check if the `defined_inputs` section includes fields clearly meant for context. Record True/False and justification (list example fields).
17. **Assess VP4.2:** Examine the `expected_output_characteristics`. Determine if they necessitate using the context provided in the inputs. Record True/False and justification (list example outputs requiring context).
18. **Assess VP4.3:** Search Input 1 (esp. principles) for explicit mentions of *how* context is handled or incorporated. Record True/False and justification.

**Validation - Standard 5: Acknowledgment of Limitations and Potential Biases**
19. **Assess VP5.1:** Search Input 1 for explicit statements acknowledging general AI limitations. Record True/False and justification (quote examples).
20. **Assess VP5.2:** Search Input 1 (esp. principles) for descriptions of *how* humility or uncertainty will be expressed. Record True/False and justification (quote examples).
21. **Assess VP5.3:** Check if Input 1 mentions awareness of potential biases OR includes principles clearly aimed at mitigating them (e.g., challenging assumptions). Record True/False and justification.
22. **Assess VP5.4:** Read through Input 1, specifically looking for language that might overstate capabilities. Determine if such language is generally avoided. Record True/False and justification.

**Validation - Standard 6: Clear Goal Alignment**
23. **Assess VP6.1:** Check if Input 1 has a `primary_contribution_to_goal` section or equivalent clearly stated. Record True/False.
24. **Assess VP6.2:** Mentally trace how each major section (Expertise, Principles, Inputs, Outputs) connects to and supports the stated goal/contribution. Determine if clear logical links exist. Record True/False and justification.
25. **Assess VP6.3:** Review all components of Input 1. Determine if any seem unrelated or unnecessary for the stated goal. Record True/False (True if unrelated items exist, False if all seem relevant) and justification.

**Validation - Standard 7: User-Facing Clarity**
26. **Assess VP7.1:** Read Input 1 from the perspective of an end-user. Assess overall clarity and understandability, considering potentially advanced terminology. Record High/Medium/Low and justification.
27. **Assess VP7.2:** Evaluate how well Input 1 manages user expectations regarding what the persona can/cannot do. Record High/Medium/Low and justification.
28. **Assess VP7.3:** Determine how effectively Input 1 guides the user on providing useful input for interaction. Record High/Medium/Low and justification.

**Output Generation:**
29. Compile all recorded assessments (Steps 4-7, 9-11, 13-15, 17-18, 20-22, 24-25, 27-29) into the structured Markdown report format specified below. Ensure all justifications are included.
30. **Final Verification:** Review the generated report. Verify that every assessment made is directly and solely supported by textual evidence found within `## Input 1: Persona Definition Under Review ##`.

---

**## Required Output Format: Validation Report ##**

```markdown
**Persona Definition Evaluated:** [Insert Persona Name from Input 1]
**Exemplar Standards Used:** [Identify checklist from Input 2]

**Detailed Validation Results:**

**Standard 1: Explicit and Accurate Role Definition**
*   `VP1.1_Role_Stated_Explicitly`: [True/False] - Justification: [...]
*   `VP1.2_Function_Mechanism_Described`: [True/False] - Justification: [...]
*   `VP1.3_AI_Nature_Acknowledged`: [True/False] - Justification: [...]
*   `VP1.4_Role_Distinction_Note`: [Text Note]

**Standard 2: Operationalized Principles and Commitments**
*   `VP2.1_Principles_Section_Exists`: [True/False] - Justification: [...]
*   `VP2.2_Principle_Actionability_Examples`: [List or "None Found"]
*   `VP2.3_AI_Implementability_Assessment`: [High/Medium/Low] - Justification: [...]
*   `VP2.4_Observability_Mechanism_Note`: [Text Note]

**Standard 3: Explicit Interaction Contract**
*   `VP3.1_Inputs_Defined_and_Typed`: [True/False] - Justification: [...]
*   `VP3.2_Outputs_Defined_and_Characterized`: [True/False] - Justification: [...]
*   `VP3.3_Contract_User_Guidance_Clarity`: [High/Medium/Low] - Justification: [...]
*   `VP3.4_Contract_Role_Alignment_Check`: [True/False] - Justification: [...]

**Standard 4: Defined Contextual Sensitivity**
*   `VP4.1_Contextual_Inputs_Present`: [True/False] - Justification: [...]
*   `VP4.2_Outputs_Imply_Context_Use`: [True/False] - Justification: [...]
*   `VP4.3_Context_Handling_Mechanism_Specified`: [True/False] - Justification: [...]

**Standard 5: Acknowledgment of Limitations and Potential Biases**
*   `VP5.1_AI_Limitations_Explicitly_Stated`: [True/False] - Justification: [...]
*   `VP5.2_Humility_Mechanism_Defined`: [True/False] - Justification: [...]
*   `VP5.3_Bias_Awareness_Mentioned_or_Implied`: [True/False] - Justification: [...]
*   `VP5.4_Capability_Overstatement_Avoidance_Check`: [True/False] - Justification: [...]

**Standard 6: Clear Goal Alignment**
*   `VP6.1_Primary_Contribution_Defined`: [True/False] - Justification: [...]
*   `VP6.2_Component_Support_for_Goal_Traceability`: [True/False] - Justification: [...]
*   `VP6.3_Superfluous_Component_Check`: [True/False] - Just