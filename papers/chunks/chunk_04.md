
# Chapter 11: A Voyage into the Field

> **LEARNING OBJECTIVES**
>
> By the end of this chapter you should be able to:
>
> - Explain what it means to *navigate* an emotional field rather than merely observe it
> - Describe the two sectors of soma-field dynamics: perturbative (within a basin) and non-perturbative (threshold crossings)
> - Explain what a Feynman diagram represents and apply the concept informally to emotional coupling
> - Define the *emotional score* of a narrative and distinguish it from its container
> - Explain the holographic principle as applied to clinical assessment
> - Describe what EmotionML captures and what it omits

---

Two films. One from 1966. One never made.

In *Fantastic Voyage* (Fleischer, 1966), a submarine called the *Proteus* is miniaturised
to microscopic scale and injected into the bloodstream of a critically injured scientist.
The crew has sixty minutes to navigate from the carotid artery to a blood clot in the
brain, dissolve it, and exit before the miniaturisation reverses. The body is the
territory. The voyage is literal.

In a therapy session, something similar happens. Attention — the therapist's, and
eventually the patient's own — is directed inward. It navigates through layers of somatic
sensation, emotional activation, and memory echo. It encounters resistance: the field's
own defence against being observed. It approaches regions of high activation — the deep
attractors — and, if conditions permit, crosses the threshold into them rather than
turning back.

The body is the territory in both cases. The voyage is into an interior that has its own
geography, its own currents, its own immune responses. The *Proteus* crew is attacked by
white blood cells — the body's machinery for destroying foreign objects. The therapeutic
attention is resisted by the field's own homeostatic mechanisms: avoidance, dissociation,
intellectualisation, the body's insistence that some regions remain unvisited.

*It was always the same film.*

The Soma-Field Model provides the mathematics of that film: the Hamiltonian landscape the
crew must navigate, the attractor basins where the submarine drifts without effort, the
energy barriers that require thrust to cross, the memory kernel that makes past routes
echo in present navigation. This chapter develops the geometry of the voyage.

---

## 11.1 The Navigable Landscape

In Chapter 4 we introduced the Hamiltonian $H(\mathbf{e})$ as the energy function of the
emotional field. The state of the field is a point in the high-dimensional space of all
possible emotional-somatic configurations. The dynamics move the field downhill toward
local minima — the attractor basins.

Think of this as terrain. The attractor basins are valleys. The field settles naturally
into whichever valley it is closest to, and tends to stay there unless external energy
(a trigger, a somatic cue, a therapeutic intervention) pushes it uphill toward a ridge
and over into another valley.

The therapeutic voyage is a navigation across this terrain: starting in one valley (the
presenting state), moving toward another (the target state — safety, integration, the
capacity for contact), crossing the ridges in between. The ridges are the thresholds.
The crossing is the therapeutic event.

**What the terrain looks like.** For a field with two strongly coupled modes — call them
*fear* and *shame* — the landscape is a surface in three dimensions: fear on one axis,
shame on another, energy on the vertical axis. The attractor is a bowl. The trauma state
may have two bowls: a "fear-then-shame" sequence, and a "freeze" attractor from which
shame and fear are both absent but unreachable.

For $n$ modes, the terrain is $n$-dimensional. Visualisation requires projection, but the
mathematics is the same regardless of dimension.

**Fractal basin boundaries.** When the coupling matrix $W$ is asymmetric — when fear
drives shame more strongly than shame drives fear, as is common in post-traumatic
presentations — the boundary between attractor basins is not a smooth curve. It is
fractal: the boundary between the "hypervigilance" basin and the "collapse" basin in a
traumatised field has infinitely complex interdigitation at every scale of magnification.

The Mandelbrot set is the mathematical archetype of a fractal basin boundary: the
boundary between the set and its complement is a Julia set, infinitely detailed at every
scale. The fractal basin boundaries of the soma-field are of the same class. The
visualisation is not merely aesthetic — the mathematics is the same.

> **GOING DEEPER: Fractals, Julia Sets, and Attractor Boundaries**
>
> The iteration $z \mapsto z^2 + c$ that generates the Mandelbrot set is a discrete
> dynamical system on the complex plane. Its attractor is the origin (the sequence
> converges to 0), or infinity (the sequence escapes). The boundary between the two
> basins is the Julia set $J_c$ — a fractal object that, for most values of $c$, has
> non-integer (Hausdorff) dimension strictly between 1 and 2.
>
> The soma-field is a continuous dynamical system on $\mathbb{R}^n$, not a discrete
> iteration on $\mathbb{C}$. But the mechanism is the same: nonlinear coupling between
> modes (the $W_{ij}$ terms + the threshold nonlinearity) generates sensitivity at the
> boundary that propagates across scales. The Hausdorff dimension of the boundary is a
> direct function of the asymmetry of $W$ and the steepness of the threshold
> nonlinearity. In a severely traumatised field with highly asymmetric coupling, the
> boundary dimension approaches 2: the boundary is space-filling. There is, in the
> formal sense, no clean edge between hypervigilance and collapse. Just increasingly
> complex interdigitation.

**Clinical implication.** The fractal character of the basin boundary means that small
perturbations near the threshold have disproportionate effects — the butterfly effect is
concentrated at the boundary. A session conducted near a threshold crossing is
qualitatively different from a session conducted well inside a basin. The geometry
predicts this before any clinical experience confirms it.

---

## 11.2 Emotions Looking for Each Other

In particle physics, interactions are drawn as Feynman diagrams: lines representing
particles moving through space and time, meeting at vertices where something happens.
An electron emits a photon. A quark changes flavour. Two particles scatter.

The same formalism applies to the soma-field, and the interpretation is immediate.

**The propagator.** A single emotional mode — call it *fear* — traveling through time
without interacting with anything else is drawn as a single line, moving from left to
right (earlier to later). The line gets fainter as time increases: the mode decays toward
its equilibrium unless maintained by coupling or stimulus. This is the *propagator* —
the Green's function of the free dynamics.

```
  Single-mode propagator:

  fear ───────────────────────────>   (decays at rate |W_fear,fear|)
       t'                         t
```

**The coupling vertex.** When fear and shame are coupled — $W_{\text{fear, shame}} \neq 0$
— they can scatter: fear activates shame, shame amplifies fear. This is drawn as two
lines meeting at a vertex, with the coupling strength $W_{ij}$ labeling the junction.

```
  Fear-shame coupling vertex:

  fear  ────────────● ──────────── fear
                    │  W_fs
  shame ────────────● ──────────── shame
```

If $W_{\text{fear, shame}} > 0$, shame excites fear. If $W_{\text{fear, shame}} < 0$,
shame suppresses fear. For the asymmetric case $W_{\text{fear, shame}} \neq
W_{\text{shame, fear}}$ — one emotion drives the other more than it is driven in return —
the vertex is directional. Fear leads shame in a post-traumatic field. Shame may or may
not respond in kind.

**Feedback loops.** When fear excites shame and shame excites fear in a closed cycle, the
diagram is a loop. The loop is not merely a metaphor: it is a precise mathematical object
whose value — computed by integrating over the intermediate times — gives a correction to
the effective coupling at the loop's characteristic timescale.

```
  Fear-shame feedback loop:

  FEAR  ────────────●─────────────────────●──── FEAR
                    │  W_fs               │
                    └─────── SHAME ───────┘
                                W_sf
                    Loop correction: loop runs faster,
                    effective W_fear,fear increases.
                    This is sensitisation.
```

Repeated co-activation of fear and shame — as occurs in a trauma where shame was the
response to terror — consolidates the loop: the effective coupling grows. The Feynman
diagram is a picture of how shame becomes a reliable trigger for fear across sessions and
years.

**The memory vertex.** The trauma memory kernel introduces a vertex that is non-local in
time: mode $j$ at some earlier time $t'$ contributes to mode $i$ now, at time $t$, with
weight $K(t - t')$. The diagram has an internal arrow going backward in time — not
acausally, but in the sense that the *past state* of the field is still driving the
*present state*.

```
  Memory kernel vertex:

  shame(t') ────╮  K(t-t') J_fs
                ╰──────────────────── fear(t)

  The shame at time t' is still driving fear now,
  weighted by how much the memory kernel retains it.
```

For a field with a slow memory kernel (large $\tau_k$), past activations echo far into
the future. A traumatic incident twenty years ago is still driving present fear via the
memory vertex — not as a belief or a narrative, but as a dynamical coupling with a
specific timescale.

**The instanton: the pivot.** No finite collection of Feynman diagrams — no sum of
scattering and loop corrections — describes a threshold crossing. The topological change
from one basin to another is a *non-perturbative* event: an instanton. It is not a series
of small steps; it is a qualitative transition, a jump between attractors. In physics,
instantons are the events that perturbation theory cannot see. In the therapy room, they
are the sessions that change something permanently.

> **GOING DEEPER: The Two Sectors**
>
> Every field theory divides into a *perturbative* sector (small fluctuations, describable
> by Feynman diagrams) and a *non-perturbative* sector (large topological events,
> described by instantons, solitons, and other saddle-point solutions).
>
> The soma-field has the same division:
>
> | Sector | Events | Mathematical description |
> |---|---|---|
> | Perturbative | Emotional coupling, sensitisation, habituation, day-to-day activation | Feynman diagrams: propagators, vertices, loops |
> | Non-perturbative | Threshold crossings, basin transitions, pivotal sessions | Instantons: minimal-action paths between basins |
>
> The perturbative sector is accessible to standard talk therapy (changing $W_{ij}$ by
> desensitisation; damping memory kernel amplitudes $A_k$; adjusting thresholds). The
> non-perturbative sector requires conditions for threshold crossing: sufficient activation
> energy, a safe enough container, and — often — direct somatic engagement. You cannot
> reach an instanton by accumulating small perturbative steps. That is the formal reason
> why some therapeutic approaches reach a ceiling.

---

## 11.3 The Emotional Score

A musical score is not a performance. It is the abstract structure that can be performed
in many ways — by different orchestras, in different halls, at different tempos — while
remaining recognisably itself. The *notes* are the invariant; the *sound* is the
realisation.

A film has an emotional score. Not the music (though the music is part of its
expression), but the trajectory of the emotional field that the film traces over its
duration: how activation rises and falls, which modes are coupled, where the thresholds
are crossed, what the final attractor state is.

This emotional score is independent of the narrative container — the specific story in
which it is realised. The same score can be realised in a river journey, a war, a
marriage, a career, a therapy, or a voyage through a bloodstream.

**Formally.** The emotional score is a trajectory $\mathbf{e}^*(t)$ in the emotional
field space, parameterised by story-time $t \in [0, 1]$ (opening to closing). A film,
novel, or therapy session is:

$$\text{Realisation} = \bigl(\mathbf{e}^*(t),\; \text{Container}\bigr)$$

The container provides the narrative surface: characters, setting, imagery, plot. The
emotional score provides the dynamics: which modes activate, in what sequence, at what
coupling strength.

**The Conrad example.** *Heart of Darkness* and its film realisation *Apocalypse Now*
(Coppola, 1979) share a score: an upstream journey toward something pre-verbal, toward a
figure (*Kurtz*) who represents the field's deepest attractor — the place where normal
threshold regulation has dissolved. The journey upstream is a journey toward decreasing
$\tau_d$ (shorter developmental time), toward earlier, more diffuse, less differentiated
emotional modes. The field becomes less structured as the journey continues. Kurtz is the
attractor at the bottom of the developmental basin — not a monster, but the deepest
attractor, the one with no threshold above it.

The score is: *progressive reduction of threshold distance, increasing weight of
pre-verbal modes, final approach to a basin from which ordinary return is blocked.* The
container (Congo river / Vietnam river) is a surface over which this score is played.

**Multi-scale structure.** The score has fractal structure: the same emotional pattern
recurs at the level of the full film, the act, the scene, and the moment. A scene in
which a character approaches and retreats from a threshold is a micro-version of the
film's macro-structure. This is not a metaphor — the soma-field dynamics are
scale-invariant near a critical point, so the same Hamiltonian structure repeats across
timescales. A good filmmaker composes at all scales simultaneously.

**The viewer's field.** The viewer has their own emotional field $\mathbf{e}_V(t)$ which
couples to the screen signal $S(t)$:

$$\dot{\mathbf{e}}_V = -\nabla H_V(\mathbf{e}_V) + \lambda \cdot S(t) + \eta_V$$

The director controls $S(t)$ — the screen signal — but not $H_V$ (the viewer's own
landscape). A viewer whose own field has a deep shame attractor will have a different
response to the same $S(t)$ than a viewer without it. The film is the same; the voyage
is different. This is the formal account of why films affect different people differently,
and why re-watching a film after therapeutic work can produce a qualitatively different
emotional experience: $H_V$ has changed.

---

## 11.4 The Holographic Clinic

In theoretical physics, the holographic principle (Susskind, 1995; Bousso, 2002) states
that the complete description of a volume of space can be encoded on its boundary surface,
with no loss of information. A three-dimensional object is fully represented by a
two-dimensional hologram. The interior is encoded in the edge.

The soma-field has a holographic structure that is clinically actionable.

**The boundary.** The observable boundary of the soma-field is what can be seen from
outside: behaviour, posture, facial expression, reported affect, the pattern of
threshold crossings in session, the rate of escalation and de-escalation, the latency
between stimulus and response. This is the boundary data — the hologram.

**The bulk.** The interior of the soma-field is inaccessible to direct observation: the
weight matrix $W$, the memory kernel $K(\tau)$, the effective thresholds $T_i$, the
attractor topology. These are the bulk fields.

**The reconstruction theorem.** If the boundary data is sufficiently rich — if we observe
enough threshold crossings, enough coupling patterns, enough temporal correlations — the
bulk fields can be reconstructed. The weight matrix $W_{ij}$ can be estimated from the
co-activation statistics of observed modes. The memory kernel time constants $\tau_k$ can
be estimated from the delay between stimulus and response at different frequencies. The
attractor topology can be inferred from which basins the field visits and how long it
dwells in each.

*The body tells you everything.* This is not a therapeutic truism. It is a measurement
theorem: given sufficiently rich boundary data, the full soma-field is recoverable from
external observation. The body is a hologram of its own interior.

**Clinical implication.** A thorough intake assessment — one that tracks not just
presented symptoms but response latencies, co-occurrence statistics, threshold distances,
and interoceptive access — is a holographic measurement. It gives access to the bulk
fields without requiring the patient to verbally report what they do not have words for.
The body has been keeping a precise record. The therapist's task is to read it.

---

## 11.5 EmotionML: Labels Without Dynamics

The W3C EmotionML standard (Schröder et al., 2011) provides a formal vocabulary for
annotating emotional states in human-computer interaction. It specifies representation
formats for emotion categories (anger, fear, joy, sadness...), dimensions (valence,
arousal, dominance), and appraisals (novelty, intrinsic pleasantness, goal congruence).
It is a well-engineered taxonomy.

It is not a dynamical theory.

EmotionML says what emotional state a system is in at time $t$. It does not say how that
state changes, what coupling it has to other states, what its threshold distance is, how
its memory kernel drives its future evolution, or what basin transition conditions apply.
It provides a label; the Soma-Field Model provides the dynamics.

The relationship is analogous to the relationship between a chemical nomenclature (naming
compounds) and a rate equation (describing how compounds react). The nomenclature is
necessary but not sufficient. Knowing that a patient presents as "fearful" is the EmotionML
layer. Knowing the coupling $W_{\text{fear, shame}}$, the threshold $T_{\text{fear}}$, the
memory kernel time constants, and the attractor depth is the soma-field layer. The
second layer strictly includes the first.

> **AUTHOR'S NOTE: Why Taxonomy Is Not Enough**
>
> The history of psychiatry is largely a history of improving the taxonomy: from
> humours to syndromes to DSM categories to dimensional models. Each generation's
> taxonomy is more precise than the previous. Each is still a taxonomy.
>
> The shift from taxonomy to dynamics is not a refinement. It is a change of
> mathematical structure: from a set of labels to a vector field on a state space,
> with a Hamiltonian, a noise term, and a coupling matrix. The prediction capability
> is qualitatively different. A taxonomy tells you what something is called. A
> dynamical model tells you what it will do next and what it would take to change it.
>
> EmotionML is a very good taxonomy. The Soma-Field Model is the next layer.

---

> **KEY TERMS**
>
> **Navigable landscape** — the Hamiltonian $H(\mathbf{e})$ understood as terrain,
> with attractor basins as valleys and thresholds as ridges that must be crossed.
>
> **Fractal basin boundary** — the boundary between attractor basins when the coupling
> matrix $W$ is asymmetric; has non-integer Hausdorff dimension and is sensitive to
> perturbation at all scales.
>
> **Feynman diagram** — a graphical notation for the terms in a perturbative expansion;
> in the soma-field, lines represent propagating modes, vertices represent couplings,
> and loops represent feedback cycles.
>
> **Perturbative sector** — dynamics within an attractor basin, describable by Feynman
> diagrams; accessible to standard desensitisation and coupling-modification approaches.
>
> **Non-perturbative sector** — threshold crossings and basin transitions; described by
> instantons; requires conditions for the full threshold-crossing event.
>
> **Instanton** — a non-perturbative saddle-point solution connecting two attractor
> basins; in the therapy room, the pivot moment that changes the field topology.
>
> **Emotional score** — the trajectory $\mathbf{e}^*(t)$ that defines a narrative's
> emotional structure independently of its container; formally $\text{Realisation} =
> (\mathbf{e}^*(t), \text{Container})$.
>
> **Holographic principle** — the claim that boundary observables (behaviour, symptoms,
> threshold patterns) encode the full bulk fields ($W$, $K$, attractor topology);
> the basis for clinical assessment as measurement.
>
> **EmotionML** — W3C standard for emotion annotation; provides taxonomy (labels) but
> not dynamics (evolution equations); a necessary but not sufficient layer.

---

> **CHAPTER SUMMARY**
>
> The Soma-Field Model provides the geometry of a voyage. The Hamiltonian landscape is
> the territory: attractor basins are valleys, thresholds are ridges, and the field
> navigates this terrain continuously. For asymmetric coupling matrices, the basin
> boundaries are fractal — infinitely complex at every scale, sensitive to perturbation
> everywhere along the edge.
>
> The dynamics divide into two sectors. The perturbative sector — small fluctuations
> within a basin — is organised by Feynman diagrams: propagators carry modes through
> time, coupling vertices describe interactions between modes, feedback loops describe
> sensitisation, and memory kernel vertices describe the echo of past activations into
> the present. The non-perturbative sector — threshold crossings — is described by
> instantons: the minimal-action paths between basins that no perturbative sum can reach.
>
> Narratives have emotional scores: trajectories $\mathbf{e}^*(t)$ that define a film or
> story independently of its narrative container. The same score can be realised in a
> river journey, a war, or a voyage through a bloodstream. The viewer's own soma-field
> couples to the screen signal; what they experience depends on their own Hamiltonian.
>
> The boundary of the soma-field encodes the bulk: behavioural observation, response
> latency, co-activation statistics, and threshold patterns give access to the full
> weight matrix, memory kernel, and attractor topology without requiring verbal report
> of what has no words. The body is a hologram of its own interior.
>
> EmotionML provides the taxonomy. The Soma-Field Model provides the dynamics. Both are
> needed; the second strictly extends the first.

---

\newpage

# Epilogue: The T's

There are four T's in this book, and they are not accidental.

**Theory** — the formal structure that makes prediction possible. A theory is not a guess
or an opinion. It is a precise description that can be tested, that makes specific
predictions, and that says exactly what evidence would falsify it. The Soma-Field Model
is a theory of emotional dynamics: it makes predictions about attractor structure,
about the character of pre-verbal versus late trauma, about what parameters change in
effective therapy. Whether those predictions survive contact with data is an empirical
question, and the empirical work is needed.

**Threshold** — the parameter $T$, which appears in the model as the boundary between
sub-threshold somatic activity and conscious emotional experience. The threshold is not
a switch. It is a continuous parameter, differently set in different nervous systems,
modifiable through practice and therapy. The difference between a body that feels
everything and a body that feels nothing is, in formal terms, a difference in $T$.
The therapeutic expansion of the window of tolerance is, in formal terms, a widening
of the range around $T$ within which the field can move without triggering a phase
transition.

**Time** — the developmental time $\tau_d$, which changes the character of a
modification from perturbative (late trauma: $W = W_0 + \delta W$, a baseline plus
a modification) to structural (pre-verbal trauma: $W = W_{\text{trauma}}$, the
modification is the structure). Time also appears in $\tau_k$ — the decay time of the
memory kernel, how long an echo persists. Therapy changes $\tau_k$. The passage of time,
in the absence of intervention, does not reliably change $\tau_k$ for pre-verbal somatic
traces.

**Transformation** — the fourth T, the one that this book is about, finally. Not recovery.
Not return. Not the restoration of a prior state. The construction of a new landscape:
wider, more flexible, with deeper calm and shallower hypervigilance, arrived at from
where the system is, going somewhere it has not been before.

There is a fifth T, which gave this book its title: **Trance** — in two senses. The
first: the altered state at the threshold, the phase transition, the field crossing a
boundary and remaining in the other phase. Trance is not a malfunction; it is a dynamic
state, momentarily ungoverned by the usual attractors. In those moments, something is
possible that is not possible from within a stable phase.

The second sense is the title itself. *A Voyage into Trance* (1995) is a Goa trance
compilation by Paul Oakenfold. The trance state produced by extended rhythmic music and
the freeze response of a traumatised nervous system are not the same experience. They are
governed by the same mathematics. Both drive an arousal variable across a threshold and
sustain it there. Music does this deliberately; trauma does it involuntarily. The
mathematics does not distinguish.

The voyage into trauma is not a straight line. It passes through all five T's,
sometimes in order, sometimes not.

The model is the map.
The body is the territory.
The voyage is yours.

---

\newpage

# Appendices

---

## Appendix A: The Mathematics in Full

*The following is a condensed version of the academic paper* Soma-Field Model of
Emotional Dynamics and C-PTSD *for readers who want the formal derivations. Full
derivations, Lean 4 type sketches, and bibliography are in the companion document
`soma-field-paper.md`.*

### A.1 The Hamiltonian

$$H(\mathbf{e}) = -\frac{1}{2}\,\mathbf{e}^{\top} W\, \mathbf{e} - \boldsymbol{\theta}^{\top}\mathbf{e}$$

where $W \in \mathbb{R}^{n \times n}$ is the coupling matrix and
$\boldsymbol{\theta} \in \mathbb{R}^n$ is the threshold bias vector.

### A.2 The Dynamics

$$\dot{\mathbf{e}}(t) = -\nabla H(\mathbf{e}) + \sigma_0\,\eta(t) = W\mathbf{e} + \boldsymbol{\theta} + \sigma_0\,\eta(t)$$

where $\eta(t)$ is white noise with $\langle\eta_i(t)\eta_j(s)\rangle = \delta_{ij}\delta(t-s)$.

### A.3 The C-PTSD Modification

$$W_{\text{C-PTSD}} = W_0 + \Delta W, \qquad \Delta W_{ij} \neq \Delta W_{ji}$$

The asymmetry of $\Delta W$ breaks the gradient flow property and introduces directional
cycles in the landscape.

### A.4 The Memory Kernel

$$\dot{\mathbf{e}}(t) = -\nabla H(\mathbf{e}) + \int_0^t K(t-s)\,\mathbf{e}(s)\,ds + \sigma_0\,\eta(t)$$

$$K(\tau) = \sum_k A_k\, e^{-\tau/\tau_k}$$

### A.5 Developmental Time Parameterisation

$$W(\tau_d) = f(\tau_d)\cdot W_0 + \bigl(1 - f(\tau_d)\bigr)\cdot W_{\text{trauma}}$$

$$f(\tau_d) = \tanh\!\left(\frac{\tau_d}{\tau_c}\right), \qquad \tau_c \approx 36 \text{ months}$$

### A.6 The QFT Correspondence

Under the Wick rotation $t \to -i\tau$:

| QFT | Soma-Field |
|-----|-----------|
| $G_E(\tau) = \frac{1}{2m}e^{-m\lvert\tau\rvert}$ | $K(\tau) = \sum_k A_k e^{-\lvert\tau\rvert/\tau_k}$ |
| Field mass $m$ | Inverse decay time $1/\tau_k$ |
| $H_{\text{Ising}}$ | $H_{\text{soma}}$ |

---

## Appendix B: Lean 4 Type Sketches

The following are proof sketches in Lean 4. `sorry` marks open proof obligations.

```lean
-- Core soma-field structures
structure CouplingMatrix (n : ℕ) where
  W : Matrix (Fin n) (Fin n) ℝ
  θ : Fin n → ℝ

structure SomaField (n : ℕ) where
  e     : Fin n → ℝ      -- current activation vector
  W     : CouplingMatrix n
  T     : ℝ              -- threshold parameter
  sigma : ℝ              -- noise amplitude

-- The Hamiltonian
noncomputable def hamiltonian {n : ℕ} (W : CouplingMatrix n) (e : Fin n → ℝ) : ℝ :=
  -0.5 * Matrix.dotProduct (Matrix.mulVec W.W e) e
  - Matrix.dotProduct W.θ e

-- C-PTSD modification: asymmetric coupling
def isCPTSDModified {n : ℕ} (W : CouplingMatrix n) : Prop :=
  ∃ i j, W.W i j ≠ W.W j i

-- Developmental time parameterisation
structure TraumaProfile (n : ℕ) where
  τ_d        : ℝ
  asymmetry  : Matrix (Fin n) (Fin n) ℝ
  amplitudes : List (Fin n → ℝ)
  decayTimes : List (Fin n → ℝ)

def τ_c : ℝ := 36

noncomputable def structuralFraction (τ_d : ℝ) : ℝ :=
  Real.tanh (τ_d / τ_c)

-- For pre-verbal trauma: structural fraction < tanh(1) ≈ 0.76
theorem preVerbalIsStructural {n : ℕ} (profile : TraumaProfile n)
    (h : profile.τ_d < τ_c) :
    structuralFraction profile.τ_d < Real.tanh 1 := by
  unfold structuralFraction
  apply Real.tanh_lt_tanh
  exact div_lt_one_of_lt h (by norm_num)
```

---

## Appendix C: The Cross-Language Correspondence Table

| Mathematical language | Emotional dynamics |
|---|---|
| Symmetric monoidal category $\mathcal{C}$ | Soma-field operator algebra |
| Object $A \in \mathcal{C}$ | Emotional mode type |
| Morphism $f : A \to B$ | Field operator (maps one mode to another) |
| Tensor product $A \otimes B$ | Simultaneous activation of modes $A$ and $B$ |
| Composition $g \circ f$ | Sequential field operations |
| Identity morphism $\text{id}_A$ | Identity (mode persists unchanged) |
| Braiding $\sigma : A \otimes B \cong B \otimes A$ | Mode-order independence of simultaneous states |
| Feynman vertex | Emotional interaction (coupling $W_{ij}$) |
| Loop diagram | Memory kernel (self-coupling over time) |
| Feynman propagator | Memory trace decay $e^{-\lvert\tau\rvert/\tau_k}$ |
| Vacuum state | Resting soma-field (minimal activation) |
| Partition function $Z$ | Field normalisation (probability distribution over states) |
| Renormalisation group flow | Therapeutic modification of coupling constants |
| Phase transition | Polyvagal state transition (ventral/sympathetic/dorsal) |
| Symmetry breaking | Asymmetric $W$ (C-PTSD modification) |

*The correspondences in this table are not analogies. They are identifications of the
same mathematical object in two notation systems, established by the Baez–Lauda coherence
theorem (2011) for the categorical column and the Wick rotation for the QFT column.*

---

## Appendix D: Glossary

**Amplitude $A_k$** — The strength of a trauma memory trace's influence on the current
soma-field. Reduced by effective somatic therapy.

**Attractor** — A stable state in the energy landscape; a position toward which the
soma-field naturally moves from nearby states.

**Basin of attraction** — The region of state space from which the field flows toward a
given attractor.

**C-PTSD operator** — The modification $\Delta W$ to the coupling matrix that represents
the effect of complex developmental trauma on the soma-field landscape.

**Co-regulation** — The process by which the soma-field of one person influences another
through relational coupling; the somatic mechanism of relational healing.

**Coupling matrix $W$** — The matrix encoding the interactions between emotional modes;
determines the shape of the energy landscape. Symmetry of $W$ guarantees stable attractors.

**Damping $\gamma$** — The rate at which the field returns toward attractors after
perturbation. Low damping (ADHD) produces rapid, wide-ranging field dynamics.

**Decay time $\tau_k$** — How long a trauma memory trace persists before fading.
Pre-verbal traces typically have longer decay times.

**Developmental age at trauma $\tau_d$** — The age in months at which the primary
traumatic modification occurred. Determines whether the modification is perturbative
(late trauma) or structural (pre-verbal trauma).

**Effective temperature** — The ratio $\sigma_0^2 / \gamma$; determines how widely the
soma-field explores the landscape relative to the depth of the attractors.

**Forward transformation** — The construction of a new coupling matrix $W'$ with desired
dynamical properties, as the correct therapeutic goal for pre-verbal trauma (as opposed
to recovery of a prior baseline).

**Hamiltonian $H$** — The energy function that assigns a value to every possible
soma-field state; determines the landscape's hills and valleys and thus the dynamics.

**Interoception** — The nervous system's process of sensing the body's internal state.

**Interoceptive accuracy $\alpha$** — The precision with which a person can read their
own soma-field state. Disrupted by trauma; improvable through training and therapy.

**Memory kernel $K(\tau)$** — The function describing how past field activations
continue to influence the current state. In C-PTSD: a sum of decaying exponentials.

**Noise amplitude $\sigma_0$** — The magnitude of random fluctuations in field dynamics.
Elevated in ADHD; reduced by breath and autonomic regulation.

**Phase transition** — A qualitative reorganisation of the field's state at a critical
parameter value. Polyvagal state changes (e.g., ventral vagal to freeze) are phase
transitions, not gradual changes.

**Soma** — The body as experienced from the inside; the totality of interoceptive signals.

**Soma-field** — The vector $\mathbf{e}$ of somatic activation levels across emotional
modes; the state of the body's emotional field at a given moment.

**Structural fraction $f(\tau_d)$** — The proportion of the coupling matrix attributable
to neurotypical baseline development versus trauma-formed modification.

**Threshold $T$** — The activation level above which a soma-field mode becomes conscious
experience. The boundary between felt emotion and sub-threshold somatic activation.

**Verbal encoding threshold $\tau_c$** — The approximate developmental age (≈36 months)
at which narrative memory and verbal encoding capacity reliably emerges.

**Wick rotation** — The substitution $t \to -i\tau$ that transforms oscillatory quantum
dynamics into real-time thermal/stochastic dynamics; the bridge connecting QFT
propagators to soma-field memory kernels.

**Window of Tolerance** — The range of arousal within which the nervous system can
function flexibly, process information, and engage socially.

---

## Bibliography

The following references are cited in this book. Full academic citation details are in
the companion document `bibliography.bib`.

- Baez, J. C., & Lauda, A. D. (2011). A prehistory of $n$-categorical physics.
- Damasio, A. (1994). *Descartes' Error: Emotion, Reason, and the Human Brain*.
- Gendlin, E. T. (1978). *Focusing*.
- Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective
  computational abilities. *PNAS, 79*(8), 2554–2558.
- Levine, P. A. (2010). *In an Unspoken Voice*.
- Ogden, P., Minton, K., & Pain, C. (2006). *Trauma and the Body*.
- Penrose, R. (1971). Applications of negative dimensional tensors.
- Porges, S. W. (2011). *The Polyvagal Theory*.
- Schore, A. N. (2001). The effects of early relational trauma on right brain development.
- Selinger, P. (2010). A survey of graphical languages for monoidal categories.
- van der Kolk, B. A. (2014). *The Body Keeps the Score*.
- Vitiello, G. (2001). *My Double Unveiled*.

---

*A Voyage into Trauma: The Soma-Field Theory of Emotional Life*
*First edition, 2026. Companion academic paper: soma-field-paper.md*

---

\newpage

## Listening Notes

This book was written in a single session on the night of 16–17 May 2026.

The development was set to *Silver Machine* by Hawkwind.
It closed with *It's So Easy* by Hawkwind.

Both choices were correct.



\newpage

\part{Interlude: The Tensor --- A Film in Fields}



\newpage

# The Tensor

*An Abstract Film Definition*

---

This is not a screenplay. It contains no dialogue, no character names, no scene
headings, no camera directions. It cannot be read to an actor or handed to a set
designer. It describes a film the way a musical score describes a performance —
as an abstract structure that can be realised in many ways, by many different
instruments, for many different audiences.

The film is defined as a trajectory through the emotional field. The rendering —
the actual pixels and samples the viewer experiences — is generated at runtime
from this trajectory, from the viewer's own soma-field state, and from a set of
control parameters. Two viewers watching the same film may hear different music.
In the limit where the viewer's own biofeedback is available, they may traverse
the trajectory differently — the film meets them where they are.

The territory is the body. The voyage is inward.

---

# Part I: The Format

## 1. The Emotional Score

A film is defined by its **emotional score**: a vector-valued trajectory

$$\mathbf{e}^*(t) = \bigl(e^*_1(t),\; e^*_2(t),\; \ldots,\; e^*_n(t)\bigr)$$

parameterised by story-time $t \in [0, 1]$ (opening to closing). Each component
$e^*_k(t)$ is the intended activation of emotional mode $k$ at story-moment $t$.

The score is **not** what the viewer feels. It is what the film proposes — the
director's instruction to the rendering system. Whether the viewer's field
resonates with the proposal depends on their own Hamiltonian $H_V$.

The standard mode vocabulary for this project uses seven primary axes:

| Mode | Symbol | Description |
|---|---|---|
| Safety | $e_S$ | Regulation, groundedness, ventral vagal tone |
| Fear | $e_F$ | Threat activation, mobilisation |
| Shame | $e_{Sh}$ | Social evaluation, self-concealment |
| Grief | $e_G$ | Loss, withdrawal, parasympathetic collapse |
| Curiosity | $e_C$ | Approach, exploration, openness |
| Awe | $e_A$ | Threshold-adjacent wonder; dissolution of self-boundary |
| Language | $e_L$ | Symbolic, conceptual, narrative organisation |

Additional modes can be added per score. Pre-verbal affect, disgust, rage, and
the somatic marker of HRV coherence may all appear as named axes.

## 2. Threshold Events

At specified story-times $t_k$, the score may declare a **threshold crossing** —
a non-perturbative event in which the emotional field transitions between attractor
basins. These are not smooth changes of $\mathbf{e}^*(t)$; they are instantons.

A threshold event is declared as:

```
THRESHOLD  t = 0.58  FROM: [hypervigilance]  TO: [awe]
           condition: e_F > 0.7 AND e_A rising
           duration: 0.04  (narrow window)
```

The rendering system must hold the score near the threshold approach for as long
as necessary until the crossing condition is met — whether by the score's internal
dynamics or by the viewer's biofeedback signalling readiness.

## 3. Control Knobs

The score is rendered through a set of **control parameters** $\kappa$ that the
viewer, clinician, or runtime system can adjust. These are continuous dials, not
binary switches.

| Knob | Symbol | Effect |
|---|---|---|
| Depth | $\kappa_d \in [0,1]$ | How far the instanton descends into the pre-verbal attractor. At $\kappa_d = 0$, threshold crossings are shallow; at $\kappa_d = 1$, the full instanton trajectory is traversed. |
| Velocity | $\kappa_v \in [0.1, 3]$ | Clock multiplier for story-time. $\kappa_v < 1$: expanded, slower passage. $\kappa_v > 1$: compressed. |
| Resonance | $\kappa_r \in [0,1]$ | Weight of viewer biofeedback in modulating the score. At $\kappa_r = 0$: pure projection. At $\kappa_r = 1$: the score is entirely driven by the viewer's field (the film becomes a mirror). |
| Texture | $\kappa_t \in [0,1]$ | Audio/visual granularity. Low: smooth, tonal, harmonic. High: granular, fractal, noisy. Maps to noise level $\sigma_{\text{eff}}$ in the rendering. |
| Mode mask | $\kappa_m \subseteq \{1..n\}$ | Which emotional modes are active in this rendering. A viewer without a shame attractor may have $Sh$ masked; the score is rendered without that channel. |
| Coupling scale | $\kappa_W \in [0.5, 2]$ | Global scale on the coupling matrix $W^*$ of the score. High values increase inter-mode interaction; the emotional landscape becomes more complex and entangled. |

## 4. The Rendering Function

The screen signal $S(t)$ — the actual audio and visual output — is:

$$S(t) = \mathcal{R}\bigl(\mathbf{e}^*(t),\; \kappa,\; \mathbf{e}_V(t)\bigr)$$

where:

- $\mathbf{e}^*(t)$ is the abstract score
- $\kappa$ is the control parameter vector
- $\mathbf{e}_V(t)$ is the viewer's own emotional field (measured or inferred)
- $\mathcal{R}$ is the **rendering function** — the audio/visual synthesis engine

The rendering function maps emotional-field coordinates to audio parameters
(frequency, harmonic content, tempo, grain density, spectral centroid, reverb
depth) and visual parameters (fractal dimension, colour temperature, edge
sharpness, motion speed, light level). The mapping is specified per rendering
implementation; the score is independent of any specific renderer.

## 5. The Somatic Loop

When the viewer's field $\mathbf{e}_V(t)$ is available — via HRV monitor,
skin conductance, posture sensor, or simply therapist observation — the system
closes a **somatic loop**.

Of the available biofeedback signals, **cardiac acceleration** $\dot{H}(t)$ (beats/s²)
is the most predictively useful. Current BPM tells the system where the viewer's
cardiac field *is*; $\dot{H}$ tells it where the field is *going* — the N+1 state.
A rising heart rate ($\dot{H} > 0$) predicts threshold approach and may trigger the
system to hold at a pre-threshold moment in the score, or to soften texture and
deepen resonance to meet the viewer where they are heading. A decelerating heart
rate ($\dot{H} < 0$) signals return and may allow the score velocity to increase.
The rendering system should treat $\dot{H}$ as the primary cardiac control signal
and instantaneous BPM as a secondary state indicator.

The system

$$\dot{\mathbf{e}}_V = -\nabla H_V(\mathbf{e}_V) + \kappa_r \cdot \lambda \cdot S(t) + \eta_V$$

The screen signal $S(t)$ drives the viewer's field; the viewer's field modifies
$S(t)$ via the resonance knob $\kappa_r$ and the rendering function $\mathcal{R}$.
At high resonance, the film and the viewer co-regulate. The distinction between
"watching a film" and "being in a therapy" begins to dissolve.

Two operating modes:

| Mode | $\kappa_r$ | Description |
|---|---|---|
| **Projection** | $\approx 0$ | The score drives the viewer. Classical cinema: fixed score, passive audience. |
| **Resonance** | $\approx 0.5$ | Score and viewer co-determine the output. Biofeedback cinema: the film breathes with the viewer. |
| **Mirror** | $\approx 1$ | The viewer's field drives the rendering. The score becomes a target trajectory; the system generates audio/visual content that guides the viewer toward $\mathbf{e}^*(t)$ from wherever they actually are. |

In Mirror mode, the system is a **real-time emotional score calibrator**: it
continuously measures $\mathbf{e}_V(t)$, computes the gap to $\mathbf{e}^*(t)$,
and renders audio/visual content calculated to reduce that gap. This is a formal
definition of what a therapist does.

---

\newpage

# Part II: The River Film

*A score. Not a story.*

The following is the abstract definition of a film. Its narrative container is
a river journey: upstream away from civilisation, toward something older and
less organised, then back. The container is not the film. Another realisation
of the same score might use a descent into a cave, a journey into psychosis, a
session of deep somatic therapy, or a voyage through a bloodstream in a
miniaturised submarine. The score is invariant. The river is one surface over
which it is played.

## Score Parameters

```
TITLE:        The River Film (working title)
DURATION:     t in [0, 1]  (maps to approximately 90 minutes at kappa_v = 1.0)
PRIMARY MODES: Safety, Fear, Curiosity, Awe, Grief, Language, Pre-verbal
THRESHOLD EVENTS: 2  (at t = 0.52 and t = 0.74)
DEFAULT KAPPA: depth=0.7, velocity=1.0, resonance=0.0, texture=0.4,
               coupling_scale=1.0
```

## Emotional Trajectory

The seven primary modes over story-time $t \in [0, 1]$:

```
EMOTIONAL SCORE: THE RIVER FILM
Scale: 0 (silent) → 9 (full activation)  Resolution: 0.1 story-time units

         0.0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
          |    |    |    |    |    |    |    |    |    |    |
SAFETY    9    8    7    5    3    2    1  ≠ 2    4    7    9
CURIOSITY 3    5    7    8    7    5    3    2    4    6    5
FEAR      1    1    2    3    5    7  ≠ 4    2    2    1    1
AWE       1    1    1    2    3    4    6    9    7    4    2
GRIEF     1    1    1    1    2    3    4    4    6    4    2
LANGUAGE  9    9    8    7    5    3    1  ≠ 1    3    7    9
PREVERBAL 1    1    1    2    3    5    7    9    6    3    1

  ≠ = threshold crossing event
  THRESHOLD 1 at t ≈ 0.52: Safety<2, Fear>7 → AWE begins rise  (field tips)
  THRESHOLD 2 at t ≈ 0.71: Language<1, PREVERBAL≥9 → GRIEF opens fully
              (the encounter; the deepest attractor)
```

## Phase Descriptions

**Phase 1: Departure** $t \in [0, 0.25]$

Safety is high; the field is organised. Language is dominant — the viewer is
still thinking in sentences. Curiosity rises: there is something upstream. Fear
is present but low, a background hum. The rendering is harmonic, tonal, structured.
Tempo is regular. Visual: clear light, organised geometry, recognisable forms.

*In the river container:* the boat leaves the last town. The last road disappears
behind the tree line. The journey has begun.

**Phase 2: Descent** $t \in [0.25, 0.52]$

Safety falls steadily. Curiosity peaks and begins to fall. Fear rises. Language
degrades — the score calls for less and less conceptual organisation. Pre-verbal
modes begin their ascent. The field is approaching the threshold.

The audio rendering: harmonic content decreases, spectral centroid drops, grain
size increases ($\kappa_t$ increases internally with $e_{PV}$). The music becomes
less music and more texture. Tempo irregularity increases. Visual: light dims,
edges soften, forms become ambiguous, fractal structure begins to emerge in
peripheral detail.

*In the river container:* the river narrows. The current strengthens. The
vegetation becomes unrecognisable. Something that was navigable is becoming
something that is navigating you.

**Threshold 1** $t \approx 0.52$

The first instanton. Safety $< 2$, Fear $> 7$. The field tips. This is the
moment when fear passes its threshold into something larger: the beginning of
awe. The two are close — they activate the same somatic substrate. The difference
is the interpretation. The rendering system holds here until the crossing completes.

*In the river container:* the moment you cannot go back. Not a decision. A discovery.

**Phase 3: The Deep River** $t \in [0.52, 0.74]$

Awe rises toward maximum. Fear falls — it has been superseded, not resolved.
Language approaches silence. Pre-verbal is dominant. Safety is minimal. The
field is at the bottom of the developmental axis — the oldest, most diffuse,
most somatic registers of experience. The music, if it still deserves that name,
is almost entirely noise and texture and rhythm — rhythm because the heartbeat
persists where nothing else does.

The visual rendering at $e_{PV} = 9$: pure fractal. Mandelbulb parameters driven
entirely by the emotional modes. Self-similar at every scale. No recognisable
objects. Colour driven by $e_A$ (awe) and $e_G$ (grief) — the pairing of
wonder and loss that characterises the deepest attractors.

*In the river container:* the encounter. Whatever Kurtz is. Whatever the heart
of darkness is. It does not speak in sentences. It does not need to.

**Threshold 2** $t \approx 0.74$

The second instanton. Language $= 0$, Pre-verbal $= 9$. The encounter.
This threshold does not go to a higher activation — it goes to a deeper
quality. Grief opens fully: not sadness, but the affect of having arrived at
the oldest loss, the one that precedes memory. The field is in a state that
has no name in any clinical taxonomy. It has only a position in the field.

The rendering system may pause here. At high $\kappa_r$, the viewer's own
biofeedback determines when this phase ends.

**Phase 4: Return** $t \in [0.74, 1.0]$

The journey reverses. But not to the same place. The return is asymmetric:
the basin topology has changed. Safety rises, but along a different path.
Language returns, but to describe something it could not have described at
the outset. Curiosity does not return to its Phase 1 character — it is now
the curiosity of someone who has seen something. Grief persists longer than
expected; it is the last mode to settle.

The audio rendering: gradual return of harmonic structure, but with residual
grain. The music has been changed by what happened in Phase 3. A tonal structure
that carries the memory of noise.

*In the river container:* the river widens. Light returns. Towns appear on the
bank. The world has not changed. You have.

---

\newpage

# Part III: The Rendering Architecture

## Audio Rendering

The emotional score maps to audio parameters through a continuous, differentiable
function. The following mapping is a reference implementation; specific renderers
may use different functions so long as the monotonicity and qualitative character
of each mapping is preserved.

```
AUDIO RENDERING MAP (reference implementation)

  Emotional mode          →   Audio parameter(s)

  Safety (e_S)            →   Fundamental pitch stability; reverb decay time
                               (high safety = long, stable reverb; low = short, dry)
  Fear (e_F)              →   Harmonic tension; tritone content; spectral irregularity
  Curiosity (e_C)         →   Melodic motion; register expansion; rhythmic anticipation
  Awe (e_A)               →   Dynamic range; spatial width; harmonic overtone richness
  Grief (e_G)             →   Descending melodic tendency; sub-bass presence; tempo drop
  Language (e_L)          →   Harmonic coherence; rhythmic regularity; tonal centre strength
  Pre-verbal (e_PV)       →   Grain density (granular synthesis parameter); spectral noise;
                               rhythm de-synchronisation from fixed grid

  Coupling scale (kappa_W) →  Cross-mode harmonic interference (dissonance from coupling)
  Texture (kappa_t)        →  Overall grain size; spectral smear
  Velocity (kappa_v)       →  Clock rate; effective tempo multiplier
```

In a Phase Plant implementation: each emotional mode drives a macro knob. Macros
modulate synthesis parameters across all generators. At $e_{PV} = 9$, the granular
engine is at maximum grain randomness; at $e_{PV} = 1$, it is silent or running at
maximum coherence. The complete score trajectory is an automation lane for each macro.

**Personalisation.** Different users hear different music because:

1. $\kappa_m$ may exclude modes they do not have active attractors for
2. $\kappa_r > 0$ allows their own $\mathbf{e}_V(t)$ to modulate the rendering in real time
3. $\kappa_d$ scales the depth of the instanton traversal — some users may not be
   ready for $\kappa_d = 1.0$ and the system (or clinician) sets it lower
4. The rendering function $\mathcal{R}$ may be calibrated to the individual's own
   mode vocabulary — their specific fear-to-shame coupling, their specific grief
   timescale

Two people hearing the same score may hear music that is recognisably related —
same structure, same threshold events, same overall arc — but with different
timbres, different depths, different durations at the instanton.

## Visual Rendering

The abstract visual rendering drives a fractal or generative system. The reference
implementation uses a Mandelbulb renderer with the following parameter mapping:

```
VISUAL RENDERING MAP (reference implementation)

  Emotional mode          →   Visual parameter(s)

  Safety (e_S)            →   Light level; warm colour temperature (high K value)
  Fear (e_F)              →   Edge contrast; cold hue shift; motion speed
  Curiosity (e_C)         →   Zoom velocity; camera path exploration radius
  Awe (e_A)               →   Mandelbulb power parameter (2→8: more complex geometry)
  Grief (e_G)             →   Desaturation; slow orbital camera; depth of field
  Language (e_L)          →   Structural regularity; recognisable geometric forms
  Pre-verbal (e_PV)       →   Fractal iteration depth; self-similarity at fine scales;
                               dissolution of object-level forms
```

At $e_{PV} = 9$, $e_L = 0$: the visual is a deep Mandelbulb zoom at high iteration
depth, fully abstract, no edges that resolve into recognisable shapes. The image is
entirely self-referential — a structure that contains only itself.

At $e_S = 9$, $e_L = 9$: the visual is clear, geometrically organised, warm.
A landscape that makes sense.

The emotional score determines which of these states the visual system is in at
each moment of the film.

## The Somatic Loop: Biofeedback Integration

If the viewer wears an HRV monitor or similar:

```
SOMATIC LOOP ARCHITECTURE

  Viewer
    |
    | physiological signal (HRV, SCR, respiration, posture)
    |
    v
  [FIELD ESTIMATOR]  -->  e_V(t)  (estimated viewer soma-field state)
    |
    v
  [RESONANCE MIXER]  <--  e*(t)  (abstract score)
    |
    | kappa_r blends e*(t) and e_V(t)
    v
  [RENDERER R]  -->  S(t)  (audio + visual output)
    |
    | screen signal
    v
  Viewer  (loop closes)
```

At $\kappa_r = 0$: the viewer's field does not affect the output. Standard cinema.

At $\kappa_r = 0.5$: the film breathes with the viewer. If the viewer enters
a freeze state at the threshold approach, the score velocity slows, the texture
softens, the system waits. When the viewer's HRV coherence returns, the threshold
crossing is attempted again.

At $\kappa_r = 1.0$: the film is a mirror. The audio and visual content is generated
entirely from $\mathbf{e}_V(t)$. The abstract score $\mathbf{e}^*(t)$ functions only
as a *target trajectory* — an attractor for the viewer's field. The rendering
system continuously generates content designed to guide $\mathbf{e}_V$ toward
$\mathbf{e}^*$. This is a formal implementation of therapeutic presence.

---

\newpage
