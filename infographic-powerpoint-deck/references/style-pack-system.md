# Style-pack system (modular style architecture)

Purpose: treat style as a reusable folderized template pack, not scattered defaults.
Style pack controls the visual language. Layout is chosen separately per slide.

## Directory model

```text
references/style-packs/
  base-core/
    manifest.toml
    00-core-foundation.md
  <style-pack-id>/
    manifest.toml
    10-style-profile.md
    20-motif.md
    30-consistency.md
    40-scene-bias.md
```

## Composition rule (required)

Compose style prompt blocks in this order:
1. `base-core`
2. selected `<style-pack-id>`
3. slide-specific content from `prompt_template.md`

Never mix blocks from different style packs in one deck unless explicitly requested.

## Orthogonality rule

- **Style pack** defines palette, lighting, texture, typography attitude, and scene bias.
- **Layout** defines where text and imagery sit on a given slide.
- The same style pack may support split-panel slides, framework slides, comparison slides, and full-bleed overlay slides inside one deck.

## How to use in practice

1. If the user provides raw article content, infer deck archetype first using `references/deck_archetype_routing.md`.
2. If the user also provides reference slides/screenshots, extract reusable visual grammar using `references/reference_slide_intake.md`.
3. Select style pack ID from `style-pack-catalog.md`.
4. Compose blocks with:
   ```bash
   python3 scripts/compose_style_pack_blocks.py --pack-id <style-pack-id>
   ```
5. Paste output under the style section of each slide prompt.
6. Keep the same style pack for all slides in one deck unless the user explicitly requests mixing.
7. Auto-route the layout per slide from `references/layout_routing_policy.md` unless the user or upstream artifact provides an explicit override; do not assume one style pack implies one fixed layout.
8. If a reference slide reveals a reusable new look, either refine the nearest pack or scaffold a new one.

## Add a new style pack

1. Create scaffold:
   ```bash
   python3 scripts/create_style_pack.py --pack-id <new-id> --display-name "<Name>" --keywords "keyword1,keyword2" --scene-tags "tag1,tag2"
   ```
2. Add `manifest.toml` with:
   - `id`, `display_name`, `inherits`, `intent_keywords`, `default_scene_tags`.
3. Add `10/20/30/40` blocks to define full style behavior.
4. Register the pack in `style-pack-catalog.md`.
5. If needed, add matching scenes in `scene-catalog.md` using `scene-entry-template.md`.
6. Validate the pack by composing it with:
   ```bash
   python3 scripts/compose_style_pack_blocks.py --pack-id <new-id>
   ```
   and checking that all inherited files resolve cleanly.
7. If the new pack was inspired by a reference slide, also add at least one compact example to `references/prompt_example_library.md`.

## Naming conventions

- IDs: lowercase + hyphen only (e.g., `calm-minimal`, `warm-editorial`).
- Block files use numeric prefix to enforce stable load order.
- Keep each block narrowly scoped:
  - `10`: palette/text-treatment/light/layout-family compatibility
  - `20`: recurring motif language
  - `30`: deck-level consistency locks
  - `40`: scene selection bias and exclusions
