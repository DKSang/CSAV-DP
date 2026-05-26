# Step 04 — DQ Rule Gate

## Mandatory Rules

- Stop at this gate.
- User must approve minimum DQ rule set.
- DQ rules must match trust expectation.
- If rules are missing, trigger HALT-14.

## Task

Run GATE-18 — Data Quality Rule Gate.

## Options

A. Approve minimum DQ rules  
B. Approve with caveats  
C. Add stricter DQ rules  
D. Reduce DQ scope for MVP  
E. Return to model/transformation design  

## Required summary

| Area | Minimum Rules | Risk if Missing | Recommendation |
|---|---|---|---|
| Source | | | |
| Silver | | | |
| Gold | | | |
| Serving | | | |

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record

Update:
- dq-rule-catalog.md
- data-quality-rules.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-18-data-quality-rule:
    status: approved / approved-with-caveats / blocked
```

## Continue checkpoint

Ask:

`[C] Continue to severity and action policy`
