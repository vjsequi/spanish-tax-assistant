"""Reference and fixture mutation tests; no expected tax labels are read."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.build_review_cases import build
from scripts.check_repository import ROOT, RepositoryError
from scripts.check_tax_pack import check, input_document, input_payload, no_float, specification
from scripts.package_tax_review import review_inventory
from scripts.pin_official_sources import approved_url, verify_selected_version


class TaxPackControls(unittest.TestCase):
    def test_review_package_excludes_unlisted_files_and_cases(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            records = {
                "data/rules/2025/manifest.json": {
                    "entries": [{"destination": "data/rules/2025/originals/selected.pdf"}]
                },
                "third_party/development-licences.json": {"entries": []},
                "evals/inputs/manifest.json": {
                    "cases": [{"case_id": "C001", "case_file": "evals/inputs/C001/case.json"}]
                },
                "evals/inputs/C001/case.json": {"documents": [{"file": "documents/D001.pdf"}]},
            }
            for name, payload in records.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(payload))
            for name in (
                "data/rules/2025/originals/unlisted.pdf",
                "evals/inputs/unlisted.pdf",
                "evals/inputs/C999/documents/D001.pdf",
            ):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"unlisted canary, not taxpayer data")
            names = review_inventory(root)
            self.assertIn("evals/inputs/C001/documents/D001.pdf", names)
            self.assertIn("data/rules/2025/originals/selected.pdf", names)
            self.assertFalse(any("unlisted" in name or "C999" in name for name in names))

    def test_retained_pack_has_integrity_without_tax_approval(self) -> None:
        result = check()
        self.assertEqual(result["pinned_sources"], 15)
        self.assertEqual(result["synthetic_cases"], 20)
        self.assertEqual(result["open_tax_questions"], 9)

    def test_boe_silent_latest_fallback_is_rejected(self) -> None:
        html = b'<html><a class="version-selected" href="?id=BOE-A-1&p=20260613">latest</a></html>'
        with self.assertRaisesRegex(RepositoryError, "different consolidation"):
            verify_selected_version({"selected_version": "20250724"}, html)

    def test_boe_selected_edition_is_required(self) -> None:
        with self.assertRaisesRegex(RepositoryError, "different consolidation"):
            verify_selected_version({"selected_version": "20250724"}, b"<html>no edition</html>")

    def test_official_sources_cannot_redirect_outside_allowlist(self) -> None:
        for url in (
            "http://www.boe.es/example",
            "https://www.boe.es.attacker.invalid/example",
            "https://user:password@www.boe.es/example",
            "https://www.boe.es:444/example",
            "https://example.invalid/",
        ):
            with self.subTest(url=url), self.assertRaises(RepositoryError):
                approved_url(url)

    def test_expected_values_cannot_enter_case_metadata(self) -> None:
        payload = {
            "schema_version": 1,
            "case_id": "C001",
            "classification": "synthetic_development_input",
            "tax_year": 2025,
            "jurisdiction": "ES-IB",
            "review_status": "not_independently_reviewed",
            "fact_confirmation": "pending",
            "documents": [],
            "expected_final_tax": "123.45",
        }
        with self.assertRaisesRegex(RepositoryError, "answer/authoring"):
            input_payload(payload)

    def test_case_path_escape_is_rejected_before_any_target_read(self) -> None:
        document = {
            "id": "D001",
            "file": "../../expected/example.json",
            "media_type": "application/pdf",
            "sha256": "0" * 64,
            "pages": 1,
            "declared_source_type": "salary_certificate",
        }
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RepositoryError, "own document directory"):
                input_document(Path(directory), "C001", document)

    def test_binary_float_cannot_become_a_tax_parameter(self) -> None:
        with self.assertRaisesRegex(RepositoryError, "binary floating"):
            no_float({"nested": [{"rate": 0.095}]})

    def test_reviewed_sources_cannot_be_regenerated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "evals/authoring").mkdir(parents=True)
            (root / "evals/inputs").mkdir(parents=True)
            (root / "evals/authoring/cases.json").write_text(
                json.dumps({"no_private_reference_used": True, "review_status": "not_reviewed"})
            )
            (root / "evals/inputs/manifest.json").write_text(
                json.dumps({"review_status": "independently_reviewed"})
            )
            with self.assertRaisesRegex(RepositoryError, "new version"):
                build(root)

    def test_field_page_mutation_is_detected_against_retained_form(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            base = root / "data/rules/2025"
            (base / "originals").mkdir(parents=True)
            for filename in (
                "manifest.json",
                "calculation-stages.json",
                "aeat-fields.json",
                "rule-register.json",
                "review-questions.json",
            ):
                shutil.copy2(ROOT / "data/rules/2025" / filename, base / filename)
            shutil.copy2(
                ROOT / "data/rules/2025/originals/boe-modelo-100-2025.pdf",
                base / "originals/boe-modelo-100-2025.pdf",
            )
            (root / "docs/requirements").mkdir(parents=True)
            shutil.copy2(
                ROOT / "docs/requirements/requirements.json",
                root / "docs/requirements/requirements.json",
            )
            data = json.loads((base / "aeat-fields.json").read_text())
            data["fields"][0]["physical_page"] = 1
            (base / "aeat-fields.json").write_text(json.dumps(data))
            with self.assertRaisesRegex(RepositoryError, "absent from the declared"):
                specification(root)


if __name__ == "__main__":
    unittest.main()
