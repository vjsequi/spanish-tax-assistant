"""Explicitly provisional ordinary cash-employment branch; no document/model or I/O access."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from decimal import ROUND_DOWN, ROUND_HALF_UP, Decimal, InvalidOperation

ZERO = Decimal("0.00")
CENT = Decimal("0.01")
ENGINE_VERSION = "2025-ib-cash-development-0.1"


class InputError(ValueError):
    """Missing, invalid, unconfirmed or unsupported input."""


def money(value: object) -> Decimal:
    """Parse exact canonical decimals or unambiguous Spanish monetary notation."""
    if not isinstance(value, str) or len(value) > 32:
        raise InputError("Introduzca el importe como texto decimal exacto.")
    value = value.strip()
    if "," in value:
        if re.fullmatch(r"-?(?:[0-9]+|[0-9]{1,3}(?:\.[0-9]{3})+),[0-9]{2}", value) is None:
            raise InputError("Formato monetario ambiguo; use 38.500,00 o 38500.00.")
        value = value.replace(".", "").replace(",", ".")
    if re.fullmatch(r"-?[0-9]+(?:\.[0-9]{1,2})?", value) is None:
        raise InputError(
            "Se requieren como máximo dos decimales; no se admite notación científica."
        )
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise InputError("Importe no válido.") from exc
    if not result.is_finite() or abs(result) > Decimal("10000000"):
        raise InputError("Importe fuera del límite de desarrollo.")
    return result.quantize(CENT)


def rounded(value: Decimal) -> Decimal:
    # Disclosed development assumption. RQ-08 remains pending professional QA.
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class Fact:
    value: str
    document_id: str
    confirmed: bool
    page: int = 1
    method: str = "manual"


FACT_LABELS = {
    "birth_date": "Fecha de nacimiento",
    "salary": "Retribuciones dinerarias brutas",
    "social_security": "Cotizaciones a la Seguridad Social",
    "salary_withholding": "Retenciones sobre retribuciones dinerarias",
    "interest": "Intereses brutos",
    "bank_withholding": "Retenciones bancarias",
    "bank_fees": "Comisiones ordinarias de cuenta",
    "in_kind": "Valoración fiscal de retribución en especie",
    "employer_pension": "Contribución empresarial a plan de empleo",
    "worker_elected_pension": "Aportación empresarial por decisión del trabajador",
}

COVERAGE_LABELS = {
    "residence": "2025 completo, residente en Illes Balears y declaración individual ordinaria",
    "all_sources": (
        "Todos los empleadores, cuentas e ingresos están incluidos; hay un único pagador"
    ),
    "ordinary_employment": (
        "Sin atrasos, indemnizaciones, exenciones ni tratamientos laborales especiales"
    ),
    "no_dependants": (
        "Sin descendientes, ascendientes dependientes, discapacidad ni créditos familiares"
    ),
    "owned_home": (
        "Vivienda habitual en propiedad; sin alquiler pagado ni otros inmuebles o derechos"
    ),
    "no_other_income": (
        "Sin otras rentas, ganancias, imputaciones, rentas extranjeras ni subvenciones"
    ),
    "no_other_expenses": (
        "Sin cuotas sindicales/colegiales, defensa jurídica ni otros gastos laborales"
    ),
    "no_reliefs": "Sin pensiones individuales, donativos, otras reducciones o deducciones",
    "no_history": "Sin saldos pendientes de años anteriores ni deducciones a regularizar",
    "no_other_payments": (
        "Sin otros pagos a cuenta, anticipos, rectificación ni compensación con cónyuge"
    ),
}


@dataclass(frozen=True)
class Band:
    lower: Decimal
    quota: Decimal
    rate: Decimal


@dataclass(frozen=True)
class Policy:
    state_scale: tuple[Band, ...]
    regional_scale: tuple[Band, ...]
    savings_scale: tuple[Band, ...]
    allowance: Decimal
    state_minimum: Decimal
    regional_minimum: Decimal
    reduction_ceiling: Decimal
    credit_ceiling: Decimal
    digest: str


@dataclass(frozen=True)
class Stage:
    id: str
    label: str
    formula: str
    fields: dict[str, str]
    rule_ids: tuple[str, ...]


@dataclass(frozen=True)
class Calculation:
    fields: dict[str, str]
    stages: tuple[Stage, ...]
    policy_digest: str
    engine_version: str = ENGINE_VERSION
    status: str = "provisional_professional_qa_pending"
    independently_validated: bool = False
    rounding_assumption: str = (
        "Decimal ROUND_HALF_UP por casilla; tipos medios truncados. RQ-08 pendiente."
    )


def scale(base: Decimal, bands: tuple[Band, ...]) -> Decimal:
    if base < ZERO or not bands or bands[0].lower != ZERO:
        raise InputError("Base o escala no válida.")
    selected = bands[0]
    for band in bands:
        if band.lower <= base:
            selected = band
    return rounded(selected.quota + (base - selected.lower) * selected.rate / Decimal("100"))


def average(quota: Decimal, base: Decimal) -> Decimal:
    return ZERO if base == ZERO else (quota / base * 100).quantize(CENT, rounding=ROUND_DOWN)


def calculate(
    facts: Mapping[str, Fact], coverage: Mapping[str, bool], policy: Policy
) -> Calculation:
    if set(facts) != set(FACT_LABELS) or set(coverage) != set(COVERAGE_LABELS):
        raise InputError("Faltan hechos o declaraciones de cobertura; no se sustituyen por cero.")
    missing = [label for key, label in COVERAGE_LABELS.items() if coverage[key] is not True]
    if missing:
        raise InputError("Cobertura pendiente o fuera de esta primera rama: " + "; ".join(missing))
    if any(fact.confirmed is not True for fact in facts.values()):
        raise InputError("Confirme cada dato frente a su imagen antes de calcular.")
    try:
        born = date.fromisoformat(facts["birth_date"].value)
    except ValueError as exc:
        raise InputError("Fecha de nacimiento no válida.") from exc
    if not date(1961, 1, 1) <= born <= date(2007, 12, 31):
        raise InputError("Esta rama inicial cubre adultos menores de 65 años al cierre de 2025.")
    amounts = {key: money(fact.value) for key, fact in facts.items() if key != "birth_date"}
    if any(value < ZERO for value in amounts.values()):
        raise InputError("Los importes negativos necesitan una rama adicional.")
    if any(
        amounts[key] != ZERO for key in ("in_kind", "employer_pension", "worker_elected_pension")
    ):
        raise InputError("Las retribuciones en especie y pensiones aún no están implementadas.")
    salary = amounts["salary"]
    social = amounts["social_security"]
    if social > salary:
        raise InputError("Las cotizaciones superan el salario; resuelva el dato antes de calcular.")
    prior = salary - social
    # Article 20 uses income before the general other-expense allowance, not after it.
    if prior < policy.reduction_ceiling or salary < policy.credit_ceiling:
        raise InputError(
            "La reducción/crédito de rentas laborales bajas requiere la siguiente rama."
        )
    general = prior - policy.allowance
    if general < max(policy.state_minimum, policy.regional_minimum):
        raise InputError("La asignación del mínimo entre bases aún no está implementada.")
    interest = amounts["interest"]
    fields: dict[str, str] = {}
    stages: list[Stage] = []

    def stage(
        ident: str, label: str, formula: str, values: dict[str, Decimal], rules: tuple[str, ...]
    ) -> None:
        formatted = {key: format(value, ".2f") for key, value in values.items()}
        fields.update(formatted)
        stages.append(Stage(ident, label, formula, formatted, rules))

    stage(
        "S20",
        "Trabajo",
        "Bruto − Seguridad Social − gasto general anual; reducción art.20 = 0 en esta rama.",
        {
            "0003": salary,
            "0012": salary,
            "0013": social,
            "0017": prior,
            "0018": prior,
            "0019": policy.allowance,
            "0022": general,
            "0023": ZERO,
            "0025": general,
        },
        ("EMP-01", "EMP-02", "EMP-03"),
    )
    stage(
        "S30",
        "Intereses",
        "Interés bruto atribuido al 100%; retención y comisión ordinaria se conservan separadas.",
        {"0027": interest, "0036": interest, "0038": interest, "0040": interest, "0041": interest},
        ("INT-01",),
    )
    stage(
        "S40-S60",
        "Bases imponibles y liquidables",
        "Trabajo en base general; intereses en ahorro; sin otras reducciones confirmadas.",
        {
            "0432": general,
            "0435": general,
            "0429": interest,
            "0460": interest,
            "0500": general,
            "0505": general,
            "0510": interest,
        },
        ("BASE-01", "BASE-02"),
    )
    sm, rm = policy.state_minimum, policy.regional_minimum
    stage(
        "S70",
        "Mínimos",
        "Adulto menor de 65, sin dependientes/discapacidad; mínimo íntegro en base general.",
        {
            "0511": sm,
            "0512": rm,
            "0519": sm,
            "0520": rm,
            "0521": sm,
            "0522": ZERO,
            "0523": rm,
            "0524": ZERO,
        },
        ("MIN-ES-01", "MIN-IB-01"),
    )
    sg, rg = scale(general, policy.state_scale), scale(general, policy.regional_scale)
    st, rt = scale(sm, policy.state_scale), scale(rm, policy.regional_scale)
    sn, rn = sg - st, rg - rt
    ss, rs = scale(interest, policy.savings_scale), scale(interest, policy.savings_scale)
    state_gross, regional_gross = sn + ss, rn + rs
    stage(
        "S80",
        "Gravamen estatal y autonómico",
        "Escala(base) − escala(mínimo), por componente; ahorro calculado aparte.",
        {
            "0528": sg,
            "0529": rg,
            "0530": st,
            "0531": rt,
            "0532": sn,
            "0533": rn,
            "0534": average(sn, general),
            "0535": average(rn, general),
            "0536": ss,
            "0537": rs,
            "0538": ZERO,
            "0539": ZERO,
            "0540": ss,
            "0541": rs,
            "0542": average(ss, interest),
            "0543": average(rs, interest),
            "0545": state_gross,
            "0546": regional_gross,
        },
        ("SCALE-ES-G", "IB-SCALE-G", "SCALE-SAVINGS"),
    )
    total = state_gross + regional_gross
    stage(
        "S90-S110",
        "Cuota resultante",
        "Sin deducciones/reducciones adicionales confirmadas; crédito laboral 2025 = 0 por renta.",
        {
            "0570": state_gross,
            "0571": regional_gross,
            "0585": state_gross,
            "0586": regional_gross,
            "0587": total,
            "0414": ZERO,
            "0595": total,
        },
        ("LIQUID", "EMP-CREDIT-2025"),
    )
    paid = amounts["salary_withholding"] + amounts["bank_withholding"]
    result = total - paid
    stage(
        "S120-S140",
        "Resultado provisional",
        "Cuota resultante − pagos a cuenta; sin créditos/anticipos familiares confirmados.",
        {
            "0596": amounts["salary_withholding"],
            "0597": amounts["bank_withholding"],
            "0609": paid,
            "0610": result,
            "0670": result,
        },
        ("PAY-01", "RESULT"),
    )
    return Calculation(fields, tuple(stages), policy.digest)
