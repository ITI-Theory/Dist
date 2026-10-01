# Dist — Distribution Repository

| Directory | Contents |
|---|---|
| `papers/` | Individual paper PDFs, datasets with PDFs, and omnibus builds |
| `lulu/` | Print-preview candidates for Lulu hardcovers |
| `nlm-min/` | NotebookLM: 2-file general corpus |
| `nlm-max/` | NotebookLM: expert corpus, one file per paper plus collections |
| `zenodo/` | Zenodo upload queue, public metadata, DOI runbook |
| `stuff/` | Stickers, cheat sheet, cover artwork |
| `interactive/` | Static public web artefacts |
| `PROMPTS.md` | Example questions by audience type |

---

## Release process

This is the canonical operational runbook. Commands run in `U`, but release
decisions, accepted artefacts, registry metadata, and public distribution are
owned here in `Dist`.

`PAPERS.yaml` is the master registry. In `U`, adopt it deliberately with
`make generate`; do not maintain a second hand-written release list.

### Release board

There are two acceptance tracks. Do not mix their UAT decisions or their
external actions.

| Track | Principal candidate | Main UAT | External action |
|---|---|---|---|
| **Papers** | `omnibus-a4.pdf`, changed canonical papers, D1/D2 | Scientific consistency, source/claim review, NotebookLM | Zenodo new versions/new records |
| **[T]-Theory** | Fractal Thesis, Volumes I/II, cheatsheet | Reader/cheatsheet review, NotebookLM, print review | Lulu; C2 Zenodo version only after thesis acceptance |

### The release cycle

Release is iterative, not a one-way software deployment. A content correction,
metadata change, or Zenodo decision can require another candidate build and a
repeat of the relevant UAT track. Keep the cycle narrow: repeat only the track
and artefacts affected.

1. **Reconcile external truth**: run `cd U && py bin/zenodo-audit --json uat/zenodo-community.json`.
   Resolve any missing record, untracked community record, or version-versus-concept
   DOI drift before choosing an external release action.
2. **Select scope**: decide `papers` or `ttheory`; record the selected registry
   records and intended Zenodo/Lulu action in `ISSUES.md`.
3. **Build candidates in U**:
   - `cd U && make generate`
   - Papers: `make registry-papers && make uat-stage-papers`
   - [T]-Theory: `make registry-fractal && make uat-stage-ttheory`
4. **Automated gate**: run `cd U && make uat-check`. Resolve a failing check
   or explicitly defer it before continuing.
5. **NotebookLM UAT before print**: upload the selected PDFs from
   `U/uat/staging/<track>/`. The generated `MANIFEST.md` records source paths
   and SHA-256 hashes. Use a fresh private `nlm-uat` notebook; record outcomes
   in `U/paper/UAT.md` and the active issue.
6. **Lulu review for [T]-Theory only**: after NotebookLM acceptance, inspect
   the staged Volumes I/II in Lulu's print preview. Do not use Lulu as the
   first PDF test.
7. **Promote accepted PDFs to Dist**: use the registry-generated targets from
   U (`make papers`, `make nlm`, `make lulu`, or the selected copy rule). Then
   verify paths and checksums against the UAT staging manifest.
8. **Zenodo actions**: only for accepted formal records. Follow
   [zenodo/README.md](zenodo/README.md). Uploads are moving to
   `U/bin/zenodo-publish` with sandbox and dry-run defaults; do not hand-edit
   metadata that belongs in `zenodo/metadata.yaml`.
9. **Close the loop**: update public README/DOI mirrors, release log, and
   issues; commit and tag U and Dist together. If an update changes a candidate,
   return to step 3 for that track.

### Current state — 2026-10-01

- U has built and staged the current candidates: paper omnibus `omnibus-a4.pdf`
  (427 pages), Fractal Thesis (1,296 pages), Vol I (680 pages), Vol II
  (655 pages), all fifteen standalone [T]-Theory books, and the booklet set.
- Candidates are staged in `U/uat/staging/papers/` and
  `U/uat/staging/ttheory/` with SHA-256 manifests.
- UAT has **not** started. By the author's decision, the app/Atlas review comes
  first; then NotebookLM UAT, Lulu preview, promotion to Dist, and Zenodo.
- Zenodo publication should use the scripted path: sandbox first, dry-run by
  default, live only after UAT acceptance and author approval.
- `PAPERS.yaml` is the registry source for IDs, files, titles, levels, and DOI state.

Detailed local build and Zenodo form instructions live in `U/PROCESS.md` and
`zenodo/README.md`; they do not override this sequence.

### NLM min vs max — update rules

| Corpus | Files | Rebuild when |
|---|---|---|
| **min** | 2 files: paper omnibus + Fractal Thesis | Either omnibus is rebuilt |
| **max** | 30 PDFs: 24 papers + 4 collection/volume files + D2 + cheatsheet | Any paper, collection, or cheatsheet changes |

Datasets in the public registry are E1, D1, and D2. E1 has no single Dist PDF;
D1 is carried by the paper release/omnibus; D2 is the formal appendix PDF.

---

## Release log

*New release at bottom. Separator line between each release.*

═══════════════════════════════════════════════════════════════

### Frankenstein — 2026-08-10

21 canonical papers (P1–P21), 15 fractal programme books, OS axiom work, and
3 Lulu hardcovers. NLM notebook live.

Correction note added 2026-10-01: earlier public wording from this release
overstated the evidence. Treat old M-theory derivation phrasing as an
11-dimensional modelling motivation; QUANT-EXP-1 as an exact 8-qubit
statevector simulation, not a hardware experiment; and zero-sorry/all-obligations
phrasing as superseded by the current proof-surface ledger (20 axioms and seven
real `sorry`s remain).

Zenodo: new records P10–P20 + C2 + C1v2 + P14–P15; existing P1–P9, D1–D2, C1.

═══════════════════════════════════════════════════════════════

### frankenstein-p1 patch — 2026-08-10 (superseded)

This 4-record queue is obsolete. The 2026-10-01 hardening pass changed the
larger public surface, so Zenodo actions are now tracked in the current table
in `zenodo/README.md`.

═══════════════════════════════════════════════════════════════

### Phase 1 wrap — 2026-08-?? (superseded by 2026-10-01 hardening)

The previous P21–P24-only upload plan is no longer sufficient. P21 now awaits
author review; P22–P24 remain first-upload candidates; D1, D2, P1–P20, C1v2,
and C2 need new versions after the hardening pass.

═══════════════════════════════════════════════════════════════

### 2026-10-01 — Hardening and Fractal Thesis rewrite

- All 24 papers and D1/D2 were hardened for proof status, simulation wording,
  clinical/physical claims, and Planck 2018 cosmology comparisons.
- P4's public title changed to **The Soma-Field Research Programme: Method,
  Model, and Computational Test**.
- All fifteen [T]-Theory books are source-owned and rewritten with
  "[T]-Theory: <Name>" titles; the former consciousness book is now
  **[T]-Theory: Philosophy**.
- Current candidate page counts: paper omnibus 427 pages; Fractal Thesis
  1,296 pages; Vol I 680 pages; Vol II 655 pages.
- Zenodo will be uploaded through `U/bin/zenodo-publish` after sandbox and
  dry-run checks; per-record metadata lives in `zenodo/metadata.yaml`.
