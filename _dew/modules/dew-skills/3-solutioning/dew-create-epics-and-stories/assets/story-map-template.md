# Story Map Template

```markdown
# Story Map

## Purpose

This file maps story candidates to implementation order and dependencies.

## Story Map Table

| Story ID | Epic ID | Title | Layer | Depends On | Required Design Input | Evidence Required | Status |
|---|---|---|---|---|---|---|---|
| 1.1 | EPIC-01 | Initialize project structure | foundation | | dataops-runbook | setup evidence | backlog |

## Layer Order

Recommended order:

1. Foundation
2. Source access
3. Bronze ingestion
4. Source contract tests
5. Silver transformation
6. Gold model / KPI computation
7. DQ tests and evidence
8. Serving product
9. Governance documentation
10. DataOps / observability

## Dependency Notes

## Caveats Carried Into Stories
```
