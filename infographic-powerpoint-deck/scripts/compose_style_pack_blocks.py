#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path


def load_manifest(pack_dir: Path) -> dict:
    manifest_path = pack_dir / "manifest.toml"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Missing manifest: {manifest_path}")

    data: dict = {}
    for raw_line in manifest_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, raw_value = line.split("=", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        try:
            value = ast.literal_eval(raw_value)
        except Exception:
            value = raw_value.strip('"').strip("'")
        data[key] = value
    return data


def resolve_pack_order(pack_id: str, packs_root: Path, visited: set[str], stack: set[str]) -> list[str]:
    if pack_id in stack:
        cycle = " -> ".join(list(stack) + [pack_id])
        raise ValueError(f"Cyclic style-pack inheritance detected: {cycle}")
    if pack_id in visited:
        return []

    pack_dir = packs_root / pack_id
    if not pack_dir.is_dir():
        raise FileNotFoundError(f"Style pack not found: {pack_dir}")

    stack.add(pack_id)
    manifest = load_manifest(pack_dir)
    inherited = manifest.get("inherits", [])
    if isinstance(inherited, str):
        inherited = [inherited]

    order: list[str] = []
    for parent_id in inherited:
        order.extend(resolve_pack_order(parent_id, packs_root, visited, stack))

    order.append(pack_id)
    visited.add(pack_id)
    stack.remove(pack_id)
    return order


def pack_block_files(pack_dir: Path) -> list[Path]:
    return sorted(
        [path for path in pack_dir.glob("*.md") if path.name[:2].isdigit()],
        key=lambda path: path.name,
    )


def unfence_markdown_block(text: str) -> list[str]:
    lines = text.rstrip().splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return lines


def prompt_ready_block(text: str) -> str:
    lines = unfence_markdown_block(text)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines:
        return ""

    first = lines[0].strip()
    if (
        first.startswith("Style Pack:")
        or first.startswith("Motif (")
        or first.startswith("Consistency Lock (")
        or first.startswith("Scene Bias (")
        or first.startswith("Base constraints (")
    ):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines.pop(0)

    return "\n".join(lines).strip()


def list_packs(packs_root: Path) -> str:
    rows: list[str] = []
    rows.append("Available style packs:")
    for pack_dir in sorted([path for path in packs_root.iterdir() if path.is_dir()], key=lambda path: path.name):
        manifest_path = pack_dir / "manifest.toml"
        if not manifest_path.exists():
            continue
        manifest = load_manifest(pack_dir)
        pack_id = manifest.get("id", pack_dir.name)
        display_name = manifest.get("display_name", "")
        keywords = manifest.get("intent_keywords", [])
        if isinstance(keywords, str):
            keywords = [keywords]
        kw = ", ".join(keywords[:6])
        rows.append(f"- {pack_id} ({display_name}) :: {kw}".rstrip())
    return "\n".join(rows) + "\n"


def compose_blocks(pack_id: str, packs_root: Path, *, annotated: bool) -> str:
    order = resolve_pack_order(pack_id, packs_root, visited=set(), stack=set())
    chunks: list[str] = []

    if annotated:
        chunks.append(f"# Style Pack Bundle: {pack_id}")
        chunks.append("")
        chunks.append("Use this full bundle under the style section of each slide prompt.")
        chunks.append("")

        for current_id in order:
            pack_dir = packs_root / current_id
            chunks.append(f"## Pack: {current_id}")
            for block_path in pack_block_files(pack_dir):
                relative = block_path.relative_to(packs_root.parent)
                chunks.append(f"### Source: `{relative}`")
                chunks.append(block_path.read_text(encoding="utf-8").rstrip())
                chunks.append("")
    else:
        for current_id in order:
            pack_dir = packs_root / current_id
            for block_path in pack_block_files(pack_dir):
                cleaned = prompt_ready_block(block_path.read_text(encoding="utf-8"))
                if cleaned:
                    chunks.append(cleaned)
                    chunks.append("")

    return "\n".join(chunks).rstrip() + "\n"


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    default_root = script_dir.parent / "references" / "style-packs"

    parser = argparse.ArgumentParser(description="Compose inherited style-pack blocks for prompt usage.")
    parser.add_argument("--pack-id", default="", help="Style pack ID, e.g. editorial-light")
    parser.add_argument("--list", action="store_true", help="List available style packs")
    parser.add_argument("--annotated", action="store_true", help="Include pack/source headers for debugging instead of prompt-ready raw blocks")
    parser.add_argument("--packs-root", default=str(default_root), help="Path to style-packs directory")
    parser.add_argument("--out", default="", help="Write composed output to file (optional)")
    args = parser.parse_args()

    packs_root = Path(args.packs_root).resolve()
    if not packs_root.is_dir():
        print(f"Invalid packs root: {packs_root}", file=sys.stderr)
        return 1

    if args.list:
        listing = list_packs(packs_root)
        if args.out:
            output_path = Path(args.out).resolve()
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(listing, encoding="utf-8")
        else:
            print(listing, end="")
        return 0

    if not args.pack_id:
        print("Missing --pack-id (or use --list).", file=sys.stderr)
        return 1

    try:
        composed = compose_blocks(args.pack_id, packs_root, annotated=args.annotated)
    except Exception as error:
        print(str(error), file=sys.stderr)
        return 1

    if args.out:
        output_path = Path(args.out).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(composed, encoding="utf-8")
    else:
        print(composed, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
