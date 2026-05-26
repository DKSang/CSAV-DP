# Step 06 — Scope and Caveat Resolution

## Mandatory Rules

- Caveats must be explicit.
- High severity caveats must be accepted by the user or block the gate.
- User-approved caveats are not evidence.
- Every caveat needs downstream impact and revisit trigger.

## Task

Resolve caveats and MVP scope before architecture.

## Build Caveat Register

For each caveat, capture:

| Caveat ID | Area | Description | Severity | Accepted? | Downstream Impact | Revisit Trigger |
|---|---|---|---|---|---|---|

## Severity

### High

Blocks architecture unless accepted explicitly.

Examples:
- primary KPI not sample-verified
- P1 source lacks schema evidence
- source grain unknown
- freshness unknown for decision-critical output
- privacy/security unresolved

### Medium

Can proceed with caveat if documented.

Examples:
- limited sample size
- field meaning needs owner confirmation
- source update pattern not formally guaranteed

### Low

Documentation or minor uncertainty.

## Scope options

If caveats are too severe, present options:

A. Keep current MVP with caveats  
B. Reduce MVP scope  
C. Defer unresolved KPI/source  
D. Return to validation  
E. Stop architecture readiness  

Ask user to choose if any High caveat exists.

## Update report

Update:
- Caveat Register
- MVP scope impact
- Architecture readiness matrix

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context
  - step-03-kpi-readiness-review
  - step-04-source-readiness-review
  - step-05-trust-grain-freshness-gates
  - step-06-scope-caveat-resolution