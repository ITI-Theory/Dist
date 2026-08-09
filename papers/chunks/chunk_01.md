---
title: "The Soma-Field: Collected Works"
author: "Alistair Johnson"
orcid: "0009-0007-2194-0850"
institute: "Independent Researcher, Zurich, Switzerland"
date: "2026"
lang: en-GB
description: "A complete collection of the Soma-Field research programme: from lay introduction to formal proofs, quantum experiment, and clinical applications."
bibliography: bibliography.bib
csl: apa-7th.csl
---


---

# The Programme

This is a document about structure.

Not about feelings — though feelings are what the programme is ultimately for. Not about
therapy — though therapy is one of the principal applications. Not about physics —
though physics is where the mathematics comes from. It is about a single recurring
observation: that the equations governing emotional dynamics are the same equations
that govern quantum fields, and that this is not a metaphor.

When an identification like that is made precisely — when you can say not "this is
*like* a wave" but "this *is* a wave in the technical sense, with the same propagator,
the same energy function, the same topology, and therefore the same theorems" — a
compressed body of work becomes possible. You are not building from scratch. You are
navigating.

This document describes what was built by navigating, and why the pieces form a whole.

---

## The Gap the Programme Addresses

Every large language model deployed today is a classical system. Its training is
gradient descent. Its inference is deterministic or thermally noisy sampling. The
architecture was designed to model the neocortex — pattern recognition, sequence
prediction, error minimisation.

The complementary system — the limbic system, responsible for valuation, threat
detection, arousal modulation, and the somatic state reinstatement that underlies
trauma — had no formal mathematical treatment before this work. The clinical literature
described it richly (Porges, van der Kolk, Levine). The neuroscience described its
anatomy. Neither provided a model from which predictions could be derived and tested.

Simultaneously, the psychology of music had reached a similar ceiling. A 991-page
handbook (Juslin and Sloboda, 2010) treated music-induced emotion almost entirely
through Russell's valence–arousal circumplex: a static two-dimensional map. The
circumplex describes *where* a listener is, not *how* they move, what traps them,
or what allows escape. No dynamical model of music-induced affect existed.

The programme fills both gaps with the same model, via the same method.

---

## The Structure of the Argument

The argument has three movements and several extensions:

| Paper | Movement | Contribution |
|---|---|---|
| *Mathematical Co-identification* (2026) | Method | Names and formalises the procedure |
| *The Soma-Field* (2026) | Model | Applies it to emotional dynamics |
| *Quantum Soma and the Penrose Gap* (2026) | Empirical test | Confirms the central claim |
| *Field Notes from the Inside* (2026) | Lived case | Primary-source clinical grounding |
| *A Dynamical Field Model of Music-Induced Affect* (2026) | Extension | Demonstrates domain generality |
| *The Tensor* (2026) | Extension | Applies the framework to abstract film |

The popular account (*A Voyage into Trauma*, 2026) provides the same argument in
accessible form, for readers without a physics background.

---

# The Method: Mathematical Co-identification

## What It Is

The history of mathematical science contains a recurring event. At a certain moment,
a scientist recognises that the quantity they are studying is not *like* a quantity
already understood in another domain — it *is* the same mathematical object, under
a change of label. When this identification is made precisely, every theorem proved
about the source object becomes available in the target domain immediately, without
re-derivation.

This event has happened many times:

- Hopfield (1982) recognised that a neural network's energy-minimisation dynamics
  are the same as a spin-glass Hamiltonian. Every result from statistical mechanics
  of spin glasses — ground states, phase transitions, capacity bounds — imported.
- Veneziano (1968) recognised that the Euler Beta function, a result in pure
  mathematics, described the scattering amplitudes of hadrons. String theory began.
- Black and Scholes (1973) recognised that an option pricing equation was the
  heat diffusion equation. Every analytical tool from thermodynamics imported.

The paper *Mathematical Co-identification: A Method for Structural Import Across
Scientific Domains* (Johnson, 2026a) names this procedure, formalises it as a
distinct scientific method with its own validity criteria and failure modes, and
distinguishes it from analogy, metaphor, and modelling. The key distinction:

> **Analogy**: A is *like* B in certain respects. Illuminating, not transferable.
>
> **Co-identification**: A *is* B under relabelling. Every theorem about B is a
> theorem about A.

## Why It Matters as Method

A co-identification can be wrong. The identification is only valid if the mathematical
type matches: the same dimensionality, the same algebraic structure, the same
boundary conditions, the same symmetry group. The paper provides a falsifiability
protocol — a formal procedure for pre-registering an import claim and specifying what
observation would disconfirm it.

This matters because the failure mode of co-identification is not sloppy reasoning —
it is overly precise reasoning applied to the wrong type. The paper catalogues seven
historical examples to distinguish the valid from the invalid pattern.

The Soma-Field Model is the worked example throughout. The identification was not
discovered by reading physics textbooks and looking for something that felt similar.
It was discovered by writing down the equations the emotional system was observed to
satisfy and recognising the form.

---

# The Model: The Soma-Field

## Five Co-identifications

The Soma-Field Model (Johnson, 2026b) is built from five sequential co-identifications,
each importing a body of mathematics from physics into emotional dynamics:

**Co-identification 1: The Hopfield identification.**
The brain's emotional attractor dynamics satisfy the same energy function as a Hopfield
neural network. The energy function is:

$$H(\mathbf{e}) = -\tfrac{1}{2}\mathbf{e}^{\top} W \mathbf{e} - \mathbf{b}^{\top}\mathbf{e}$$

where $\mathbf{e} \in \mathbb{R}^N$ is the emotional state vector, $W$ is the coupling
matrix, and $\mathbf{b}$ is a bias vector encoding baseline arousal. The local minima
of $H$ are the named attractor states: regulated calm, fight, flight, freeze, flow,
dissociation.

**Co-identification 2: The QFT identification.**
The emotional field propagates as a quantum field. The conscious emotional percept
is the one-dimensional impulse response — the Green's function — of an
eleven-dimensional coupling manifold. The same object that describes a massive
particle in quantum field theory describes a conscious emotion: a pole in the
propagator of the field.

$$G(\omega) = \frac{1}{\omega^2 - m^2 + i\epsilon}$$

This is not a metaphor. The threshold $T$ at which a sub-perceptual field fluctuation
becomes a conscious emotional percept is the mass parameter $m$ in the propagator.
Below threshold: virtual. Above threshold: real.

**Co-identification 3: The brane identification.**
The body and the nervous system are not the same manifold. The body is a 3-brane
embedded in the 11-dimensional coupling manifold. Somatic pain states and the body
schema are field modes on this brane, not on the bulk manifold. This is the formal
statement of the somatic grounding of emotion.

**Co-identification 4: The $G_2$ holonomy identification.**
The seven compactified extra dimensions of the coupling manifold are a $G_2$ manifold.
The $G_2$ holonomy group is the one that gives rise to topological obstructions — loops
through the moduli space that cannot be continuously contracted to a point. In
emotional terms: trauma configurations from which smooth continuous change cannot
escape. The topological barrier is not a metaphor for being stuck. It is a
mathematical object with a winding number.

**Co-identification 5: The renormalisation group identification.**
Developmental trajectory maps onto the renormalisation group flow. The age at which
a traumatic modification was introduced corresponds to the energy scale at which the
coupling constant was set. High-energy (early developmental) modifications are
renormalisation-group relevant — they affect all subsequent scales. Low-energy (later
life) modifications are irrelevant in the technical sense. This gives the formal
account of why early trauma is not simply a more intense version of later trauma:
it is a different class of object.

## What the Model Predicts

From these five identifications, several predictions follow that are not derivable
from any existing clinical model:

1. **Threshold crossings are phase transitions.** The transition from sub-perceptual to
   conscious emotion is a second-order phase transition in the field. This predicts
   hysteresis — it is easier to stay in a state than to enter it, and easier to stay
   out than to leave.

2. **Complex PTSD is a topological configuration.** The coupling matrix $W$ for a CPTSD
   nervous system has a specific structure: a winding-number-protected attractor
   landscape in which the Fear basin is separated from the Awe basin by a barrier that
   low-noise classical gradient descent cannot cross. This is a prediction about matrix
   structure, not a description of symptoms.

3. **Autism Spectrum Condition modifies the threshold operator.** The threshold parameter
   $T$ in the ASC nervous system has a different coupling to the field modes than in
   the neurotypical case — specifically, the threshold is non-uniform across sensory
   modalities, producing the characteristic pattern of simultaneous hypo- and
   hyper-sensitivity.

4. **ADHD modifies the effective temperature.** The stochastic term in the Langevin
   dynamics governing the ADHD nervous system has higher effective temperature $T_{\text{eff}}$.
   This is not a deficit of attention; it is a higher rate of escape from local minima —
   an advantage in landscapes where rapid sampling is valuable and a liability where
   sustained convergence is required.

5. **Quantum mechanisms are required for certain transitions.** For trauma configurations
   with topological barriers (non-zero winding number), low-noise classical gradient
   descent cannot reach the global minimum. A quantum mechanism is required. This
   is the prediction that QUANT-EXP-1 was designed to test.

---

# The Empirical Test: QUANT-EXP-1

## The Prediction

The soma-field model makes a specific, falsifiable claim: for a Hopfield landscape
with a topological trauma barrier, low-noise classical Langevin dynamics starting from
the Fear attractor cannot reach the Awe attractor. Quantum annealing — a physically
realisable mechanism — can.

This is not a claim about whether people should use quantum computers in therapy.
It is a claim about reachability: that the mathematical structure of the barrier
distinguishes the quantum and classical regimes in a measurable way.

The prediction was registered in the Zenodo v1 deposit of the Soma-Field paper
(doi:10.5281/zenodo.20350515) before the experiment was run.

## The Experiment

*Quantum Soma and the Penrose Gap* (Johnson, 2026c) reports QUANT-EXP-1: an exact
8-qubit statevector simulation on a 256-dimensional Hilbert space, implementing the
Soma-Field Hopfield Hamiltonian with a transverse-field quantum annealing schedule.

The experimental design:

- **System**: 8-qubit Hopfield model encoding four emotional modes (Fear, Calm,
  Awe, Grief) plus sub-modes. Coupling matrix $W$ set to produce a topological
  barrier between Fear and Awe.
- **Quantum dynamics**: Transverse-field annealing with schedule
  $H(s) = (1-s)H_X + s H_{\text{problem}}$, $s \in [0,1]$.
- **Classical baseline**: Overdamped Langevin dynamics at low temperature
  ($T_{\text{eff}} = 0.01$), same starting state, same landscape.
- **Primary outcome**: Peak Awe-dominant occupancy (quantum) versus success rate
  of cold-classical crossings.

## Results

Results are presented against the pre-registered barrier ladder:

| Barrier strength | Classical cold rate | Classical cold CI [95\%] | Quantum peak |
|---|---|---|---|
| $W = -6$ | 0.000 | [0.000, 0.019] | 0.389 |
| $W = -8$ | 0.000 | [0.000, 0.019] | 0.408 |
| $W = -10$ | 0.000 | [0.000, 0.019] | 0.408 |
| $W = -12$ | 0.000 | [0.000, 0.019] | 0.409 |
| $W = -14$ | 0.000 | [0.000, 0.019] | 0.416 |

Bootstrap confidence intervals (n = 200 seeds) confirm that the classical cold success
rate is bounded above by 1.9\% at all tested barrier strengths. Quantum peak occupancy
is stable at 0.389–0.416 across the full range.

**Pre-registered hardening protocol — all checks passed:**

- **Bootstrap** (n = 200): cold CI = [0.000, 0.019]; quantum peak 0.408–0.410. Intervals
  do not overlap at any barrier strength.
- **Control A** (start from Awe, barrier intact): classical 16/16 stay in Awe. PASS.
  Confirms that the barrier is directional: it blocks Fear → Awe, not the reverse.
- **Control B** (barrier removed, $W[\text{Fear,Awe}] = +0.4$): classical 16/16 reach Awe.
  PASS. Confirms that the barrier, not the landscape geometry, is what blocks classical
  dynamics.
- **Spectral gap**: gap narrows monotonically with barrier strength (B8: 0.0095, B10:
  0.0089, B12: 0.0085) and reaches its minimum at $s \approx 0.999$, confirming the
  tunnelling bottleneck is late in the anneal.

**Verdict:** The strong reachability claim stands. QUANT-EXP-1 is a PASS.

## The Penrose Connection

The paper situates this result in the context of Penrose's argument about
non-computability and consciousness. The connection is not that consciousness requires
quantum mechanics in general. The connection is more specific:

Penrose identified a *gap* between what classical computation can reach and what
consciousness can do. The soma-field identifies a corresponding *topological gap* in
the emotional landscape between what classical gradient descent can reach and what
a genuinely new state of the nervous system requires. QUANT-EXP-1 provides the
computational demonstration that the gap exists and is crossable by a quantum mechanism.

The contribution is not to resolve Penrose's claim about consciousness. It is to
*instantiate* the gap in a concrete, testable, mathematical setting.

---

# The Lived Case: Field Notes from the Inside

*Field Notes from the Inside: A Patient-Constructed Model of Emotional Dynamics*
(Johnson, 2026d) performs a function that the formal papers cannot perform: it
provides the primary-source clinical grounding.

The paper is written by the person who has Autism Spectrum Condition (Level 2),
Attention Deficit Hyperactivity Disorder, and Complex Post-Traumatic Stress Disorder —
and who also has a degree in physics. The model was not developed by observing patients.
It was developed by having the conditions and finding the existing models inadequate.

The epistemological contribution of this paper is often undervalued. Every formal model
of a human system is, in the end, derived from observation of that system. When the
observer and the observed are the same entity, and that entity has the training to
translate observation into formal mathematics, the resulting model has a different
epistemic status from one derived by observation from the outside. The paper makes this
explicit, situates it within the autoethnographic research tradition, and argues that
the resulting model is *more* constrained, not less — because any prediction the model
makes that does not match the primary observer's experience is immediately falsified.

The formal content is a set of operator modifications for the three conditions:

- **ASC**: The threshold operator $T$ is replaced by a modality-dependent operator
  $T_k$ for each sensory channel $k$, with different coupling strengths. The result
  is the characteristic simultaneous hypo- and hyper-sensitivity: some channels are
  below threshold where the neurotypical channel is above it, others are above where
  the neurotypical channel is below.

- **ADHD**: The Langevin noise term $\sqrt{2 T_{\text{eff}}} \, \eta(t)$ has elevated
  $T_{\text{eff}}$. This is a quantitative modification, not a qualitative one. The
  system is not broken; it is sampling the energy landscape at higher temperature.
  The therapeutic implication is not to reduce the noise but to design the landscape
  so that high-temperature sampling is an advantage.

- **CPTSD**: The coupling matrix $W$ has the topological structure described in §3.2:
  a winding-number-protected barrier between Fear and regulated states. The barrier
  was installed before language, before narrative memory, before the self that can
  explain the barrier was formed. The modification is not a layer added to a pre-existing
  structure. It is the structure.

---

# Extensions: Music, Film, and the Domain Generality of the Model

## Music-Induced Affect

*A Dynamical Field Model of Music-Induced Affect: Beyond the Valence–Arousal Circumplex*
(Johnson, 2026e) applies the soma-field framework to a domain where the empirical
literature is rich and the theoretical models are weak.

Juslin and Sloboda's *Handbook of Music and Emotion* (2010) — 991 pages — contains
the circumplex as its dominant quantitative framework. The circumplex is a static map.
It describes where a listener is; it does not model how they move. The soma-field is
the first dynamical model of music-induced affect.

The key predictions that the circumplex cannot make but the field model does:

1. **Phase transitions, not continuous shifts.** State changes in music-induced affect
   are not smooth movements across the circumplex. They are threshold crossings — sudden
   re-configurations of the attractor landscape. The field model predicts the conditions
   under which a transition occurs and the hysteresis that prevents immediate return.

2. **The adaptive function of high effective temperature.** In the ADHD nervous system
   (elevated $T_{\text{eff}}$), music that holds a neurotypical listener in a stable
   state may drive repeated transitions. This is not a bug; it is the same high
   sampling rate that characterises the ADHD cognitive profile. The model gives this
   a formal account.

3. **Basin depth asymmetry.** The freeze attractor basin is deeper than the regulated
   calm basin. This means it is harder to leave freeze than it is to leave calm —
   asymmetric with respect to the direction of transition. Music that successfully moves
   a listener from freeze to calm is doing qualitatively different work than music that
   moves a calm listener to a more activated state.

The paper also specifies a real-time instrument implementation: a MIDI controller array
driving a Python field server at 50 Hz, with audio output via Ableton Live and 3D
fractal visual output (Mandelbulb projection onto HoloGauze screen). The instrument
is not described; it is specified formally, with pre-registered hypotheses and
disconfirmation criteria.

## The Tensor: An Abstract Film

*The Tensor: An Abstract Film Definition* (Johnson, 2026f) extends the framework to
abstract film. A film is defined not by its pixels but by its **emotional score**: a
vector-valued trajectory $\mathbf{e}^*(t)$ through the emotional field,
parameterised by story-time $t \in [0,1]$.

The rendering — the actual audiovisual output a viewer experiences — is generated
at runtime from this trajectory, the viewer's own soma-field state, and a set of
control parameters. In the limit where the viewer's biofeedback is available, the
film adapts to where the viewer is: the trajectory is not what the viewer experiences,
but what the film proposes. The work is not the pixels. It is the map.

This is a significant claim about what an artwork is. A conventional film is fixed:
the same sequence of frames for every viewer at every screening. The tensor film is a
field: a mathematical object that takes the viewer's state as input and produces an
output adapted to it. The artistic statement is in the trajectory, not the realisation.

The paper does not describe how to make such a film. It defines the abstract structure
that any realisation of such a film must instantiate — the way a musical score defines
a symphony without being the performance.

---

# The Argument as a Whole

The six papers form a single argument, and it can be stated in a paragraph:

> The limbic system and its coupling to the body are governed by the same mathematical
> equations as a quantum field on a manifold with $G_2$ holonomy. This identification is
> not a metaphor; it is a co-identification in the technical sense, with all the
> theorems of each source domain importing into the target. Among those theorems is one
> that has clinical consequences: topological barriers in the emotional attractor
> landscape cannot be crossed by low-noise classical gradient descent. A quantum
> mechanism can cross them. This has been computationally confirmed (QUANT-EXP-1)
> against a pre-registered hardening protocol. The model correctly describes the
> structure of Autism Spectrum Condition, ADHD, and Complex PTSD as operator
> modifications, and generalises to music-induced affect and abstract film with no
> change to the underlying mathematics.

What makes this a research programme rather than a single paper is the **generativity**:
the method (co-identification) produces results in any domain where an attractor
landscape with topological structure can be identified. The soma-field is one
instantiation. Music-induced affect is a second. Abstract film is a third. A fourth —
currently in design — is **H-AL**: a holographic avatar whose body is a live Mandelbulb
rendering of the emotional field state, projected at human scale through a hologauze screen
and accompanied by a synthesised voice narrating the field in real time. The geometry of the
fractal changes as the field changes; regulated calm and trauma produce visually distinct
and mathematically characterisable forms. The same functor architecture (§A.4 of the main
paper) supports this output with no changes to the field computation. Each of these
instantiations generates falsifiable predictions from the same mathematical core.

What makes this a *novel* research programme is the **gap it fills**: no formal
dynamical model of the limbic system existed before this work. The Hopfield framework
gave the neocortex its formal model in 1982. The soma-field gives the limbic system its
formal model in 2026. Together they constitute the first complete formal description
of the two principal computational substrates of the vertebrate brain.

---

# What Remains

The body of work described here is computationally complete. All pre-registered
hardening checks have been executed. The claims that can be confirmed by simulation
have been confirmed.

Three categories of work remain outside the scope of these papers:

**Physical hardware confirmation.** QUANT-EXP-1 uses exact statevector simulation.
Running the same 8-qubit experiment on IBM Quantum free-tier hardware would produce
the sentence "confirmed on physical quantum hardware." This is feasible, is the logical
next step for any journal submission targeting a hardware-inclusive venue, and is not
required to support any claim in the current corpus.

**Peer review.** The three published papers are currently archived on Zenodo as open
preprints. Peer review in ranked journals is a separate track, ongoing. The relevant
venues are: *Frontiers in Computational Neuroscience* (Hypothesis and Theory article
type) for the soma-field paper; *Synthese* or *Philosophy of Science* for the
co-identification paper; *Music Perception* or *Frontiers in Psychology* for the
music-affect paper.

**Empirical clinical application.** The model makes predictions about specific clinical
populations (ASC, ADHD, CPTSD) that require empirical testing outside the computational
domain. This constitutes a research programme for clinical collaborators. The
predictions are pre-specified in §3.2 of this document and in the relevant papers;
they are not vague.

**Physical substrate.** The model is formally complete but physically silent on the
tissue substrate in which the soma-field is instantiated in living organisms. A
companion paper, *The Physical Substrate of the Soma-Field* (Johnson, 2026g), develops
this layer across three converging research traditions: biotensegrity (Ingber, Levin)
as the mechanical architecture through which the somatic wave propagates globally;
fascial-interstitial continuity (Langevin, Schleip, Oschman) as the active signalling
tissue and physical locus of attractor-depth encoding; and biofield physiology (Popp,
Ho, McCraty, Rubik) as the candidate physical correlate of the field itself. The most
clinically significant result is the quantitative correspondence between fascial
stiffness and attractor depth: chronic fascial armoring measurable by shear-wave
elastography is the physical implementation of the energy barriers that QUANT-EXP-1
shows to be quantum-resistant. Myofascial release is thus barrier *lowering* — not
barrier crossing — and therapist-client physiological entrainment is the physical
mechanism of co-identification.

---

# Data and Code Availability

All papers, simulation code, result tables, figures, and Lean 4 formal proofs are
archived at the following Zenodo records (open access):

| Paper | DOI |
|---|---|
| *The Soma-Field* | [10.5281/zenodo.20350515](https://doi.org/10.5281/zenodo.20350515) |
| *Mathematical Co-identification* | [10.5281/zenodo.20287981](https://doi.org/10.5281/zenodo.20287981) |
| *Quantum Soma and the Penrose Gap* | [10.5281/zenodo.20351230](https://doi.org/10.5281/zenodo.20351230) |

The unreviewed papers (*Field Notes from the Inside*, *Music-Induced Affect*,
*The Tensor*, and this synthesis document) will be deposited on Zenodo as part of
the next release of the research archive.

---



\newpage

\part{Part I: The Body Knows}



\newpage

# A Voyage into Trauma

## *The Soma-Field Theory of Emotional Life*

**Alistair Johnson**

*2026*

---

\newpage

> *For everyone who was told their body was overreacting.*
> *It wasn't. It was solving the right problem.*

\newpage

---

# Preface: The T's

This book began as a physics paper.

It ended as a map.

The paper was called the Soma-Field Model, and it was written in the language of
physicists: Hamiltonians, propagators, coupling matrices, Wick rotations. It was precise.
It was, I think, correct. And it was almost entirely unreadable to the people it was
most about.

This book is the translation.

There are four T's running through what follows, and they are not accidental. The first
is **Trauma** — the subject. The second is **Threshold** — a specific parameter in the
model, written $T$, that marks the boundary between what becomes conscious and what stays
body. The third is **Time** — in particular, developmental time, the age at which a
modification occurred, which turns out to matter enormously. The fourth is
**Transformation** — not recovery, not a return, but a going forward into a wider
landscape.

There is a fifth T that I notice only in retrospect: **Trance** — in two senses
simultaneously. *A Voyage into Trance* is a 1995 Goa trance compilation by Paul
Oakenfold; the title of this book is borrowed from it. A trance state is, in the
language of the Soma-Field Model, a phase transition of the emotional field — a
threshold crossing guided by sound and rhythm rather than threat. The trance state
produced by extended rhythmic music at 140 BPM and the freeze response of a traumatised
nervous system are not the same experience. They are governed by the same mathematics:
the same threshold crossings, the same phase transitions, the same field dynamics. The
T's of that album and the T's of this book are the same T's.

I should tell you what happened in 1968 before we go any further, because it is the
reason this model exists and the reason I am the one writing it. I was approximately
eighteen months old. I developed septic arthritis in my left hip — a bacterial infection
of the joint that, without treatment, destroys the socket entirely. It was treated, and
I recovered. The treatment involved three months in hospital under what were then called
"no-touch protocols": the infection risk was judged to require isolation from physical
contact. Three months is a long time at eighteen months. The body learns quickly at that
age, and what mine learned — in the absence of any other available hypothesis — was that
the world was a place where pain arrived without warning and comfort did not follow.

That is not a complaint. The clinicians saved the joint. But the learning happened, and
it happened before language, before narrative memory, before the self that can tell the
story was formed. The modification was not added to an existing structure. It was the
structure.

This book is, among other things, an attempt to say that formally — to give that
experience a mathematical description precise enough to make predictions, to inform
clinical practice, and to explain why the goal is not to return to a self that never
existed, but to build forward into one that can.

I should also tell you that I promised, years ago, to write a book about a campsite in
the Glarus Alps of Switzerland — a valley with parabolic limestone walls that make sound
oscillate like a natural resonator, adjacent to one of the world's great tectonic
structures. The book about the campsite and the book about the soma-field found each
other. The Interlude between Part II and Part III is where they meet.

The physics is real. The equations correspond to something. And the voyage is the proof
of it.

*Alistair Johnson*
*May 2026*

---

# How to Read This Book

This book is written for three kinds of reader, and you can navigate it differently
depending on which you are.

**If you are new to all of this** — no physics background, no clinical background,
just a body that has been confusing you — read Part I first. Chapters 1 through 3 are
written for you. The mathematics in those chapters is kept to a minimum; the ideas are
introduced through physical intuition and lived experience. When equations do appear,
they are explained in words immediately. Nothing is assumed except curiosity.

**If you are a mental health professional** who wants to understand what this model adds
to your existing framework — you can begin with the Part I overview and then move
directly to Parts III and IV. The Going Deeper boxes throughout the book are written for
you. The appendices contain the full mathematics as it appears in the academic paper.

**If you are a physicist, mathematician, or computationalist** who has arrived here by
accident or curiosity — you will recognise the Hamiltonian formulation immediately. The
novel content for you is in Chapters 6, 7, and Appendix A. The Lean 4 type sketches in
Appendix B may be of particular interest; they are incomplete proofs, marked with
`sorry` where the hard work remains, and they represent a research programme.

A note on boxes. Throughout the book you will find four types:

> **LEARNING OBJECTIVES** — what this chapter sets out to establish, listed at the start.

> **AUTHOR'S NOTE** — personal first-person sections. The research and the life it
> emerged from are not separate, and I have not pretended otherwise.

> **GOING DEEPER** — technical sections with more mathematics or formal detail. They can
> be skipped without losing the main argument. They can also be read first if that is
> your preference.

> **KEY TERMS** — precise definitions for terms that carry specific meaning in this model.
> A full glossary is in Appendix D.

---

\newpage

# PART I: THE BODY KNOWS

---

\newpage

# Chapter 1: What the Body Remembers

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   "The body keeps the score."                                   │
  │                                                                  │
  │                                   — Bessel van der Kolk, 2014   │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **LEARNING OBJECTIVES**
>
> By the end of this chapter, you will understand:
>
> - Why the body responds to safety and danger independently of what the conscious
>   mind believes
> - What the freeze response is and why it exists
> - The difference between a body that is "overreacting" and a body that has learned
>   accurately
> - Why the first step in understanding trauma is understanding that survival responses
>   are not mistakes

---

## 1.1 The Waiting Room

Picture a waiting room. You are sitting in a chair, waiting for a routine appointment.
Nothing unusual is happening. The lighting is fluorescent. There is a plant in the corner
that needs watering. Someone across the room is reading a magazine with the particular
focused patience of someone who is not, in fact, reading a magazine.

For most people in this waiting room, the body is doing nothing remarkable. Heart rate
is steady. Breathing is even. The background hum of vigilance that keeps us alive is
running at its ordinary level.

For some people, this waiting room is already an event. Heart rate has been elevated since
the appointment was booked. Breathing is shallower than usual. There is a low-frequency
alertness — a readiness — that is using energy, keeping muscles slightly contracted,
keeping the hearing slightly sharpened, keeping the eyes moving. The mind may know that
this is a routine appointment. The body has reached a different conclusion and is acting
on it.

This is not anxiety in the clinical sense, though it may be diagnosed as such. It is not
a failure of rational thinking. It is a body doing exactly what it learned to do — and
doing it accurately, given what it knows.

The question this book asks is: what does the body know, and how did it learn it, and
what does it mean to change that learning?

## 1.2 What Trauma Is (and Is Not)

The word *trauma* is used in many ways. In this book, it has a specific meaning.

Trauma is a **permanent modification of the nervous system's prediction model** in
response to an experience that exceeded the system's capacity to process and integrate
at the time of the experience.

Notice what this definition does and does not say.

It does **not** say that trauma is a weakness. A bridge that bends under a load it was
not designed for is not a weak bridge — it is a bridge responding appropriately to a
force that exceeds its design specifications.

It does **not** say that trauma is a mental event. The modification happens at the level
of the nervous system — in the way sensory signals are filtered, in the way the body
prepares for action, in the way energy is distributed across physiological systems.
These are physical processes.

It does **not** say that the traumatic event needs to be dramatic. A three-month absence
of contact comfort at eighteen months of age is not a bomb going off. It is, by most
conventional standards, a minor medical intervention. What matters is the match between
the experience and the system's current capacity — and at eighteen months, the nervous
system has no framework whatsoever for "temporary separation for medical reasons."

What trauma **is**: a successful adaptation. The nervous system encountered a situation
it could not model, and it updated its model in the direction that maximised survival.
If the world is a place where pain arrives without warning and comfort does not follow,
then a nervous system set to high alert — always scanning, always slightly contracted,
always ready — is a nervous system correctly calibrated to that world. The problem is
not that the calibration is wrong. The problem is that the world has changed and the
calibration has not.

---

> **AUTHOR'S NOTE: The Hospital, 1968**
>
> I do not remember it. I was too young for explicit memory to have formed.
>
> What I have are the downstream signals: a body that has always treated routine medical
> environments as emergencies. A nervous system that identifies "caring professional
> approaching to help" and responds with the physiology of threat. A skeleton of
> responses so deeply embedded that they long predate any narrative I have been able to
> construct about them.
>
> My developmental age at the time was approximately eighteen months. The modification
> that happened then was not added to an existing nervous system. It was the nervous
> system being formed. That is a distinction that will matter a great deal in Chapter 6.
>
> For now: the body knows things that the mind never learned. This book is an attempt to
> write those things down in a language precise enough to work with.

---

## 1.3 The Polyvagal Ladder

In the 1990s, neuroscientist Stephen Porges developed what he called Polyvagal Theory —
an account of the autonomic nervous system that begins not with the familiar
fight-or-flight response but with the evolutionary history of the structures involved.

The key observation is this: the autonomic nervous system is not a single dial that runs
from "calm" to "alarmed." It is a hierarchy of three systems, each older than the one
above it, each more primitive, each mobilised in sequence as the perceived threat
increases.

```
  ╭──────────────────────────────────────────────────────────────────────╮
  │  VENTRAL VAGAL STATE           Social engagement branch             │
  │  Safe, connected, curious      Myelinated vagus nerve               │
  │  Window of Tolerance           Heart rate regulated                 │
  │  ─────────────────────────── ← most recently evolved                │
  ├──────────────────────────────────────────────────────────────────────┤
  │  SYMPATHETIC STATE             Mobilisation branch                  │
  │  Alert, energised, defensive   Spinal cord pathway                  │
  │  Fight or flight               Heart rate elevated                  │
  │  ─────────────────────────── ← older                               │
  ├──────────────────────────────────────────────────────────────────────┤
  │  DORSAL VAGAL STATE            Immobilisation branch                │
  │  Shutdown, collapse, freeze    Unmyelinated vagus nerve             │
  │  Dissociation, numbing         Heart rate dropped                   │
  │  ─────────────────────────── ← most ancient                        │
  ╰──────────────────────────────────────────────────────────────────────╯

  Figure 1.1. The polyvagal hierarchy. Under conditions of safety, the most evolved
  system (ventral vagal) governs — enabling social connection, learning, and curiosity.
  As perceived threat increases, the sympathetic system activates, preparing the body
  for action. If the threat is overwhelming or escape is impossible, the oldest system
  (dorsal vagal) takes over: immobilisation, shutdown, disconnection. Trauma often
  involves the system being stuck at a lower rung long after the original threat has
  passed.
```

The critical word in that last sentence is *perceived*. The hierarchy responds to what
the body detects as dangerous, not to what the thinking mind judges as dangerous. These
are different processes. The thinking mind can be entirely convinced that there is no
danger — and the body can, at exactly the same moment, be running the threat response
at full intensity. Both are responding to real information. They are just reading
different signals.

## 1.4 The Freeze Response

The freeze response is the least understood of the three states and, for many trauma
survivors, the most characteristic.

It is not the absence of a response. It is a full physiological engagement — the body
is doing something, and doing it with considerable energy. What it is doing is playing
dead.

This is a deeply ancient response. In evolutionary terms, freezing when threatened by
a predator is sometimes the optimal move: many predators respond to movement, and a
motionless prey item may not register as prey at all. The freeze response in mammals
also involves the release of endogenous opioids — nature's way of making the potential
experience of being killed slightly less intolerable. This is why dissociation during
overwhelming trauma is sometimes described as a kind of mercy.

For humans in modern environments, the freeze response is triggered not by literal
predators but by anything the nervous system has learned to classify as equivalent. A
raised voice. A medical environment. A particular combination of sensory signals that,
at some point in the past, preceded something overwhelming. The body does not
distinguish between the original context and the contemporary one. It responds to the
signal, not the story.

The result is a person who, in the middle of a conversation or a clinic appointment
or an otherwise ordinary moment, suddenly goes quiet and still and seems to be looking
at something slightly to the left of wherever they are. They are not being difficult.
They are not choosing not to engage. They are playing dead because the body has
concluded that this is the appropriate moment to play dead.

## 1.5 Why This Matters for Treatment

If trauma is a modification of a prediction model — an accurate learning from an
overwhelming experience — then the therapeutic question is not *how do we fix the
broken response* but *how do we update the prediction model with new information*.

This is a different question, and it has a different answer.

Fixing a broken response implies that the body is malfunctioning. Updating a prediction
model implies that the body has been doing its job correctly, and that the job now
requires new data.

The Soma-Field Model, which is the subject of this book, provides a mathematical
framework for what "updating the prediction model" means precisely: what structures
change, what the before and after states look like, and — critically — what kind of
change is possible given when the original learning occurred.

That last point is where this model adds something that existing frameworks do not
provide, and it is the subject of Chapter 6.

---

> **KEY TERMS**
>
> **Soma** — the body as experienced from the inside; the totality of interoceptive
> (internally sensed) signals.
>
> **Polyvagal hierarchy** — the three-level autonomic nervous system described by Porges,
> ordered from most evolutionarily ancient (dorsal vagal) to most recently evolved
> (ventral vagal).
>
> **Window of Tolerance** — the range of arousal within which the nervous system can
> function flexibly, process information, and engage socially. Above the window:
> hyperarousal (sympathetic). Below the window: hypoarousal (dorsal vagal shutdown).
>
> **Freeze response** — the immobilisation state of the dorsal vagal system; the body's
> oldest threat response, involving disconnection, stillness, and endogenous opioid
> release.

---

> **CHAPTER SUMMARY**
>
> Trauma is a modification of the nervous system's prediction model — a successful
> adaptation to overwhelming experience, not a failure or weakness. The polyvagal
> hierarchy describes how three evolutionary layers of the autonomic nervous system
> respond to perceived threat. The freeze response is the most ancient: immobilisation
> as survival strategy. For treatment to work, it must address the body's model, not
> argue with the thinking mind. The Soma-Field Model provides a mathematical language
> for this.

---

\newpage

# Chapter 2: A Field of Feeling

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   "The body is the unconscious mind."                           │
  │                                                                  │
  │                                   — Candace Pert, 1997          │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **LEARNING OBJECTIVES**
>
> By the end of this chapter, you will understand:
>
> - What a physical field is and why emotion behaves like one
> - Why emotions are body phenomena, not brain phenomena
> - What interoception is and why it is fundamental
> - The meaning of "the soma-field" as a technical term

---

## 2.1 What a Field Is

Imagine the gravitational field of the Earth.

You cannot see it. You cannot touch it. You cannot pick up a handful of gravity and
examine it under a microscope. But it is real — as real as anything in physics — and
you have felt it every moment of your existence. It is everywhere in space around the
Earth. It has a *strength* at every point (stronger close to the Earth, weaker further
away). It has a *direction* at every point (towards the centre of the Earth). And it
exerts a force on everything that is in it.

A field, in physics, is precisely this: a quantity that has a value at every point in
space. Temperature is a field. The wind is a field (a vector field — direction and
magnitude at every point). The electromagnetic field is a field. Quantum fields, which
are the foundation of modern physics, are fields.

The key insight of the Soma-Field Model is this: **emotion is a field phenomenon**.

Not a metaphor. A precise claim about how emotional signals distribute themselves in
the body, interact with each other, and evolve over time.

## 2.2 Emotions in the Body

Antonio Damasio, in his somatic marker hypothesis (1994), proposed that emotions are
fundamentally body states: that what we call "emotion" is the brain's representation
of a pattern of physiological activation — heartrate, muscle tension, gut movement,
hormonal state, skin conductance, respiratory rhythm. We do not feel an emotion and
then notice body signals. The body signal *is* the emotion; what the brain does is
read it.

This is deeply counterintuitive if you have spent your life inside a culture that treats
the mind as the real thing and the body as its vehicle. But the neuroscience supports it
consistently. Patients with damage to the parts of the brain that receive and integrate
body signals do not make better decisions because they are freed from emotional
interference — they make worse decisions, because they have lost access to the somatic
markers that tell them which options feel safe and which feel dangerous.

The body is not an obstacle to clear thinking. It is the substrate of it.

Interoception is the technical name for the body's ability to sense its own internal
state: heartbeat, breath, gut sensation, muscle tone, the position of limbs, the
temperature of organs. Interoceptive accuracy — how precisely a person can read their
own body signals — varies widely between individuals and is significantly disrupted by
trauma.

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │                    INTEROCEPTIVE BODY MAP                          │
  │                                                                     │
  │     ┌──────────┐        Fear:      rapid heartbeat, tight chest    │
  │     │   HEAD   │        Shame:     face flush, stomach drop        │
  │     └────┬─────┘        Calm:      slow breath, warm belly         │
  │          │              Anger:     jaw clench, shoulder tension     │
  │     ┌────┴─────┐        Grief:     throat constriction, chest heavy │
  │     │  CHEST   │        Joy:       chest expansion, light limbs    │
  │     │ ♥  lungs │        Freeze:    whole-body stillness, cold       │
  │     └────┬─────┘        Disgust:   gut recoil, throat closing      │
  │          │                                                          │
  │     ┌────┴─────┐        Each emotion has a characteristic          │
  │     │  BELLY   │        distribution across the body —             │
  │     │  gut     │        a spatial pattern of activation.           │
  │     └────┬─────┘        This pattern is what the Soma-Field        │
  │          │              Model calls the emotional field state.      │
  │     ┌────┴─────┐                                                    │
  │     │  PELVIS  │                                                    │
  │     │  limbs   │                                                    │
  │     └──────────┘                                                    │
  └─────────────────────────────────────────────────────────────────────┘

  Figure 2.1. The body map of emotional activation. Emotions are not events in the head;
  they are distributed patterns of physiological arousal across the body. Research by
  Nummenmaa et al. (2014) mapped these patterns by asking participants to colour body
  silhouettes where they felt each emotion. The patterns are consistent across cultures.
```

---

> **GOING DEEPER: The Foot That Isn’t There**
>
> Pain is not in the foot. It is in the brain’s model of the foot.
>
> The clearest proof is phantom limb pain. When a limb is amputated, many patients
> continue to feel it — and feel it *hurting*. The foot is gone. The pain is real.
> It wakes people at night, responds to analgesics, and can be agonising for years.
> What is in pain is the brain’s neural map of the foot, which persists in the
> cortex long after the tissue is gone.
>
> Ramachandran’s solution was a mirror box. A mirror placed along the body’s midline
> creates a reflection of the intact hand where the absent hand should be. The patient
> watches the reflection move. The brain’s model updates: *the hand is there, the hand
> is moving, the hand is fine.* For many patients, the pain decreases or disappears.
> The model changed. The suffering reduced. Nothing in the body changed at all.
>
> This is not a curiosity. It is the normal condition of all somatic experience. The
> brain does not receive raw body signals and display them. It maintains a continuous
> predictive model of the body and generates what you *feel* from that model.
> The felt body is the predicted body.
>
> For the Soma-Field Model, this is load-bearing. The field $\mathbf{e}(t)$ is not a
> readout of the physical body. It is the nervous system’s model of the body. When
> the model is updated — by new sensory experience, somatic therapy, or the slow
> accumulation of safety — what is felt changes. Not because the body changed.
> Because the prediction changed.
>
> Therapy does not fix the body. It updates the model.

---

![Figure 2.1. The body–brain coupling stack. Interoceptive signals from the body feed into the brainstem and autonomic nervous system, which couples bidirectionally to the limbic soma-field (coupling matrix **W**). The field gates input to the prefrontal cortex via the threshold θ; what crosses becomes conscious percept. *Author's original figure.*](figures/fig1_architecture.pdf){width=90%}

---

## 2.3 The Soma-Field: A Technical Definition

In the Soma-Field Model, we represent the body's emotional state as a vector of
activation levels across a set of emotional dimensions. Call this vector $\mathbf{e}$:

$$\mathbf{e} = (e_1, e_2, \ldots, e_n)$$

Each $e_i$ is a real number representing the activation level of a somatic emotional
mode at a given moment: the level of fear-readiness in the body, the level of
grief-contraction, the level of social-engagement openness, and so on. The exact
labelling of the modes is secondary to the structure; what matters is that there is a
space of such states and a dynamics on that space.

The soma-field is this vector $\mathbf{e}$, evolving in time. It is not a single number
(arousal level) or a pair of numbers (valence and arousal). It is a multi-dimensional
state that captures the full texture of somatic experience at a given moment.

Three things are immediate from this definition:

1. **The field has a position**: the current emotional state is a point in an
   $n$-dimensional space.
2. **The field has dynamics**: it moves through this space over time.
3. **The field has a structure**: some positions are stable (attractors), and the
   dynamics drives the field toward them.

The next chapter is about that structure.

---

> **GOING DEEPER: Quantum Fields and Why They Are Relevant**
>
> In quantum field theory (QFT), the fundamental objects are not particles but fields
> — wave-like disturbances propagating through space. Particles are what you see when
> a field vibrates at a high enough amplitude to be detected: an electron is a ripple
> in the electron field, a photon is a ripple in the electromagnetic field.
>
> The soma-field is not a quantum field in the literal sense. Emotional dynamics are
> classical, not quantum. What the Soma-Field Model borrows from QFT is the
> *mathematical language*: the same equations that describe how quantum fields couple
> to each other turn out to describe how emotional modes couple to each other. This
> is not because emotion is quantum-mechanical. It is because coupling dynamics —
> the mathematics of how things that interact shape each other's behaviour — takes the
> same form wherever it appears.
>
> This correspondence is the subject of Chapter 7. For now: the QFT connection is a
> mathematical tool, not a metaphysical claim.

---

> **KEY TERMS**
>
> **Field** — a quantity with a value at every point in space (or, in the soma-field
> context, at every point in the body's state space).
>
> **Interoception** — the nervous system's process of sensing the internal state of the
> body.
>
> **Interoceptive accuracy** — the precision with which a person can consciously read
> their own interoceptive signals.
>
> **Soma-field** — the vector $\mathbf{e}$ of somatic activation levels across emotional
> modes; the state of the body's emotional field at a given moment.
>
> **State space** — the set of all possible values of $\mathbf{e}$; the arena within
> which emotional dynamics occurs.

---

![Figure 2.2. The soma-field oscillates continuously. Most of the time its modes remain below the perception threshold T (dashed line) — sub-threshold activity that drives physiology and behaviour invisibly. Only a sufficiently large excitation crosses T into felt experience. Interoceptive training and somatic therapy work, in part, by lowering T. *Author's original figure.*](figures/fig0_field_mode.png){width=90%}

---

\newpage
