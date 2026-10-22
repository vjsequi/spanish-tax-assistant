"""Provisional source-derived engineering regressions, NOT independent tax labels."""

from __future__ import annotations

import copy
import http.client
import json
import shutil
import tempfile
import threading
import unittest
from dataclasses import replace
from decimal import Decimal
from io import BytesIO
from pathlib import Path
from typing import Any, ClassVar

from pypdf import PdfReader

from renta_assistant.application.workbench import Workbench
from renta_assistant.domain.calculation import (
    COVERAGE_LABELS,
    Fact,
    InputError,
    Policy,
    calculate,
    money,
    scale,
)
from renta_assistant.infrastructure.export import pdf_packet
from renta_assistant.infrastructure.repository import ROOT, Sources, admitted
from renta_assistant.infrastructure.state import FileStore
from renta_assistant.infrastructure.web import make_server


class ProvisionalCalculatorTests(unittest.TestCase):
    sources: ClassVar[Sources]
    policy: ClassVar[Policy]
    facts: ClassVar[dict[str, Fact]]
    coverage: ClassVar[dict[str, bool]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.sources = Sources()
        cls.policy = cls.sources.policy()
        cls.facts = {k: replace(v, confirmed=True) for k, v in cls.sources.candidates().items()}
        cls.coverage = dict.fromkeys(COVERAGE_LABELS, True)

    def test_c001_provisional_worksheet_checks_components_and_total(self) -> None:
        result = calculate(self.facts, self.coverage, self.policy)
        # Authored arithmetic: 38,500 − 2,440 − 2,000 = 34,060; state/regional scales,
        # tax on 5,550 minimum, and 240 gross interest; 7,245.60 prepaid.
        # These are software-author expectations awaiting final professional QA.
        expected = {
            "0018": "36060.00",
            "0019": "2000.00",
            "0022": "34060.00",
            "0027": "240.00",
            "0528": "4191.75",
            "0529": "4220.50",
            "0530": "527.25",
            "0531": "499.50",
            "0532": "3664.50",
            "0533": "3721.00",
            "0540": "22.80",
            "0541": "22.80",
            "0595": "7431.10",
            "0609": "7245.60",
            "0670": "185.50",
        }
        for field, value in expected.items():
            self.assertEqual(result.fields[field], value, field)
        self.assertFalse(result.independently_validated)
        self.assertIn("pending", result.status)

    def test_withholding_changes_balance_without_changing_taxable_income(self) -> None:
        changed = {
            **self.facts,
            "salary_withholding": replace(self.facts["salary_withholding"], value="7300.00"),
        }
        result = calculate(changed, self.coverage, self.policy)
        self.assertEqual(result.fields["0670"], "85.50")
        self.assertEqual(result.fields["0435"], "34060.00")

    def test_bank_fees_do_not_silently_reduce_gross_interest(self) -> None:
        changed = {**self.facts, "bank_fees": replace(self.facts["bank_fees"], value="500.00")}
        self.assertEqual(calculate(changed, self.coverage, self.policy).fields["0027"], "240.00")

    def test_money_is_exact_and_ambiguous_or_binary_values_fail(self) -> None:
        self.assertEqual(money("38.500,00"), Decimal("38500.00"))
        for value in (38.5, True, "1e3", "NaN", "38,500.00", "1.001", "", "1,2"):
            with self.subTest(value=value), self.assertRaises(InputError):
                money(value)

    def test_missing_unknown_or_unconfirmed_is_not_zero(self) -> None:
        for facts, coverage in (
            ({k: v for k, v in self.facts.items() if k != "interest"}, self.coverage),
            (self.facts, {**self.coverage, "all_sources": False}),
            (
                {**self.facts, "interest": replace(self.facts["interest"], confirmed=False)},
                self.coverage,
            ),
        ):
            with self.assertRaises(InputError):
                calculate(facts, coverage, self.policy)

    def test_unimplemented_branches_block_instead_of_assuming_zero(self) -> None:
        for key, value in (
            ("birth_date", "1960-12-31"),
            ("salary", "16000.00"),
            ("in_kind", "100.00"),
            ("employer_pension", "1.00"),
        ):
            with self.subTest(key=key), self.assertRaises(InputError):
                calculate(
                    {**self.facts, key: replace(self.facts[key], value=value)},
                    self.coverage,
                    self.policy,
                )

    def test_scale_boundary_uses_source_quota(self) -> None:
        for schedule in (
            self.policy.state_scale,
            self.policy.regional_scale,
            self.policy.savings_scale,
        ):
            for band in schedule:
                self.assertEqual(scale(band.lower, schedule), band.quota)


class WorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.store = FileStore(Path(self.temporary.name) / "state")
        self.workbench = Workbench(Sources(), self.store)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def command(self, *, complete: bool = True) -> dict[str, Any]:
        state = self.workbench.view()
        return {
            "version": state["version"],
            "source_digest": state["source_digest"],
            "request_id": "test-command-00000001",
            "facts": {
                k: {"value": v["value"], "document_id": v["document_id"], "confirmed": complete}
                for k, v in state["facts"].items()
            },
            "coverage": dict.fromkeys(COVERAGE_LABELS, complete),
            "draft_confirmed": complete,
        }

    def test_partial_save_resumes_and_never_emits_a_total(self) -> None:
        state = self.workbench.confirm_and_calculate(self.command(complete=False))
        self.assertEqual(state["result"]["status"], "blocked_partial_review")
        self.assertNotIn("0670", state["result"]["fields"])
        resumed = Workbench(Sources(), self.store).view()
        self.assertEqual(resumed["version"], 1)
        self.assertFalse(resumed["facts"]["salary"]["confirmed"])

    def test_independent_local_writers_cannot_overwrite_a_newer_version(self) -> None:
        stale_state = self.workbench.state()
        self.workbench.confirm_and_calculate(self.command())
        stale_state["version"] = 1
        second_store = FileStore(Path(self.temporary.name) / "state")
        with self.assertRaisesRegex(InputError, "otro proceso"):
            second_store.save(stale_state)

    def test_confirmation_compares_only_supplied_and_confirmed_draft_fields(self) -> None:
        state = self.workbench.confirm_and_calculate(self.command())
        self.assertEqual(len(state["result"]["comparisons"]), 5)
        self.assertTrue(all(row["status"] == "equal" for row in state["result"]["comparisons"]))
        self.assertFalse(state["result"]["independently_validated"])

    def test_draft_optional_without_fabricated_prior_values(self) -> None:
        command = self.command()
        command["draft_confirmed"] = False
        state = self.workbench.confirm_and_calculate(command)
        self.assertEqual(state["result"]["comparisons"], [])
        self.assertIn("0670", state["result"]["fields"])

    def test_stale_commands_and_conflicting_idempotency_are_rejected(self) -> None:
        command = self.command()
        self.workbench.confirm_and_calculate(command)
        self.assertEqual(self.workbench.confirm_and_calculate(command)["audit_event_count"], 1)
        conflict = copy.deepcopy(command)
        conflict["facts"]["salary"]["value"] = "39000.00"
        with self.assertRaisesRegex(InputError, "idempotente"):
            self.workbench.confirm_and_calculate(conflict)
        stale = copy.deepcopy(command)
        stale["request_id"] = "test-command-00000002"
        with self.assertRaisesRegex(InputError, "obsoleta"):
            self.workbench.confirm_and_calculate(stale)

    def test_cross_case_evidence_and_cloud_local_identity_fail_closed(self) -> None:
        with self.assertRaises(InputError):
            Workbench(Sources(), self.store, profile="production")
        command = self.command()
        command["facts"]["salary"]["document_id"] = "../C002/D002"
        with self.assertRaises(InputError):
            self.workbench.confirm_and_calculate(command)
        with self.assertRaises(InputError):
            admitted(ROOT, "evals/expected/do-not-read.json")

    def test_pdf_export_is_provisional_and_has_no_active_script(self) -> None:
        self.workbench.confirm_and_calculate(self.command())
        reader = PdfReader(BytesIO(pdf_packet(self.workbench.packet())))
        text = " ".join(page.extract_text() or "" for page in reader.pages)
        self.assertIn("185.50", text)
        self.assertIn("PROVISIONAL", text)
        self.assertNotIn("/JavaScript", str(reader.trailer))

    def test_http_origin_host_and_csrf_protection(self) -> None:
        server = make_server(self.workbench, Sources(), 0)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            conn = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=10)
            conn.request("GET", "/api/case")
            response = conn.getresponse()
            state = json.loads(response.read())
            self.assertEqual(response.status, 200)
            self.assertIn(
                "frame-ancestors 'none'", response.getheader("Content-Security-Policy") or ""
            )
            conn.request(
                "POST",
                "/api/calculate",
                body=json.dumps(self.command()),
                headers={"Content-Type": "application/json", "Origin": "https://example.invalid"},
            )
            response = conn.getresponse()
            response.read()
            self.assertEqual(response.status, 403)
            conn.request("GET", "/api/case", headers={"Host": "attacker.invalid"})
            response = conn.getresponse()
            response.read()
            self.assertEqual(response.status, 403)
            self.assertIn("csrf_token", state)
            conn.close()
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=2)

    def test_rule_change_invalidates_saved_export(self) -> None:
        root = Path(self.temporary.name) / "sources"
        for folder in ("data/rules/2025", "data/development/2025/c001", "evals/inputs/C001"):
            shutil.copytree(ROOT / folder, root / folder)
        workbench = Workbench(Sources(root), self.store)
        self.workbench = workbench
        workbench.confirm_and_calculate(self.command())
        path = root / "data/rules/2025/rule-register.json"
        path.write_bytes(path.read_bytes() + b"\n")
        self.assertTrue(workbench.view()["result_is_stale"])
        with self.assertRaisesRegex(InputError, "obsoleto"):
            workbench.packet()

    def test_tampered_source_cannot_be_used(self) -> None:
        root = Path(self.temporary.name) / "sources"
        shutil.copytree(ROOT / "evals/inputs/C001", root / "evals/inputs/C001")
        path = root / "evals/inputs/C001/documents/D002.pdf"
        path.write_bytes(path.read_bytes() + b"tampered")
        with self.assertRaisesRegex(InputError, "Hash"):
            Sources(root).case("C001")


if __name__ == "__main__":
    unittest.main()
