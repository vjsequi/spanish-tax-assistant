"""A working synthetic case, with explicit confirmation, persistence and safe publication."""

from __future__ import annotations

import hashlib
import json
import re
import threading
import time
from dataclasses import asdict
from datetime import UTC, datetime
from typing import Any

from renta_assistant.application.ports import CaseSources, StateStore
from renta_assistant.domain.calculation import (
    COVERAGE_LABELS,
    FACT_LABELS,
    Fact,
    InputError,
    calculate,
)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


class Workbench:
    def __init__(
        self, sources: CaseSources, store: StateStore, *, profile: str = "local-synthetic"
    ) -> None:
        if profile != "local-synthetic":
            raise InputError("Este adaptador no admite identidad local en perfiles cloud/privados.")
        self.sources = sources
        self.store = store
        self.lock = threading.RLock()
        self.metrics: dict[str, int | float | str] = {
            "provider_calls": 0,
            "commands_completed": 0,
            "commands_rejected": 0,
            "last_command_ms": 0,
            "profile": profile,
        }

    def state(self) -> dict[str, Any]:
        with self.lock:
            sources = self.sources.case("C001")
            data = self.store.load()
            if data is not None:
                if data["source_digest"] != sources["source_digest"]:
                    raise InputError(
                        "Las fuentes cambiaron; el estado guardado requiere migración explícita."
                    )
                return data
            return {
                "case_id": "C001",
                "version": 0,
                "source_digest": sources["source_digest"],
                "facts": {k: asdict(v) for k, v in self.sources.candidates().items()},
                "coverage": {key: None for key in COVERAGE_LABELS},
                "draft_confirmed": False,
                "result": None,
                "events": [],
                "requests": {},
            }

    def view(self) -> dict[str, Any]:
        data = self.state()
        return {
            **{k: v for k, v in data.items() if k not in {"events", "requests"}},
            "fact_labels": FACT_LABELS,
            "coverage_labels": COVERAGE_LABELS,
            "documents": self.sources.case("C001")["documents"],
            "draft": self.sources.draft(),
            "references": self.sources.references(),
            "result_is_stale": data["result"] is not None
            and data["result"]["policy_digest"] != self.sources.policy().digest,
            "audit_event_count": len(data["events"]),
            "metrics": self.metrics,
            "notice": (
                "Desarrollo sintético · Cálculo provisional · QA fiscal profesional pendiente"
            ),
            "extraction_method": "Plantilla digital determinista + revisión visual/manual; sin IA.",
        }

    def confirm_and_calculate(self, command: dict[str, Any]) -> dict[str, Any]:
        started = time.monotonic()
        try:
            return self._command(command)
        except (InputError, ValueError, TypeError, KeyError) as exc:
            self.metrics["commands_rejected"] = int(self.metrics["commands_rejected"]) + 1
            if isinstance(exc, InputError):
                raise
            raise InputError("Comando incompleto o con tipos no válidos.") from exc
        finally:
            self.metrics["last_command_ms"] = round((time.monotonic() - started) * 1000, 2)

    def _command(self, command: dict[str, Any]) -> dict[str, Any]:
        allowed = {"version", "source_digest", "request_id", "facts", "coverage", "draft_confirmed"}
        if set(command) != allowed:
            raise InputError("Comando fuera del contrato permitido.")
        request_id = command["request_id"]
        if (
            not isinstance(request_id, str)
            or re.fullmatch(r"[a-zA-Z0-9-]{16,64}", request_id) is None
        ):
            raise InputError("Identificador de petición no válido.")
        command_digest = digest(json.dumps(command, sort_keys=True).encode())
        with self.lock:
            data = self.state()
            if request_id in data["requests"]:
                if data["requests"][request_id] != command_digest:
                    raise InputError("La clave idempotente ya se usó con otro contenido.")
                return self.view()
            if type(command["version"]) is not int or command["version"] != data["version"]:
                raise InputError("Versión obsoleta: recargue el expediente antes de confirmar.")
            if command["source_digest"] != data["source_digest"]:
                raise InputError("La versión de las fuentes no coincide.")
            if len(data["events"]) >= 1000:
                raise InputError("Se alcanzó el límite de eventos de esta demostración local.")
            if set(command["facts"]) != set(FACT_LABELS):
                raise InputError("No se admiten datos omitidos o nuevos campos del modelo.")
            facts = {}
            for key, value in command["facts"].items():
                if set(value) != {"value", "document_id", "confirmed"}:
                    raise InputError("Dato sin el contrato de confirmación requerido.")
                if not isinstance(value["value"], str) or len(value["value"]) > 64:
                    raise InputError("Valor del dato no válido.")
                self.sources.document("C001", value["document_id"])
                facts[key] = Fact(
                    value["value"],
                    value["document_id"],
                    value["confirmed"],
                    method="human_confirmation",
                )
            policy = self.sources.policy()
            try:
                result = calculate(facts, command["coverage"], policy)
                record = asdict(result)
            except InputError as blocked:
                record = {
                    "status": "blocked_partial_review",
                    "fields": {},
                    "stages": [],
                    "questions": [str(blocked)],
                    "independently_validated": False,
                    "policy_digest": policy.digest,
                }

            if (
                command["draft_confirmed"] not in (True, False)
                or type(command["draft_confirmed"]) is not bool
            ):
                raise InputError("Confirme el estado del extracto del borrador.")
            comparisons = []
            if command["draft_confirmed"] is True:
                for field, old in self.sources.draft().items():
                    new = record["fields"].get(field)
                    if new is None:
                        continue
                    comparisons.append(
                        {
                            "field": field,
                            "supplied": old,
                            "calculated": new,
                            "status": "equal" if old == new else "provisional_difference",
                            "source": {"document_id": "D004", "page": 1},
                        }
                    )
            record = {
                **record,
                "comparisons": comparisons,
                "draft_status": "confirmed_excerpt"
                if command["draft_confirmed"]
                else "not_confirmed_no_changes_proposed",
            }
            # Recheck immutable evidence after calculation, before publishing a new version.
            if self.sources.case("C001")["source_digest"] != data["source_digest"]:
                raise InputError("Las fuentes cambiaron durante el cálculo.")
            if self.sources.policy().digest != policy.digest:
                raise InputError("Las reglas cambiaron durante el cálculo.")
            data.update(
                version=data["version"] + 1,
                facts={key: asdict(value) for key, value in facts.items()},
                coverage=command["coverage"],
                draft_confirmed=command["draft_confirmed"],
                result=record,
            )
            data["events"].append(
                {
                    "event": "case_saved_with_provisional_or_blocked_calculation",
                    "version": data["version"],
                    "command_digest": command_digest,
                    "at": datetime.now(UTC).isoformat(),
                    "policy_digest": policy.digest,
                }
            )
            data["requests"][request_id] = command_digest
            self.store.save(data)
            self.metrics["commands_completed"] = int(self.metrics["commands_completed"]) + 1
            return self.view()

    def packet(self) -> dict[str, Any]:
        data = self.state()
        if data["result"] is None:
            raise InputError(
                "Confirme los datos y genere el resultado provisional antes de exportar."
            )
        if data["result"]["policy_digest"] != self.sources.policy().digest:
            raise InputError("Resultado obsoleto: las reglas han cambiado; vuelva a calcular.")
        return {
            **{key: value for key, value in data.items() if key != "requests"},
            "references": self.sources.references(),
        }
