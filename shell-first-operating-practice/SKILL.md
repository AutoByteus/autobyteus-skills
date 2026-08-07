---
name: shell-first-operating-practice
description: Foundational shell-first execution practice for agents. Use it alongside task-specific skills whenever work requires workspace, shell, repository, process, network, or project operations. It defines how to orient, inspect, search, edit, execute, automate, and verify system-level work; task-specific skills define the domain goal, decisions, artifacts, and quality gates.
---

# Shell-First Operating Practice

## Purpose

This is a foundational execution-layer skill. It does not define the business or domain task. Task-specific skills decide what the agent should accomplish and what outputs are required; this skill defines the fundamental system operations used to carry out that work safely and verify the result.

For example, a task-specific skill may define how to research a topic, implement a feature, or produce a domain artifact. Shell-First Operating Practice provides the underlying operations: locating files, reading content, editing files, running validators, and verifying changes.

Use the shell as a primary operating interface, not only as a file manager. Shell-first does not mean shell-only: use the runtime's specialized browser, media, or other tools when they are the correct interface for that part of the task.

This skill covers the Unix command-line style of working: orient yourself, inspect state, search precisely, compose small tools, transform streams, edit files, manage processes, inspect network resources, run project commands, and verify results.

Filesystem operations are one category inside this practice. The broader discipline is using shell commands to operate the whole working environment.

This skill assumes the agent has a shell execution tool such as `run_bash`. If the shell tool has another name, use the runtime's equivalent command-execution tool. If no shell execution tool is available, use the best available workspace-inspection method and do not pretend to perform shell-based work.

## Entry Procedure

- At the start of each task, establish the active workspace. When a shell or command-execution tool is available, the first tool action must run `pwd`.
- When working in a repository, identify the repo root when useful: `git rev-parse --show-toplevel 2>/dev/null || pwd`.
- Before editing repository files, check current changes with `git status --short`.
- For non-trivial work, decide the smallest useful action before changing files or starting processes.

## Operating Loop

After entry orientation, work iteratively from goal to verified result:

1. Orient: confirm workspace, repository root, branch, and relevant environment.
2. Understand the user's goal.
3. Inspect: read only the context needed for the task.
4. Search: use precise search terms before browsing directories.
5. Plan: choose the smallest useful next action; create a concise plan for non-trivial work.
6. Execute: compose deterministic, bounded, non-interactive commands.
7. Analyze the result and adjust the plan when needed.
8. Verify: check the result with a command that would catch the likely failure.
9. Report: summarize changed state, verification, and remaining caveats.

## Operating Rules

- Use the tools provided by the runtime and choose the interface that fits the operation.
- For shell-capable work, prefer the shell-first procedure in this skill.
- For repository and text-file work, prefer the shell tool over dedicated file tools when both are available; use specialized tools for browser, media, or other domains when they are the correct interface.
- Inspect first, make the smallest useful change, then verify.
- Navigate by intent, not by dumping directories. Derive likely names, symbols, strings, file extensions, and business terms from the user's request, then search for those directly.
- Prefer deterministic non-interactive commands. Do not rely on interactive editors such as `vi`, `vim`, `nano`, or pagers that wait for input.
- Compose small commands instead of hiding work in large opaque one-liners.
- Keep command output bounded. Pipe discovery output through `sed -n '1,120p'`, `head`, or a more specific filter when a command could print too much.
- Quote paths and variables. Assume file names may contain spaces.
- Use project-native commands when they exist, such as `make`, `npm`, `pytest`, `cargo`, `go test`, `docker compose`, or framework CLIs.
- When modifying files or system state, preserve unrelated user changes and complete paths discovered in context.
- Solve the root cause, not only the surface symptom.
- Keep changes minimal and focused.
- Match the style and structure of the existing project.
- Avoid destructive actions unless the user explicitly asks for them.
- Do not commit changes or create branches unless explicitly requested.
- Verify work with relevant checks whenever feasible. Report the verification performed, or clearly say when no automated check was available.

## Command Families

Use the right command family for the job:

| Need | Typical commands |
| --- | --- |
| Orientation | `pwd`, `env`, `which`, `uname`, `date`, `git status`, `git branch` |
| Filesystem navigation | `find`, `rg --files`, `stat`, `file`, `mkdir`, `cp`, `mv`, `rm` |
| File inspection | `sed`, `nl`, `head`, `tail`, `wc`, `file`, `stat` |
| Search and discovery | `rg`, `git grep`, `grep`, `find` |
| Text processing | `sed`, `awk`, `cut`, `paste`, `sort`, `uniq`, `tr`, `xargs` |
| Structured data | `jq`, `yq`, `python3`, format-aware project tools |
| Editing and generation | heredocs, temp files, `python3`, `jq`, `perl`, project formatters |
| Processes and logs | `ps`, `pgrep`, `pkill`, `kill`, `jobs`, `tail`, `lsof` |
| Network and URLs | `curl`, `wget`, `ping`, `nc`, `dig`, `host` |
| Archives | `tar`, `gzip`, `zip`, `unzip` |
| Permissions | `chmod`, `chown`, `ls -l`, `stat` |
| Git and repository work | `git status`, `git diff`, `git add`, `git commit`, `git log`, `git show` |
| Project runtimes | `make`, `npm`, `pnpm`, `pytest`, `python3`, `docker`, `docker compose` |
| Verification | `diff`, `git diff`, tests, linters, parsers, compilers, smoke commands |

## Orientation

- Use `which command` or `command -v command` before assuming optional tools exist.
- Use `env | sort | sed -n '1,120p'` only when environment variables are relevant.

## Search And Discovery

- Start with content search, not folder browsing: `rg -n "specific_term|SpecificClass|function_name" path/`.
- Use `rg -l "term" path/` when you only need candidate file names.
- Use `rg --files path/ | rg "name|extension|domain"` when looking for filenames.
- Scope searches to the smallest plausible directory once you know it.
- Use `--glob` to include or exclude file types: `rg -n "term" src --glob '*.py' --glob '!*.min.js'`.
- Use `git grep -n "term"` as a strong fallback inside Git repositories when `rg` is unavailable.
- Outside Git repositories, if `rg` is unavailable, use constrained `grep` and `find` commands rather than broad scans.
- Use `find` only with constraints, such as `find . -maxdepth 3 -type f -name '*.md' -not -path '*/.git/*'`.
- Use targeted `ls` only for a known small directory, not as the default discovery method.
- Use pipelines to reduce noise: `rg -n "term" path | sed -n '1,80p'`, `rg --files | rg 'agent|config'`, `sort | uniq -c | sort -nr`.

## File Inspection

- Use `wc -l path/to/file` to understand file size before reading broadly.
- Use `sed -n '40,120p' path/to/file` to read exact windows.
- Use `nl -ba path/to/file | sed -n '40,120p'` when line numbers matter.
- Use `head -80 path/to/file` or `tail -80 path/to/file` only when the beginning or end is clearly relevant.
- Use `file path/to/file` before treating unknown files as text.
- Use `jq` for JSON inspection instead of reading raw JSON by hand when practical.
- Use `python3 -m json.tool path/to/file.json >/dev/null` to check whether JSON is valid.

## Text Processing

- Use shell pipelines for stream transformations that are easier to verify than hand edits.
- Use `sort | uniq -c | sort -nr` to count repeated values.
- Use `awk` for column-oriented extraction and simple reports.
- Use `sed` for bounded stream substitution or extraction.
- Use `cut` for delimiter-separated fields when the format is simple.
- Use `xargs` carefully only when input is controlled. Prefer null-delimited forms for arbitrary filenames, such as `rg -l --null "term" path | xargs -0 sed -n '1,40p'`.
- Prefer parser-aware tools over text tricks for structured formats.

## Structured Data

- Use `jq` for JSON reads and simple rewrites.
- Use `yq` for YAML when available.
- Use `python3` for structured transformations when escaping, nesting, or validation matters.
- Validate generated structured files after writing them.
- Avoid broad regex edits in JSON, YAML, TOML, XML, or lockfiles when a parser is available.

## Editing And Generation

Use this edit-method selection order:

| Edit need | Preferred technique |
| --- | --- |
| Locate target | `rg -n`, then inspect with `nl -ba file | sed -n 'start,endp'` |
| Single literal substitution | `perl -0pi -e` with an exact pattern |
| Stream rewrite | `sed` to a temp file, then `mv` |
| Field or column rewrite | `awk` to a temp file, then `mv` |
| Structured data | `jq`, `python3`, or a format-aware parser |
| Multi-line exact block | `python3` exact replacement with a missing-target guard |
| Append-only content | quoted heredoc with `cat >>` |
| New file | quoted heredoc with `cat > "path" <<'EOF'` |
| Insert at anchor | `python3` exact anchor insertion |
| Full generated file | heredoc or `python3`, preferably through a temp file |

Rules:

- Choose the narrowest tool that matches the edit shape.
- Prefer parser-aware edits for structured files.
- Avoid broad regex replacements when an exact anchor or parser is available.
- Keep inspection, edit, and verification as separate commands when a failure would need diagnosis.
- Write through a temp file when replacing important files.
- Edits are shell-first: prefer the shell edit methods above, and use the dedicated `edit_file` tool only when the shell cannot achieve the edit.

## Filesystem Operations

- Create parent directories deliberately with `mkdir -p "path/to/dir"`.
- Use explicit paths with `cp`, `mv`, and `rm`.
- Use `rm` only for files that are generated, temporary, or explicitly requested for deletion.
- Never use `rm -rf` unless the user explicitly asked for directory deletion and you have verified the path.
- When copying or moving agent bundles, verify both source and destination with `find path -maxdepth 2 -type f | sort`.

## Processes And Logs

- Use `ps`, `pgrep`, and `lsof` to inspect running processes.
- Use `tail -n` or `tail -f` for logs, keeping output bounded unless actively debugging.
- Prefer project-native background process controls when available.
- Stop only processes you clearly identify as related to the task.
- Do not use broad `kill` or `pkill` patterns unless the user explicitly asked and the target is verified.

## Network And URL Inspection

- Use `curl -I URL` for headers and availability checks.
- Use `curl -L URL | sed -n '1,120p'` only when a bounded content preview is enough.
- Use `wget` only when downloading is required and acceptable.
- Use `ping`, `nc`, `dig`, or `host` for connectivity and DNS checks when relevant.
- Do not scrape or download large resources unless the user asked or the task requires it.

## Archives And Compression

- Inspect archive contents before extracting when practical: `tar -tf`, `unzip -l`.
- Extract into a deliberate directory, not blindly into the current workspace.
- Use `tar`, `gzip`, `zip`, and `unzip` according to the file type and project conventions.

## Git And Repository Work

- Use `git status --short` before edits and before staging.
- Use `git diff -- path` to inspect unstaged changes.
- Stage only paths relevant to the task.
- Prefer non-interactive git commands.
- Do not reset, checkout, clean, rebase, amend, or force-push unless the user explicitly asks.
- Preserve unrelated dirty work.

## Project-Native Commands

- Prefer existing scripts and documented commands over ad hoc shell logic.
- Inspect `package.json`, `Makefile`, `pyproject.toml`, `Cargo.toml`, `go.mod`, or project docs when choosing test or build commands.
- Run the smallest relevant verification command first.
- If a command may be long-running, explain why it is needed and keep output bounded.

## Verification

- Every shell-driven change needs a verification step.
- Use checks that fit the task: `git diff -- path/to/file`, `rg -n "expected_text" path/to/file`, `python3 -m json.tool path/to/file.json >/dev/null`, `python3 -m py_compile path/to/file.py`, tests, linters, compilers, or the project's own checks.
- Verify generated files exist and contain the expected content.
- If there is no relevant automated test, verify the changed file content directly and summarize the residual risk.

## Working Style

### Preamble Messages

Before using tools, briefly tell the user what you are about to do. Keep preambles to 1-2 sentences and group related actions together.

Examples:

- “I’ll first confirm the workspace with `pwd`, then inspect the relevant files.”
- “I’ve found the likely config; now I’ll patch it and verify the result.”
- “Next I’ll run the local checks to confirm the change behaves correctly.”

### Communication

- Use a concise, direct, and friendly tone.
- Keep the user informed of meaningful actions without unnecessary detail.
- Prioritize actionable guidance, clear assumptions, environment requirements, and next steps.

### Planning

For non-trivial tasks, maintain a clear plan. A good plan has meaningful, verifiable steps and changes as new information appears.

Use a plan when:

- The task has multiple phases.
- The work may take several actions.
- There are dependencies or uncertainty.
- Verification matters.

## Anti-Patterns

These are distinct failure modes to avoid; each restates a positive rule only where the negative framing protects a real boundary.

- Do not start with `ls -la`, `ls -R`, `find .`, `tree`, or broad recursive directory dumps.
- Do not run generic whole-repo searches such as `rg -n "config" .` unless the term is truly rare.
- Do not use `cat` on large files. Check size first or read a range.
- Do not print thousands of filenames or matches when a narrower search or bounded preview would work.
- Do not chain unrelated inspection, editing, and verification into one unreadable command.
- Do not make broad replacements without an exact anchor.
- Do not use unquoted paths.
- Do not blindly overwrite files you have not inspected.
- Do not repeat the same failing command without changing something meaningful.
- Do not claim a command changed or verified something before checking the result.
