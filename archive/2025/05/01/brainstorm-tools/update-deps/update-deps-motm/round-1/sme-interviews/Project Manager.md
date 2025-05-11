# Project Manager - MotM Round 1 SME Interview

**Date:** 2025-05-01
**Interviewee:** Project Manager (PM)
**Interviewer:** Facilitator

**(Facilitator):** Thanks for your pre-analysis. You pointed out that while the Top 15 has useful elements like risk indicators (#13) and branching (#11), it lacks explicit integration with PM tooling, effort visibility, progress tracking, and reporting.

**(Facilitator):** How critical is direct integration with PM tools like Jira (your #2 refinement) versus just providing formatted output? Is the latter sufficient?

**(PM):** Direct integration is highly desirable for reducing friction. Manually copying/pasting tasks (#2 refinement) is better than nothing, but it adds overhead and risks information becoming outdated. Ideally, the assistant could suggest creating a Jira ticket populated with the summary (#10), risk level (#13), potential breaking changes (#2), and maybe the effort bucket (PO/PM #3 refinement). The ticket status could then potentially be updated automatically based on the branch (#11) status (your #1 refinement) or test results (#3).

**(Facilitator):** You and the PO both pushed for adding effort indicators (#3 refinement). Given the acknowledged difficulty in AI estimating this accurately, how would you actually use such an indicator in planning?

**(PM):** We'd use it as a *very rough initial guide* only, not a commitment. If the AI flags an update as 'Large' effort, we know to allocate significant time for developer investigation and testing in sprint planning. If it flags 'Trivial', it might be bundled with other small tasks or handled quickly. It helps size the *investigation* task, not necessarily the final implementation time. We'd absolutely need to calibrate it heavily based on our team's experience and refine the heuristics over time.

**(Facilitator):** If you were designing the workflow integration aspect, what would your ideal solution look like?

**(PM):** Ideal flow:
1.  **Scheduled Trigger (CI/CD - Arch-1):** Tool runs automatically (e.g., weekly).
2.  **Reporting (#9 concept):** Generates a concise dashboard/report view: # projects scanned, # critical updates pending, trends over time.
3.  **Task Suggestion (#2 refinement):** For high-priority updates (Critical/High risk #13), suggests creating tickets in the PM tool, pre-populated with details.
4.  **Status Linking (#1 refinement):** Links the PM ticket status to the Git branch (#11) status (e.g., Open -> Branch Created -> In Review -> Merged/Closed).
5.  **Manual Trigger:** Developers can also trigger it manually for specific dependencies.
The key is automating the reporting and task creation/linking to minimize manual PM overhead for routine maintenance.

**(Facilitator):** What unknown unknowns concern you most about integrating AI-assisted updates into project management?

**(PM):** The biggest unknown is the actual impact on team velocity and predictability. Will the tool *save* time overall by streamlining analysis, or will it *cost* time due to chasing down flagged issues (#2) or dealing with inaccurate risk assessments (#13) or effort hints (#3 refinement)? Another unknown is how to effectively budget time for dependency updates – should it be a standard % allocation per sprint, or handled reactively based on the tool's reports?

**(Facilitator):** Does the Top 15 concept have major blindspots from a project workflow or tracking perspective?

**(PM):** As mentioned, the lack of explicit PM tool integration (#2 refinement), progress tracking (#1 refinement), and reporting (#9 concept) are the main blindspots compared to a fully integrated solution. It feels more like a developer tool than a full project maintenance workflow tool in its current Top 15 form.

**(Facilitator):** Any missing SMEs you'd recommend adding?

**(PM):** Perhaps someone from Finance or Procurement, *if* we consider integrating license cost information (#6). Understanding the cost implications of dependencies could become relevant. Otherwise, the current group covers the main technical and product aspects relevant to project planning.

**(Facilitator):** Useful insights on the value of direct PM tool integration, using effort indicators cautiously, the ideal automated workflow, and the unknowns around velocity impact. Thank you. 