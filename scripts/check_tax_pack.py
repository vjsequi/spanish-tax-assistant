"""Verify retained references, specification links and unlabelled synthetic-source isolation."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from PIL import Image
from pypdf import PdfReader

from scripts.check_repository import ROOT, inside, read_object, require, verify_manifest
from scripts.pin_official_sources import verify as verify_sources

RULES = "data/rules/2025/"
CASE_KEYS = {
    "schema_version",
    "case_id",
    "classification",
    "tax_year",
    "jurisdiction",
    "review_status",
    "fact_confirmation",
    "documents",
}
DOCUMENT_KEYS = {"id", "file", "media_type", "sha256", "pages", "declared_source_type"}


def hashed(root: Path, relative: str, expected: str) -> Path:
    path = inside(root, relative)
    require(path.stat().st_size <= 32 * 1024 * 1024, "Pack artifact exceeds verifier size limit")
    require(hashlib.sha256(path.read_bytes()).hexdigest() == expected, "Pack artifact hash drift")
    return path


def input_document(root: Path, case_id: str, document: dict[str, Any]) -> Path:
    require(set(document) == DOCUMENT_KEYS, "Unexpected document metadata/answer fields")
    relative = document["file"]
    require(
        isinstance(relative, str)
        and re.fullmatch(r"documents/D[0-9]{3}\.(pdf|png|jpg)", relative) is not None,
        "Case document path must stay in its own document directory",
    )
    require(re.fullmatch(r"C[0-9]{3}", case_id) is not None, "Unsafe case identifier")
    require(document["id"] == Path(relative).stem, "Document identity/path drift")
    return hashed(root, f"evals/inputs/{case_id}/{relative}", document["sha256"])


def input_payload(payload: dict[str, Any]) -> None:
    require(set(payload) == CASE_KEYS, "Case input contains unexpected or answer/authoring fields")
    require(payload["classification"] == "synthetic_development_input", "Not a synthetic input")
    require(
        payload["tax_year"] == 2025 and payload["jurisdiction"] == "ES-IB", "Case context drift"
    )
    require(payload["fact_confirmation"] == "pending", "Source facts cannot self-confirm")
    require(payload["review_status"] == "not_independently_reviewed", "No independent labels exist")


def no_float(value: Any) -> None:
    require(not isinstance(value, float), "Tax parameters must not contain binary floating point")
    if isinstance(value, dict):
        for child in value.values():
            no_float(child)
    elif isinstance(value, list):
        for child in value:
            no_float(child)


def specification(root: Path) -> dict[str, int]:
    manifest = read_object(inside(root, RULES + "manifest.json"))
    source_hash = hashlib.sha256(inside(root, RULES + "manifest.json").read_bytes()).hexdigest()
    sources = {entry["id"]: entry for entry in manifest["entries"]}
    readers: dict[str, PdfReader] = {}

    def reader(source_id: str) -> PdfReader:
        if source_id not in readers:
            readers[source_id] = PdfReader(inside(root, sources[source_id]["destination"]))
        return readers[source_id]

    requirements = {
        item["id"]
        for item in read_object(inside(root, "docs/requirements/requirements.json"))["requirements"]
    }
    stage_data = read_object(inside(root, RULES + "calculation-stages.json"))
    field_data = read_object(inside(root, RULES + "aeat-fields.json"))
    rule_data = read_object(inside(root, RULES + "rule-register.json"))
    for data in (stage_data, field_data, rule_data):
        require(data["source_manifest_sha256"] == source_hash, "Specification/source version drift")
        require(data["tax_year"] == 2025, "Specification tax year drift")
    stages = {item["id"]: item for item in stage_data["stages"]}
    require(len(stages) == len(stage_data["stages"]), "Repeated calculation stage")
    visited: set[str] = set()
    for stage in stage_data["stages"]:
        require(set(stage["depends_on"]) <= visited, "Cyclic, missing or out-of-order dependency")
        require(set(stage["requirement_ids"]) <= requirements, "Unknown stage requirement")
        visited.add(stage["id"])
    require(field_data["form_publication_year"] == 2026, "Wrong annual form publication")
    seen: set[str] = set()
    text_cache: dict[int, str] = {}
    layout_cache: dict[int, str] = {}
    for field in field_data["fields"]:
        ident = field["id"]
        require(
            isinstance(ident, str) and re.fullmatch(r"[0-9]{4}", ident) is not None,
            "Field IDs preserve four digits",
        )
        require(ident not in seen, "Repeated contextual field mapping")
        seen.add(ident)
        require(field["stage_id"] in stages, "Unknown field stage")
        require(ident in stages[field["stage_id"]]["aeat_outputs"], "Field/stage output drift")
        require(field["source_id"] == "BOE-MODELO-100", "Field source is not the selected form")
        page = field["physical_page"]
        require(
            type(page) is int and 1 <= page <= len(reader(field["source_id"]).pages),
            "Invalid form physical page",
        )
        if page not in text_cache:
            text_cache[page] = reader(field["source_id"]).pages[page - 1].extract_text() or ""
        pattern = rf"(?<![0-9]){ident}(?![0-9])"
        if re.search(pattern, text_cache[page]) is None and page not in layout_cache:
            # Adjacent form labels can merge (e.g. 1123 + 1122 -> 11231122) in plain extraction.
            # Layout extraction must still contain a separate field token; never use substring
            # matching as proof of field membership. Neither mode verifies the semantic mapping.
            layout_cache[page] = (
                reader(field["source_id"]).pages[page - 1].extract_text(extraction_mode="layout")
                or ""
            )
        require(
            re.search(pattern, text_cache[page]) is not None
            or re.search(pattern, layout_cache.get(page, "")) is not None,
            "Mapped field is absent from the declared source page",
        )
    questions = read_object(inside(root, RULES + "review-questions.json"))["questions"]
    question_ids = {item["id"] for item in questions}
    rule_ids = {item["id"] for item in rule_data["rules"]}
    require(len(rule_ids) == len(rule_data["rules"]), "Repeated rule ID")
    require(rule_data["approved_for_application"] is False, "Tax rules remain unreviewed")
    for rule in rule_data["rules"]:
        require(rule["approved_for_application"] is False, "Unreviewed rule approved")
        require(rule["review_status"] == "pending_independent_tax_review", "No tax sign-off exists")
        require(rule["stage_id"] in stages, "Unknown rule stage")
        require(set(rule["requirement_ids"]) <= requirements, "Unknown rule requirement")
        require(set(rule["review_questions"]) <= question_ids, "Unknown rule review question")
        require(bool(rule["source_refs"]), "A tax rule needs retained source references")
        no_float(rule["parameters"])
        for ref in rule["source_refs"]:
            require(ref["source_id"] in sources, "Unknown retained rule reference")
            for page in ref.get("physical_pages", []):
                require(
                    type(page) is int and 1 <= page <= len(reader(ref["source_id"]).pages),
                    "Rule citation page outside source",
                )
    for question in questions:
        require(set(question["rule_ids"]) <= rule_ids, "Review question references unknown rule")
        require(set(question["source_ids"]) <= sources.keys(), "Unknown review source")
        require(
            question["resolution"] is None and question["reviewer"] is None,
            "Unobtained tax review must stay pending",
        )
    return {
        "stages": len(stages),
        "fields": len(seen),
        "rules": len(rule_ids),
        "open_tax_questions": len(questions),
    }


def cases(root: Path) -> dict[str, int]:
    manifest_path = inside(root, "evals/inputs/manifest.json")
    manifest = read_object(manifest_path)
    hashed(root, "evals/authoring/cases.json", manifest["authoring_sha256"])
    hashed(root, "data/rules/2025/manifest.json", manifest["source_manifest_sha256"])
    require(manifest["generator"] == "scripts/build_review_cases.py", "Unknown fixture generator")
    hashed(root, manifest["generator"], manifest["generator_sha256"])
    require(manifest["review_status"] == "not_independently_reviewed", "No synthetic review exists")
    case_ids: set[str] = set()
    source_files = total_pages = 0
    for entry in manifest["cases"]:
        case_id = entry["case_id"]
        require(
            isinstance(case_id, str) and re.fullmatch(r"C[0-9]{3}", case_id) is not None,
            "Unsafe case identifier",
        )
        require(case_id not in case_ids, "Repeated synthetic case")
        case_ids.add(case_id)
        require(
            entry["case_file"] == f"evals/inputs/{case_id}/case.json", "Case manifest path drift"
        )
        payload = read_object(hashed(root, entry["case_file"], entry["sha256"]))
        input_payload(payload)
        require(payload["case_id"] == case_id, "Case identity drift")
        pages = 0
        allowed = {"case.json"}
        for document in payload["documents"]:
            path = input_document(root, case_id, document)
            allowed.add(document["file"])
            if document["media_type"] == "application/pdf":
                require(path.suffix == ".pdf", "Media/extension mismatch")
                pdf = PdfReader(path)
                page_count = len(pdf.pages)
                if case_id == "C016":
                    require(
                        all(not page.extract_text() for page in pdf.pages),
                        "Scan fixture unexpectedly contains an embedded text layer",
                    )
            else:
                require(
                    document["media_type"] in {"image/png", "image/jpeg"},
                    "Unexpected fixture media",
                )
                with Image.open(path) as image:
                    require(image.width * image.height <= 20_000_000, "Fixture image is too large")
                    image.verify()
                page_count = 1
            require(
                type(document["pages"]) is int and document["pages"] == page_count,
                "Source page count drift",
            )
            pages += page_count
        folder = root / "evals/inputs" / case_id
        actual = {
            path.relative_to(folder).as_posix() for path in folder.rglob("*") if path.is_file()
        }
        require(actual == allowed, "Unexpected source/answer/authoring artifact in case inputs")
        require(
            entry["source_files"] == len(payload["documents"]) and entry["pages"] == pages,
            "Case counts disagree with retained files",
        )
        if case_id == "C018":
            require(entry["source_files"] == 30 and pages == 100, "Benchmark workload drift")
        source_files += entry["source_files"]
        total_pages += pages
    for requirement in read_object(inside(root, "docs/requirements/requirements.json"))[
        "requirements"
    ]:
        require(
            set(requirement["review_case_ids"]) <= case_ids,
            "Requirement references an unknown review case",
        )
        require(
            requirement["trace_status"] == "draft_design_and_unreviewed_inputs_only",
            "No requirement behaviour or tax-validation evidence exists yet",
        )
        for reference in requirement["detail_refs"]:
            inside(root, reference)
    request = read_object(inside(root, "evals/review/review-request.json"))
    require(
        request["input_manifest_sha256"] == hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "Review request/input version drift",
    )
    require(
        request["source_manifest_sha256"] == manifest["source_manifest_sha256"],
        "Review request/source version drift",
    )
    require(
        {item["case_id"] for item in request["case_requests"]} == case_ids,
        "Incomplete review denominator",
    )
    require(
        all(
            item["reviewer"] is None and item["review_status"] == "pending"
            for item in request["case_requests"]
        ),
        "No completed review may be invented",
    )
    template = read_object(inside(root, "evals/review/answer-template.json"))
    require(
        all(
            value is None or value == [] or key == "schema_version"
            for key, value in template.items()
        ),
        "Blank review template contains answers",
    )
    guide = PdfReader(inside(root, "output/pdf/tax-2025-review-guide.pdf"))
    require(len(guide.pages) > 1, "Missing multi-page review guide")
    return {
        "synthetic_cases": len(case_ids),
        "source_files": source_files,
        "source_pages": total_pages,
        "guide_pages": len(guide.pages),
    }


def check(root: Path = ROOT) -> dict[str, int]:
    licences = verify_manifest(root, "third_party/development-licences.json")
    return {
        "development_licence_files": licences,
        "pinned_sources": verify_sources(root),
        **specification(root),
        **cases(root),
    }


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True))
    print("Reference/specification/fixture integrity only; no independent tax or model result.")
