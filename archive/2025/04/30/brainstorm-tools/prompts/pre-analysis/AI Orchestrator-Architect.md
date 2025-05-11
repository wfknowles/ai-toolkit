# AI Orchestrator/Architect - Initial Concepts

Considering the software maintenance lifecycle and leveraging AI orchestration:

1.  **Maintenance Workflow Automation:** A prompt to define and orchestrate a multi-step maintenance task (e.g., apply patch -> run tests -> deploy to staging -> run smoke tests -> notify team) using different AI tools/prompts for each step.
2.  **Intelligent Issue Triage Agent:** Design a prompt for an agent that ingests bug reports, classifies severity/priority using context from code and past issues, identifies potential duplicate issues, and routes the report to the appropriate team/engineer.
3.  **Cross-Tool Knowledge Synthesis for Debugging:** A prompt to orchestrate analysis across multiple tools (logs, metrics, traces, code analysis) for a given issue, synthesizing the findings to pinpoint a likely root cause.
4.  **Adaptive Monitoring Configuration:** A prompt that analyzes system performance metrics and logs during maintenance windows (e.g., post-deployment) and suggests adjustments to monitoring thresholds or alert rules.
5.  **Rollback Strategy Generation:** A prompt that, given a failed deployment or critical post-release bug, analyzes the changes made and generates a sequence of steps (manual or automated) for a safe rollback procedure.
6.  **Resource Optimization for Maintenance Tasks:** A prompt to analyze the resource requirements (CPU, memory, network) for planned maintenance tasks (e.g., data migration script, large test suite execution) and suggest optimal scheduling or resource allocation.
7.  **Proactive Maintenance Prediction:** A prompt to analyze historical trends in issues, performance, and code churn to predict components likely to require maintenance soon, suggesting proactive refactoring or testing.
8.  **Impact Assessment Orchestration:** A prompt that orchestrates multiple analysis prompts (dependency analysis, code change impact, test coverage) to provide a comprehensive impact assessment report for a proposed change during maintenance.
9.  **Multi-Agent Debugging Swarm:** Define prompts for multiple specialized AI agents (e.g., Log Analyzer Agent, Code Structure Agent, Performance Agent) that collaborate, orchestrated by a master prompt, to diagnose complex production issues. 