#!/usr/bin/env python3
"""
sync_dist.py — Sync built PDFs from U repo into Dist subdirectories.

Run after any paper/omnibus/fractal rebuild to keep Dist current.

Usage (from Dist/ or anywhere):
    python sync_dist.py           # sync all
    python sync_dist.py --nlm     # nlm-min and nlm-max only
    python sync_dist.py --papers  # papers/ only
"""

import argparse
import shutil
from pathlib import Path

# ── paths ────────────────────────────────────────────────────────────────────
DIST  = Path(__file__).parent
U     = DIST.parent / "U"          # ITI-Theory/U
PAPER = U / "paper" / "bld"
FRAC  = U / "Part2" / "fractal-programme" / "bld"

def cp(src: Path, dst: Path):
    if not src.exists():
        print(f"  SKIP (missing): {src.name}")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  {src.name} → {dst.relative_to(DIST)}")

# ── paper catalogue ───────────────────────────────────────────────────────────
# (source filename in bld/, dest name in papers/)
PAPER_FILES = [
    ("soma-field-paper.pdf",             "soma-field-paper.pdf"),
    ("quantum-soma-penrose.pdf",          "quantum-soma-penrose.pdf"),
    ("mathematical-co-identification.pdf","mathematical-co-identification.pdf"),
    ("soma-field-synthesis.pdf",          "soma-field-synthesis.pdf"),
    ("soma-physical-substrate.pdf",       "soma-physical-substrate.pdf"),
    ("soma-field-book.pdf",               "soma-field-book.pdf"),
    ("soma-field-patient-pov.pdf",        "soma-field-patient-pov.pdf"),
    ("the-tensor.pdf",                    "the-tensor.pdf"),
    ("music-affect-dynamics.pdf",         "music-affect-dynamics.pdf"),
    ("soma-temporal-dynamics.pdf",        "soma-temporal-dynamics.pdf"),
    ("zoomable-somatic-field.pdf",        "zoomable-somatic-field.pdf"),
    ("experimental-validation.pdf",       "experimental-validation.pdf"),
    ("missing-limbic-layer.pdf",          "missing-limbic-layer.pdf"),
    ("usf-euclidean-qft.pdf",             "P14-usf-euclidean-qft.pdf"),
    ("usf-interacting-qft.pdf",           "P15-usf-interacting-qft.pdf"),
    ("geographic-somatic-field.pdf",      "geographic-somatic-field.pdf"),
    ("gestalt-field-dynamics.pdf",        "gestalt-field-dynamics.pdf"),
    ("preverbal-manifold.pdf",            "preverbal-manifold.pdf"),
    ("swarm-propagator.pdf",              "swarm-propagator.pdf"),
    ("universal-somatic-field.pdf",       "universal-somatic-field.pdf"),
    ("lean-proofs-appendix.pdf",          "lean-proofs-appendix.pdf"),
    ("ttheory-cheatsheet.pdf",            "ttheory-cheatsheet.pdf"),
    # omnibus
    ("omnibus-a4.pdf",     "omnibus-a4.pdf"),
    ("omnibus-royal.pdf",  "omnibus-royal.pdf"),
]

# fractal-programme/bld/ → papers/
FRAC_FILES = [
    ("ttheory-omnibus.pdf",          "ttheory-omnibus.pdf"),
    ("ttheory-vol1.pdf",             "ttheory-vol1-foundation.pdf"),
    ("ttheory-vol2.pdf",             "ttheory-vol2-application.pdf"),
]

# nlm-min: just the two source files
NLM_MIN = [
    ("omnibus-a4.pdf",       "01-omnibus-v2.pdf"),
    ("ttheory-omnibus.pdf",  "02-ttheory-fractal-programme.pdf"),
]

# nlm-max: full corpus (source name in papers/, dest name in nlm-max/)
NLM_MAX_FROM_PAPERS = [
    ("omnibus-a4.pdf",                    "01-omnibus-v2.pdf"),
    ("ttheory-omnibus.pdf",               "02-fractal-programme.pdf"),
    ("ttheory-vol1-foundation.pdf",       "03-fractal-vol1-foundation.pdf"),
    ("ttheory-vol2-application.pdf",      "04-fractal-vol2-application.pdf"),
    ("lean-proofs-appendix.pdf",          "05-lean-proofs-appendix.pdf"),
    ("soma-field-paper.pdf",              "P01-soma-field.pdf"),
    ("quantum-soma-penrose.pdf",          "P02-quantum-penrose.pdf"),
    ("mathematical-co-identification.pdf","P03-mathematical-co-identification.pdf"),
    ("soma-field-synthesis.pdf",          "P04-synthesis.pdf"),
    ("soma-physical-substrate.pdf",       "P05-physical-substrate.pdf"),
    ("soma-field-book.pdf",               "P06-field-book.pdf"),
    ("soma-field-patient-pov.pdf",        "P07-patient-pov.pdf"),
    ("the-tensor.pdf",                    "P08-the-tensor.pdf"),
    ("music-affect-dynamics.pdf",         "P09-music-affect.pdf"),
    ("soma-temporal-dynamics.pdf",        "P10-temporal-dynamics.pdf"),
    ("zoomable-somatic-field.pdf",        "P11-zoomable-field.pdf"),
    ("experimental-validation.pdf",       "P12-experimental-validation.pdf"),
    ("missing-limbic-layer.pdf",          "P13-missing-limbic-layer.pdf"),
    ("P14-usf-euclidean-qft.pdf",         "P14-euclidean-qft.pdf"),
    ("P15-usf-interacting-qft.pdf",       "P15-interacting-qft.pdf"),
    ("geographic-somatic-field.pdf",      "P16-geographic-field.pdf"),
    ("gestalt-field-dynamics.pdf",        "P17-gestalt-dynamics.pdf"),
    ("preverbal-manifold.pdf",            "P18-preverbal-manifold.pdf"),
    ("swarm-propagator.pdf",              "P19-swarm-propagator.pdf"),
    ("universal-somatic-field.pdf",       "P20-universal-somatic-field.pdf"),
    ("ttheory-cheatsheet.pdf",            "cheatsheet.pdf"),
]

def sync_papers():
    print("── papers/ ──────────────────────────")
    for src_name, dst_name in PAPER_FILES:
        cp(PAPER / src_name, DIST / "papers" / dst_name)
    for src_name, dst_name in FRAC_FILES:
        cp(FRAC / src_name, DIST / "papers" / dst_name)

def sync_nlm():
    print("── nlm-min/ ─────────────────────────")
    for src_name, dst_name in NLM_MIN:
        # nlm-min sources are omnibus from PAPER and fractal from FRAC
        if src_name == "omnibus-a4.pdf":
            cp(PAPER / src_name, DIST / "nlm-min" / dst_name)
        else:
            cp(FRAC / src_name, DIST / "nlm-min" / dst_name)

    print("── nlm-max/ ─────────────────────────")
    for src_name, dst_name in NLM_MAX_FROM_PAPERS:
        cp(DIST / "papers" / src_name, DIST / "nlm-max" / dst_name)
    # PROMPTS.md
    cp(DIST / "PROMPTS.md", DIST / "nlm-max" / "PROMPTS.md")

def sync_lulu():
    print("── lulu/ ────────────────────────────")
    cp(PAPER / "omnibus-a4.pdf",      DIST / "lulu" / "01-omnibus-v2.pdf")
    cp(FRAC  / "ttheory-vol1.pdf",    DIST / "lulu" / "03-ttheory-vol1-foundation.pdf")
    cp(FRAC  / "ttheory-vol2.pdf",    DIST / "lulu" / "04-ttheory-vol2-application.pdf")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync built PDFs into Dist subdirs.")
    parser.add_argument("--papers", action="store_true", help="Sync papers/ only")
    parser.add_argument("--nlm",    action="store_true", help="Sync nlm-min/ and nlm-max/ only")
    parser.add_argument("--lulu",   action="store_true", help="Sync lulu/ only")
    args = parser.parse_args()

    if not any(vars(args).values()):
        sync_papers(); sync_nlm(); sync_lulu()
    else:
        if args.papers: sync_papers()
        if args.nlm:    sync_nlm()
        if args.lulu:   sync_lulu()

    print("\nDone. Run: git add -A && git commit -m 'dist: sync' && git push")
