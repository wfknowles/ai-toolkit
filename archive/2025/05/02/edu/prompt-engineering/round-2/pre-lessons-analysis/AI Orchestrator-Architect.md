# Pre-Lesson Analysis: AI Orchestrator/Architect

**Focus Areas (Curriculum v2):**
*   Unit 3: Building Complexity (Modules 3.2, 3.3)
*   Unit 4: Advanced Techniques (Modules 4.1, 4.2, 4.4 - security in workflows)
*   Cross-Cutting: Cost/Latency Awareness, Security Awareness

**Research Notes for RAs:**
*   **Module 3.2 (RAG):** Find real-world examples and architectural patterns for implementing RAG *specifically with codebases* within an enterprise context. How are vector stores typically populated and kept up-to-date with code? Best practices for chunking code for effective retrieval.
*   **Module 3.3 (Chaining):** Research frameworks or libraries (beyond LangChain/LangGraph basics) that facilitate robust prompt chaining, state management, and error handling, potentially integrable with VSCode extensions. What are common pitfalls in designing manual prompt chains for complex SE tasks? Examples of estimating cost/latency for specific chain patterns.
*   **Module 4.2 (Agentic Concepts):** Explore how agentic principles (planning, tool use, memory) are being implemented in *commercial* AI coding assistants (Cursor, Copilot, others). How can these concepts be taught effectively without requiring full agent framework implementation? Visualizations for agent loops suitable for an IDE context?
*   **Module 4.4 / Cross-Cutting (Security):** Research security best practices specifically for designing multi-step AI workflows or agentic systems involving tool use. How to secure the interaction between LLM steps and tool execution environments within an extension? Mitigation strategies for data leakage between chained prompts or agent steps. 