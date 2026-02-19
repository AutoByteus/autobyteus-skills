# LinkedIn Posting Lessons

- Use DOM-first on `https://www.linkedin.com/feed/` and verify login state before compose actions.
- If authentication or security checks appear, pause for human intervention.
- Validate final text and media state in the active composer before clicking `Post`.
- After posting, verify the newest profile post content and media.
- LinkedIn does not reliably support replacing media on an already published post; delete + repost is the dependable path.
- If external/local image fetch is blocked in composer, generate a high-resolution in-browser image and attach it through `#media-editor-file-selector__file-input`.
