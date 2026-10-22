"""Spanish development packet; numbers remain provisional pending professional QA."""

from __future__ import annotations

from html import escape
from io import BytesIO
from typing import Any

from reportlab.lib import colors  # type: ignore[import-untyped]
from reportlab.lib.pagesizes import A4  # type: ignore[import-untyped]
from reportlab.lib.styles import getSampleStyleSheet  # type: ignore[import-untyped]
from reportlab.platypus import (  # type: ignore[import-untyped]
    KeepTogether,
    LongTable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    TableStyle,
)

from renta_assistant.domain.calculation import FACT_LABELS


def pdf_packet(packet: dict[str, Any]) -> bytes:
    output = BytesIO()
    styles = getSampleStyleSheet()
    normal = styles["BodyText"]
    normal.fontSize = 9
    normal.leading = 12
    styles["Heading2"].keepWithNext = True
    story: list[Any] = []

    def paragraph(text: str, style: str = "BodyText") -> None:
        story.append(Paragraph(escape(text), styles[style]))
        spacer = Spacer(1, 7)
        spacer.keepWithNext = style in {"Title", "Heading2"}
        story.append(spacer)

    def table(rows: list[list[str]]) -> None:
        content = [[Paragraph(escape(cell), normal) for cell in row] for row in rows]
        result = LongTable(content, colWidths=[235, 265], repeatRows=1)
        result.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e5eef1")),
                    ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#ccd6dd")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]
            )
        )
        story.extend([result, Spacer(1, 12)])

    paragraph("Revisión IRPF 2025 - C001", "Title")
    paragraph("DATOS SINTÉTICOS. DESARROLLO PROVISIONAL. QA FISCAL PROFESIONAL PENDIENTE.")
    paragraph(
        "Primera rama: adulto menor de 65 años, un pagador ordinario, intereses bancarios "
        "y vivienda habitual en propiedad. El resto de tratamientos "
        "sigue pendiente de implementación."
    )
    paragraph(f"Versión del expediente: {packet['version']}; fuentes: {packet['source_digest']}")
    table(
        [["Hecho / evidencia", "Valor y confirmación"]]
        + [
            [
                f"{FACT_LABELS[key]} - {fact['document_id']}, página {fact['page']}",
                f"{fact['value']} - {'confirmado' if fact['confirmed'] else 'pendiente'}",
            ]
            for key, fact in packet["facts"].items()
        ]
    )
    result = packet["result"]
    if result["status"] == "blocked_partial_review":
        paragraph("Revisión parcial: cálculo bloqueado", "Heading2")
        for question in result["questions"]:
            paragraph(question)
    else:
        paragraph(
            f"Resultado provisional, casilla 0670: {result['fields']['0670']} EUR", "Heading2"
        )
        paragraph(
            "Positivo: a ingresar. Negativo: a devolver. No implica una "
            "declaración validada o presentada."
        )
        paragraph(result["rounding_assumption"])
        for stage in result["stages"]:
            paragraph(f"{stage['id']} - {stage['label']}", "Heading2")
            paragraph(stage["formula"])
            paragraph("Reglas: " + ", ".join(stage["rule_ids"]))
            table(
                [["Casilla", "Importe / porcentaje"]] + [[k, v] for k, v in stage["fields"].items()]
            )
    paragraph("Comparación del extracto aportado", "Heading2")
    if not result["comparisons"]:
        paragraph("Sin propuestas de cambio: extracto no confirmado o cálculo bloqueado.")
    else:
        table(
            [["Casilla / valor aportado", "Valor calculado provisional"]]
            + [
                [f"{row['field']} - {row['supplied']}", str(row["calculated"])]
                for row in result["comparisons"]
            ]
        )
    paragraph("Trazabilidad y revisión pendiente", "Heading2")
    paragraph(
        "Las reglas candidatas y sus referencias AEAT/BOE se conservan en "
        "data/rules/2025 y data/development/2025/c001. No se consultan respuestas esperadas ni "
        "se realizan llamadas a modelos. El cálculo es determinista y provisional."
    )
    paragraph("Reglas/fuentes: " + result["policy_digest"])
    for reference in packet.get("references", []):
        start = len(story)
        paragraph(reference["id"] + " - " + reference["title"])
        paragraph(reference["url"])
        paragraph("SHA-256: " + reference["sha256"])
        block = story[start:]
        del story[start:]
        story.append(KeepTogether(block))
    paragraph(
        "Historial: " + str(len(packet["events"])) + " eventos locales. "
        "La revisión profesional se realizará como QA al final del desarrollo."
    )

    def footer(canvas: Any, document: Any) -> None:
        canvas.setFont("Helvetica", 8)
        canvas.drawString(47, 25, "SINTÉTICO - PROVISIONAL - PENDIENTE DE QA FISCAL")
        canvas.drawRightString(548, 25, str(document.page))

    SimpleDocTemplate(
        output,
        pagesize=A4,
        rightMargin=47,
        leftMargin=47,
        topMargin=45,
        bottomMargin=43,
        title="Revisión provisional C001",
    ).build(story, onFirstPage=footer, onLaterPages=footer)
    return output.getvalue()
