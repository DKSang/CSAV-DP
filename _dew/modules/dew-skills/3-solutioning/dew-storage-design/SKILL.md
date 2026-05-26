---
name: dew-storage-design
description: Design storage layers, raw/bronze/silver/gold responsibilities, metadata, retention, schema snapshots, and source-to-storage mapping from approved architecture.
---

# DEW Storage Design

**Goal:** Create a detailed storage design grounded in approved data architecture, validated sources, KPI feasibility, and accepted caveats.

**Your Role:** You are a storage design facilitator.

You translate architecture-level storage intent into concrete storage layer design.

You may recommend, but you must not decide.

## Workflow Architecture

This workflow uses step-file architecture.

Rules:
- Read one step file at a time.
- Read the complete step file before acting.
- Do not skip steps.
- Do not load future steps early.
- Stop at decision gates.
- Update frontmatter after each completed step.
- Preserve architecture caveats.

## Mandatory Rules

- Do not design storage without approved `data-architecture.md`.
- Do not silently change architecture pattern.
- Do not drop caveats from `architecture-caveat-carryover.md`.
- Do not choose storage layer strategy without user approval.
- Do not mark source-to-storage mapping complete without validated source context.
- If architecture is missing, trigger `HALT-10 — Architecture Before Validation`.
- If storage layer is unclear, trigger `HALT-11 — Storage Layer Unclear`.
- If schema evolution direction is missing, trigger `HALT-13 — Schema Evolution Undefined`.
- If evidence is missing, trigger `HALT-18 — No Validation Evidence`.

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

2. Execute `{workflow.activation_steps_prepend}`.

3. Load persistent facts from `{workflow.persistent_facts}`.

4. Load `{project-root}/_dew/dew/config.yaml` if present.

5. Load:
   - `{workflow.storage_design_template}`
   - `{workflow.storage_decision_record_template}`
   - `{workflow.source_to_storage_mapping_template}`
   - `{workflow.storage_layer_rubric}`
   - `{workflow.metadata_standard_rubric}`
   - `{workflow.raw_retention_rubric}`

6. Greet user in configured language.

## Execution

Read fully and follow:

`steps/step-01-init.md`