#!/usr/bin/env python3
"""
translate_chunks.py — Translate all chunk_NN.md files to DE, IT, FR using Anthropic API.

Usage:
    pip install anthropic
    set ANTHROPIC_API_KEY=sk-ant-...
    python translate_chunks.py

Output: chunk_NN.de.md, chunk_NN.it.md, chunk_NN.fr.md  (same directory)
Resume: already-translated files are skipped automatically.
"""
import os, sys
from pathlib import Path

MODEL = "claude-opus-4-7"
LANGS = [("de", "German"), ("it", "Italian"), ("fr", "French")]

SYSTEM = """\
You are a professional academic translator specialising in psychology, \
neuroscience, and somatic therapy. Translate the following English markdown text to {label}.

Rules:
1. Preserve ALL markdown formatting exactly: # headings, **bold**, *italic*, tables, \
bullet lists, numbered lists, YAML frontmatter (--- blocks).
2. In YAML frontmatter: translate title, description, abstract values. \
Set lang: to {lang_code}. Keep all other fields verbatim.
3. Keep these terms untranslated: Soma-Field, Hopfield network, biotensegrity, \
QUANT-EXP-1, all DOIs, all citations like [@key], all URLs.
4. Academic register throughout.
5. Return ONLY the translated text. No preamble, no explanations.\
"""

def main():
    try:
        import anthropic
    except ImportError:
        print("Run: pip install anthropic"); sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Set ANTHROPIC_API_KEY environment variable"); sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    here = Path(__file__).parent
    chunks = sorted(here.glob("chunk_??.md"))

    if not chunks:
        print("No chunk_NN.md files found."); sys.exit(1)

    print(f"Model: {MODEL}")
    print(f"Chunks: {len(chunks)}  x  {len(LANGS)} languages  =  {len(chunks)*len(LANGS)} calls\n")

    for lang_code, label in LANGS:
        print(f"=== {label} ===")
        for chunk_path in chunks:
            out = chunk_path.with_suffix(f".{lang_code}.md")
            if out.exists():
                print(f"  {chunk_path.name} -> {out.name}  (exists, skipped)")
                continue
            text = chunk_path.read_text(encoding="utf-8")
            print(f"  {chunk_path.name}  ({len(text.split()):,} words)...", end=" ", flush=True)
            msg = client.messages.create(
                model=MODEL,
                max_tokens=8192,
                temperature=0.2,
                system=SYSTEM.format(label=label, lang_code=lang_code),
                messages=[{"role": "user", "content": text}],
            )
            translated = msg.content[0].text
            out.write_text(translated, encoding="utf-8")
            print("ok")
        print()

    print("Done. Reassemble with: python assemble.py")

if __name__ == "__main__":
    main()
