# Step 02 — Load Source Context

## Mandatory Rules

- Load candidate source context before validation.
- Do not infer source access, grain, freshness, or field coverage silently.
- If source inventory is missing, trigger `HALT-04 — Source Not Identified`.

## Task

Load source context from prior artifacts.

## Input discovery

Search for:
- `{planning_artifacts}/**/source-inventory.md`
- `{planning_artifacts}/**/source-scorecard.md`
- `{planning_artifacts}/**/kpi-catalog.md`
- `{planning_artifacts}/**/kpi-source-matrix.md`
- `{planning_artifacts}/**/data-product-prd.md`
- `{planning_artifacts}/**/kpi-feasibility-report.md`
- `{planning_artifacts}/**/.decision-log.md`
- `{learning_artifacts}/**/.learning-log.md`

## Extract for each source

- source ID
- source name
- source type
- access method
- related KPI(s)
- required fields
- expected grain
- expected freshness
- validation priority
- known risks

## Validate minimum source definition

A source is minimally defined only if it has:
- source ID
- source name
- source type
- expected role
- access method hypothesis
- related KPI or product requirement

If missing, stop and trigger `HALT-04`.

## Update report

Append source context summary to `source-validation-report.md`.

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-source-context