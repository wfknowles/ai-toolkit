# Senior Software Engineer SME Interview

**1. Do you see any inherent challenges to the concept?**
Yes. The main challenge is building a robust, stateful workflow using only prompts and file I/O in a chat interface. This approach is brittle and lacks the guarantees of traditional application code. The "no copy/paste" and "chat only" constraints make error recovery and state management difficult.

**2. Do you anticipate any areas where there might be friction or hard limits?**
- File writes are not atomic, so tool failures could corrupt state.
- Context window and prompt size limitations may cause loss of important information.
- Error handling and user feedback will be hard to implement reliably without more control over the environment.

**3. If you were to take this concept and bring it to fruition, how would your solution look like?**
I would use a modular backend structure with clear separation of concerns, robust unit and integration tests, and a CI pipeline. State would be managed in JSON for structure, and all tool logic would be thoroughly tested and logged. I would also advocate for a rollback/undo mechanism for code insertions.

**4. Are there any questions that you feel like need to be asked? Or areas where unknown unknowns exist?**
- How do we recover from partial or failed state updates?
- What are the performance implications for large files or long conversations?
- How do we ensure extensibility for future tools and workflows?

**5. Does the current concept have any blindspots?**
Yes. The reliance on file-based state and prompt chaining may not scale for more complex workflows. There may also be blindspots around error recovery, performance, and extensibility.

**6. Do you believe any SMEs have been left out of this round that should attend future rounds based on this specific concept?**
A Test Engineer for automated testing and a Security Engineer for reviewing file and tool access risks would be valuable additions. 