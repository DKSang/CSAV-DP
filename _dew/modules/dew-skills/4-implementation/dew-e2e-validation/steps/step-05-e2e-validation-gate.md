# Step 05 — E2E Validation Gate

## Mandatory Rules

- Stop at this gate.
- User must approve E2E validation result.
- Critical finding blocks release.
- Missing E2E evidence blocks release.

## Decision options

A. E2E pass  
B. E2E pass with caveats  
C. Return to implementation  
D. Block release  

## Required summary

| Area | Status | Finding | Release Impact |
|---|---|---|---|

## Recommendation

Recommend one option.

## User decision

Ask user to choose A/B/C/D.

Do not continue until user chooses.

## Record

Update:
- e2e-validation-report.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-25-e2e-validation:
    status: approved / approved-with-caveats / blocked
```

## Continue checkpoint

Ask:

`[C] Continue to finalize E2E validation`
