# Dist Release Board

Canonical release sequencing is in `README.md`. This file is the short list
of live decisions and external actions. Historical issue detail belongs in git
history and the U research issue tracker.

## RC2 Baseline - 2026-08-16

- U: `v1.0.0-rc2` at `33b25c9`
- Dist: `v1.0.0-rc2` at `e7d7f88`
- D1 `SFT-DEMO-CASE.pdf` is present in `papers/`.
- Automated UAT passed 12 checks at RC2; follow-up acceptance is track-specific.

## ISS-001: Papers Track Acceptance - OPEN

**Purpose:** accept the scientific paper release before any Zenodo action.

- [x] Build and stage Papers candidates in U: `make uat-stage-papers`
- [x] NotebookLM UAT: paper omnibus plus changed formal records (accepted 2026-08-18; C-3 reader bridges deferred)
- [ ] Review P21 before first Zenodo upload
- [ ] Verify accepted staged hashes against `papers/`
- [ ] Execute Zenodo actions: P11, P12, D2, C1v2 new versions; P21-P24 new records
- [ ] Record concept/version DOIs in `PAPERS.yaml`, `zenodo/README.md`, and public README mirrors

## ISS-002: [T]-Theory Track Acceptance - OPEN

**Purpose:** finish Fractal Thesis/print acceptance independently of Papers.

- [ ] Complete the Gateway cheatsheet review, then apply the approved pattern to the remaining domain sheets
- [ ] Build and stage [T]-Theory candidates in U: `make uat-stage-ttheory`
- [ ] NotebookLM UAT: Fractal Thesis and Gateway cheatsheet
- [ ] Lulu preview: Volumes I and II after NotebookLM acceptance
- [ ] Verify accepted staged hashes against `papers/`, `nlm-*`, and `lulu/`
- [ ] Create C2 Zenodo new version only after Fractal Thesis acceptance

## ISS-003: Registry and Public Mirrors - OPEN

- [ ] Classify or remove untracked `PAPERS.md`; `PAPERS.yaml` remains the master registry
- [x] Resolve RC2 Zenodo audit: normalize 13 version DOIs to concept DOIs in `PAPERS.yaml`
- [x] Add the public QUANT-EXP-1 experiment record (`10.5281/zenodo.20438007`)
- [ ] After each accepted Zenodo action, update DOI mirrors in U, `.github`, and `.github-private`
- [ ] Keep `zenodo/README.md`, `nlm-min/README.md`, `nlm-max/README.md`, and `lulu/README.md` aligned with current file names and counts

## Closed Historical Items

- PDF angle-bracket encoding was fixed in U and rebuilt before RC2.
- Lulu spine metadata is stored in `PAPERS.yaml`.
- Registry-driven distribution targets are implemented through `U/mk/dist.mk`.
