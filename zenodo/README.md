# Zenodo — Release Runbook

This file is the paste-ready public text for the ITI-Theory Zenodo community
and its records. Keep wording evidence-labelled: formal checks, simulations,
model-derived comparisons, interpretations, and open hypotheses are different
claims.

---

## DOI policy

`PAPERS.yaml` stores the stable **concept DOI** in `doi`. It resolves to the
latest public version and is the DOI used in public links and citations. The
specific uploaded DOI is stored separately as `zenodo_version_doi` for release
audit history. Creating a new version changes only `zenodo_version_doi`; it
does not replace the concept DOI.

---

## Scripted uploads

Zenodo uploads are done with `U/bin/zenodo-publish` (run `plan` first; sandbox before live).

- Use Zenodo sandbox first.
- Dry-run is the default.
- Live tokens are read from `ZENODO_TOKEN`; sandbox tokens from
  `ZENODO_SANDBOX_TOKEN`.
- Tokens must stay in the environment and must never be committed.
- Per-record metadata lives in `zenodo/metadata.yaml`; this README mirrors the
  public wording for review and paste checks.

---

## Evidence wording rules

- QUANT-EXP-1 is an exact 8-qubit statevector simulation, not a hardware run.
- Lean checks named formal statements under their definitions and axioms; it
  does not establish the physical or clinical interpretation of those
  definitions.
- The current Lean surface includes 20 axioms in `FieldAxioms.lean` and seven
  real `sorry`s.
- M-theory language is motivation/model structure: use "modelled on" or
  "motivated by an 11-dimensional decomposition"; do not present the model as
  established high-energy physics.
- Cosmology numbers are model-derived comparisons with Planck 2018, not
  independent confirmation.
- Clinical and lived-experience material is case material, interpretation, and
  open hypothesis, not validated medical mechanism.
- The corpus is not peer reviewed.

---

## Zenodo community — check on each release

Community URL: https://zenodo.org/communities/iti-theory/settings

**Short description** (paste into Settings → Short description):

```
Universal Somatic Field and [T]-Theory research programme: 24 papers, datasets,
Lean 4 formal artefacts, simulations, and 15 domain books. Evidence-labelled
open research by Alistair Johnson · ORCID 0009-0007-2194-0850 · Zurich.
```

**About page** (paste into Settings → Pages → About):

```
[T]-Theory Research Programme — Universal Somatic Field

Research output of Alistair Johnson (ORCID 0009-0007-2194-0850), Independent
Researcher, Zurich, 2025–2026.

The Universal Somatic Field (USF) is a scale-invariant modelling framework for
emotional dynamics, formal propagators, and cross-domain analogies. Its field
language is motivated by an 11-dimensional decomposition and by Green-function
methods; clinical, physical, and consciousness claims are explicitly labelled
as formal checks, model-derived results, simulations, interpretations, or open
hypotheses.

The collection includes 24 papers (P1–P24), datasets and appendices (E1, D1,
D2), collected works, an exact 8-qubit statevector simulation (QUANT-EXP-1),
Lean 4 formal artefacts, and the [T]-Theory Fractal Programme of 15 domain
books. The Lean files check named statements under their definitions and
axioms; the current proof surface includes axioms and remaining sorries. The
work is public, citable, and falsifiable, but it is not peer reviewed and does
not provide medical advice.
```

---

## Pending Zenodo actions (2026-10-01)

All actions wait for the relevant UAT track and author approval. P21 needs
author review before first upload.

| Record | Action | Status | File |
|---|---|---|---|
| D1 `SFT-DEMO-CASE` | New version | hardened clinical case wording | `papers/SFT-DEMO-CASE.pdf` |
| D2 `lean-proofs-appendix` | New version | hardened proof-surface wording | `papers/lean-proofs-appendix.pdf` |
| P1 `soma-field-paper` | New version | hardened claims | `papers/soma-field-paper.pdf` |
| P2 `quantum-soma-penrose` | New version | simulation wording | `papers/quantum-soma-penrose.pdf` |
| P3 `mathematical-co-identification` | New version | method/evidence wording | `papers/mathematical-co-identification.pdf` |
| P4 `soma-field-synthesis` | New version | title and programme framing updated | `papers/soma-field-synthesis.pdf` |
| P5 `soma-physical-substrate` | New version | physical-substrate claims hardened | `papers/soma-physical-substrate.pdf` |
| P6 `soma-field-book` | New version | lived-experience claims hardened | `papers/soma-field-book.pdf` |
| P7 `soma-field-patient-pov` | New version | restored/hardened patient-perspective text | `papers/soma-field-patient-pov.pdf` |
| P8 `the-tensor` | New version | tensor/art claims hardened | `papers/the-tensor.pdf` |
| P9 `music-affect-dynamics` | New version | music-affect evidence wording | `papers/music-affect-dynamics.pdf` |
| P10 `soma-temporal-dynamics` | New version | temporal/path wording hardened | `papers/soma-temporal-dynamics.pdf` |
| P11 `zoomable-somatic-field` | New version | Planck/proof wording updated | `papers/zoomable-somatic-field.pdf` |
| P12 `experimental-validation` | New version | benchmark wording updated | `papers/experimental-validation.pdf` |
| P13 `missing-limbic-layer` | New version | neural/clinical wording hardened | `papers/missing-limbic-layer.pdf` |
| P14 `usf-euclidean-qft` | New version | OSforGFF/Lean scope clarified | `papers/P14-usf-euclidean-qft.pdf` |
| P15 `usf-interacting-qft` | New version | research-programme claims hardened | `papers/P15-usf-interacting-qft.pdf` |
| P16 `geographic-somatic-field` | New version | cross-domain claims hardened | `papers/geographic-somatic-field.pdf` |
| P17 `gestalt-field-dynamics` | New version | philosophical status hardened | `papers/gestalt-field-dynamics.pdf` |
| P18 `preverbal-manifold` | New version | case/diagnostic claims hardened | `papers/preverbal-manifold.pdf` |
| P19 `swarm-propagator` | New version | coordination claims hardened | `papers/swarm-propagator.pdf` |
| P20 `universal-somatic-field` | New version | scale/cosmology wording hardened | `papers/universal-somatic-field.pdf` |
| C1v2 `omnibus-v2` | New version | rebuilt paper omnibus, 427 pages | `zenodo/C1v2-omnibus.pdf` |
| C2 `ttheory-fractal-programme` | New version | rebuilt Fractal Thesis | `zenodo/C2-ttheory-fractal-programme.pdf` |
| P21 `cosmological-constant-derivation` | First upload after author review | pending-review | `papers/cosmological-constant-derivation.pdf` |
| P22 `dark-matter-spatial-vacuum` | First upload | pending-upload | `papers/dark-matter-spatial-vacuum.pdf` |
| P23 `ttheory-phenomena` | First upload | pending-upload | `papers/ttheory-phenomena.pdf` |
| P24 `g2-symmetry-breaking` | First upload | pending-upload | `papers/g2-symmetry-breaking.pdf` |
| C2-vol1 `ttheory-vol1` | First upload | pending-upload | `papers/ttheory-vol1.pdf` |
| C2-vol2 `ttheory-vol2` | First upload | pending-upload | `papers/ttheory-vol2.pdf` |
| C2-book-01 `ttheory-book-gateway` | First upload | pending-upload | `papers/book-gateway.pdf` |
| C2-book-02 `ttheory-book-physics` | First upload | pending-upload | `papers/book-physics.pdf` |
| C2-book-03 `ttheory-book-complex-systems` | First upload | pending-upload | `papers/book-complex-systems.pdf` |
| C2-book-04 `ttheory-book-formal-mathematics` | First upload | pending-upload | `papers/book-formal-mathematics.pdf` |
| C2-book-05 `ttheory-book-neuroscience` | First upload | pending-upload | `papers/book-neuroscience.pdf` |
| C2-book-06 `ttheory-book-consciousness` | First upload | pending-upload | `papers/book-consciousness.pdf` |
| C2-book-07 `ttheory-book-computer-science` | First upload | pending-upload | `papers/book-computer-science.pdf` |
| C2-book-08 `ttheory-book-music-arts` | First upload | pending-upload | `papers/book-music-arts.pdf` |
| C2-book-09 `ttheory-book-clinical-psychology` | First upload | pending-upload | `papers/book-clinical-psychology.pdf` |
| C2-book-10 `ttheory-book-psychiatry-asd` | First upload | pending-upload | `papers/book-psychiatry-asd.pdf` |
| C2-book-11 `ttheory-book-social-science` | First upload | pending-upload | `papers/book-social-science.pdf` |
| C2-book-12 `ttheory-book-geophysics` | First upload | pending-upload | `papers/book-geophysics.pdf` |
| C2-book-13 `ttheory-book-law` | First upload | pending-upload | `papers/book-law.pdf` |
| C2-book-14 `ttheory-book-ppe` | First upload | pending-upload | `papers/book-ppe.pdf` |
| C2-book-15 `ttheory-book-economics` | First upload | pending-upload | `papers/book-economics.pdf` |

---

## Common upload fields

All records unless overridden:

- Access: Open
- Licence: CC BY 4.0
- Language: English
- Creator: Alistair Johnson · ORCID 0009-0007-2194-0850 · Independent Researcher · Zurich, Switzerland
- Community: ITI-Theory

**Keywords tip:** paste the whole comma-separated string into the keywords box
and press Enter — Zenodo will split on commas automatically.

---

## Per-record metadata: papers and datasets

| ID | Title | Description | Keywords |
|---|---|---|---|
| P1 | The Soma-Field: A Wave-Based Model of Emotional Dynamics | Introduces the Soma-Field as a mathematical and computational model of emotional dynamics. Claims are presented as model definitions, hypotheses, and proposed tests rather than clinical facts. | soma field, emotional dynamics, Hopfield network, Green function, computational psychology, trauma model |
| P2 | Quantum Topology and Trauma: A Soma-Field Model of Limbic Gate Tunnelling | Presents a quantum-inspired barrier-crossing model and QUANT-EXP-1 as an exact 8-qubit statevector simulation of reachability in the model class. | quantum-inspired model, statevector simulation, trauma attractor, barrier crossing, Hopfield, somatic field |
| P3 | Mathematical Co-identification: A Formal Model of Therapeutic Attunement | Develops co-identification as a formal and philosophical method for mapping therapeutic attunement without treating it as clinical evidence. | co-identification, therapeutic attunement, methodology, formal model, philosophy of science |
| P4 | The Soma-Field Research Programme: Method, Model, and Computational Test | Current programme overview: method, mathematical model, simulation work, formal artefacts, and validation gaps. | soma field research programme, method, computational model, evidence labels, validation |
| P5 | The Physical Substrate of the Soma-Field | Reviews candidate psychophysiological and electromagnetic substrates as hypotheses to be tested. | psychophysiology, interoception, CEMI, electromagnetic field, somatic field, open hypothesis |
| P6 | A Voyage into Trauma: The Soma-Field as Lived Experience | Book-length lived-experience and interpretive treatment of trauma through the Soma-Field model. | trauma studies, autoethnography, lived experience, soma field, interpretation |
| P7 | Field Notes from the Inside: A Patient Perspective on the Soma-Field | Patient-perspective account and clinical case material, presented as testimony and hypothesis. | patient perspective, case material, trauma, lived experience, somatic field |
| P8 | The Tensor: Formal Structure of the Universal Somatic Field | Art-theory and tensor-formalism bridge for the Universal Somatic Field. | tensor, universal somatic field, art theory, mathematical aesthetics, field formalism |
| P9 | Music-Induced Affect Dynamics: A Soma-Field Model of the BRECVEMA Mechanisms | Models music-induced affect with BRECVEMA pathways and field-response language; replication remains pending. | music psychology, affect dynamics, BRECVEMA, entrainment, somatic field |
| P10 | Temporal Dynamics of the Universal Somatic Field: Retarded Propagators, Transition Rates, and the Memory of Feeling | Develops temporal propagators, transition-rate models, and memory kernels for the USF framework. | temporal dynamics, retarded Green function, memory kernel, transition rates, window of tolerance |
| P11 | The Zoomable Universal Somatic Field: A Scale-Invariant Green's Function Architecture | Presents the 20-scale zoom architecture as a scale-invariant modelling framework. | scale invariance, Green function, zoom operator, 20-scale hierarchy, somatic field |
| P12 | Experimental Benchmarks for the Universal Somatic Field Framework | Defines benchmark tasks and reports simulation status for the USF validation programme. | benchmarks, simulation, Hopfield network, Kuramoto, GHZ, phase transition, validation |
| P13 | The Missing Limbic Layer: A Somatic Field Extension of Hopfield Networks via the Correspondence Principle | Extends Hopfield networks with a limbic-field layer and correspondence-principle argument. | Hopfield network, limbic field, FM-HN, CEMI, neurodivergence, correspondence principle |
| P14 | The Universal Somatic Field as a Euclidean Quantum Field Theory: Osterwalder–Schrader Axiom Verification via Lean 4 | Applies OSforGFF formal results to a Gaussian free field presentation; the USF identification is a model step. Lean checks named statements under definitions and axioms. | Osterwalder-Schrader axioms, Gaussian free field, Lean 4, formal methods, Euclidean QFT |
| P15 | Osterwalder–Schrader Axioms for the Interacting Universal Somatic Field: Reflection Positivity under Hopfield Coupling | Research-programme paper for the interacting case; separates assumptions, partial formal structure, and open proof obligations. | interacting QFT, Hopfield coupling, reflection positivity, constructive QFT, research programme |
| P16 | The Geographic Somatic Field: Scale-Invariant Wave Propagation in Human Landscapes | Applies USF propagator language to human geography as a cross-domain modelling hypothesis. | geography, human landscapes, wave propagation, scale invariance, place, Green function |
| P17 | The Mathematical Foundations of Gestalt Field Dynamics: Formalising the Soma-Field via Russellian Neutral Monism | Connects Gestalt dynamics, neutral monism, and field modelling as a philosophical framework. | gestalt, neutral monism, perception, philosophy, soma field, formal model |
| P18 | The Pre-Verbal Manifold: A Soma-Field Case Study of Acquired Neurodevelopmental Phenotypes | N=1 case-study and modelling paper on acquired neurodevelopmental phenotypes; diagnostic claims remain hypotheses. | preverbal manifold, case study, neurodevelopment, ASD, ADHD, trauma, hypothesis |
| P19 | Single-Step Multi-Agent Coordination via Green's Function Propagators: A Macroscopic Brane Projection Framework | Models multi-agent coordination using Green-function propagators and states the formal assumptions behind the coordination result. | multi-agent systems, Green function, propagator, coordination, swarm robotics, brane model |
| P20 | The Universal Somatic Field: Green's Functions as Scale-Invariant Oscillators across Eleven Orders of Magnitude | Presents the USF as a scale-invariant oscillator framework across modelled physical and somatic scales. | universal somatic field, Green function, scale invariance, oscillators, dimensional model |
| P21 | The Cosmological Constant as the Vacuum Amplitude of the Universal Somatic Field: Λ ≡ ⟨tr Φ⟩₀ from USF Compactification | Pending author review. Compares a model-derived cosmological-constant value with Planck 2018 parameters under stated assumptions. | cosmological constant, Planck 2018, vacuum amplitude, compactification model, dark energy |
| P22 | Dark Matter as the Spatial Block Vacuum of 11-Dimensional M-Theory: Ω_DM = 3/11 from USF Spatial Sector | Proposes a spatial-sector model comparison for dark-matter density and reports discrepancy against Planck 2018 values under assumptions. | dark matter, Planck 2018, spatial sector, compactification model, Omega DM, cosmology |
| P23 | [T]-Theory as Fixed Point: The Universal Somatic Field Describes Its Own Propagation | Fixed-point and cultural-theory paper connecting USF propagation with the [T]-Theory programme. | fixed point, self-reference, Universal Somatic Field, [T]-Theory, cultural theory |
| P24 | G₂ Symmetry Breaking in the BRECVEMA Emotional Tensor: W8ℝ = ⁶⁄₅I₈ + δW and the 8→7 Dimensional Resolution | Algebraic model of G₂ symmetry breaking in the BRECVEMA tensor, with formal and interpretive claims separated. | G2 symmetry, BRECVEMA, emotional tensor, symmetry breaking, Lean 4, algebra |
| E1 | QUANT-EXP-1: Quantum Annealing Reachability Experiment on an 8-Mode Soma-Field Hamiltonian | Dataset/experiment artefact for the exact 8-qubit statevector simulation of model reachability. | statevector simulation, 8 qubits, Hamiltonian, reachability, quantum-inspired, dataset |
| D1 | SFT Applied: A Worked Clinical Example | Worked clinical-style example used to illustrate the model; not medical validation or treatment advice. | clinical example, case illustration, soma field, trauma, open hypothesis |
| D2 | Lean 4 Formal Proofs Appendix | Formal appendix documenting named Lean statements, dependencies, axioms, and proof-surface limitations. | Lean 4, formal methods, proof appendix, axioms, theorem proving |

---

## Per-record metadata: collections and volumes

| ID | Title | Description | Keywords |
|---|---|---|---|
| C1v2 | The Soma-Field: Collected Works — Second Edition | Rebuilt paper omnibus containing the current paper corpus and appendices; 427 pages in the current candidate. | collected works, soma field, Universal Somatic Field, papers, omnibus |
| C2 | [T]-Theory: The Complete Fractal Programme — Fifteen Domain Books on the Universal Somatic Field | Rebuilt Fractal Thesis collecting the 15 source-owned domain books; current candidate is 1,296 pages. | [T]-Theory, Fractal Programme, domain books, Universal Somatic Field, thesis |
| C2-vol1 | [T]-Theory Vol I: Foundation | Print volume for the foundation-side Fractal Programme; current candidate is 680 pages. | [T]-Theory, foundation, Fractal Programme, print volume |
| C2-vol2 | [T]-Theory Vol II: Application | Print volume for the application-side Fractal Programme; current candidate is 655 pages. | [T]-Theory, application, Fractal Programme, print volume |

---

## Per-record metadata: fifteen [T]-Theory books

| ID | Title | Subtitle | Description | Keywords |
|---|---|---|---|---|
| C2-book-01 | [T]-Theory: A Universal Field Theory of Mind, Body, and Cosmos | An Introduction to the Fractal Programme | Popular gateway to the programme and its evidence labels. | gateway, Universal Somatic Field, Fractal Programme, introduction |
| C2-book-02 | [T]-Theory: Physics | Field Equations of Mind | Physics-facing account of propagators, field equations, and model-derived comparisons. | physics, Green function, field equation, mind, model |
| C2-book-03 | [T]-Theory: Complex Systems | Scale-Free Dynamics | Complex-systems treatment of scale-free dynamics and cross-domain modelling. | complex systems, scale-free dynamics, criticality, networks |
| C2-book-04 | [T]-Theory: Mathematics | Dependent Types and the Geometry of Feeling | Mathematical and type-theoretic account of the formal surface. | mathematics, dependent types, Lean 4, geometry, formal methods |
| C2-book-05 | [T]-Theory: Neuroscience | The Electromagnetic Nervous System | Neuroscience-facing model of nervous-system field coupling, presented as testable hypothesis. | neuroscience, CEMI, nervous system, field model, hypothesis |
| C2-book-06 | [T]-Theory: Philosophy | Consciousness, Effect, and Proof in the Fractal Programme | Philosophy volume replacing the former consciousness title; treats consciousness claims as interpretive and open unless formally scoped. | philosophy, consciousness, effect, proof, Fractal Programme |
| C2-book-07 | [T]-Theory: Computing | Verified Emotional Computing | Computing account of formal artefacts, agent models, and affective-state propagation. | computing, agents, formal verification, emotional computing |
| C2-book-08 | [T]-Theory: Music and the Arts | The Physics of Music and Affect | Music/art account of affect dynamics, entrainment, and creative response. | music, arts, affect dynamics, entrainment, aesthetics |
| C2-book-09 | [T]-Theory: Trauma | Trauma as Topology | Clinical-psychology-facing account of trauma as model geometry and open clinical hypothesis. | trauma, topology, clinical psychology, attractor, hypothesis |
| C2-book-10 | [T]-Theory: Rewiring | Neurodivergence and Trauma | Psychiatry/neurodivergence volume with diagnostic and therapeutic claims kept hypothesis-labelled. | neurodivergence, trauma, psychiatry, ASD, ADHD |
| C2-book-11 | [T]-Theory: Society | The Physics of Society | Social-science model of coordination, contagion, and collective field dynamics. | society, social science, coordination, contagion, field model |
| C2-book-12 | [T]-Theory: Geophysics | The Geological Soma | Geophysics analogy and model framework for wave propagation in Earth systems. | geophysics, geological soma, seismic waves, analogy |
| C2-book-13 | [T]-Theory: Law | Topology of Justice | Legal-theory application of topology and field constraints as interpretive model. | law, justice, topology, legal theory, norms |
| C2-book-14 | [T]-Theory: PPE | Mind, Market, and Mandate | Philosophy, politics, and economics synthesis framed as open modelling. | PPE, politics, economics, mandate, social model |
| C2-book-15 | [T]-Theory: Economics | Economic Criticality | Economic-systems model using attractors, criticality, and equilibrium language. | economics, criticality, markets, attractor, equilibrium |

---

## After uploading

1. Record the concept DOI and version DOI in `PAPERS.yaml`.
2. Update `zenodo/metadata.yaml` if Zenodo normalises fields differently.
3. Update DOI mirrors in U, `.github`, and `.github-private`.
4. Re-run the Zenodo audit before closing the issue.
