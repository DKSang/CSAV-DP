# Implementation Task Rubric

## Foundation story

Must usually include:
- project folders
- config files
- README/run guide
- evidence folder
- environment instructions

## Source access story

Must usually include:
- source access code/script/notebook
- access log
- error handling
- sample output

## Bronze ingestion story

Must usually include:
- ingestion script/notebook
- raw/bronze output
- metadata fields
- run log
- row count
- schema snapshot

## Source contract story

Must usually include:
- required field tests
- schema drift test
- row count test
- freshness test if applicable
- contract test result

## Silver transformation story

Must usually include:
- transformation code
- DQ checks
- output dataset
- invalid/quarantine handling
- validation evidence

## Gold/KPI story

Must usually include:
- KPI computation code
- Gold model output
- KPI sample output
- grain validation
- DQ evidence

## Serving story

Must usually include:
- dashboard/API/report/app artifact
- metric contract reference
- trust statement display/reference
- freshness/caveat display if relevant

## DataOps story

Must usually include:
- runbook update
- observability output
- monitoring/logging code or plan
- incident/backfill instruction
