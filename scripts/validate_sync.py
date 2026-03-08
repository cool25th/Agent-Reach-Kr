#!/usr/bin/env python3
"""Validate fork-specific documentation and code sync assumptions."""

from __future__ import annotations

import re
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_RAW_PREFIX = "https://raw.githubusercontent.com/Panniantong/agent-reach/main"
DOC_FILES = [
    ROOT / "README.md",
    ROOT / "docs" / "install.md",
    ROOT / "docs" / "update.md",
    ROOT / "docs" / "README_en.md",
    ROOT / "agent_reach" / "skill" / "SKILL.md",
]
RAW_URL_EXPECTATIONS = {
    ROOT / "README.md": ("docs/install.md", "docs/update.md"),
    ROOT / "docs" / "install.md": ("docs/install.md",),
    ROOT / "docs" / "update.md": ("docs/update.md",),
    ROOT / "docs" / "README_en.md": ("docs/install.md", "docs/update.md"),
    ROOT / "agent_reach" / "skill" / "SKILL.md": ("docs/install.md",),
}
PROVIDER_EXPECTATIONS = {
    "exa": ("agent_reach/channels/exa_search.py", "ExaSearchChannel"),
    "xiaohongshu": ("agent_reach/channels/xiaohongshu.py", "XiaoHongShuChannel"),
    "weibo": ("agent_reach/channels/weibo.py", "WeiboChannel"),
    "douyin": ("agent_reach/channels/douyin.py", "DouyinChannel"),
    "linkedin": ("agent_reach/channels/linkedin.py", "LinkedInChannel"),
    "bosszhipin": ("agent_reach/channels/bosszhipin.py", "BossZhipinChannel"),
}


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def parse_repo_slug(remote_url: str) -> str | None:
    if remote_url.startswith("git@github.com:"):
        slug = remote_url.split(":", 1)[1]
    elif remote_url.startswith("https://github.com/"):
        slug = remote_url.split("https://github.com/", 1)[1]
    elif remote_url.startswith("http://github.com/"):
        slug = remote_url.split("http://github.com/", 1)[1]
    else:
        return None

    slug = slug.removesuffix(".git").strip("/")
    return slug or None


def expected_raw_prefix() -> str:
    env_slug = os.environ.get("EXPECTED_REPO_SLUG")
    if env_slug:
        return f"https://raw.githubusercontent.com/{env_slug}/main"

    remote_url = run_git("config", "--get", "remote.origin.url")
    slug = parse_repo_slug(remote_url)
    if not slug:
        raise RuntimeError(f"Could not infer origin repo slug from remote URL: {remote_url}")
    return f"https://raw.githubusercontent.com/{slug}/main"


def extract_configure_choices(cli_text: str) -> set[str]:
    match = re.search(
        r'p_conf\.add_argument\("key".*?choices=\[(.*?)\]',
        cli_text,
        re.DOTALL,
    )
    if not match:
        raise RuntimeError("Could not find configure choices in agent_reach/cli.py")
    return set(re.findall(r'"([^"]+)"', match.group(1)))


def find_documented_configure_keys(text: str) -> set[str]:
    keys = set(re.findall(r"agent-reach configure ([a-z0-9-]+)", text))
    return {key for key in keys if not key.startswith("--")}


def find_documented_mcporter_providers(text: str) -> set[str]:
    return set(re.findall(r"mcporter call '([a-z_]+)\.", text))


def main() -> int:
    errors: list[str] = []
    raw_prefix = expected_raw_prefix()
    registry_text = (ROOT / "agent_reach" / "channels" / "__init__.py").read_text()
    cli_text = (ROOT / "agent_reach" / "cli.py").read_text()
    supported_config_keys = extract_configure_choices(cli_text)

    for path in DOC_FILES:
        text = path.read_text()
        if UPSTREAM_RAW_PREFIX in text:
            errors.append(f"{path.relative_to(ROOT)} still points to upstream raw docs")

        for suffix in RAW_URL_EXPECTATIONS.get(path, ()):
            expected = f"{raw_prefix}/{suffix}"
            if expected not in text:
                errors.append(f"{path.relative_to(ROOT)} is missing expected raw link: {expected}")

        documented_keys = find_documented_configure_keys(text)
        missing_keys = sorted(documented_keys - supported_config_keys)
        if missing_keys:
            errors.append(
                f"{path.relative_to(ROOT)} documents unsupported configure keys: {', '.join(missing_keys)}"
            )

        documented_providers = find_documented_mcporter_providers(text)
        for provider in sorted(documented_providers & PROVIDER_EXPECTATIONS.keys()):
            file_path, class_name = PROVIDER_EXPECTATIONS[provider]
            if not (ROOT / file_path).exists():
                errors.append(
                    f"{path.relative_to(ROOT)} references '{provider}', but {file_path} does not exist"
                )
            if class_name not in registry_text:
                errors.append(
                    f"{path.relative_to(ROOT)} references '{provider}', but {class_name} is not in channel registry"
                )

    install_text = (ROOT / "docs" / "install.md").read_text()
    if "mcp-server-weibo" in install_text and "_install_weibo_deps" not in cli_text:
        errors.append("docs/install.md documents Weibo auto-install, but cli.py has no _install_weibo_deps hook")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Sync validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
