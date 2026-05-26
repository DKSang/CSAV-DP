# Release Decision Rubric

## A. Release

Use when:
- E2E validation passed
- evidence complete
- no critical/high blockers
- trust/governance/DataOps are ready
- user approves

## B. Release with caveats

Use when:
- E2E passed with caveats
- evidence gaps are medium/low
- caveats are documented
- user accepts limitations

## C. Do not release; return to implementation

Use when:
- code/story output incomplete
- evidence missing
- DQ failure exists
- serving output missing

## D. Do not release; return to design

Use when:
- issue comes from wrong requirement/KPI/source/model/design
- implementation cannot fix it safely

## E. Archive as learning/demo only

Use when:
- project produced learning value
- but is not trustworthy enough for data product release
