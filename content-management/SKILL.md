---
name: content-management
description: Write, update and restructure content so it stays easy to read, follow and find things in, as it grows. Covers articles and papers, documents and designs, living records (task boards, logs, indexes, notes), instruction packages, and folders of files. Use when writing any of these, when adding to or changing them, when asked to make something clearer, tidier or easier to follow, or when content has grown hard to read, repeats itself, or has outgrown its files or folders.
---

# Content Management

Content is for its readers: who reads it, when, and what they need first. Reading is the real cost (time, attention, tokens), and it is paid again at every read, so a good structure lets each reader find what they need and read no more. Content is never finished: it is written, updated many times, and restructured when it outgrows its shape.

Manage content the way a good engineer manages code:
- **Architecture:** its parts and their boundaries.
- **Flow:** the order a reader moves through it.
- **Single source of truth:** one home per fact.
- **Duplication:** repeated text, which, as in code, usually means a part without a clear owner.
- **Refactoring:** restructuring, where the meaning stays the same and is checked before and after.
- **The test:** reading it as its reader would.

Small changes that are each right alone make content drift, just as they make code drift, so its structure needs continuous upkeep.

## What good content has

- **A clear line.** Parts come in the order the reader needs them: for an argument, the order of the ideas; for a procedure, the order of the work; for a record, the live items first.
- **A summary first, detail below.** A title or first line says the whole thing in one sentence (lists and searches often show only that line); then short labelled sections in a steady order.
- **One home per fact, and per kind of record.** Each fact lives in one place; everywhere else points to it by name, link or ID. Records of one kind (decisions, follow-ups, results) live in one place, even when many people add to them. A copy drifts; an index points, it does not copy.
- **Parts split by lifetime.** What changes daily (live items), what only grows (history) and what stays put (rules, definitions) live apart, with a pointer from the live part to the others.
- **Names that say what is inside.** Files, folders, sections and headings are named for their content and use; a word keeps one meaning throughout, and a thing keeps one name.
- **No words that change nothing.** Every sentence gives the reader something they need: a fact, a step, a reason, an example. Say a point once, where it belongs, and point to it elsewhere. Cut filler and repeats, but keep each distinction that changes what the reader understands or does.

## By kind of content

Each kind has its own reader and its own checks:

- **Article or paper.**
  - It answers one question for one reader.
  - The answer, or the thesis, comes in the opening paragraph.
  - Each section is one step of the argument and says how it follows from the previous one.
  - Each point is made once, backed by a concrete example or a source.
  - The ending answers the opening question; it does not restate the sections.
- **Folder of files.**
  - Top-level folders are grouped by what the people who use them look for, usually purpose or project, not file type.
  - One naming scheme holds throughout (for example `YYYY-MM-DD-topic`).
  - Each folder has an entrance (a README or index) saying what is where.
  - Stray files at the top go to where their kind lives.
  - Scratch and generated output are kept apart from the work.
  - Before moving anything, find what depends on its path, including other people's or agents' instructions.
- **Living record (board, log, index, notes).**
  - One short line per live item, pointing to where its detail lives.
  - Finished and parked items are in files beside it.
  - Stale waits are raised once.
- **Instructions (skills, guides, procedures).**
  - The steps come in the order the work happens.
  - Each rule comes with its reason.
  - There is nothing the reader would do anyway without being told.

## Write

1. Know the reader and the purpose before the first sentence: what should they know or be able to do afterwards?
2. Build the line before the prose. For an argument: the claim in one sentence, then the ideas that carry it, each following from the one before (a cause, a consequence, a contrast, an example). Test each idea by asking what breaks without it, and cut or merge the ones that break nothing.
3. Then strengthen each idea: evidence, a concrete example, exact terms. Polish wording last, cutting what repeats or adds nothing.

For a full research article or a voice-matched article, use `deep-research-article` or `bilingual-author-style-writer`; this skill covers the structure under them.

## Update

Before adding anything, find where that fact or kind of record already lives, and extend that place instead of adding a new one. Small additions that each start a new section, file or copy are how content drifts: each looks right alone, and together they bury the line. Put a new item where its lifetime belongs: a live item on the live record, a finished one in the history.

## Restructure

Restructure when friction shows:
- it is slow to read or to edit;
- a name no longer fits what the part holds;
- a file keeps gaining sections for different readers;
- one task sends the reader through many files;
- the same thing is said in several places.

The structure grows with the volume: a desk holds the few things in use, a full table needs a shelf, a full shelf needs a library with an index and categories. Do not build the library for three items.

1. **Map first.** Read the whole body of content and note what each part holds, who reads it, when, and how the parts connect.
2. **Judge at three levels, highest first.** The set: would you draw these boundaries if you started fresh? A part: does it do one job for one reader at one moment, and does its name fit? Inside a part: order, repeats, wording. Rewording cannot fix a part that holds two jobs.
3. **Restructure from the readers:** what each needs, and when. Separate the restructure from any change of meaning, so each can be checked on its own.
4. **Lose nothing.**
   - Keep the original (a backup or version control) until the new shape is checked.
   - Map every old part to its new home.
   - Keep rules as strong as they were: "must", "never" and "only" stay.
   - Update everything that points to a moved or renamed part (links, indexes, scripts, instructions) in the same step, or leave the part where it is.
5. **Tell the reader** in a few lines what moved where.

Decide the structure yourself; that is the job. Ask only about what you cannot decide alone: dropping content, changing what it means, or a move that breaks something others rely on.

## Check

Read the result in order, as its reader would at the moment they read it. Can they follow the line, find what they need without reading the rest, and act on it? After a restructure, compare the old and new versions: same meaning, nothing lost. When the same kind of correction keeps coming back, do not add one more sentence. Change the structure that produces the problem: where things live, what comes first, or what a template asks for.
