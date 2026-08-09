
# Chapitre 3 : Le Paysage d'Énergie

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   «La nature ne crée pas les montagnes et les vallées au hasard.│
  │    Elles sont façonnées par les forces qui les sous-tendent.»  │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **LEARNING OBJECTIVES**
>
> À la fin de ce chapitre, vous comprendrez :
>
> - Pourquoi certains états émotionnels sont stables et d'autres transitoires
> - La signification d'«attracteur» et de «bassin d'attraction»
> - Ce qu'est l'Hamiltonien et pourquoi il organise le modèle
> - Pourquoi vous continuez à revenir à des états émotionnels familiers même quand vous ne le voulez pas

---

## 3.1 Collines et Vallées

Imaginez placer une balle sur un paysage vallonné. Si vous la placez au fond d'une vallée et lui donnez une petite poussée, elle roule loin d'où vous l'avez poussée — puis roule en retour. La vallée est stable. Le fond de la vallée est un *attracteur* : la balle est attirée vers lui depuis les positions voisines.

Si vous placez la balle au sommet d'une colline et lui donnez une petite poussée, elle roule loin du sommet — et continue. Le sommet est *instable*. De petites perturbations grandissent en grands départs.

La même géométrie s'applique aux états émotionnels.

Certains états émotionnels sont au fond de vallées dans le paysage du corps : ils sont stables, c'est là que le système tend à se reposer, et les perturbations qui éloignent le corps d'eux sont suivies d'un retour. D'autres états sont au sommet de collines : ce sont des configurations instables que le système traverse en chemin entre les vallées.

La question cruciale — la question qui distingue un système nerveux régulé d'un système dérégulé, et distingue le paysage d'une personne de celui d'une autre — est : où sont les vallées ? Quelle est leur profondeur ? Leur largeur ? Combien y en a-t-il ?

![Figure 3.1. Le paysage d'énergie émotionnel (contour 2D). Quatre bassins attracteurs sont visibles : Calm (large, le plus profond — le minimum global d'un système nerveux régulé), Freeze (étroit et très profond — facile à y tomber, difficile à quitter), Fight et Flight (profondeur intermédiaire). Le système roule vers le bas vers le bassin le plus proche ; la profondeur contrôle la difficulté d'évasion et la largeur contrôle la résilience à la perturbation. *Figure originale de l'auteur.*](figures/fig3a_energy_landscape.png){width=95%}

## 3.2 Attracteurs et Bassins

Un **attracteur** est un état stable — un fond de vallée. Un **bassin d'attraction** est l'ensemble de tous les points à partir desquels le système roule vers un attracteur donné : la «zone de captage» de la vallée.

Pour un système nerveux régulé, l'attracteur primaire est une version de l'engagement social calme — l'état vagal ventral de la Théorie Polyvagale. Le bassin est large : une grande gamme de perturbations (émotions, sensations, situations sociales) se résolvent toutes en retour à cet état de repos. Le système est résilient.

Pour un système nerveux modifié par le trauma, le paysage a changé. Un second attracteur — l'hypervigilance, la préparation d'alerte, l'état de mobilisation sympathique — peut être devenu profond et large. L'attracteur calme peut toujours exister mais son bassin s'est rétréci : il faut très peu pour faire basculer le système hors du calme et dans l'alerte. Et un troisième attracteur — l'état freeze, le shutdown vagal dorsal — peut être très profond en effet : une fois que le système y bascule, l'évasion requiert une grande entrée d'énergie.

Ce n'est pas une métaphore pour ce que le trauma «ressent». C'est une description de la dynamique réelle du système.

![Figure 3.2. Carte de bassin d'attraction. Chaque point dans l'espace d'état est coloré par l'attracteur vers lequel il s'écoule sous descente de gradient : bleu = Calm, violet = Freeze, orange = Fight, vert = Flight. Le bassin calm domine un paysage régulé. Freeze occupe une petite zone mais est disproportionnellement profond — un entonnoir étroit. Les frontières entre bassins sont les séparatrices : seuils invisibles dans l'espace d'état qui déterminent à quelle vallée une perturbation donnée se résout. *Figure originale de l'auteur.*](figures/figB1_attractor_basins.png){width=90%}

## 3.3 L'Hamiltonien

Le paysage a un nom en physique : l'**Hamiltonien**. Noté $H$, c'est une fonction qui assigne une valeur d'énergie à chaque état possible du système.

Pour le champ soma, l'Hamiltonien prend la forme :

$$H(\mathbf{e}) = -\frac{1}{2}\sum_{i,j} W_{ij}\, e_i\, e_j - \sum_i \theta_i\, e_i$$

Lisons ceci en langage clair.

Le premier terme, $-\frac{1}{2}\sum_{i,j} W_{ij}\, e_i\, e_j$, capture les *interactions entre modes émotionnels*. $W_{ij}$ est le couplage entre le mode $i$ et le mode $j$ — combien fortement ils s'influencent. Quand fear est élevé, est-ce que shame monte avec ? Quand calm est présent, est-ce que anger tombe ? La matrice $W$ encode toutes ces influences mutuelles. Le signe moins signifie que le couplage aligné (modes se renforçant mutuellement) abaisse l'énergie — rend l'état plus stable.

Le second terme, $-\sum_i \theta_i\, e_i$, capture les *seuils individuels* de chaque mode. $\theta_i$ est le biais du mode $i$ — combien le système tend vers ou s'éloigne de lui en l'absence de couplage. Un mode avec un grand $\theta_i$ positif a une tendance naturelle vers une activation élevée.

La dynamique — la façon dont le champ se déplace à travers l'espace d'état au fil du temps — découle de cette fonction d'énergie. Le champ se déplace toujours *vers le bas* : vers des valeurs plus basses de $H$.

$$\dot{\mathbf{e}} = -\nabla H(\mathbf{e}) + \eta(t)$$

Cette équation dit : le taux de changement de l'état émotionnel ($\dot{\mathbf{e}}$) est égal au gradient négatif de l'énergie (la direction de descente la plus raide sur le paysage) plus un terme de bruit $\eta(t)$ représentant les petites fluctuations aléatoires de variation physiologique et environnementale. Le système roule toujours vers la vallée la plus proche, avec une petite quantité de bruit qui le pousse occasionnellement par-dessus une colline dans un bassin différent.

Le terme de bruit a une structure plus profonde. Le *niveau* de bruit — combien larges sont les fluctuations — est défini par le système nerveux autonome, spécifiquement par la variabilité du rythme cardiaque (HRV) : une cohérence élevée dans le rythme cardiaque rétrécit le bruit, stabilisant le champ ; une HRV faible l'élargit. Mais il y a une seconde quantité cardiaque, plus prédictive : l'**accélération cardiaque** $\dot{H}$ — le taux auquel le rythme cardiaque *change*. Un rythme cardiaque montant prédit l'approche d'un seuil ; un rythme cardiaque tombant prédit le retrait de l'un d'eux. Le BPM actuel vous dit où vous êtes. L'accélération du BPM vous dit où vous allez ensuite.

> **GOING DEEPER : La Gravité et le Battement Cardiaque**
>
> La gravité, en unités SI, est mesurée en mètres par seconde au carré (m/s²) — c'est une *accélération*, pas une vitesse. Elle vous dit non pas où est un objet tombant, mais à quelle vitesse sa vélocité change : où il sera ensuite.
>
> L'accélération cardiaque — le taux de changement du rythme cardiaque — a des unités de battements/s². Même type, dimension physique différente. Et le même caractère logique : elle vous dit non pas ce qu'est le BPM, mais où il se dirige. N+1, pas N.
>
> Dans le champ soma, l'accélération cardiaque agit comme une **inclinaison de paysage** : elle incline la fonction d'énergie vers l'activation ou le repos avant qu'aucun seuil émotionnel ne soit traversé. Quand le cœur s'accélère, le champ est tiré vers des états de plus haute énergie par une force qu'il ne peut voir et ne peut toujours attribuer correctement. Une certaine anxiété qui semble émotionnellement causée est cardiaque dans son origine — le champ ne peut distinguer les deux de l'intérieur. C'est le principe d'équivalence somatique : vous ne pouvez dire, à partir de votre propre expérience, si votre paysage émotionnel s'est incliné parce que quelque chose s'est passé, ou parce que votre cœur s'est accéléré en premier.
>
> Cliniquement : surveiller la *direction* du changement du rythme cardiaque, pas seulement son niveau, donne un avertissement plus précoce de l'approche du seuil que tout autre signal non invasif.

---

> **GOING DEEPER : Pourquoi les Physiciens Adorent l'Hamiltonien**
>
> L'Hamiltonien a été introduit par William Rowan Hamilton dans les années 1830 comme un moyen de réécrire les équations de Newton sous une forme plus élégante. Ce que Hamilton a découvert, c'est que la trajectoire de tout système physique — le chemin qu'il prend à travers son espace d'état au fil du temps — peut être dérivée entièrement d'une seule fonction scalaire $H$. Vous n'avez pas besoin de décrire toutes les forces. Vous avez juste besoin du paysage d'énergie, et la dynamique en découle.
>
> En mécanique quantique, l'opérateur Hamiltonien $\hat{H}$ joue le même rôle : il détermine comment un état quantique évolue au fil du temps à travers l'équation de Schrödinger, $i\hbar\,\partial_t\psi = \hat{H}\psi$. Les valeurs propres de $\hat{H}$ sont les niveaux d'énergie autorisés.
>
> Dans le Modèle du Champ Soma, $H(\mathbf{e})$ n'est ni newtonien ni quantique : c'est l'Hamiltonien d'un système stochastique classique (un système de Langevin), où la dynamique est la descente de gradient avec bruit. Mais la structure mathématique — une fonction d'énergie scalaire qui détermine tout le reste — est identique.
>
> Ce n'est pas une coïncidence. C'est parce que «un système a des états stables auxquels il retourne» est un principe physique très général, et l'Hamiltonien est la manière la plus générale de le formaliser.

---

## 3.4 La Matrice de Couplage

La matrice $W$ — la matrice de couplage — est l'objet central du modèle. Elle encode l'architecture émotionnelle d'un système nerveux : quels modes s'excitent mutuellement, lesquels s'inhibent, à quelle force, et dans quelle direction.

Pour un système nerveux neurotypique et régulé, $W$ a une propriété mathématique spécifique : elle est *symétrique*. $W_{ij} = W_{ji}$ : l'influence du mode $i$ sur le mode $j$ est égale à l'influence du mode $j$ sur le mode $i$. Cette symétrie n'est pas accessoire. C'est ce qui garantit l'existence d'une fonction d'énergie : si $W$ n'est pas symétrique, la dynamique ne peut être écrite comme une descente de gradient, et le système peut ne pas avoir de points fixes stables du tout. Il peut cycler indéfiniment.

Le trauma, dans ce modèle, est une modification de $W$ qui brise cette symétrie. Un système nerveux traumatisé a des couplages qui ne s'équilibrent pas : fear active shame plus fortement que shame n'active fear ; l'hypervigilance active la réponse freeze plus facilement que la réponse freeze ne se résout en retour à l'hypervigilance. Les couplages asymétriques créent des flux directionnels dans le paysage — des attracteurs qui sont faciles à y tomber et difficiles à en sortir.

C'est la base formelle de l'observation clinique que le trauma se sent souvent comme une roue à cliquet à sens unique.

---

> **KEY TERMS**
>
> **Attracteur** — un état stable dans le paysage d'énergie ; une vallée vers laquelle le champ roule depuis des positions voisines.
>
> **Bassin d'attraction** — la région de l'espace d'état à partir de laquelle le système s'écoule vers un attracteur donné.
>
> **Hamiltonien** — la fonction d'énergie $H(\mathbf{e})$ qui organise la dynamique ; la description mathématique du paysage.
>
> **Matrice de couplage $W$** — la matrice encodant les interactions entre modes émotionnels ; façonne le paysage en déterminant quels états abaissent l'énergie.
>
> **Seuil $\theta_i$** — le biais individuel du mode émotionnel $i$ ; décale son niveau de repos naturel.

---

> **CHAPTER SUMMARY**
>
> Les états émotionnels sont des points dans un paysage façonné par l'Hamiltonien $H$. Les attracteurs sont des états stables (fonds de vallées) ; les bassins d'attraction sont les régions à partir desquelles le système roule vers chaque attracteur. La dynamique — descente de gradient avec bruit — se déplace toujours vers une énergie plus basse. La matrice de couplage $W$ encode les interactions qui façonnent le paysage. La symétrie de $W$ garantit des attracteurs stables ; l'asymétrie (introduite par le trauma) crée des flux directionnels difficiles à inverser.

---

![Figure 3.3. Coupe transversale d'énergie 1D le long d'un axe principal du paysage. La hauteur de chaque barrière entre bassins détermine la probabilité de transition : un puits Freeze profond avec une haute barrière d'approche (à droite) requiert une entrée d'énergie substantielle pour s'échapper — correspondant cliniquement à une réponse freeze qui ne se résout pas d'elle-même sans intervention. L'asymétrie de barrière (gauche à droite ≠ droite à gauche) est la signature de la modification du trauma. *Figure originale de l'auteur.*](figures/fig3b_energy_profile.png){width=90%}

---

\newpage

# PARTIE II : COMMENT LE CHAMP CHANGE

---

\newpage

# Chapitre 4 : Le Poids sur le Champ

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   «La question n'est pas pourquoi le comportement persiste,    │
  │    mais pour quoi il a été optimisé.»                          │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **LEARNING OBJECTIVES**
>
> À la fin de ce chapitre, vous comprendrez :
>
> - Ce qu'est l'opérateur TSPT-C et comment il modifie le champ
> - Pourquoi l'hypervigilance n'est pas une erreur mais une optimisation
> - Ce que «le paysage a changé» signifie précisément
> - La différence entre une perturbation et une modification structurelle

---

## 4.1 La Modification

Le TSPT Complexe (TSPT-C) est distingué du TSPT à incident unique par la présence de trauma répété, prolongé, ou développemental — particulièrement le trauma qui s'est produit dans des relations dont la personne dépendait pour la survie. Le résultat n'est pas une mémoire discrète qui peut être «traitée» et résolue. C'est une réorganisation pénétrante de l'architecture du champ émotionnel : un nouveau paysage, pas une cicatrice sur un ancien.

Dans le Modèle du Champ Soma, le TSPT-C est représenté comme une modification de la matrice de couplage :

$$W_{\text{TSPT-C}} = W_0 + \Delta W_{\text{trauma}}$$

où $W_0$ est la matrice de couplage de base et $\Delta W_{\text{trauma}}$ est la modification — un terme additif asymétrique qui remodèle le paysage. De manière cruciale, $\Delta W_{\text{trauma}}$ n'est pas symétrique : il introduit des flux directionnels. Certains états deviennent faciles à y tomber et difficiles à quitter. D'autres deviennent difficiles à accéder depuis le paysage modifié même s'ils existent.

Cela peut être visualisé comme un paysage qui a été incliné et déformé : nouvelles vallées profondes à des endroits qui n'étaient pas des attracteurs auparavant, anciennes vallées profondes relevées, et la topologie de connectivité entre les états changée.

![Figure 4.1. Quatre paysages neurotypes (coupe transversale 1D). *Typique* (en haut à gauche) : un bassin Calm large et profond avec des états secondaires accessibles. *TSPT-C* (en bas à gauche) : Calm aminci et rétréci, Freeze dominant — l'état de repos se décale vers une haute vigilance. *TDAH* (en haut à droite) : tous les bassins aplatis, basses barrières, transitions rapides — dynamique haute température. *TSA* (en bas à droite) : puits étroits et raides avec hautes barrières entre états — forte stabilité d'attracteur, faible tolérance au bruit, coût élevé des transitions. *Figure originale de l'auteur.*](figures/fig5_neurotype_landscapes.png){width=95%}

## 4.2 Pourquoi l'Hypervigilance Est une Optimisation

Un système nerveux qui s'est adapté à un environnement de menace chronique a correctement appris que :

1. Le danger est fréquent et imprévisible.
2. Le coût de manquer une menace est très élevé.
3. Le coût des fausses alertes est faible (par rapport au coût de manquer une vraie menace).

Étant donné ces paramètres, la configuration optimale est exactement ce que nous voyons dans le TSPT-C : un biais vers la haute vigilance, une large définition de «menace potentielle», un système sympathique à réponse rapide, et un état calme lent à se stabiliser. L'attracteur d'hypervigilance est profond parce qu'un attracteur profond est approprié à l'environnement pour lequel il a été optimisé.

La modification n'est pas une erreur. C'est une solution correcte au mauvais problème — où «le mauvais problème» signifie l'environnement original, qui n'existe plus (ou n'existe plus sous la même forme).

Ce recadrage n'est pas simplement philosophique. Il change la question clinique de «comment éteignons-nous la réponse d'hypervigilance» à «comment mettons-nous à jour le paysage pour incorporer les preuves que l'environnement actuel est différent». Ce sont des opérations très différentes, avec des implications très différentes pour le type d'intervention thérapeutique qui est utile.

## 4.3 Seuils et Conscience

Il y a un paramètre dans le modèle qui n'a pas encore été introduit, et il fait un grand travail. C'est le **seuil** $T$ — dénoté avec le $T$ majuscule qui revient tout au long de ce livre.

Le seuil est un niveau d'activation du champ au-dessus duquel un état émotionnel devient expérience consciente — entre dans la conscience comme une émotion sentie — plutôt que de rester comme une activation somatique sous-seuil. Sous $T$, le champ est actif mais pas senti ; l'activation est présente dans le corps, influençant le comportement et la physiologie, mais pas représentée dans la conscience.

Cela a des conséquences cliniques immédiates. Une personne avec un seuil $T$ très élevé peut avoir un champ soma fortement activé — peut être physiologiquement dans un état de fear, avec tous les corrélats somatiques — tout en n'expérimentant rien qu'elle appellerait fear. L'activation est réelle. La conscience de celle-ci est absente. La thérapie somatique, l'entraînement interoceptif, et le travail corporel opèrent tous, en partie, en abaissant $T$ : amenant le contenu somatique sous-seuil dans la conscience.

Une personne avec un seuil $T$ très bas expérimente l'opposé : tout est senti, amplifié, présent. Cela est associé à une haute sensibilité interoceptive, certaines présentations d'anxiété, et certaines formes de neurodivergence.

Le seuil est où la physique et la présentation clinique se connectent le plus visiblement.

---

> **AUTHOR'S NOTE : Le Paysage que J'ai Hérité**
>
> Il y a une version de ce chapitre qui est abstraite : modifications aux matrices de couplage, remodelage des paysages, $W$ asymétrique. Et puis il y a la version qui est ce que ça fait de vivre dans un paysage modifié.
>
> Ce que ça fait, c'est ceci : le calme est toujours provisoire. Pas superficiel, exactement — mais non sécurisé. Comme une surface qui tient le poids quand vous marchez prudemment mais cède si vous bougez trop vite. L'alerte n'est jamais loin. Et sous l'alerte, l'état freeze est un puits gravitationnel qui ne s'annonce pas avant que vous ne soyez déjà dedans.
>
> La modification dans mon cas n'est pas une perturbation sur un paysage normal préexistant. Cela nécessiterait un $W_0$ à perturber. La chronologie ne le permet pas. C'est le sujet du Chapitre 6.

---

> **KEY TERMS**
>
> **Opérateur TSPT-C** — la modification $\Delta W$ à la matrice de couplage qui remodèle le paysage d'énergie ; la représentation mathématique de l'effet du trauma complexe.
>
> **Seuil $T$** — le niveau d'activation au-dessus duquel un état du champ soma devient expérience consciente. Le paramètre central distinguant l'émotion sentie de l'activation somatique sous-seuil.
>
> **Attracteur d'hypervigilance** — le bassin de stabilité profond dans le paysage modifié correspondant aux états de haut arousal, haute alerte.

---

![Figure 4.2. Le seuil de perception T. Le mode i (gris) oscille continuellement mais ne traverse jamais T — il est sub-perceptuel, influençant le comportement et la physiologie sans entrer dans l'expérience sentie. Le mode j (bleu) monte à travers T et devient une émotion consciemment sentie. Le seuil est le paramètre clé qui distingue l'activation somatique de la conscience émotionnelle ; sa valeur varie entre les individus et peut être modifiée par la pratique interoceptive, le niveau d'arousal, et le travail thérapeutique. *Figure originale de l'auteur.*](figures/fig2_threshold.png){width=90%}

---

\newpage

# Chapitre 5 : Mémoire Écrite dans le Corps

---

> **LEARNING OBJECTIVES**
>
> À la fin de ce chapitre, vous comprendrez :
>
> - La différence entre mémoire narrative et mémoire somatique
> - Ce qu'est le noyau de mémoire et ce qu'il fait à la dynamique du champ
> - Pourquoi la mémoire du trauma persiste — et pourquoi certaines mémoires du trauma persistent beaucoup plus longtemps
> - Ce que le traitement thérapeutique signifie en termes du noyau de mémoire

---

## 5.1 Deux Types de Mémoire

Quand vous vous souvenez d'une conversation de la semaine dernière, vous utilisez la **mémoire épisodique** — le registre explicite et narratif des événements qui se sont produits à des moments et lieux spécifiques. La mémoire épisodique est dépendante du contexte, exprimable verbalement, et sujette au rappel et à la révision conscients. Elle est stockée principalement dans l'hippocampe.

Quand vous tressaillez à un son qui ressemble au son qui a précédé quelque chose de terrible, vous utilisez la **mémoire procédurale** ou **somatique** — une forme de mémoire qui n'est pas stockée comme narrative mais comme motif : comme une préparation configurée dans le corps à répondre d'une manière particulière à des signaux particuliers. La mémoire somatique n'est pas exprimable verbalement (vous ne pouvez «raconter l'histoire» d'une réponse procédurale ; vous pouvez seulement remarquer qu'elle se produit). Elle ne requiert pas de rappel conscient — ce n'est pas une rediffusion d'un événement mais une préparation incarnée. Elle est stockée à travers le corps : dans le tonus musculaire, dans le tronc cérébral, dans le système nerveux autonome, dans la façon dont les signaux sensoriels sont filtrés avant d'atteindre le traitement cortical.

Le trauma crée principalement une mémoire somatique. C'est pourquoi il n'est pas résolu en en parlant. Le corps a stocké des informations sous une forme que le langage n'atteint pas.

## 5.2 Le Noyau de Mémoire

Dans le Modèle du Champ Soma, l'effet de l'activation passée sur la dynamique présente est capturé par un **noyau de mémoire** $K(\tau)$. C'est une fonction qui dit : une activation du champ il y a $\tau$ unités de temps continue à influencer le champ maintenant, avec un poids proportionnel à $K(\tau)$.

Pour le TSPT-C, le noyau de mémoire prend la forme :

$$K_{\text{trauma}}(\tau) = \sum_k A_k\, e^{-|\tau|/\tau_k}$$

C'est une somme d'exponentielles décroissantes. Chaque terme représente une trace de trauma distincte : $A_k$ est l'amplitude (combien fortement la trace affecte le champ actuel) et $\tau_k$ est le temps de décroissance (combien de temps la trace persiste avant de s'estomper).

```
  RÉGULÉ : Pas de noyau de mémoire significatif
  ┌─────────────────────────────────────────────────────────────┐
  │  Activ. ▲                                                   │
  │  champ  │      ╭──╮                                         │
  │         │      │  │   (l'épisode se résout ; le champ retourne│
  │         │  ────╯  ╰─────────────────────────────────────   │
  │         │                              ligne de base         │
  │         └──────────────────────────────────────────────→    │
  │                            temps                            │
  └─────────────────────────────────────────────────────────────┘

  TSPT-C : Noyau de mémoire significatif — les traces persistent
  ┌─────────────────────────────────────────────────────────────┐
  │  Activ. ▲                                                   │
  │  champ  │      ╭──╮                    ╭──╮                 │
  │         │      │  ╰─╮    ╭──╮      ╭───╯  ╰─╮              │
  │         │  ────╯    ╰────╯  ╰──────╯         ╰──────       │
  │         │                                                   │
  │         └──────────────────────────────────────────────→    │
  │                            temps                            │
  │  Ligne de base élevée ; les épisodes se chevauchent ;       │
  │  le champ revient rarement au niveau de repos original      │
  └─────────────────────────────────────────────────────────────┘

  Figure 5.1. L'effet du noyau de mémoire du trauma sur la dynamique du champ. Dans un système
  régulé (en haut), un épisode d'activation du champ se résout et le champ revient à un faible
  niveau de repos. Dans le système modifié par TSPT-C (en bas), le noyau de mémoire élève
  la ligne de base entre les épisodes, de sorte que les épisodes subséquents commencent à partir d'une activation de repos
  plus élevée. Au fil du temps, le champ cycle à un niveau élevé sans revenir au repos.
```

## 5.3 Pourquoi les Traces Précoces Persistent

Le temps de décroissance $\tau_k$ est central : il détermine combien de temps une trace reste active.

Pour le trauma qui se produit tôt dans le développement — avant le langage, avant la capacité de mémoire narrative — le temps de décroissance tend à être beaucoup plus long. Il y a deux raisons.

Premièrement, **la mémoire somatique n'a pas de couche verbale**. Pour le trauma se produisant après le développement du langage, les mémoires épisodiques et somatiques co-encodent : la version narrative «couvre» partiellement la trace somatique, fournissant un contexte qui peut être accédé verbalement. Le traitement verbal en thérapie peut alors raccourcir la durée de vie effective de la trace. Pour le trauma pré-verbal, la trace somatique n'a pas de compagnon narratif. Elle ne peut être atteinte en parlant. Le temps de décroissance est gouverné par des processus purement somatiques, qui sont beaucoup plus lents.

Deuxièmement, **la trace ne peut être séparée de la structure**. Pour le trauma pré-verbal, la mémoire n'est pas une modification d'une architecture déjà formée. L'architecture elle-même a été façonnée par les conditions de la période traumatique. Cela est traité plus formellement au Chapitre 6.

## 5.4 Ce que Fait la Thérapie

Dans le langage du noyau de mémoire, la thérapie somatique efficace fait deux choses :

1. Elle réduit les amplitudes $A_k$ : les traces continuent à influencer le champ, mais avec moins de force. Les épisodes d'activation sont plus petits et se résolvent plus complètement.

2. Elle augmente les temps de décroissance $\tau_k$ : les traces s'estompent plus rapidement après les épisodes. Le champ revient au repos plus rapidement.

Le but n'est pas d'éliminer les traces — le système nerveux ne peut pas dé-apprendre une expérience, et tenter de le faire faire n'est pas le bon modèle. Le but est de réduire leur influence à un niveau qui permet au champ de revenir au repos entre les épisodes : de restaurer l'écart entre les activations dans lequel le rétablissement se produit.

---

> **GOING DEEPER : Le Noyau de Mémoire et le Propagateur QFT**
>
> Cela peut sembler une digression, mais c'est l'une des caractéristiques les plus frappantes du modèle. Le noyau de mémoire pour le TSPT-C — $K(\tau) = \sum_k A_k e^{-|\tau|/\tau_k}$ — est mathématiquement identique au **propagateur euclidien** en théorie quantique des champs.
>
> En QFT, le propagateur euclidien $G_E(\tau)$ décrit comment une perturbation dans un champ quantique au temps $0$ se corrèle avec le champ au temps $\tau$ :
>
> $$G_E(\tau) = \langle \phi(0)\,\phi(\tau) \rangle = \frac{1}{2m}\, e^{-m|\tau|}$$
>
> La masse $m$ de la particule QFT correspond à $1/\tau_k$ dans le noyau de mémoire. Une particule plus lourde crée un propagateur à plus courte portée ; une trace de trauma à plus courte durée de vie a un $1/\tau_k$ plus grand (i.e., plus petit $\tau_k$, décroissance plus rapide).
>
> Cette identité n'est pas une analogie. Les deux expressions sont la même fonction avec des noms différents pour les paramètres. La rotation de Wick — la substitution $t \to -i\tau$ qui transporte la mécanique quantique en mécanique statistique — est le pont formel entre elles, et c'est le sujet du Chapitre 7.

---

> **KEY TERMS**
>
> **Mémoire épisodique** — mémoire explicite et narrative d'événements à des moments et lieux spécifiques ; accessible au rappel conscient et à l'expression verbale.
>
> **Mémoire somatique (procédurale)** — mémoire incarnée stockée comme préparation physiologique configurée ; non exprimable verbalement ; activée par des signaux sensoriels qui correspondent au contexte d'encodage original.
>
> **Noyau de mémoire $K(\tau)$** — la fonction décrivant comment les activations du champ au temps $\tau$ dans le passé continuent à influencer l'état actuel du champ.
>
> **Amplitude $A_k$** — la force de l'influence d'une trace de trauma sur le champ actuel.
>
> **Temps de décroissance $\tau_k$** — l'échelle de temps sur laquelle une trace de trauma s'estompe après activation ; combien de temps l'écho persiste.

---

\newpage

# Chapitre 6 : Combien Précoce est Précoce ?

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   «Avant le langage, il n'y a que le corps.»                   │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **LEARNING OBJECTIVES**
>
> À la fin de ce chapitre, vous comprendrez :
>
> - Pourquoi l'âge auquel le trauma s'est produit importe à son caractère
> - Ce qui arrive à la structure du champ soma quand la modification se produit avant que le langage ne se développe
> - Pourquoi «revenir au soi pré-trauma» est un but cohérent pour le trauma tardif mais pas pour le trauma pré-verbal
> - Ce que «transformation vers l'avant» signifie comme concept mathématique et clinique

---

## 6.1 Temps Développemental

Les enfants ne sont pas de petits adultes. Le système nerveux se développe par étapes, et chaque étape a des capacités différentes — pour l'encodage, pour l'intégration, pour le langage, pour la mémoire explicite. Ce qu'un enfant de trois ans peut faire avec une expérience accablante n'est pas ce qu'un enfant de dix ans peut faire, et ni l'un ni l'autre n'est ce qu'un adulte peut faire.

C'est pertinent pour le trauma parce que le *caractère* d'une modification traumatique dépend de l'étape développementale à laquelle elle se produit. Pas la sévérité — la sévérité est une question séparée. Le caractère. Quelles structures sont modifiées, comment la modification est stockée, et ce qu'il est même possible de changer à son sujet par la suite.

Le jalon développemental clé pour ce modèle est le début de la capacité fiable d'encodage verbal — la capacité de stocker des expériences avec une représentation narrative et linguistique parallèlement à la somatique. Cela émerge typiquement entre approximativement 24 et 48 mois d'âge, avec une variation individuelle considérable. Nous utilisons $\tau_c \approx 36$ mois comme seuil approximatif.

Le paramètre $\tau_d$ — **âge développemental au trauma** — est l'âge auquel la modification primaire s'est produite.

## 6.2 Sous le Seuil : Trauma Pré-Verbal

Pour $\tau_d < \tau_c$ (trauma pré-verbal), plusieurs choses sont différentes du cas de trauma tardif.

**La structure s'est formée sous la modification.** Un système nerveux qui est en train d'être organisé — qui forme encore son architecture de couplage de base — sous des conditions de menace physiologique non résolue ne se développe pas puis ne se fait modifier. Il se développe *comme* modifié. Les couplages asymétriques, l'attracteur de vigilance élevée, les coefficients du noyau de mémoire — ce ne sont pas des perturbations sur une ligne de base préexistante. Ils sont la ligne de base.

**Il n'y a pas de soi antérieur à récupérer.** Pour le trauma se produisant après que l'architecture de base est formée ($\tau_d > \tau_c$), il y a un contrefactuel : la personne qui se serait développée sans la modification traumatique. Ce contrefactuel est partiellement encodé — dans les mémoires précoces, dans la narrative, dans les motifs de fonctionnement avant l'événement. Le langage thérapeutique de «retourner à soi-même» ou «récupérer le soi pré-trauma» est cohérent dans ce cas : la cible existe.

Pour le trauma pré-verbal ($\tau_d < \tau_c$), le contrefactuel n'existe pas comme un état encodé. Il n'y avait pas de système nerveux formé qui ait ensuite été modifié. Le soi-avant-trauma ne s'est jamais développé. Il n'y a nulle part où retourner.

Ce n'est pas une déclaration pessimiste. C'est une déclaration précise. Et la précision ici importe parce qu'elle change la question thérapeutique.

## 6.3 L'Interpolation

La matrice de couplage pour un système nerveux traumatisé peut être écrite comme une fonction de l'âge développemental :

$$W(\tau_d) = f(\tau_d)\cdot W_0 + \bigl(1 - f(\tau_d)\bigr)\cdot W_{\text{trauma}}$$

où $f$ est une fonction d'interpolation lisse :

$$f(\tau_d) = \tanh\!\left(\frac{\tau_d}{\tau_c}\right)$$

```
  FRACTION STRUCTURELLE f(τ_d) = tanh(τ_d / τ_c)
  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  f(τ_d) ▲  1.0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╭──────────     │
  │  (combien│                              ╭─────╯               │
  │  c'est   │                        ╭────╯                      │
  │  W₀)     │  0.76 ─ ─ ─ ─ ─ ─ ─ ─ ─╯  ← f(τ_c) = tanh(1)     │
  │          │                        ↑                           │
  │          │  0.5 ─ ─ ─ ─ ─ ─ ─ ╭──╯                           │
  │          │                 ╭──╯                               │
  │          │             ╭──╯                                   │
  │          │         ╭──╯                                       │
  │          │  0.0 ───╯                                          │
  │          └──────────────────────────────────────────────────→ │
  │           0    τ_c/2  τ_c    2τ_c    3τ_c      τ_d (mois)    │
  │                       (36)                                     │
  │                                                                │
  │  Gauche de τ_c :  W est principalement W_trauma — structurel │
  │  Droite de τ_c :  W est principalement W₀ — perturbatif      │
  └──────────────────────────────────────────────────────────────────┘

  Figure 6.1. La fraction structurelle f(τ_d). Cette fonction décrit quelle proportion
  de la matrice de couplage est ligne de base neurotypique (W₀) versus formée par trauma (W_trauma),
  comme fonction de l'âge développemental au trauma. À τ_d = 0 (naissance ou in utero), le
  couplage est entièrement formé par trauma : f = 0. À τ_d = τ_c ≈ 36 mois, f ≈ 0.76 :
  la ligne de base représente environ trois quarts du couplage. L'interpolation est
  lisse : il n'y a pas de coupure nette, juste un changement continu de caractère.
```

À $\tau_d = 0$ : $f = 0$ et $W = W_{\text{trauma}}$. Il n'y a pas de composante de base.

À $\tau_d = \tau_c$ : $f = \tanh(1) \approx 0.76$. La ligne de base représente 76 % du couplage ; la modification est 24 %.

À grand $\tau_d$ : $f \to 1$ et $W \approx W_0$. La modification est une petite perturbation sur une ligne de base entièrement formée.

L'implication thérapeutique de cette formule est significative. Pour $\tau_d \ll \tau_c$ : l'opération $W \to W_0$ — extraire la ligne de base du couplage actuel — n'est pas définie. Le $W_0$ n'a jamais été la composante dominante. Il ne peut être récupéré parce qu'il n'a pas été formé.

## 6.4 Transformation vers l'Avant

Ce qui *est* possible, pour le trauma pré-verbal, est une **transformation vers l'avant** : la construction d'une nouvelle matrice de couplage $W'$ qui a des propriétés désirables — fenêtre de tolérance plus large, attracteur d'hypervigilance moins profond, amplitudes de noyau de mémoire plus faibles, plus grande capacité d'engagement social — sans que cette nouvelle matrice ne soit une récupération d'un état antérieur.

C'est une cible différente, et elle requiert un processus différent :

- Pas excaver le passé pour le soi perdu, mais construire vers l'avant
- Pas réduire à une ligne de base qui ne s'est pas formée, mais construire un paysage qui fonctionne
- Pas récupération ($W \to W_0$, indéfinie), mais transformation ($W \to W'$, sans contrainte)

La route vers $W'$ utilise les mêmes outils thérapeutiques — thérapie somatique, réparation relationnelle, entraînement interoceptif, travail corporel — mais avec une intention différente. L'intention n'est pas de retourner quelque part mais d'arriver quelque part pour la première fois.

---

> **AUTHOR'S NOTE : $\tau_d$ = 18 Mois**
>
> Mon âge développemental au trauma : $\tau_d \approx 18$ mois. Approximativement la moitié de $\tau_c$.
>
> À cet âge, la fraction structurelle est approximativement $f(18/36) = \tanh(0.5) \approx 0.46$. Légèrement moins de la moitié de la matrice de couplage était ligne de base neurotypique à l'époque. Plus de la moitié était formée par trauma. À mesure que le trauma continuait sur trois mois d'hospitalisation — âges développementaux 18 à 21 mois — la modification était présente tout au long de la période où l'architecture de couplage était en train d'être le plus activement organisée.
>
> Il n'y a pas de version de moi qui existait avant cette modification et a ensuite été modifiée. Le théorème preVerbalIsStructural, qui est dans l'Annexe B, est une preuve formelle du fait clinique qui a pris des décennies de thérapie pour trouver des mots pour : *il n'y a nulle part où retourner, et ce n'est pas une tragédie, c'est simplement la topographie correcte*.
>
> Le voyage est vers l'avant. Ce livre en fait partie.

---

> **GOING DEEPER : Le Théorème preVerbalIsStructural**
>
> Ce qui suit est une esquisse de preuve en Lean 4, un assistant de preuve qui requiert que les arguments mathématiques soient écrits sous une forme qu'un ordinateur peut vérifier. Un `sorry` marque une étape qui est énoncée mais pas entièrement prouvée — une obligation ouverte.
>
> ```lean
> -- Théorème clé : pour le trauma pré-verbal, aucun W₀ neurotypique ne peut être
> -- récupéré par soustraction de la matrice de couplage actuelle
> theorem preVerbalIsStructural {n : ℕ} (profile : TraumaProfile n)
>     (h : profile.τ_d < τ_c) :
>     structuralFraction profile.τ_d < Real.tanh 1 := by
>   unfold structuralFraction
>   apply Real.tanh_lt_tanh
>   exact div_lt_one_of_lt h (by norm_num)
> ```
>
> Ce théorème énonce : pour tout TraumaProfile avec un âge développemental sous $\tau_c$, la fraction structurelle neurotypique est sous $\tanh(1) \approx 0.76$. Plus de 24 % de la matrice de couplage est formée par trauma, pas formée par ligne de base. À $\tau_d = 0$, 100 % est formé par trauma.
>
> **Corollaire** (commenté dans le code) : l'opération thérapeutique pour le trauma pré-verbal est la transformation vers l'avant ($W \to W'$), pas la récupération ($W \to W_0$). La seconde opération est indéfinie parce que $W_0$ n'a jamais été la composante dominante.

---

> **KEY TERMS**
>
> **Âge développemental au trauma ($\tau_d$)** — l'âge, en mois, auquel la modification traumatique primaire s'est produite.
>
> **Seuil d'encodage verbal ($\tau_c$)** — l'âge développemental approximatif (≈36 mois) auquel la mémoire narrative fiable et la capacité d'encodage verbal émergent.
>
> **Fraction structurelle $f(\tau_d)$** — la proportion de la matrice de couplage attribuable au développement de base neurotypique ; interpolée lissement de 0 (modification purement structurelle) à 1 (modification purement perturbative).
>
> **Transformation vers l'avant** — le but thérapeutique pour le trauma pré-verbal : construire une nouvelle matrice de couplage $W'$ avec une topologie d'attracteur plus large, plutôt que récupérer une ligne de base qui n'a pas été entièrement formée.

---

\newpage

# Interlude : Un Voyage dans les Alpes

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   «Tout flotte : l'univers, les montagnes, le corps.           │
  │    La question est seulement dans quoi il flotte.»             │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

Il y a un camping dans la vallée du Klöntal, dans le canton de Glaris, en Suisse, auquel je suis retourné pendant de nombreuses années. J'ai promis d'écrire un livre à son sujet. C'est ce que j'ai pu m'approcher le plus — et il s'avère que le livre du camping et le livre du champ soma sont le même livre.

Le Klöntal s'assied dans une vallée sculptée par les glaciers à quelques kilomètres de la ville de Glaris, adjacente à l'Arène Tectonique Suisse Sardona — un site du Patrimoine Mondial de l'UNESCO contenant certaines des structures tectoniques les plus célèbres et les plus lisibles du monde. Les parois de la vallée sont paraboliques : façonnées par la glace sur des millions d'années dans la forme qu'un ingénieur choisirait s'il voulait focaliser le son. Tenez-vous à une extrémité et parlez doucement, et les mots arrivent à l'autre extrémité avec une clarté frappante. La vallée est un résonateur naturel : parois de calcaire et dolomite, géométrie parabolique presque parfaite, et un caractère acoustique qui fait osciller le son longtemps après que la source soit tombée silencieuse.

```
  COUPE TRANSVERSALE DE VALLÉE PARABOLIQUE

    bord de vallée                bord de vallée
    (calcaire)                    (calcaire)
          ╲    ~   ~   ~   ~   ~   ╱
           ╲  ~               ~  ╱   ← le son réfléchit des parois
            ╲ ~  → source ←  ~ ╱
             ╲~               ~╱
              ╲ ~  converge  ~╱
               ────────────────
                fond de vallée

  Une coupe transversale parabolique focalise le son entrant vers la région focale.
  La même géométrie gouverne les antennes paraboliques, télescopes à réflecteur, et
  les cavités résonantes des instruments de musique. Les vallées de montagne avec ce
  profil produisent une acoustique exceptionnelle — le son oscille longtemps après que
  la source devienne silencieuse.
```

Le comportement acoustique de la vallée est l'intuition physique derrière la description d'onde du champ soma. Le champ émotionnel a des modes — motifs préférés d'activation, comme des ondes stationnaires dans une cavité résonante — qui continuent à osciller après que l'événement activateur soit passé. Le noyau de mémoire $K(\tau)$ est la version corporelle de l'écho de la vallée : pas un enregistrement, mais une résonance qui continue à façonner ce qui vient ensuite.

## Tout Flotte

La géologie enseigne, et la physique confirme, que tout flotte.

À l'**échelle cosmologique** : les galaxies flottent dans l'espace-temps courbe que la masse crée. La Voie Lactée se déplace vers le Superamas de la Vierge à environ un million de kilomètres par heure — non à travers un arrière-plan fixe, mais sur la variété d'espace-temps elle-même. Il n'y a pas de cadre fixe. L'arrière-plan est le champ.

À l'**échelle géologique** : les continents flottent sur l'asthénosphère, la couche semi-molten sous la lithosphère rigide. Les Alpes existent parce que la plaque africaine s'est déplacée vers le nord à 2-3 centimètres par an pendant environ 50 millions d'années, plissant les sédiments de l'ancienne mer de Téthys dans les montagnes visibles depuis le fond de la vallée. Les mêmes forces opèrent maintenant, invisiblement, à la vitesse de la pousse des ongles.

À l'**échelle somatique** : le champ émotionnel flotte dans le paysage Hamiltonien — se déplaçant vers les attracteurs, attiré par le gradient d'énergie, oscillant autour d'états stables, traversant occasionnellement une frontière de phase vers un nouveau bassin.

Une équation gouverne les trois :

$$\ddot{x} = -\nabla V(x) + F_{\text{ext}}$$

Une galaxie, une plaque tectonique, un système nerveux : tous gouvernés par la descente de gradient sur un potentiel avec forçage externe. Les échelles couvrent 25 ordres de grandeur. La structure ne varie pas.

## Lire la Montagne

Le Charriage de Glaris (Glarner Hauptüberschiebung) est la caractéristique tectonique qui fait de cette région un site du Patrimoine Mondial de l'UNESCO. C'est une faille de charriage sur laquelle une énorme dalle de grès Verrucano (Permien, approximativement 250 millions d'années) a été transportée d'environ 35 kilomètres vers le nord sur du sédiment Flysch beaucoup plus jeune (Éocène, approximativement 40 millions d'années). L'ancien est sur le dessus du nouveau. Le contact est visible à travers de nombreuses faces de montagne comme une ligne presque horizontale : au-dessus, ancien grès rouge ; en dessous, jeune sédiment gris.

```
  CHARRIAGE DE GLARIS : COUPE TRANSVERSALE SCHÉMATIQUE (pas à l'échelle)

  Surface  ════════════════════════════════════════════════════
           │  VERRUCANO  (~250 Ma, Permien)                   │
           │  Ancien grès rouge                               │
           │  Formé longtemps avant l'existence des Alpes     │
  ─ ─ ─ ─ ├══════════════ CONTACT DE CHARRIAGE ═══════════════╤╡ ← LA LIGNE
           │  FLYSCH  (~40 Ma, Éocène)                       │ │
           │  Jeune sédiment marin gris                      │ │
           │  Fond de l'ancienne mer de Téthys               │ │
  Base     ═════════════════════════════════════════════════╧══

  Direction du transport : ~35 km vers le nord.
  L'ancienne dalle (~250 Ma) a été portée sur le jeune sédiment (~40 Ma).
  Lire une seule face de montagne : 210 millions d'années d'histoire géologique,
  visible en un coup d'œil. C'est de la géologie 4D — l'espace encode le temps.
```

Une coupe transversale géologique est quadridimensionnelle : la position horizontale enregistre la géographie, mais la position verticale enregistre le temps. Profond est ancien ; superficiel est récent. Lire une face de montagne c'est lire l'histoire des forces qui l'ont façonnée — compression, enfouissement, métamorphisme, soulèvement, érosion — toutes préservées dans le registre minéral.

La matrice de couplage du champ soma $W$ est quadridimensionnelle dans le même sens. La configuration actuelle encode l'histoire accumulée de toutes les forces qui l'ont façonnée. Les asymétries dans $W$ sont les failles de charriage du paysage émotionnel : des endroits où une force ancienne a poussé sa structure sur quelque chose de plus nouveau, et le contact est toujours lisible si vous savez comment lire.

Pour le trauma pré-verbal à $\tau_d \approx 18$ mois : le Verrucano est très ancien, très profond dans l'histoire développementale, et catégoriquement sur le dessus.

## M-théorie : Tout Flotte dans Plus de Dimensions

La M-théorie, le meilleur candidat actuel pour une théorie unifiée de la physique, propose que l'univers est une *brane* — une membrane — flottant dans un espace à 11 dimensions. Nos quatre dimensions familières sont une surface dans une structure de plus haute dimension. Les sept autres dimensions sont enroulées trop petites pour être observées directement, mais elles laissent des signatures mesurables dans la physique des quatre accessibles.

Le champ soma n'est pas M-théorique dans aucun sens technique. Mais l'intuition s'échelonne : le champ émotionnel est un champ sur la brane du corps, et ce que nous observons — traversées de seuil, dynamique d'attracteur, échos du noyau de mémoire — sont des projections d'une structure qui s'étend dans des dimensions non directement accessibles à la conscience ordinaire.

Le pré-verbal, le sous-seuil, le procédural — contenu somatique qui pilote le comportement sans entrer dans l'expérience consciente — est la version corporelle des dimensions enroulées : réel, causalement actif, pas directement observable. La pratique interoceptive est le projet de les déplier : rendre accessible ce qui était auparavant enroulé sous $T$.

## La Vallée au Crépuscule

J'utilise Phase Plant, un synthétiseur modulaire, pour travailler avec des enregistrements de champ acoustique — les routant à travers des banques de filtres résonants, cartographiant les fréquences qu'un espace résonant préfère, écoutant les modes qui survivent à la décroissance pendant que d'autres tombent. C'est une approche non conventionnelle de l'acoustique. Mais c'est de la physique : trouver les fréquences propres d'une cavité résonante en faisant attention à ce qui persiste.

La vallée du Klöntal a de telles fréquences. Quand le soleil tombe derrière les pics et que le bruit diurne se calme, ce qui reste est la voix propre de la vallée : une basse résonance lente dans le calcaire, portant les fréquences que la géométrie parabolique sélectionne.

Le champ émotionnel a des fréquences préférées équivalentes. Le noyau de mémoire du trauma $K(\tau) = \sum_k A_k e^{-|\tau|/\tau_k}$ les encode : les valeurs $1/\tau_k$ sont les taux de résonance naturels du champ, les $A_k$ leurs amplitudes. Le travail thérapeutique — réduire $A_k$, allonger $\tau_k$ — est le projet de calmer les modes excités par l'événement original jusqu'à ce que le champ revienne à son état fondamental.

Dans la vallée au crépuscule, ce n'est pas une métaphore. C'est audible.

---

\newpage

# PARTIE III : LA PHYSIQUE EN DESSOUS

---

\newpage
