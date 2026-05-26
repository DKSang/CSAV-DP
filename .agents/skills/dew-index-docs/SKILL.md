---
name: dew-index-docs
description: 'Generates or updates an index.md to reference all docs in a target folder.'
---

# DEW Index Docs

**Goal:** Generate or update an `index.md` to reference all docs in a target folder.

## Execution

### Step 1 — Scan Directory

- List all files and subdirectories in the target location.
- Skip hidden files unless the user explicitly asks to include them.
- HALT if the target directory does not exist or is inaccessible.

### Step 2 — Group Content

- Organize files by type, purpose, or subdirectory.
- For DEW projects, prefer these groups when applicable:
  - planning artifacts
  - implementation artifacts
  - evidence artifacts
  - learning artifacts
  - source docs
  - runbooks

### Step 3 — Generate Descriptions

- Read each file enough to understand its actual purpose.
- Create brief 3-10 word descriptions based on content, not just filename.
- Do not guess when the content is unavailable; mark as `description unavailable`.

### Step 4 — Create or Update Index

Write `index.md` using relative links.

## Output Format

```markdown
# Directory Index

## Files

- **[filename.ext](./filename.ext)** - Brief description

## Subdirectories

### subfolder/

- **[file1.ext](./subfolder/file1.ext)** - Brief description
```

## Validation

- Use relative paths starting with `./`.
- Group similar files together.
- Sort alphabetically within groups.
- Keep descriptions concise but informative.

## HALT Conditions

- HALT if target directory does not exist or is inaccessible.
- HALT if write permissions are unavailable.
