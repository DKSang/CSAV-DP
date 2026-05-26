# Step 04 — Run or Review E2E Validation

## Mandatory Rules

- Do not fabricate E2E results.
- If command cannot be run, document manual review path.
- If required evidence is missing, trigger HALT-18.

## Task

Execute or review E2E validation.

## If command exists

Run or instruct:

```bash
# project-specific E2E validation command
```

Record:

* command
* timestamp
* result
* output path
* failure logs

## If manual/hybrid

Review:

* source access evidence
* ingestion evidence
* transformation evidence
* DQ evidence
* serving evidence
* operational evidence

## Record findings

Classify:

* Critical
* High
* Medium
* Low

## Continue checkpoint

Ask:

`[C] Continue to E2E validation gate`
