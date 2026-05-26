#!/usr/bin/env python3
"""Resolve DEW skill customization.

Reads a skill's customize.toml and optional project overrides from:

  _dew/custom/<skill-name>.toml
  _dew/custom/<skill-name>.user.toml

Then prints the requested top-level table as JSON.

Usage:
  python3 _dew/scripts/resolve_customization.py --skill <skill-root> --key workflow
  python3 _dew/scripts/resolve_customization.py --skill <skill-root> --key agent
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None


def load_toml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    if tomllib is None:
        raise RuntimeError("tomllib is unavailable. Use Python 3.11+ for DEW customization resolution.")
    with path.open("rb") as handle:
        return tomllib.load(handle)


def deep_merge(base: Any, override: Any) -> Any:
    if isinstance(base, dict) and isinstance(override, dict):
        merged = dict(base)
        for key, value in override.items():
            merged[key] = deep_merge(merged.get(key), value)
        return merged

    if isinstance(base, list) and isinstance(override, list):
        return base + override

    if override is None:
        return base

    return override


def find_project_root(start: Path) -> Path:
    current = start.resolve()
    if current.is_file():
        current = current.parent

    for candidate in [current, *current.parents]:
        if (candidate / "_dew").exists():
            return candidate

    env_root = os.environ.get("DEW_PROJECT_ROOT")
    if env_root:
        return Path(env_root).resolve()

    return Path.cwd().resolve()


def resolve(skill_root: Path, key: str, project_root: Path | None = None) -> Dict[str, Any]:
    skill_root = skill_root.resolve()
    if project_root is None:
        project_root = find_project_root(Path.cwd())
    else:
        project_root = project_root.resolve()

    skill_name = skill_root.name
    base_path = skill_root / "customize.toml"
    team_override_path = project_root / "_dew" / "custom" / f"{skill_name}.toml"
    user_override_path = project_root / "_dew" / "custom" / f"{skill_name}.user.toml"

    merged: Dict[str, Any] = {}
    for path in [base_path, team_override_path, user_override_path]:
        data = load_toml(path)
        if data:
            merged = deep_merge(merged, data)

    requested = merged.get(key, {})
    if not isinstance(requested, dict):
        requested = {"value": requested}

    return {
        "skill": skill_name,
        "skill_root": str(skill_root),
        "project_root": str(project_root),
        "key": key,
        "resolved": requested,
        "sources": {
            "base": str(base_path),
            "team_override": str(team_override_path) if team_override_path.exists() else None,
            "user_override": str(user_override_path) if user_override_path.exists() else None,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve DEW skill customization.")
    parser.add_argument("--skill", required=True, help="Path to installed skill directory")
    parser.add_argument("--key", required=True, help="Top-level customize.toml key to resolve, e.g. workflow or agent")
    parser.add_argument("--project-root", default=None, help="Project root containing _dew")
    args = parser.parse_args()

    try:
        result = resolve(
            skill_root=Path(args.skill),
            key=args.key,
            project_root=Path(args.project_root) if args.project_root else None,
        )
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
