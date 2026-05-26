# Step 04 — Release Risk Review

## Mandatory Rules

- Classify release risks honestly.
- Critical risk blocks release.
- High risk requires explicit user acceptance.

## Task

Review release risks.

## Risk categories

- data correctness
- KPI correctness
- source reliability
- freshness
- DQ
- serving
- privacy/security
- operational readiness
- documentation/trust

## Required table

| Risk ID | Severity | Risk | Mitigation | Release Impact |
|---|---|---|---|---|

## Rollback/recovery

Define:
- rollback trigger
- recovery path
- backfill/replay notes
- communication notes

## Update

Update:
- release-readiness-report.md
- release-notes.md

## Continue checkpoint

Ask:

`[C] Continue to release readiness gate`
