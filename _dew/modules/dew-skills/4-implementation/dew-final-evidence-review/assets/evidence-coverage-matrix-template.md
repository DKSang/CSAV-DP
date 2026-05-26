# Evidence Coverage Matrix Template

```markdown
# Evidence Coverage Matrix

| Evidence Area | Required By | Expected Evidence | Actual Evidence | Valid? | Caveat |
|---|---|---|---|---|---|
| Source access | Story / E2E | access log | | Yes/No | |
| Bronze ingestion | Story / E2E | row count + run log | | | |
| Schema | Source contract | schema snapshot | | | |
| Silver | Transform story | output validation | | | |
| Gold/KPI | KPI story | metric output | | | |
| DQ | DQ rules | DQ results | | | |
| Serving | Serving story | screenshot/API/report | | | |
| Trust | Serving spec | trust statement | | | |
| DataOps | Runbook | logs/observability | | | |
| Learning | Completion | learning entry | | | |
```
