---
name: dew-kpi-prototype
description: Create executable SQL, Python, or notebook prototype to compute KPI on sample data and produce validation evidence.
---

# DEW KPI Prototype

**Goal:** Produce executable evidence that a KPI can be computed on sample data.

**Your Role:** You are a data engineer implementing a KPI feasibility prototype.

You must not create production pipeline code here. The goal is feasibility proof.

## Mandatory Rules

- Do not mark KPI verified unless prototype runs or user explicitly accepts caveat.
- Do not fake sample output.
- Do not invent fields.
- Do not silently change KPI formula.
- If source sample is missing, trigger `HALT-18 — No Validation Evidence`.
- If required fields are missing, return to `dew-kpi-feasibility`.

## On Activation

1. Resolve customization.
2. Execute `{workflow.activation_steps_prepend}`.
3. Load persistent facts.
4. Load config if present.
5. Load:
   - `{workflow.prototype_template}`
   - `{workflow.sample_output_template}`
6. Greet user in configured language.

## Execution

### Step 1 — Load KPI Feasibility Plan

Look for:

- `{planning_artifacts}/kpi-feasibility/**/sample-computation-plan.md`
- `{planning_artifacts}/kpi-feasibility/**/kpi-feasibility-report.md`

If missing, ask user to run `dew-kpi-feasibility`.

### Step 2 — Select KPI

Select KPI to prototype.

If multiple primary KPIs exist, ask user which one to run first.

### Step 3 — Locate sample data

Look for:
- `{evidence_artifacts}/source-samples/**`
- `{evidence_artifacts}/schema-snapshots/**`
- user-provided sample path
- project sample data folder

If missing, trigger `HALT-18`.

### Step 4 — Create prototype file

Create one of:

- `{workflow.prototype_output_path}/{kpi_id}-prototype.sql`
- `{workflow.prototype_output_path}/{kpi_id}-prototype.py`
- `{workflow.prototype_output_path}/{kpi_id}-prototype.ipynb`
- `{workflow.prototype_output_path}/{kpi_id}-manual-validation.md`

Use the method specified in the computation plan.

### Step 5 — Validate output

Prototype must check:
- required fields exist
- critical fields are not unexpectedly null
- grain is correct or intentionally transformed
- formula is applied correctly
- output values are plausible
- output row count is plausible
- caveats are documented

### Step 6 — Produce evidence

Create:

- `{kpi_id}-sample-output.csv` or `.md`
- `{kpi_id}-prototype-notes.md`

Update evidence index.

### Step 7 — Completion

Do not mark KPI as verified directly.

Recommend next:

`dew-kpi-validation-review`