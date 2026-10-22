"""Manifest-constrained synthetic sources and additive, source-bound development policy."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
import threading
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from PIL import Image
from pypdf import PdfReader

from renta_assistant.domain.calculation import Band, Fact, InputError, Policy, money

ROOT = Path(__file__).resolve().parents[3]


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def admitted(root: Path, relative: str) -> Path:
    parts = Path(relative).parts
    if (
        Path(relative).is_absolute()
        or ".." in parts
        or {"expected", ".private"}.intersection(parts)
    ):
        raise InputError("Ruta fuera del inventario público permitido.")
    current = root
    for part in parts:
        current /= part
        if current.is_symlink():
            raise InputError("No se admiten enlaces simbólicos.")
    if not current.resolve().is_relative_to(root.resolve()) or not current.is_file():
        raise InputError("Fuente no disponible en el inventario.")
    if current.stat().st_size > 32 * 1024 * 1024:
        raise InputError("La fuente supera el límite local.")
    return current


def obj(path: Path) -> dict[str, Any]:
    result: Any = json.loads(path.read_bytes())
    if not isinstance(result, dict):
        raise InputError("Registro no válido.")
    return result


class Sources:
    def __init__(self, root: Path = ROOT) -> None:
        self.root = root
        self._images: dict[str, bytes] = {}
        self._render_lock = threading.Lock()

    def case(self, case_id: str) -> dict[str, Any]:
        if case_id != "C001":
            raise InputError(
                "La primera demostración ejecutable está limitada al caso sintético C001."
            )
        path = admitted(self.root, f"evals/inputs/{case_id}/case.json")
        data = obj(path)
        if data.get("classification") != "synthetic_development_input":
            raise InputError("Solo se admiten las fuentes sintéticas de desarrollo.")
        hashes = [digest(path.read_bytes())]
        for document in data["documents"]:
            raw = self.document(case_id, document["id"]).read_bytes()
            if digest(raw) != document["sha256"]:
                raise InputError("La fuente ha cambiado; revise sus versiones.")
            hashes.append(digest(raw))
        return {**data, "source_digest": digest("|".join(hashes).encode())}

    def document(self, case_id: str, document_id: str) -> Path:
        if case_id != "C001" or re.fullmatch(r"D[0-9]{3}", document_id) is None:
            raise InputError("Documento fuera del expediente autorizado.")
        data = obj(admitted(self.root, f"evals/inputs/{case_id}/case.json"))
        matches = [item for item in data["documents"] if item["id"] == document_id]
        if len(matches) != 1:
            raise InputError("Documento no encontrado.")
        item = matches[0]
        if re.fullmatch(r"documents/D[0-9]{3}\.(pdf|png|jpg)", item["file"]) is None:
            raise InputError("Ruta de documento no válida.")
        path = admitted(self.root, f"evals/inputs/{case_id}/{item['file']}")
        if digest(path.read_bytes()) != item["sha256"]:
            raise InputError("Hash de fuente incorrecto.")
        return path

    def candidates(self) -> dict[str, Fact]:
        # A deliberately narrow digital-template baseline, never described as AI/vision extraction.
        patterns = {
            "birth_date": ("D001", r"Nacimiento: ([0-9]{4}-[0-9]{2}-[0-9]{2})"),
            "salary": ("D002", r"Retribuciones dinerarias brutas: ([0-9.,]+) EUR"),
            "social_security": (
                "D002",
                r"Cotizaciones a la Seguridad Social del trabajador: ([0-9.,]+) EUR",
            ),
            "salary_withholding": (
                "D002",
                r"Retenciones sobre retribuciones dinerarias: ([0-9.,]+) EUR",
            ),
            "interest": ("D003", r"Intereses brutos: ([0-9.,]+) EUR"),
            "bank_withholding": ("D003", r"Retenciones: ([0-9.,]+) EUR"),
            "bank_fees": ("D003", r"Comisiones ordinarias de cuenta: ([0-9.,]+) EUR"),
            "in_kind": ("D002", r"Valoración fiscal de retribución en especie: ([0-9.,]+) EUR"),
            "employer_pension": (
                "D002",
                r"Contribución empresarial a plan de empleo imputada: ([0-9.,]+) EUR",
            ),
            "worker_elected_pension": (
                "D002",
                r"Aportación empresarial por decisión del trabajador: ([0-9.,]+) EUR",
            ),
        }
        texts = {
            d: PdfReader(self.document("C001", d)).pages[0].extract_text() or ""
            for d in ("D001", "D002", "D003")
        }
        result = {}
        for key, (document_id, pattern) in patterns.items():
            matches = re.findall(pattern, texts[document_id])
            value = matches[0] if len(matches) == 1 else ""
            result[key] = Fact(value, document_id, False, method="digital_template_v1")
        return result

    def draft(self) -> dict[str, str]:
        text = PdfReader(self.document("C001", "D004")).pages[0].extract_text() or ""
        matches = re.findall(r"Casilla ([0-9]{4}): ([0-9.,]+) EUR", text)
        if len({key for key, _ in matches}) != len(matches):
            raise InputError("Casillas duplicadas o conflictivas en el extracto.")
        return {key: format(money(value), ".2f") for key, value in matches}

    def image(self, document_id: str, page: int = 1) -> bytes:
        source = self.document("C001", document_id)
        if type(page) is not int or page != 1:
            raise InputError("Página fuera del inventario de C001.")
        key = digest(source.read_bytes()) + ":page1:100dpi:png:v1"
        with self._render_lock:
            if key not in self._images:
                self._images[key] = self._render(source)
            return self._images[key]

    def _render(self, source: Path) -> bytes:
        with tempfile.TemporaryDirectory(prefix="tax-synthetic-render-") as temporary:
            target = Path(temporary) / "page"
            subprocess.run(
                [
                    "pdftoppm",
                    "-f",
                    "1",
                    "-l",
                    "1",
                    "-r",
                    "100",
                    "-singlefile",
                    "-png",
                    str(source),
                    str(target),
                ],
                check=True,
                timeout=15,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )
            path = target.with_suffix(".png")
            if path.stat().st_size > 8 * 1024 * 1024:
                raise InputError("La imagen renderizada supera el límite.")
            with Image.open(path) as image:
                if image.width * image.height > 2_000_000:
                    raise InputError("Demasiados píxeles en la imagen.")
                image.verify()
            return path.read_bytes()

    def policy(self) -> Policy:
        path = admitted(self.root, "data/rules/2025/rule-register.json")
        register = obj(path)
        manifest = admitted(self.root, "data/rules/2025/manifest.json")
        if register["source_manifest_sha256"] != digest(manifest.read_bytes()):
            raise InputError("La versión de reglas no coincide con sus fuentes.")
        for receipt in obj(manifest)["entries"]:
            if (
                digest(admitted(self.root, receipt["destination"]).read_bytes())
                != receipt["sha256"]
            ):
                raise InputError("Una referencia oficial ha cambiado.")
        supplement = admitted(self.root, "data/development/2025/c001/manifest.json")
        for receipt in obj(supplement)["entries"]:
            if (
                digest(admitted(self.root, receipt["destination"]).read_bytes())
                != receipt["sha256"]
            ):
                raise InputError("La guía oficial complementaria ha cambiado.")
        rules = {r["id"]: r["parameters"] for r in register["rules"]}

        def bands(values: list[dict[str, str]]) -> tuple[Band, ...]:
            from decimal import Decimal

            result = tuple(
                Band(
                    money(v["lower_eur"]), money(v["base_quota_eur"]), money(v["marginal_percent"])
                )
                for v in values
            )
            if any(b.rate < Decimal("0") or b.rate > Decimal("100") for b in result):
                raise InputError("Tipo de gravamen fuera del intervalo válido.")
            if any(result[i].lower <= result[i - 1].lower for i in range(1, len(result))):
                raise InputError("Escala desordenada.")
            return result

        return Policy(
            bands(rules["SCALE-ES-G"]["bands"]),
            bands(rules["IB-SCALE-G"]["bands"]),
            bands(rules["SCALE-SAVINGS"]["each_component_bands"]),
            money(rules["EMP-02"]["other_expenses_eur"]),
            money(rules["MIN-ES-01"]["taxpayer_base_eur"]),
            money(rules["MIN-IB-01"]["unchanged_under_65_taxpayer_base_eur"]),
            money(rules["EMP-03"]["rnt_bands_eur"][-1]),
            money(rules["EMP-CREDIT-2025"]["gross_threshold_eur"]),
            digest(
                path.read_bytes()
                + supplement.read_bytes()
                + admitted(self.root, "data/rules/2025/aeat-fields.json").read_bytes()
                + (Path(__file__).parent.parent / "domain/calculation.py").read_bytes()
            ),
        )

    def references(self) -> list[dict[str, str]]:
        references = []
        for name in ("data/rules/2025/manifest.json", "data/development/2025/c001/manifest.json"):
            for entry in obj(admitted(self.root, name))["entries"]:
                parsed = urlsplit(entry["url"])
                if parsed.scheme != "https" or parsed.hostname not in {
                    "sede.agenciatributaria.gob.es",
                    "www.boe.es",
                }:
                    raise InputError("Referencia fuera de los editores oficiales permitidos.")
                if entry["id"] in {
                    "AEAT-MANUAL-1",
                    "BOE-LIRPF",
                    "BOE-BALEAR",
                    "BOE-MODELO-100",
                } or entry["id"].startswith("DEV-"):
                    references.append({key: entry[key] for key in ("id", "title", "url", "sha256")})
        return references
