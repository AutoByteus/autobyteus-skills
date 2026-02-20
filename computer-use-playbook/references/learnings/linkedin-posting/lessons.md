# LinkedIn Posting Lessons

## Scope
- Prefer `https://www.linkedin.com/preload/sharebox/` for compose. It is more stable than feed-embedded compose surfaces.

## Core Rules
- Use DOM-first and verify login state before compose actions.
- If authentication or security checks appear, pause for human intervention.
- Treat text and media as separate checkpoints; never publish until both are verified.

## Composer Reliability Rules
- For text insertion in Quill, use `.ql-editor[role="textbox"]` and dispatch input/change events after insertion.
- Do not trust script success alone; require editor-visible text length `> 0`.
- If `execCommand('insertText')` fails, fallback to paragraph-based DOM insertion (`<p>` per line) plus events.

## Media Reliability Rules
- Add media through `#media-editor-file-selector__file-input` after clicking `Add media`.
- If external/local fetch is blocked in HTTPS composer, generate infographic in-browser (canvas -> File) and attach via the same file input.
- After upload, require editor step transition (`Next`) before final publish step.

## Pre-Publish Checklist
- `textLen > 0` in `.ql-editor[role="textbox"]`.
- At least one media preview is visible when image is required.
- Composer `Post` button is enabled.

## Publish Verification Checklist
- Confirm success toast (`Post successful`/equivalent).
- Capture the produced post URL (`/feed/update/urn:li:share:...`).
- Open live post URL and verify opening sentence + expected hashtag/media.
- Capture one evidence screenshot.

## Recovery Playbook
- If post is missing text/media, delete and repost from `/preload/sharebox/`.
- LinkedIn edit flow is unreliable for media replacement; treat delete + repost as default correction path.
