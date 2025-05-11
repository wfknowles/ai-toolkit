# Expert Persona Panel - AWS Serverless Focus

**`persona_panel_id`**: `aws-panel-serverless`


**`AI Systems Auditor`**`/Users/wknowles/Develop/ai/myAi/trevipay/persona/ai-systems-auditor.persona.md`
**`App & Cloud Security`**`/Users/wknowles/Develop/ai/myAi/trevipay/persona/app-and-cloud-security.md`
**`Cybersecurity Risk Analyst`**`/Users/wknowles/Develop/ai/myAi/trevipay/persona/cyber-risk-analyst.persona.md`
**`Communications & Dialogue`**`/Users/wknowles/Develop/ai/myAi/trevipay/persona/dev-sec-ops.persona.md`
**`DevX & Tooling`**`/Users/wknowles/Develop/ai/myAi/trevipay/persona/devx-and-tooling.md`

---
```ts
import { buildPanel, CaseTransformer, caseTransformer } from '../ts/buildPanel.ts';
```

**`persona`**
```json
[
    {
       "id": "`AI Systems Auditor`.persona_id",
       "name": "`AI Systems Auditor`.persona_name",
       "source": "`AI Systems Auditor`.source", 
    },
    {
       "id": "`App & Cloud Security`.persona_id",
       "name": "`App & Cloud Security`.persona_name",
       "source": "`App & Cloud Security`.source", 
    },
    {
       "id": "`Cybersecurity Risk Analyst`.persona_id",
       "name": "`Cybersecurity Risk Analyst`.persona_name",
       "source": "`Cybersecurity Risk Analyst`.source", 
    },
    {
       "id": "`Communications & Dialogue`.persona_id",
       "name": "`Communications & Dialogue`.persona_name",
       "source": "`Communications & Dialogue`.source", 
    },
    {
       "id": "`DevX & Tooling`.persona_id",
       "name": "`DevX & Tooling`.persona_name",
       "source": "`DevX & Tooling`.source", 
    },
]
```
---

**## Required Output: ##**

A single JSON object conforming strictly to `Session State Object Schema v1.1`. Example:
```json
{
  "panelId": {{ persona_panel_id }},
  "persona": [
  ```
  ```markdown
{{#if persona}}
    {{#each persona}}

    ```json
    {
        "id": {{ id }},
        "name": {{ name }},
        "source": {{ source }}
    },
    ```

    ```markdown
    {{/each}}
{{/if}}
```json
  ],
}
```

```
```

---