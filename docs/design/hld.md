# High level design

**Proposed, 21 October 2026.** This is the first architecture hypothesis for the agreed review packet. The application and cloud components are not implemented.

```mermaid
flowchart LR
    U[Individual or authorised reviewer] --> UI[Review workbench]
    UI --> API[Authenticated application boundary]
    API --> INTAKE[PDF and image intake]
    INTAKE --> PRIVATE[Private immutable sources and versions]
    INTAKE --> PAGES[Versioned PDF pages and image evidence]
    PAGES --> EXTRACT[Visual fact extraction and confirmation]
    EXTRACT --> CASE[Case and fact services]
    API --> CASE
    CASE --> PRIVATE[Private immutable sources and versions]
    CASE --> JOB[Durable investigation jobs]
    JOB --> HARNESS[Bounded investigation workflow]
    CORPUS[Reviewed 2025 Balearics rule corpus] --> HARNESS
    HARNESS --> TOOLS[Scoped retrieval and deterministic rule tools]
    HARNESS --> MODEL[Bounded service model adapter]
    EXTRACT -. authorised inference .-> MODEL
    TOOLS --> VALIDATE[Independent validation]
    MODEL --> VALIDATE
    VALIDATE --> PENDING[Pending proposed field changes]
    PENDING --> REVIEW[Human review and packet export]
    REVIEW --> MANUAL[Person handles Renta WEB submission]
    API -. redacted diagnostics .-> OTEL[OpenTelemetry]
    JOB -. redacted diagnostics .-> OTEL
```

Start with one modular Python core, explicit typed domain/application interfaces and local adapters. The first retrieval baseline can be deterministic; a bounded LangGraph workflow or a higher-level harness must earn its cost through comparison. Model, extraction, persistence and cloud choices remain candidates in [ADR 0002](../decisions/0002-stack-and-reuse.md).

The rule corpus and private evidence are separate stores. Retrieval receives authorised case identity from trusted application code and filters rules by tax year, region and supported treatment. The model cannot choose another taxpayer, invoke arbitrary SQL, fetch arbitrary URLs or create permissions.

Local use and later hosted environments share domain and review logic. The public portfolio uses synthetic recorded outputs and no model connection. AWS is the preferred hosted candidate, GCP the fallback; adapt one provider after cost/runtime validation rather than implementing two stacks.

## Visual evidence boundary

The owner selected image-based PDF understanding and standalone screenshot/image support for the first usable version. Preserve originals and versioned page images; render digital/scanned PDFs and decode admitted image formats through bounded adapters. A page-image read need not depend on embedded text. Text/OCR may aid indexing or comparison. See [ADR 0003](../decisions/0003-visual-document-evidence.md).

Visual extraction and later investigation share the same explicit inference authorisation/accounting boundary. Rendering is deterministic local work; model interpretation consumes separately bounded provider resources and runs outside transactions. No image-provider compatibility, rendering implementation or model superiority is verified yet.
