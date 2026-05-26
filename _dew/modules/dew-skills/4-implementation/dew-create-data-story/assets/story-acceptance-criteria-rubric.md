# Story Acceptance Criteria Rubric

Good acceptance criteria are:

- specific
- testable
- tied to data output
- tied to evidence
- tied to design artifact
- not vague

## Bad

- Pipeline works.
- Data is clean.
- Dashboard looks good.

## Good

- Given source sample SRC-001 exists, when ingestion runs, then a Bronze file/table is created at the target path with required metadata fields.
- Given Bronze dataset exists, when Silver transformation runs, then required fields are cast to approved types and invalid rows are quarantined.
- Given Gold model exists, when KPI validation runs, then KPI output matches expected grain and DQ evidence is written.
