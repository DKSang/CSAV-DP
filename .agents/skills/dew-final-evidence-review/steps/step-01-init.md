# Step 01 — Final Evidence Review Initialization

## Mandatory Rules

- Do not review release readiness before E2E validation exists.
- Do not treat missing evidence as acceptable without caveat.

## Task

Initialize final evidence review.

## Sequence

1. Detect existing final evidence review.
2. Validate prerequisite:
   - e2e-validation-report.md
   - validation-evidence-index.md

If missing:
- E2E missing → return to `dew-e2e-validation`
- evidence missing → `HALT-18`

3. Create workspace:

`{workflow.evidence_review_output_path}/{workflow.run_folder_pattern}/`

Create:
- `final-evidence-review.md`
- `evidence-coverage-matrix.md`

4. Initialize frontmatter.

5. Continue checkpoint:

`[C] Continue to load evidence index`
