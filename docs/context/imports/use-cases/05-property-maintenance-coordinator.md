---
created: 2026-10-20
status: candidate
tags: [ai, use-cases, property]
---

# Property Maintenance Coordinator

[Use cases index](00-ai-production-use-cases.md)

Help a small property manager clarify maintenance requests, find duplicate tickets, gather relevant history and prepare work orders. The recurring work combines resident communication, records and coordination.

## Established example

[AppFolio's case study](https://claude.com/customers/appfolio) describes AI assistance using resident history, existing maintenance tickets and property policies. Its [maintenance product](https://www.appfolio.com/property-manager/maintenance) includes a coordination workflow. A portfolio implementation could cover a small set of request types for one operator.

## Demonstration case

A resident reports that a washing machine is leaking. Another household member has already opened a ticket, and a contractor visited recently. The coordinator links the duplicate, checks the repair history, asks for missing practical details and prepares the next work order for staff review.

## First scope

Handle routine appliance and maintenance requests with an operator-approved routing policy. Identify urgent or out-of-scope situations for human escalation. Keep contractor commitments and expenditure subject to approval.

## Security and operation

Restrict access by property and role. Protect resident contact details and access instructions. Treat attachments and resident messages as untrusted. Duplicate reports must not trigger duplicate contractor orders; updates and cancellations need explicit state transitions.

Observe unassigned cases, failed notifications, contractor handoffs and unresolved-case age. Record why a request was escalated and what a staff member changed.

## Evaluation

Test duplicate detection, correct property context, necessary questions, routing and escalation. Include conflicting descriptions, missing contact information, an urgent report and an existing unresolved repair. Measure staff effort and time to an appropriate next step.

## Main dependency

A property manager who can validate the process, particularly urgency and escalation. Synthetic cases support development, while actual user feedback is needed to establish usefulness.
