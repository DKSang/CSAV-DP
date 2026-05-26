# Step 03 — Serving Mode Gate

## Mandatory Rules

- Stop at this gate.
- User must approve serving mode.
- Do not choose dashboard/API/mart silently.
- Serving mode must match consumer and trust expectation.

## Options

A. Dashboard  
B. Gold data mart  
C. API  
D. Notebook/report  
E. Web app feature  
F. ML feature table  
G. Reverse ETL output  

## Required comparison table

| Option | Fit | Pros | Cons | Risk | Required Governance |
|---|---|---|---|---|---|

## Recommendation

Recommend one or more modes.

## User decision

Ask user to choose.

Do not continue until user chooses.

## Record

Update:
- serving-data-product-spec.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-20-serving-mode:
    status: approved / approved-with-caveats
```

## Continue checkpoint

Ask:

`[C] Continue to metric contract and consumer experience`
