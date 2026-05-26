# Step 02 — Load Validated Context

## Mandatory Rules

- Load all prior validated artifacts before judging readiness.
- Do not treat missing artifacts as completed.
- Do not treat caveats as evidence.
- If KPI feasibility report is missing, trigger `HALT-03`.
- If source validation report is missing, trigger `HALT-06` or `HALT-18`.

## Task

Load and summarize all required prior artifacts.

## Input discovery

Search for:

- `{planning_artifacts}/**/brief.md`
- `{planning_artifacts}/**/business-discovery.md`
- `{planning_artifacts}/**/data-product-prd.md`
- `{planning_artifacts}/**/kpi-catalog.md`
- `{planning_artifacts}/**/kpi-source-matrix.md`
- `{planning_artifacts}/**/kpi-feasibility-report.md`
- `{planning_artifacts}/**/source-inventory.md`
- `{planning_artifacts}/**/source-scorecard.md`
- `{planning_artifacts}/**/source-validation-report.md`
- `{evidence_artifacts}/**/validation-evidence-index.md`
- `{planning_artifacts}/**/.decision-log.md`
- `{learning_artifacts}/**/.learning-log.md`

## Extract

Extract:

### Business
- data consumer
- decision supported
- data product type
- MVP scope

### KPI
- primary KPI list
- feasibility status
- unresolved KPI blockers
- KPI caveats

### Source
- validation-first source list
- P1/P2/exploration/rejected/block status
- source evidence
- unresolved source blockers
- source caveats

### Evidence
- KPI evidence
- source evidence
- missing evidence
- stale/invalid evidence if any

## Update report

Append input artifact table and executive readiness summary.

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context