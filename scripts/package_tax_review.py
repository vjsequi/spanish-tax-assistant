"""Package an explicit public/synthetic review inventory; never include private or expected data."""

from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

from scripts.check_repository import ROOT, inside, read_object, require
from scripts.check_tax_pack import check

DESTINATION = "output/review/tax-2025-review-pack.zip"


def review_inventory(root: Path) -> set[str]:
    names: set[str] = {
        "docs/requirements/tax-2025.md",
        "docs/requirements/requirements.json",
        "docs/product/acceptance.md",
        "evals/review/reviewer-guide.md",
        "evals/review/review-request.json",
        "evals/review/answer-template.json",
        "output/pdf/tax-2025-review-guide.pdf",
        "THIRD_PARTY_NOTICES.md",
        "data/rules/2025/README.md",
        "data/rules/2025/catalog.json",
        "data/rules/2025/manifest.json",
        "data/rules/2025/calculation-stages.json",
        "data/rules/2025/aeat-fields.json",
        "data/rules/2025/rule-register.json",
        "data/rules/2025/review-questions.json",
        "evals/inputs/README.md",
        "evals/inputs/manifest.json",
        "third_party/development-licences.json",
    }
    for receipt in ("data/rules/2025/manifest.json", "third_party/development-licences.json"):
        names.update(
            entry["destination"] for entry in read_object(inside(root, receipt))["entries"]
        )
    for entry in read_object(inside(root, "evals/inputs/manifest.json"))["cases"]:
        names.add(entry["case_file"])
        case = read_object(inside(root, entry["case_file"]))
        names.update(
            f"evals/inputs/{entry['case_id']}/{document['file']}" for document in case["documents"]
        )
    return names


def write_entry(archive: zipfile.ZipFile, name: str, raw: bytes | str) -> None:
    info = zipfile.ZipInfo(name, date_time=(2026, 10, 21, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    archive.writestr(info, raw)


def package(root: Path = ROOT) -> Path:
    check(root)
    files = []
    for name in sorted(review_inventory(root)):
        require(
            not {".private", ".runtime", "expected", "authoring"}.intersection(Path(name).parts),
            "Review package cannot include private, answer or construction data",
        )
        source = inside(root, name)
        files.append({"path": name, "sha256": hashlib.sha256(source.read_bytes()).hexdigest()})
    target = root / DESTINATION
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        write_entry(
            archive,
            "START-HERE.txt",
            "IRPF 2025 Illes Balears - independent synthetic review request\n"
            "Start with output/pdf/tax-2025-review-guide.pdf and "
            "evals/review/reviewer-guide.md.\n"
            "Source documents are in evals/inputs/C001 ... C020/documents.\n"
            "Rule/field/stage maps, open questions and unmodified official references are "
            "in data/rules/2025.\n"
            "All cases and rule contracts remain pending independent review. "
            "No expected tax answers are included.\n"
            "Complete a COPY of evals/review/answer-template.json in a separate review "
            "workspace; keep answers away from application/model inputs.\n"
            "This is a focused review package; contextual repository links may refer to "
            "files in the full repository at https://github.com/vjsequi/spanish-tax-assistant.\n"
            "Do not add private taxpayer documents to this public synthetic pack.\n",
        )
        for entry in files:
            raw = inside(root, entry["path"]).read_bytes()
            require(
                hashlib.sha256(raw).hexdigest() == entry["sha256"], "Source changed during export"
            )
            write_entry(archive, entry["path"], raw)
        write_entry(
            archive,
            "review-package-manifest.json",
            json.dumps(
                {
                    "schema_version": 1,
                    "review_status": "pending_independent_review",
                    "files": files,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )
    return target


if __name__ == "__main__":
    print(package())
