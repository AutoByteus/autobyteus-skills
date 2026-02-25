# Style-pack system (modular style architecture)

Purpose: treat style as a reusable folderized template pack, not scattered defaults.

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

## How to use in practice

1. Select style pack ID from `style-pack-catalog.md`.
2. Compose blocks with:
   ```bash
   python3 scripts/compose_style_pack_blocks.py --pack-id <style-pack-id>
   ```
3. Paste output under the style section of each slide prompt.
4. Keep the same style pack for all slides in one deck.

## Add a new style pack

1. Create scaffold:
   ```bash
   python3 scripts/create_style_pack.py --pack-id <new-id> --display-name "<Name>" --keywords "关键词1,关键词2" --scene-tags "tag1,tag2"
   ```
2. Add `manifest.toml` with:
   - `id`, `display_name`, `inherits`, `intent_keywords`, `default_scene_tags`.
3. Add `10/20/30/40` blocks to define full style behavior.
4. Register the pack in `style-pack-catalog.md`.
5. If needed, add matching scenes in `scene-catalog.md` using `scene-entry-template.md`.
6. Validate with the skill validator.

## Naming conventions

- IDs: lowercase + hyphen only (e.g., `calm-minimal`, `warm-editorial`).
- Block files use numeric prefix to enforce stable load order.
- Keep each block narrowly scoped:
  - `10`: palette/panel/light/typography look
  - `20`: recurring motif language
  - `30`: deck-level consistency locks
  - `40`: scene selection bias and exclusions
