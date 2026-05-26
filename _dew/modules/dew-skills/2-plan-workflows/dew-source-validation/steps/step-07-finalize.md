# Step 07 — Finalize Source Validation Report

## Mandatory Rules

- Do not finalize if validation-first P1 source lacks access/sample/schema evidence unless user explicitly approved caveated continuation.
- Do not mark architecture ready unless source trust gate is approved or approved-with-caveats.
- Evidence must be indexed if it exists.

## Task

Finalize source validation report.

## Checklist

Run `checklist.md`.

## Required final outputs

- source-validation-report.md
- source sample notes
- schema snapshot notes
- source profile notes
- decision log entry
- learning log entry
- evidence index update if evidence exists

## Architecture readiness status

Choose one:

A. Architecture can proceed after requirement gate  
B. Architecture can proceed with source caveats after requirement gate  
C. Architecture cannot proceed; source validation unresolved  
D. Reduce MVP scope  

## Final status

Set report frontmatter:

```yaml
status: final
updated: {date}
stepsCompleted:
  - step-01-init
  - step-02-load-source-context
  - step-03-access-check
  - step-04-sample-and-schema
  - step-05-grain-freshness-profile
  - step-06-source-trust-gate
  - step-07-finalize