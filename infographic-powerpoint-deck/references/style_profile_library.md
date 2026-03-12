# Style profile library (legacy alias)

Canonical style definitions now live in folderized style packs:
- `references/style-pack-catalog.md`
- `references/style-pack-system.md`
- `references/style-packs/<pack-id>/`

Use this file only as a legacy alias table.

| Legacy style name | New pack ID |
|---|---|
| Style A (Cinematic Dark) | `cinematic-dark` |
| Style B (Editorial Light) | `editorial-light` |
| Style C (Airy Relaxed) | `airy-relaxed` |
| Style D (Clean Corporate) | `clean-corporate` |

Fallback when user intent and inferred archetype are both unclear: `editorial-light`.
Style packs remain compatible with multiple layout families; choose the layout separately per slide, including split layouts, didactic board layouts, and full-bleed overlays.

Additional direct packs (no legacy alias name required):
- `cinematic-light`
- `cinematic-editorial`
- `animated-feature-bright`
- `warm-sermon`
- `neo-tech`
- `youth-social`
- `research-academic`
