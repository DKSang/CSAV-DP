# Story Evidence Requirements Rubric

Every data engineering story should produce evidence.

## Common evidence types

- run log
- row count summary
- schema snapshot
- source access log
- sample output
- DQ test result
- failed records output
- freshness report
- model validation report
- metric sample output
- screenshot/report export
- README/run instructions

## Evidence rule

If a story changes data, it must produce data evidence.

If a story changes a metric, it must produce metric evidence.

If a story changes serving, it must produce consumer-facing evidence.

If a story changes operations, it must produce runbook/monitoring evidence.
