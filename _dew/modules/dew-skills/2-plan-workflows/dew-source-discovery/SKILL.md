---
name: dew-source-discovery
description: Discover candidate data sources and document their expected role, access method, owner, grain, and source type without accepting them yet.
---

# DEW Source Discovery

**Goal:** Discover and document candidate sources for the data product without prematurely accepting them.

**Your Role:** You are a source discovery facilitator.

You help the user identify possible source systems, but you must not claim a source is usable until it is validated.

## Mandatory Rules

- Candidate source does not mean accepted source.
- Do not mark any source as P1 in this skill.
- Do not assume access works.
- Do not assume schema exists or is stable.
- Do not assume source fields match KPI required fields.
- If no candidate source exists for a primary KPI, trigger `HALT-04 — Source Not Identified`.

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

4. Load `{project-root}/_dew/dew/config.yaml` if present and resolve:
   - `{user_name}`
   - `{project_name}`
   - `{communication_language}`
   - `{document_output_language}`
   - `{planning_artifacts}`
   - `{evidence_artifacts}`
   - `{learning_artifacts}`
   - `{learning_mode}`

5. Load:
   - `{workflow.source_inventory_template}`
   - `{workflow.source_candidate_rubric}`
   - `{workflow.source_type_guide}`

6. Greet `{user_name}` in `{communication_language}`.

## Intent Modes

### Create

Create a source inventory from project brief, PRD, KPI catalog, KPI-source matrix, and user-provided context.

### Update

Update source inventory when new sources are discovered or existing sources are removed.

### Validate

Validate whether source inventory is complete enough to proceed to assessment.

## Execution

### Step 1 — Load context

Look for:
- project brief
- business discovery
- KPI catalog
- KPI-source matrix
- data product PRD
- decision log

### Step 2 — Identify candidate sources

For each source, capture:
- source ID
- source name
- source type
- expected business role
- expected KPI dependency
- access method
- owner/provider
- expected grain
- expected freshness
- status = Candidate

### Step 3 — Check source coverage

For each primary KPI, check whether at least one candidate source exists.

If no source exists for a primary KPI, trigger `HALT-04 — Source Not Identified`.

### Step 4 — Create source inventory

Create:

`{workflow.source_output_path}/{workflow.run_folder_pattern}/source-inventory.md`

### Step 5 — Finalize

Run checklist.

Recommend next:

`dew-source-assessment`