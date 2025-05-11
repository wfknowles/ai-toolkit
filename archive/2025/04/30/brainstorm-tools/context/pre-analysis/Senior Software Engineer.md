# Senior Software Engineer - Initial Context Management Concepts

Focusing on practical implementation and leveraging code/data context effectively:

1.  **Code-Aware Context Injection:** Automatically injecting relevant code snippets, function definitions, or class structures into the prompt based on the file/function the user is currently working on in the IDE.
2.  **Database Schema as Context:** Providing relevant parts of the database schema (table definitions, relationships) as context when generating or analyzing SQL queries or ORM code.
3.  **API Contract Contextualization:** Injecting OpenAPI/Swagger definitions or relevant parts of API client/server code as context when working on API integration tasks or generating API tests.
4.  **Version Control Context (Diffs/History):** Using recent code changes (diffs) or commit history messages as context for prompts related to debugging regressions, understanding recent modifications, or generating related tests.
5.  **Configuration File Context:** Providing relevant sections of configuration files (e.g., `.env`, `config.yaml`, Kubernetes manifests) as context when generating deployment scripts, troubleshooting configuration issues, or explaining system behavior.
6.  **Contextualized Error Message Analysis:** A prompt that takes an error message and stack trace, automatically retrieves the relevant code snippets mentioned in the trace, and uses both as context to suggest potential causes and fixes.
7.  **Dependency Graph Context:** Utilizing information from a dependency graph (e.g., `package-lock.json`, Maven POM) as context when analyzing the impact of library updates or identifying potential conflicts.
8.  **Embedding Technical Documentation Context (RAG):** Setting up Retrieval-Augmented Generation specifically over internal technical documentation, wikis, and runbooks, allowing prompts to pull in accurate procedural or architectural context.
9.  **Test Execution Results as Context:** Feeding the results of recent test runs (especially failures) into subsequent prompts for debugging, test fixing, or generating supplementary tests. 