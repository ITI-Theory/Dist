# Dist Release Board

Canonical release sequencing is in `README.md`. This file is the short list
of live decisions and external actions. Historical issue detail belongs in git
history and the U research issue tracker.

## Current Baseline — 2026-10-01

- U candidates are built and staged, but UAT has not started.
- Author decision: app/Atlas review first, then NotebookLM UAT, Lulu preview,
  promotion, and Zenodo.
- `PAPERS.yaml` remains the master registry.

## ISS-001: Papers Track Acceptance — OPEN

**Purpose:** accept the scientific paper release before any Zenodo action.

- [x] Build and stage Papers candidates in U: `U/uat/staging/papers/`
- [x] Harden D1, D2, and P1–P24 for simulation/proof/clinical claim wording
- [ ] Author review of P21 before first Zenodo upload
- [ ] NotebookLM UAT: paper omnibus plus changed formal records
- [ ] Verify accepted staging hashes against promoted `Dist` files
- [ ] Scripted Zenodo upload: sandbox test, then live new versions/new records
- [ ] Record concept/version DOIs in `PAPERS.yaml`, `zenodo/README.md`, and public mirrors

## ISS-002: [T]-Theory Track Acceptance — OPEN

**Purpose:** finish Fractal Thesis/print acceptance independently of Papers.

- [x] Build and stage [T]-Theory candidates in U: `U/uat/staging/ttheory/`
- [x] Rewrite all fifteen domain books with hardened evidence labels
- [ ] NotebookLM UAT: Fractal Thesis, Vol I/II, and representative booklets
- [ ] Lulu preview: paper omnibus, Vol I, and Vol II after NotebookLM acceptance
- [ ] Verify accepted staged hashes against `papers/`, `nlm-*`, and `lulu/`
- [ ] Create C2 Zenodo new version only after Fractal Thesis acceptance

## ISS-003: Registry and Public Mirrors — OPEN

- [x] Resolve RC2 Zenodo audit: normalise version DOI handling in `PAPERS.yaml`
- [x] Add the public QUANT-EXP-1 simulation record (`10.5281/zenodo.20438007`)
- [x] Harden Zenodo community text to paste
- [ ] Finish `zenodo/metadata.yaml` and keep it aligned with `zenodo/README.md`
- [ ] Promote accepted PDFs and verify SHA-256 hashes against UAT manifests
- [ ] After each accepted Zenodo action, update DOI mirrors in U, `.github`, and `.github-private`

## Closed Historical Items

- PDF angle-bracket encoding was fixed in U and rebuilt before RC2.
- Lulu spine metadata is stored in `PAPERS.yaml`.
- Registry-driven distribution targets are implemented through `U/mk/dist.mk`.
