# Step 05 — Trust, Limitations, and Feedback

## Mandatory Rules

- Stop if trust statement is missing.
- Limitations must be shown to consumers.
- Accepted caveats are not evidence.
- Feedback loop must exist.

## Task

Create trust and limitations statement.

## Required sections

- intended use
- not intended for
- trust expectation
- source caveats
- KPI caveats
- freshness caveats
- grain caveats
- DQ caveats
- known missing coverage
- user responsibilities
- issue reporting

## Gate

Ask user to approve trust/limitations statement:

A. Approve  
B. Approve with caveats  
C. Revise limitations  
D. Return to DQ/model design  

Do not continue until user chooses.

## Record

Update:
- trust-and-limitations-statement.md
- serving-data-product-spec.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-serving-trust-limitations:
    status: approved / approved-with-caveats / blocked
```

## Continue checkpoint

Ask:

`[C] Continue to finalize serving design`
