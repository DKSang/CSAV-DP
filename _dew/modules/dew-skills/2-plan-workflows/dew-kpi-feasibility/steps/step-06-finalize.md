# Step 06 — Finalize KPI Feasibility Report

## Mandatory Rules

- Do not finalize if primary KPI status is still Hypothesis only unless user explicitly approved caveated continuation.
- Do not mark architecture ready unless KPI feasibility gate is approved or approved-with-caveats.
- Evidence must be indexed if it exists.

## Task

Finalize KPI feasibility report.

## Checklist

Run `checklist.md`.

## Required final outputs

- `kpi-feasibility-report.md`
- `field-availability.md`
- `sample-computation-plan.md`
- decision log entry
- learning log entry
- evidence index update if evidence exists

## Architecture readiness status

Choose one:

A. Architecture can proceed after source validation  
B. Architecture can proceed with KPI caveats after source validation  
C. Architecture cannot proceed; KPI feasibility unresolved  
D. Reduce MVP scope  

## Final status

Set report frontmatter:

```yaml
status: final
updated: {date}
stepsCompleted:
  - step-01-init
  - step-02-load-kpi-context
  - step-03-field-availability
  - step-04-computation-plan
  - step-05-feasibility-gate
  - step-06-finalize