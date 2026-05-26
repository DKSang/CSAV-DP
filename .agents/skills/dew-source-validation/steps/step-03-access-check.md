# Step 03 — Source Access Check

## Mandatory Rules

- Do not assume access works.
- If access cannot be tested, mark as Unknown or Blocked.
- A source cannot become P1 without access evidence or explicit caveated user approval.

## Task

Validate or document access for each validation-first source.

## Access evidence types

Allowed evidence:
- successful API call log
- downloaded file path
- database query log
- manual file sample
- web page capture/extraction notes
- owner confirmation
- documented access limitation

## For each source

Record:

| Source ID | Access Method | Access Status | Evidence | Notes |
|---|---|---|---|---|

Access status:
- Verified
- Failed
- Blocked
- Manual only
- Unknown

## If access is missing

Trigger:

`HALT-05 — Source Access Not Verified`

Options:
A. Run access check now  
B. Continue with caveat  
C. Mark source as blocked  
D. Reject source  

## Update report

Update `source-validation-report.md`.

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-source-context
  - step-03-access-check