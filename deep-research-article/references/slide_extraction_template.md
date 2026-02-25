# slide_extraction.md template (article → infographic deck handoff)

Make one row per slide. Keep the headline as a **claim** and include direct rendering fields for image-only PPT prompts.

| Slide | Slide role | Headline (claim) | Must-appear text (verbatim) | Evidence anchor + source ID(s) | Supporting bullets (2–4) | Recommended style pack ID | Scene ID | Visual suggestion (location + hero symbol + props) | Layout hint | Text budget |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | opening |  |  |  |  | editorial-light | sunlit-library-day |  | L4 | short |
| 2 | key-claim |  |  |  |  | editorial-light | atrium-morning |  | L1 | medium |
| 3 | evidence |  |  |  |  | research-academic | whiteboard-framework-session |  | L2 | heavy |

Field notes:
- `Slide role`: opening / context / key-claim / evidence / contrast / objection / application / closing.
- `Must-appear text (verbatim)`: final on-slide text payload (title, quote lines, bullets, footer) for direct prompt insertion.
- `Recommended style pack ID`: use IDs from infographic style catalog (e.g., `editorial-light`, `warm-sermon`, `neo-tech`).
- `Scene ID`: use IDs from infographic scene catalog; if custom, use `custom:<slug>`.
- `Layout hint`: use L1–L6 from infographic layout library.

Text budget meanings:
- `short`: title + 2–3 bullets
- `medium`: title + 1–2 quote lines + 3–5 bullets
- `heavy`: dense page; prefer L3 or split slide
