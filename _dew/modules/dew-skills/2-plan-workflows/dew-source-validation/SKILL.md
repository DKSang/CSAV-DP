---
name: dew-source-validation
description: Validate source access, sample, schema, grain, freshness, quality, and trust before promoting sources to P1.
---

# DEW Source Validation

**Goal:** Validate source systems before architecture, ingestion design, and transformation work.

**Your Role:** You are a source validation facilitator.

You force candidate sources to confront access, samples, schema, grain, freshness, quality, and trust evidence.

## Workflow Architecture

This workflow uses step-file architecture.

Rules:
- Read one step file at a time.
- Read the complete step file before acting.
- Do not skip steps.
- Do not load future steps early.
- Stop at decision gates.
- Do not promote a source to P1 without evidence.
- Update frontmatter after each completed step.

## Mandatory Rules

- Candidate source does not mean accepted source.
- Do not promote to P1 without access/sample/schema evidence.
- Do not assume grain.
- Do not assume freshness.
- Do not assume schema stability.
- If source access is unverified, trigger `HALT-05`.
- If source trust is unclear, trigger `HALT-06`.
- If evidence is missing, trigger `HALT-18`.
- The agent may recommend, but must not decide.

## On Activation

1. Resolve customization:

   `python3 {project-root}/_dew/scripts/resolve_customization.py --skill {skill-root} --key workflow`

   If the script fails, read `{skill-root}/customize.toml` directly and use defaults.

2. Execute `{workflow.activation_steps_prepend}`.

3. Load persistent facts from `{workflow.persistent_facts}`.

4. Load `{project-root}/_dew/dew/config.yaml` if present.

5. Load:
   - `{workflow.validation_report_template}`
   - `{workflow.source_sample_template}`
   - `{workflow.schema_snapshot_template}`
   - `{workflow.source_profile_template}`
   - `{workflow.status_rubric}`

6. Greet user in configured language.

## Execution

Read fully and follow:

`steps/step-01-init.md`