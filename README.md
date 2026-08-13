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

**Order:** build → sync → Zenodo → Lulu → NLM → READMEs → commit.

1. **Build** — `cd U/paper && make all` (rebuilds all PDFs from source)
2. **Sync** — run `python U/paper/scripts/sync_dist.py` (copies PDFs → `papers/`, `nlm-min/`, `nlm-max/`, `lulu/`, `stuff/`)
3. **Zenodo** — follow `zenodo/README.md`:
   - New records: upload PDF → fill form fields → Publish → record DOI
   - Version patches: go to record → **New version** → upload → Publish
4. **Lulu** — follow `lulu/README.md` if print content changed
5. **NLM** — replace source PDFs per `nlm-min/README.md` and `nlm-max/README.md`
6. **Fill DOIs** — update `zenodo/README.md` DOI table + `U/.github/copilot-instructions.md`
7. **Commit & push** — `Dist`, `U`, `.github-private`, `.github`

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

