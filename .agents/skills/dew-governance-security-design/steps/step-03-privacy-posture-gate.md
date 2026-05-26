# Step 03 — Privacy Posture Gate

## Mandatory Rules

- Stop at this gate.
- User must approve privacy posture.
- If sensitivity is unknown, recommend blocking until reviewed.
- If privacy/security unreviewed, trigger HALT-16.

## Options

A. No sensitive data identified  
B. Low-risk internal data  
C. PII/sensitive data present with controls  
D. High-risk data requiring governance review  
E. Unknown; block until reviewed  

## Required table

| Asset | Sensitivity | Exposure | Risk | Recommendation |
|---|---|---|---|---|

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record

Update:
- governance-security-review.md
- governance-decision-record.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-21-privacy-posture:
    status: approved / approved-with-caveats / blocked
```

## Continue checkpoint

Ask:

`[C] Continue to access control and ownership`
