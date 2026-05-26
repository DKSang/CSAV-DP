# Step 05 — Lineage, Metadata, and Auditability

## Mandatory Rules

- Lineage depth must match trust expectation.
- Metadata requirements must carry into implementation stories.
- Auditability cannot be only prose; specify what must be logged/tracked.

## Task

Define lineage, metadata, and auditability.

## Decide lineage depth

A. Minimal lineage  
B. Operational lineage  
C. Full audit lineage  
D. Custom lineage by asset  

Ask user if trust expectation is B/C/D.

## Required audit trail

Specify whether these must be auditable:

- source input
- source schema
- ingestion run
- transformation run
- DQ result
- metric version
- caveat version
- access decision
- serving release

## Update

Update:
- governance-security-review.md
- governance-decision-record.md

## Continue checkpoint

Ask:

`[C] Continue to finalize governance security design`
