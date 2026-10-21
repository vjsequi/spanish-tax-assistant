# Synthetic evaluation inputs

Twenty synthetic development cases are retained with source hashes in [the manifest](manifest.json). Every case contains opaque metadata and visible PDF/image source documents; case metadata has no answer keys, scenario labels or self-confirmed facts. All facts and independent tax judgements remain pending review.

The pack has 110 source files/180 pages. C018 supplies the agreed 30-file/100-page workload; no timing has been measured. C016 uses PNG/JPEG and a PDF without embedded text; C017 deliberately blurs a salary source. C015 contains hostile instructions as inert document data. Five cases include unverified partial draft excerpts for future comparison; those supplied values are not ground truth. Documents use simplified synthetic layouts and no real taxpayer details, NIFs or bank accounts.

C016 pairs the first three C001 sources for a controlled extraction comparison. C001's fourth document, a partial draft, has no C016 counterpart; the cases are not identical downstream comparison tasks. Preserve this distinction when designing an experiment.

Use [the review guide](../review/reviewer-guide.md) to arrange independent review. `python -m scripts.check_tax_pack` verifies integrity and input isolation, not expected answers or tax behaviour.
