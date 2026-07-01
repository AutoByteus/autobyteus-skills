#!/usr/bin/env python3
"""Validate the static Product Iteration Team / workflow contract.

Standard-library only. This is a static docs/config validator, not a live
Team Communication smoke test.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

Result = tuple[bool, str]

REQUIRED_TEAM_MEMBERS = {
    "product_manager": "product-manager",
    "solution_designer": "solution-designer",
    "architecture_reviewer": "architecture-reviewer",
    "implementation_engineer": "implementation-engineer",
    "code_reviewer": "code-reviewer",
    "api_e2e_engineer": "api-e2e-engineer",
    "delivery_engineer": "delivery-engineer",
}

AGENTS_REQUIRED = {
    "README.md": ["Product Iteration Plan", "send an acceptance packet to `product_manager`", "Only Product Manager `Accepted` is the product-loop verification signal"],
    "agent-teams/software-product-iteration-team/team.md": ["product-iteration mode is `Active` by default", "Product Iteration Plan", "Acceptance callback status `Sent` / `Pending` / `Blocked` records packet delivery only"],
    "agent-teams/software-engineering-team/team.md": ["product iteration is inactive by default", "Product Iteration Plan", "Callback `Sent` is not Product Manager `Accepted`"],
    "agent-teams/software-engineering-team/agents/product-manager/agent.md": ["delivery acceptance packet intake", "Product Iteration Plan/backlog ownership"],
    "agent-teams/software-engineering-team/agents/product-manager/skills/product-manager/SKILL.md": ["Product Iteration Plan", "Record the Product Manager acceptance decision: `Accepted`, `Needs Rework`, or `Blocked`", "callback `Sent` means the packet arrived, not that Product Manager accepted it"],
    "agent-teams/software-engineering-team/agents/product-manager/skills/product-manager/templates/product-iteration-plan-template.md": ["ordered candidate slices/backlog", "Product Iteration Loop Status"],
    "agent-teams/software-engineering-team/agents/product-manager/skills/product-manager/templates/product-feature-brief-template.md": ["Selected slice ID", "Product Iteration Plan reference/path"],
    "agent-teams/software-engineering-team/agents/product-manager/skills/product-manager/templates/product-acceptance-finding-template.md": ["Product Manager Acceptance Status", "Engineering Intake / `solution_designer`"],
    "agent-teams/software-engineering-team/agents/delivery-engineer/skills/delivery-engineer/SKILL.md": ["Product Manager acceptance status `Accepted`", "Acceptance Callback Status (`Sent` / `Pending` / `Blocked`) is separate", "callback `Sent` never permits product-iteration ticket archival/finalization without Product Manager `Accepted`"],
    "agent-teams/software-engineering-team/agents/delivery-engineer/skills/delivery-engineer/templates/release-deployment-report-template.md": ["Acceptance callback status: `Not Required` / `Not Started` / `Sent` / `Pending` / `Blocked`", "Product Iteration Loop Status", "only `Accepted` unlocks product-iteration ticket archival/finalization"],
}

SKILLS_REQUIRED = {
    "AGENTS.md": ["Product Manager acceptance packet for `product_manager`", "Product Manager Acceptance Status = `Accepted` is required before product-iteration archival/finalization", "Product Iteration Loop Status is separate"],
    ".codex/agents/deployment-engineer.toml": ["Product Manager Acceptance Status = `Accepted` for product-iteration runs", "Product Manager acceptance packet from the handoff summary", "Callback `Sent` is not Product Manager Acceptance Status = `Accepted`"],
    "software-engineering-workflow-skill/SKILL.md": ["applicable verification signal", "Product Manager Acceptance Status = `Accepted` for product-iteration runs", "Product Iteration Plan/backlog/cursor", "Callback `Sent` is not Product Manager `Accepted`", "Product-iteration Stage 10 sequence: handoff/release notes -> send or persist Product Manager acceptance packet -> record Acceptance Callback Status -> wait for Product Manager Acceptance Status = `Accepted` or route `Needs Rework` / `Blocked` -> archive/finalize"],
    "software-engineering-workflow-skill/agents/openai.yaml": ["Product Manager Acceptance Status = `Accepted`", "Product Iteration Plan/backlog/cursor", "Callback `Sent`/`Pending`/`Blocked`"],
    "software-engineering-workflow-skill/shared/workflow-state-template.md": ["Acceptance Callback Status", "Product Manager Acceptance Status", "Product Iteration Loop Status", "Only `Accepted` unlocks product-iteration ticket archival/finalization"],
    "software-engineering-workflow-skill/stages/00-bootstrap/bootstrap-checklist.md": ["Product Iteration Plan reference", "selected slice ID"],
    "software-engineering-workflow-skill/stages/02-requirements/requirements-refinement-guide.md": ["Product Iteration Plan reference", "Stage 10 Product Manager acceptance or user verification as applicable"],
    "software-engineering-workflow-skill/stages/10-handoff/README.md": ["Product Manager Acceptance Status = `Accepted` before ticket archival/finalization", "Callback `Sent` / `Pending` / `Blocked` or persisted packet status alone does not satisfy Product Manager acceptance"],
    "software-engineering-workflow-skill/stages/10-handoff/handoff-guide.md": ["Acceptance Callback Status", "Product Manager Acceptance Status = `Accepted` as the product-loop verification signal", "persisted packet status alone does not satisfy Product Manager acceptance"],
    "software-engineering-workflow-skill/stages/10-handoff/handoff-summary-template.md": ["Acceptance callback status: `Not Required` / `Not Started` / `Sent` / `Pending` / `Blocked`", "Product Iteration Loop Status", "only `Accepted` unlocks product-iteration ticket archival/finalization"],
}

FORBIDDEN = [
    "a acceptance packet",
    "delivery completion packet",
    "completion packet",
    "move a ticket from `in-progress` to `done` only when the user explicitly confirms",
    "after the explicit user completion/verification signal",
    "Product Manager acceptance request/status",
    "Product Manager acceptance request sent/persisted",
    "Product Manager acceptance request/acceptance tracking",
    "only on explicit user completion/verification",
    "Stage 10 user verification/finalization",
    "Acceptance request status",
    "Completion packet source / payload path",
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--skills-root", help="Skills repository root; inferred from script path when omitted.")
    p.add_argument("--agents-root", help="Agents repository root; inferred from a sibling path when omitted.")
    return p.parse_args()


def text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def infer_agents(skills_root: Path) -> Path | None:
    for candidate in (skills_root.parent / skills_root.name.replace("skills", "agents", 1), skills_root.parent / "autobyteus-agents"):
        if (candidate / "agent-teams").is_dir():
            return candidate.resolve()
    return None


def check_required(root: Path, mapping: dict[str, list[str]], label: str) -> list[Result]:
    results: list[Result] = []
    for rel, needles in mapping.items():
        body = text(root / rel)
        if body is None:
            results.append((False, f"{label}:{rel}: missing file"))
            continue
        for needle in needles:
            results.append((needle in body, f"{label}:{rel}: required text: {needle}"))
        for bad in FORBIDDEN:
            if bad in body:
                results.append((False, f"{label}:{rel}: forbidden text present: {bad}"))
    return results


def check_stage10_output_order(skills_root: Path) -> list[Result]:
    rel = "software-engineering-workflow-skill/SKILL.md"
    body = text(skills_root / rel)
    if body is None:
        return [(False, f"skills:{rel}: missing file for Stage 10 order check")]
    start_marker = "- Stage 10 (final handoff + verification/acceptance + move ticket to done + repository finalization + cleanup):"
    end_marker = "\n## Templates And References"
    start = body.find(start_marker)
    end = body.find(end_marker, start)
    if start < 0 or end < 0:
        return [(False, f"skills:{rel}: Stage 10 Output Defaults block not found")]
    block = body[start:end]
    ordered = [
        "create/update `tickets/in-progress/<ticket-name>/handoff-summary.md`",
        "send or persist the Product Manager acceptance packet before waiting for Product Manager acceptance",
        "record Acceptance Callback Status (`Sent` / `Pending` / `Blocked`) and Product Manager Acceptance Status",
        "wait for Product Manager Acceptance Status = `Accepted` before archival/finalization;",
        "Product Manager Acceptance Status `Needs Rework` or `Blocked` routes the stated issue instead of finalizing",
        "only after the applicable verification signal",
        "first move the ticket folder to `tickets/done/<ticket-name>/`",
    ]
    positions = [block.find(item) for item in ordered]
    missing = [item for item, pos in zip(ordered, positions) if pos < 0]
    if missing:
        return [(False, f"skills:{rel}: Stage 10 Output Defaults missing ordered marker(s): {missing}")]
    in_order = positions == sorted(positions)
    return [(in_order, f"skills:{rel}: Stage 10 Output Defaults order is handoff -> send/persist packet -> record statuses -> wait/route -> archive/finalize")]


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def check_json_configs(root: Path) -> list[Result]:
    results: list[Result] = []
    product = root / "agent-teams/software-product-iteration-team/team-config.json"
    normal = root / "agent-teams/software-engineering-team/team-config.json"
    pm_agent = root / "agent-teams/software-engineering-team/agents/product-manager/agent-config.json"
    try:
        product_cfg, normal_cfg, pm_cfg = load_json(product), load_json(normal), load_json(pm_agent)
    except (OSError, json.JSONDecodeError) as exc:
        return [(False, f"JSON config load failed: {exc}")]
    results.append((isinstance(product_cfg, dict) and product_cfg.get("coordinatorMemberName") == "product_manager", "Product Iteration Team coordinatorMemberName is product_manager"))
    results.append((isinstance(normal_cfg, dict) and normal_cfg.get("coordinatorMemberName") == "solution_designer", "Software Engineering Team coordinatorMemberName is solution_designer"))
    results.append((isinstance(pm_cfg, dict) and "product-manager" in pm_cfg.get("skillNames", []), "Product Manager agent config attaches product-manager skill"))
    members = {m.get("memberName"): m for m in product_cfg.get("members", []) if isinstance(m, dict)} if isinstance(product_cfg, dict) else {}
    for name, directory in REQUIRED_TEAM_MEMBERS.items():
        ref = f"team-local-agent:software-engineering-team:{directory}"
        member = members.get(name, {})
        results.append((member.get("ref") == ref and member.get("refType") == "agent", f"Product Iteration Team member {name} uses {ref}"))
        results.append(((root / "agent-teams/software-engineering-team/agents" / directory).is_dir(), f"Referenced agent directory exists for {name}"))
    return results


def main() -> int:
    args = parse_args()
    sr = Path(args.skills_root).expanduser().resolve() if args.skills_root else Path(__file__).resolve().parents[2]
    ar = Path(args.agents_root).expanduser().resolve() if args.agents_root else infer_agents(sr)
    results: list[Result] = []
    if sr.is_dir():
        results += check_required(sr, SKILLS_REQUIRED, "skills")
        results += check_stage10_output_order(sr)
    else:
        results.append((False, f"skills root missing: {sr}"))
    if ar and ar.is_dir():
        results += check_json_configs(ar)
        results += check_required(ar, AGENTS_REQUIRED, "agents")
    else:
        results.append((False, f"agents root missing: {ar}"))
    for ok, message in results:
        print(f"{'PASS' if ok else 'FAIL'}: {message}")
    failures = [m for ok, m in results if not ok]
    if failures:
        print(f"\nproduct-iteration loop contract validation failed: {len(failures)} issue(s)", file=sys.stderr)
        return 1
    print("\nproduct-iteration loop contract validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
