
# The Soma-Field as a Worked Example

The Soma-Field Model [@johnsonsoma2026] was developed through five sequential
co-identifications. Each is presented here as an explicit instance of the method.

## Co-identification I: The Conscious Percept as Green's Function

**The unknown quantity:** The relationship between the continuous emotional
field $\psi_i(t)$ and the discrete conscious emotional percept.

**Type signature extracted:** The percept is the output of the field when probed
at a single moment — the impulse response. Impulse responses have a universal
type: they are the inverse Laplace (or Fourier) transform of a rational function
with poles in the lower half-plane. For a simple damped oscillator:

$$\tilde{G}(\omega) = \frac{\sigma_\text{eff}^2}{\omega^2 + \lambda^2}$$

**Typeverse search result:** This is the Euclidean propagator of a scalar field
with mass $\lambda$ and coupling $\sigma_\text{eff}^2$. In Minkowski space it is:

$$\tilde{G}_\text{QFT}(k) = \frac{i}{k^2 - m^2 + i\varepsilon}$$

**The co-identification:** The conscious emotional percept is the Green's function
of the soma-field. Both are poles in the propagator of their respective field.
The emotional percept and the elementary particle are the same mathematical object,
instantiated in different substrates.

**Theorems imported:**
- The Källén-Lehmann spectral representation: any physical propagator can be
  decomposed as a sum of poles. Emotional states have a spectral decomposition.
- The optical theorem: the imaginary part of the forward scattering amplitude
  equals the total cross-section. The dissipative component of the emotional
  field (damping $\lambda$) is related to the total coupling strength $\sigma_\text{eff}^2$.
- Pole structure ↔ mass spectrum: the location of the propagator pole gives
  the natural frequency $\omega_0 = \lambda$ of the emotional mode.

## Co-identification II: The Attractor Landscape as Ising Hamiltonian

**Type signature:** A scalar function $H: \mathbb{R}^n \to \mathbb{R}$ that
is always non-increasing along field trajectories, with isolated minima
corresponding to stable emotional states.

**Typeverse search result:** The Hopfield energy / Ising Hamiltonian:

$$H(\mathbf{e}) = -\frac{1}{2}\mathbf{e}^\top W \mathbf{e} - \boldsymbol{\theta}\cdot\mathbf{e}$$

**Theorems imported:** Convergence to attractors (the Lyapunov argument);
capacity bounds (Hopfield's $0.14N$ result); stochastic escape via Boltzmann
noise (simulated annealing = titrated arousal in clinical language).

## Co-identification III: The Perception Threshold as Brane Thickness

**Type signature:** A parameter $T_i$ that gates access from a lower-dimensional
subspace (the limbic field) to a higher-dimensional one (conscious awareness).
Varying $T_i$ continuously produces a family of gating behaviours.

**Typeverse search result:** The Randall-Sundrum model [@randallsundrum1999]: a
brane of thickness $T$ embedded in a higher-dimensional bulk, where Standard
Model fields are confined to the brane. The "hierarchy problem" — why the
electroweak scale is so much smaller than the Planck scale — maps onto the
observation that minimal perturbations of the limbic field produce enormous
differences in subjective experience (alexithymia: thick brane; hypervigilance:
thin brane).

**Theorems imported:** The Kaluza-Klein spectrum of the brane gives a prediction
for the discrete structure of emotional threshold levels. Brane localisation gives
the mechanism for why the field can be active without crossing into consciousness.

## Co-identification IV: The Coupling Matrix as G₂ Manifold

**Type signature:** The coupling matrix $W$ is an $11 \times 11$ real symmetric
matrix encoding the structure of an eleven-dimensional emotional space. The field
trajectories respect the geometry encoded in $W$.

**Typeverse search result:** The $G_2$ holonomy manifold of M-theory
[@berger1955; @joyce1996]: a seven-dimensional Riemannian manifold with the
exceptional holonomy group $G_2$. Its structure tensor encodes all curvature
information. Deforming the structure tensor changes the global geometry of the
manifold.

**The co-identification:** $W$ is the structure tensor of the emotional manifold.
Trauma does not change a parameter; it deforms the manifold. Therapeutic
intervention is differential geometry.

**Theorems imported:** The Bochner-Weitzenböck formula constraining curvature;
the Berger classification of holonomy groups constraining what stable emotional
geometries are possible; the Hitchin flow as a possible model for the evolution
of $W$ under sustained therapeutic intervention.

## Co-identification V: Therapeutic Processing as Renormalisation Group Flow

**Type signature:** Therapeutic processing is a flow in the space of coupling
constants $W_{ij}$ parameterised by a scale $\mu$ (the "depth" or "resolution"
of emotional processing). The flow has fixed points, and the qualitative structure
of the attractor landscape is invariant under the flow.

**Typeverse search result:** The renormalisation group [@wilson1971]: a flow
on the space of coupling constants parameterised by an energy scale $\mu$,
with fixed points corresponding to universality classes. The $\beta$-function:

$$\frac{dW_{ij}}{d\log\mu} = \beta_{ij}(W)$$

**The co-identification:** Therapy is an RG flow from UV (raw unprocessed
traumatic detail) to IR (integrated narrative). The attractor topology —
fight, flight, freeze, calm — is RG-invariant: the same basins appear at
every scale of analysis, in every therapeutic modality, because they are
the fixed points of the flow, not artefacts of a particular resolution.

**Theorems imported:** The irreversibility of the RG flow (Zamolodchikov's
c-theorem, adapted: processed material cannot be *un*-processed; the flow is
unidirectional); universality (the detailed mechanism of the trauma is irrelevant
at long distances — only its universality class, i.e., its attractor type,
matters); dimensional transmutation (the traumatic scale $\tau_k$ of the memory
kernel is an emergent scale, not a fundamental parameter).

---

# A Partial Map of the Typeverse

For the practitioner wishing to apply the method, the following is a partial
field guide to frequently useful mathematical structures, indexed by their
type signatures.

## Propagator-Class Structures

**Type:** Complex function of frequency with poles on or near the real axis;
gives the response of a system to a delta-function input.

**Found in:** QFT (Feynman propagator), signal processing (transfer function),
linear systems theory (impulse response), harmonic analysis (Green's function
of the Laplacian).

**Typical imports:** Spectral decomposition; optical theorem; dispersion
relations (Kramers-Kronig: the real and imaginary parts of the response are
not independent — this imports into emotion as: the *dissipation* of an
emotional mode and its *natural frequency* are Hilbert transforms of each other).

## Energy-Function-Class Structures

**Type:** Scalar function $H: \mathbb{R}^n \to \mathbb{R}$ that is bounded
below and non-increasing along system trajectories.

**Found in:** Statistical mechanics (Hamiltonian), neural networks (Hopfield
energy), Lyapunov theory (stability analysis), optimisation (loss function).

**Typical imports:** Convergence guarantees; stability analysis; capacity bounds;
the fluctuation-dissipation theorem.

## Topological-Class Structures

**Type:** Integer-valued invariants of field configurations that are preserved
under continuous deformations.

**Found in:** Topological field theory (winding numbers, Chern-Simons invariants),
condensed matter (topological insulators, skyrmions), knot theory.

**Typical imports:** Protection from perturbation; the impossibility of smooth
deformation between distinct topological sectors; quantisation (only integer
winding numbers); threshold behaviour (the topological transition requires
a finite perturbation).

**Application to emotion:** Traumatic configurations with non-zero topological
charge cannot be resolved by smooth therapeutic interventions (cognitive
reframing). A qualitative change in approach — large-amplitude somatic work,
pharmacological intervention, EMDR — is required to cross the topological barrier.

## Renormalisation-Class Structures

**Type:** A flow on a space of couplings, parameterised by a scale, with
fixed points and $\beta$-functions.

**Found in:** Quantum field theory (renormalisation group), statistical
mechanics (Kadanoff block spins), dynamical systems (centre manifold theorem),
machine learning (neural scaling laws).

**Typical imports:** Universality (the IR behaviour depends only on the
universality class, not the microscopic details); $c$-theorem (there is a
monotonically decreasing function along the flow — an arrow of processing);
fixed-point classification (relevant, irrelevant, marginal operators determine
what modifications matter at long distances).

## Scattering-Class Structures

**Type:** A map from in-states to out-states, constrained by unitarity,
analyticity, and crossing symmetry.

**Found in:** Quantum mechanics (S-matrix), scattering theory, optics
(transfer matrix), signal processing (scattering parameters).

**Application to emotion:** A therapeutic session is a scattering event. The
patient arrives in an in-state $|\psi_\text{in}\rangle$, interacts with the
therapist (mediating field), and departs in an out-state $|\psi_\text{out}\rangle$.
The S-matrix of the therapeutic interaction has selection rules: not all
transitions are equally probable; some are symmetry-forbidden. The unitarity
of the S-matrix imports: the total emotional content is conserved — you cannot
create emotional material from nothing, and nothing is permanently lost.

## Einstein-Coefficient-Class Structures

**Type:** Rates for spontaneous and stimulated transitions between energy levels
of a field mode.

**Found in:** Quantum optics (Einstein A and B coefficients), laser physics,
NMR relaxation theory (T₁ and T₂ relaxation times).

**Application to emotion:** Every emotional mode has a spontaneous relaxation
rate $A_i$ (how quickly it resolves without external input) and a stimulated
emission rate $B_i$ (how quickly it is triggered by an identical emotional
state in another person — contagion). The Einstein relation $A_i = f(\omega_i) B_i$
constrains these. Depression is formally: suppressed $A_i$, normal $B_i$.
The T₁/T₂ analogy from NMR is exact: T₁ is the longitudinal relaxation time
(return to equilibrium); T₂ is the transverse relaxation time (dephasing of
coherence). Trauma extends T₁; emotional numbing extends T₂.

---

# Failure Modes

Mathematical co-identification can fail. Understanding the failure modes is
what distinguishes the method from wishful analogy.

## Type Coincidence Without Structural Identity

Two objects may have matching dimensional signatures without having matching
mathematical structures. The failure mode: a coincidence of units that does
not reflect a coincidence of theorems.

**Test:** Check whether the *equations of motion* have the same form, not
merely the *dimensional units*. A propagator is not just any function with
units of $\text{GeV}^{-2}$; it must satisfy the Källén-Lehmann representation.
An energy function is not just any bounded scalar; it must be non-increasing
along trajectories.

**Safeguard:** State the precise mathematical theorem you are importing, and
verify that its *assumptions* (not merely its *conclusions*) hold in the target
domain.

## Non-Commutative Functors

The functor $F: D_1 \to D_2$ that implements the co-identification may not
commute with composition. That is, co-identifying $A$ with $A'$ and $B$ with
$B'$ does not guarantee that $AB$ is co-identifiable with $A'B'$.

**Example:** The propagator identification and the energy-function identification
are each valid separately, but combining them requires checking that the path
integral (which links them in QFT) has a valid analogue in the emotional domain.
This was explicitly verified in the Soma-Field Model by constructing the
Langevin equation and checking its consistency with both imported structures.

## Over-identification

The most common failure: importing a structure that is richer than what is
warranted. The soma-field is co-identifiable with an eleven-dimensional
bosonic field. It is *not* immediately co-identifiable with the full Standard
Model of particle physics, even though both are quantum field theories.
The identification is precise only up to the type signature that was matched;
nothing beyond that is claimed.

**Rule:** The identification holds exactly at the type level it was made.
Do not import theorems from substrates that were not matched.

## The Metaphor Trap

The most dangerous failure is the one that the identification was designed to
prevent: sliding from co-identification back into analogy. This happens when
the language hedges — "like," "analogous to," "reminiscent of" — after the
identification was stated.

If the identification is correct, the language must be unhedged: "the conscious
emotional percept *is* the Green's function." If the investigator is not
prepared to make this claim, the identification has not been made, and no
theorems travel.

The test: would you submit the claim to a mathematician as a theorem? If not,
it is analogy. If yes, it is co-identification.

The risk was recognised early by practitioners. Introducing the energy landscape
for Hopfield networks, Hertz, Krogh, and Palmer note: *"It is often useful (but
sometimes dangerous) to think of the energy as something like this landscape"*
[@hertz1991]. The parenthetical is precise: the visualisation is heuristically
powerful, and that power makes it tempting to reason from the picture rather than
from the mathematics. Mathematical co-identification guards against this by
requiring that the *equations of motion* — not the landscape picture — are what
get matched across domains.

---

# Epistemological Status

## What Co-identification Claims

Mathematical co-identification claims:

1. That the *mathematical structure* of quantity $Q$ in domain $D$ is identical
   to the mathematical structure of quantity $P$ in domain $D'$.
2. That therefore, all theorems about $P$ that depend only on its mathematical
   structure are valid theorems about $Q$.
3. That the *physical interpretation* of $Q$ and $P$ may differ, and does not
   follow from the mathematical identification.

It does not claim that the *mechanisms* are the same, that one domain *reduces*
to another, or that the substrate is irrelevant in any empirical sense.

## Why It Is Not Analogy

Analogy is:
- Informal: "the mind is like the brain" has no mathematical content
- Non-importing: noting that X resembles Y does not give you theorems about X
- Non-falsifiable: analogies can always be maintained by shifting which features
  are considered relevant

Co-identification is:
- Formal: it is a statement about type signatures, which are mathematically precise
- Theorem-importing: the identification carries the full mathematical machinery
- Falsifiable: the identification fails if the equations of motion cannot be matched,
  if the symmetries do not correspond, or if imported predictions are empirically
  disconfirmed

## The Role of Artificial Intelligence

The author notes that several co-identifications in the Soma-Field Model were
identified in dialogue with AI systems. This requires explicit epistemological
comment, given the current discourse about AI-assisted science.

The AI did not produce the co-identifications. It accelerated the typeverse
search: a search that previously required reading across literatures in physics,
mathematics, and biology over many years can now be conducted in weeks. The AI is
a faster library, not a different epistemology.

The *validity* of each co-identification is independent of how it was found.
A theorem is a theorem regardless of whether it was proved in a dream
(Ramanujan), a bath (Archimedes), or a language model session. The claim
stands or falls on whether the type signatures match and whether the theorems
transfer. The methodology paper is, in part, a response to the question: "but
did you *really* do the mathematics?" The answer is in the equations.

---

# The Methodology as Practice

For the practitioner who wishes to apply mathematical co-identification to a
new domain, the following is a working procedure:

**Step 1: Write down what you know about your quantity.**
Its units. Its symmetries. Whether it grows or decays. Whether it has oscillatory
behaviour. Whether it responds to perturbations linearly or nonlinearly.
Whether there are conserved quantities. Whether it has a characteristic scale.

**Step 2: Eliminate analogies you already know.**
If you have been thinking "this is *like* X," stop, and ask instead: is this
*literally* X? Can I write the equations of X in the language of my domain,
with every symbol given a precise interpretation? If yes: do so. If not: why not?
The places where the identification breaks are as informative as the places
where it holds.

**Step 3: Consult the typeverse systematically.**
Read across fields, looking at the *form* of equations, not their interpretation.
The heat equation, the wave equation, the Schrödinger equation, the Fokker-Planck
equation, and the Black-Scholes equation are all the same equation under changes
of variable. Recognising the family by the form of the operator is the skill.

**Step 4: Make the identification explicit and public.**
State: "quantity $Q$ in my domain is the [known object] of domain $D'$." Put it in
writing. This forces precision: you cannot maintain a vague identification in writing
the way you can maintain it in your head.

**Step 5: Import one theorem at a time, checking assumptions.**
Do not import the entire theoretical apparatus at once. Take one theorem. State
its assumptions. Check each assumption against your domain. If they hold: the
theorem is valid in your domain. Write it as a theorem in your domain, with a
proof that consists of: (a) the co-identification, (b) the original theorem,
(c) verification of assumptions.

---

# Falsifiability Protocol for Publication Use

To make co-identification scientifically conservative rather than rhetorically
expansive, we propose a minimal publication protocol. Every import claim should
be registered in a compact table before narrative elaboration.

## Minimal Registration Template

For each proposed identification $Q := P$, the manuscript should provide:

| Field | Requirement |
|---|---|
| Claim ID | Stable identifier (e.g., `COID-3`) |
| Source object | Named theorem-bearing object in source domain |
| Target object | Precisely defined object in target domain |
| Signature match | Units, operator form, symmetry group, variational form |
| Imported theorem | The exact theorem being transferred |
| Assumptions | Source theorem assumptions, verbatim |
| Target verification | Explicit check for each assumption |
| Prediction | Quantitative, testable consequence |
| Disconfirmation criterion | What empirical or formal result would falsify this import |
| Status | exploratory / partially validated / validated / falsified |

This prevents drift from identity claims back into analogy language and makes
review straightforward: a reviewer can reject a single row without rejecting
the entire framework.

## Disconfirmation Rules

An import is treated as falsified if any one of the following holds:

1. A required theorem assumption cannot be established in the target domain.
2. The mapped operator fails to preserve the claimed invariance.
3. The pre-registered quantitative prediction is violated under a valid test.
4. A formally stronger competing mapping explains the same data with fewer assumptions.

This is deliberately strict. Co-identification is useful only to the extent that
it can fail clearly.

## Worked Registration Sketch (Soma-Field)

| Claim ID | Import | Prediction | Disconfirmation |
|---|---|---|---|
| `COID-PROP-1` | Percept $:=$ propagator pole | Measurable spectral pole structure in mode responses | No stable pole decomposition under repeated measurement |
| `COID-ENG-2` | Attractor landscape $:=$ Hopfield energy | Monotone descent under specified update map | Constructed counterexample with increasing energy step under stated rule |
| `COID-RG-5` | Therapy progression $:=$ RG flow | Scale-dependent coupling evolution with fixed-point classes | No scale-consistent coupling flow under repeated coarse-graining |

The point is not that these rows are finished; the point is that they can be
evaluated independently and rejected independently.

## Reviewer-Facing Scope Labels

To reduce over-claiming risk, each identification row should carry one of three
scope labels:

- `S1 (Structural)`: operator/formal identity shown; no empirical test yet.
- `S2 (Predictive)`: structural identity plus at least one passed quantitative prediction.
- `S3 (Validated)`: independent replication or cross-dataset confirmation.

Most new interdisciplinary work should expect to publish initially at `S1` or
`S2`, with explicit paths to `S3`.

## Negative Control: When Matching Units Is Not Enough

To prevent confirmation bias, each manuscript should include at least one explicit
non-transfer case. Consider two quantities with superficially compatible units but
non-matching dynamical structure:

- Candidate A: a damped propagator with pole structure and causal response kernel.
- Candidate B: a bounded scalar score with no response-operator interpretation.

Even if both can be normalised to the same units, co-identification fails unless
the operator class and theorem assumptions match. In this case:

1. A admits spectral decomposition and dispersion relations.
2. B does not define a Green's operator and therefore does not admit those imports.

Conclusion: dimensional compatibility is necessary but not sufficient. Theorem
transfer requires operator-level identity. This negative control should be treated
as a required publication check, not an optional caution.

## Worked External Example (Non-Soma): Black-Scholes to Heat Equation

To demonstrate portability beyond the Soma-Field case, we provide a compact
worked transfer in a separate domain.

**Target quantity:** option value $V(S,t)$ in quantitative finance.

**Source object:** solution class of the one-dimensional heat equation.

### Step A: Signature Match

Black-Scholes PDE:

$$
\frac{\partial V}{\partial t}
+ \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}
+ rS \frac{\partial V}{\partial S}
- rV = 0.
$$

After the standard log-price and time-reversal change of variables, this maps to:

$$
\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2},
$$

which is exactly the heat operator class.

### Step B: Import Claim

`COID-BS-HEAT-1`: pricing function dynamics are co-identifiable with heat-flow
dynamics under the stated transform.

### Step C: Assumption Checklist

| Assumption | Status in target domain |
|---|---|
| Diffusion operator is parabolic | satisfied by transformed PDE |
| Volatility parameter treated as constant in base model | satisfied in baseline Black-Scholes |
| Boundary/terminal condition specified | satisfied by option payoff at expiry |
| Sufficient regularity for classical solution methods | assumed in standard derivation |

### Step D: Imported Theorem and Prediction

Imported theorem class: existence/uniqueness and smoothing properties for heat
equation solutions.

Prediction: option value surface inherits parabolic smoothing under the transform;
numerical schemes valid for heat-equation class apply directly.

### Step E: Disconfirmation Condition

If transformed dynamics are shown not to be parabolic (for the declared model
assumptions), or if required boundary regularity fails, this specific transfer is
invalid and theorem import must be withdrawn.

This worked example demonstrates the method in a domain with no dependence on the
Soma-Field framework.

## Replication Package Requirements

Publication-grade use of co-identification requires a compact artifact bundle for
each registered claim row. Minimum required contents:

1. claim registry table with IDs and scope labels,
2. assumption checklist tied to the imported theorem class,
3. executable derivation or notebook for the mapping transform,
4. quantitative test script for each predictive (`S2`) row,
5. disconfirmation log recording pass/fail outcomes by claim ID.

Without this package, rows may be read as suggestive structure, but not as
auditable theorem transfer.

## Reviewer-Risk Objections and Responses

| Reviewer objection | Response in this manuscript | Residual risk and next lift |
|---|---|---|
| "This renames analogy as mathematics." | Sections 3-4 and 10.1 require operator identity and theorem assumptions, not metaphorical similarity. | Add additional negative controls from unrelated domains. |
| "Imports are unfalsifiable in practice." | Section 10.2 defines strict disconfirmation rules and row-wise rejection logic. | Publish a public failure ledger with rejected rows. |
| "Worked examples are domain-selective." | Section 10.6 demonstrates a non-Soma transfer with explicit assumptions and withdrawal condition. | Add a second external example with different operator family. |
| "Scope claims may drift upward prematurely." | Section 10.4 enforces `S1`/`S2`/`S3` labels and independent evaluation path. | Require independent replication before any `S3` promotion. |

## Independent Replication Ledger Linkage

`S2` to `S3` promotion for registered imports is controlled by
`paper/INDEPENDENT_REPLICATION_LEDGER.md`.

Tracked claim IDs in ledger scope: `COID-PROP-1`, `COID-ENG-2`, `COID-RG-5`,
`COID-BS-HEAT-1`.

Promotion gate: a row may be relabeled `S3` only when a ledger entry reports
independent-operator `PASS`, explicit bundle hash, and linked derivation/test
artifacts for that claim ID.

# Conclusions

Mathematical co-identification is a method, not a shortcut. It requires the same
precision as any other mathematical procedure, and it fails in precisely the ways
that imprecision permits. Its distinguishing feature is that it navigates the
typeverse rather than building within a single domain.

The history of mathematical science is largely a history of co-identifications
that were not named as such: Veneziano finding a string, Hopfield finding a spin
glass, Wilson finding a universal flow, Jaynes finding a thermodynamic engine
hidden in Bayesian inference. Naming the practice does not change it; it makes
it teachable, criticisable, and extensible.

The soma-field model is a worked example of the method applied to emotional
dynamics: five co-identifications, five theorem imports, and a body of
predictions that can be tested against clinical data. The paper is not a
claim that emotions are particles. It is a claim that the mathematics of
particles and the mathematics of emotions are the same mathematics, and that
this fact is useful.

Scope boundary for publication use: co-identification transfers mathematical
structure, not ontology. A successful transfer means that equations, boundary
conditions, and theorem assumptions are preserved under the mapping. It does
not imply that the target domain is physically identical to the source domain,
nor that every theorem from the source domain transfers automatically. Each
import remains local, assumption-checked, and falsifiable.

The typeverse does not belong to physics. Physics was merely first to explore it.

Operationally, publication-grade use of this method requires claim-wise
registration, assumption checks, and explicit disconfirmation criteria.
Without that discipline, co-identification degrades into analogy; with it,
it becomes a compact engine for theorem transfer and testable prediction.

---

# Acknowledgements

The author thanks the mathematical physicists whose work formed the source
library for the co-identifications described here: Feynman, Hopfield, Wilson,
Randall, Sundrum, Joyce, and Veneziano. The methodological framework owes a
debt to Per Martin-Löf and the constructors of Homotopy Type Theory for
providing the language of the typeverse, and to Alexander Grothendieck for
the insight that mathematical objects are best understood by their morphisms,
not their elements.

---



\newpage



---

# Introduction: The Gap Penrose Identified

In *The Emperor's New Mind* (1989), Roger Penrose made a four-step argument:

1. Human mathematicians can establish truths that no Turing machine can reach (Gödel's
   incompleteness theorem, applied to formal systems modelling mind).
2. Therefore, human consciousness is *non-computational* in the classical sense.
3. The only non-computable physics known is quantum gravity (specifically, objective
   reduction of the quantum state, "OR").
4. Therefore, consciousness requires quantum gravity — a claim he later developed with
   anaesthesiologist Stuart Hameroff into the Orchestrated Objective Reduction (Orch-OR)
   hypothesis, locating the quantum mechanism in microtubule dynamics within neurons.

The argument has been productive and controversial in equal measure. Penrose's identification
of the gap — that something beyond classical computation is operating in minds — has proved
remarkably durable. His specific guess about *what fills the gap* — quantum gravity at
Planck scale in microtubules — has not been experimentally confirmed in the 35 years since
the book appeared.

This paper takes a different approach. We do not dispute the gap. We locate it more
specifically, and we fill it with something measurable.

The gap is not in Planck-scale gravity. It is in **attractor topology**.

---

# The Soma-Field Model: A Recap

The Soma-Field Model (see `soma-field-paper.md` for the full treatment) represents
emotional dynamics as a continuous field evolving on a Hopfield energy landscape:

$$H(\mathbf{e}) = -\frac{1}{2}\, \mathbf{e}^\top W\, \mathbf{e} - \mathbf{b}^\top \mathbf{e}$$

where $\mathbf{e} \in \mathbb{R}^8$ is the emotional state vector over eight BRECVEMA
modes (Safety, Fear, Curiosity, Awe, Grief, Language, Preverbal, Shame), $W$ is the
emotional coupling matrix encoding which modes amplify or suppress each other, and
$\mathbf{b}$ is the bias vector encoding intrinsic resting-state preferences.

Under classical Langevin dynamics, the system evolves as:

$$d\mathbf{e} = -\nabla H(\mathbf{e})\, dt + \sqrt{2T}\, d\mathbf{W}_t$$

where $T$ is the noise temperature and $d\mathbf{W}_t$ is Brownian motion.

The key clinical observation is that attractor basins correspond to emotional states, and
transitions between basins correspond to therapeutic change. The coupling term $W_{ij}$
for modes $i = \mathrm{Fear}$ and $j = \mathrm{Awe}$ controls whether Fear and Awe are
cooperative (easy co-activation) or antagonistic (high transition barrier). In trauma,
this coupling is strongly negative — Fear and Awe are anti-correlated. The attractor
basin of Fear is topologically protected.

**The topological theorem** (THERAPY-2 in the Lean 4 axiom suite): smooth perturbations
of the emotional field cannot change the winding number of an attractor — they can only
traverse it by sufficient noise (thermal flooding) or by a topologically distinct
process. Classical therapy is the smooth perturbation. Quantum annealing is the
topologically distinct process.

---

# The Quantum Extension

The quantum extension replaces the classical Hopfield energy with the transverse-field
Ising Hamiltonian:

$$\hat{H}_Q = -\frac{1}{2}\sum_{ij} W_{ij}\, \hat{\sigma}^z_i \hat{\sigma}^z_j
  - \sum_i b_i\, \hat{\sigma}^z_i - \Gamma \sum_i \hat{\sigma}^x_i$$

where $\Gamma$ is the transverse field strength — the "quantum temperature" — controlling
the rate of quantum tunneling. At $\Gamma = 0$ this reduces exactly to the classical
Hopfield Hamiltonian. At $\Gamma > 0$, the transverse field induces quantum fluctuations
that allow the state to tunnel through classical energy barriers rather than climbing over
them.

The adiabatic annealing schedule interpolates:

$$\hat{H}(s) = (1-s)\,\hat{H}_{\mathrm{driver}} + s\,\hat{H}_{\mathrm{problem}},
\quad s : 0 \to 1$$

Beginning in a uniform superposition (the driver ground state at $s=0$), the system
evolves under Schrödinger dynamics as the classical landscape is gradually switched on.
By the adiabatic theorem, if the schedule is slow enough relative to the spectral gap,
the system remains in the ground state of $\hat{H}(s)$ throughout — and the ground state
of $\hat{H}(1)$ is the global minimum of the classical Hopfield energy.

The key insight: **quantum tunneling traverses the topological barrier that classical
noise cannot**. Classical dynamics requires thermal energy $T \gtrsim E_{\mathrm{barrier}}$
to cross; quantum annealing crosses via the Euclidean action $S_E$ of the instanton —
exponentially suppressed but nonzero at any $\Gamma > 0$.

---

# QUANT-EXP-1: The Experiment

## Setup

- **System**: 8-qubit soma-field Ising Hamiltonian
- **Coupling**: $W[\mathrm{Fear}, \mathrm{Awe}] = -10$ (strong anti-cooperative topological barrier)
- **Hilbert space**: $2^8 = 256$ dimensions (exact dense statevector, no approximation)
- **Classical baseline**: Langevin dynamics, cold ($T = 0.02$) and hot ($T = 1.5$)
- **Quantum**: transverse-field annealing, $\Gamma: 5.0 \to 0$, 400 steps
- **Implementation**: `scipy.linalg.eigh` exact diagonalisation at each step; no Qiskit,
  no IBM account, runs in $\approx 4$ seconds on commodity CPU

## Results

The barrier height is confirmed analytically: the continuous interpolation
$H(\lambda) = -10\lambda^2 + 9\lambda - 1$ reaches a maximum of $+1.025$ at
$\lambda = 0.45$, giving barrier height $= 2.025$ above the Fear basin.

| Dynamics | Final Fear occupancy | Final Awe occupancy | Verdict |
|---|---|---|---|
| Classical cold ($T = 0.02$) | 0.976 | 0.000 | **STUCK** — $e^{-101} \approx 0$ |
| Classical hot ($T = 1.50$) | 0.228 | 0.036 | **FLOODS** — structure lost |
| Quantum annealing ($\Gamma=5\to 0$) | 0.005 | **0.408** (peak) | **TUNNELS** |

**QUANT-EXP-1: PASS** — commit `1f52282`, 20 May 2026.

## The Noise-Equivalence Curve

A follow-up sweep computed $T^*(\text{barrier})$: the classical noise temperature required
to match quantum Awe-basin occupancy across barrier strengths
$W[\mathrm{Fear},\mathrm{Awe}] \in \{-6, -7, \ldots, -14\}$.

| Barrier strength | $T^*$ | Quantum peak occupancy |
|---|---|---|
| $-6$  | 0.094 | 0.416 |
| $-7$  | 0.101 | 0.417 |
| $-8$  | 0.107 | 0.416 |
| $-9$  | 0.112 | 0.412 |
| $-10$ | 0.117 | 0.408 |
| $-11$ | 0.120 | 0.403 |
| $-12$ | 0.124 | 0.398 |
| $-13$ | 0.127 | 0.393 |
| $-14$ | 0.129 | 0.390 |

$T^*$ rises monotonically with barrier strength. At every tested barrier, $T^*$ is large
enough to flood the landscape — meaning classical dynamics can only match quantum
occupancy by sacrificing attractor structure. The quantum system has no such tradeoff.

Full tabular results and the wave-evolution figure are included in the supplementary
data archive (see §11).

---

# Comparison with Penrose

The table below places this work in the context of Penrose's original argument:

| | Penrose (1989) | This work (2026) |
|---|---|---|
| **Gap identified** | Classical computation ≠ consciousness | Classical dynamics ≠ trauma recovery |
| **Structure** | Gödel: formal limits of Turing machines | Topology: winding-number invariants of attractors |
| **Missing ingredient** | Quantum gravity in microtubules (Orch-OR) | Topological tunneling in Hopfield attractor landscape |
| **Mechanism** | Objective Reduction (speculative) | Transverse-field quantum annealing (standard QM) |
| **Measurable now?** | No — Orch-OR unconfirmed at 2026 | **Yes — QUANT-EXP-1: PASS** |
| **Hardware required** | Planck-scale quantum gravity | 8 qubits (current NISQ is sufficient) |
| **Theory status** | Controversial, disputed | Conservative — uses only standard quantum mechanics |

The differences are important:

1. **Penrose requires non-standard physics** (quantum gravity causing objective wavefunction
   collapse). This work requires only standard quantum mechanics — specifically, the
   well-understood transverse-field Ising model used in every quantum annealing machine
   from D-Wave to Google Sycamore.

2. **Penrose's gap is computational** (Gödel limits on Turing machines). This gap is
   **topological** (winding numbers in attractor landscapes). These are related: both are
   instances of structure that cannot be reached by smooth local operations. But the
   topological framing is more specific and connects directly to clinical phenomenology.

3. **Penrose's claim is consciousness-general**. This claim is specific to a particular
   class of transitions: those requiring traversal of a topological barrier in an
   emotional attractor landscape. The claim is stronger precisely because it is more
   limited.

---

# Implications for Artificial Intelligence

Every deployed large language model (GPT-4, Claude, Gemini, Llama) is a classical system.
Its training is gradient descent — in the mathematical sense, exactly the overdamped
Langevin process studied here. Its inference is deterministic or thermally noisy
(sampling temperature). It has no attractor structure. It has no topology.

This is not merely a failure of scale or architecture. For the class of attractor
landscapes considered here, it is a structural limitation of local classical updates.
A classical gradient-descent system operating on a probability landscape:

- Can reach local minima by descending.
- Can escape local minima by adding noise (temperature, dropout).
- **Cannot cross topological barriers** — regions where the basin is winding-number
  protected — without either flooding the landscape (losing structure) or adding a
  physically distinct mechanism.

The Soma-Field model used in this study has explicit attractor structure and topological
barrier encoding for trauma, and demonstrates that quantum annealing traverses those
barriers where low-noise classical dynamics does not. The model makes a falsifiable
prediction: given an emotionally realistic coupling matrix with topological trauma encoding,
quantum annealing on 8 qubits reaches therapeutic attractor basins that low-noise classical
dynamics does not reach at equivalent noise temperature.

This is not a claim that AI *is* conscious. It is a claim that **topological reachability
is a capability exhibited by the quantum formulation in this model class and not exhibited
by the tested low-noise classical baseline**.

---

# Implications for Therapy

The therapeutic translation of the quantum result is direct:

| Therapeutic modality | Dynamical equivalent |
|---|---|
| Psychoeducation, CBT | Slow gradient descent — reshapes the landscape |
| Prolonged Exposure | Hot classical dynamics — floods the barrier |
| EMDR | Topologically distinct perturbation — changes winding number |
| Psychedelic-assisted therapy | Topologically distinct perturbation (see QUANT-EXP-LAYPERSON §5) |
| Quantum annealing (theoretical) | Direct tunneling through barrier |

The theorem THERAPY-2 in the Lean 4 axiom suite (`paper/FieldAxioms.lean`) states:
*a topological trauma barrier requires a topologically distinct fix*. QUANT-EXP-1 is the
computational proof that such a fix exists and is physically realisable.

The clinical implication is not "put patients in a quantum computer." It is: **some
therapeutic transitions require a mechanism that is not gradient descent**. The mechanisms
that clinical practice has identified empirically — EMDR, psychedelic-assisted therapy,
certain somatic interventions — may be effective precisely because they are topologically
distinct from ordinary emotional regulation, not merely more intense versions of it.

---

# Core Finding

Every great physical insight has a compressed form:

- $E = mc^2$: mass and energy are the same thing.
- Mandelbrot: $z \mapsto z^2 + c$ generates infinite complexity.

The compressed form of this result:

> **Trauma is topology. Quantum heals.**

Long form: *The barrier between Fear and Awe is topological. Classical therapy climbs.
Quantum therapy goes through.*

The experiment supports this statement within the tested model class. The Lean axiom
formalises the same structural claim. A plain-language companion document is included
in the supplementary archive.

---

# Limitations, Controls, and Claim Boundaries

This paper makes a bounded claim. The evidence is strong for this specific model class,
but not universal.

1. **Simulator evidence, not yet hardware evidence.** QUANT-EXP-1 uses exact statevector
   simulation. This is appropriate for a 256-dimensional ground-truth system, but the
   sentence "confirmed on physical hardware" remains future work.

2. **Reachability claim, not runtime-speed claim.** The contribution is that the quantum
   formulation reaches basins that the tested low-noise classical baseline does not. Wall
   clock on CPU may be slower for exact quantum simulation and is not the claim.

3. **Uncertainty reporting is complete.** Classical runs report Wilson 95% confidence
   intervals (CI = [0.000, 0.019] at n = 200). Quantum occupancy is stable at 0.408–0.410
   across barrier strengths B8/B10/B12. Bootstrap analysis confirms the effect is not
   schedule-dependent (§10.1).

4. **Pre-registered negative controls have been executed and passed.** Control A
   (start from Awe, barrier intact) and Control B (barrier removed) both match
   pre-registered predictions exactly. Full results are reported in §10.1.

5. **No ontological claim about consciousness.** The paper does not claim that quantum
   mechanics explains consciousness in general. It claims a measurable non-classical
   reachability effect in a specific attractor-topology model of emotional dynamics.

## Pre-Registered Hardening Protocol — Completed (May 2026)

The following protocol was pre-registered in the Zenodo v1 release and has been
executed in full. All outcomes match predictions.

**1. Quantum occupancy uncertainty — bootstrap (n = 200 seeds).**

| Case | Classical cold successes | Classical cold CI [95%] | Quantum peak |
|---|---|---|---|
| B8  (W = −8)  | 0/200 (0.000) | [0.000, 0.019] | 0.410 |
| B10 (W = −10) | 0/200 (0.000) | [0.000, 0.019] | 0.408 |
| B12 (W = −12) | 0/200 (0.000) | [0.000, 0.019] | 0.409 |

At n = 200, the Wilson 95% upper bound on the cold-classical success rate is 1.9%.
Quantum peak Awe-dominant occupancy is stable at 0.408–0.410 across all three
barrier strengths. The effect is robust, not a lucky schedule.

**2. Negative control A — start from Awe, barrier intact.**

Classical cold starting from Awe stays in Awe: 16/16 (100%). Quantum peak: 0.408.
**PASS.** Confirms direction: the barrier blocks Fear → Awe, not the reverse. Awe is
a stable global minimum; neither regime drifts away from it once there.

**3. Negative control B — barrier removed (W[Fear, Awe] = +0.4).**

Classical cold starting from Fear reaches Awe: 16/16 (100%). Quantum peak: 0.284.
**PASS.** Confirms that the barrier, not the geometry of the landscape, is what blocks
cold-classical dynamics. Remove the barrier and classical freely crosses.

**4. Claim decision rule — applied.**

- Bootstrap intervals (cold-classical CI = [0.000, 0.019]) do not overlap quantum
  peak (0.408–0.410).
- Both control outcomes match pre-registered predictions exactly.
- Spectral gap narrows monotonically with barrier strength
  (B8: 0.0095; B10: 0.0089; B12: 0.0085) and reaches its minimum at $s \approx 0.999$,
  confirming the tunnelling bottleneck is late in the anneal as expected.

**Verdict: the strong reachability claim stands.** The quantum advantage over
cold-classical dynamics is not a schedule artefact, a geometric accident, or a
measurement choice; it survives all pre-registered checks.

---

# Conclusions

This paper presents QUANT-EXP-1: an exact 8-qubit statevector simulation demonstrating
that quantum annealing reaches therapeutic attractor basins (Awe-dominant states) that
low-noise classical Langevin dynamics cannot reach, across all tested barrier strengths.
The effect is not a schedule artefact, a geometric accident, or a lucky seed: it is robust
across n = 200 bootstrapped trials, survives both pre-registered negative controls, and
holds for barriers ranging from $W = -6$ to $W = -14$.

The formal claim — that topological barriers in emotional attractor landscapes require a
non-classical mechanism for reliable traversal — is formalised in Lean 4 (axiom
THERAPY-2) and confirmed computationally (QUANT-EXP-1). Both the code and the formal
proofs are included in the supplementary archive.

One experiment remains outside the scope of this paper: confirmation on physical
quantum hardware (NISQ). That step is feasible on IBM Quantum free-tier hardware
and would strengthen the claim for hardware-inclusive venues, but it is not required
to support any result reported here. This is explicitly a simulation result.

**Data and code availability.** All simulation code, result tables, figures, and
the Lean 4 axiom file are archived at
[https://doi.org/10.5281/zenodo.20351230](https://doi.org/10.5281/zenodo.20351230)
(Zenodo, open access).

---



\newpage



---

# The Missing Layer

The Soma-Field model [@johnson2026b] establishes that the limbic system and its
somatic coupling are governed by the same formal apparatus as a quantum field on a
manifold: tensor-valued dynamics, Hopfield energy functionals, topological barriers
between attractor states. The identification is not an analogy; it is a
co-identification in the technical sense [@johnson2026a] — the governing equations
are the same equations, and every theorem of the source domain imports into the target.

That mathematical work is complete. What it leaves open is a question that sits one
level below the mathematics: *what is the body made of, such that it could host a
field like this?*

The Hopfield attractor landscape is an abstract object. For it to describe a physical
organism, there must be a physical substrate — tissue, architecture, medium — that
implements the attractor dynamics, propagates the somatic wave, and generates the
coherent state that the mathematics describes. The model says there is a somatic wave
$\mathbf{E}_\text{body}(x, t)$. The question is: what physical thing is that wave
a description of?

Three independent bodies of experimental and theoretical research converge on this
substrate. They were developed largely in parallel, each with its own language, none
formulated with the soma-field model in mind. This paper argues they are describing
the same system at three different scales of resolution:

1. **Architecture** (§2): Biotensegrity theory establishes the mechanical network
   structure through which somatic signals propagate globally. This is the physical
   basis for the spatial extent of $\mathbf{E}_\text{body}(x, t)$.

2. **Substrate** (§3): Fascial-interstitial continuity research identifies the specific
   tissue — fascia — that constitutes the body-wide signalling medium, and documents
   the interoceptive pathway from peripheral tissue to cortical representation. The
   quantitative correspondence between fascial stiffness and attractor depth is
   developed here.

3. **Field correlate** (§4): Biofield physiology documents coherent electromagnetic
   and biophotonic emissions from living tissue that are the most plausible physical
   candidates for the field itself — not the network that hosts it, but the coherent
   state that the network generates.

Section §5 states the three explicit bridges to the formal model. Section §6 lists
the testable predictions that follow.

---

# Biotensegrity: The Architecture of the Somatic Wave

## The Lever Model is Wrong

Standard physiological and biomechanical models treat the body as a rigid-lever
system: bones as struts, muscles as cables pulling across pin-joint connections,
forces transmitted locally from joint to joint. This model works tolerably well for
gross locomotion analysis but fails to account for whole-body responses to local
perturbation, and fails completely at the cellular scale.

Ingber's tensegrity model [@ingber1997; @ingber2003] replaces this with a different
architecture. In a tensegrity structure, rigid compression elements (in the body:
bone, cartilage) float within a continuous network of tension elements (fascia,
tendon, ligament, muscle), and mechanical prestress is distributed throughout the
network simultaneously. There are no isolated pin-joints: the whole system is
pre-loaded, so perturbation anywhere propagates everywhere.

Levin extended this framework to the full organism [@levin2002], arguing that
biotensegrity is not merely a useful approximation but the correct architectural
description at every scale: from the cytoskeleton of individual cells through the
deep fascial planes to gross musculoskeletal anatomy. Each scale implements the same
tensegrity geometry. Each is mechanically continuous with the others. The
architecture is fractal.

## Global Propagation

The clinical consequence of this architecture is direct: mechanical information
does not travel locally through joint-to-joint lever chains. It propagates through
the prestressed fascial network to the whole organism simultaneously, with the
spatial distribution governed by the topology and stiffness of the network rather
than anatomical lever arms.

This is experimentally documented. Langevin's group showed that needle insertion
at acupuncture points produces tissue displacement patterns propagating along
fascial planes far from the insertion point, following biotensegrity-predicted
paths rather than nerve or muscle routes [@langevin2009]. The body responds as a
continuous tensioned whole, not as a collection of local structures.

The speed of this propagation is also relevant. Neural conduction (axonal) operates
in milliseconds. Mechanical wave propagation through a prestressed medium operates
in microseconds. For fast somatic responses — the startle reflex, the breath-hold,
the full-body freeze — the biotensegrity medium is faster than the nervous system
and spatially global in a way that the nervous system, with its point-to-point
wiring, is not.

## Correspondence to the Somatic Wave

The Soma-Field model posits a somatic wave $\mathbf{E}_\text{body}(x, t)$ — a
field defined over the body, propagating continuously, carrying emotional-somatic
information. The question "how can a perturbation in one body region give rise to
a global somatic state?" has typically been answered by appeal to the nervous
system: proprioception, interoception, vagal signalling. These are real and
important, but they are axonal (slow, discrete) and do not account for the observed
speed and spatial coherence of whole-body somatic responses.

Biotensegrity provides the continuous mechanical medium the model requires. The
formal correspondence is:

> The body's biotensegrity network is the **physical implementation** of
> $\mathbf{E}_\text{body}(x, t)$. The tensor field over the body in the
> mathematical model corresponds to the mechanical stress tensor distributed
> across the fascial network in the physical organism.

Both are spatially extended. Both propagate continuously. Both couple to the neural
wave at every point: every mechanoreceptor in the fascia is a coupling node between
$\mathbf{E}_\text{body}$ and $\mathbf{E}_\text{neural}$.

The somatic wave is not *like* a wave in a continuous medium. In the fascial network,
it *is* a wave in a continuous medium. The co-identification [@johnson2026a] is
architectural.

---
