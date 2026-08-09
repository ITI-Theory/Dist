# Zenodo — Full Release Runbook

## What's already published (do NOT re-upload)

| Record | DOI | Status |
|---|---|---|
| P1 soma-field-paper | https://doi.org/10.5281/zenodo.20350515 | ✅ published |
| P2 quantum-soma-penrose | https://doi.org/10.5281/zenodo.20351230 | ✅ published |
| P3 mathematical-co-identification | https://doi.org/10.5281/zenodo.20287981 | ✅ published |
| D1 SFT-DEMO-CASE | https://doi.org/10.5281/zenodo.20459825 | ✅ published |
| P4 soma-field-synthesis | https://doi.org/10.5281/zenodo.20460118 | ✅ published |
| P5 soma-physical-substrate | https://doi.org/10.5281/zenodo.20460357 | ✅ published |
| P6 soma-field-book | https://doi.org/10.5281/zenodo.20460455 | ✅ published |
| P7 soma-field-patient-pov | https://doi.org/10.5281/zenodo.20460523 | ✅ published |
| P8 the-tensor | https://doi.org/10.5281/zenodo.20460613 | ✅ published |
| P9 music-affect-dynamics | https://doi.org/10.5281/zenodo.20460685 | ✅ published |
| C1 omnibus (20 papers) | https://doi.org/10.5281/zenodo.20460771 | ✅ published |

**The thesis** (`omnibus-a4.pdf`) is the same 20 papers in thesis format. It does NOT need
its own Zenodo record — C1 already covers this content. Use `Dist/lulu/01-thesis-omnibus.pdf`
for printing only.

---

## PART 1 — Zenodo Account Setup (Do This First, Once)

Go to **https://zenodo.org** → sign in with your GitHub account (Alistair-Johnson).

### Settings to configure (takes 10 minutes):

**1. Link your ORCID**
- Account → Linked accounts → "Connect ORCID"
- Your ORCID: `0009-0007-2194-0850`
- This auto-populates your ORCID on every record — important for discoverability

**2. Profile / Contact email**
- Account → Profile → set your email (this is not public unless you choose)
- Zenodo uses it for notifications only; does not appear on records by default

**3. GitHub integration** (optional but nice)
- Account → Linked accounts → "Connect GitHub" — already done if you signed in via GitHub
- Not needed for manual uploads; useful for future automation

**4. Communities** (optional)
- Create an ITI-Theory community: https://zenodo.org/communities/new — name it `iti-theory`
- Add all existing records to it — one landing page for everything

---

## PART 2 — Upload Order

Go to **https://zenodo.org/uploads/new** for each. Do them in order:

| # | File in this directory | Record type |
|---|---|---|
| P10 | `P10-soma-temporal-dynamics.pdf` | Publication → Preprint |
| P11 | `P11-zoomable-somatic-field.pdf` | Publication → Preprint |
| P12 | `P12-experimental-validation.pdf` | Publication → Preprint |
| P13 | `P13-missing-limbic-layer.pdf` | Publication → Preprint |
| C2 | `C2-ttheory-fractal-omnibus.pdf` | Publication → Book |

For all records:
- **Access**: Open
- **Licence**: CC BY 4.0
- **Language**: English
- **Author**: Alistair Johnson · ORCID 0009-0007-2194-0850 · Independent Researcher · Zurich, Switzerland

---

## PART 3 — Exact Form Fields

### P10 — Temporal Dynamics

| Field | Value |
|---|---|
| File | `P10-soma-temporal-dynamics.pdf` |
| Resource type | Publication → Preprint |
| Title | Temporal Dynamics of the Universal Somatic Field: Retarded Propagators, Transition Rates, and the Memory of Feeling |
| Description | The Universal Somatic Field (USF) has been established as a scale-invariant field-theoretic architecture governing dynamics from quantum foam to the cosmic web. This paper completes the kinematic picture with the full time-dependent formulation: the retarded Green's function, the Somatic Memory Kernel K(τ) = K₀·exp(−τ/τ_m), and the Kramers mean first-passage time formula for emotional state transitions. Clinical implications include a field-theoretic derivation of why trauma formation is faster than trauma dissolution, a formal account of why somatic therapies are more efficient than cognitive therapies for complex PTSD, and a quantitative definition of the window of tolerance as a temporal bandwidth constraint on the retarded propagator. Therapeutic intervention is formulated as an optimal control problem on the field trajectory. |
| Keywords | temporal dynamics, retarded Green's function, somatic field theory, emotional transition rates, trauma, memory kernel, Kramers formula, WKB approximation, window of tolerance, therapeutic intervention |
| Related identifiers | `Is part of` → https://doi.org/10.5281/zenodo.20460771 |

---

### P11 — Zoomable Somatic Field

| Field | Value |
|---|---|
| File | `P11-zoomable-somatic-field.pdf` |
| Resource type | Publication → Preprint |
| Title | The Zoomable Universal Somatic Field: A Scale-Invariant Green's Function Architecture Unifying Quantum, Biological, and Cosmological Dynamics |
| Description | We present the Zoomable Universal Somatic Field (zUSF), a scale-invariant field-theoretic architecture in which a single structural equation — the Helmholtz Green's function — governs field propagation across twenty orders of magnitude, from quantum foam to the observable universe. The Zoom Operator Λ is formalised as a dependent type constructor instantiating the field equation at each of 20 scale levels. The Field-Modulated Hopfield Network (FM-HN) provides a falsifiable computational model in which the limbic field controls the inverse temperature β of an associative memory network at runtime; under zero somatic stress the FM-HN reduces exactly to the classical 1982 Hopfield network (Correspondence Principle, Lean 4 verified). Multi-agent coordination is shown to require O(N²) field interactions. The architecture encapsulates McFadden's CEMI theory, Schreiber's Modal HoTT, and Hoffman's Conscious Agents as special cases. |
| Keywords | scale invariance, Green's function, somatic field theory, M-theory, zoom operator, consciousness, Hopfield networks, Lean 4, HoTT, CEMI |
| Related identifiers | `Is part of` → https://doi.org/10.5281/zenodo.20460771 |

---

### P12 — Experimental Validation

| Field | Value |
|---|---|
| File | `P12-experimental-validation.pdf` |
| Resource type | Publication → Preprint |
| Title | Experimental Benchmarks for the Universal Somatic Field Framework |
| Description | Five experimental benchmarks moving the USF framework's claims from proved to demonstrated: (1) a four-model timed comparison of Hopfield 1982, 2016, 2020, and FM-HN USF 2026 on a fear-to-awe basin-crossing task; (2) MNIST corrupted character test showing classical networks settle into false attractors while FM-HN escapes via WKB tunnelling; (3) macroscopic synchronisation benchmarks (GHZ entanglement, Kuramoto order parameter) grounding the O(N²) coordination theorem; (4) God-Knob hysteresis test for second-order phase-transition asymmetry; (5) direct replication of the quantum annealing experiment (QUANT-EXP-1). All benchmarks implemented as Lean 4 #eval blocks in Benchmark.lean, cross-referenced against three kernel-verified theorems. |
| Keywords | Hopfield network, quantum tunnelling, MNIST, Kuramoto, GHZ entanglement, phase transition, formal verification, Lean 4, soma field, D-Wave |
| Related identifiers | `Is part of` → https://doi.org/10.5281/zenodo.20460771 |

---

### P13 — Missing Limbic Layer

| Field | Value |
|---|---|
| File | `P13-missing-limbic-layer.pdf` |
| Resource type | Publication → Preprint |
| Title | The Missing Limbic Layer: A Somatic Field Extension of Hopfield Networks via the Correspondence Principle |
| Description | We present the Field-Modulated Hopfield Network (FM-HN), a unified architecture in which the classical 1982 and modern 2020 Hopfield Networks emerge as two limiting cases of a single equation parameterised by an inverse temperature β controlled at runtime by the somatic electromagnetic field. The central result is a formal Correspondence Principle proof: under zero somatic stress, the FM-HN field equations collapse exactly to standard connectionist dynamics. Under non-zero somatic stress, the Limbic Electromagnetic Field (CEMI) modulates β and the weight matrix W in real time, enabling escape from local minima without stochastic resets. Three neurodivergent conditions (ADHD, Autism Spectrum Condition, and Complex PTSD) correspond to distinct dynamical regimes of the FM-HN, each characterised by a specific β profile and barrier geometry. Lean 4 type-checked. |
| Keywords | Hopfield network, limbic field, CEMI, somatic field, autism, ADHD, CPTSD, FM-HN, Correspondence Principle, Lean 4, neurodivergence |
| Related identifiers | `Is part of` → https://doi.org/10.5281/zenodo.20460771 |

---

### C2 — T-Theory Fractal Programme Omnibus

| Field | Value |
|---|---|
| File | `C2-ttheory-fractal-omnibus.pdf` |
| Resource type | Publication → Book |
| Title | [T]-Theory: The Complete Fractal Programme — Fifteen Domain Books on the Universal Somatic Field |
| Description | The [T]-Theory Fractal Programme is a collection of fifteen domain-specific books, each applying the Universal Somatic Field (USF) framework to a different academic discipline: mathematical physics, neuroscience, clinical psychology, computer science, formal mathematics, consciousness studies, complex systems, music and arts, geophysics, social science, economics, law, philosophy-politics-economics, and psychiatry/ASD. Each volume contains a domain-specific introduction (kappa), curated canonical USF papers, and a domain-specific conclusion and research agenda. This collected volume is a companion to the primary USF research canon (C1: https://doi.org/10.5281/zenodo.20460771). |
| Keywords | soma field theory, universal somatic field, fractal programme, consciousness, M-theory, Lean 4, trauma, geophysics, game theory, neuroscience, [T]-Theory |
| Related identifiers | `Is compiled from` → https://doi.org/10.5281/zenodo.20460771 |

---

## PART 4 — After Uploading

Record your DOIs here and then paste them back to Copilot to update the release sheets:

```
P10 temporal-dynamics:    https://doi.org/10.5281/zenodo._______
P11 zoomable-somatic:     https://doi.org/10.5281/zenodo._______
P12 experimental-val:     https://doi.org/10.5281/zenodo._______
P13 missing-limbic:       https://doi.org/10.5281/zenodo._______
C2  ttheory-omnibus:      https://doi.org/10.5281/zenodo._______
```

Then I will update:
- `paper/ZENODO_RELEASE_SHEETS.md`
- `T/.github/copilot-instructions.md`
- `U/.github/copilot-instructions.md`


Upload each file as a **separate record**. Do them in order P10 → P11 → P12 → P13 → C2.

For all records:
- **Access**: Open
- **Licence**: CC BY 4.0
- **Language**: English
- **Author**: Alistair Johnson · ORCID 0009-0007-2194-0850 · Independent Researcher · Zurich, Switzerland

---

## P10 — Temporal Dynamics
- **File**: `P10-soma-temporal-dynamics.pdf`
- **Type**: Publication → Preprint
- **Title**: Temporal Dynamics of the Universal Somatic Field: Retarded Propagators, Transition Rates, and the Memory of Feeling
- **Keywords**: temporal dynamics, retarded Green's function, somatic field theory, emotional transition rates, trauma, memory kernel, Kramers formula, WKB approximation, window of tolerance
- **Related**: `Is part of` → https://doi.org/10.5281/zenodo.20460771

---

## P11 — Zoomable Somatic Field
- **File**: `P11-zoomable-somatic-field.pdf`
- **Type**: Publication → Preprint
- **Title**: The Zoomable Universal Somatic Field: A Scale-Invariant Green's Function Architecture Unifying Quantum, Biological, and Cosmological Dynamics
- **Keywords**: scale invariance, Green's function, somatic field theory, M-theory, zoom operator, consciousness, Hopfield networks, Lean 4, HoTT, CEMI
- **Related**: `Is part of` → https://doi.org/10.5281/zenodo.20460771

---

## P12 — Experimental Validation
- **File**: `P12-experimental-validation.pdf`
- **Type**: Publication → Preprint
- **Title**: Experimental Benchmarks for the Universal Somatic Field Framework
- **Keywords**: Hopfield network, quantum tunnelling, MNIST, Kuramoto, GHZ entanglement, phase transition, formal verification, Lean 4, soma field, D-Wave
- **Related**: `Is part of` → https://doi.org/10.5281/zenodo.20460771

---

## P13 — Missing Limbic Layer
- **File**: `P13-missing-limbic-layer.pdf`
- **Type**: Publication → Preprint
- **Title**: The Missing Limbic Layer: A Somatic Field Extension of Hopfield Networks via the Correspondence Principle
- **Keywords**: Hopfield network, limbic field, CEMI, somatic field, autism, ADHD, CPTSD, FM-HN, Correspondence Principle, Lean 4, neurodivergence
- **Related**: `Is part of` → https://doi.org/10.5281/zenodo.20460771

---

## C2 — T-Theory Fractal Programme Omnibus
- **File**: `C2-ttheory-fractal-omnibus.pdf`
- **Type**: Publication → Book
- **Title**: [T]-Theory: The Complete Fractal Programme — Fifteen Domain Books on the Universal Somatic Field
- **Keywords**: soma field theory, universal somatic field, fractal programme, consciousness, M-theory, Lean 4, trauma, [T]-Theory
- **Description**: The [T]-Theory Fractal Programme applies the Universal Somatic Field framework to 15 academic domains. Each book contains a domain-specific introduction, curated canonical papers, and a research agenda. Companion to the primary canon (C1: https://doi.org/10.5281/zenodo.20460771).
- **Related**: `Is compiled from` → https://doi.org/10.5281/zenodo.20460771

---

## After uploading — record the DOIs here
```
P10 temporal-dynamics:    https://doi.org/10.5281/zenodo._______
P11 zoomable-somatic:     https://doi.org/10.5281/zenodo._______
P12 experimental-val:     https://doi.org/10.5281/zenodo._______
P13 missing-limbic:       https://doi.org/10.5281/zenodo._______
C2  ttheory-omnibus:      https://doi.org/10.5281/zenodo._______
```

Then update `paper/ZENODO_RELEASE_SHEETS.md` and `T/.github/copilot-instructions.md`
with the new DOIs.
