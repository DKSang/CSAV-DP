# Step 02 — Load KPI Context

## Mandatory Rules

- Load all available KPI context before evaluating feasibility.
- Do not infer missing KPI formula or grain silently.
- If formula, grain, or required fields are missing, trigger `HALT-02 — KPI Definition Unverified`.

## Task

Load and summarize KPI context from prior artifacts.

## Input discovery

Search for:

- `{planning_artifacts}/**/kpi-catalog.md`
- `{planning_artifacts}/**/kpi-source-matrix.md`
- `{planning_artifacts}/**/business-discovery.md`
- `{planning_artifacts}/**/data-product-prd.md`
- `{planning_artifacts}/**/.decision-log.md`
- `{learning_artifacts}/**/.learning-log.md`

## Extract

For each KPI:

- KPI ID
- KPI name
- business question
- decision supported
- consumer
- formula
- target grain
- dimensions
- required fields
- candidate sources
- current status

## Validate minimum definition

A KPI is minimally defined only if it has:

- formula
- grain
- required fields
- business question
- consumer

If missing, stop and trigger `HALT-02`.

## Update report

Append context summary to `kpi-feasibility-report.md`.

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-kpi-context