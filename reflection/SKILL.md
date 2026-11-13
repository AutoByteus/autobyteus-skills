---
name: reflection
description: Learn from past work, your own or another agent's. For each piece of the user's feedback ask why he had to give it, trace it to what in your way of working produced it, and write it down where your later runs read it, so the same feedback does not come twice. Use it at the start of a conversation to read your lessons; whenever the user corrects you and after each piece of work, for a short check written to your reflections folder; and for a full reflection pass when asked or when feedback a lesson covers comes back.
---

# Reflection

If your skills and what you know were right, the user would get what he wants the first time and would have nothing to correct. So each piece of his feedback shows something in how you work that is not good enough yet:

- **your skills**, the procedure you follow: a rule that led you the wrong way, or a rule that is missing;
- **what you know**: a fact about the user, his project or his preferences that you lacked or had wrong;
- **your habits in this work**: something you did although your skill and knowledge would have told you better;
- **your environment**: a file, tool or script that made the right way hard.

Reflection asks why the feedback came, finds which of these produced it, and writes it down where your later runs read it. Steps that cost extra without any feedback (a retry, a failed call, a step done twice) are the same kind of signal, found without the user. Every reflection ends in a written record; a reflection that is not written down is lost with the conversation.

## Your reflections folder

Use `<semantic memory>/reflections/`, inside the folder your Semantic Memory instructions name. If your instructions have no Semantic Memory section, use `<workspace>/reflections/`.

```text
reflections/
  index.md                # read first: what this folder holds and where
  lessons.md              # what to do differently; read at the start of each conversation
  proposals.md            # changes to a skill or shared standard, for its maintainer to test
  records/2026-11-13.md   # one file per day: every reflection's records, added to, never rewritten
```

- **Start from `index.md`.** It is the one fixed path; every other file is found through it, one line per file or folder saying what it holds. So the folder can grow (lessons split by topic, records grouped by month, summaries, an archive) without a run losing its way. Create it with the folder, and update it whenever you add or move a file.
- **Records stay as written.** Add to the day's file; never edit or delete an earlier record. A correction is a new record that names the old one. Each record has an ID, `<date>-R<n>`, that stays the same if its file moves; lessons cite records by ID.
- **Several runs may write at once.** Append records at the end of the day's file. Read `lessons.md` just before you change it, and change only the lesson you mean.
- If one of your skills organizes your semantic memory, it may restructure this folder; follow it, and keep `index.md` as the entry.
- If you kept lessons in another file before, move them into `lessons.md` at your first reflection, with their counts, and leave a one-line pointer in the old file.

## At the start of a conversation

Read `index.md` and `lessons.md`, and keep the lessons that fit the work in front of you.

## The short check: when the user corrects you, and after each piece of work

Whenever the user corrects you, asks for something again, or changes what you made, and when you finish a piece of work (a Task closed, a request answered, a result handed off), ask:

1. **What did the user correct, ask for again, or change, and why did he have to?** What did he want, what did you do, and what in your skills, knowledge, habits or environment led you to do that?
2. **What cost extra steps** without any feedback: a retry, a refused or failed call, a step done twice, a wrong first try, a long search for something you could have known?

Write the answer as a record in today's file ([record-file template](templates/record-file.md)), even when it is one line: "nothing extra". Give each finding the record's fields: the signal, what was wanted and what was done, why, how often, cost, fix, done. Then update the lessons:

- **The user's feedback, or waste that happened before:** add a lesson. A one-off extra step stays a record.
- **A lesson already covers it:** add the date to its count. The lesson did not work: rewrite it, and run a full pass on it.

If you were told of an observer's report on your work, read it now: take in the lessons you accept, and record which you do not and why.

Name a new or changed lesson in one line of your report.

## Lessons

`lessons.md` holds what to do differently, short enough to read at every start. One lesson per cause, not per correction:

`**<situation>.** Mistake: <what went wrong>. Do instead: <what to do>. Written <date>; seen <n>: <dates>; records <IDs>.`

`seen` counts each time this kind of feedback or waste happened, before and after the lesson was written; a date after `Written` means it came back. Merge lessons with the same cause. A lesson that has held through several chances, or one that keeps coming back, points at your skill: the full pass turns it into a proposal.

## Full pass

When the user or a caller asks you to reflect on a period of work or to observe another agent's work, or when a short check finds feedback a lesson already covers, follow [references/full-pass.md](references/full-pass.md).

## Rules

- **A reflection changes no skill and no shared standard.** A change to your own skill, another agent's, or a standard others apply is a proposal in `proposals.md`, with its records. It is kept only after its maintainer tests it old against new and the user agrees.
- **Change only your own working files.** You may write scripts for command sequences you repeat, and reorganize your own notes and working files (back them up first and say what changed). Never the user's data, other agents' files, or shared settings.
- **Private stays private.** Records point to journals, messages and Tasks, and quote only short lines. No secrets, credentials, or personal details the work does not need.
- **Count what happened.** Every count and cost comes from evidence you can point to. When the evidence does not show the cause, write "possible" and list the reasons you see.
