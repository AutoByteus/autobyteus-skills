# Xiaohongshu Posting Experience Log

## Entry Format
- Date:
- Task:
- Context:
- Failure signal:
- Root cause:
- Fix that worked:
- Reusable rule:

- Date: 2026-02-19
- Task: Open Xiaohongshu creator publish page and prepare post publishing
- Context: Started from `xiaohongshu.com/explore`, then navigated to `creator.xiaohongshu.com/publish/publish`.
- Failure signal: Redirected to `creator.xiaohongshu.com/login?redirectReason=401` with security/login gates; publish composer inaccessible.
- Root cause: Creator platform requires authenticated creator-session state; explore-page login overlays are insufficient for direct publish access.
- Fix that worked: Use human-in-the-loop handoff for SMS/QR login completion first, then re-check creator URL and composer elements before drafting.
- Reusable rule: For Xiaohongshu posting, verify creator-login state on `creator.xiaohongshu.com` before any compose automation; do not continue on explore-page login assumptions.
