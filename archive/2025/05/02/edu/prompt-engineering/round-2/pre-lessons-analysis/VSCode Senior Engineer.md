# Pre-Lesson Analysis: VSCode Senior Engineer

**Focus Areas (Curriculum v2):**
*   Unit 2-5: Technical implementation within Extension
*   Supporting Elements: VSCode Extension development, Web-Extension API (implementation side)

**Research Notes for RAs:**
*   **Extension Tech:** Deep dive into the pros/cons and technical implementation details of using VSCode Notebook API vs. Webview API for *interactive educational content*. Find examples of extensions using each for similar purposes. Performance implications and best practices for optimization within Cursor?
*   **Cursor APIs:** Investigate any specific APIs exposed by Cursor itself for interacting with its AI features (chat, diffs, context providers) from an extension. Stability, documentation, limitations?
*   **State Management:** Research best practices and libraries for managing state within a VSCode extension, especially for coordinating user progress and exercise state potentially synced with a web backend.
*   **Testing Extensions:** Find frameworks and best practices for automated testing (unit, integration, e2e) of VSCode extensions, particularly those involving webviews or complex interactions with the editor/language servers. How to test interactions with Cursor's specific features? 