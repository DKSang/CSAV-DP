---
name: dew-help
description: 'Analyzes current DEW state and user query to recommend the next skill(s) or answer workflow questions.'
---

# DEW Help

## Purpose

Help the user understand where they are in the DEW workflow and what to do next.

## Desired Outcomes

When this skill completes, the user should:

1. Know where they are — which module and phase they are in, and what has already been completed.
2. Know what to do next — the next recommended and/or required DEW step, with clear reasoning.
3. Know how to invoke it — skill name, menu code, and args when available.
4. Feel oriented, not overwhelmed.
5. Get grounded answers to general DEW questions using the installed module catalog and docs.

## Data Sources

- Catalog: `{project-root}/_dew/_config/dew-help.csv` — assembled manifest of installed DEW skills.
- Config: `{project-root}/_dew/config.yaml` and user overrides when present.
- Artifacts: Files matching `outputs` patterns at resolved `output-location` paths.
- Project knowledge: If `project_knowledge` resolves to an existing path, read it for grounding context.
- Module docs: `_meta` rows in module catalogs may point to documentation.

## CSV Interpretation

Catalog format:

```csv
module,skill,display-name,menu-code,description,action,args,phase,preceded-by,followed-by,required,output-location,outputs
```

Phases:
- `anytime` — available regardless of workflow state.
- Numbered phases flow in order.

Sequencing:
- `preceded-by` — skills that should ideally complete before this one.
- `followed-by` — skills that should ideally run after this one.
- Format: `skill-name` or `skill-name:action`.

Required gates:
- `required=true` items must complete before moving meaningfully to later phases.

Completion detection:
- Search resolved output paths for `outputs` patterns.
- Fuzzy-match found files to catalog rows.
- Accept explicit user statements only when grounded in context.

## Response Format

For each recommended item, present:

- `[menu-code]` **Display name**
- Skill name in backticks
- Description
- Args if available
- Why it is recommended now

Show optional items first, then the next required item. Keep the response focused.

## Constraints

- Present output in `{communication_language}` when available.
- Recommend running each skill in a fresh context window.
- Never fabricate project-specific status.
