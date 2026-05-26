# Step 06 — Business Rule Gate

## Mandatory Rules

- Stop at this gate.
- Business rules must be approved by user.
- Business rules must have owner/change process.
- Do not hide thresholds, mappings, or classification logic.

## Task

Run Transformation Rule / Business Rule Gate.

## Required table

| Rule ID | Rule Name | Rule Type | Related KPI | Owner | Change Process | Risk |
|---|---|---|---|---|---|---|

## Options

A. Approve business rules as documented  
B. Approve with caveats  
C. Revise specific rules  
D. Defer specific rules  
E. Return to KPI/source validation  

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record

Update:
- business-rule-catalog.md
- transformation-design.md
- transformation-decision-record.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-19-transformation-rule:
    status: approved / approved-with-caveats / blocked
```

## Continue checkpoint

Ask:

`[C] Continue to finalize transformation design`
