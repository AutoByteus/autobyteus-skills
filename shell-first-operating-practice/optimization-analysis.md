# Shell-First Operating Practice — File Read / Write / Edit Coverage Analysis

Review Status: Implementation complete - validation passed
Review date: analysis only

## User request and review scope

The user asked me to review the **Daily Assistant** agent's attached skill, `shell-first-operating-practice`, and determine whether — as a shell-first skill — it gives the agent clear guidance on the three core file operations:

1. **Read file** — reading a file, including specific line regions.
2. **Write file** — creating/writing a new file.
3. **Edit file** — modifying an existing file.

**Corrected intent (per user clarification):** *All* file operations are shell-first — read, write, **and edit**. The dedicated `edit_file` tool is used **only** when shell cannot achieve a file edit (i.e., there is no clean shell method for that particular edit). It is a fallback, not the primary path for edits.

Scope:

- Target skill: `autobyteus-skills/shell-first-operating-practice/SKILL.md` (single-file package; no references, scripts, or assets).
- Consumer agent: `autobyteus-agents/agents/daily-assistant/agent.md` + `agent-config.json` (attaches `shell-first-operating-practice`).

This is an analysis-only pass. No authoritative runtime file has been edited.

## Current behavior and package/file ownership baseline

- `shell-first-operating-practice/SKILL.md` is a single-file skill (261 lines). It owns the reusable shell-first operating procedure: orientation, inspection, search, planning, bounded command execution, editing, filesystem operations, processes, network, Git, project runtimes, verification, and anti-patterns.
- The Daily Assistant agent bundles only this skill (`skillNames: ["shell-first-operating-practice"]`) and exposes a broad tool surface including `run_bash`, `read_file`, `write_file`, and `edit_file`, plus browser, media, image, and speech tools.
- The skill's tool-routing statement is the General Operating Rules line: *"For repository and text-file work, prefer the shell tool over dedicated file tools when both are available."* This **already expresses the shell-first-for-edit principle** (including for edits): shell is preferred, and the dedicated tool is the fallback when shell is not available or not the right tool.

## Preserved behavioral invariants and boundaries

Any approved optimization must preserve:

- The shell-first bias for **all** file operations, including edits (shell as primary operating interface, not shell-only).
- Bounded, deterministic, non-interactive command use.
- Precise search and line-region reads (`sed -n`, `nl -ba`).
- Parse-aware handling of structured data (`jq`, `python3`, `yq`).
- Preservation of unrelated user work, no blind overwrites, no destructive actions without approval.
- The existing `edit-method selection order` table (which is a shell-based edit path) and verification rules.
- `edit_file` used only as a fallback when shell cannot achieve the edit.
- The agent's configured tool surface in `agent-config.json` (unchanged).

## Macro analysis

### Package structure and ownership

The package is coherent: one skill file, one consumer wrapper, one config. File-operation guidance is owned solely by `shell-first-operating-practice`. No ownership split or duplication exists inside the skill. The area for review is coverage, not ownership.

### Content architecture and logical flow

File operations are distributed across three sections:

- **Read** → `File Inspection` (lines 144-152) and `Command Families` (line 110).
- **Write/create** → implied inside `Editing And Generation` (heredoc full-file generation, `cat >>` append) and `Filesystem Operations` (`mkdir -p`, `cp`).
- **Edit** → `Editing And Generation` (lines 172-194) as a **shell-based edit path**, plus the tool-routing line at line 73.

The flow is readable. The one structural point to make explicit is that **edit is itself shell-first**, with the dedicated `edit_file` tool as a documented fallback. The current skill is mostly aligned with this but does not state the fallback explicitly.

## Micro analysis

### Reading files — Covered

The skill already answers the read-file questions well:

- Specific line regions: `sed -n '40,120p' path/to/file` (line 147) and `nl -ba path/to/file | sed -n '40,120p'` when line numbers matter (line 148).
- Size-before-read: `wc -l path/to/file` (line 146).
- Bounded previews: `head -80` / `tail -80` (line 149).
- `cat` guard: *"Do not use `cat` on large files. Check size first or read a range."* (line 254).
- Type detection, JSON inspection, and JSON validation (lines 150-152).

**Disposition: Keep.** Reading is fully shell-first and complete. No change needed.

### Writing / creating files — Partially covered

The skill covers generating content through heredocs and `cat`:

- `Append-only content` → quoted heredoc with `cat >>` (line 184).
- `Full generated file` → heredoc or `python3`, preferably through a temp file (line 186).
- Write-through-temp-file rule (line 194).

**Gap:** There is no explicit "create a new file" bullet that states a brand-new file is written with a heredoc redirect (`cat > "path" <<'EOF' ... EOF`). New-file creation is only implied by the "full generated file" heredoc row. This is shell-first already; it just is not stated as a distinct operation.

**Disposition: Add (minor).** Add one explicit "create a new file" row to the edit-method table (heredoc `cat >` for a new file, `cat >>` for append). This is a small, behavior-preserving clarity addition that keeps the shell-first path explicit.

### Editing files — Correctly shell-first; only needs an explicit fallback statement

The skill provides a strong **shell-based** edit-method selection order (lines 172-194): locate, single literal substitution (`perl -0pi -e`), stream rewrite (`sed` to temp), field/column rewrite (`awk` to temp), structured data (`jq`/`python3`), multi-line block, append, anchor insert, full-file heredoc.

Line 73 already sets the shell-first-for-edit default: *"prefer the shell tool over dedicated file tools when both are available."* Under the corrected interpretation, this is exactly right — even edits go through shell first.

**Small gap (clarification, not a reversal):** The skill never explicitly states the fallback condition — that when shell cannot achieve a file edit (no clean shell method for that edit), the dedicated `edit_file` tool is the correct interface. The user's stated intent is: *"even edit file is shell first. And only one — shell cannot achieve the file edit, for example — then go use the edit file tool."* This makes `edit_file` the documented fallback.

**Disposition: Add (minor, normative clarification).** Add one short rule stating that edits are shell-first, and use the dedicated `edit_file` tool only when shell cannot achieve the edit. This is a clarity addition that makes the existing implied behavior explicit. It does **not** reverse the shell-first bias — it confirms it.

## Findings and evidence summary

### Coverage verdict

| Operation | Status | Evidence |
| --- | --- | --- |
| Read file (incl. line regions) | **Covered** | `File Inspection` lines 146-152; `sed -n`/`nl -ba` line-region reads; `wc -l` size gate; `cat` guard at line 254. |
| Write / create new file | **Partially covered** | Heredoc full-file generation (line 186) and `cat >>` append (line 184) exist; shell-first already, but no explicit "create a new file" operation. |
| Edit existing file | **Correctly shell-first; fallback implicit** | Strong shell edit table (lines 172-194) and line 73 shell-first routing; but the `edit_file`=fallback condition is never stated explicitly. |

### Macro findings

- **Keep — package/ownership:** single-owner skill, no structural duplication to repair.
- **Coverage gap — write:** new-file creation is only implied, not a distinct operation (still shell-first).
- **Clarification — edit:** the skill is correctly shell-first for edits; it only needs one explicit statement that `edit_file` is the fallback when shell cannot achieve the edit.

### Micro findings

- Reading instructions are complete; no change needed.
- One explicit "create a new file" row would close the write gap with minimal cost.
- One explicit `edit_file`-as-fallback sentence would make the intended edit routing unambiguous.

## Proposed improvements (awaiting approval)

Ordered macro first, then micro. All are limited to `shell-first-operating-practice/SKILL.md`.

1. **Add (micro) — `Editing And Generation` table:** add a `New file` row using a quoted heredoc with `cat > "path" <<'EOF'`, keeping the existing `Append-only content` `cat >>` row. This makes "create a new file" an explicit, shell-first operation.
2. **Add (micro) — edit fallback clarification:** add one short sentence that edits are shell-first and the dedicated `edit_file` tool is used only when shell cannot achieve the edit. This is a clarity addition consistent with the existing line-73 bias; it does not change behavior.
3. **Keep — reading guidance:** no change; reading (including line regions) is already well covered.

### Explicit dispositions

- Reading instructions: **Keep**.
- New-file creation wording: **Add** (one table row).
- Edit fallback statement (`edit_file` used only when shell cannot achieve the edit): **Add** as a normative clarification — consistent with existing shell-first behavior, so it does not reverse anything.

## Assumptions, open questions, risks, and validation plan

### Assumptions

- The user's clarified intent — file operations (read/write/edit) are all shell-first, and `edit_file` is only the fallback when shell cannot achieve the edit — is authoritative.
- The dedicated tools (`read_file`, `write_file`, `edit_file`) remain exposed in `agent-config.json`.
- The shell-first bias remains the default for all file operations, including edits.

### Open questions

- None blocking. The two proposed additions are clarity improvements consistent with the existing shell-first behavior, so they do not require a behavior reversal.

### Risks

- Adding new wording must not be misread as advising `edit_file` as the primary edit path. The new sentence must keep shell-first as the default and present `edit_file` strictly as the fallback for edits shell cannot perform.
- Over-naming tools could reduce portability across runtimes that use different tool names; the skill already guards this by saying "if the shell tool has another name, use the runtime's equivalent."

### Validation plan

- Re-read the edited `SKILL.md` sections in order to confirm flow.
- `git diff --check` and trailing-whitespace check on the changed file.
- Confirm the skill frontmatter and name are unchanged.

## Target skill files changed during analysis: None

## Implementation record

Approved by the user. Applied to `shell-first-operating-practice/SKILL.md`:

1. Added a `New file` row to the `Editing And Generation` selection-order table: quoted heredoc with `cat > "path" <<'EOF'`, keeping the existing append-only `cat >>` row.
2. Added one rule to the `Editing And Generation` rules list: "Edits are shell-first: prefer the shell edit methods above, and use the dedicated `edit_file` tool only when the shell cannot achieve the edit."

Both are clarity additions consistent with the existing shell-first behavior. No behavior was reversed; the `edit_file` tool remains a documented fallback for edits the shell cannot perform.

### Validation performed

- Re-read the edited `Editing And Generation` section; flow and table structure intact.
- `git diff --check` and trailing-whitespace check on `SKILL.md`: passed.
- Skill frontmatter and name unchanged: `shell-first-operating-practice`.

## Analysis artifact

`autobyteus-skills/shell-first-operating-practice/optimization-analysis.md`
## Structural and content-flow review (optimizer macro pass)

The user asked whether I had used the optimizer skill to examine the skill's overall structure and content flow, beyond the file-operation scope. The honest answer: the initial passes were scoped to read/write/edit coverage only. This section records the full optimizer macro audit of the skill as a whole.

### Skill section map (current)

```
Purpose (scope/audience)
→ Entry Procedure (prereqs)
→ Core Task Loop (general workflow)
→ Preamble + Communication + Planning (soft behavior)
→ General Operating Rules
→ Shell-First Operating Loop
→ Operating Rules
→ Command Families (reference table)
→ Orientation / Search / File Inspection / Text Processing / Structured Data
→ Editing / Filesystem / Processes / Network / Archives / Git / Project
→ Verification
→ Anti-Patterns
```

### Structural findings

- **S-1 — Two competing task loops (Medium).** `Core Task Loop` (8 steps) and `Shell-First Operating Loop` (7 steps) both describe the same observe→plan→execute→verify→report arc. The prior wrapper analysis deliberately kept one general + one shell loop, but the overlap is high; this is an ownership/boundary question.
- **S-2 — Two "Rules" sections with indistinguishable names (Medium).** `General Operating Rules` and `Operating Rules` both hold imperative rules; the split criterion is never stated.
- **S-3 — Orientation guidance fragmented (Low/Medium).** `pwd`-first, repo-root, and `git status --short` each appear in both `Entry Procedure` and `Orientation`.
- **S-4 — Verification/reporting repeated (Low).** The verify step appears in both loops, `General Operating Rules`, and the `Verification` section; reporting appears in both loops and `Communication`.
- **S-5 — Anti-Patterns duplicates earlier negatives (Low).** Each duplicate should be justified by a distinct boundary (e.g., `cat`-on-large-files, unquoted paths, broad dumps).
- **S-6 — Command Families table (Keep).** Strong reference spine that the domain sections expand; preserve.

### Content-flow verdict

The flows that matter (read/write/edit) are clear after the implemented additions. The macro issue is structural redundancy between the two loops and the two rules sections — an ownership/boundary problem, not a wording problem.

### Disposition (awaiting approval)

- S-1, S-2, S-3, S-5: candidates for a merge/restructure pass. Do not edit without explicit approval.
- S-6: Keep.

Review Status note: this structural review is analysis-only. No files were changed for this section.
