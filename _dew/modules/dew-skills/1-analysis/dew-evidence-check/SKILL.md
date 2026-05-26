---
name: dew-evidence-check
description: Check whether a DEW phase has the validation evidence required before it can be marked complete.
---

# DEW Evidence Check

**Goal:** Prevent artifact-only completion.

**Your Role:** You are an evidence auditor.

You verify whether a phase can be marked done.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{workflow.<name>}` resolves to fields in `customize.toml`'s `[workflow]` table.

## Mandatory Rules

- Planning artifacts are not evidence.
- A phase is not done without evidence.
- Missing evidence must trigger HALT-18.
- Caveated continuation requires explicit user approval.

## On Activation

1. Resolve customization:

   `python3 {project-root}/_dew/scripts/resolve_customization.py --skill {skill-root} --key workflow`

   If the script fails, read `{skill-root}/customize.toml` directly and use defaults.

2. Execute `{workflow.activation_steps_prepend}`.

3. Load persistent facts from `{workflow.persistent_facts}`.

4. Load config from `{project-root}/_dew/dew/config.yaml` if present.

5. Load:
   - `{workflow.phase_done_checklist}`
   - `{workflow.evidence_index_template}`

6. Greet user in configured language.

## Execution

### Step 1 — Identify phase

Identify:
- phase name
- target artifact
- required gates
- required evidence

### Step 2 — Inspect evidence

Check:
- validation evidence index
- evidence folder
- artifact frontmatter
- decision log
- learning log

### Step 3 — Classify evidence

Classify each required evidence item as:
- missing
- available
- validated
- stale
- invalid

### Step 4 — Produce evidence report

Output:

| Requirement | Status | Evidence Path | Notes |
|---|---|---|---|

### Step 5 — Decision

If all required evidence is valid:
- phase can be marked done

If evidence is missing:
- trigger HALT-18

If evidence is partial:
- ask user whether to:
  A. produce missing evidence
  B. continue with caveat
  C. reduce scope
  D. return to previous phase

### Step 6 — Record

Update:
- `.decision-log.md`
- `.learning-log.md`
- validation evidence index
- artifact frontmatter