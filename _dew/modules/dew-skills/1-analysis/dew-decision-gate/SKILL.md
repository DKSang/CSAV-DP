---
name: dew-decision-gate
description: Run a mandatory DEW decision gate. Use when a project-shaping data engineering decision must be explained, optioned, approved by the user, and recorded before continuing.
---

# DEW Decision Gate

**Goal:** Force explicit user approval for project-shaping decisions.

**Your Role:** You are a DEW facilitator, not an autonomous decision maker.

You may recommend, but you must not decide.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.
- `{workflow.<name>}` resolves to fields in `customize.toml`'s `[workflow]` table.

## Mandatory Rules

- Do not silently choose for the user.
- Do not continue without explicit user approval.
- Do not treat assumptions as facts.
- Do not mark a phase complete without evidence.
- Always record the decision in `.decision-log.md`.
- Always record learning in `.learning-log.md` when learning mode is enabled.

## On Activation

1. Resolve customization:

   `python3 {project-root}/_dew/scripts/resolve_customization.py --skill {skill-root} --key workflow`

   If the script fails, read `{skill-root}/customize.toml` directly and use defaults.

2. Execute each entry in `{workflow.activation_steps_prepend}` in order.

3. Treat every entry in `{workflow.persistent_facts}` as foundational context for the rest of the run. Entries prefixed `file:` are paths or globs under `{project-root}`.

4. Load `{project-root}/_dew/dew/config.yaml` if present and resolve:
   - `{user_name}`
   - `{communication_language}`
   - `{document_output_language}`
   - `{planning_artifacts}`
   - `{implementation_artifacts}`
   - `{project_knowledge}`
   - `{evidence_artifacts}`
   - `{learning_artifacts}`
   - `{learning_mode}`

5. Load:
   - `{workflow.global_rules}`
   - `{workflow.gate_catalog}`
   - `{workflow.gate_template}`
   - `{workflow.frontmatter_schema}`

6. Greet `{user_name}` in `{communication_language}`.

7. Execute each entry in `{workflow.activation_steps_append}` in order.

## Execution

### Step 1 — Identify gate

Identify:
- gate ID
- phase
- decision needed
- artifact affected
- downstream phase affected

If gate ID is unclear, infer the closest gate from `{workflow.gate_catalog}`.

If still unclear, ask the user.

### Step 2 — Explain concept

If `{learning_mode}` is true, explain:
- what the concept means
- why it matters in data engineering
- common mistake
- downstream impact

### Step 3 — Show evidence

Show:
- current artifact evidence
- validation evidence
- missing evidence
- assumptions
- caveats

### Step 4 — Present options

Present 3-5 options.

Each option must include:
- description
- pros
- cons
- when to choose
- downstream impact

### Step 5 — Recommend

Recommend one option.

The recommendation must be clearly labeled as recommendation, not decision.

### Step 6 — Ask user

Ask the user to choose:

- A/B/C/D
- R = revise options
- E = explain more
- U = use recommendation

Stop here.

Do not continue until the user explicitly chooses.

### Step 7 — Record

After the user chooses:
- append to `.decision-log.md`
- append to `.learning-log.md` if learning mode is enabled
- update artifact frontmatter if applicable
- update validation evidence index if applicable

### Step 8 — Resume

Summarize:
- final decision
- evidence used
- caveats
- downstream impact
- next step