# Step 06 — History and Bridge Design

## Mandatory Rules

- Do not choose SCD/history pattern silently.
- Bridge assumptions must be explicit.
- User must approve history/bridge design if it affects KPI semantics.

## Task

Define:
- dimensions
- facts
- bridges
- history/SCD strategy

## History options

A. No history  
B. Type 1 overwrite  
C. Type 2 history  
D. Snapshot history  
E. Event history  

Ask user if history impacts KPI or serving trust.

## Bridge options

A. No bridge required  
B. Static bridge table  
C. Time-aware bridge table  
D. Rule-derived bridge  
E. Return to transformation design  

Ask user if bridge affects KPI semantics.

## Update

Update:
- data-model-spec.md
- .decision-log.md
- .learning-log.md if enabled

## Continue checkpoint

Ask:

`[C] Continue to finalize data model design`
