# Result: content-management skill (autobyteus-skills-1)

- Status: `Completed` for review; merge waits on the user's choice about the Write section (below).
- Operation: `create` (`update_intent: new-package`). Package type: `skill` (standalone).
- Added:
  - `content-management/SKILL.md`
  - `content-management/agents/openai.yaml`
- Modified: `README.md` (one entry).
- Request: Task autobyteus-skills-1 and the user's direction on 2026-10-24: content management means writing, updating and restructuring; the main cases are a technical article, a messy folder, and content-heavy agent teams. Vocabulary is a minor part.

## What the skill holds

- **What good content has:**
  - a clear line;
  - a summary first;
  - one home per fact and per kind of record;
  - parts split by lifetime;
  - names that say what is inside.
- **Write:** the line before the prose; strengthen each idea; it points to `deep-research-article` and `bilingual-author-style-writer` for full article workflows.
- **Update:** extend where a fact already lives, not a new section or copy; put a new item in the place for its lifetime.
- **Restructure:**
  - the signs of friction;
  - the structure grows with the volume (desk, shelf, library);
  - map first, then judge at three levels;
  - restructure from the readers, separate from changes of meaning;
  - lose nothing (backup, map old to new, rules keep their strength, links follow moves);
  - tell what moved;
  - decide the structure yourself.

No project data is in the skill.

## Replay

- **Setup:** isolated AutoByteus 1.5.9-beta.2. Test agent "Content Manager" with the skill, and an identical "Content Manager (baseline)" without it. Both on `claude_agent_sdk` / `opus`, with file tools only, so no delegation or Tasks were possible.
- **Inputs:** copies of real content, reset to the same baseline before each run.

| Case | With the skill (it loaded the skill each time) | Baseline |
| --- | --- | --- |
| Oversized board (real 108 KB, 302 lines) | Live board 65 KB plus a word-for-word archive. Rules gathered in one list with "never" and "only" kept; a team-copies index; stale items flagged. 0 of 162 Task keys, 63 run IDs and 58 long IDs lost. | One file grown to 129 KB (more index tables, nothing moved out). Nothing lost. |
| Messy folder (copy of the agents repo's `tickets/`: 115 tickets, 325 files, almost all finished but left in `in-progress/`) | 112 finished tickets moved to `done/`. 52 files' self-references updated to the new paths. `tickets/README.md` added as the folder's entrance. All 325 files kept. | 95 moved to `done/`. Stale paths left inside the records; no index. Its check of what is really finished was slightly more careful (an uncommitted team stayed in progress). |
| Technical article from the user's rough notes | Clear article: a one-line summary first; a problem → diagnosis → principle → fix → generalization line. | Equally clear and arguably as good. **No visible gain from the skill.** |

**Reading:** the skill changes behaviour where content is restructured or grows (board, folder). For writing an article, Opus already does what the Write section says.

## Choice for the user

Keep the Write section as it is (short; it covers writers on weaker models and ties the skill to the article skills), or shrink it to one line pointing to the article skills.

## Follow-up proposed

A Task in the AutoByteus Agents project: add a one-line reference to `content-management` in the roles that manage content (Project Task Manager, Solution Designer, Architecture Reviewer, Agent Package Creator), each keeping its own specific rules.
