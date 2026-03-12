#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def normalize_list(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def validate_pack_id(pack_id: str) -> bool:
    return re.fullmatch(r"[a-z0-9-]+", pack_id) is not None


def write_file(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    default_root = script_dir.parent / "references" / "style-packs"

    parser = argparse.ArgumentParser(description="Scaffold a new style pack.")
    parser.add_argument("--pack-id", required=True, help="New pack id, e.g. warm-minimal")
    parser.add_argument("--display-name", required=True, help="Display name, e.g. Warm Minimal")
    parser.add_argument("--keywords", default="", help="Comma-separated intent keywords")
    parser.add_argument("--scene-tags", default="", help="Comma-separated default scene tags")
    parser.add_argument("--inherits", default="base-core", help="Comma-separated inherited pack IDs")
    parser.add_argument("--packs-root", default=str(default_root), help="Path to style-packs directory")
    parser.add_argument("--force", action="store_true", help="Overwrite if pack folder exists")
    args = parser.parse_args()

    if not validate_pack_id(args.pack_id):
        print("Invalid --pack-id. Use lowercase letters, digits, hyphens only.", file=sys.stderr)
        return 1

    packs_root = Path(args.packs_root).resolve()
    packs_root.mkdir(parents=True, exist_ok=True)
    pack_dir = packs_root / args.pack_id

    if pack_dir.exists() and not args.force:
        print(f"Pack already exists: {pack_dir}. Use --force to overwrite.", file=sys.stderr)
        return 1

    pack_dir.mkdir(parents=True, exist_ok=True)

    keywords = normalize_list(args.keywords)
    tags = normalize_list(args.scene_tags)
    inherits = normalize_list(args.inherits) or ["base-core"]

    manifest = [
        f'id = "{args.pack_id}"',
        f'display_name = "{args.display_name}"',
        "inherits = [" + ", ".join(f'"{item}"' for item in inherits) + "]",
        "intent_keywords = [" + ", ".join(f'"{item}"' for item in keywords) + "]",
        "default_scene_tags = [" + ", ".join(f'"{item}"' for item in tags) + "]",
    ]
    write_file(pack_dir / "manifest.toml", "\n".join(manifest))

    write_file(
        pack_dir / "10-style-profile.md",
        """```text
Style Pack: <pack-id> (<display name>)
- Layout behavior: preferred layout families (direct-overlay-first / split-panel / mixed), plus split-panel proportions only if relevant. If the pack is cinematic/editorial/warm/story-led, describe split-panel as a fallback rather than a default.
- Color palette: primary background, body text, accent color.
- Text treatment: if split-panel fallback is used, describe that panel style; also describe full-bleed direct-overlay behavior with no obvious caption box by default.
- Lighting: brightness, contrast, and whether vignette is allowed.
- Background bias: preferred visual semantics or scene classes.
```""",
    )
    write_file(
        pack_dir / "20-motif.md",
        """```text
Motif (<pack-id>):
- Repeated symbol / texture element 1.
- Repeated symbol / texture element 2.
- Repeated symbol / texture element 3.
- Repeated symbol / texture element 4.
```""",
    )
    write_file(
        pack_dir / "30-consistency.md",
        """```text
Consistency Lock (<pack-id>):
- Cross-slide layout consistency rules.
- Type hierarchy and sizing consistency rules.
- Icon and color consistency rules.
- Readability hard constraints and forbidden elements.
```""",
    )
    write_file(
        pack_dir / "40-scene-bias.md",
        """```text
Scene Bias (<pack-id>):
- Preferred scene tags: tag1, tag2, tag3.
- Recommended scene IDs: scene-1, scene-2, scene-3.
- Forbidden: visual styles that do not fit this pack.
```""",
    )

    print(f"Created style pack scaffold: {pack_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
