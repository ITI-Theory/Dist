
# Chapter 3: The Energy Landscape

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   "Nature does not create mountains and valleys at random.      │
  │    They are shaped by the forces beneath them."                 │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **LEARNING OBJECTIVES**
>
> By the end of this chapter, you will understand:
>
> - Why some emotional states are stable and others are transient
> - The meaning of "attractor" and "basin of attraction"
> - What the Hamiltonian is and why it organises the model
> - Why you keep returning to familiar emotional states even when you don't want to

---

## 3.1 Hills and Valleys

Imagine placing a ball on a hilly landscape. If you place it at the bottom of a valley
and give it a small push, it rolls away from where you pushed it — and then rolls back.
The valley is stable. The bottom of the valley is an *attractor*: the ball is drawn
toward it from nearby positions.

If you place the ball at the top of a hill and give it a small push, it rolls away from
the hilltop — and keeps going. The hilltop is *unstable*. Small perturbations grow into
large departures.

The same geometry applies to emotional states.

Some emotional states are at the bottom of valleys in the body's landscape: they are
stable, they are where the system tends to rest, and perturbations that push the body
away from them are followed by a return. Other states are at hilltops: they are unstable
configurations that the system passes through on its way between valleys.

The crucial question — the question that distinguishes a regulated nervous system from
a dysregulated one, and distinguishes one person's landscape from another's — is: where
are the valleys? How deep are they? How wide? How many are there?

![Figure 3.1. The emotional energy landscape (2D contour). Four attractor basins are visible: Calm (wide, deepest — the global minimum of a regulated nervous system), Freeze (narrow and very deep — easy to fall into, hard to leave), Fight and Flight (intermediate depth). The system rolls downhill to the nearest basin; the depth controls escape difficulty and the width controls resilience to perturbation. *Author's original figure.*](figures/fig3a_energy_landscape.png){width=95%}

## 3.2 Attractors and Basins

An **attractor** is a stable state — a bottom of a valley. A **basin of attraction** is
the set of all points from which the system rolls toward a given attractor: the "catchment
area" of the valley.

For a regulated nervous system, the primary attractor is some version of calm social
engagement — the ventral vagal state of Polyvagal Theory. The basin is wide: a large
range of perturbations (emotions, sensations, social situations) all resolve back to this
resting state. The system is resilient.

For a trauma-modified nervous system, the landscape has changed. A second attractor —
hypervigilance, alert-readiness, the sympathetic mobilisation state — may have become
deep and wide. The calm attractor may still exist but its basin has narrowed: it takes
very little to tip the system out of calm and into alertness. And a third attractor —
the freeze state, the dorsal vagal shutdown — may be very deep indeed: once the system
tips into it, escape requires a large input of energy.

This is not a metaphor for how trauma "feels." It is a description of the actual
dynamics of the system.

![Figure 3.2. Basin of attraction map. Each point in state space is coloured by the attractor it flows to under gradient descent: blue = Calm, purple = Freeze, orange = Fight, green = Flight. The calm basin dominates a regulated landscape. Freeze occupies a small area but is disproportionately deep — a narrow funnel. The boundaries between basins are the separatrices: invisible thresholds in state space that determine which valley a given perturbation resolves to. *Author's original figure.*](figures/figB1_attractor_basins.png){width=90%}

## 3.3 The Hamiltonian

The landscape has a name in physics: the **Hamiltonian**. Denoted $H$, it is a function
that assigns an energy value to every possible state of the system.

For the soma-field, the Hamiltonian takes the form:

$$H(\mathbf{e}) = -\frac{1}{2}\sum_{i,j} W_{ij}\, e_i\, e_j - \sum_i \theta_i\, e_i$$

Let us read this in plain English.

The first term, $-\frac{1}{2}\sum_{i,j} W_{ij}\, e_i\, e_j$, captures the *interactions
between emotional modes*. $W_{ij}$ is the coupling between mode $i$ and mode $j$ — how
strongly they influence each other. When fear is high, does shame rise with it? When calm
is present, does anger fall? The matrix $W$ encodes all of these mutual influences. The
minus sign means that aligned coupling (modes reinforcing each other) lowers the energy
— makes the state more stable.

The second term, $-\sum_i \theta_i\, e_i$, captures the *individual thresholds* of each
mode. $\theta_i$ is the bias of mode $i$ — how much the system tends toward or away from
it in the absence of coupling. A mode with a large positive $\theta_i$ has a natural
tendency toward high activation.

The dynamics — the way the field moves through state space over time — follows from this
energy function. The field always moves *downhill*: toward lower values of $H$.

$$\dot{\mathbf{e}} = -\nabla H(\mathbf{e}) + \eta(t)$$

This equation says: the rate of change of the emotional state ($\dot{\mathbf{e}}$) equals
the negative gradient of the energy (the direction of steepest descent on the landscape)
plus a noise term $\eta(t)$ representing the small random fluctuations of physiological
and environmental variation. The system is always rolling toward the nearest valley,
with a small amount of noise that occasionally kicks it over a hill into a different
basin.

The noise term has a deeper structure. The *level* of noise — how wide the fluctuations
are — is set by the autonomic nervous system, specifically by heart rate variability
(HRV): high coherence in the cardiac rhythm narrows the noise, stabilising the field;
low HRV widens it. But there is a second, more predictive cardiac quantity: the
**cardiac acceleration** $\dot{H}$ — the rate at which heart rate is *changing*. A
rising heart rate predicts approach to a threshold; a falling heart rate predicts retreat
from one. The current BPM tells you where you are. The acceleration of BPM tells you
where you are going next.

> **GOING DEEPER: Gravity and the Heartbeat**
>
> Gravity, in SI units, is measured in metres per second squared (m/s²) — it is an
> *acceleration*, not a speed. It tells you not where a falling object is, but how
> fast its velocity is changing: where it will be next.
>
> Cardiac acceleration — the rate of change of heart rate — has units beats/s².
> Same type, different physical dimension. And the same logical character: it tells
> you not what the BPM is, but where it is heading. N+1, not N.
>
> In the soma-field, cardiac acceleration acts as a **landscape tilt**: it tips the
> energy function toward activation or rest before any emotional threshold is crossed.
> When the heart accelerates, the field is being pulled toward higher-energy states
> by a force it cannot see and cannot always attribute correctly. Some anxiety that
> feels emotionally caused is cardiac in origin — the field cannot distinguish the
> two from the inside. This is the somatic equivalence principle: you cannot tell,
> from your own experience, whether your emotional landscape tilted because something
> happened, or because your heart accelerated first.
>
> Clinically: monitoring the *direction* of heart rate change, not just its level,
> gives earlier warning of threshold approach than any other non-invasive signal.

---

> **GOING DEEPER: Why Physicists Love the Hamiltonian**
>
> The Hamiltonian was introduced by William Rowan Hamilton in the 1830s as a way of
> rewriting Newton's equations in a more elegant form. What Hamilton discovered is that
> the trajectory of any physical system — the path it takes through its state space over
> time — can be derived entirely from a single scalar function $H$. You do not need to
> describe all the forces. You just need the energy landscape, and the dynamics follows.
>
> In quantum mechanics, the Hamiltonian operator $\hat{H}$ plays the same role: it
> determines how a quantum state evolves over time through Schrödinger's equation,
> $i\hbar\,\partial_t\psi = \hat{H}\psi$. The eigenvalues of $\hat{H}$ are the
> allowed energy levels.
>
> In the Soma-Field Model, $H(\mathbf{e})$ is neither Newtonian nor quantum: it is the
> Hamiltonian of a classical stochastic system (a Langevin system), where the dynamics
> is gradient descent with noise. But the mathematical structure — a scalar energy
> function that determines everything else — is identical.
>
> This is not a coincidence. It is because "a system has stable states to which it
> returns" is a very general physical principle, and the Hamiltonian is the most general
> way to formalise it.

---

## 3.4 The Coupling Matrix

The matrix $W$ — the coupling matrix — is the central object of the model. It encodes
the emotional architecture of a nervous system: which modes excite each other, which
inhibit each other, how strongly, and in which direction.

For a neurotypical, regulated nervous system, $W$ has a specific mathematical property:
it is *symmetric*. $W_{ij} = W_{ji}$: the influence of mode $i$ on mode $j$ equals the
influence of mode $j$ on mode $i$. This symmetry is not incidental. It is what guarantees
the existence of an energy function: if $W$ is not symmetric, the dynamics cannot be
written as gradient descent, and the system may not have stable fixed points at all.
It may cycle indefinitely.

Trauma, in this model, is a modification of $W$ that breaks this symmetry. A traumatised
nervous system has couplings that do not balance: fear activates shame more strongly than
shame activates fear; hypervigilance activates the freeze response more readily than
the freeze response resolves back to hypervigilance. The asymmetric couplings create
directional flows in the landscape — attractors that are easy to fall into and hard to
climb out of.

This is the formal basis of the clinical observation that trauma often feels like a
one-way ratchet.

---

> **KEY TERMS**
>
> **Attractor** — a stable state in the energy landscape; a valley that the field rolls
> toward from nearby positions.
>
> **Basin of attraction** — the region of state space from which the system flows toward
> a given attractor.
>
> **Hamiltonian** — the energy function $H(\mathbf{e})$ that organises the dynamics; the
> mathematical description of the landscape.
>
> **Coupling matrix $W$** — the matrix encoding the interactions between emotional modes;
> shapes the landscape by determining which states lower the energy.
>
> **Threshold $\theta_i$** — the individual bias of emotional mode $i$; shifts its
> natural resting level.

---

> **CHAPTER SUMMARY**
>
> Emotional states are points in a landscape shaped by the Hamiltonian $H$. Attractors
> are stable states (valley bottoms); basins of attraction are the regions from which the
> system rolls toward each attractor. The dynamics — gradient descent with noise — always
> moves toward lower energy. The coupling matrix $W$ encodes the interactions that shape
> the landscape. Symmetry of $W$ guarantees stable attractors; asymmetry (introduced by
> trauma) creates directional flows that are hard to reverse.

---

![Figure 3.3. 1D energy cross-section along a principal axis of the landscape. The height of each barrier between basins determines transition probability: a deep Freeze well with a high approach barrier (right) requires substantial energy input to escape — corresponding clinically to a freeze response that does not self-resolve without intervention. Barrier asymmetry (left-to-right ≠ right-to-left) is the signature of trauma modification. *Author's original figure.*](figures/fig3b_energy_profile.png){width=90%}

---

\newpage

# PART II: HOW THE FIELD CHANGES

---

\newpage

# Chapter 4: The Weight on the Field

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   "The question is not why the behaviour persists,              │
  │    but what it was optimised for."                              │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **LEARNING OBJECTIVES**
>
> By the end of this chapter, you will understand:
>
> - What the C-PTSD operator is and how it modifies the field
> - Why hypervigilance is not an error but an optimisation
> - What "the landscape has changed" means precisely
> - The difference between a perturbation and a structural modification

---

## 4.1 The Modification

Complex PTSD (C-PTSD) is distinguished from single-incident PTSD by the presence of
repeated, prolonged, or developmental trauma — particularly trauma that occurred in
relationships on which the person depended for survival. The result is not a discrete
memory that can be "processed" and resolved. It is a pervasive reorganisation of the
emotional field architecture: a new landscape, not a scar on an old one.

In the Soma-Field Model, C-PTSD is represented as a modification of the coupling matrix:

$$W_{\text{C-PTSD}} = W_0 + \Delta W_{\text{trauma}}$$

where $W_0$ is the baseline coupling matrix and $\Delta W_{\text{trauma}}$ is the
modification — an asymmetric additive term that reshapes the landscape. Crucially,
$\Delta W_{\text{trauma}}$ is not symmetric: it introduces directional flows. Certain
states become easy to fall into and hard to leave. Others become difficult to access
from the modified landscape even though they exist.

This can be visualised as a landscape that has been tilted and deformed: new deep valleys
in places that were not attractors before, old deep valleys raised, and the topology of
connectivity between states changed.

![Figure 4.1. Four neurotype landscapes (1D cross-section). *Typical* (upper left): a deep wide Calm basin with accessible secondary states. *C-PTSD* (lower left): Calm shallowed and narrowed, Freeze dominant — the resting state shifts toward high-vigilance. *ADHD* (upper right): all basins flattened, low barriers, rapid transitions — high-temperature dynamics. *ASD* (lower right): narrow steep wells with high barriers between states — strong attractor stability, low noise tolerance, high cost of transitions. *Author's original figure.*](figures/fig5_neurotype_landscapes.png){width=95%}

## 4.2 Why Hypervigilance Is an Optimisation

A nervous system that has adapted to an environment of chronic threat has correctly
learned that:

1. Danger is frequent and unpredictable.
2. The cost of missing a threat is very high.
3. The cost of false alarms is low (relative to the cost of missing a real threat).

Given these parameters, the optimal configuration is exactly what we see in C-PTSD: a
bias toward high vigilance, a wide definition of "potential threat," a fast-responding
sympathetic system, and a slow-to-settle calm state. The hypervigilance attractor is
deep because a deep attractor is appropriate to the environment it was optimised for.

The modification is not an error. It is a correct solution to the wrong problem — where
"the wrong problem" means the original environment, which no longer exists (or no longer
exists in the same form).

This reframing is not merely philosophical. It changes the clinical question from
"how do we extinguish the hypervigilance response" to "how do we update the landscape
to incorporate evidence that the current environment is different." These are very
different operations, with very different implications for what kind of therapeutic
intervention is useful.

## 4.3 Thresholds and Consciousness

There is a parameter in the model that has not yet been introduced, and it does a great
deal of work. This is the **threshold** $T$ — denoted with the capital $T$ that recurs
throughout this book.

The threshold is a level of field activation above which an emotional state becomes
conscious experience — enters awareness as a felt emotion — rather than remaining as
sub-threshold somatic activation. Below $T$, the field is active but not felt; the
activation is present in the body, influencing behaviour and physiology, but not
represented in consciousness.

This has immediate clinical consequences. A person with a very high threshold $T$ may
have a strongly activated soma-field — may be physiologically in a fear state, with all
the somatic correlates — while experiencing nothing that they would call fear. The
activation is real. The consciousness of it is absent. Somatic therapy, interoceptive
training, and bodywork all operate, in part, by lowering $T$: bringing below-threshold
somatic content into awareness.

A person with a very low threshold $T$ experiences the opposite: everything is felt,
amplified, present. This is associated with high interoceptive sensitivity, certain
presentations of anxiety, and some forms of neurodivergence.

The threshold is where the physics and the clinical presentation most visibly connect.

---

> **AUTHOR'S NOTE: The Landscape I Inherited**
>
> There is a version of this chapter that is abstract: modifications to coupling matrices,
> reshaping of landscapes, asymmetric $W$. And then there is the version that is what
> it feels like to live in a modified landscape.
>
> What it feels like is this: calm is always provisional. Not shallow, exactly —
> but unsecured. Like a surface that holds weight when you step carefully but gives way
> if you shift too quickly. Alert is never far away. And underneath alert, the freeze
> state is a gravity well that does not announce itself before you are already in it.
>
> The modification in my case is not a perturbation on a pre-existing normal landscape.
> That would require a $W_0$ to perturb. The timeline does not allow for that. That is
> the subject of Chapter 6.

---

> **KEY TERMS**
>
> **C-PTSD operator** — the modification $\Delta W$ to the coupling matrix that reshapes
> the energy landscape; the mathematical representation of the effect of complex trauma.
>
> **Threshold $T$** — the activation level above which a soma-field state becomes
> conscious experience. The central parameter distinguishing felt emotion from
> sub-threshold somatic activation.
>
> **Hypervigilance attractor** — the deep stability basin in the modified landscape
> corresponding to high-arousal, high-alert states.

---

![Figure 4.2. The perception threshold T. Mode i (grey) oscillates continuously but never crosses T — it is sub-perceptual, influencing behaviour and physiology without entering felt experience. Mode j (blue) rises through T and becomes a consciously felt emotion. The threshold is the key parameter that distinguishes somatic activation from emotional awareness; its value varies across individuals and can be modified by interoceptive practice, arousal level, and therapeutic work. *Author's original figure.*](figures/fig2_threshold.png){width=90%}

---

\newpage

# Chapter 5: Memory Written in the Body

---

> **LEARNING OBJECTIVES**
>
> By the end of this chapter, you will understand:
>
> - The difference between narrative memory and somatic memory
> - What the memory kernel is and what it does to the field dynamics
> - Why trauma memory persists — and why some trauma memories persist much longer
> - What therapeutic processing means in terms of the memory kernel

---

## 5.1 Two Kinds of Memory

When you remember a conversation from last week, you are using **episodic memory** — the
explicit, narrative record of events that occurred at specific times and places. Episodic
memory is context-dependent, verbally expressible, and subject to conscious recall and
revision. It is stored primarily in the hippocampus.

When you flinch at a sound that resembles the sound that preceded something terrible, you
are using **procedural** or **somatic memory** — a form of memory that is not stored as
narrative but as pattern: as a configured readiness in the body to respond in a particular
way to particular signals. Somatic memory is not verbally expressible (you cannot "tell
the story" of a procedural response; you can only notice it happening). It does not
require conscious recall — it is not a replay of an event but an embodied preparation.
It is stored across the body: in muscle tone, in the brainstem, in the autonomic nervous
system, in the way sensory signals are gated before they reach cortical processing.

Trauma creates primarily somatic memory. This is why it is not resolved by talking about
it. The body has stored information in a form that language does not reach.

## 5.2 The Memory Kernel

In the Soma-Field Model, the effect of past activation on present dynamics is captured
by a **memory kernel** $K(\tau)$. This is a function that says: an activation of the
field $\tau$ time units ago continues to influence the field now, with a weight
proportional to $K(\tau)$.

For C-PTSD, the memory kernel takes the form:

$$K_{\text{trauma}}(\tau) = \sum_k A_k\, e^{-|\tau|/\tau_k}$$

This is a sum of decaying exponentials. Each term represents a distinct trauma trace:
$A_k$ is the amplitude (how strongly the trace affects the current field) and $\tau_k$
is the decay time (how long the trace persists before fading).

```
  REGULATED: No significant memory kernel
  ┌─────────────────────────────────────────────────────────────┐
  │  Field  ▲                                                   │
  │  activ. │      ╭──╮                                         │
  │         │      │  │   (episode resolves; field returns       │
  │         │  ────╯  ╰─────────────────────────────────────   │
  │         │                              baseline              │
  │         └──────────────────────────────────────────────→    │
  │                            time                             │
  └─────────────────────────────────────────────────────────────┘

  C-PTSD: Significant memory kernel — traces persist
  ┌─────────────────────────────────────────────────────────────┐
  │  Field  ▲                                                   │
  │  activ. │      ╭──╮                    ╭──╮                 │
  │         │      │  ╰─╮    ╭──╮      ╭───╯  ╰─╮              │
  │         │  ────╯    ╰────╯  ╰──────╯         ╰──────       │
  │         │                                                   │
  │         └──────────────────────────────────────────────→    │
  │                            time                             │
  │  Baseline elevated; episodes bleed into one another;        │
  │  field rarely returns to original rest level                │
  └─────────────────────────────────────────────────────────────┘

  Figure 5.1. The effect of the trauma memory kernel on field dynamics. In a regulated
  system (top), a field activation episode resolves and the field returns to a low
  resting level. In the C-PTSD-modified system (bottom), the memory kernel elevates
  the baseline between episodes, so that subsequent episodes begin from a higher resting
  activation. Over time, the field cycles at an elevated level without returning to rest.
```

## 5.3 Why Early Traces Persist

The decay time $\tau_k$ is central: it determines how long a trace remains active.

For trauma that occurs early in development — before language, before narrative memory
capacity — the decay time tends to be much longer. There are two reasons.

First, **somatic memory has no verbal layer**. For trauma occurring after language
develops, the episodic and somatic memories co-encode: the narrative version partially
"covers" the somatic trace, providing a context that can be accessed verbally. Verbal
processing in therapy can then shorten the effective lifetime of the trace. For pre-verbal
trauma, the somatic trace has no narrative companion. It cannot be reached by talking.
The decay time is governed by purely somatic processes, which are much slower.

Second, **the trace cannot be separated from the structure**. For pre-verbal trauma,
the memory is not a modification of an already-formed architecture. The architecture
itself was shaped by the conditions of the traumatic period. This is addressed more
formally in Chapter 6.

## 5.4 What Therapy Does

In the language of the memory kernel, effective somatic therapy does two things:

1. It reduces the amplitudes $A_k$: the traces continue to influence the field, but
   with less force. Activation episodes are smaller and resolve more completely.

2. It increases the decay times $\tau_k$: the traces fade more quickly after episodes.
   The field returns to rest more rapidly.

The goal is not to eliminate the traces — the nervous system cannot un-learn an
experience, and attempting to make it do so is not the right model. The goal is to
reduce their influence to a level that allows the field to return to rest between
episodes: to restore the gap between activations in which recovery occurs.

---

> **GOING DEEPER: The Memory Kernel and the QFT Propagator**
>
> This may seem like a digression, but it is one of the most striking features of the
> model. The memory kernel for C-PTSD — $K(\tau) = \sum_k A_k e^{-|\tau|/\tau_k}$ —
> is mathematically identical to the **Euclidean propagator** in quantum field theory.
>
> In QFT, the Euclidean propagator $G_E(\tau)$ describes how a disturbance in a quantum
> field at time $0$ correlates with the field at time $\tau$:
>
> $$G_E(\tau) = \langle \phi(0)\,\phi(\tau) \rangle = \frac{1}{2m}\, e^{-m|\tau|}$$
>
> The mass $m$ of the QFT particle corresponds to $1/\tau_k$ in the memory kernel. A
> heavier particle creates a shorter-range propagator; a shorter-lived trauma trace
> has a larger $1/\tau_k$ (i.e., smaller $\tau_k$, faster decay).
>
> This identity is not an analogy. The two expressions are the same function with
> different names for the parameters. The Wick rotation — the substitution
> $t \to -i\tau$ that takes quantum mechanics into statistical mechanics — is the
> formal bridge between them, and it is the subject of Chapter 7.

---

> **KEY TERMS**
>
> **Episodic memory** — explicit, narrative memory of events at specific times and places;
> accessible to conscious recall and verbal expression.
>
> **Somatic (procedural) memory** — embodied memory stored as configured physiological
> readiness; not verbally expressible; activated by sensory signals that match the
> original encoding context.
>
> **Memory kernel $K(\tau)$** — the function describing how field activations at time
> $\tau$ in the past continue to influence the current field state.
>
> **Amplitude $A_k$** — the strength of a trauma trace's influence on the current field.
>
> **Decay time $\tau_k$** — the timescale over which a trauma trace fades after
> activation; how long the echo persists.

---

\newpage

# Chapter 6: How Early Is Early?

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   "Before language, there is only the body."                   │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **LEARNING OBJECTIVES**
>
> By the end of this chapter, you will understand:
>
> - Why the age at which trauma occurred matters to its character
> - What happens to the structure of the soma-field when modification occurs
>   before language develops
> - Why "returning to the pre-trauma self" is a coherent goal for late trauma but
>   not for pre-verbal trauma
> - What "forward transformation" means as a mathematical and clinical concept

---

## 6.1 Developmental Time

Children are not small adults. The nervous system develops in stages, and each stage
has different capacities — for encoding, for integration, for language, for explicit
memory. What a three-year-old can do with an overwhelming experience is not what a
ten-year-old can do, and neither is what an adult can do.

This is relevant to trauma because the *character* of a traumatic modification depends
on the developmental stage at which it occurs. Not the severity — severity is a separate
question. The character. What structures are modified, how the modification is stored,
and what it is even possible to change about it afterward.

The key developmental milestone for this model is the onset of reliable verbal encoding
capacity — the ability to store experiences with a narrative, linguistic representation
alongside the somatic one. This typically emerges between approximately 24 and 48 months
of age, with considerable individual variation. We use $\tau_c \approx 36$ months as
an approximate threshold.

The parameter $\tau_d$ — **developmental age at trauma** — is the age at which the
primary modification occurred.

## 6.2 Below the Threshold: Pre-Verbal Trauma

For $\tau_d < \tau_c$ (pre-verbal trauma), several things are different from the
late-trauma case.

**The structure was formed under the modification.** A nervous system that is being
organised — that is still forming its basic coupling architecture — under conditions of
unresolved physiological threat does not develop and then get modified. It develops
*as* modified. The asymmetric couplings, the elevated vigilance attractor, the memory
kernel coefficients — these are not perturbations on a pre-existing baseline. They
are the baseline.

**There is no prior self to recover.** For trauma occurring after the baseline
architecture is formed ($\tau_d > \tau_c$), there is a counterfactual: the person that
would have developed without the traumatic modification. This counterfactual is
partially encoded — in early memories, in narrative, in the patterns of functioning
before the event. Therapeutic language of "returning to yourself" or "recovering the
pre-trauma self" is coherent in this case: the target exists.

For pre-verbal trauma ($\tau_d < \tau_c$), the counterfactual does not exist as an
encoded state. There was no formed nervous system that then got modified. The
self-before-trauma never developed. There is nowhere to return to.

This is not a pessimistic statement. It is a precise one. And precision here matters
because it changes the therapeutic question.

## 6.3 The Interpolation

The coupling matrix for a traumatised nervous system can be written as a function of
developmental age:

$$W(\tau_d) = f(\tau_d)\cdot W_0 + \bigl(1 - f(\tau_d)\bigr)\cdot W_{\text{trauma}}$$

where $f$ is a smooth interpolation function:

$$f(\tau_d) = \tanh\!\left(\frac{\tau_d}{\tau_c}\right)$$

```
  STRUCTURAL FRACTION f(τ_d) = tanh(τ_d / τ_c)
  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  f(τ_d) ▲  1.0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╭──────────     │
  │  (how    │                               ╭─────╯              │
  │  much    │                         ╭────╯                     │
  │  is W₀)  │  0.76 ─ ─ ─ ─ ─ ─ ─ ─ ─╯  ← f(τ_c) = tanh(1)    │
  │          │                        ↑                           │
  │          │  0.5 ─ ─ ─ ─ ─ ─ ─ ╭──╯                           │
  │          │                 ╭──╯                               │
  │          │             ╭──╯                                   │
  │          │         ╭──╯                                       │
  │          │  0.0 ───╯                                          │
  │          └──────────────────────────────────────────────────→ │
  │           0    τ_c/2  τ_c    2τ_c    3τ_c      τ_d (months)  │
  │                       (36)                                     │
  │                                                                │
  │  Left of τ_c:  W is mostly W_trauma — structural             │
  │  Right of τ_c: W is mostly W₀ — perturbative                 │
  └──────────────────────────────────────────────────────────────────┘

  Figure 6.1. The structural fraction f(τ_d). This function describes what proportion
  of the coupling matrix is neurotypical baseline (W₀) versus trauma-formed (W_trauma),
  as a function of developmental age at trauma. At τ_d = 0 (birth or in utero), the
  coupling is entirely trauma-formed: f = 0. At τ_d = τ_c ≈ 36 months, f ≈ 0.76:
  the baseline accounts for about three-quarters of the coupling. The interpolation is
  smooth: there is no sharp cutoff, just a continuous change in character.
```

At $\tau_d = 0$: $f = 0$ and $W = W_{\text{trauma}}$. There is no baseline component.

At $\tau_d = \tau_c$: $f = \tanh(1) \approx 0.76$. The baseline accounts for 76% of
the coupling; the modification is 24%.

At large $\tau_d$: $f \to 1$ and $W \approx W_0$. The modification is a small
perturbation on a fully formed baseline.

The therapeutic implication of this formula is significant. For $\tau_d \ll \tau_c$:
the operation $W \to W_0$ — extracting the baseline from the current coupling — is not
defined. The $W_0$ was never the dominant component. It cannot be recovered because it
was not formed.

## 6.4 Forward Transformation

What *is* possible, for pre-verbal trauma, is a **forward transformation**: the
construction of a new coupling matrix $W'$ that has desirable properties — wider
window of tolerance, shallower hypervigilance attractor, lower memory kernel amplitudes,
greater capacity for social engagement — without that new matrix being a recovery of a
prior state.

This is a different target, and it requires a different process:

- Not excavating the past for the lost self, but building forward
- Not reducing to a baseline that didn't form, but constructing a landscape that works
- Not recovery ($W \to W_0$, undefined), but transformation ($W \to W'$, unconstrained)

The route to $W'$ uses the same therapeutic tools — somatic therapy, relational repair,
interoceptive training, bodywork — but with a different intention. The intention is not
to return somewhere but to arrive somewhere for the first time.

---

> **AUTHOR'S NOTE: $\tau_d$ = 18 Months**
>
> My developmental age at trauma: $\tau_d \approx 18$ months. Approximately half of
> $\tau_c$.
>
> At that age, the structural fraction is approximately $f(18/36) = \tanh(0.5) \approx
> 0.46$. Slightly less than half of the coupling matrix was neurotypical baseline at the
> time. More than half was trauma-formed. As the trauma continued over three months
> of hospitalisation — developmental ages 18 to 21 months — the modification was
> present throughout the period when the coupling architecture was being most actively
> organised.
>
> There is no version of me that existed before this modification and then got
> modified. The preVerbalIsStructural theorem, which is in Appendix B, is a formal
> proof of the clinical fact that has taken decades of therapy to find words for:
> *there is nowhere to return to, and that is not a tragedy, it is simply the correct
> topography*.
>
> The voyage is forward. This book is part of it.

---

> **GOING DEEPER: The preVerbalIsStructural Theorem**
>
> The following is a proof sketch in Lean 4, a proof assistant that requires
> mathematical arguments to be written in a form that a computer can verify.
> A `sorry` marks a step that is stated but not fully proved — an open obligation.
>
> ```lean
> -- Key theorem: for pre-verbal trauma, no neurotypical W₀ can be
> -- recovered by subtraction from the current coupling matrix
> theorem preVerbalIsStructural {n : ℕ} (profile : TraumaProfile n)
>     (h : profile.τ_d < τ_c) :
>     structuralFraction profile.τ_d < Real.tanh 1 := by
>   unfold structuralFraction
>   apply Real.tanh_lt_tanh
>   exact div_lt_one_of_lt h (by norm_num)
> ```
>
> This theorem states: for any TraumaProfile with developmental age below $\tau_c$,
> the neurotypical structural fraction is below $\tanh(1) \approx 0.76$. More than
> 24% of the coupling matrix is trauma-formed, not baseline-formed. At $\tau_d = 0$,
> 100% is trauma-formed.
>
> **Corollary** (commented in the code): the therapeutic operation for pre-verbal trauma
> is forward transformation ($W \to W'$), not recovery ($W \to W_0$). The second
> operation is undefined because $W_0$ was never the dominant component.

---

> **KEY TERMS**
>
> **Developmental age at trauma ($\tau_d$)** — the age, in months, at which the primary
> traumatic modification occurred.
>
> **Verbal encoding threshold ($\tau_c$)** — the approximate developmental age (≈36
> months) at which reliable narrative memory and verbal encoding capacity emerges.
>
> **Structural fraction $f(\tau_d)$** — the proportion of the coupling matrix attributable
> to neurotypical baseline development; interpolated smoothly from 0 (purely structural
> modification) to 1 (purely perturbative modification).
>
> **Forward transformation** — the therapeutic goal for pre-verbal trauma: constructing a
> new coupling matrix $W'$ with wider attractor topology, rather than recovering a
> baseline that was not fully formed.

---

\newpage

# Interlude: A Voyage to the Alps

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   "Everything floats: the universe, the mountains, the body.   │
  │    The question is only what it is floating in."               │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

There is a campsite in the Klöntal valley, in the canton of Glarus, Switzerland, that I
have been returning to for many years. I promised to write a book about it. This is the
closest I have managed — and as it turns out, the campsite book and the soma-field book
are the same book.

The Klöntal sits in a glacially carved valley a few kilometres from the town of Glarus,
adjacent to the Swiss Tectonic Arena Sardona — a UNESCO World Heritage Site containing
some of the most famous and legible tectonic structures in the world. The valley walls
are parabolic: shaped by ice over millions of years into the form that an engineer would
choose if they wanted to focus sound. Stand at one end and speak quietly, and the words
arrive at the other end with startling clarity. The valley is a natural resonator:
limestone and dolomite walls, near-perfect parabolic geometry, and an acoustic character
that makes sound oscillate long after the source has fallen silent.

```
  PARABOLIC VALLEY CROSS-SECTION

    valley rim                    valley rim
    (limestone)                   (limestone)
          ╲    ~   ~   ~   ~   ~   ╱
           ╲  ~               ~  ╱   ← sound reflects from walls
            ╲ ~  → source ←  ~ ╱
             ╲~               ~╱
              ╲ ~  converge  ~╱
               ────────────────
                  valley floor

  A parabolic cross-section focuses incoming sound to the focal region.
  The same geometry governs satellite dishes, reflector telescopes, and
  the resonant cavities of musical instruments. Mountain valleys with this
  profile produce exceptional acoustics — sound oscillates long after the
  source goes quiet.
```

The valley's acoustic behaviour is the physical intuition behind the soma-field wave
description. The emotional field has modes — preferred patterns of activation, like
standing waves in a resonant cavity — that continue to oscillate after the activating
event has passed. The memory kernel $K(\tau)$ is the body's version of the valley's
echo: not a recording, but a resonance that continues to shape what comes next.

## Everything Floats

Geology teaches, and physics confirms, that everything floats.

At the **cosmological scale**: galaxies float in the curved spacetime that mass creates.
The Milky Way is moving toward the Virgo Supercluster at approximately one million
kilometres per hour — not through a fixed background, but on the spacetime manifold
itself. There is no fixed frame. The background is the field.

At the **geological scale**: continents float on the asthenosphere, the semi-molten
layer beneath the rigid lithosphere. The Alps exist because the African plate has been
moving north at 2–3 centimetres per year for approximately 50 million years, crumpling
the sediments of the ancient Tethys Sea into the mountains visible from the valley floor.
The same forces are operating now, invisibly, at the speed of growing fingernails.

At the **somatic scale**: the emotional field floats in the Hamiltonian landscape —
moving toward attractors, drawn by the energy gradient, oscillating around stable states,
occasionally crossing a phase boundary into a new basin.

One equation governs all three:

$$\ddot{x} = -\nabla V(x) + F_{\text{ext}}$$

A galaxy, a tectonic plate, a nervous system: all governed by gradient descent on a
potential with external forcing. The scales span 25 orders of magnitude. The structure
does not vary.

## Reading the Mountain

The Glarus Thrust (Glarner Hauptüberschiebung) is the tectonic feature that makes this
region a UNESCO World Heritage Site. It is a thrust fault on which an enormous slab of
Verrucano sandstone (Permian, approximately 250 million years old) was transported
roughly 35 kilometres northward over much younger Flysch sediment (Eocene, approximately
40 million years old). The old sits on top of the new. The contact is visible across many
mountain faces as a near-horizontal line: above it, ancient red sandstone; below it,
young grey sediment.

```
  GLARUS THRUST: SCHEMATIC CROSS-SECTION (not to scale)

  Surface  ════════════════════════════════════════════════════
           │  VERRUCANO  (~250 Ma, Permian)                   │
           │  Ancient red sandstone                           │
           │  Formed long before the Alps existed             │
  ─ ─ ─ ─ ├══════════════ THRUST CONTACT ═══════════════════╤╡ ← THE LINE
           │  FLYSCH  (~40 Ma, Eocene)                       │ │
           │  Young grey marine sediment                     │ │
           │  Floor of the ancient Tethys Sea                │ │
  Base     ═════════════════════════════════════════════════╧══

  Direction of transport: ~35 km northward.
  The ancient slab (~250 Ma) was carried over the young sediment (~40 Ma).
  Read a single mountain face: 210 million years of geological history,
  visible in one glance. This is 4D geology — space encodes time.
```

A geological cross-section is four-dimensional: horizontal position records geography,
but vertical position records time. Deep is old; shallow is recent. To read a mountain
face is to read the history of the forces that shaped it — compression, burial,
metamorphism, uplift, erosion — all preserved in the mineral record.

The soma-field coupling matrix $W$ is four-dimensional in the same sense. The current
configuration encodes the accumulated history of all the forces that shaped it. The
asymmetries in $W$ are the thrust faults of the emotional landscape: places where an
ancient force has pushed its structure over something newer, and the contact is still
legible if you know how to read it.

For pre-verbal trauma at $\tau_d \approx 18$ months: the Verrucano is very old, very
deep in the developmental history, and emphatically on top.

## M-Theory: Everything Floats in More Dimensions

M-theory, the current best candidate for a unified theory of physics, proposes that the
universe is a *brane* — a membrane — floating in an 11-dimensional space. Our familiar
four dimensions are a surface in a higher-dimensional structure. The other seven
dimensions are curled too small to observe directly, but they leave measurable signatures
in the physics of the accessible four.

The soma-field is not M-theoretic in any technical sense. But the intuition scales: the
emotional field is a field on the brane of the body, and what we observe — threshold
crossings, attractor dynamics, memory kernel echoes — are projections of a structure
that extends into dimensions not directly accessible to ordinary awareness.

The pre-verbal, the sub-threshold, the procedural — somatic content that drives
behaviour without entering conscious experience — is the body's version of the curled
dimensions: real, causally active, not directly observable. Interoceptive practice is
the project of unfolding them: making accessible what was previously curled below $T$.

## The Valley at Dusk

I use Phase Plant, a modular synthesizer, to work with acoustic field recordings —
routing them through resonant filter banks, mapping the frequencies that a resonant
space prefers, listening for the modes that survive decay while others fall away. It is
an unconventional approach to acoustics. But it is physics: finding the eigenfrequencies
of a resonant cavity by attending to what persists.

The Klöntal valley has such frequencies. When the sun drops behind the peaks and the
daytime noise subsides, what remains is the valley's own voice: a low, slow resonance
in the limestone, carrying the frequencies that the parabolic geometry selects.

The emotional field has equivalent preferred frequencies. The trauma memory kernel
$K(\tau) = \sum_k A_k e^{-|\tau|/\tau_k}$ encodes them: the values $1/\tau_k$ are the
field's natural resonance rates, the $A_k$ their amplitudes. Therapeutic work — reducing
$A_k$, lengthening $\tau_k$ — is the project of quieting the modes excited by the
original event until the field returns to its ground state.

In the valley at dusk, this is not a metaphor. It is audible.

---

\newpage

# PART III: THE PHYSICS UNDERNEATH

---

\newpage
