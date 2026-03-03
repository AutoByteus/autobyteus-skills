# LinkedIn Posting Lessons

## Scope
- Applies to LinkedIn posting via `https://www.linkedin.com/preload/sharebox/`.

## Operating Mode
- Run in lesson-lock mode: execute the primary workflow first and do not improvise before documented fallbacks.

## Core Rules
- Verify login state first; if authentication/security checks appear, pause for human intervention.
- Never publish until the user explicitly approves the exact final draft for this run.
- Preserve user argument and tone; do not add marketing framing unless requested.
- For long text, require insertion integrity checks before publish: expected length plus opening/ending lines.
- LinkedIn may rewrite outbound links to `lnkd.in`; treat this as normal if final meaning and references are preserved.

## Mandatory Primary Workflow
1. Navigate directly to `https://www.linkedin.com/preload/sharebox/`.
2. Verify compose editor exists (`.ql-editor[role="textbox"]`) and page is interactive.
3. Insert approved draft with Quill-compatible input semantics.
4. Verify editor text integrity:
   - expected length threshold,
   - opening line matches,
   - ending line matches.
5. Verify media state matches intent and `Post` is enabled.
6. Click publish once (primary action button in composer).
7. Verify success via toast and extract canonical post URL (`/feed/update/...` or activity URL).
8. Open the post URL and verify rendered post opening line and media presence.
9. Capture one evidence screenshot.

## Allowed Fallbacks (Only If Primary Step Fails)
- If feed-surface composer interactions fail, do not retry feed clicks; stay on `/preload/sharebox/`.
- If initial insertion partially drops content, reinsert text once with Quill-compatible events and re-run integrity checks.
- If media replacement is needed after publish, use delete + repost path; edit mode is not reliable for media replacement.

## Recovery
- If publish result is incorrect, capture URL and failure evidence, delete/repost from `/preload/sharebox/`, and re-verify final live post.
