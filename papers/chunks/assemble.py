#!/usr/bin/env python3
"""
assemble.py — Reassemble translated chunks into omnibus-body-plus.{lang}.md

Usage:
    python assemble.py
"""
from pathlib import Path

here = Path(__file__).parent
out_dir = here.parent  # Dist/papers/

for lang in ("de", "it", "fr"):
    chunks = sorted(here.glob(f"chunk_??.{lang}.md"))
    if not chunks:
        print(f"[{lang}] no chunks found, skipping")
        continue
    out = out_dir / f"omnibus-body-plus.{lang}.md"
    text = "\n".join(c.read_text(encoding="utf-8") for c in chunks)
    out.write_text(text, encoding="utf-8")
    print(f"[{lang}] {len(chunks)} chunks -> {out.name}  ({len(text.split()):,} words)")
