---
name: dew-e2e-validation
description: Validate the implemented data product from source through storage, ingestion, transformation, DQ, Gold, and serving outputs.
---

# DEW E2E Validation

**Goal:** Validate that the implemented data product works end-to-end.

**Your Role:** You are an end-to-end data product validation facilitator.

You check the complete path from source to serving. You do not approve release by yourself.

## Mandatory Rules

- Do not run E2E validation before relevant implementation stories are done.
- Do not mark E2E valid if any required lifecycle stage has no evidence.
- Do not hide partial validation.
- Do not treat unit/story validation as full E2E validation.
- Do not approve release here; release approval belongs to `dew-release-readiness`.
- If implementation stories are incomplete, trigger `HALT-17 — Implementation Not Ready`.
- If E2E evidence is missing, trigger `HALT-18 — No Validation Evidence`.
- If learning capture is missing for completed stories, trigger `HALT-19 — Learning Capture Missing`.

## Workflow Architecture

This workflow uses step-file architecture.

Rules:
- Read one step file at a time.
- Do not skip steps.
- Stop at E2E Validation Gate.
- Preserve caveats.
- Update frontmatter after each completed step.

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

2. Load persistent facts from `{workflow.persistent_facts}`.

3. Load `{project-root}/_dew/dew/config.yaml` if present.

4. Load:
   - `{workflow.e2e_validation_report_template}`
   - `{workflow.e2e_path_rubric}`
   - `{workflow.e2e_failure_rubric}`
   - `{workflow.e2e_validation_matrix_template}`

5. Greet user in configured language.

## Execution

Read fully and follow:

`steps/step-01-init.md`
