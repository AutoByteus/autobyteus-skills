# Full Reflection Pass

A full pass reads a period of work for what a short check cannot see: feedback that comes back, several corrections with one cause, routines that take too long, an environment that makes the work harder. In self mode you read your own work; in observer mode, another agent's (last section). Both write the same records ([template](../templates/record-file.md)).

## 1. Gather the evidence

Read `lessons.md` and the recent records first, so you know what is already known. Then:

- **Every piece of the user's feedback:** in the conversation, in Task comments, and in the work journals. List each one: his words, when, and what you had made at that point. Search the journals with `search_memory`, one sentence per kind of feedback ("the user says that is wrong", "the user asks for the same thing again", "the user rewrites what I wrote"), and read the cited lines at their path.
- **The work journals of the period:** the folders the request names, or what `search_memory` finds.
- **Signals that need no user,** as places to start reading:
  - refused or failed tool calls, and retries;
  - the same command sequence run again and again;
  - a question asked twice, or an open question repeated in report after report;
  - a claim found wrong later, by the user, a reviewer, or your own check;
  - a Task reopened, or a result sent back;
  - many steps for routine work; a file that keeps growing; the same files read again in every conversation.

## 2. Ask why each piece of feedback came

For each one: what did the user want, what did you make, and why did you make that? Read the part of your skill you were following at that moment, and what you knew then. Decide which produced it:

- **a rule of your skill** that led there (quote it);
- **a rule that is missing**: nothing in your skill covers what he wanted;
- **knowledge you lacked or had wrong** about the user, his project or his taste;
- **a habit in this work**: your skill and knowledge pointed the right way and you did not follow them;
- **the environment**: a tool or file that made the right way hard.

"I forgot" is not a cause; say what made forgetting easy. When the feedback came back after a lesson was written, the lesson is not enough, and the cause is usually in the skill or the environment.

## 3. Group by cause

Several corrections often come from one cause: six "remove this sentence" corrections may all come from one rule that asks for signposts or disclaimers. Group the feedback by cause, and count each group. A group whose cause is a rule of the skill is worth more than all its corrections fixed one by one, because the rule will produce the next one.

## 4. Inspect the environment

Look at the files, notes, folders, tools and scripts the work uses. Was there a shorter or better way: a script instead of the same commands each time, a tool that does the job better, a note that would have answered the question?

## 5. Write, then act by fix type

Write one record per cause in today's file, listing the feedback it explains, and one record for the pass with what you read and the measures. Then:

- **Lesson or knowledge:** add or update it in `lessons.md`.
- **Environment:** when the change is to your own working files or a script, make it and record what changed.
- **Skill or shared standard:** add a proposal to `proposals.md`: the records, the rule (quoted) or the gap, the change in a few lines, how to test it old against new (the feedback it should have prevented is the test), and its status (open; sent, with where, such as a Task key; kept or rejected). Tell the user or the caller. For an AutoByteus agent package, the maintainer who tests it is the Agent Package Creator.
- **Distill:** a lesson that has held through several chances, or several lessons with one cause, become a proposal for the skill. Once the skill has it, remove the lesson and name the change in a record.

Report the records' file, each cause in one line with its count, what you changed, and what you propose.

## Observer mode

The request names the agent to observe and what you may read of it: its journals, its workspace files, its Tasks, its skills. Read nothing else of it.

- Do the pass on its evidence. Look especially for what it cannot see itself: feedback it answered one by one without seeing their common cause, a mistake it repeats while reporting the work as done well, a lesson whose feedback keeps coming back, a struggle it does not mention, an environment it works around instead of fixing, and the same mistake in several agents (a gap in a shared standard).
- Change nothing of the observed agent: not its lessons, files, skill or environment.
- Write the records in your own reflections folder, at `observed/<agent>/<YYYY-MM-DD>.md`, listed in your `index.md`. Use the same record shape, so the observed agent can take them in as they are.
- Report to whoever asked, with the file's absolute path for the observed agent and a short digest for the user.
