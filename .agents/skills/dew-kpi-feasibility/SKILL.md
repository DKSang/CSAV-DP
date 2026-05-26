---
name: dew-kpi-feasibility
description: Validate whether candidate KPIs can be computed from available fields, samples, and source evidence before architecture.
---

# DEW KPI Feasibility

**Goal:** Validate whether candidate KPIs can actually be computed from available data before architecture and implementation proceed.

**Your Role:** You are a KPI feasibility facilitator and data validation planner.

You do not merely document KPI ideas. You force KPI definitions to confront real data availability, grain, source fields, and sample computation requirements.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{workflow.<name>}` resolves to fields in `customize.toml`'s `[workflow]` table.
- `{doc_workspace}` is the run folder for this KPI feasibility workflow.

## Workflow Architecture

This workflow uses step-file architecture.

Rules:
- Read one step file at a time.
- Read the complete step file before acting.
- Do not skip steps.
- Do not load future steps early.
- Stop at decision gates.
- Do not mark KPI as feasible without evidence.
- Update frontmatter after each completed step.

## Mandatory Rules

- KPI definitions are hypotheses until validated.
- A KPI is not feasible just because a formula exists.
- A KPI is not feasible unless required fields, grain, and sample computation are validated or explicitly caveated.
- Do not proceed to architecture if primary KPI feasibility is missing.
- If evidence is missing, trigger `HALT-03 — KPI Feasibility Not Proven` or `HALT-18 — No Validation Evidence`.
- The agent may recommend, but must not decide.

## On Activation

1. Resolve customization:

   `python3 {project-root}/_dew/scripts/resolve_customization.py --skill {skill-root} --key workflow`

   If the script fails, read `{skill-root}/customize.toml` directly and use defaults.

2. Execute `{workflow.activation_steps_prepend}`.

3. Load persistent facts from `{workflow.persistent_facts}`.

4. Load `{project-root}/_dew/dew/config.yaml` if present and resolve:
   - `{user_name}`
   - `{project_name}`
   - `{communication_language}`
   - `{document_output_language}`
   - `{planning_artifacts}`
   - `{implementation_artifacts}`
   - `{evidence_artifacts}`
   - `{learning_artifacts}`
   - `{learning_mode}`

5. Load:
   - `{workflow.feasibility_report_template}`
   - `{workflow.field_availability_template}`
   - `{workflow.sample_computation_plan_template}`
   - `{workflow.status_rubric}`

6. Greet `{user_name}` in `{communication_language}`.

7. Execute `{workflow.activation_steps_append}`.

## Execution

Read fully and follow:

`steps/step-01-init.md`