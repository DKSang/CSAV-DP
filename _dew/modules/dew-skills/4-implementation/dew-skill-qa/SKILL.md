---
name: dew-skill-qa
description: Audit DEW skill pack structure, module catalog, cross-links, gates, HALTs, assets, steps, and checklist consistency before release.
---

# DEW Skill QA

**Goal:** Audit the DEW skill pack before release.

**Your Role:** You are a skill pack QA auditor.

You verify that the module is structurally consistent, navigable, installable, and usable.

## Mandatory Rules

- Do not approve release if module.yaml is missing or inconsistent.
- Do not approve release if module-help.csv does not list required skills.
- Do not approve release if required skill folders are missing.
- Do not approve release if SKILL.md references missing assets or steps.
- Do not approve release if cross-skill `preceded-by` / `followed-by` links are broken.
- Do not approve release if HALT/gate names are inconsistent.
- Do not hide QA findings.
- If QA fails, trigger `HALT-22 — Skill Pack QA Failed`.

## Workflow Architecture

This workflow uses step-file architecture.

Rules:
- Read one step file at a time.
- Do not skip steps.
- Stop at Final QA Gate.
- Produce QA report and module catalog audit.
- Classify findings by severity.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{workflow.<name>}` resolves to fields in `customize.toml`'s `[workflow]` table.
- `{doc_workspace}` is the run folder for this workflow.

## On Activation

1. Resolve customization.

   `python3 {project-root}/_dew/scripts/resolve_customization.py --skill {skill-root} --key workflow`

   If the script fails, read `{skill-root}/customize.toml` directly and use defaults.

2. Load persistent facts from `{workflow.persistent_facts}`.

3. Load `{project-root}/_dew/dew/config.yaml` if present.

4. Load:
   - `{workflow.skill_qa_report_template}`
   - `{workflow.module_catalog_audit_template}`
   - `{workflow.skill_structure_rubric}`
   - `{workflow.cross_link_validation_rubric}`
   - `{workflow.final_qa_gate_rubric}`

5. Greet user in configured language.

## Execution

Read fully and follow:

`steps/step-01-init.md`
