═══════════════════════════════════════════════════════════════

[T]-Theory / Dist / Issues

Format: top-level # sections = one issue. Status in name: OPEN or CLOSED.
Closure line at bottom of issue: `> CLOSED: reason`.
New issues appended at end. Link to GH issue if it grows: `→ GH#NNN`.

═══════════════════════════════════════════════════════════════

# ISS-001: Phase 1 wrap review — CLOSED

**Validation framework (CM → HP → SH):**

- **Sherlock** — "Did we build it right?" Pre-release UAT: open a private NotebookLM (`nlm-uat`)
  with Omnibus V2, Fractal Thesis, old files (for comparison), dot-files, reference docs.
  Toggle files on/off as needed. Ephemeral — delete after use, always load fresh.
  UAT process lives in U; Dist just needs the right files.

- **Harry Potter** — "Did we build the right thing?" Re-use `nlm-uat`, different questions.

- **Cookie Monster** — "Can anyone understand it?" The cheat-sheet is the Cookie Monster test.
  Validate last. Enhancement idea: footnote on Zoom Operator table linking each level to its
  supporting domain book in the Fractal Thesis.

**Other points:**
- P21–P24 are cosmological/physics-level — P23 (gateway) should emphasise this shift
- Verify all files committed and saved before release

**Paper action list (from PAPERS.yaml):**

| ID | Slug | Action |
|---|---|---|
| P11 | zoomable-somatic-field | Zenodo → New version |
| P12 | experimental-validation | Zenodo → New version |
| C1v2 | omnibus-v2 | Zenodo → New version |
| C2 | ttheory-fractal-programme | Zenodo → New version |
| P21 | cosmological-constant-derivation | Review PDF, then upload |
| P22 | dark-matter-spatial-vacuum | Upload new record |
| P23 | ttheory-phenomena | Upload new record |
| P24 | g2-symmetry-breaking | Upload new record |

> CLOSED: action list captured above; Zenodo uploads and UAT tracked here until done.
> CM→HP→SH framework documented in U/PROCESS.md UAT section (2026-08-13).

═══════════════════════════════════════════════════════════════

# ISS-002: Phase 1 → Phase 2 directory structure — OPEN

Phase 1 = MVP (prove it works). Phase 2 = use the theory and revise Phase 1 as we go.
Dist is a clean room now. As Phase 2 produces revised papers, we need a convention.

Options:
- Same slugs / replace in place (Zenodo "New version" handles versions)
- Phase-tagged directories (`papers/p1/`, `papers/p2/`)
- PAPERS.yaml `phase: 1|2` field + replace in place

Lean towards: replace in place + `phase:` field in PAPERS.yaml.

═══════════════════════════════════════════════════════════════

# ISS-003: PDF encoding — cosmological-constant cover page — OPEN

Cover page shows broken angle brackets: `Λ ≡ ￿tr Φ￿₀` — should be `Λ ≡ ⟨tr Φ⟩₀`.
Fix in source `.md` (font/encoding for `⟨ ⟩`), rebuild PDF, run `sync_dist.py --papers`.

═══════════════════════════════════════════════════════════════

# ISS-004: Lulu metadata — spine info needed in PAPERS.yaml — OPEN

Lulu upload needs: spine title, spine author name.
Options per volume: `Alistair Johnson`, `A. Johnson`, `[T]-Theory`.
Add `lulu_spine_title` and `lulu_spine_author` fields to PAPERS.yaml entries for lulu files.


═══════════════════════════════════════════════════════════════

# ISS-005: Dist metadata  for Dist dirs in PAPERS.yaml — OPEN

The idea is that rather than have lists in `Dist/NLM-*,  Dist/Zenodo` et cetera we just have a tag
in PAPERS.yaml.
- [ ] Opinion needed before implementation as there may be some hidden issues that I messed.
