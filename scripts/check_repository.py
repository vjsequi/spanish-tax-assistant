"""Validate repository controls; this does not evaluate tax or model quality."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", ".runtime", ".private", "node_modules", "__pycache__"}
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
LINK = re.compile(r"\[[^\]]+\]\(([^)\n]+)\)")


class RepositoryError(ValueError):
    """A foundation invariant is not satisfied."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RepositoryError(message)


def inside(root: Path, relative: str) -> Path:
    require(not Path(relative).is_absolute(), f"Absolute manifest path: {relative}")
    candidate = root / relative
    current = root
    for part in Path(relative).parts:
        current = current / part
        require(not current.is_symlink(), f"Symbolic link is not allowed: {relative}")
    resolved = candidate.resolve()
    require(resolved.is_relative_to(root.resolve()), f"Path leaves repository: {relative}")
    require(resolved.is_file(), f"Missing file: {relative}")
    return resolved


def read_object(path: Path) -> dict[str, Any]:
    value: Any = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"Expected JSON object: {path.name}")
    assert isinstance(value, dict)
    return value


def verify_manifest(root: Path, relative: str) -> int:
    manifest = read_object(inside(root, relative))
    require(manifest.get("schema_version") == 1, f"Unknown manifest version: {relative}")
    entries = manifest.get("entries")
    require(isinstance(entries, list) and bool(entries), f"No manifest entries: {relative}")
    assert isinstance(entries, list)
    destinations: set[str] = set()
    for entry in entries:
        require(isinstance(entry, dict), "Invalid manifest entry")
        require(isinstance(entry.get("destination"), str), "Missing destination")
        destination = entry["destination"]
        require(destination not in destinations, f"Repeated destination: {destination}")
        destinations.add(destination)
        expected = entry.get("sha256")
        require(isinstance(expected, str) and SHA256.fullmatch(expected) is not None, "Bad hash")
        actual = hashlib.sha256(inside(root, destination).read_bytes()).hexdigest()
        require(actual == expected, f"Source drift: {destination}")
    return len(entries)


def verify_disabled_defaults(root: Path) -> None:
    policy = read_object(inside(root, "config/live-policy.json"))
    require(policy.get("schema_version") == 1, "Unknown live-policy version")
    for flag in (
        "inference_enabled",
        "cloud_provisioning_authorised",
        "aeat_operations_authorised",
    ):
        require(policy.get(flag) is False, f"Unexpected authority at foundation stage: {flag}")
    require(type(policy.get("authorised_calls")) is int, "Call allowance must be an integer")
    require(policy["authorised_calls"] == 0, "No live calls are authorised")
    require(policy.get("monetary_budget_eur") is None, "No live budget is set")
    for environment in ("development", "staging", "production"):
        data = read_object(inside(root, f"config/environments/{environment}.json"))
        require(data.get("name") == environment, "Environment name mismatch")
        require(data.get("state") == "unprovisioned", "Foundation has no deployed environments")
        require(data.get("inference_enabled") is False, "Environment enables inference")


def verify_skills(root: Path) -> int:
    relative = "docs/security/skill-manifest.json"
    manifest = read_object(inside(root, relative))
    require(manifest.get("repository") == "mattpocock/skills", "Wrong skill upstream")
    require(
        manifest.get("commit") == "5beb35b040e3de97e54fa9e386d7e42d15c295c2",
        "Skill revision requires a new review",
    )
    count = verify_manifest(root, relative)
    expected = {entry["destination"] for entry in manifest["entries"]}
    actual: set[str] = set()
    for path in (root / ".agents" / "skills").rglob("*"):
        require(not path.is_symlink(), "Skill links are not allowed")
        if path.is_file():
            actual.add(path.relative_to(root).as_posix())
    require(actual == expected, "Unreviewed or missing skill file")
    return count


def verify_docs(root: Path) -> int:
    count = 0
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP or part.endswith("_cache") for part in path.relative_to(root).parts):
            continue
        require(not path.is_symlink(), "Markdown symbolic links are not allowed")
        text = path.read_text(encoding="utf-8")
        require(text.count("```") % 2 == 0, f"Unbalanced code fences: {path.name}")
        # Instruction-bearing vendor files are verified byte-for-byte by their own manifest.
        if ".agents" not in path.relative_to(root).parts:
            require("[[" not in text, f"Unconverted vault link: {path.name}")
        for target in LINK.findall(text):
            target = target.strip("<>")
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            relative = (path.parent / target).relative_to(root).as_posix()
            inside(root, relative)
        count += 1
    return count


def check(root: Path = ROOT) -> dict[str, int]:
    root = root.resolve()
    ignore = inside(root, ".gitignore").read_text(encoding="utf-8").splitlines()
    require(
        all(pattern in ignore for pattern in (".env", ".runtime/", ".private/")),
        "Private files need explicit ignore entries",
    )
    sources = verify_manifest(root, "docs/context/source-manifest.json")
    skills = verify_skills(root)
    verify_disabled_defaults(root)
    register = read_object(inside(root, "docs/requirements/requirements.json"))
    requirements = register.get("requirements", [])
    require(isinstance(requirements, list) and bool(requirements), "No draft requirements")
    ids = [item["id"] for item in requirements]
    require(len(ids) == len(set(ids)), "Repeated requirement ID")
    status = read_object(inside(root, "docs/process/status.json"))
    require(status.get("model_evaluation") == "not_run", "No tax model evaluation exists yet")
    require(status.get("deployment") == "unprovisioned", "No deployment exists yet")
    return {
        "markdown_files": verify_docs(root),
        "imported_sources": sources,
        "reviewed_skill_files": skills,
        "draft_requirements": len(ids),
    }


def main() -> int:
    try:
        result = check()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Repository check failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    print("Foundation controls verified; no tax correctness, model quality or deployment claimed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
