# Step 02 — Load Serving and Data Context

## Mandatory Rules

- Review actual served assets and datasets.
- Do not assume data is public/non-sensitive.

## Task

Extract governance/security context.

## Extract

From serving spec:
- consumers
- assets
- serving modes
- external/internal exposure
- trust limitations

From data model:
- fields
- Gold/Silver assets
- possible sensitive fields

From source validation:
- source type
- provider
- license/usage notes
- privacy risk

From DQ/governance caveats:
- known risks
- quality limitations

## Update

Update:
- governance-security-review.md
- access-control-matrix.md

## Continue checkpoint

Ask:

`[C] Continue to privacy posture gate`
