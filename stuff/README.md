# [T]-Theory — Supplementary Materials

Printable and distributable artefacts. Not part of the formal academic record
(that lives in `zenodo/`) — these are the things you hand to someone, stick on
a wall, or use to print a cover.

---

## Files

### `ttheory-cheatsheet.pdf`
A one-page mathematical reference card for the Universal Somatic Field.
Contains the master field equation, retarded propagator, somatic memory kernel,
Hopfield energy function, Zoom Operator hierarchy, and the five OS axioms.

Dense enough to use as a working reference; compact enough to print double-sided
on a single A4 sheet. It also, apparently, looks exactly like a rave flyer —
which turned out to be useful, since the open items listed on it became the
Lean 4 proof obligations that closed the formal verification.

**Download:** [`ttheory-cheatsheet.pdf`](https://github.com/ITI-Theory/Dist/blob/main/stuff/ttheory-cheatsheet.pdf)
Source: [`U/paper/soma/ttheory-cheatsheet/ttheory-cheatsheet.md`](https://github.com/ITI-Theory/U/blob/main/paper/soma/ttheory-cheatsheet/ttheory-cheatsheet.md)
Rebuild: `cd U/paper && make cheatsheet`

---

### `t-theory-sticker.png`
The [T]-Theory sticker design. Suitable for printing as a die-cut sticker
(recommended: 90×90 mm on white vinyl, or 50 mm circle for laptop use).

**Download:** [`t-theory-sticker.png`](https://github.com/ITI-Theory/Dist/blob/main/stuff/t-theory-sticker.png)
Source: [`U/Part2/fractal-programme/t-theory-sticker.png`](https://github.com/ITI-Theory/U/blob/main/Part2/fractal-programme/t-theory-sticker.png)

---

### `lulu-cover-template/cover-omnibus-v2.tex`
XeLaTeX source for the Lulu hardcover dust jacket for Omnibus V2.
Black background, gold [T]-Theory decorative field lines, [T] watermark,
gold rules. Compile with `xelatex` against the Lulu cover spec
(spine width = f(page count, paper weight)).

**Browse:** [`lulu-cover-template/`](https://github.com/ITI-Theory/Dist/tree/main/stuff/lulu-cover-template)
Paired with: [`Dist/lulu/01-omnibus-v2.pdf`](https://github.com/ITI-Theory/Dist/blob/main/lulu/01-omnibus-v2.pdf)
