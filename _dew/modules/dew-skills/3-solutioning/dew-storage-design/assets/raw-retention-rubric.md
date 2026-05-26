# Raw Retention Rubric

## Keep all raw inputs

Use when:
- reproducibility matters
- source may change
- auditability matters
- storage cost is acceptable

## Keep raw inputs for MVP period only

Use when:
- storage cost matters
- project is still experimental
- reproducibility is needed only during build phase

## Keep raw samples and schema snapshots only

Use when:
- source is large
- raw data is externally available
- source can be re-pulled
- project is learning-focused

## Keep raw externally and store references

Use when:
- source has stable URLs/object references
- copying data is unnecessary or restricted

## No raw retention

Use only with explicit caveat.

Risk:
- weak reproducibility
- harder debugging
- harder backfill