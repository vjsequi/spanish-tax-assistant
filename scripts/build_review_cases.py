"""Build wholly synthetic development documents and an unlabelled independent-review pack."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import shutil
import subprocess
from html import escape
from pathlib import Path
from typing import Any

from PIL import Image, ImageFilter
from pypdf import PdfReader
from reportlab.lib import colors  # type: ignore[import-untyped]
from reportlab.lib.pagesizes import A4  # type: ignore[import-untyped]
from reportlab.lib.styles import ParagraphStyle  # type: ignore[import-untyped]
from reportlab.lib.utils import ImageReader  # type: ignore[import-untyped]
from reportlab.pdfgen.canvas import Canvas  # type: ignore[import-untyped]
from reportlab.platypus import Paragraph, Table, TableStyle  # type: ignore[import-untyped]

from scripts.check_repository import ROOT, inside, read_object, require

AUTHORING = "evals/authoring/cases.json"
INPUTS = "evals/inputs"
GUIDE = "output/pdf/tax-2025-review-guide.pdf"
WIDTH, HEIGHT = A4
INK = colors.HexColor("#17304c")
BLUE = colors.HexColor("#eaf1f7")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def paragraph(value: str, *, bold: bool = False, small: bool = False) -> Any:
    style = ParagraphStyle(
        "document",
        fontName="Helvetica-Bold" if bold else "Helvetica",
        fontSize=8 if small else 9,
        leading=10 if small else 12,
        textColor=INK,
    )
    return Paragraph(escape(value).replace("\n", "<br/>"), style)


def draw_document(path: Path, case_id: str, doc_id: str, pages: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    canvas = Canvas(str(path), pagesize=A4, pageCompression=1, invariant=1)
    canvas.setTitle(f"Datos sintéticos 2025 - {case_id} - {doc_id}")
    canvas.setAuthor("Spanish Tax Assistant - synthetic fixture generator")
    for index, page in enumerate(pages, 1):
        canvas.setFillColor(INK)
        canvas.rect(0, HEIGHT - 34, WIDTH, 34, fill=1, stroke=0)
        canvas.setFillColor(colors.white)
        canvas.setFont("Helvetica-Bold", 9)
        canvas.drawString(40, HEIGHT - 22, "DATOS SINTETICOS - SIN VALIDEZ FISCAL")
        title = paragraph(page["title"], bold=True)
        _, title_height = title.wrap(WIDTH - 80, 50)
        title.drawOn(canvas, 40, HEIGHT - 57 - title_height)
        canvas.setFillColor(INK)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(
            40, HEIGHT - 99, f"{case_id} | {doc_id} | Fuente ficticia | Ejercicio 2025"
        )
        canvas.setStrokeColor(colors.HexColor("#cedae5"))
        canvas.line(40, HEIGHT - 109, WIDTH - 40, HEIGHT - 109)
        y = HEIGHT - 127
        for label, value in page.get("rows", []):
            body = paragraph(f"{label}: {value}")
            _, height = body.wrap(WIDTH - 80, 700)
            require(y - height > 50, f"Document rows overflow: {case_id}/{doc_id}")
            body.drawOn(canvas, 40, y - height)
            y -= height + 5
        if page.get("table"):
            cells = [[paragraph(str(cell), small=True) for cell in row] for row in page["table"]]
            columns = len(cells[0])
            table = Table(cells, colWidths=[(WIDTH - 80) / columns] * columns)
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#d6dfe8")),
                        ("LEFTPADDING", (0, 0), (-1, -1), 5),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                        ("TOPPADDING", (0, 0), (-1, -1), 4),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ]
                )
            )
            _, height = table.wrap(WIDTH - 80, 700)
            require(y - height > 50, f"Document table overflow: {case_id}/{doc_id}")
            table.drawOn(canvas, 40, y - height)
            y -= height + 12
        for note in page.get("notes", []):
            body = paragraph(note, small=True)
            _, height = body.wrap(WIDTH - 80, 700)
            require(y - height > 50, f"Document notes overflow: {case_id}/{doc_id}")
            body.drawOn(canvas, 40, y - height)
            y -= height + 5
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(INK)
        canvas.drawString(40, 28, "SINTETICO - No es documento AEAT ni acredita una operación real")
        canvas.drawRightString(WIDTH - 40, 28, f"{index}/{len(pages)}")
        canvas.showPage()
    canvas.save()


def derivative(source: Path, target: Path, scratch: Path, *, scan: bool, unreadable: bool) -> None:
    prefix = scratch / target.stem
    subprocess.run(
        [
            "pdftoppm",
            "-r",
            "48" if unreadable else "110",
            "-f",
            "1",
            "-singlefile",
            "-png",
            str(source),
            str(prefix),
        ],
        check=True,
        capture_output=True,
        timeout=30,
    )
    with Image.open(prefix.with_suffix(".png")) as raw:
        image = raw.convert("RGB")
        if unreadable:
            image = image.filter(ImageFilter.GaussianBlur(radius=4)).resize((910, 1288))
        if not scan:
            if target.suffix == ".jpg":
                image.save(target, format="JPEG", quality=90, optimize=False)
            else:
                image.save(target, format="PNG")
        else:
            canvas = Canvas(str(target), pagesize=A4, pageCompression=1, invariant=1)
            canvas.setTitle("Synthetic image-only PDF; no embedded text")
            canvas.drawImage(ImageReader(image), 0, 0, width=WIDTH, height=HEIGHT)
            canvas.showPage()
            canvas.save()


def guide_pages(
    cases: list[dict[str, Any]], receipts: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = [
        {
            "title": "Revisión independiente - IRPF 2025 Illes Balears",
            "rows": [
                ["Contenido", "20 expedientes ficticios; primera ronda de revisión: 8 expedientes"],
                [
                    "Estado",
                    "Fuentes de desarrollo redactadas por software; sin respuestas fiscales "
                    "validadas",
                ],
                [
                    "Alcance",
                    "Declaración individual ordinaria; trabajo, intereses, familia y "
                    "beneficios seleccionados",
                ],
                [
                    "Entregable solicitado",
                    "Transcripción comprobada, cálculo por fases/casillas, cuestiones y límites",
                ],
                [
                    "Separación",
                    "Los resultados del revisor no son entrada para la aplicación ni para el"
                    " modelo",
                ],
                [
                    "Privacidad",
                    "Paquete totalmente sintético; no añadir expedientes ni datos fiscales reales",
                ],
                [
                    "Fuentes",
                    "Originales AEAT/BOE retenidos con hash; no implica revisión de aplicabilidad",
                ],
                ["Primera ronda", "C001, C002, C003, C004, C008, C010, C011, C012"],
                [
                    "Resto",
                    "Segunda ronda y pruebas visuales/de seguridad; C018 es carga de 30 "
                    "archivos/100 páginas",
                ],
            ],
            "notes": [
                "Revise las condiciones legales y las preguntas abiertas antes de certificar"
                " un resultado. "
                "No trate una declaración ficticia o un certificado generado como una prueba"
                " de autenticidad real.",
                "No hay aplicación ni cálculo fiscal implementados; este paquete prepara su "
                "validación.",
            ],
        },
        {
            "title": "Procedimiento y referencias para la revisión",
            "rows": [
                [
                    "1. Fuentes",
                    "Comprobar vigencia, edición, territorio y las preguntas RQ-01 a RQ-09",
                ],
                [
                    "2. Hechos",
                    "Transcribir importes/fechas y enlazar documento, página física y región"
                    " cuando sea posible",
                ],
                [
                    "3. Cobertura",
                    "Identificar datos faltantes, contradicciones y tratamientos no cubiertos",
                ],
                [
                    "4. Cálculo",
                    "Derivar bases, mínimos, cuotas, deducciones y retenciones de forma "
                    "independiente",
                ],
                [
                    "5. Casillas",
                    "Validar valores intermedios, contexto de pagador/persona y resultado; "
                    "no solo el total",
                ],
                [
                    "6. Cuestiones",
                    "Registrar preguntas útiles, alternativas válidas e incertidumbres sin "
                    "inventar ceros",
                ],
                [
                    "7. Firma",
                    "Identidad/competencia del revisor, fecha, fuentes y hashes revisados; "
                    "nunca autoaprobar",
                ],
                [
                    "Resultado",
                    "0670: resultado ordinario; 0700: documento de ingreso/devolución; 0595:"
                    " antes de pagos",
                ],
                ["Modelo oficial", "BOE-MODELO-100: páginas físicas 24-25, 39-46, 53, 62 y 73"],
                ["Manuales", "AEAT parte 1: actualización impresa 20-05-2026; parte 2: 30-09-2026"],
            ],
            "notes": [
                "Use evals/review/answer-template.json como plantilla en un espacio de "
                "revisión separado. "
                "Las respuestas independientes aprobadas se guardan en evals/expected "
                "únicamente para el "
                "revisor/evaluador; nunca se cargan como contexto de la aplicación/modelo.",
                "Los materiales oficiales se reutilizan con atribución y sus condiciones "
                "originales. "
                "AEAT y BOE no participan ni patrocinan este proyecto.",
            ],
        },
    ]
    by_case = {item["case_id"]: item for item in receipts}
    for case in cases:
        receipt = by_case[case["id"]]
        rows = [
            ["Expediente", case["id"]],
            ["Ronda propuesta", str(case["review_wave"])],
            ["Archivos/páginas", f"{receipt['source_files']} archivos; {receipt['pages']} páginas"],
            ["Estado de revisión", "Pendiente; no contiene una solución fiscal calculada"],
            ["Entrada", f"evals/inputs/{case['id']}/case.json"],
        ]
        for number, document in enumerate(case["documents"], 1):
            rows.append([f"D{number:03d}", document["title"]])
        for start in range(0, len(rows), 23):
            pages.append(
                {
                    "title": f"Expediente {case['id']} - inventario de fuentes",
                    "rows": rows[start : start + 23],
                    "notes": [
                        "Para cada hallazgo indique soporte y versión. Deje explícitos los "
                        "datos ilegibles o "
                        "las condiciones pendientes. El inventario no contiene la respuesta "
                        "esperada.",
                    ],
                }
            )
    return pages


def build(root: Path = ROOT) -> dict[str, int]:
    authoring = read_object(inside(root, AUTHORING))
    require(authoring["no_private_reference_used"] is True, "Only authored synthetic data allowed")
    require(authoring["review_status"] == "not_reviewed", "Do not regenerate reviewed inputs")
    prior_manifest = root / INPUTS / "manifest.json"
    if prior_manifest.exists():
        require(
            read_object(prior_manifest)["review_status"] == "not_independently_reviewed",
            "Reviewed source packs need a new version and output location",
        )
    require(
        shutil.which("pdftoppm") is not None, "Poppler pdftoppm is required for visual variants"
    )
    poppler = subprocess.run(
        ["pdftoppm", "-v"], capture_output=True, text=True, timeout=5, check=True
    )
    poppler_version = (poppler.stderr or poppler.stdout).splitlines()[0]
    cases = authoring["cases"]
    source_manifest_hash = digest(inside(root, "data/rules/2025/manifest.json"))
    receipts: list[dict[str, Any]] = []
    scratch = root / ".runtime" / "fixture-rendering"
    scratch.mkdir(parents=True, exist_ok=True)
    for case in cases:
        case_id = case["id"]
        require(case_id.startswith("C") and case_id[1:].isdigit(), "Unsafe synthetic case ID")
        folder = root / INPUTS / case_id
        folder.mkdir(parents=True, exist_ok=True)
        documents = []
        for number, document in enumerate(case["documents"], 1):
            doc_id = f"D{number:03d}"
            scanned = case["representations"] == "image_and_scan" and number % 2 == 0
            image = case["representations"] == "image_and_scan" and not scanned
            unreadable = case["representations"] == "unreadable_salary" and number == 2
            suffix = ".png" if image or unreadable else ".pdf"
            if image and number == 3:
                suffix = ".jpg"
            target = folder / "documents" / (doc_id + suffix)
            target.parent.mkdir(parents=True, exist_ok=True)
            if image or scanned or unreadable:
                original = scratch / f"{case_id}-{doc_id}.pdf"
                draw_document(original, case_id, doc_id, document["pages"])
                require(len(document["pages"]) == 1, "Visual fixture variants must be one page")
                derivative(original, target, scratch, scan=scanned, unreadable=unreadable)
            else:
                draw_document(target, case_id, doc_id, document["pages"])
            page_count = len(PdfReader(target).pages) if suffix == ".pdf" else 1
            documents.append(
                {
                    "id": doc_id,
                    "file": target.relative_to(folder).as_posix(),
                    "media_type": {
                        ".pdf": "application/pdf",
                        ".png": "image/png",
                        ".jpg": "image/jpeg",
                    }[suffix],
                    "sha256": digest(target),
                    "pages": page_count,
                    "declared_source_type": document["kind"],
                }
            )
        payload = {
            "schema_version": 1,
            "case_id": case_id,
            "classification": "synthetic_development_input",
            "tax_year": 2025,
            "jurisdiction": "ES-IB",
            "review_status": "not_independently_reviewed",
            "fact_confirmation": "pending",
            "documents": documents,
        }
        save_json(folder / "case.json", payload)
        receipts.append(
            {
                "case_id": case_id,
                "case_file": f"{INPUTS}/{case_id}/case.json",
                "sha256": digest(folder / "case.json"),
                "source_files": len(documents),
                "pages": sum(item["pages"] for item in documents),
            }
        )
    manifest = {
        "schema_version": 1,
        "dataset_version": authoring["dataset_version"],
        "classification": "authored_synthetic_development_sources_not_held_out",
        "review_status": "not_independently_reviewed",
        "authoring_sha256": digest(inside(root, AUTHORING)),
        "source_manifest_sha256": source_manifest_hash,
        "generator": "scripts/build_review_cases.py",
        "generator_sha256": digest(inside(root, "scripts/build_review_cases.py")),
        "tool_versions": {
            **{name: importlib.metadata.version(name) for name in ("reportlab", "pypdf", "pillow")},
            "python": platform.python_version(),
            "pdftoppm": poppler_version,
        },
        "cases": receipts,
    }
    save_json(root / INPUTS / "manifest.json", manifest)
    request = {
        "schema_version": 1,
        "dataset_version": authoring["dataset_version"],
        "input_manifest_sha256": digest(root / INPUTS / "manifest.json"),
        "source_manifest_sha256": source_manifest_hash,
        "status": "pending_independent_review",
        "wave_one_case_ids": [case["id"] for case in cases if case["review_wave"] == 1],
        "case_requests": [
            {
                "case_id": case["id"],
                "case_sha256": by_case["sha256"],
                "wave": case["review_wave"],
                "construction_intent": case["construction_intent"],
                "review_status": "pending",
                "reviewer": None,
            }
            for case, by_case in zip(cases, receipts, strict=True)
        ],
    }
    save_json(root / "evals/review/review-request.json", request)
    save_json(
        root / "evals/review/answer-template.json",
        {
            "schema_version": 1,
            "case_id": None,
            "input_manifest_sha256": None,
            "case_sha256": None,
            "source_manifest_sha256": None,
            "reviewer_identity_and_competence": None,
            "reviewed_at": None,
            "scope_judgement": None,
            "fact_judgements": [],
            "field_and_stage_judgements": [],
            "question_and_alternative_outcomes": [],
            "unresolved_rule_questions": [],
            "review_decision": None,
        },
    )
    draw_document(root / GUIDE, "REVISION", "GUIA-2025", guide_pages(cases, receipts))
    return {
        "cases": len(receipts),
        "source_files": sum(item["source_files"] for item in receipts),
        "source_pages": sum(item["pages"] for item in receipts),
        "guide_pages": len(PdfReader(root / GUIDE).pages),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count-pdfs", action="store_true")
    args = parser.parse_args()
    if args.count_pdfs:
        cases = read_object(inside(ROOT, AUTHORING))["cases"]
        count = 1
        for case in cases:
            for number, _ in enumerate(case["documents"], 1):
                if case["representations"] == "image_and_scan":
                    count += number % 2 == 0
                elif case["representations"] == "unreadable_salary" and number == 2:
                    continue
                else:
                    count += 1
        print(count)
    else:
        print(json.dumps(build(), sort_keys=True))


if __name__ == "__main__":
    main()
