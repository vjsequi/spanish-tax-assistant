"""Mutation checks for source/skill integrity, path confinement and live defaults."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_repository import (
    ROOT,
    RepositoryError,
    check,
    inside,
    verify_disabled_defaults,
    verify_docs,
    verify_manifest,
    verify_skills,
)


class RepositoryControls(unittest.TestCase):
    def test_document_check_does_not_open_expected_answer_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("Public documentation\n")
            hidden = root / "evals/expected"
            hidden.mkdir(parents=True)
            # A canary that cannot be decoded; this is not a tax label or an answer key.
            (hidden / "canary.md").write_bytes(b"\xff\xfe")
            self.assertEqual(verify_docs(root), 1)

    def test_actual_foundation_is_consistent(self) -> None:
        result = check()
        self.assertGreaterEqual(result["imported_sources"], 2)
        self.assertEqual(result["reviewed_skill_files"], 4)

    def test_source_mutation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.txt"
            source.write_text("reviewed source\n")
            manifest = {
                "schema_version": 1,
                "entries": [
                    {
                        "destination": "source.txt",
                        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                    }
                ],
            }
            (root / "manifest.json").write_text(json.dumps(manifest))
            self.assertEqual(verify_manifest(root, "manifest.json"), 1)
            source.write_text("unreviewed replacement\n")
            with self.assertRaisesRegex(RepositoryError, "Source drift"):
                verify_manifest(root, "manifest.json")

    def test_manifest_cannot_read_outside_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            (root.parent / "outside.txt").write_text("outside")
            with self.assertRaisesRegex(RepositoryError, "leaves repository"):
                inside(root, "../outside.txt")

    def test_symlink_cannot_bypass_source_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            target = root.parent / "outside.txt"
            target.write_text("outside")
            (root / "link.txt").symlink_to(target)
            with self.assertRaisesRegex(RepositoryError, "Symbolic link"):
                inside(root, "link.txt")

    def test_live_defaults_reject_bool_as_call_count(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "config").mkdir()
            policy = json.loads((ROOT / "config/live-policy.json").read_text())
            policy["authorised_calls"] = False
            (root / "config/live-policy.json").write_text(json.dumps(policy))
            with self.assertRaisesRegex(RepositoryError, "must be an integer"):
                verify_disabled_defaults(root)

    def test_live_defaults_reject_inference_enablement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "config").mkdir()
            policy = json.loads((ROOT / "config/live-policy.json").read_text())
            policy["inference_enabled"] = True
            (root / "config/live-policy.json").write_text(json.dumps(policy))
            with self.assertRaisesRegex(RepositoryError, "Unexpected authority"):
                verify_disabled_defaults(root)

    def test_unreviewed_skill_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skills = root / ".agents/skills"
            skills.mkdir(parents=True)
            manifest_dir = root / "docs/security"
            manifest_dir.mkdir(parents=True)
            reviewed = skills / "reviewed.md"
            reviewed.write_text("reviewed")
            manifest = {
                "schema_version": 1,
                "repository": "mattpocock/skills",
                "commit": "5beb35b040e3de97e54fa9e386d7e42d15c295c2",
                "entries": [
                    {
                        "destination": ".agents/skills/reviewed.md",
                        "sha256": hashlib.sha256(reviewed.read_bytes()).hexdigest(),
                    }
                ],
            }
            (manifest_dir / "skill-manifest.json").write_text(json.dumps(manifest))
            self.assertEqual(verify_skills(root), 1)
            (skills / "unreviewed-hook.sh").write_text("echo unreviewed")
            with self.assertRaisesRegex(RepositoryError, "Unreviewed or missing"):
                verify_skills(root)


if __name__ == "__main__":
    unittest.main()
