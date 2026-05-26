# Cross-Link Validation Rubric

## Valid link

A `preceded-by` or `followed-by` value is valid when:
- the referenced skill exists in module-help.csv
- the referenced skill folder exists
- the workflow order makes sense
- the output of previous skill is input of next skill

## Broken link

A link is broken when:
- skill name typo
- referenced skill not listed
- referenced folder missing
- workflow loops unintentionally
- output/input mismatch

## Suspicious link

A link is suspicious when:
- optional skill blocks required skill
- implementation skill depends on documentation skill too early
- phase order is wrong
- output artifact is not defined
