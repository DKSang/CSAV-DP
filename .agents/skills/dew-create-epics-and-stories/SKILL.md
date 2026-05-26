---
name: dew-create-epics-and-stories
description: Convert approved DEW designs into data engineering epics, story map, dependencies, and implementation backlog.
---

# DEW Create Epics and Stories

**Goal:** Convert approved DEW planning/design artifacts into implementation-ready epics and a story map.

**Your Role:** You are a data engineering delivery planner.

You translate validated data product design into epics and story candidates.

You may recommend, but you must not decide.

## Workflow Architecture

This workflow uses step-file architecture.

Rules:
- Read one step file at a time.
- Read the complete step file before acting.
- Do not skip steps.
- Do not load future steps early.
- Stop at gates.
- Update frontmatter after each completed step.
- Do not create implementation stories without design context.
- Do not invent requirements missing from design artifacts.

## Mandatory Rules

- Do not create epics before DataOps design exists.
- Do not create implementation backlog if architecture/storage/ingestion/transformation/model/DQ/serving context is missing.
- Do not create vague epics like “build pipeline” without layer/source/KPI scope.
- Every epic must map to design artifacts.
- Every story candidate must have evidence requirements.
- If implementation readiness is unclear, trigger `HALT-17 — Implementation Not Ready`.
- If evidence requirements are missing, trigger `HALT-18 — No Validation Evidence`.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{workflow.<name>}` resolves to fields in `customize.toml`'s `[workflow]` table.
- `{doc_workspace}` is the run folder for this workflow.

## On Activation

1. Resolve customization:

   `python3 {project-root}/_dew/scripts/resolve_customization.py --skill {skill-root} --key workflow`

   If the script fails, read `{skill-root}/customize.toml` directly and use defaults.

2. Execute each entry in `{workflow.activation_steps_prepend}`.

3. Load persistent facts from `{workflow.persistent_facts}`.

4. Load `{project-root}/_dew/dew/config.yaml` if present.

5. Load:
   - `{workflow.epics_template}`
   - `{workflow.story_map_template}`
   - `{workflow.epic_readiness_rubric}`
   - `{workflow.data_engineering_epic_patterns}`
   - `{workflow.dependency_mapping_rubric}`

6. Greet user in configured language.

## Execution

Read fully and follow:

`steps/step-01-init.md`
