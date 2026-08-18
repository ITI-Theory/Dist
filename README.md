# Dist — Distribution Repository

| Directory | Contents |
|---|---|
| `papers/` | All individual paper PDFs + omnibus builds |
| `lulu/` | Print-ready hardcover files for Lulu |
| `nlm-min/` | NotebookLM: 2-file general corpus |
| `nlm-max/` | NotebookLM: full expert corpus (one file per paper) |
| `zenodo/` | Zenodo upload queue, form fields, DOI runbook |
| `stuff/` | Stickers, cheat sheet, cover artwork |
| `PROMPTS.md` | 50+ example questions by audience type |

---

## Release process

This is the canonical operational runbook. Commands run in `U`, but release
decisions, accepted artifacts, registry metadata, and public distribution are
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
and artifacts affected.

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
   [zenodo/README.md](zenodo/README.md) for new records or **New version**.
   Record concept DOI, version DOI, and changed status in `PAPERS.yaml`.
9. **Close the loop**: update public README/DOI mirrors, release log, and
   issues; commit and tag U and Dist together. If an update changes a candidate,
   return to step 3 for that track.

### Current RC2 hand-off

- U tag: `v1.0.0-rc2` (`33b25c9`)
- Dist tag: `v1.0.0-rc2` (`e7d7f88`)
- Papers next: accept the staged paper omnibus and changed formal records.
- [T]-Theory next: finish cheatsheet/Sherlock review, then stage the Fractal
  Thesis and print volumes for NotebookLM and Lulu review.

Detailed local build and Zenodo form instructions live in `U/PROCESS.md` and
`zenodo/README.md`; they do not override this sequence.

### NLM min vs max — update rules

| Corpus | Files | Rebuild when |
|---|---|---|
| **min** | 2 files: omnibus + fractal omnibus | Omnibus or fractal omnibus is rebuilt |
| **max** | One file per paper + collected works | Any paper changes; add new papers as `PNN-slug.pdf` |

---

## Release log

*New release at bottom. Separator line between each release.*

═══════════════════════════════════════════════════════════════

### Frankenstein — 2026-08-10

21 canonical papers (P1–P21), 15 fractal programme books, OS axioms machine-verified (0 sorries).
All four former proof obligations closed. 3 Lulu hardcovers. NLM notebook live.

Zenodo: new records P10–P20 + C2 + C1v2 + P14–P15; existing P1–P9, D1–D2, C1.

═══════════════════════════════════════════════════════════════

### frankenstein-p1 patch — 2026-08-10 (4 version updates, pending)

Content changed after initial upload. Each needs **New version** on Zenodo:

| Record | DOI | What changed |
|---|---|---|
| P11 zoomable-somatic-field | [21873391](https://doi.org/10.5281/zenodo.21873391) | Problems 1+2 closed; axiom table updated |
| P12 experimental-validation | [21873456](https://doi.org/10.5281/zenodo.21873456) | “Open Problem 5” → “GAP-1 in USF test suite” |
| C1v2 omnibus-v2 | [21873942](https://doi.org/10.5281/zenodo.21873942) | Rebuilt with updated P11 |
| C2 fractal-programme | [21873722](https://doi.org/10.5281/zenodo.21873722) | Rebuilt with TOC + updated P12 content |

═══════════════════════════════════════════════════════════════

### Phase 1 wrap — 2026-08-?? (in progress)

Lean build clean: SomaField + DyadicField (exit 0, 2590 jobs, 2026-08-13).

Zenodo: P21 (⚠ pending review) + new records P22, P23, P24.
DOIs to fill: see `zenodo/README.md`.

