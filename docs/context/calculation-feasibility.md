# Complete-calculation scope research

**21 October 2026; research, not an implemented or independently validated engine.** The owner requires a complete independent payable/refundable result for the supported 2025 profile. Salary and bank interest alone do not establish that all material facts are present. A completeness screen must expose other income, reliefs, prior-year balances and personal/family circumstances before a whole-return result can be issued.

**Subsequent specification:** the [detailed requirements](../requirements/tax-2025.md) now map 17 stages, 108 form fields and 25 draft rule contracts to fifteen retained references. This earlier brief remains research context; the pinned specification takes precedence for the next review. Exact tax treatment and labels remain unvalidated.

## Deterministic chain to specify and review

| Stage | Facts and rules to establish | Official starting point |
|---|---|---|
| Tax context | Residence, Balearic jurisdiction, ordinary regime, individual filing, period and original-return status | [2025 practical manual](official-sources.md) |
| Employment income | Each employer's attributable cash/kind income, applicable exemptions/reductions, evidenced deductible expenses and net-income adjustments | [AEAT employment calculation scheme](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c03-rendimientos-trabajo/rendimiento-neto-trabajo-integrar-base-imponible/esquema-general.html) |
| General and savings bases | Gross taxable interest, ownership attribution, classification and current/prior-year offsetting | [AEAT integration and offsetting](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c12-integracion-compensacion-rentas.html) |
| Bases liquidables | Applicable reductions, including supported pension contributions, with ordering and limits | [AEAT base reductions](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c13-determinacion-renta-contribuyente-sujeta-gravamen/reducciones-base-imponible-general.html) |
| Gross liability | Separate state/regional and general/savings calculations; applicable personal/family minima | [AEAT liability method](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/introduccion/general.html), [Balearic minima](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c14-adecuacion-impuesto-circunstancias-personales/minimo-autonomico-personal-familiar/comunidad-autonoma-illes-balears.html) |
| Deductions/adjustments | Applicable national/regional credits, ordering, caps and incompatibilities, including the distinct 2025 employment-income deduction | [AEAT 2025 employment deduction](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/deducciones-cuota-liquida-total/deduccion-obtencion-rendimientos-trabajo.html) |
| Final result | Evidenced withholding/payments on account, applicable refundable family benefits and advance-payment reconciliation | [AEAT final calculation stages](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion.html) |

Personal/family minima are part of the liability method, not a blanket subtraction from gross salary. Child-related conditions can involve entitlement, income and filing by dependants; see [AEAT descendant conditions](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c14-adecuacion-impuesto-circunstancias-personales/minimo-descendientes/concepto-requisitos-descendientes.html). Supporting a regional childcare deduction alone does not cover every family-related effect on a final result.

## Product decisions and engineering work

The owner selects the employment/family/relief branches required for the first release. Engineers and the independent tax reviewer establish definitions, applicable year-specific scales, amounts, allocation, ordering, rounding and exact field mapping. These legal facts are not preferences for the owner to invent.

Maintain a versioned coverage checklist: each material branch is supported with confirmed facts, explicitly established as inapplicable, or unresolved/unsupported. Unknown is not false or zero. Property/imputed property income, grants, disposals, foreign income, carryforwards and other material reliefs cannot disappear merely because the visible documents contain salary and interest.

Use supplied AEAT values only for comparison. Derive intermediate bases, liability and balance from confirmed input facts; isolate independent expected answers in the scorer/reviewer. Check stages and fields as well as the total so compensating errors cannot pass.

These mutable official links orient specification. Retain exact source versions and obtain independent field-level expectations before rule freezing. The separate [deduction brief](deduction-feasibility.md) records unresolved rent/childcare source questions. No numeric rates, thresholds or rounding implementation has been selected or tested here.
