# Step 04 — Source Readiness Review

## Mandatory Rules

- Do not mark a source ready without validation status.
- Do not treat candidate source as P1.
- P1 source cannot lack access/sample/schema evidence unless user explicitly accepts caveat.
- Missing source evidence triggers `HALT-06` or `HALT-18`.

## Task

Review whether source requirements are ready for architecture.

## For each source needed by MVP

Review:

| Source ID | Source Name | Validation Status | Evidence | Caveat | Architecture Impact |
|---|---|---|---|---|---|

## Required source evidence for P1

- access check
- sample
- schema snapshot
- grain assessment
- freshness assessment
- field coverage
- DQ/profile notes or caveat
- source trust decision

## Allowed source readiness statuses

- Ready
- Ready with caveats
- Blocked
- Deferred
- Rejected
- Exploration only

## If P1 source is blocked

Trigger:

`HALT-06 — Source Trust Not Established`

Options:
A. Return to source validation  
B. Continue with caveat  
C. Defer source  
D. Reduce MVP scope  

## Update report

Update Source Readiness section.

Update caveat register if caveats exist.

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context
  - step-03-kpi-readiness-review
  - step-04-source-readiness-review