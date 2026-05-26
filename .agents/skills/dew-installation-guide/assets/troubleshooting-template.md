# Troubleshooting Template

```markdown
# DEW Troubleshooting

## Common Issue: Skill cannot find artifact

### Symptom

### Cause

### Fix

- Check artifact path.
- Check config variables.
- Check previous skill output.

## Common Issue: HALT triggered

### Symptom

Skill stops with HALT.

### Fix

- Read HALT reason.
- Resolve missing decision/evidence/artifact.
- Re-run or continue from checkpoint.

## Common Issue: Missing source evidence

### Fix

Run:
- dew-source-access-check
- dew-source-sampler
- dew-source-contract-test

## Common Issue: KPI not feasible

### Fix

Run:
- dew-kpi-feasibility
- dew-kpi-prototype
- dew-kpi-validation-review

## Common Issue: Story not ready-for-dev

### Fix

Run:
- dew-create-data-story
- dew-implementation-readiness-review

## Common Issue: Release blocked

### Fix

Run:
- dew-e2e-validation
- dew-final-evidence-review
- dew-release-readiness
```
