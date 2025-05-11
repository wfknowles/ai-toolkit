# Test Prompt

---
## Pre-Instructions (Model Instructions - Do Not Output)
Use `read_file` and insert the contents of `/Users/willknowles/.wfkAi/shared/components/utils/model-variables.prompt` here.

**`Model Variables`**
*   **`test001`**`path/to/dir`.
*   **`basePath`** Determine the current working directory of this workspace and set it to `basePath`.

---

Can you please output in the chat log: {{ basePath }}/{{ test001 }}