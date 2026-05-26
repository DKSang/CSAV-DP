# DQ Gate Policy Template

```markdown
# DQ Gate Policy

## Purpose

Define how DQ failures affect pipeline progression and serving.

## Policy Table

| Severity | Action | Pipeline Continues? | Data Served? | User Approval Required? |
|---|---|---|---|---|
| Critical | fail | No | No | Yes |
| High | fail/quarantine | Maybe | No unless caveated | Yes |
| Medium | warn/caveat | Yes | Yes with caveat | Maybe |
| Low | log | Yes | Yes | No |

## Layer Policy

### Source / Ingestion

### Silver

### Gold

### Serving

## Evidence Policy

Every DQ run must produce:
- timestamp
- dataset
- rule IDs
- pass/fail counts
- failed records location if applicable
- caveats
```
