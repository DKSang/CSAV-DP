# Step 04 — Sample Computation Plan

## Mandatory Rules

- Do not mark KPI feasible before sample computation.
- Do not design production transformation here.
- The goal is proving feasibility on sample, not building the final pipeline.

## Task

Create a sample computation plan for each primary KPI.

## For each KPI

Define:

- prototype method: SQL / Python / notebook / manual / not possible yet
- input sample needed
- formula implementation
- target grain
- validation checks
- expected output columns
- evidence to produce

## Computation readiness

Classify each KPI:

- Ready for prototype
- Needs source sample
- Needs schema snapshot
- Needs field mapping
- Needs formula revision
- Not ready

## Required output

Update:

- `sample-computation-plan.md`
- `kpi-feasibility-report.md`

## Next implementation skill

If at least one KPI is ready for prototype, recommend:

`dew-kpi-prototype`

If no KPI is ready, trigger:

`HALT-03 — KPI Feasibility Not Proven`

## Update frontmatter

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-kpi-context
  - step-03-field-availability
  - step-04-computation-plan