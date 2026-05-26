# Model Grain Rubric

## Model grain definition

A model grain answers:

What does one row represent?

Examples:
- one row per ward per day
- one row per customer per month
- one row per source event
- one row per station per hour
- one row per product per store per day

## Good grain

A good grain is:
- explicit
- testable
- linked to keys
- compatible with KPI/serving needs
- documented in model spec

## Bad grain

A bad grain is:
- implicit
- mixed in one model
- changed without documentation
- not testable with uniqueness rules

## Grain decision options

A. One grain per model  
B. Multiple models for multiple grains  
C. Bridge table between grains  
D. Aggregate to serving grain in Gold  
E. Return to transformation design
