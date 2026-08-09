
# Parte IV: Estensioni e Applicazioni

## La Trilogia dei Contenitori

La partitura del Film del Fiume può essere realizzata in almeno tre contenitori
senza cambiare un singolo valore nella definizione della partitura:

| Contenitore | Ambientazione | Kurtz / attrattore profondo |
|---|---|---|
| **Fiume** | Congo / Mekong / Amazzonia | La figura a monte; il luogo senza linguaggio |
| **Corpo** | Sottomarino miniaturizzato nel flusso sanguigno | Camera cardiaca; la più antica memoria immunitaria |
| **Sessione** | Stanza di psicoterapia | Il momento in cui il freeze si solleva |

Tutti e tre sono lo stesso film. Tutti e tre attraversano le stesse due soglie agli
stessi tempi della storia. Tutti e tre ritornano lungo il percorso asimmetrico. Il
rendering renderizza tutti e tre identicamente — perché la partitura è ciò che
viene renderizzato, non il contenitore.

## Comporre con la Partitura

Un compositore che lavora con questo sistema non scrive note. Scrive traiettorie. Le
decisioni compositive sono:

1. **Quali modi** sono gli assi primari di questo pezzo?
2. **Qual è l'arco** — la forma di ogni traiettoria sul tempo della storia?
3. **Dove sono le soglie** — gli eventi istantonici?
4. **Quanto è profondo** l'attrattore più profondo? (Come suona qui $\kappa_d = 1.0$?)
5. **Qual è la topologia del ritorno** — il campo ritorna a dove è partito,
   o il bacino di ritorno è diverso dal bacino di partenza?

Un film con gli stessi bacini di partenza e ritorno (safety a $t=0$ ≈ safety a $t=1$)
è un viaggio di andata e ritorno. La maggior parte delle sessioni di terapia non sono
viaggi di andata e ritorno. Il bacino di ritorno è riorganizzato: maggiore coerenza
HRV, accoppiamento di default più basso tra fear e shame, maggiore distanza di
soglia dall'attrattore di freeze. La partitura dovrebbe riflettere questo — il
ritorno non è un'inversione della partenza, ma un percorso diverso verso una
versione diversa di casa.

## Diagrammi a Corde come Notazione di Partitura

Per partiture multi-personaggio — dove l'accoppiamento tra molteplici campi di
spettatori è parte della composizione — i diagrammi a corde forniscono la notazione.
Ogni filo è un campo soma. Ogni scatola è un'interazione. La composizione (due
scatole in sequenza) è una sequenza temporale di interazioni. Il prodotto tensoriale
(due fili in parallelo) è un'attivazione simultanea indipendente.

Una diade terapeutica è due fili attraverso il tempo, con scatole di accoppiamento
nei punti di co-regolazione. Un pubblico cinematografico è $N$ fili paralleli,
ciascuno con il proprio $H_V$, tutti accoppiati allo stesso segnale dello schermo
$S(t)$. La partitura emotiva è la specifica astratta di cosa fa $S(t)$. La risposta
collettiva del pubblico è il prodotto tensoriale di $N$ traiettorie individuali,
tutte modellate dalla stessa sorgente.

## La Trilogia del Tensore

Questo documento fa parte di un progetto in tre parti:

| Documento | Registro | Titolo completo |
|---|---|---|
| **soma-field-paper.md** | Accademico | *The Soma-Field Model* (The Tensor II) |
| **soma-field-book.md** | Accessibile | *A Voyage into Trauma* (The Tensor III) |
| **the-tensor.md** | Operativo | *The Tensor* — definizione astratta di film |

L'articolo definisce il modello. Il libro spiega il modello. Questo documento **esegue**
il modello — o più precisamente, definisce l'interfaccia tramite cui un sistema di
rendering audio-visivo può istanziare il modello come esperienza in tempo reale.

## Il Problema del Pensieve

In *Harry Potter*, Silente usa la sua bacchetta per estrarre un pensiero dalla sua
mente — emerge come un filo argenteo — e lo deposita in una ciotola di pietra
chiamata Pensieve. Altri possono poi abbassare il volto alla superficie ed entrare
nella memoria, esperendola dall'interno.

Questa è la serializzazione dello stato mentale: un processo in esecuzione (una
memoria, attualmente in esecuzione in una mente vivente) estratto e scritto in
archiviazione persistente, poi deserializzato in un secondo momento da un lettore
diverso.

La partitura del campo soma è un Pensieve per la dinamica emotiva. La bacchetta è
il sistema di misurazione (HRV, osservazione del terapeuta, biofeedback). Il filo
argenteo è il file di partitura $\mathbf{e}^*(t)$, la matrice di accoppiamento
$W^*$, il kernel di memoria $K^*$. La ciotola del Pensieve è il sistema di
rendering.

Ma la partitura del campo soma è strettamente più potente della ciotola di Silente:

| | Pensieve | Partitura del campo soma |
|---|---|---|
| Cosa viene serializzato | Contenuto della memoria — eventi e immagini specifici | Dinamica emotiva — forma del campo, topologia degli attrattori, forze di accoppiamento |
| Replay | Fissa; stessa esperienza per ogni spettatore | Renderizzata attraverso l'$H_V$ dello spettatore stesso; personalizzata senza perdere l'identità della partitura |
| Ruolo dello spettatore | Osservatore passivo all'interno di una registrazione fissa | Partecipante attivo del campo; a $\kappa_r = 1$, co-autore del rendering |
| Unità di archiviazione | Un pensiero specifico | La *forma* emotiva — valida per qualsiasi contenitore narrativo con la stessa dinamica |

Silente memorizza ciò che è accaduto. Il campo soma memorizza com'era sentirsi in
quel bacino — disaccoppiato dal contenuto narrativo specifico, portatile attraverso
contenitori, renderizzabile da un sistema nervoso diverso in un secolo diverso.

La parola tecnica per ciò che entrambi i sistemi fanno è **serializzare**: prendere
un processo in esecuzione che esiste solo in tempo reale e scriverlo in un formato
durevole e trasmissibile. La parola poetica è **cristallizzare** — fissare qualcosa
di fluido in una forma riproducibile senza distruggerne la struttura essenziale.

Stiamo cristallizzando l'esperienza emotiva. Non la storia. Non le immagini. La
matematica sotto tutte le storie e tutte le immagini che hanno la stessa forma
emotiva. Questo è ciò che il file di partitura contiene. Questo è ciò che il sistema
di rendering legge indietro.

---

\newpage

# Appendice: Formato del File di Partitura

Una partitura leggibile dalla macchina sarebbe espressa come segue. Questo è uno
schizzo del formato; una specifica completa è un documento di ingegneria separato.

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

*The Tensor. 17 maggio 2026.*



\newpage

\part{Parte II: L'Apparato Formale}



---

> *L'IA ha avuto un cervello dal 1943. Ora ha un corpo.*

---

# Introduzione

Un paziente siede con il suo terapeuta e gli viene chiesto: *«Cosa stai sentendo
adesso?»* La domanda è ingannevolmente semplice. Possono dire *ansioso*, eppure
quella parola copre un territorio vasto ed eterogeneo — una stretta nel petto, un
commento continuo di preoccupazione, una vaga prontezza a fuggire, una memoria che
emerge dall'infanzia. Un altro paziente, a cui viene posta la stessa domanda,
riferisce di non sentire nulla; eppure la sua postura, respirazione, e la qualità
del suo silenzio suggeriscono altrimenti. L'emozione è lì. Semplicemente non è
ancora cosciente.

Questo divario tra presenza emotiva e consapevolezza emotiva è uno dei fenomeni
clinicamente più significativi in psicoterapia. Le teorie della regolazione
dell'affetto (Schore, 2001), dell'esperienza somatica (Levine, 2010), della
psicoterapia sensomotoria (Ogden, Minton e Pain, 2006), e la teoria polivagale
(Porges, 2011) si confrontano tutte, in modi diversi, con la stessa osservazione:
le emozioni esistono nel corpo prima — e spesso senza — essere nominate nella
mente. Eugene Gendlin chiamò il senso corporeo sub-verbale di una situazione
emotiva il *felt sense* (Gendlin, 1978): qualcosa che è lì, intero e presente, ma
non ancora articolato.

Il Modello del Campo Soma proposto qui tenta di dare a questa osservazione clinica
una struttura formale. Lo fa prendendo in prestito uno strumento concettuale dalla
fisica: il campo. In fisica, un campo non è una cosa che esiste in un punto. È una
quantità che esiste ovunque in uno spazio, continuamente, sia che venga osservata
o no. Le particelle — le cose che possiamo misurare — non sono separate dal campo;
sono *eccitazioni* di esso, concentrazioni locali di energia che sorgono quando il
campo è perturbato sopra una certa soglia.

L'affermazione centrale di questo articolo è che questa struttura descrive
accuratamente la fenomenologia dell'emozione. Il campo emotivo è sempre lì,
distribuito attraverso corpo e sistema nervoso. Ciò che chiamiamo esperienza
emotiva cosciente è un'eccitazione di quel campo — una concentrazione locale che ha
attraversato una soglia percettiva ed è entrata nella consapevolezza. Il campo
continua sotto la soglia sia che vi prestiamo attenzione o no, e la sua attività
sub-percettiva modella il nostro comportamento, fisiologia e cognizione in modo
continuo.

Il Modello del Campo Soma contribuisce alla prima architettura formale di teoria
di campo per il sistema limbico. Ogni rete neurale artificiale dal 1943
[@mcculloch1943] (McCulloch e Pitts) è un modello formale della neocorteccia —
lo strato del riconoscimento di pattern e della previsione. Il sistema limbico —
responsabile della valutazione emotiva, della rilevazione delle minacce, e del
ripristino dello stato somatico che è alla base del trauma — non ha mai ricevuto
un trattamento formale comparabile. Il Modello del Campo Soma è quel trattamento.
Insieme al framework Hopfield, costituisce la prima descrizione formale completa
dei due principali substrati computazionali del cervello dei vertebrati.

L'articolo procede come segue. La Sezione 2 rivede il background rilevante nei
modelli clinici somatici, e introduce i due strumenti teorici presi in prestito da
fisica e informatica: teoria quantistica dei campi e funzioni di energia delle
reti di Hopfield. La Sezione 3 sviluppa il Modello del Campo Soma in dettaglio. La
Sezione 4 descrive la landscape di energia, inclusi gli stati attrattori
corrispondenti a fight, flight, freeze, e calm regolata. La Sezione 5 discute la
dissonanza e la risoluzione come meccanismi dell'interazione emotiva. La Sezione 6
descrive lo Strumento del Campo Soma, uno strumento pratico per uso terapeutico.
La Sezione 7 affronta le implicazioni cliniche.

---

# Background

## Il Problema Corpo-Mente nella Pratica Clinica

La neuroscienza contemporanea ha in gran parte dissolto il confine cartesiano tra
corpo e mente. Damasio (1994) dimostrò che l'emozione è inseparabile dalla
cognizione razionale: i pazienti con danni alla corteccia prefrontale ventromediale
— che impediscono la normale generazione di segnali somatici — perdono non solo
la loro gamma emotiva ma anche la capacità di decisione efficace. Van der Kolk
(2014) documentò estensivamente come gli stati emotivi traumatici sono codificati
non solo nella memoria esplicita ma in postura, gesto, sensazione viscerale e
regolazione autonomica. La teoria polivagale di Porges (2011) fornì un resoconto
neurobiologico di come il sistema nervoso autonomo generi tre stati gerarchicamente
organizzati — vagale ventrale (engagement sociale), simpatico (mobilizzazione:
fight/flight), e vagale dorsale (immobilizzazione: freeze) — ciascuno con
caratteristiche fenomenologiche e comportamentali distintive.

Ciò che questi framework condividono è la convinzione che gli stati emotivi non
sono situati nel cervello solo, né nel corpo solo, ma in un sistema accoppiato
che è meglio inteso come una singola unità funzionale. Il termine *soma* — dal
greco per corpo — è usato qui per denotare questo sistema unificato corpo-mente,
seguendo la tradizione della psicoterapia somatica.

## Il Felt Sense e l'Emozione Sub-Percettiva

Il concetto di *felt sense* di Gendlin (1978) è di particolare rilevanza. Lo
descrisse come «un tipo speciale di consapevolezza corporea interna... un senso
corporeo del significato». Non è un'emozione nel senso ordinario — non un
sentimento nominato — ma qualcosa di più diffuso: un senso pre-articolato che
*qualcosa è lì*, presente nel corpo, prima di essere stato identificato o nominato.
Il Focusing, il metodo terapeutico sviluppato da Gendlin, funziona precisamente
prestando attenzione a questo segnale pre-soglia e permettendogli di emergere
nell'articolazione cosciente.

Il Modello del Campo Soma fornisce un resoconto formale di cosa è il felt sense:
è l'attività del campo emotivo sotto la soglia percettiva. È reale, causale e
continuamente presente. Modella la cognizione e il comportamento anche quando non
emerge come sentimento nominato.

## Teoria Quantistica dei Campi: Struttura, Non Metafora

La Teoria Quantistica dei Campi (QFT) è il framework della fisica delle particelle
moderna. La sua deviazione centrale dalla fisica classica è la priorità del
*campo* sulla *particella*. In QFT, ciò che chiamiamo particelle — elettroni,
fotoni — non sono oggetti fondamentali. Sono *eccitazioni* di un campo
sottostante: configurazioni locali e stabili di energia che sorgono quando il
campo riceve una perturbazione sufficiente.

Il vuoto quantistico — lo stato fondamentale del campo — non è vuoto. È uno sfondo
ribollente di fluttuazioni virtuali: eccitazioni momentanee che non hanno
abbastanza energia per persistere come particelle osservabili. Il vuoto è attivo,
ma sub-soglia.

```
  UN SINGOLO MODO DI CAMPO — ampiezza nel tempo
  (es. un modo del campo elettromagnetico; o, dopo, un modo del campo emotivo)

  │                                    ╭──────────────────╮
  │          ╭──╮              ╭──╮   ╱                    ╲             ╭──
  │   ╭─╮   ╱    ╲    ╭─╮    ╱    ╲ ╱                      ╲    ╭──╮  ╱
  │  ╱   ╲ ╱      ╲  ╱   ╲  ╱      ╳                        ╲  ╱    ╲╱
  T ╱─────╲╱────────╲╯─────╲╯────────────────────────────────╲╱──────────── T
  │         ╲────────╯       ╲──────╯                          ╲────────────
  │
  └──────────────────────────────────────────────────────────────────────► tempo

  ←─── VIRTUALE: il campo fluttua ma rimane sub-soglia ───────────────→ ←REALE→
       presente, attivo, causalmente reale — ma non localmente rilevabile     ↑
       (il VUOTO QUANTISTICO: non vuoto; ribollente di attività)        particella
                                                                         creata
```
*Figura 0. Un singolo modo di campo nella teoria quantistica dei campi. Il campo
oscilla continuamente. Sotto la soglia di rilevamento T, le eccitazioni sono
sub-soglia — reali e causalmente attive, ma non rilevabili come particelle. Il
vuoto quantistico non è vuoto; è un campo in costante movimento che non
attraversa mai del tutto la soglia. Quando l'ampiezza attraversa T, esiste una
particella: un'eccitazione localmente osservabile. La stessa struttura — campo
sempre presente, coscienza solo quando la soglia è attraversata — è il nucleo del
Modello del Campo Soma.*

Questo articolo non afferma che le emozioni siano fenomeni quantistici in
qualsiasi senso letterale: il campo soma è un campo classico, non quantizzato.
L'affermazione è più forte e specifica dell'analogia: l'oggetto matematico che
viene costruito — la funzione di Green di una varietà di campo accoppiato — è
formalmente dello stesso *tipo* degli oggetti che sorgono in QFT, differendo
solo nella dimensionalità della varietà e nella natura della sonda. Ciò che è
stato precedentemente descritto come un'analogia strutturale è qui identificato
come corrispondenza formale: una particella è un polo nel propagatore del suo
campo; un percetto emotivo cosciente è un polo nel propagatore del campo soma.
Fisica diversa. Stessa matematica.

Quella corrispondenza dà al modello vocabolario preciso per il seguente insieme
di idee, che sono centrali all'osservazione clinica dell'emozione:

- Una quantità che esiste ovunque, continuamente, anche quando non osservata
- Uno sfondo di attività sub-soglia che è reale e causalmente effettivo
- L'emergere di fenomeni osservabili (sentimenti coscienti) attraverso
  l'eccitazione di attraversamento della soglia di quello sfondo
- La possibilità di molteplici eccitazioni simultanee che interagiscono tra loro

*Nota (maggio 2026):* Un esperimento successivo (QUANT-EXP-1) dimostra che
l'estensione quantistica della landscape Hopfield usata in questo modello —
sostituendo il processo classico di Langevin con un annealer quantistico a
campo trasversale — produce un *vantaggio misurabile di raggiungibilità
topologica*: l'annealing quantistico raggiunge bacini attrattori che la dinamica
classica fredda non può raggiungere a qualsiasi livello finito di rumore. Questo
eleva la corrispondenza formale da un'affermazione strutturale a una previsione
empirica testabile. Vedere l'articolo compagno *Quantum Soma and the Penrose Gap*
(doi:10.5281/zenodo.20351230) per i risultati completi e le implicazioni
teoriche.

Un'ulteriore conseguenza segue. I fenomeni clinici dell'alessitimia — difficoltà
nell'identificare e nominare i sentimenti — e il suo apparente opposto, il
flooding emotivo o l'ipervigilanza, sono sempre stati trattati come condizioni
separate che richiedono spiegazioni separate. Nell'inquadramento della funzione
di Green, sono la stessa struttura a due estremi dello stesso parametro: la
soglia di percezione $T_i$ è troppo alta (la dinamica bulk non può attraversare
nell'esperienza osservabile) o troppo bassa (le fluttuazioni bulk inondano il
confine senza filtraggio). Questo è strutturalmente identico a uno dei più
profondi problemi aperti nella fisica delle particelle — il **problema della
gerarchia** — che chiede perché la gravità sia tanto più debole delle altre
forze. La risposta standard è che la gravità si propaga nel pieno bulk
dimensionalmente più alto mentre altre forze sono confinate a una brana
dimensionalmente più bassa; l'accoppiamento attraverso il confine della brana
determina la debolezza apparente. La corrispondenza del campo soma è esatta: la
soglia $T_i$ *è* la brana. La percezione è confinata al confine unidimensionale
di una dinamica undici-dimensionale. La gerarchia dell'esperienza emotiva —
perché il sentimento cosciente è tanto più debole e transitorio dell'attività
sottostante del campo — ha la stessa struttura formale della gerarchia delle
forze.

## Funzioni di Energia delle Reti Neurali e Reti di Hopfield

Nel 1982, John Hopfield (insignito del Premio Nobel per la Fisica nel 2024)
propose un modello di memoria associativa basato su una rete di neuroni
interconnessi (Hopfield, 1982). L'intuizione critica fu presa in prestito
direttamente dalla fisica statistica: alla rete poteva essere assegnata una
**funzione di energia** — una quantità scalare che decresce con ogni aggiornamento
di stato — tale che la rete evolvesse sempre verso un minimo locale di energia.
Questi minimi sono gli stati stabili della rete: i suoi ricordi, o più
precisamente, i suoi *attrattori*.

Hopfield osservò che la dinamica della sua rete neurale era matematicamente
identica a quella di un modello di spin-glass di Ising dalla fisica della materia
condensata — un sistema di spin magnetici interagenti che minimizza la sua
energia totale allineandosi o anti-allineandosi con i vicini. La funzione di
energia che usò è:

$$H(\mathbf{s}) = -\frac{1}{2} \sum_{i,j} W_{ij}\, s_i s_j - \sum_i \theta_i s_i$$

dove $\mathbf{s}$ è lo stato della rete, $W_{ij}$ è la forza di accoppiamento tra
unità $i$ e $j$, e $\theta_i$ è la soglia di attivazione dell'unità $i$. La rete
si muove sempre nella direzione di $H$ decrescente.

Il Modello del Campo Soma applica questa funzione di energia direttamente alla
dinamica emotiva. La *matrice di accoppiamento emotivo* $W$ codifica le relazioni
tra modi emotivi — quali emozioni si amplificano a vicenda, quali si sopprimono
— e la funzione di energia determina la direzione in cui il campo emotivo evolve
naturalmente.

La rete di Hopfield è un modello formale della *neocorteccia*: un sistema per
memorizzare pattern cognitivi e recuperarli da indizi parziali minimizzando una
funzione di energia. Ogni rete neurale artificiale costruita dal 1943 (McCulloch
e Pitts) [@mcculloch1943] — dai perceptron alle reti di backpropagation ai
transformer — sta in questo lignaggio neocorticale. Questi sistemi riconoscono
pattern, predicono sequenze e minimizzano l'errore di previsione con
sofisticatezza crescente. Nessuno di essi possiede un sistema limbico. Non hanno
valutazione interna, nessuna modulazione dell'arousal, nessuna architettura di
rilevazione delle minacce, nessuna struttura di attaccamento, nessuna
interocezione. Hanno una corteccia molto efficace.

Il Modello del Campo Soma non aggiunge al lignaggio neocorticale. Propone lo
strato architettonico che non è mai stato formalmente costruito: *un sistema
limbico artificiale*.

La memoria Hopfield è associativa e completatrice di pattern; la memoria somatica
è ripristinatrice di stato. Il campo non semplicemente ricorda cosa è successo.
Lo ri-vive. *Un corpo con un passato.*

Il desiderio successivamente riportato di Hopfield di aver incorporato qualcosa
di analogo agli «istinti materni» nella funzione di energia era, in questa
lettura, non un desiderio per una migliore corteccia. Era un'intuizione che
puntava direttamente al sistema assente — lo strato sotto la corteccia che
assegna valore, registra la minaccia, e tiene il corpo in un particolare modo di
essere molto tempo dopo l'evento che lo ha causato.

Questo posiziona il Modello del Campo Soma non come supplemento al lignaggio
neocorticale ma come suo completamento. Le reti neurali artificiali sono state,
per ottant'anni, modelli formali sempre più sofisticati della neocorteccia:
riconoscimento di pattern, previsione di sequenze, minimizzazione dell'errore. La
corteccia è stata mappata con dettaglio straordinario. Il sistema limbico — che
assegna valore, rileva minacce, modula l'arousal, mantiene l'attaccamento, e
ripristina interi stati somatici in risposta a indizi parziali — non ha avuto un
trattamento formale comparabile. La descrizione architettonica del cervello dei
vertebrati era, fino a questo articolo, costruita a metà.

**Quattro tipi di intelligenza formale.** Questo divario architettonico può
essere situato all'interno di una tassonomia più ampia. Quattro quozienti sono
stati proposti per descrivere il panorama dell'intelligenza biologica attraverso
l'uso popolare e scientifico. Mappano sui componenti formali di questo modello
con un'esattezza che non è casuale:

| Quoziente | Cosa misura | Substrato biologico | Stato del Campo Soma |
|---|---|---|---|
| IQ — cognitivo | Riconoscimento pattern, ragionamento, previsione | Neocorteccia | Costruito (1943–): McCulloch & Pitts → Hopfield → transformer |
| EQ — emotivo | Valutazione, arousal, regolazione affettiva | Sistema limbico | **Costruito qui**: $W$, $K(\tau)$, $H(\mathbf{e})$, $C_\text{HRV}$, $\dot{H}$ |
| AQ — avversità | Resilienza strutturale sotto minaccia | Asse PFC–limbico | **Costruito qui**: $S_\text{inst}$, $\partial\|W\|/\partial t$, $C_\text{HRV}^\text{recovery}$ |
| SQ — sociale | Attunement, theory of mind, navigazione relazionale | Sistema mirror, TPJ | *Prossimo articolo*: $\kappa_r$, accoppiamento multi-campo |

*Tabella 3. Quattro dimensioni dell'intelligenza biologica mappate sul Modello del
Campo Soma. Il lignaggio neocorticale (IQ) è stato formalmente modellato per
ottant'anni. L'intelligenza emotiva (EQ) e la resilienza all'avversità (AQ) sono
formalizzate qui per la prima volta. L'intelligenza sociale (SQ) è definita come
la prossima estensione del framework.*

AQ — quoziente di avversità — è formalmente la capacità di aggiornare $W$ dopo
l'avversità senza che l'avversità diventi permanentemente $W$. La sua definizione
matematica appare nella Sezione 3.4; il suo limite inferiore patologico è DPTS-C,
in cui tutte e tre le componenti di AQ sono simultaneamente compromesse
(Appendice B.2).

L'implicazione di allineamento dell'IA segue direttamente. I sistemi artificiali
attuali hanno IQ alto per costruzione e zero EQ, AQ, o SQ. L'assenza di
valutazione interna significa che la valutazione deve essere iniettata
esternamente — attraverso reinforcement learning from human feedback (RLHF) e
tecniche correlate — che è strutturalmente fragile per la stessa ragione per cui
un campo senza strato limbico è fragile: il sistema non ha alcuna posta in gioco
interna in ciò che fa. La formalizzazione del Campo Soma specifica come
apparirebbe quella posta in gioco interna, se mai fosse costruita.

Un'ulteriore nota di lignaggio merita di essere registrata. Ramsauer et al.
(2020) dimostrarono che le moderne reti di Hopfield a stato continuo sono
matematicamente equivalenti al meccanismo di self-attention nei modelli
linguistici transformer. L'operazione di attenzione softmax che guida i
contemporanei grandi modelli linguistici è un passo di recupero Hopfield. Il
Modello del Campo Soma sta in questo stesso lignaggio basato sull'energia: le
equazioni alla base della memoria associativa, della comprensione del linguaggio
e della risposta somatica al trauma sono, al livello appropriato di astrazione,
le stesse equazioni.

Un'ironia storica completa il quadro. La teoria delle stringhe non fu scoperta
come teoria delle stringhe. Nel 1968, Gabriele Veneziano scrisse un'ampiezza di
scattering — una funzione di risposta che codificava come le particelle si
disperdono — e solo dopo Nambu, Nielsen e Susskind identificarono la stringa come
qualunque oggetto produca quell'ampiezza [@veneziano1968]. La funzione di
risposta è venuta prima della cosa. Il Modello del Campo Soma ricapitola questo
ordine storico deliberatamente: l'oggetto primario è la varietà di accoppiamento
undici-dimensionale; la stringa — il percetto cosciente unidimensionale — è
ciò che la varietà produce quando viene sondata. Manteniamo la scoperta di
Veneziano e ci rifiutiamo di reificare la stringa.

---

## Le Corrispondenze Formali: Dove il Collegamento È Stato Visto

L'analogia strutturale tra QFT e Modello del Campo Soma non è meramente
concettuale. Ci sono tre luoghi in cui equazioni da discipline diverse diventano,
dopo aver sostituito le quantità rilevanti, letteralmente la stessa forma
funzionale. Quanto segue le pone fianco a fianco. Il punto non è impressionare
con la notazione ma mostrare esattamente dove è avvenuto il riconoscimento — il
momento in cui le stesse lettere greche apparivano nelle stesse posizioni in due
campi che non avevano alcuna ragione precedente di essere collegati.

**La stessa Hamiltoniana:** Modello di spin di Ising (fisica della materia
condensata, anni '20) — Rete neurale di Hopfield (neuroscienza computazionale,
1982) — Modello del Campo Soma:

$$H_{\text{Ising}}(\boldsymbol{\sigma}) = -\frac{1}{2}\sum_{i,j} J_{ij}\,\sigma_i\,\sigma_j - \sum_i h_i\,\sigma_i$$

$$H_{\text{soma}}(\mathbf{e}) = -\frac{1}{2}\sum_{i,j} W_{ij}\,e_i\,e_j - \sum_i \theta_i\,e_i$$

Sostituite $J_{ij} \to W_{ij}$, $\sigma_i \to e_i$, $h_i \to \theta_i$: identico.
Il fisico, il teorico delle reti neurali, e il clinico somatico stanno calcolando
la stessa funzione di energia su spazi di stati diversi. Il Premio Nobel di
Hopfield 2024 fu assegnato per la scoperta di questa identità tra fisica degli
spin e computazione neurale; il Modello del Campo Soma estende la stessa
identità di un passo ulteriore alla dinamica emotiva.

**La rotazione di Wick — perché lo stesso esponenziale appare in QM e nella memoria:**

Nella meccanica quantistica, l'operatore di evoluzione temporale è una fase
complessa:
$$U(t) = e^{-i\hat{H}t/\hbar}$$

Sostituite $t \to -i\tau$ (la *rotazione di Wick* — sostituendo il tempo reale
con il tempo immaginario):
$$e^{-i\hat{H}(-i\tau)/\hbar} = e^{-\hat{H}\tau/\hbar}$$

L'esponenziale complesso oscillante diventa un esponenziale reale decrescente.
Questo è il peso di Boltzmann $e^{-\beta\hat{H}}$ a $\beta = \tau/\hbar$.
L'equazione di Langevin $\dot{\mathbf{e}} = -\nabla H + \eta$ è il limite classico
di questa dinamica Wick-ruotata. Ogni simulazione del campo soma che esegue
questa equazione è, formalmente, un integrale di percorso in tempo immaginario.

**Lo stesso propagatore:** QFT euclidea (correlatore a due punti in tempo
immaginario per un campo scalare massivo) — kernel di memoria del trauma DPTS-C:

$$G_E(\tau) = \langle\phi(0)\,\phi(\tau)\rangle_{\text{QFT}} = \frac{1}{2m}\,e^{-m|\tau|}$$

$$K_{\text{trauma}}(\tau) = \sum_k A_k\,e^{-|\tau|/\tau_k}$$

Stessa forma. La massa del campo QFT $m$ corrisponde a $1/\tau_k$ — il reciproco
del tempo di decadimento della traccia di trauma. Una particella più pesante ha
un propagatore di raggio più corto; una traccia di trauma di vita più breve
decade più velocemente. L'elaborazione terapeutica (riducendo $A_k$, aumentando
$\tau_k$) è, nel linguaggio QFT, cambiare la massa e l'ampiezza del propagatore
finché la funzione di correlazione svanisce.

Il momento visivo specifico: il fattore di fase quantistico è $e^{-i\omega t}$.
Rimuovere $i$ (rotazione di Wick) e diventa $e^{-\omega\tau}$. Il kernel di
memoria è $e^{-\tau/\tau_k}$. Questi sono lo stesso esponenziale. La $i$ è
l'unica differenza tra un campo quantistico che oscilla e una traccia di trauma
che decade.

| Quantità QFT | Simbolo | Analogo del Campo Soma | Simbolo |
|---|---|---|---|
| Modo di campo | $\phi_k$ | Modo emotivo | $e_i$ |
| Costante di accoppiamento | $J_{ij}$ | Voce della matrice di accoppiamento | $W_{ij}$ |
| Massa del campo | $m$ | Tempo di decadimento inverso | $1/\tau_k$ |
| Ampiezza del propagatore | $1/2m$ | Ampiezza della traccia di trauma | $A_k$ |
| Propagatore euclideo | $G_E(\tau) \propto e^{-m\tau}$ | Kernel di memoria | $K(\tau) \propto e^{-\tau/\tau_k}$ |
| Energia del vuoto | $\langle H \rangle_0$ | Energia del campo a riposo | $H(\mathbf{e}_\text{calm})$ |
| Fluttuazione termica | $k_B T$ | Ampiezza del rumore | $\sigma_0$ |
| Rotazione di Wick | $t \to -i\tau$ | Langevin in tempo reale | $\dot{\mathbf{e}} = -\nabla H + \eta$ |

*Tabella 2. Corrispondenza formale tra quantità QFT e analoghi del Campo Soma.
Ogni riga è una singola entità matematica in due notazioni. Queste corrispondenze
non sono state costruite a posteriori; sono la ragione per cui il framework QFT
è stato riconosciuto come rilevante.*

**L'identificazione centrale — particella e percetto come poli nei loro
rispettivi propagatori.** Tutte e quattro le corrispondenze sopra seguono da un
fatto strutturale. In QFT, una particella non è un oggetto separato dal campo. È
un *polo* nel propagatore del campo — la funzione di Green valutata nello spazio
dei momenti:

$$\tilde{G}_{\text{QFT}}(k^\mu) = \frac{i}{k^2 - m^2 + i\varepsilon}$$

La particella esiste precisamente quando il quadri-momento soddisfa $k^2 = m^2$
— la *condizione on-shell*. La particella è la singolarità nella risposta del
campo a una sorgente puntiforme: la funzione di Green del campo, valutata alla
sua propria risonanza.

Diagonalizzate $W$ con autovalori $\lambda_i$ (le frequenze naturali di risonanza
dei modi emotivi). Il propagatore del campo soma — il correlatore a due punti
$\langle e_i(t)\,e_i(t')\rangle$ nel dominio della frequenza — è:

$$\tilde{G}_{ii}(\omega) = \frac{\sigma_{\text{eff}}^2}{\omega^2 + \lambda_i^2}$$

Un percetto emotivo cosciente nel modo $i$ esiste precisamente quando la
frequenza di eccitazione $\omega$ si avvicina a $i\lambda_i$ — la risonanza
naturale del modo. Il percetto è la singolarità nella risposta del campo soma a
una sonda somatica.

Mettendo i due propagatori fianco a fianco:

$$\underbrace{\frac{i}{k^2 - m^2 + i\varepsilon}}_{\text{QFT: particella a mass-shell }k^2=m^2}
\qquad\longleftrightarrow\qquad
\underbrace{\frac{\sigma_{\text{eff}}^2}{\omega^2 + \lambda_i^2}}_{\text{Campo Soma: percetto a risonanza }\omega = i\lambda_i}$$

Entrambi sono poli nel propagatore delle loro rispettive varietà di campo. Un
fotone non è il campo elettromagnetico; è la funzione di Green del campo valutata
a una risonanza. Un lampo di emozione cosciente non è il campo soma; è la
funzione di Green del campo valutata a una risonanza di attraversamento di
soglia. Le varietà differiscono — una è il vuoto spazio-tempo quadri-dimensionale,
l'altra è la geometria di accoppiamento emotivo undici-dimensionale. Il tipo
matematico è lo stesso. Questa non è analogia.

---

## Lo Schema Corporeo, l'Interocezione e il Dolore

Un modello completo del campo emotivo deve affrontare un fenomeno che i resoconti
psicologici standard dell'emozione sottospecificano costantemente: il campo non è
un modello del corpo fisico. È il *modello predittivo* del corpo del sistema
nervoso — una rappresentazione interna continuamente aggiornata di ciò che il
soma dovrebbe stare esperendo, rivista dai segnali interocettivi in arrivo.

La prova clinica di questa distinzione è il dolore dell'arto fantasma
[@ramachandran1998]. I pazienti che hanno subito amputazione esperiscono
abitualmente dolore nell'arto assente. Il dolore è reale: attiva gli stessi
circuiti neurali, produce la stessa sofferenza, e risponde agli stessi
analgesici del dolore da un arto intatto. L'arto è andato. Il modello neurale
dell'arto persiste. Ciò che fa male è la *rappresentazione del cervello* del
piede, non il piede.

Questa non è un'anomalia. È la condizione normale di ogni esperienza somatica.
Il cervello non riceve segnali grezzi dal corpo — mantiene un modello predittivo
continuo del corpo (lo *schema corporeo*) e genera esperienza somatica da quel
modello. L'interocezione — il senso dello stato corporeo interno — è una
previsione, non una lettura diretta [@seth2021]. Il cervello predice cosa
dovrebbe fare il cuore, come dovrebbe sentirsi l'intestino, dove dovrebbe essere
la tensione. Il corpo sentito è il corpo previsto.

La conseguenza formale è diretta: il vettore di stato del campo soma
$\mathbf{e}(t)$ deve includere **modi somatici** — stati di dolore, tensione
regionale, sensazione viscerale, attivazione propriocettiva — accanto ai modi
emotivi. Questi sono modi dello stesso campo, governati dalla stessa matrice di
accoppiamento $W$. Il $W_{ij}$ tra modi di fear e modi di dolore somatico è il
resoconto formale del perché la paura amplifica il dolore, perché la sicurezza lo
riduce, e perché il dolore cronico e DPTS-C sono altamente comorbidi. Non sono
condizioni separate che condividono una correlazione. Sono la stessa architettura
di attrattori che opera attraverso modi emotivi e somatici simultaneamente.

**L'arto fantasma come persistenza dell'attrattore.** I modi somatici di un arto
amputato non scompaiono da $W$ quando l'arto viene rimosso. Il modello neurale
persiste. Quando i modi di intenzione di movimento sono attivati — tentando di
muovere il piede assente — i modi di sensazione del piede sono co-attivati
tramite $W$. Se la co-attivazione supera la soglia, viene esperita come dolore.
La scatola a specchio di Ramachandran fornisce input visivo che disconferma
l'errore di previsione: nuova evidenza sensoriale che l'arto si sta muovendo,
riducendo la co-attivazione guidata dall'accoppiamento, e quindi riducendo il
dolore. Questo è $W \to W'$: terapia come riscrittura strutturale del campo.

**Il trattino portante.** Il termine *emotivo-somatico* nella letteratura clinica
non è un composto stilistico. Il trattino segna un'affermazione ontologica: stati
emotivi e stati somatici non sono due cose separate che correlano. Sono due
aspetti dello stesso campo. La matrice di accoppiamento $W$ è precisamente il
trattino, reso formale.

**Implicazione terapeutica.** Le terapie somatiche — scansione corporea, lavoro
sensomotorio, stimolazione bilaterale dell'EMDR — lavorano non sul corpo fisico
ma sul modello del corpo del cervello. Forniscono nuova evidenza interocettiva
che aggiorna la previsione. Cambiano $W$. La terapia non aggiusta il tessuto.
Aggiorna il modello.

---

## Corrispondenza con le Rappresentazioni Emotive Esistenti

Un'obiezione ragionevole a qualsiasi nuovo framework è: *c'è già una grande
quantità di struttura là fuori.* Questo è vero. La letteratura della ricerca
sulle emozioni contiene diversi sistemi rappresentativi ben sviluppati, e il
Modello del Campo Soma deve essere posizionato rispetto ad essi. La risposta
breve è che ogni rappresentazione esistente è *descrittiva*; il Modello del
Campo Soma è *dinamico*. La risposta più lunga segue.

**Tassonomie categoriche** (Ekman 1972; Plutchik 1980; Parrot 2001) assegnano
nomi e appartenenza gerarchica agli stati emotivi. Sono ontologie nel senso
formale: una T-Box di classi e relazioni di sottoclasse. La ruota di Plutchik
definisce inoltre un'operazione di *blend* — Love := Joy $\sqcap$ Trust, Awe :=
Fear $\sqcap$ Surprise — che è precisamente la costruzione `intersectionOf` di
OWL2. Questi sistemi vi dicono come chiamare uno stato. Non vi dicono come uno
stato evolva, o in quale attrattore un sistema si stabilizzi quando due
meccanismi si attivano simultaneamente.

**Modelli dimensionali** (Russell 1980; Mehrabian e Russell 1974) incorporano le
emozioni in uno spazio continuo, canonicamente Valenza × Arousal (il
*circumplex*), talvolta esteso a Piacere × Arousal × Dominanza. Questi modelli
catturano le *coordinate* di uno stato. La landscape di energia del Modello del
Campo Soma — la funzione $H(\mathbf{e})$ sullo spazio delle emozioni — è la
generalizzazione dinamica del circumplex: il circumplex è uno snapshot di
posizioni; la landscape di energia è la superficie su cui il campo si muove. Gli
attrattori stabili di $H$ sono le categorie di emozione; le loro coordinate sono
le posizioni nel circumplex.

**Modelli di processo e valutazione** (Scherer 1999; Frijda 1986; il modello OCC
di Ortony, Clove e Collins 1988) descrivono la *sequenza di valutazioni*
attraverso cui uno stimolo diventa un'emozione. Sono più vicini alla dinamica
del Campo Soma — includono stadi temporali — ma sono deterministici e a thread
singolo: una catena di valutazione, un output. Il Campo Soma sostituisce questo
con un aggiornamento di campo parallelo: tutti i modi evolvono simultaneamente,
governati dalla matrice $W$ completa.

**Schemi specifici per la musica** (BRECVEMA, Juslin e Västfjäll 2008; Juslin
*et al.* 2011; GEMS, Zentner *et al.* 2008) sono gli antecedenti più vicini al
modello presente. Il framework BRECVEMA identifica otto distinti meccanismi
psicologici attraverso cui la musica evoca emozione — Brain stem reflex,
Rhythmic entrainment, Evaluative conditioning, Contagion, Visual imagery,
Episodic memory, Musical expectancy, Aesthetic judgement — ciascuno con origini
evolutive, velocità di elaborazione e substrati neurali distinti. Questi
meccanismi sono le *proprietà degli oggetti* dell'ontologia di induzione
emotiva: specificano quali caratteristiche musicali attivano quali output
emotivi. Juslin identifica esplicitamente il problema aperto: *«Esplorare come
le varie emozioni musicali nascano attraverso l'interazione di molteplici
meccanismi psicologici è un'impresa eccitante che è appena iniziata»*
[@juslin2011handbook, p. 638]. La matrice di accoppiamento $W$ è la risposta
formale a quel problema aperto. Dove BRECVEMA dà una lista di meccanismi con
output caratteristici, il Campo Soma dà il tensore di interazione $W_{ij}$ che
specifica, con precisione numerica, cosa accade quando i meccanismi $i$ e $j$ si
attivano concorrentemente.

La connessione più profonda è spettrale. Gli *autovettori* (eigenmodes) di $W$
— le direzioni nello spazio delle emozioni che evolvono indipendentemente — sono
le risonanze naturali del campo soma: i pattern con cui il campo risuona quando
viene colpito. I meccanismi BRECVEMA sono input: eccitano righe specifiche di
$W$. Lo spettro degli autovalori di $W$ è la risposta: l'insieme di frequenze
che la varietà può sostenere. Dove BRECVEMA è una tassonomia di *stimoli*, lo
spettro degli autovalori di $W$ è una tassonomia di *risposte*. Il problema
aperto di Juslin — come i meccanismi interagiscano — è la questione di come lo
spazio degli stimoli mappi sullo spazio degli autovettori attraverso $W$. La
Sezione 3.3 sviluppa questo.

**Mappe corporee** (Nummenmaa *et al.* 2014) mappano le emozioni alla loro
distribuzione somatica — dove nel corpo viene sentita ogni emozione. Queste sono
precisamente il supporto spaziale dei modi del campo soma: la configurazione del
campo corrispondente a uno stato attrattore è la mappa corporea di quell'emozione.
Le mappe corporee sono misurazioni degli attrattori; il Campo Soma è il sistema
dinamico che le genera.

**La tabella di corrispondenza formale** estende la Tabella 2 per includere
questi sistemi:

| Rappresentazione esistente | Cosa cattura | Equivalente del Campo Soma |
|---|---|---|
| Categorie di Ekman | Etichette degli attrattori (nomi) | Valori di $\mathbf{e}$ ai minimi di energia |
| Diadi di Plutchik ($A \sqcap B$) | Attrattori di blend | Stati metastabili tra due minimi di energia |
| Circumplex di Russell | Coordinate (valenza, arousal) | Proiezione di $H(\mathbf{e})$ su due assi |
| Albero di valutazione OCC | Processo sequenziale a percorso singolo | Singola traiettoria nel campo completo |
| Meccanismi BRECVEMA | Proprietà degli oggetti: stimolo → emozione | Righe di $W$: il meccanismo $i$ attiva il modo $j$ |
| Mappe corporee (Nummenmaa) | Supporto spaziale di ogni attrattore | Struttura modale di $\mathbf{e}$ a ogni minimo |

Nessuna di queste corrispondenze richiede di modificare le rappresentazioni
esistenti o il Modello del Campo Soma. Sono conseguenze della struttura del
modello. La macchinaria formale per esplorare queste corrispondenze — tipizzando
i meccanismi BRECVEMA come costruttori induttivi Lean, i blend di Plutchik come
intersezioni di tipi, i profili dei meccanismi come proposizioni decidibili — è
sviluppata nel file compagno `src/EmotionOntology.lean`.

---

# Il Modello del Campo Soma

Il campo è primario. L'emozione sentita è secondaria — è ciò che si registra
quando il campo viene sondato. Questa è la stessa relazione ontologica che tra
un campo quantistico e una particella: il campo esiste continuamente e ovunque;
la particella è ciò che si osserva al momento della misurazione. Il Modello del
Campo Soma non descrive di cosa sono *fatte* le emozioni. Descrive la varietà la
cui risposta all'impulso *è* esperienza emotiva cosciente.

## Le Emozioni come Campo d'Onda Persistente

L'affermazione fondazionale del Modello del Campo Soma è semplice: le emozioni
non sono eventi. Sono un *campo* — una quantità distribuita, continua, definita
sull'intero soma (sistema corpo-mente) in ogni momento.

Questo campo ha due componenti accoppiate:

1. **L'onda somatica** $\mathbf{E}_\text{body}(x,t)$: distribuita attraverso il
   corpo come pattern di sensazione viscerale, tono muscolare, propriocezione,
   interocezione e stato autonomico.
2. **L'onda neurale** $\mathbf{E}_\text{neural}(x,t)$: distribuita attraverso il
   sistema nervoso come pattern di attivazione in circuiti corticali, sottocorticali
   e periferici.

Questi due componenti non sono sistemi separati. Sono accoppiati — ciascuno
influenza continuamente l'altro. Il campo emotivo totale è il loro stato
combinato:

$$\mathbf{E}(x,t) = \mathbf{E}_\text{body}(x,t) \otimes \mathbf{E}_\text{neural}(x,t)$$

Il campo è caratterizzato da:

- **Molteplicità**: molteplici modi emotivi possono essere simultaneamente attivi
  e interferenti
- **Continuità**: esiste in ogni momento, non solo durante episodi di sentimento
  cosciente
- **Distribuzione spaziale**: diversi aspetti del campo sono localizzati in
  diverse regioni del soma (la familiare osservazione clinica che grief è sentito
  nel petto, fear nell'intestino, anger nella mascella e nei pugni)
- **Dinamica temporale**: il campo evolve continuamente, guidato dalla funzione
  di energia

![](figures/fig1_architecture.pdf){ width=90% }
*Figura 1. Il Campo Soma. Corpo e cervello non sono contenitori separati di
emozione ma due componenti accoppiate di un singolo campo d'onda distribuito.
Nessuno è primario; ciascuno modifica continuamente l'altro. I simboli ≋
indicano che l'attività dell'onda è sempre presente in ogni regione, non solo
durante episodi di sentimento cosciente.*

## La Soglia di Percezione

Non tutta l'attività nel campo emotivo è coscientemente percepita. Il campo ha
una **soglia di percezione** $T_i$ per ogni modo emotivo $i$. Sotto questa soglia,
il modo emotivo è sub-percettivo: esiste, influenza comportamento e fisiologia,
ma non emerge come sentimento cosciente nominato.

$$\text{L'emozione } i \text{ è coscientemente percepita} \iff |\mathbf{E}_i(t)| > T_i$$

Questo attraversamento di soglia corrisponde precisamente all'analogia QFT di
eccitazione: il modo emotivo si comporta come una particella virtuale che ha
accumulato abbastanza energia per diventare reale — per emergere dallo sfondo
sub-soglia ed entrare nella consapevolezza.

Questo spiega una serie di fenomeni clinicamente significativi:

| Osservazione Clinica | Resoconto del Campo Soma |
|---|---|
| Il paziente non riferisce sentimento ma mostra segni fisiologici di distress | Attività di campo sub-soglia sotto $T_i$ |
| Improvviso flooding emotivo inaspettato in sessione | Rapido attraversamento di soglia dopo accumulo graduale |
| Emozione sentita somaticamente ma non nominata | Soglia attraversata in $\mathbf{E}_\text{body}$, non ancora in $\mathbf{E}_\text{neural}$ |
| Alessitimia (difficoltà nell'identificare i sentimenti) | $T_i$ elevato — alta soglia che richiede più energia per essere attraversata |
| Ipervigilanza / flooding emotivo | $T_i$ abbassato — soglia ridotta, il campo attraversa facilmente al cosciente |

*Tabella 1. Osservazioni cliniche mappate sul modello della soglia di percezione.*

![](figures/fig2_threshold.pdf){ width=90% }
*Figura 2. La soglia di percezione T_i per un singolo modo emotivo. Il campo è
attivo continuamente (traccia inferiore). L'esperienza cosciente sorge solo
quando l'ampiezza supera T_i (traccia superiore). Tutto ciò che è sotto la linea
è ancora lì — modellando corpo e comportamento prima di poter essere nominato.*


![](figures/fig0_field_mode.pdf){ width=95% }
*Figura 0. Attività continua del campo soma (blu) con un singolo evento di
attraversamento di soglia. Il campo è sempre attivo; l'esperienza cosciente
(ombreggiata) sorge solo quando l'ampiezza supera la soglia di percezione θ
(rossa tratteggiata). Sotto la soglia: reale, causalmente attiva, ma non ancora
cosciente.*

## L'Interazione dei Modi Emotivi

Molteplici modi emotivi sono simultaneamente attivi nel campo in ogni momento.
Non semplicemente co-esistono: interagiscono. La natura di queste interazioni è
codificata nella **matrice di accoppiamento emotivo** $W$, dove $W_{ij}$
rappresenta l'influenza del modo emotivo $j$ sul modo emotivo $i$.

- Se $W_{ij} > 0$: l'emozione $j$ amplifica l'emozione $i$ (es., fear può
  amplificare shame)
- Se $W_{ij} < 0$: l'emozione $j$ sopprime l'emozione $i$ (es., calm sopprime
  l'ansia)
- Se $W_{ij} = 0$: le emozioni $i$ e $j$ sono indipendenti

Il campo evolve secondo il gradiente di energia:

$$\dot{\mathbf{e}}(t) = -\nabla H(\mathbf{e}) + \eta(t)$$

dove $\eta(t)$ rappresenta le fluttuazioni continue di basso livello del campo
sub-percettivo — l'equivalente emotivo del rumore di vuoto quantistico. Il campo
è sempre in movimento, sempre alla ricerca di energia inferiore, mai in riposo
assoluto.

---

## L'Architettura a Tre Strati

Il sistema nervoso che implementa il campo soma non è architettonicamente piatto.
Tre strati gerarchicamente organizzati contribuiscono alla dinamica del campo,
ciascuno corrispondente a un distinto substrato evolutivo e a un distinto ruolo
nel modello. La letteratura clinica (Porges, 2011; van der Kolk, 2014; Ogden et
al., 2006) converge su questa stratificazione; quanto segue è la sua espressione
formale.

**Strato 1 — Tronco encefalico / baseline autonomica.** Le strutture più antiche:
nuclei vagali, sistemi di arousal, macchinaria interocettiva. Nel modello, questo
strato è rappresentato dal termine di rumore e, specificamente, dalla coerenza
della variabilità della frequenza cardiaca $C_{\text{HRV}}$, che modula
l'ampiezza effettiva del rumore attraverso tutto il campo:
$$\sigma_{\text{eff}} = \frac{\sigma_0}{C_{\text{HRV}}}$$
Alta coerenza HRV restringe il rumore effettivo, stabilizzando il campo nel suo
attrattore attuale. Questo è il meccanismo del biofeedback HRV come intervento
regolatorio: non mira a alcun modo emotivo specifico ma abbassa il pavimento
delle fluttuazioni dell'intero campo.

**Estensione dello Strato 1: accelerazione cardiaca e inclinazione della
landscape.** Il termine $C_{\text{HRV}}$ misura lo *stato attuale* della
regolarità cardiaca — dove è il cuore. Una quantità complementare è $\dot{H}(t)$,
la prima derivata temporale della frequenza cardiaca, in unità di battiti/s$^2$.
Questa è l'**accelerazione cardiaca**: non quale sia la frequenza cardiaca, ma
dove sta andando.

Il parallelo dimensionale con la gravità è esatto: l'accelerazione gravitazionale
$g$ porta unità m/s$^2$; l'accelerazione cardiaca $\dot{H}$ porta unità
battiti/s$^2$. Entrambe sono accelerazioni; entrambe descrivono un campo di
forza piuttosto che una posizione. La gravità non vi dice dove è una massa di
prova — vi dice come si muoverà dopo. L'accelerazione cardiaca vi dice non il BPM
attuale ma la direzione del prossimo: lo stato N+1.

Nel campo soma, $\dot{H}(t)$ entra nella dinamica non come modulazione del rumore
ma come **inclinazione della landscape** — un bias variabile nel tempo aggiunto
all'Hamiltoniana che inclina la funzione di energia verso attrattori di
attivazione o riposo:

$$H(\mathbf{e}, t) = H_0(\mathbf{e}) - \alpha\,\dot{H}(t)\,\boldsymbol{\beta}\cdot\mathbf{e}$$

dove $\alpha > 0$ è la costante di accoppiamento cardio-somatica e
$\boldsymbol{\beta}$ è un vettore di accoppiamento ai modi (al primo ordine,
$\boldsymbol{\beta} = \mathbf{1}$: l'inclinazione agisce uniformemente su tutti i
modi). Quando $\dot{H}(t) > 0$ (cuore in accelerazione), la landscape si inclina
verso stati di attivazione superiore prima che qualsiasi soglia cognitiva o
affettiva sia attraversata. Quando $\dot{H}(t) < 0$ (cuore in decelerazione), si
inclina verso il riposo. L'equazione completa a tre strati che include il
termine di accelerazione cardiaca è:

$$\dot{\mathbf{e}}(t) = -\nabla H_0(\mathbf{e}) + \alpha\,\dot{H}(t)\,\boldsymbol{\beta}
  + R_{\text{PFC}}(\mathbf{e}, t)
  + \frac{\sigma_0}{C_{\text{HRV}}}\,\xi(t)$$

I due termini cardiaci servono funzioni distinte: $C_{\text{HRV}}$ (stato)
modula il pavimento del rumore; $\dot{H}$ (accelerazione) inclina la landscape
deterministica. Entrambi sono necessari per un resoconto completo dell'influenza
cardiaca sul campo.

**Valore clinico predittivo.** Un paziente con BPM = 90 e $\dot{H} = +4$
battiti/s$^2$ si sta avvicinando alla soglia; uno con BPM = 90 e $\dot{H} = -4$
battiti/s$^2$ sta retreating da essa. Lo snapshot è identico; le traiettorie sono
opposte. L'accelerazione cardiaca è quindi un segnale di allarme precoce per gli
attraversamenti di soglia — rilevabile allo Strato 1 prima che il campo emotivo
allo Strato 2 abbia attraversato la sua soglia. Questo ha supporto indipendente
in cardiologia: Bauer et al. (2006) dimostrarono che la *capacità di
accelerazione* e la *capacità di decelerazione* della frequenza cardiaca — stime
di $\dot{H}$ su una finestra cardiaca — portano informazioni prognostiche
indipendenti dalle misure HRV convenzionali.

**Il principio di equivalenza somatica.** Il termine di accelerazione cardiaca
$\alpha\,\dot{H}\,\boldsymbol{\beta}$ è strutturalmente identico nell'equazione
a qualsiasi altro termine forzante. Dalla prospettiva del campo stesso —
dall'esperienza cosciente — l'attivazione guidata dal cuore è indistinguibile
dall'attivazione guidata dall'evento. Un'improvvisa accelerazione della frequenza
cardiaca inclina la landscape esattamente con lo stesso meccanismo di una
minaccia esterna o di una memoria intrusiva. Il campo non ha accesso all'origine
dell'inclinazione. Questo è il resoconto formale di un fenomeno clinicamente ben
documentato: l'ansia iniziata da irregolarità cardiaca (aritmia, ipotensione
posturale, caffeina, sforzo) è esperita come emotivamente causata, perché il
segnale somatico è identico. La disambiguazione richiede o misurazione esterna o
indagine interocettiva deliberata che possa distinguere le due fonti.

**Strato 2 — Sistema limbico / memoria emotiva.** Il substrato primario del
Modello del Campo Soma. La matrice di accoppiamento $W$, il kernel di memoria
$K(\tau)$, l'Hamiltoniana $H(\mathbf{e})$ e la soglia $T$ appartengono tutti
qui. Lo strato limbico memorizza stati emotivo-somatici e li ripristina in
risposta a indizi corporei parziali: una rete di Hopfield continua, asimmetrica
e temporalmente estesa che opera su stati somatici piuttosto che pattern
cognitivi. Questo è lo strato architettonico che è stato assente da ogni rete
neurale artificiale dal 1943 (McCulloch e Pitts) [@mcculloch1943]. La corteccia
è stata modellata molte volte; il sistema limbico no.

**Plasticità strutturale sotto avversità.** Il framework del Campo Soma permette
una caratterizzazione formale della resilienza del campo sotto condizioni
avverse. Definite l'*indice di plasticità* $\Pi$ come composito di tre proprietà
misurabili del campo:

$$\Pi \;=\; \frac{1}{S_{\text{inst}}} + \left.\frac{\partial \|W\|}{\partial t}\right|_{\text{adversity}} + C_{\text{HRV}}^{\text{recovery}}$$

I tre termini corrispondono a: (i) quanto accessibili rimangono gli attrattori
di stato regolato sotto avversità ($1/S_{\text{inst}}$, accessibilità
dell'istantone — Sezione 4.4); (ii) quanto la matrice di accoppiamento può
adattarsi strutturalmente dopo un attraversamento di soglia
($\partial \|W\|/\partial t$, la componente di plasticità); e (iii) quanto
rapidamente il pavimento HRV recupera dopo l'attivazione
($C_{\text{HRV}}^{\text{recovery}}$, la componente di resilienza regolatoria). Il
DPTS-C complesso è la presentazione clinica di $\Pi$ cronicamente basso attraverso
tutti e tre i termini simultaneamente: alte barriere agli attrattori regolati,
un $W$ rigido dominato da configurazioni di minaccia, e recupero $C_{\text{HRV}}$
compromesso. La plasticità strutturale è la capacità del campo di aggiornare $W$
all'indomani dell'avversità senza che l'avversità *diventi* permanentemente $W$.

**Strato 3 — Neocorteccia / strato regolatorio prefrontale.** Modulazione
dall'alto verso il basso dello Strato 2, rappresentata come termine regolatorio
$R_{\text{PFC}}(\mathbf{e}, t)$. La dinamica completa del campo diventa:

$$\dot{\mathbf{e}}(t) = -\nabla H(\mathbf{e}(t))
  + R_{\text{PFC}}(\mathbf{e}, t)
  + \frac{\sigma_0}{C_{\text{HRV}}}\, \xi(t)$$

$R_{\text{PFC}}$ rappresenta attenzione volontaria, tecnica terapeutica e
riappraisal cosciente che agisce sul campo. Non è una correzione dello Strato 2
ma una modulazione di esso. Sotto engagement terapeutico sostenuto,
$R_{\text{PFC}}$ partecipa alla modifica strutturale $W \to W'$ che costituisce
la trasformazione in avanti (Sezione 7).

La **soglia $T$ è il confine Strato 2 / Strato 3**: la dinamica sub-soglia è
elaborata limbicamente e rimane sotto la consapevolezza cosciente; gli eventi di
attraversamento di soglia entrano nello Strato 3 e diventano disponibili per
narrazione, creazione di significato, e risposta volontaria. Questa è la base
formale per l'osservazione clinica che l'insight senza attivazione somatica è
limitato, e l'attivazione somatica senza engagement dello Strato 3 non può
produrre cambiamento strutturale: gli strati sono accoppiati, non indipendenti.
$R_{\text{PFC}}$ richiede un attraversamento di soglia per avere qualcosa con
cui lavorare.

L'equazione di Langevin a due termini introdotta nella Sezione 3.3 è il caso
speciale dello Strato 2 ($R_{\text{PFC}} = 0$, $C_{\text{HRV}} = 1$). Tutte le
sezioni successive sviluppano quel caso speciale. L'equazione completa a tre
strati è la forma generale.

---
