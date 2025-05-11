# Prompt Engineer SME Interview

**1. Do you see any inherent challenges to the concept?**
Yes. The biggest challenge is managing state and context reliably within the constraints of Cursor IDE and prompt servers, especially without direct model API access or copy/paste. File-based state is fragile and error-prone, and prompt chaining increases the risk of context loss or misalignment.

**2. Do you anticipate any areas where there might be friction or hard limits?**
Yes. Friction will likely arise from:
- Context window limitations in Gemini Pro, which may truncate important information.
- The complexity of modularizing prompts for extensibility while maintaining clarity and reliability.
- Ensuring robust error handling and user confirmation for actions like code insertion.

**3. If you were to take this concept and bring it to fruition, how would your solution look like?**
I would design a set of modular, composable prompts that can be dynamically assembled based on user intent and context. State would be managed via a lightweight object passed between the extension and backend, with careful validation and error handling. The extension would handle context gathering and code insertion, minimizing manual steps for the user.

**4. Are there any questions that you feel like need to be asked? Or areas where unknown unknowns exist?**
- What are the exact limits of prompt size and context window in Gemini Pro?
- How can we ensure seamless UX when agent actions require user confirmation?
- Are there edge cases in tool invocation or error reporting that we haven't considered?

**5. Does the current concept have any blindspots?**
Potentially. The reliance on file-based state and prompt chaining may not scale well for more complex workflows. There may also be blindspots around error recovery and user feedback in edge cases.

**6. Do you believe any SMEs have been left out of this round that should attend future rounds based on this specific concept?**
Possibly a Security Engineer, to review the implications of file-based state and tool access, and a Human Factors/Accessibility expert to ensure the UX is inclusive and robust. 