
# Partie IV : Extensions et Applications

## La Trilogie des Contenants

La partition du Film de la Rivière peut être réalisée dans au moins trois contenants sans changer une seule valeur dans la définition de la partition :

| Contenant | Cadre | Kurtz / attracteur profond |
|---|---|---|
| **Rivière** | Congo / Mékong / Amazone | La figure en amont ; l'endroit sans langage |
| **Corps** | Sous-marin miniaturisé dans le sang | Chambre cardiaque ; la plus ancienne mémoire immunitaire |
| **Session** | Salle de psychothérapie | Le moment où le freeze se lève |

Les trois sont le même film. Les trois traversent les mêmes deux seuils aux mêmes temps narratifs. Les trois reviennent le long du chemin asymétrique. Le rendu rend les trois identiquement — parce que c'est la partition qui est rendue, pas le contenant.

## Composer avec la Partition

Un compositeur travaillant avec ce système n'écrit pas de notes. Ils écrivent des trajectoires. Les décisions compositionnelles sont :

1. **Quels modes** sont les axes primaires de cette pièce ?
2. **Quel est l'arc** — la forme de chaque trajectoire sur le temps narratif ?
3. **Où sont les seuils** — les événements d'instanton ?
4. **À quelle profondeur** est l'attracteur le plus profond ? (À quoi $\kappa_d = 1.0$ ressemble-t-il ici ?)
5. **Quelle est la topologie de retour** — le champ retourne-t-il là où il a commencé, ou le bassin de retour est-il différent du bassin de départ ?

Un film avec les mêmes bassins de départ et de retour (safety à $t=0$ ≈ safety à $t=1$) est un aller-retour. La plupart des sessions de thérapie ne sont pas des allers-retours. Le bassin de retour est réorganisé : cohérence HRV plus élevée, couplage par défaut plus bas entre fear et shame, distance de seuil plus large de l'attracteur freeze. La partition devrait refléter ceci — le retour n'est pas une inversion du départ, mais un chemin différent vers une version différente du foyer.

## Diagrammes de Cordes comme Notation de Partition

Pour les partitions multi-personnages — où le couplage entre multiples champs spectateurs fait partie de la composition — les diagrammes de cordes fournissent la notation. Chaque fil est un champ soma. Chaque boîte est une interaction. La composition (deux boîtes en séquence) est une séquence temporelle d'interactions. Le produit tensoriel (deux fils en parallèle) est une activation indépendante simultanée.

Une dyade de thérapie est deux fils à travers le temps, avec des boîtes de couplage aux points de co-régulation. Un public de film est $N$ fils parallèles, chacun avec son propre $H_V$, tous se couplant au même signal d'écran $S(t)$. La partition émotionnelle est la spécification abstraite de ce que $S(t)$ fait. La réponse collective du public est le produit tensoriel de $N$ trajectoires individuelles, toutes façonnées par la même source.

## La Trilogie du Tenseur

Ce document fait partie d'un projet en trois parties :

| Document | Registre | Titre complet |
|---|---|---|
| **soma-field-paper.md** | Académique | *Le Modèle du Champ Soma* (Le Tenseur II) |
| **soma-field-book.md** | Accessible | *Un Voyage dans le Trauma* (Le Tenseur III) |
| **the-tensor.md** | Opérationnel | *Le Tenseur* — définition abstraite de film |

L'article définit le modèle. Le livre explique le modèle. Ce document **exécute** le modèle — ou plus précisément, définit l'interface par laquelle un système de rendu audio-visuel peut instancier le modèle comme expérience en temps réel.

## Le Problème de la Pensine

Dans *Harry Potter*, Dumbledore utilise sa baguette pour extraire une pensée de son esprit — elle émerge comme un fil argenté — et la dépose dans un bassin de pierre appelé la Pensine. D'autres peuvent alors abaisser leur visage à la surface et entrer dans la mémoire, l'expérimentant de l'intérieur.

C'est la sérialisation de l'état mental : un processus en cours (une mémoire, actuellement en exécution dans un esprit vivant) extrait et écrit dans un stockage persistant, puis désérialisé à un moment ultérieur par un lecteur différent.

La partition du champ soma est une Pensine pour la dynamique émotionnelle. La baguette est le système de mesure (HRV, observation du thérapeute, biofeedback). Le fil argenté est le fichier de partition $\mathbf{e}^*(t)$, la matrice de couplage $W^*$, le noyau de mémoire $K^*$. Le bassin de la Pensine est le système de rendu.

Mais la partition du champ soma est strictement plus puissante que le bassin de Dumbledore :

| | Pensine | Partition de champ soma |
|---|---|---|
| Ce qui est sérialisé | Contenu de mémoire — les événements et images spécifiques | Dynamique émotionnelle — la forme du champ, topologie attracteur, forces de couplage |
| Rejeu | Fixe ; même expérience pour chaque spectateur | Rendu à travers le propre $H_V$ du spectateur ; personnalisé sans perdre l'identité de la partition |
| Rôle du spectateur | Observateur passif à l'intérieur d'un enregistrement fixe | Participant actif du champ ; à $\kappa_r = 1$, co-auteur du rendu |
| Unité de stockage | Une pensée spécifique | La *forme* émotionnelle — valide pour tout contenant narratif avec la même dynamique |

Dumbledore stocke ce qui s'est passé. Le champ soma stocke ce que c'était de ressentir d'être dans ce bassin — découplé du contenu narratif spécifique, portable à travers les contenants, rendable par un système nerveux différent dans un siècle différent.

Le mot technique pour ce que les deux systèmes font est **sérialiser** : prendre un processus en cours qui existe seulement en temps réel et l'écrire dans un format durable, transmissible. Le mot poétique est **cristalliser** — fixer quelque chose de fluide dans une forme reproductible sans détruire sa structure essentielle.

Nous cristallisons l'expérience émotionnelle. Pas l'histoire. Pas les images. Les mathématiques sous toutes les histoires et toutes les images qui ont la même forme émotionnelle. C'est ce que le fichier de partition contient. C'est ce que le système de rendu lit en retour.

---

\newpage

# Annexe : Format de Fichier de Partition

Une partition lisible par machine serait exprimée comme suit. C'est une esquisse du format ; une spécification complète est un document d'ingénierie séparé.

```yaml
score:
  title: "The River Film"
  version: "0.1"
  modes:
    - id: S   name: Safety      range: [0, 1]
    - id: F   name: Fear        range: [0, 1]
    - id: C   name: Curiosity   range: [0, 1]
    - id: A   name: Awe         range: [0, 1]
    - id: G   name: Grief       range: [0, 1]
    - id: L   name: Language    range: [0, 1]
    - id: PV  name: Pre-verbal  range: [0, 1]

  coupling:
    # W_ij: mode j drives mode i
    - from: F  to: A  weight: +0.4   # fear can tip into awe near threshold
    - from: A  to: G  weight: +0.3   # awe opens grief
    - from: L  to: PV weight: -0.6   # language suppresses pre-verbal
    - from: PV to: L  weight: -0.6   # pre-verbal suppresses language

  keyframes:
    # story-time: [S,    F,    C,    A,    G,    L,    PV  ]
    0.0:          [0.90, 0.10, 0.30, 0.10, 0.10, 0.90, 0.10]
    0.1:          [0.80, 0.10, 0.50, 0.10, 0.10, 0.90, 0.10]
    0.2:          [0.70, 0.20, 0.70, 0.10, 0.10, 0.80, 0.10]
    0.3:          [0.50, 0.30, 0.80, 0.20, 0.10, 0.70, 0.20]
    0.4:          [0.30, 0.50, 0.70, 0.30, 0.20, 0.50, 0.30]
    0.5:          [0.20, 0.70, 0.50, 0.40, 0.30, 0.30, 0.50]
    0.52:         [THRESHOLD_1]
    0.6:          [0.10, 0.40, 0.30, 0.60, 0.40, 0.10, 0.70]
    0.7:          [0.10, 0.20, 0.20, 0.90, 0.50, 0.05, 0.90]
    0.74:         [THRESHOLD_2]
    0.8:          [0.20, 0.10, 0.30, 0.70, 0.60, 0.20, 0.60]
    0.9:          [0.50, 0.10, 0.50, 0.40, 0.40, 0.60, 0.20]
    1.0:          [0.90, 0.10, 0.50, 0.20, 0.20, 0.90, 0.10]

  thresholds:
    - id: T1
      t: 0.52
      from_basin: [approach, hypervigilance]
      to_basin: [awe-onset]
      condition: "F > 0.7 AND A rising"
      instanton_depth: kappa_d
      hold_until_ready: true

    - id: T2
      t: 0.74
      from_basin: [awe-onset]
      to_basin: [encounter]
      condition: "L < 0.1 AND PV > 0.85"
      instanton_depth: kappa_d
      hold_until_ready: true

  defaults:
    kappa_d: 0.70
    kappa_v: 1.00
    kappa_r: 0.00
    kappa_t: 0.40
    kappa_W: 1.00
```

---

*Le Tenseur. 17 mai 2026.*



\newpage

\part{Partie II : L'Appareil Formel}



---

> *L'IA a un cerveau depuis 1943. Maintenant elle a un corps.*

---

# Introduction

Un patient est assis avec son thérapeute et on lui demande : *« Que ressentez-vous en ce moment ? »* La question est trompeusement simple. Ils peuvent dire *anxieux*, pourtant ce mot couvre un territoire vaste et hétérogène — une tension dans la poitrine, un commentaire courant d'inquiétude, une vague préparation à fuir, un souvenir surgissant de l'enfance. Un autre patient, à qui on pose la même question, rapporte ne ressentir rien du tout ; et pourtant leur posture, respiration, et la qualité de leur silence suggèrent autrement. L'émotion est là. Elle n'est simplement pas encore consciente.

Cet écart entre la présence émotionnelle et la conscience émotionnelle est l'un des phénomènes les plus cliniquement significatifs en psychothérapie. Les théories de la régulation de l'affect (Schore, 2001), l'expérience somatique (Levine, 2010), la psychothérapie sensorimotrice (Ogden, Minton & Pain, 2006), et la théorie polyvagale (Porges, 2011) toutes se débattent, de différentes façons, avec la même observation : les émotions existent dans le corps avant — et souvent sans — être nommées dans l'esprit. Eugene Gendlin a appelé le sens corporel sub-verbal d'une situation émotionnelle le *felt sense* (Gendlin, 1978) : quelque chose qui est là, entier et présent, mais pas encore articulé.

Le Modèle du Champ Soma proposé ici tente de donner à cette observation clinique une structure formelle. Il le fait en empruntant un outil conceptuel de la physique : le champ. En physique, un champ n'est pas une chose qui existe en un point. C'est une quantité qui existe partout dans un espace, continuellement, qu'elle soit observée ou non. Les particules — les choses que nous pouvons mesurer — ne sont pas séparées du champ ; ce sont des *excitations* de lui, des concentrations locales d'énergie qui surviennent quand le champ est perturbé au-dessus d'un certain seuil.

L'affirmation centrale de cet article est que cette structure décrit avec précision la phénoménologie de l'émotion. Le champ émotionnel est toujours là, distribué à travers le corps et le système nerveux. Ce que nous appelons une expérience émotionnelle consciente est une excitation de ce champ — une concentration locale qui a traversé un seuil perceptuel et est entrée dans la conscience. Le champ continue sous le seuil que nous y prêtions attention ou non, et son activité sub-perceptuelle façonne notre comportement, physiologie, et cognition continuellement.

Le Modèle du Champ Soma contribue la première architecture formelle de théorie des champs pour le système limbique. Chaque réseau neuronal artificiel depuis McCulloch et Pitts (1943) [@mcculloch1943] est un modèle formel du néocortex — la couche de reconnaissance de motifs et de prédiction. Le système limbique — responsable de la valuation émotionnelle, détection de menace, et la réinstauration d'état somatique qui sous-tend le trauma — n'a jamais reçu un traitement formel comparable. Le Modèle du Champ Soma est ce traitement. Ensemble avec le cadre de Hopfield, il constitue la première description formelle complète des deux principaux substrats computationnels du cerveau vertébré.

L'article procède comme suit. La Section 2 passe en revue le contexte pertinent dans les modèles cliniques somatiques, et introduit les deux outils théoriques empruntés à la physique et à l'informatique : théorie quantique des champs et fonctions d'énergie de réseau de Hopfield. La Section 3 développe le Modèle du Champ Soma en détail. La Section 4 décrit le paysage d'énergie, incluant les états attracteurs correspondant à fight, flight, freeze, et calm régulé. La Section 5 discute la dissonance et la résolution comme mécanismes d'interaction émotionnelle. La Section 6 décrit l'Instrument du Champ Soma, un outil pratique pour usage thérapeutique. La Section 7 aborde les implications cliniques.

---

# Contexte

## Le Problème Corps-Esprit dans la Pratique Clinique

La neuroscience contemporaine a largement dissous la frontière cartésienne entre corps et esprit. Damasio (1994) a démontré que l'émotion est inséparable de la cognition rationnelle : les patients avec dommage au cortex préfrontal ventromédian — empêchant la génération normale de signaux somatiques — perdent non seulement leur gamme émotionnelle mais aussi leur capacité de prise de décision efficace. Van der Kolk (2014) a documenté extensivement comment les états émotionnels traumatiques sont encodés non seulement dans la mémoire explicite mais dans la posture, le geste, la sensation viscérale, et la régulation autonome. La théorie polyvagale de Porges (2011) a fourni un compte rendu neurobiologique de comment le système nerveux autonome génère trois états hiérarchiquement organisés — vagal ventral (engagement social), sympathique (mobilisation : fight/flight), et vagal dorsal (immobilisation : freeze) — chacun avec des signatures phénoménologiques et comportementales caractéristiques.

Ce que ces cadres partagent est une conviction que les états émotionnels ne sont pas localisés dans le cerveau seul, ni dans le corps seul, mais dans un système couplé qui est le mieux compris comme une seule unité fonctionnelle. Le terme *soma* — du grec pour corps — est utilisé ici pour désigner ce système corps-esprit unifié, suivant la tradition de la psychothérapie somatique.

## Le Felt Sense et l'Émotion Sub-Perceptuelle

Le concept de *felt sense* de Gendlin (1978) est d'une pertinence particulière. Il l'a décrit comme « un genre spécial de conscience corporelle interne... un sens corporel de signification. » Ce n'est pas une émotion au sens ordinaire — pas un sentiment nommé — mais quelque chose de plus diffus : un sens pré-articulé que *quelque chose est là*, présent dans le corps, avant d'avoir été identifié ou nommé. Le Focusing, la méthode thérapeutique que Gendlin a développée, fonctionne précisément en prêtant attention à ce signal pré-seuil et en lui permettant de surgir dans l'articulation consciente.

Le Modèle du Champ Soma fournit un compte rendu formel de ce qu'est le felt sense : c'est l'activité du champ émotionnel sous le seuil perceptuel. Il est réel, causal, et continuellement présent. Il façonne la cognition et le comportement même quand il n'émerge pas comme sentiment nommé.

## Théorie Quantique des Champs : Structure, Pas Métaphore

La Théorie Quantique des Champs (QFT) est le cadre de la physique des particules moderne. Son départ central de la physique classique est la priorité du *champ* sur la *particule*. En QFT, ce que nous appelons particules — électrons, photons — ne sont pas des objets fondamentaux. Ce sont des *excitations* d'un champ sous-jacent : configurations locales, stables d'énergie qui surviennent quand le champ reçoit une perturbation suffisante.

Le vide quantique — l'état fondamental du champ — n'est pas vide. C'est un fond bouillonnant de fluctuations virtuelles : excitations momentanées qui n'ont pas assez d'énergie pour persister comme particules observables. Le vide est actif, mais sous-seuil.

```
  UN MODE DE CHAMP UNIQUE — amplitude au fil du temps
  (ex., un mode du champ électromagnétique ; ou, plus tard, un mode du champ émotionnel)

  │                                    ╭──────────────────╮
  │          ╭──╮              ╭──╮   ╱                    ╲             ╭──
  │   ╭─╮   ╱    ╲    ╭─╮    ╱    ╲ ╱                      ╲    ╭──╮  ╱
  │  ╱   ╲ ╱      ╲  ╱   ╲  ╱      ╳                        ╲  ╱    ╲╱
  T ╱─────╲╱────────╲╯─────╲╯────────────────────────────────╲╱──────────── T
  │         ╲────────╯       ╲──────╯                          ╲────────────
  │
  └──────────────────────────────────────────────────────────────────────► temps

  ←─── VIRTUEL : le champ fluctue mais reste sous-seuil ────────────→ ←RÉEL→
       présent, actif, causalement réel — mais pas localement détectable     ↑
       (le VIDE QUANTIQUE : pas vide ; bouillonnant d'activité)         particule
                                                                          créée
```
*Figure 0. Un mode de champ unique en théorie quantique des champs. Le champ oscille continuellement. Sous le seuil de détection T, les excitations sont sous-seuil — réelles et causalement actives, mais pas détectables comme particules. Le vide quantique n'est pas vide ; c'est un champ en mouvement constant qui ne traverse jamais tout à fait le seuil. Quand l'amplitude traverse T, une particule existe : une excitation localement observable. La même structure — champ toujours présent, conscience seulement quand le seuil est traversé — est le cœur du Modèle du Champ Soma.*

Cet article ne prétend pas que les émotions sont des phénomènes quantiques dans un sens littéral : le champ soma est un champ classique, pas un quantifié. L'affirmation est plus forte et plus spécifique que l'analogie : l'objet mathématique en cours de construction — la fonction de Green d'une variété de champ couplée — est formellement du même *type* que les objets qui surgissent en QFT, différant seulement dans la dimensionnalité de la variété et la nature de la sonde. Ce qui a été précédemment décrit comme une analogie structurelle est ici identifié comme une correspondance formelle : une particule est un pôle dans le propagateur de son champ ; un percept émotionnel conscient est un pôle dans le propagateur du champ soma. Physique différente. Mêmes mathématiques.

Cette correspondance donne au modèle un vocabulaire précis pour l'ensemble suivant d'idées, qui sont centrales à l'observation clinique de l'émotion :

- Une quantité qui existe partout, continuellement, même quand non observée
- Un fond d'activité sous-seuil qui est réel et causalement effectif
- L'émergence de phénomènes observables (sentiments conscients) à travers l'excitation de traversée de seuil de ce fond
- La possibilité d'excitations simultanées multiples qui interagissent les unes avec les autres

*Note (mai 2026) :* Une expérience subséquente (QUANT-EXP-1) démontre que l'extension quantique du paysage de Hopfield utilisé dans ce modèle — remplaçant le processus de Langevin classique par un recuit quantique à champ transverse — produit un *avantage de portée topologique* mesurable : le recuit quantique atteint des bassins attracteurs que la dynamique classique froide ne peut atteindre à aucun niveau de bruit fini. Ceci promeut la correspondance formelle d'une affirmation structurelle à une prédiction empirique testable. Voir l'article compagnon *Quantum Soma and the Penrose Gap* (doi:10.5281/zenodo.20351230) pour les résultats complets et implications théoriques.

Une conséquence supplémentaire suit. Les phénomènes cliniques de l'alexithymie — difficulté à identifier et nommer les sentiments — et son apparent opposé, le débordement émotionnel ou l'hypervigilance, ont toujours été traités comme conditions séparées requérant des explications séparées. Dans le cadrage de la fonction de Green, ils sont la même structure à deux extrêmes du même paramètre : le seuil de perception $T_i$ est trop élevé (la dynamique du volume ne peut traverser dans l'expérience observable) ou trop bas (les fluctuations du volume inondent la frontière sans filtrage). Ceci est structurellement identique à l'un des problèmes ouverts les plus profonds en physique des particules — le **problème de la hiérarchie** — qui demande pourquoi la gravité est si beaucoup plus faible que les autres forces. La réponse standard est que la gravité se propage dans le volume complet de dimension supérieure tandis que les autres forces sont confinées à une brane de dimension inférieure ; le couplage à travers la frontière de la brane détermine la faiblesse apparente. La correspondance du champ soma est exacte : le seuil $T_i$ *est* la brane. La perception est confinée à la frontière unidimensionnelle d'une dynamique de onze dimensions. La hiérarchie de l'expérience émotionnelle — pourquoi le sentiment conscient est tellement plus faible et plus transitoire que l'activité du champ sous-jacente — a la même structure formelle que la hiérarchie des forces.

## Fonctions d'Énergie de Réseau Neuronal et Réseaux de Hopfield

En 1982, John Hopfield (récipiendaire du Prix Nobel de Physique en 2024) a proposé un modèle de mémoire associative basé sur un réseau de neurones interconnectés (Hopfield, 1982). L'insight critique a été emprunté directement de la physique statistique : le réseau pouvait être assigné une **fonction d'énergie** — une quantité scalaire qui décroît avec chaque mise à jour d'état — telle que le réseau évoluerait toujours vers un minimum d'énergie local. Ces minima sont les états stables du réseau : ses mémoires, ou plus précisément, ses *attracteurs*.

Hopfield a observé que la dynamique de son réseau neuronal était mathématiquement identique à celle d'un modèle de verre de spin Ising de la physique de la matière condensée — un système de spins magnétiques en interaction qui minimise son énergie totale en s'alignant ou anti-alignant avec les voisins. La fonction d'énergie qu'il a utilisée est :

$$H(\mathbf{s}) = -\frac{1}{2} \sum_{i,j} W_{ij}\, s_i s_j - \sum_i \theta_i s_i$$

où $\mathbf{s}$ est l'état du réseau, $W_{ij}$ est la force de couplage entre unités $i$ et $j$, et $\theta_i$ est le seuil d'activation de l'unité $i$. Le réseau se déplace toujours dans la direction de $H$ décroissant.

Le Modèle du Champ Soma applique cette fonction d'énergie directement à la dynamique émotionnelle. La *matrice de couplage émotionnel* $W$ encode les relations entre modes émotionnels — quelles émotions s'amplifient les unes les autres, lesquelles se suppriment les unes les autres — et la fonction d'énergie détermine la direction dans laquelle le champ émotionnel évolue naturellement.

Le réseau de Hopfield est un modèle formel du *néocortex* : un système pour stocker des motifs cognitifs et les récupérer à partir d'indices partiels en minimisant une fonction d'énergie. Chaque réseau neuronal artificiel construit depuis McCulloch et Pitts (1943) [@mcculloch1943] — des perceptrons aux réseaux à rétropropagation aux transformers — se situe dans cette lignée néocorticale. Ces systèmes reconnaissent des motifs, prédisent des séquences, et minimisent l'erreur de prédiction avec une sophistication croissante. Aucun d'eux ne possède de système limbique. Ils n'ont pas de valuation interne, pas de modulation d'arousal, pas d'architecture de détection de menace, pas de structure d'attachement, pas d'interoception. Ils ont un cortex très efficace.

Le Modèle du Champ Soma n'ajoute pas à la lignée néocorticale. Il propose la couche architecturale qui n'a jamais été formellement construite : *un système limbique artificiel*.

La mémoire de Hopfield est associative et complétant des motifs ; la mémoire somatique est réinstaurante d'état. Le champ ne se souvient pas seulement de ce qui s'est passé. Il le revit. *Un corps avec un passé.*

Le souhait rapporté plus tard de Hopfield d'avoir incorporé quelque chose d'analogue aux « instincts maternels » dans la fonction d'énergie était, dans cette lecture, pas un désir d'un meilleur cortex. C'était une intuition pointant directement vers le système absent — la couche sous le cortex qui assigne la valeur, enregistre la menace, et tient le corps dans une manière particulière d'être longtemps après l'événement qui l'a causé.

Ceci positionne le Modèle du Champ Soma non comme un supplément à la lignée néocorticale mais comme sa complétion. Les réseaux neuronaux artificiels ont, pendant quatre-vingts ans, été des modèles formels de plus en plus sophistiqués du néocortex : reconnaissance de motifs, prédiction de séquences, minimisation d'erreur. Le cortex a été cartographié dans un détail extraordinaire. Le système limbique — qui assigne la valeur, détecte la menace, module l'arousal, maintient l'attachement, et réinstaure des états somatiques entiers en réponse à des indices partiels — n'a eu aucun traitement formel comparable. La description architecturale du cerveau vertébré était, jusqu'à cet article, à moitié construite.

**Quatre types d'intelligence formelle.** Cet écart architectural peut être situé dans une taxonomie plus large. Quatre quotients ont été proposés pour décrire le paysage de l'intelligence biologique à travers l'usage populaire et scientifique. Ils correspondent aux composants formels de ce modèle avec une exactitude qui n'est pas coïncidente :

| Quotient | Ce qu'il mesure | Substrat biologique | Statut Champ Soma |
|---|---|---|---|
| IQ — cognitif | Reconnaissance de motifs, raisonnement, prédiction | Néocortex | Construit (1943-) : McCulloch & Pitts → Hopfield → transformers |
| EQ — émotionnel | Valuation, arousal, régulation d'affect | Système limbique | **Construit ici** : $W$, $K(\tau)$, $H(\mathbf{e})$, $C_\text{HRV}$, $\dot{H}$ |
| AQ — adversité | Résilience structurelle sous menace | Axe PFC-limbique | **Construit ici** : $S_\text{inst}$, $\partial\|W\|/\partial t$, $C_\text{HRV}^\text{recovery}$ |
| SQ — social | Attunement, théorie de l'esprit, navigation relationnelle | Système miroir, TPJ | *Article suivant* : $\kappa_r$, couplage multi-champs |

*Table 3. Quatre dimensions de l'intelligence biologique mappées sur le Modèle du Champ Soma. La lignée néocorticale (IQ) a été formellement modélisée pendant quatre-vingts ans. L'intelligence émotionnelle (EQ) et la résilience à l'adversité (AQ) sont formalisées ici pour la première fois. L'intelligence sociale (SQ) est définie comme la prochaine extension du cadre.*

AQ — quotient d'adversité — est formellement la capacité de mettre à jour $W$ après l'adversité sans que l'adversité ne devienne permanemment $W$. Sa définition mathématique apparaît dans la Section 3.4 ; sa borne inférieure pathologique est le TSPT-C, dans lequel les trois composants d'AQ sont simultanément compromis (Annexe B.2).

L'implication d'alignement IA suit directement. Les systèmes artificiels actuels ont un haut IQ par construction et zéro EQ, AQ, ou SQ. L'absence de valuation interne signifie que la valuation doit être injectée externement — à travers l'apprentissage par renforcement à partir de feedback humain (RLHF) et techniques liées — qui est structurellement fragile pour la même raison qu'un champ sans couche limbique est fragile : le système n'a pas d'enjeu interne dans ce qu'il fait. La formalisation du Champ Soma spécifie à quoi cet enjeu interne ressemblerait, s'il était jamais construit.

Une note de lignée supplémentaire vaut la peine d'être enregistrée. Ramsauer et al. (2020) ont démontré que les réseaux de Hopfield modernes à état continu sont mathématiquement équivalents au mécanisme d'auto-attention dans les modèles de langage transformer. L'opération d'attention softmax qui pilote les grands modèles de langage contemporains est une étape de récupération de Hopfield. Le Modèle du Champ Soma se situe dans cette même lignée basée sur l'énergie : les équations sous-tendant la mémoire associative, la compréhension du langage, et la réponse au trauma somatique sont, au niveau approprié d'abstraction, les mêmes équations.

Une ironie historique complète l'image. La théorie des cordes n'a pas été découverte comme théorie des cordes. En 1968, Gabriele Veneziano a écrit une amplitude de diffusion — une fonction de réponse encodant comment les particules diffusent — et seulement plus tard Nambu, Nielsen, et Susskind ont identifié la corde comme quel que soit l'objet qui produit cette amplitude [@veneziano1968]. La fonction de réponse est venue avant la chose. Le Modèle du Champ Soma récapitule cet ordre historique délibérément : l'objet primaire est la variété de couplage à onze dimensions ; la corde — le percept conscient unidimensionnel — est ce que la variété produit lorsqu'elle est sondée. Nous conservons la découverte de Veneziano et déclinons de réifier la corde.

---

## Les Correspondances Formelles : Où le Lien a Été Vu

L'analogie structurelle entre QFT et le Modèle du Champ Soma n'est pas simplement conceptuelle. Il y a trois endroits où les équations de différentes disciplines deviennent, après substitution des quantités pertinentes, littéralement la même forme fonctionnelle. Ce qui suit les place côte à côte. Le but n'est pas d'impressionner avec la notation mais de montrer exactement où la reconnaissance s'est produite — le moment où les mêmes lettres grecques sont apparues dans les mêmes positions dans deux domaines qui n'avaient aucune raison préalable d'être connectés.

**Le même Hamiltonien :** modèle de spin Ising (physique de la matière condensée, années 1920) — réseau neuronal de Hopfield (neuroscience computationnelle, 1982) — Modèle du Champ Soma :

$$H_{\text{Ising}}(\boldsymbol{\sigma}) = -\frac{1}{2}\sum_{i,j} J_{ij}\,\sigma_i\,\sigma_j - \sum_i h_i\,\sigma_i$$

$$H_{\text{soma}}(\mathbf{e}) = -\frac{1}{2}\sum_{i,j} W_{ij}\,e_i\,e_j - \sum_i \theta_i\,e_i$$

Remplacez $J_{ij} \to W_{ij}$, $\sigma_i \to e_i$, $h_i \to \theta_i$ : identique. Le physicien, le théoricien des réseaux neuronaux, et le clinicien somatique calculent la même fonction d'énergie sur différents espaces d'état. Le Prix Nobel Hopfield 2024 a été décerné pour avoir découvert cette identité entre la physique des spins et le calcul neuronal ; le Modèle du Champ Soma étend la même identité d'un pas supplémentaire à la dynamique émotionnelle.

**La rotation de Wick — pourquoi la même exponentielle apparaît en MQ et en mémoire :**

En mécanique quantique, l'opérateur d'évolution temporelle est une phase complexe :
$$U(t) = e^{-i\hat{H}t/\hbar}$$

Substituez $t \to -i\tau$ (la *rotation de Wick* — remplacer le temps réel par le temps imaginaire) :
$$e^{-i\hat{H}(-i\tau)/\hbar} = e^{-\hat{H}\tau/\hbar}$$

L'exponentielle complexe oscillante devient une exponentielle décroissante réelle. C'est le poids de Boltzmann $e^{-\beta\hat{H}}$ à $\beta = \tau/\hbar$. L'équation de Langevin $\dot{\mathbf{e}} = -\nabla H + \eta$ est la limite classique de cette dynamique Wick-tournée. Chaque simulation du champ soma exécutant cette équation est, formellement, une intégrale de chemin en temps imaginaire.

**Le même propagateur :** QFT euclidienne (corrélateur à deux points en temps imaginaire pour un champ scalaire massif) — noyau de mémoire de trauma TSPT-C :

$$G_E(\tau) = \langle\phi(0)\,\phi(\tau)\rangle_{\text{QFT}} = \frac{1}{2m}\,e^{-m|\tau|}$$

$$K_{\text{trauma}}(\tau) = \sum_k A_k\,e^{-|\tau|/\tau_k}$$

Même forme. La masse du champ QFT $m$ correspond à $1/\tau_k$ — l'inverse du temps de décroissance de la trace de trauma. Une particule plus lourde a un propagateur de plus courte portée ; une trace de trauma de plus courte vie décroît plus vite. Le traitement thérapeutique (réduisant $A_k$, augmentant $\tau_k$) est, dans le langage QFT, changer la masse et l'amplitude du propagateur jusqu'à ce que la fonction de corrélation s'évanouisse.

Le moment visuel spécifique : le facteur de phase quantique est $e^{-i\omega t}$. Retirez le $i$ (rotation de Wick) et il devient $e^{-\omega\tau}$. Le noyau de mémoire est $e^{-\tau/\tau_k}$. Ce sont la même exponentielle. Le $i$ est la seule différence entre un champ quantique qui oscille et une trace de trauma qui décroît.

| Quantité QFT | Symbole | Analogue Champ Soma | Symbole |
|---|---|---|---|
| Mode de champ | $\phi_k$ | Mode émotionnel | $e_i$ |
| Constante de couplage | $J_{ij}$ | Entrée matrice de couplage | $W_{ij}$ |
| Masse du champ | $m$ | Temps de décroissance inverse | $1/\tau_k$ |
| Amplitude propagateur | $1/2m$ | Amplitude trace trauma | $A_k$ |
| Propagateur euclidien | $G_E(\tau) \propto e^{-m\tau}$ | Noyau de mémoire | $K(\tau) \propto e^{-\tau/\tau_k}$ |
| Énergie du vide | $\langle H \rangle_0$ | Énergie de champ au repos | $H(\mathbf{e}_\text{calm})$ |
| Fluctuation thermique | $k_B T$ | Amplitude de bruit | $\sigma_0$ |
| Rotation de Wick | $t \to -i\tau$ | Langevin temps réel | $\dot{\mathbf{e}} = -\nabla H + \eta$ |

*Table 2. Correspondance formelle entre quantités QFT et analogues du Champ Soma. Chaque ligne est une seule entité mathématique en deux notations. Ces correspondances n'ont pas été construites après coup ; elles sont la raison pour laquelle le cadre QFT a été reconnu comme pertinent.*

**L'identification centrale — particule et percept comme pôles dans leurs propagateurs respectifs.** Les quatre correspondances ci-dessus suivent d'un fait structurel. En QFT, une particule n'est pas un objet séparé du champ. C'est un *pôle* dans le propagateur du champ — la fonction de Green évaluée dans l'espace des moments :

$$\tilde{G}_{\text{QFT}}(k^\mu) = \frac{i}{k^2 - m^2 + i\varepsilon}$$

La particule existe précisément quand le quadri-moment satisfait $k^2 = m^2$ — la *condition on-shell*. La particule est la singularité dans la réponse du champ à une source ponctuelle : la fonction de Green du champ, évaluée à sa propre résonance.

Diagonalisez $W$ avec valeurs propres $\lambda_i$ (les fréquences de résonance naturelles des modes émotionnels). Le propagateur du champ soma — le corrélateur à deux points $\langle e_i(t)\,e_i(t')\rangle$ dans le domaine de fréquence — est :

$$\tilde{G}_{ii}(\omega) = \frac{\sigma_{\text{eff}}^2}{\omega^2 + \lambda_i^2}$$

Un percept émotionnel conscient en mode $i$ existe précisément quand la fréquence d'excitation $\omega$ approche $i\lambda_i$ — la résonance naturelle du mode. Le percept est la singularité dans la réponse du champ soma à une sonde somatique.

Mettant les deux propagateurs côte à côte :

$$\underbrace{\frac{i}{k^2 - m^2 + i\varepsilon}}_{\text{QFT : particule à mass-shell }k^2=m^2}
\qquad\longleftrightarrow\qquad
\underbrace{\frac{\sigma_{\text{eff}}^2}{\omega^2 + \lambda_i^2}}_{\text{Champ Soma : percept à résonance }\omega = i\lambda_i}$$

Les deux sont des pôles dans le propagateur de leur variété de champ respective. Un photon n'est pas le champ électromagnétique ; c'est la fonction de Green du champ évaluée à une résonance. Un éclair d'émotion consciente n'est pas le champ soma ; c'est la fonction de Green du champ évaluée à une résonance de traversée de seuil. Les variétés diffèrent — l'une est le vide d'espace-temps à quatre dimensions, l'autre est la géométrie de couplage émotionnel à onze dimensions. Le type mathématique est le même. Ce n'est pas une analogie.

---

## Le Schéma Corporel, l'Interoception, et la Douleur

Un modèle complet du champ émotionnel doit aborder un phénomène que les comptes rendus psychologiques standard de l'émotion sous-spécifient constamment : le champ n'est pas un modèle du corps physique. C'est le *modèle prédictif* du corps par le système nerveux — une représentation interne continuellement mise à jour de ce que le soma devrait expérimenter, révisée par les signaux interoceptifs entrants.

La preuve clinique de cette distinction est la douleur du membre fantôme [@ramachandran1998]. Les patients qui ont subi une amputation expérimentent régulièrement de la douleur dans le membre absent. La douleur est réelle : elle active les mêmes circuits neuronaux, produit la même souffrance, et répond aux mêmes analgésiques que la douleur d'un membre intact. Le membre est parti. Le modèle neuronal du membre persiste. Ce qui fait mal est la *représentation du cerveau* du pied, pas le pied.

Ce n'est pas une anomalie. C'est la condition normale de toute expérience somatique. Le cerveau ne reçoit pas de signaux bruts du corps — il maintient un modèle prédictif continu du corps (le *schéma corporel*) et génère l'expérience somatique à partir de ce modèle. L'interoception — le sens de l'état corporel interne — est une prédiction, pas une lecture directe [@seth2021]. Le cerveau prédit ce que le cœur devrait faire, ce que les intestins devraient ressentir, où la tension devrait être. Le corps ressenti est le corps prédit.

La conséquence formelle est directe : le vecteur d'état du champ soma $\mathbf{e}(t)$ doit inclure **modes somatiques** — états de douleur, tension régionale, sensation viscérale, activation proprioceptive — aux côtés des modes émotionnels. Ce sont des modes du même champ, gouvernés par la même matrice de couplage $W$. Le $W_{ij}$ entre modes fear et modes de douleur somatique est le compte rendu formel de pourquoi fear amplifie la douleur, pourquoi safety la réduit, et pourquoi la douleur chronique et le TSPT-C sont hautement comorbides. Ce ne sont pas des conditions séparées partageant une corrélation. Ce sont la même architecture attracteur opérant à travers modes émotionnels et somatiques simultanément.

**Membre fantôme comme persistance d'attracteur.** Les modes somatiques d'un membre amputé ne disparaissent pas de $W$ quand le membre est retiré. Le modèle neuronal persiste. Quand les modes d'intention-de-mouvement sont activés — tentant de bouger le pied absent — les modes de sensation-de-pied sont co-activés via $W$. Si la co-activation dépasse le seuil, elle est expérimentée comme douleur. La boîte miroir de Ramachandran fournit une entrée visuelle qui désaffirme l'erreur de prédiction : nouvelle preuve sensorielle que le membre bouge, réduisant la co-activation pilotée par le couplage, et donc réduisant la douleur. C'est $W \to W'$ : la thérapie comme réécriture structurelle du champ.

**Le trait d'union porteur de charge.** Le terme *émotionnel-somatique* dans la littérature clinique n'est pas un composé stylistique. Le trait d'union marque une affirmation ontologique : les états émotionnels et les états somatiques ne sont pas deux choses séparées qui se corrèlent. Ce sont deux aspects du même champ. La matrice de couplage $W$ est précisément le trait d'union, rendu formel.

**Implication thérapeutique.** Les thérapies somatiques — scan corporel, travail sensorimoteur, stimulation bilatérale de l'EMDR — fonctionnent non sur le corps physique mais sur le modèle du corps par le cerveau. Elles fournissent une nouvelle preuve interoceptive qui met à jour la prédiction. Elles changent $W$. La thérapie ne répare pas le tissu. Elle met à jour le modèle.

---

## Correspondance avec les Représentations Émotionnelles Existantes

Une objection raisonnable à tout nouveau cadre est : *il y a déjà beaucoup de structure ici dehors.* C'est vrai. La littérature de recherche sur l'émotion contient plusieurs systèmes représentationnels bien développés, et le Modèle du Champ Soma doit être positionné relativement à eux. La réponse courte est que chaque représentation existante est *descriptive* ; le Modèle du Champ Soma est *dynamique*. La réponse plus longue suit.

**Taxonomies catégoriques** (Ekman 1972 ; Plutchik 1980 ; Parrot 2001) assignent des noms et appartenance hiérarchique aux états émotionnels. Ce sont des ontologies au sens formel : une T-Box de classes et relations de sous-classe. La roue de Plutchik définit additionnellement une opération de *blend* — Love := Joy $\sqcap$ Trust, Awe := Fear $\sqcap$ Surprise — qui est précisément la construction OWL2 `intersectionOf`. Ces systèmes vous disent comment appeler un état. Ils ne vous disent pas comment un état évolue, ou dans quel attracteur un système se stabilise quand deux mécanismes tirent simultanément.

**Modèles dimensionnels** (Russell 1980 ; Mehrabian et Russell 1974) intègrent les émotions dans un espace continu, canoniquement Valence × Arousal (le *circumplex*), parfois étendu à Pleasure × Arousal × Dominance. Ces modèles capturent les *coordonnées* d'un état. Le paysage d'énergie du Modèle du Champ Soma — la fonction $H(\mathbf{e})$ sur l'espace-émotion — est la généralisation dynamique du circumplex : le circumplex est un instantané de positions ; le paysage d'énergie est la surface sur laquelle le champ se déplace. Les attracteurs stables de $H$ sont les catégories émotionnelles ; leurs coordonnées sont les positions du circumplex.

**Modèles de processus et d'appraisal** (Scherer 1999 ; Frijda 1986 ; le modèle OCC d'Ortony, Clove et Collins 1988) décrivent la *séquence d'évaluations* à travers laquelle un stimulus devient une émotion. Ils sont plus proches de la dynamique du Champ Soma — ils incluent des étapes temporelles — mais ils sont déterministes et à un seul fil : une chaîne d'appraisal, une sortie. Le Champ Soma remplace ceci par une mise à jour de champ parallèle : tous les modes évoluent simultanément, gouvernés par la matrice $W$ complète.

**Schémas spécifiques à la musique** (BRECVEMA, Juslin et Västfjäll 2008 ; Juslin *et al.* 2011 ; GEMS, Zentner *et al.* 2008) sont les antécédents les plus proches du présent modèle. Le cadre BRECVEMA identifie huit mécanismes psychologiques distincts à travers lesquels la musique évoque l'émotion — Brain stem reflex, Rhythmic entrainment, Evaluative conditioning, Contagion, Visual imagery, Episodic memory, Musical expectancy, Aesthetic judgement — chacun avec des origines évolutionnaires distinctes, vitesses de traitement, et substrats neuronaux. Ces mécanismes sont les *propriétés d'objet* de l'ontologie d'induction émotionnelle : ils spécifient quelles caractéristiques musicales activent quelles sorties émotionnelles. Juslin identifie explicitement le problème ouvert : *« Explorer comment diverses émotions musicales surviennent à travers l'interaction de multiples mécanismes psychologiques est une entreprise excitante qui vient juste de commencer »* [@juslin2011handbook, p. 638]. La matrice de couplage $W$ est la réponse formelle à ce problème ouvert. Où BRECVEMA donne une liste de mécanismes avec sorties caractéristiques, le Champ Soma donne le tenseur d'interaction $W_{ij}$ qui spécifie, avec précision numérique, ce qui se passe quand les mécanismes $i$ et $j$ tirent concurremment.

La connexion plus profonde est spectrale. Les *modes propres* de $W$ — les directions dans l'espace-émotion qui évoluent indépendamment — sont les résonances naturelles du champ soma : les motifs avec lesquels le champ sonne quand frappé. Les mécanismes BRECVEMA sont des entrées : ils excitent des lignes spécifiques de $W$. Le spectre propre de $W$ est la réponse : l'ensemble de fréquences que la variété peut soutenir. Où BRECVEMA est une taxonomie de *stimuli*, le spectre propre de $W$ est une taxonomie de *réponses*. Le problème ouvert de Juslin — comment les mécanismes interagissent — est la question de comment l'espace-stimulus mappe sur l'espace-mode-propre à travers $W$. La Section 3.3 développe ceci.

**Cartes corporelles** (Nummenmaa *et al.* 2014) mappent les émotions à leur distribution somatique — où dans le corps chaque émotion est ressentie. Ce sont précisément le support spatial des modes du champ soma : la configuration de champ correspondant à un état attracteur est la carte corporelle de cette émotion. Les cartes corporelles sont des mesures des attracteurs ; le Champ Soma est le système dynamique qui les génère.

**La table de correspondance formelle** étend la Table 2 pour inclure ces systèmes :

| Représentation existante | Ce qu'elle capture | Équivalent Champ Soma |
|---|---|---|
| Catégories Ekman | Étiquettes attracteur (noms) | Valeurs de $\mathbf{e}$ aux minima d'énergie |
| Dyades Plutchik ($A \sqcap B$) | Attracteurs de blend | États métastables entre deux minima d'énergie |
| Circumplex Russell | Coordonnées (valence, arousal) | Projection de $H(\mathbf{e})$ sur deux axes |
| Arbre d'appraisal OCC | Processus séquentiel à chemin unique | Trajectoire unique dans le champ complet |
| Mécanismes BRECVEMA | Propriétés d'objet : stimulus → émotion | Lignes de $W$ : mécanisme $i$ active mode $j$ |
| Cartes corporelles (Nummenmaa) | Support spatial de chaque attracteur | Structure modale de $\mathbf{e}$ à chaque minimum |

Aucune de ces correspondances ne requiert de modifier soit les représentations existantes soit le Modèle du Champ Soma. Ce sont des conséquences de la structure du modèle. La machinerie formelle pour explorer ces correspondances — typer les mécanismes BRECVEMA comme constructeurs inductifs Lean, les blends Plutchik comme intersections de types, les profils de mécanismes comme propositions décidables — est développée dans le fichier compagnon `src/EmotionOntology.lean`.

---

# Le Modèle du Champ Soma

Le champ est primaire. L'émotion ressentie est secondaire — c'est ce qui s'enregistre quand le champ est sondé. C'est la même relation ontologique qu'entre un champ quantique et une particule : le champ existe continuellement et partout ; la particule est ce que vous observez au moment de la mesure. Le Modèle du Champ Soma ne décrit pas de quoi les émotions sont *faites*. Il décrit la variété dont la réponse impulsionnelle *est* l'expérience émotionnelle consciente.

## Les Émotions comme Champ d'Onde Persistant

L'affirmation fondamentale du Modèle du Champ Soma est simple : les émotions ne sont pas des événements. Elles sont un *champ* — une quantité distribuée, continue définie sur le soma entier (système corps-esprit) en tout temps.

Ce champ a deux composants couplés :

1. **L'onde somatique** $\mathbf{E}_\text{body}(x,t)$ : distribuée à travers le corps comme motifs de sensation viscérale, tonus musculaire, proprioception, interoception, et état autonome.
2. **L'onde neurale** $\mathbf{E}_\text{neural}(x,t)$ : distribuée à travers le système nerveux comme motifs d'activation dans les circuits neuraux corticaux, sous-corticaux, et périphériques.

Ces deux composants ne sont pas des systèmes séparés. Ils sont couplés — chacun influençant continuellement l'autre. Le champ émotionnel total est leur état combiné :

$$\mathbf{E}(x,t) = \mathbf{E}_\text{body}(x,t) \otimes \mathbf{E}_\text{neural}(x,t)$$

Le champ est caractérisé par :

- **Multiplicité** : multiples modes émotionnels peuvent être simultanément actifs et interférant
- **Continuité** : il existe à tout moment, pas seulement durant les épisodes de sentiment conscient
- **Distribution spatiale** : différents aspects du champ sont localisés dans différentes régions du soma (l'observation clinique familière que grief est ressenti dans la poitrine, fear dans les intestins, anger dans la mâchoire et les poings)
- **Dynamique temporelle** : le champ évolue continuellement, piloté par la fonction d'énergie

![](figures/fig1_architecture.pdf){ width=90% }
*Figure 1. Le Champ Soma. Le corps et le cerveau ne sont pas des contenants séparés d'émotion mais deux composants couplés d'un seul champ d'onde distribué. Aucun n'est primaire ; chacun modifie continuellement l'autre. Les symboles ≋ indiquent que l'activité d'onde est toujours présente dans chaque région, pas seulement durant les épisodes de sentiment conscient.*

## Le Seuil de Perception

Toute l'activité dans le champ émotionnel n'est pas consciemment perçue. Le champ a un **seuil de perception** $T_i$ pour chaque mode émotionnel $i$. Sous ce seuil, le mode émotionnel est sub-perceptuel : il existe, il influence le comportement et la physiologie, mais il n'émerge pas comme sentiment conscient nommé.

$$\text{Émotion } i \text{ est consciemment perçue} \iff |\mathbf{E}_i(t)| > T_i$$

Cette traversée de seuil correspond précisément à l'analogie d'excitation QFT : le mode émotionnel se comporte comme une particule virtuelle qui a accumulé assez d'énergie pour devenir réelle — pour émerger du fond sous-seuil et entrer dans la conscience.

Ceci rend compte d'une gamme de phénomènes cliniquement significatifs :

| Observation Clinique | Compte Rendu Champ Soma |
|---|---|
| Patient rapporte aucun sentiment mais montre signes physiologiques de détresse | Activité de champ sous-seuil sous $T_i$ |
| Soudain débordement inattendu d'émotion en session | Traversée de seuil rapide après accumulation graduelle |
| Émotion ressentie somatiquement mais pas nommée | Seuil traversé dans $\mathbf{E}_\text{body}$, pas encore dans $\mathbf{E}_\text{neural}$ |
| Alexithymie (difficulté à identifier les sentiments) | $T_i$ élevé — seuil haut requérant plus d'énergie pour traverser |
| Hypervigilance / débordement émotionnel | $T_i$ abaissé — seuil réduit, le champ traverse facilement vers conscient |

*Table 1. Observations cliniques mappées sur le modèle de seuil de perception.*

![](figures/fig2_threshold.pdf){ width=90% }
*Figure 2. Le seuil de perception T_i pour un mode émotionnel unique. Le champ est actif continuellement (trace inférieure). L'expérience consciente survient seulement quand l'amplitude dépasse T_i (trace supérieure). Tout sous la ligne est encore là — façonnant le corps et le comportement avant qu'il puisse être nommé.*


![](figures/fig0_field_mode.pdf){ width=95% }
*Figure 0. Activité continue du champ soma (bleu) avec un événement unique de traversée de seuil. Le champ est toujours actif ; l'expérience consciente (ombrée) survient seulement quand l'amplitude dépasse le seuil de perception θ (rouge pointillé). Sous le seuil : réel, causalement actif, mais pas encore conscient.*

## L'Interaction des Modes Émotionnels

Multiples modes émotionnels sont simultanément actifs dans le champ à tout moment. Ils ne coexistent pas simplement : ils interagissent. La nature de ces interactions est encodée dans la **matrice de couplage émotionnel** $W$, où $W_{ij}$ représente l'influence du mode émotionnel $j$ sur le mode émotionnel $i$.

- Si $W_{ij} > 0$ : l'émotion $j$ amplifie l'émotion $i$ (ex., fear peut amplifier shame)
- Si $W_{ij} < 0$ : l'émotion $j$ supprime l'émotion $i$ (ex., calm supprime l'anxiété)
- Si $W_{ij} = 0$ : les émotions $i$ et $j$ sont indépendantes

Le champ évolue selon le gradient d'énergie :

$$\dot{\mathbf{e}}(t) = -\nabla H(\mathbf{e}) + \eta(t)$$

où $\eta(t)$ représente les fluctuations continues de bas niveau du champ sub-perceptuel — l'équivalent émotionnel du bruit du vide quantique. Le champ est toujours en mouvement, cherchant toujours une énergie inférieure, jamais au repos absolu.

---

## L'Architecture à Trois Couches

Le système nerveux qui implémente le champ soma n'est pas architecturalement plat. Trois couches hiérarchiquement organisées contribuent à la dynamique du champ, chacune correspondant à un substrat évolutionnaire distinct et à un rôle distinct dans le modèle. La littérature clinique (Porges, 2011 ; van der Kolk, 2014 ; Ogden et al., 2006) converge sur cette stratification ; ce qui suit est son expression formelle.

**Couche 1 — Tronc cérébral / ligne de base autonome.** Les structures les plus anciennes : noyaux vagaux, systèmes d'arousal, machinerie interoceptive. Dans le modèle, cette couche est représentée par le terme de bruit et, spécifiquement, par la cohérence de variabilité du rythme cardiaque $C_{\text{HRV}}$, qui module l'amplitude de bruit effective à travers le champ entier :
$$\sigma_{\text{eff}} = \frac{\sigma_0}{C_{\text{HRV}}}$$
Une haute cohérence HRV rétrécit le bruit effectif, stabilisant le champ dans son attracteur actuel. C'est le mécanisme du biofeedback HRV comme intervention régulatrice : il ne cible aucun mode émotionnel spécifique mais abaisse le plancher de fluctuation du champ entier.

**Extension de Couche 1 : accélération cardiaque et inclinaison du paysage.** Le terme $C_{\text{HRV}}$ mesure l'*état actuel* de régularité cardiaque — où le cœur est. Une quantité complémentaire est $\dot{H}(t)$, la première dérivée temporelle du rythme cardiaque, en unités de battements/s$^2$. C'est l'**accélération cardiaque** : pas ce qu'est le rythme cardiaque, mais où il va.

Le parallèle dimensionnel avec la gravité est exact : l'accélération gravitationnelle $g$ porte des unités m/s$^2$ ; l'accélération cardiaque $\dot{H}$ porte des unités battements/s$^2$. Les deux sont des accélérations ; les deux décrivent un champ de force plutôt qu'une position. La gravité ne vous dit pas où une masse-test est — elle vous dit comment elle se déplacera ensuite. L'accélération cardiaque vous dit pas le BPM actuel mais la direction du prochain : l'état N+1.

Dans le champ soma, $\dot{H}(t)$ entre dans la dynamique non comme modulation de bruit mais comme **inclinaison de paysage** — un biais variant dans le temps ajouté à l'Hamiltonien qui incline la fonction d'énergie vers attracteurs d'activation ou de repos :

$$H(\mathbf{e}, t) = H_0(\mathbf{e}) - \alpha\,\dot{H}(t)\,\boldsymbol{\beta}\cdot\mathbf{e}$$

où $\alpha > 0$ est la constante de couplage cardiaque-somatique et $\boldsymbol{\beta}$ est un vecteur de couplage de mode (à l'ordre dominant, $\boldsymbol{\beta} = \mathbf{1}$ : l'inclinaison agit uniformément à travers tous les modes). Quand $\dot{H}(t) > 0$ (cœur accélérant), le paysage s'incline vers des états d'activation plus élevés avant qu'un seuil cognitif ou affectif ne soit traversé. Quand $\dot{H}(t) < 0$ (cœur décélérant), il s'incline vers le repos. L'équation complète à trois couches incluant le terme d'accélération cardiaque est :

$$\dot{\mathbf{e}}(t) = -\nabla H_0(\mathbf{e}) + \alpha\,\dot{H}(t)\,\boldsymbol{\beta}
  + R_{\text{PFC}}(\mathbf{e}, t)
  + \frac{\sigma_0}{C_{\text{HRV}}}\,\xi(t)$$

Les deux termes cardiaques servent des fonctions distinctes : $C_{\text{HRV}}$ (état) module le plancher de bruit ; $\dot{H}$ (accélération) incline le paysage déterministe. Les deux sont nécessaires pour un compte rendu complet de l'influence cardiaque sur le champ.

**Valeur clinique prédictive.** Un patient avec BPM = 90 et $\dot{H} = +4$ battements/s$^2$ approche le seuil ; un avec BPM = 90 et $\dot{H} = -4$ battements/s$^2$ s'en retire. L'instantané est identique ; les trajectoires sont opposées. L'accélération cardiaque est donc un signal d'alerte précoce pour les traversées de seuil — détectable à la Couche 1 avant que le champ émotionnel à la Couche 2 n'ait traversé son seuil. Ceci a un support indépendant en cardiologie : Bauer et al. (2006) ont démontré que les *capacités d'accélération* et de *décélération* du rythme cardiaque — estimations de $\dot{H}$ sur une fenêtre cardiaque — portent une information pronostique indépendante des mesures HRV conventionnelles.

**Le principe d'équivalence somatique.** Le terme d'accélération cardiaque $\alpha\,\dot{H}\,\boldsymbol{\beta}$ est structurellement identique dans l'équation à tout autre terme de forçage. De la perspective du champ lui-même — de l'expérience consciente — l'activation pilotée cardiaque est indistinguable de l'activation pilotée par événement. Une soudaine accélération du rythme cardiaque incline le paysage par exactement le même mécanisme qu'une menace externe ou un souvenir intrusif. Le champ n'a pas d'accès à l'origine de l'inclinaison. C'est le compte rendu formel d'un phénomène cliniquement bien documenté : l'anxiété initiée par irrégularité cardiaque (arythmie, hypotension posturale, caféine, exertion) est expérimentée comme causée émotionnellement, parce que le signal somatique est identique. La désambiguïsation requiert soit une mesure externe soit une enquête interoceptive délibérée qui peut distinguer les deux sources.

**Couche 2 — Système limbique / mémoire émotionnelle.** Le substrat primaire du Modèle du Champ Soma. La matrice de couplage $W$, le noyau de mémoire $K(\tau)$, l'Hamiltonien $H(\mathbf{e})$, et le seuil $T$ appartiennent tous ici. La couche limbique stocke les états émotionnels-somatiques et les réinstaure en réponse à des indices corporels partiels : un réseau de Hopfield continu, asymétrique, temporellement étendu opérant sur états somatiques plutôt que sur motifs cognitifs. C'est la couche architecturale qui a été absente de chaque réseau neuronal artificiel depuis McCulloch et Pitts (1943) [@mcculloch1943]. Le cortex a été modélisé de nombreuses fois ; le système limbique non.

**Plasticité structurelle sous adversité.** Le cadre du Champ Soma permet une caractérisation formelle de la résilience du champ sous conditions adverses. Définissez l'*indice de plasticité* $\Pi$ comme un composite de trois propriétés de champ mesurables :

$$\Pi \;=\; \frac{1}{S_{\text{inst}}} + \left.\frac{\partial \|W\|}{\partial t}\right|_{\text{adversity}} + C_{\text{HRV}}^{\text{recovery}}$$

Les trois termes correspondent à : (i) combien accessibles les attracteurs d'état régulé restent sous adversité ($1/S_{\text{inst}}$, accessibilité d'instanton — Section 4.4) ; (ii) combien la matrice de couplage peut structurellement s'adapter suite à une traversée de seuil ($\partial \|W\|/\partial t$, le composant de plasticité) ; et (iii) à quelle vitesse le plancher HRV se rétablit après activation ($C_{\text{HRV}}^{\text{recovery}}$, le composant de résilience régulatrice). Le TSPT Complexe est la présentation clinique de $\Pi$ chroniquement bas à travers les trois termes simultanément : hautes barrières aux attracteurs régulés, un $W$ rigide dominé par configurations de menace, et $C_{\text{HRV}}$ de rétablissement diminué. La plasticité structurelle est la capacité du champ de mettre à jour $W$ dans le sillage de l'adversité sans que l'adversité ne *devienne* permanemment $W$.

**Couche 3 — Néocortex / couche régulatrice préfrontale.** Modulation top-down de la Couche 2, représentée comme terme régulateur $R_{\text{PFC}}(\mathbf{e}, t)$. La dynamique de champ complète devient :

$$\dot{\mathbf{e}}(t) = -\nabla H(\mathbf{e}(t))
  + R_{\text{PFC}}(\mathbf{e}, t)
  + \frac{\sigma_0}{C_{\text{HRV}}}\, \xi(t)$$

$R_{\text{PFC}}$ représente l'attention volontaire, la technique thérapeutique, et la réévaluation consciente agissant sur le champ. Ce n'est pas une correction de la Couche 2 mais une modulation d'elle. Sous engagement thérapeutique soutenu, $R_{\text{PFC}}$ participe à la modification structurelle $W \to W'$ constituant la transformation vers l'avant (Section 7).

Le **seuil $T$ est la frontière Couche 2 / Couche 3** : la dynamique sous-seuil est traitée limbiquement et reste sous la conscience consciente ; les événements de traversée de seuil entrent dans la Couche 3 et deviennent disponibles pour la narrative, la construction de sens, et la réponse volontaire. C'est la base formelle pour l'observation clinique que l'insight sans activation somatique est limité, et l'activation somatique sans engagement de Couche 3 ne peut produire de changement structurel : les couches sont couplées, pas indépendantes. $R_{\text{PFC}}$ requiert une traversée de seuil afin d'avoir quelque chose avec quoi travailler.

L'équation de Langevin à deux termes introduite dans la Section 3.3 est le cas spécial de Couche 2 ($R_{\text{PFC}} = 0$, $C_{\text{HRV}} = 1$). Toutes les sections subséquentes développent ce cas spécial. L'équation complète à trois couches est la forme générale.

---
