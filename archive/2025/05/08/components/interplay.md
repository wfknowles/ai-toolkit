+-----------------------------------------+      +-----------------------------------------+
| Governance & Standards Documents        |----->| Git Repo Structure & Branching (#16)    |
| (e.g., #1, #8, #10, #14, #15)           |      +-----------------------------------------+
+-----------------------+-----------------+
                        |
                        | Defines & Guides
                        V
+-----------------------------------------------------------------------+
| Centralized Repositories (Git)                                        |
|-----------------------------------------------------------------------|
|   +--------------------------+  +--------------------------+  +-------+
|   | Prompt Library (#2)      |  | Codebase Repo(s)         |  | Other |
|   | - Prompts/Templates      |  | - Application Code       |  | Repos |
|   | - Exemplars (#4 Support) |  | - Tests (Unit/Int)       |  | (#5...) |
|   | - Tests (#4 Core)        |  +--------------------------+  +-------+
|   | - Linter Config (#3)     |
|   +-----------+--------------+
|               | (Uses/Stores)
|               |
| Controls & Uses | Tests & Lints
| V             V
+--------------------------+      +--------------------------+
| Prompt Linter (#3)       |      | Prompt Eval Fw (#4)      |
+--------------------------+      +--------------------------+
       |                                |
       | Runs Linter                    | Runs Tests
       V                                V
+------------------------------------------------+      +------------------------------------------+
| GitHub Actions: Prompt CI/CD (#6)              |      | GitHub Actions: Codebase CI/CD (#7)        |
| - Triggered by Prompt Repo changes             |      | - Triggered by Codebase Repo changes     |
| - Uses Linter (#3), Eval Fw (#4)               |      | - Uses Code Linters, Security Tools      |
| - Enforces Standards via Status Checks         |      | - Uses Tool Baselines (#10)              |
+-------------------------+----------------------+      | - Enforces Standards via Status Checks   |
                          |                             +--------------------+---------------------+
                          |                                                  | Uses Tool Configs
                          |                                                  V
                          |                               +------------------------------------------+
                          |                               | Security Tool Baselines (#10)            |
                          |                               +------------------------------------------+
                          | Consumes Prompts
                          V
+------------------------------------------------+      +------------------------------------------+
| Dockerized Prompt Backend Service (#5)         |<-----| IDE Integration Plugin (#11)             |
| - Serves prompts via API                       |      | - Collects Context, Calls Backend        |
| - Uses Prompt Library (#2)                     |----->| - Displays Prompts to User in IDE        |
| - Logs Interactions (uses #14 Spec)            |      +-----------------------+------------------+
+------------------------------------------------+                              | Guides User Interaction
                                                                                V
+---------------------------------------------------------------------------------------------------+
| Developer using IDE (e.g., Cursor)                                                                |
| - Interacts with Plugin (#11)                                                                     |
| - Follows Onboarding Guide (#12), Standards (#1, #8), Contribution Guidelines (#13)                |
| - Receives feedback from Linters (#3 via IDE?), CI (#6, #7)                                       |
| - Benefits from improved DevX (defined by #11, #12)                                               |
+---------------------------------------------------------------------------------------------------+
       ^                                                                          ^
       | Inputs To                                                                | Influences
       |                                                                          |
+------+-----------------------------------------+  +-----------------------------+-----------------+
| Threat Models (#9), Ethical Review (#15),     |  | Developer Onboarding Guide (#12)            |
| Audit Log Spec (#14)                          |  | Prompt Contribution Guidelines (#13)        |
+-----------------------------------------------+  +---------------------------------------------+