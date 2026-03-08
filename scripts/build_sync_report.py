#!/usr/bin/env python3
"""Build a markdown summary for upstream sync PRs."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRANSLATABLE_PREFIXES = (
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "TRANSLATION_STATUS.md",
    "docs/",
    "agent_reach/guides/",
    "agent_reach/skill/SKILL.md",
)


def run_git(*args: str) -> list[str]:
    output = subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    return [line for line in output.splitlines() if line.strip()]


def try_git(*args: str) -> list[str]:
    try:
        return run_git(*args)
    except subprocess.CalledProcessError:
        return []


def is_translatable(path: str) -> bool:
    return path.startswith(TRANSLATABLE_PREFIXES)


def format_file_list(title: str, paths: list[str]) -> list[str]:
    lines = [f"### {title}"]
    if not paths:
        lines.append("- None")
        return lines

    lines.extend(f"- `{path}`" for path in paths)
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="Merge-base commit")
    parser.add_argument("--upstream", default="upstream/main", help="Upstream ref")
    args = parser.parse_args()

    merge_base = args.base.strip()
    if not merge_base:
        merge_base_lines = try_git("merge-base", "HEAD", args.upstream)
        merge_base = merge_base_lines[0] if merge_base_lines else ""

    if merge_base:
        changed = run_git("diff", "--name-only", f"{merge_base}..{args.upstream}")
        merge_base_display = merge_base
    else:
        changed = run_git("diff", "--name-only", "HEAD", args.upstream)
        merge_base_display = "unrelated-history"

    translatable = [path for path in changed if is_translatable(path)]
    code = [path for path in changed if path not in translatable]
    upstream_head = run_git("rev-parse", args.upstream)[0]

    lines: list[str] = [
        "## Upstream Sync Summary",
        "",
        f"- Upstream head: `{upstream_head}`",
        f"- Merge base: `{merge_base_display}`",
        f"- Total changed files: `{len(changed)}`",
        "",
    ]
    lines.extend(format_file_list("Code And Config Changes From Upstream", code))
    lines.append("")
    lines.extend(format_file_list("Translated Docs That Changed Upstream", translatable))
    lines.append("")
    if merge_base:
        lines.append(
            "Translated docs are kept from the fork on conflict. Review the files above and port upstream doc changes manually when needed."
        )
    else:
        lines.append(
            "This fork does not share Git history with upstream yet. The first sync PR is a bootstrap sync and should be reviewed carefully before merge."
        )

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
