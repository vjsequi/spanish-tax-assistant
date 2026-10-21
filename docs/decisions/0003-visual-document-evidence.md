# ADR 0003 Visual document evidence

**Status: accepted product direction, proposed implementation, 21 October 2026.** The owner rejected limiting the first version to text-based PDFs, explicitly included certificates, receipts, screenshots and other information sources, and preferred images when interpreting PDFs based on Oposiciones experience.

## Decision

Support visual document evidence in the first usable release. Preserve digital/scanned PDF originals and render their pages; admit standalone images/screenshots through tested adapters. Use page/image interpretation as the primary path for these media, with embedded text/OCR available for search, cross-checks and comparison. Keep manual fact confirmation, exact typed values and source-linked changes.

Certificates and receipts describe what information arrives; PDF/PNG/JPEG and other admitted formats describe how it arrives. Keep adapters extensible and define exact accepted types and resource bounds during feasibility. Accepting more document sources does not extend the confirmed tax profile or imply every file format is supported.

## Evidence and limits

The [native ConceptLock inspection](../context/document-ingestion-lessons.md) found rendered full-page PNGs, image attachments and page/clip support metadata, with digital text as an auxiliary/fallback route. It supplies a useful local engineering reference. Its current fresh-module route is governed separately; no workflow or provider was run and no code was copied. Neither those unit tests nor the owner's experience establishes measured superiority on tax documents.

Bind facts to original and derived-image hashes, pages and valid regions or explicit whole-page anchors. Retain visible transcription and normalised value separately. Check unclear amounts, signs, dates and column context with the reviewer. A model quote or a bounding box does not prove correct reading or authenticity.

## Consequences and next evidence

Rendering/decoding adds CPU, memory, image storage and potential provider cost. Test malformed/oversized inputs and bound pages, pixels, time and calls. Preserve full-page context and deterministic source/configuration identity for crops/cache reuse. Telemetry records safe operation/resource outcomes without image data or tax text.

Compare embedded-text, OCR-assisted, visual and optional hybrid paths on matched synthetic documents and independently reviewed facts, then choose render resolution, decoder/extractor components and model from results. Rendering may be tested offline; real visual-model evaluation still requires fresh explicit resource authorisation. No intake/extractor implementation or tax-quality result is produced by this ADR.
