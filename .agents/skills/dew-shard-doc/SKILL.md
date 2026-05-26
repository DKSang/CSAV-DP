---
name: dew-shard-doc
description: 'Splits large markdown documents into smaller organized files based on heading sections.'
---

# DEW Shard Document

**Goal:** Split large markdown documents into smaller organized files based on heading sections.

## Critical Rules

- Execute steps in order.
- Do not shard non-markdown files.
- Preserve the original document unless the user explicitly asks for archival cleanup.
- HALT immediately when halt conditions are met.

## Execution

### Step 1 — Get Source Document

- Ask for the source document path if not provided.
- Verify the file exists and is accessible.
- Verify it has `.md` extension.
- If not found or not markdown: HALT.

### Step 2 — Get Destination Folder

- Default destination: same location as source file, folder named after source file without `.md`.
- Ask user to confirm default or provide custom destination.
- Verify destination exists or can be created.
- Check write permissions.

### Step 3 — Execute Sharding

Preferred command when available:

```bash
npx @kayvan/markdown-tree-parser explode <source-document> <destination-folder>
```

If the command is unavailable, fall back to manual sharding by level 2 headings.

### Step 4 — Verify Output

- Check destination folder contains sharded files.
- Check `index.md` exists or create it.
- Count files created.
- HALT if no files were created.

### Step 5 — Report Completion

Report source path, destination path, number of files created, whether `index.md` was created, and warnings or caveats.

## HALT Conditions

- HALT if source file is missing.
- HALT if source is not markdown.
- HALT if destination cannot be written.
- HALT if sharding produces no files.
