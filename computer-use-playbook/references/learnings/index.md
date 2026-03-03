# Learnings Library

Use one subfolder per app/site/workflow.

## Structure
- `general/`: cross-task fallback logs.
- `<topic-slug>/`: topic-specific lessons and experience log.

## Load Priority
1. Load `<topic-slug>/lessons.md` first (source of truth).
2. Load `<topic-slug>/experience-log.md` second (supporting evidence).
3. Load `general/experience-log.md` only if topic guidance is missing or incomplete.

## Execution Precedence
1. Execute existing `lessons.md` first.
2. If a lesson step fails, use documented lesson fallbacks.
3. If lessons/fallbacks are insufficient and there is no human gate, run bounded self-learning attempts.
4. Promote successful new patterns back into `lessons.md`.
5. Log run details in `experience-log.md`.

## Topic Resolution (Use Canonical Slugs)
- X / Twitter / Expost -> `x-posting`
- LinkedIn / linkedin.com -> `linkedin-posting`
- Google Flow / labs.google/fx/tools/flow -> `google-flow`
- Xiaohongshu -> `xiaohongshu-posting`

Do not create near-duplicate topic folders when a canonical topic already exists.

## Topic Folder Convention
Each topic folder should contain:
- `lessons.md` (stable playbook rules)
- `experience-log.md` (incremental run notes)

## Current Topics
- `google-flow/`
- `x-posting/`
- `linkedin-posting/`
- `xiaohongshu-posting/`

## Adding a New Topic
When a new recurring tool/site appears:
1. Create `references/learnings/<topic-slug>/`.
2. Add `lessons.md` with proven workflow/checklist.
3. Add `experience-log.md` using the standard entry format.
4. Update this index by adding the new topic.
