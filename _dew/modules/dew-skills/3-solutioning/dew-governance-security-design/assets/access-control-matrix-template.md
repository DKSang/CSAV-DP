# Access Control Matrix Template

```markdown
# Access Control Matrix

## Purpose

Define who can access which data product assets.

## Matrix

| Role / User Group | Asset | Access Level | Purpose | Approval Needed? | Notes |
|---|---|---|---|---|---|
| Analyst | gold_mart | read | analysis | Yes/No | |
| Farmer/User | web app feature | view only | advisory | Yes/No | |
| Data Engineer | pipeline/logs | admin/write | operations | Yes | |

## Access Levels

- none
- view
- read
- write
- admin
- owner

## Asset Types

- raw/bronze data
- silver data
- gold data
- dashboard
- API
- web app feature
- logs
- DQ results
- evidence artifacts
- decision logs

## Caveats
```
