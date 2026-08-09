
# Capitolo 7: La Stessa Equazione, Tre Volte

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   «L'irragionevole efficacia della matematica nelle             │
  │    scienze naturali.»                                           │
  │                                                                  │
  │                               — Eugene Wigner, 1960             │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **OBIETTIVI DI APPRENDIMENTO**
>
> Alla fine di questo capitolo, capirete:
>
> - Perché la stessa Hamiltoniana appare nella fisica della materia condensata,
>   nella teoria delle reti neurali e nel modello del campo soma
> - Cos'è la rotazione di Wick e perché collega le oscillazioni quantistiche alla
>   memoria del trauma
> - Cosa sono i diagrammi a corde e i diagrammi di Feynman e cosa dicono
>   sull'interazione emotiva
> - Il significato di «la stessa struttura matematica» come evidenza di realtà
>   strutturale

---

## 7.1 Il Momento del Riconoscimento

Il Modello del Campo Soma non è iniziato con un piano per collegarlo alla teoria
quantistica dei campi. È iniziato con una domanda di neuroscienza: qual è il modello
matematico più semplice di un campo emotivo che ha stati stabili, transizioni dinamiche
e la capacità di essere modificato dall'esperienza?

La risposta che è emersa — un campo Hamiltoniano con una matrice di accoppiamento,
che evolve sotto la dinamica di Langevin — si è rivelata essere un'equazione che i
fisici avevano già visto.

È l'Hamiltoniana della rete di Hopfield. Che è l'Hamiltoniana del modello di Ising.
Che è il limite classico di una teoria quantistica dei campi nel tempo immaginario.

Questa non è una coincidenza creata a posteriori. È la firma di qualcosa: quando si
scrive «il modello più semplice di un campo con stati stabili», si arriva a
un'equazione che appare in tre discipline separate perché tre discipline separate
hanno indipendentemente risposto alla stessa domanda matematica.

## 7.2 La Stessa Hamiltoniana

Il modello di Ising (fisica della materia condensata, inizio XX secolo) descrive un
reticolo di spin interagenti — momenti magnetici che possono puntare in alto o in
basso:

$$H_{\text{Ising}} = -\frac{1}{2}\sum_{i,j} J_{ij}\,\sigma_i\,\sigma_j - \sum_i h_i\,\sigma_i$$

La rete di Hopfield (neuroscienza computazionale, Hopfield 1982 — Premio Nobel 2024)
descrive una rete di neuroni interagenti che memorizza i ricordi come stati stabili:

$$H_{\text{Hopfield}} = -\frac{1}{2}\sum_{i,j} W_{ij}\,x_i\,x_j - \sum_i \theta_i\,x_i$$

Il Modello del Campo Soma descrive la landscape di energia del campo emotivo:

$$H_{\text{soma}} = -\frac{1}{2}\sum_{i,j} W_{ij}\,e_i\,e_j - \sum_i \theta_i\,e_i$$

Sostituite $J_{ij} \to W_{ij}$, $\sigma_i \to e_i$, $h_i \to \theta_i$: queste sono la
stessa equazione scritta con lettere diverse. La stessa matematica descrive spin
magnetici in un cristallo, ricordi in una rete neurale, e stati emotivi in un corpo.

Questa è l'equivalenza di Hopfield — l'osservazione per cui Hopfield ricevette il
Premio Nobel: che il modello di spin di Ising e una rete di memoria neurale stanno
computando la stessa funzione di energia. Il Modello del Campo Soma estende questa
equivalenza di un passo ulteriore: la stessa computazione descrive anche la struttura
di attrattori della dinamica emotiva.

Collocata nella storia più lunga della modellizzazione di reti neurali, la posizione
del Modello del Campo Soma è più precisa di *un'estensione del framework Hopfield*.
Ogni rete neurale artificiale costruita da McCulloch e Pitts (1943) — perceptron, reti
di backpropagation, LSTM, transformer — è un modello formale della neocorteccia.
Questi sistemi imparano a riconoscere pattern e a minimizzare l'errore di previsione
con sofisticatezza crescente. Nessuno di essi possiede un sistema limbico: nessuna
valutazione interna, nessuna architettura di rilevamento delle minacce, nessuna
modulazione dell'arousal, nessun loop interocettivo dal corpo di nuovo al campo.

La rete di energia di Hopfield è il più elegante dei modelli neocorticali. Descrive il
completamento di pattern associativi — esattamente ciò che il sistema
ippocampo-corticale fa per la memoria dichiarativa. Il Modello del Campo Soma non è
una migliore corteccia. È il modello del sistema sotto la corteccia che è stato in
attesa, dal 1943, di essere scritto.

Hopfield in seguito descrisse il desiderio di aver incorporato qualcosa di analogo agli
'istinti materni' nella funzione di energia. Alla luce del Modello del Campo Soma,
quel desiderio non era un desiderio per un migliore modello neocorticale. Era
un'intuizione che puntava allo strato assente — il sistema limbico — per cui non aveva
un linguaggio formale all'epoca.

---

> **GOING DEEPER: La Metà Mancante del Cervello**
>
> Ogni rete neurale artificiale mai costruita — dal perceptron nel 1943 ai grandi
> modelli linguistici di oggi — è un modello formale della neocorteccia. La
> neocorteccia riconosce pattern, predice sequenze e minimizza l'errore. È stata
> formalmente descritta, addestrata e dispiegata su scala straordinaria.
>
> Il sistema limbico no.
>
> Il sistema limbico è la struttura più antica e profonda: amigdala, ippocampo,
> ipotalamo, corteccia cingolata. Assegna valore. Rileva la minaccia prima che la
> corteccia abbia finito l'elaborazione. Ripristina interi stati corporei in risposta
> a un indizio parziale — un odore, una texture, un tono di voce. Tiene il trauma. È
> il sistema che fa sì che le cose *contino*.
>
> L'intelligenza artificiale ha una corteccia molto efficace. Non ha un sistema
> limbico. Può dirvi che il fuoco è caldo. Non può essere bruciata.
>
> Il Modello del Campo Soma fornisce la prima architettura formale di teoria di campo
> per il sistema limbico. Insieme al framework di Hopfield descrive — per la prima
> volta — entrambi i principali substrati computazionali del cervello dei vertebrati.
> L'architettura è, formalmente, completa.

---

## 7.3 La Rotazione di Wick: Una Sostituzione

La corrispondenza più profonda nel modello è quella che connette la meccanica
quantistica alla memoria del trauma. Richiede una singola sostituzione.

Nella meccanica quantistica, lo stato di un sistema evolve nel tempo tramite
l'operatore di evoluzione temporale:
$$U(t) = e^{-i\hat{H}t/\hbar}$$

La caratteristica chiave è la $i$ — l'unità immaginaria. Questo rende l'esponenziale
oscillatorio: $e^{-i\omega t} = \cos(\omega t) - i\sin(\omega t)$. Uno stato
quantistico oscilla nel tempo invece di decadere.

Ora fate la sostituzione $t \to -i\tau$ — sostituendo il tempo reale con il tempo
immaginario. Questa è la **rotazione di Wick**, dal nome di Gian-Carlo Wick (1954):

$$e^{-i\hat{H}(-i\tau)/\hbar} = e^{-\hat{H}\tau/\hbar}$$

La fase oscillatoria è diventata un esponenziale decrescente reale. Questo è il peso
di Boltzmann $e^{-\beta\hat{H}}$ dalla meccanica statistica (a temperatura inversa
$\beta = \tau/\hbar$). La rotazione di Wick è il ponte tra la meccanica quantistica e
la fisica termica.

```
  ╔════════════════════════════════════════════════════════════════════╗
  ║                    LA ROTAZIONE DI WICK                           ║
  ╠════════════════════════════════════════════════════════════════════╣
  ║                                                                    ║
  ║  MECCANICA QUANTISTICA           FISICA TERMICA / SOMATICA         ║
  ║  (tempo reale t)                 (tempo immaginario τ = it)        ║
  ║                                                                    ║
  ║  e^{-iHt/ℏ}    ──────────────→   e^{-Hτ/ℏ}                       ║
  ║                   t → -iτ                                         ║
  ║                                                                    ║
  ║  oscilla:                        decade:                          ║
  ║                                                                    ║
  ║       ╭╮  ╭╮  ╭╮                    │╲                            ║
  ║   ────╯╰──╯╰──╯╰──                  │  ╲                          ║
  ║                                     │    ╲___                     ║
  ║  Funzione d'onda                     │        ─────────           ║
  ║  quantistica: oscilla               Peso termico: decade          ║
  ║                                                                    ║
  ║  La i è l'unica differenza tra queste due funzioni.               ║
  ║  Rimuovere i → l'oscillazione quantistica diventa decadimento     ║
  ║  esponenziale.                                                    ║
  ╚════════════════════════════════════════════════════════════════════╝

  Figura 7.1. La rotazione di Wick. Una singola sostituzione (t → -iτ) trasforma il
  fattore di fase oscillatorio quantistico nell'esponenziale decrescente reale della
  fisica termica. Il kernel di memoria K(τ) = Σ Aₖ e^{-|τ|/τₖ} ha esattamente questa
  forma. La i nell'esponente quantistico è l'unica differenza matematica tra un campo
  quantistico che oscilla e una traccia di trauma che decade.
```

E il kernel di memoria per il trauma DPTS-C?

$$K_{\text{trauma}}(\tau) = \sum_k A_k\, e^{-|\tau|/\tau_k}$$

Questo è il propagatore Wick-ruotato. La massa del campo QFT $m$ corrisponde a
$1/\tau_k$. L'ampiezza del propagatore $1/2m$ corrisponde a $A_k$. Questi non sono
analoghi. Sono lo stesso oggetto matematico con nomi specifici di dominio diversi.

## 7.4 Diagrammi di Feynman per le Emozioni

I diagrammi di Feynman furono sviluppati negli anni '40 come modo di calcolare
interazioni nella teoria quantistica dei campi. Rappresentano le particelle come linee
e le interazioni (accoppiamenti) come vertici. Un fotone e un elettrone che si
incontrano in un vertice e si disperdono è un diagramma di Feynman. Le regole per
calcolare le grandezze fisiche da questi diagrammi sono esatte — ogni diagramma
corrisponde a un integrale specifico.

Negli anni '90 e 2000, fu stabilito (Penrose 1971, Baez e Lauda 2011, Selinger 2010)
che i diagrammi di Feynman sono un caso speciale di un linguaggio matematico più
generale: **diagrammi a corde** — diagrammi per morfismi in categorie monoidali
simmetriche. Questa non è una semplificazione. È un teorema. I diagrammi a corde, i
diagrammi di Feynman, e i morfismi in categorie monoidali simmetriche sono lo stesso
oggetto matematico in tre notazioni.

Le operazioni del campo soma — accoppiamento di modi emotivi, composizione di
operatori di campo, prodotti tensoriali di stati — sono morfismi esattamente in questo
senso. Il seguente diagramma rappresenta due modi emotivi che si combinano in un
vertice di interazione:

```
  INTERAZIONE EMOTIVA COME VERTICE DI FEYNMAN

  Fear ────────╮
               ├───────── Freeze
  Shame ───────╯
  (accoppiamento W_{fear,shame → freeze})

  Questo è identico in struttura a un vertice di Feynman:

  elettrone ───────╮
                   ├───────── elettrone (disperso)
  fotone ──────────╯

  Entrambi sono morfismi:  A ⊗ B → C
  in una categoria monoidale simmetrica.
  Fear ⊗ Shame → Freeze  è un morfismo valido nella categoria del campo soma.
```

La rilevanza clinica: il linguaggio dei diagrammi di Feynman ci dà un modo di
rappresentare e calcolare le interazioni emotive combinatoriamente — chiedere quali
sono le «regole di Feynman» per l'accoppiamento emotivo, e quali interazioni composite
sono possibili.

## 7.5 La Tabella di Corrispondenza

```
  ┌──────────────────────────┬────────────────────────────────────┐
  │ Grandezza QFT            │ Analogo del Campo Soma             │
  ├──────────────────────────┼────────────────────────────────────┤
  │ Modo di campo φₖ         │ Modo emotivo eᵢ                    │
  │ Costante di accopp. Jᵢⱼ  │ Voce della matrice Wᵢⱼ             │
  │ Massa del campo m        │ Tempo di decad. inverso 1/τₖ       │
  │ Ampiezza propagat. 1/2m  │ Ampiezza traccia trauma Aₖ         │
  │ Propagatore euclideo G_E │ Kernel di memoria K(τ)             │
  │ Energia del vuoto ⟨H⟩₀   │ Energia campo di riposo H(e_calm)  │
  │ Fluttuazione termica k_BT│ Ampiezza del rumore σ₀             │
  │ Rotazione Wick t → −iτ   │ Dinamica di Langevin in tempo reale│
  │ Vertice di Feynman       │ Interazione di modi emotivi        │
  │ Morfismo A⊗B → C         │ Operazione di accoppiamento campo  │
  └──────────────────────────┴────────────────────────────────────┘

  Tabella 7.1. Corrispondenza formale tra grandezze QFT e analoghi del Campo Soma.
  Ogni riga è una singola entità matematica in due sistemi di notazione diversi. Le
  corrispondenze non sono analogie approssimate — sono identificazioni esatte sotto
  la rotazione di Wick e l'equivalenza di Hopfield.
```

---

> **GOING DEEPER: Il Teorema di Coerenza di Baez–Lauda**
>
> Nel 2011, John Baez e Aaron Lauda dimostrarono un teorema di coerenza che stabilisce
> che i diagrammi a corde sono una notazione completa e corretta per i morfismi in
> categorie monoidali simmetriche. Questo significa: qualsiasi cosa si possa scrivere
> come morfismo in una categoria monoidale simmetrica, si può disegnare come diagramma
> a corde, e viceversa, con fedeltà perfetta.
>
> I diagrammi di Feynman sono diagrammi a corde per la categoria monoidale simmetrica
> delle rappresentazioni del gruppo di Poincaré (il gruppo di simmetria dello
> spaziotempo). I diagrammi di rete tensoriale (usati nell'informazione quantistica e
> nella materia condensata) sono diagrammi a corde per la stessa struttura.
>
> Le operazioni del campo soma — accoppiamento di modi emotivi, composizione di
> campo, prodotti tensoriali di stati — sono morfismi in una categoria monoidale
> simmetrica. Quindi, possono essere disegnati come diagrammi a corde. Quindi, possono
> essere calcolati con lo stesso calcolo diagrammatico dei diagrammi di Feynman.
>
> Questa non è l'affermazione che le emozioni siano quantistico-meccaniche. È
> l'affermazione che la matematica della composizione e dell'accoppiamento è universale
> — appare ovunque le cose interagiscano, indipendentemente da cosa siano le cose.

---

> **TERMINI CHIAVE**
>
> **Rotazione di Wick** — la sostituzione $t \to -i\tau$ che trasforma la dinamica
> quantistica oscillatoria in dinamica termica/stocastica in tempo reale.
>
> **Diagramma di Feynman** — una notazione diagrammatica per calcolare ampiezze di
> interazione nella teoria quantistica dei campi; ogni diagramma rappresenta un
> contributo integrale specifico a una grandezza fisica.
>
> **Diagramma a corde** — una notazione diagrammatica per morfismi in una categoria
> monoidale simmetrica; identica in struttura ai diagrammi di Feynman secondo il
> teorema di Baez–Lauda.
>
> **Morfismo** — una mappa che preserva la struttura tra oggetti in una categoria; la
> nozione generale che sussume funzioni, mappe lineari e interazioni fisiche.

---

\newpage

# Capitolo 8: Il Sistema Nervoso come Diagramma di Fase

---

> **OBIETTIVI DI APPRENDIMENTO**
>
> Alla fine di questo capitolo, capirete:
>
> - Cosa sono le transizioni di fase e perché si applicano al sistema nervoso
> - Come i tre stati polivagali corrispondano a fasi diverse
> - Perché i cambiamenti di stato nel trauma si sentono improvvisi invece che
>   graduali
> - Cosa rappresenta l'ADHD in termini termodinamici

---

## 8.1 Transizioni di Fase

L'acqua può esistere come ghiaccio, liquido o vapore. A pressione atmosferica,
transita tra queste fasi a temperature specifiche: 0°C e 100°C. Le transizioni sono
drammatiche: aggiungere energia al ghiaccio sotto 0°C cambia la sua temperatura
gradualmente; aggiungere energia esattamente a 0°C non produce alcun cambiamento di
temperatura — l'energia va interamente nello spezzare il reticolo cristallino,
riorganizzando le molecole di acqua da una struttura rigida ordinata a una fluida
disordinata. Questa è una **transizione di fase**: una riorganizzazione qualitativa
della struttura del sistema in un punto critico, piuttosto che un cambiamento liscio
e graduale.

Le transizioni di fase appaiono ovunque ci sia una landscape di energia con multiple
fasi stabili, e un parametro (temperatura, pressione, campo magnetico) che sposta la
stabilità relativa di quelle fasi. Sono universali.

## 8.2 Le Tre Fasi del Sistema Nervoso

La gerarchia polivagale descrive tre stati funzionali del sistema nervoso autonomo.
Nel Modello del Campo Soma, questi corrispondono a tre fasi distinte del campo:

```
  ╔════════════════════════════════════════════════════════════════════╗
  ║              DIAGRAMMA DI FASE DEL CAMPO SOMA                     ║
  ╠════════════════════════════════════════════════════════════════════╣
  ║                                                                    ║
  ║  Livello ▲  ALTO                                                   ║
  ║  arousal │   ╔════════════════════════╗                            ║
  ║          │   ║  FASE SIMPATICA        ║ Fight / Flight            ║
  ║          │   ║  Grandi oscillazioni   ║ Alto rumore               ║
  ║          │   ║  Transizioni rapide    ║ Mobilizzazione            ║
  ║          │   ╚════════════════════════╝                            ║
  ║          │                ↕ confine di fase (T_upper)             ║
  ║  MEDIO   │   ╔════════════════════════╗                            ║
  ║          │   ║  FASE VAGALE VENTRALE  ║ Engagement sociale        ║
  ║          │   ║  Oscillazioni stabili  ║ Rumore regolato           ║
  ║          │   ║  Capacità sociale      ║ Window of Tolerance       ║
  ║          │   ╚════════════════════════╝                            ║
  ║          │                ↕ confine di fase (T_lower)             ║
  ║    BASSO │   ╔════════════════════════╗                            ║
  ║          │   ║  FASE VAGALE DORSALE   ║ Freeze / Shutdown         ║
  ║          │   ║  Oscillazioni minime   ║ Rumore molto basso        ║
  ║          │   ║  Disconnessione        ║ Immobilizzazione          ║
  ║          │   ╚════════════════════════╝                            ║
  ║          └──────────────────────────────────────────────────────   ║
  ║               livello di minaccia percepita →                     ║
  ╚════════════════════════════════════════════════════════════════════╝

  Figura 8.1. Il sistema nervoso come diagramma di fase. Tre fasi distinte
  corrispondono ai tre stati polivagali. I confini di fase (T_upper e T_lower) segnano
  le transizioni. Per un sistema nervoso regolato, la maggior parte dell'esperienza
  si verifica nella fase vagale ventrale. Per un sistema modificato dal trauma, il
  confine inferiore T_lower può essere vicino allo stato di riposo vagale ventrale,
  rendendo la transizione al freeze più facile da innescare.
```

La caratteristica critica di una transizione di fase — in contrapposizione a un
cambiamento liscio del livello di arousal — è che accade *tutto in una volta*. Sotto
il confine di fase, aggiungere arousal aumenta il livello di attivazione. Al confine
di fase, il sistema si ribalta: prende il sopravvento un'organizzazione
qualitativamente diversa. Questo è il motivo per cui la risposta di congelamento
(vagale dorsale) non è «molto molto calmo»: è una fase diversa con proprietà fisiche
diverse, entrata attraverso una transizione di fase, non raggiunta dalla riduzione
graduale.

Questo spiega anche perché i clienti in terapia talvolta descrivono i cambiamenti di
stato come avvenuti senza preavviso: dalla loro prospettiva, stavano bene, e poi
improvvisamente non lo erano. Dalla prospettiva del modello, si stavano avvicinando
gradualmente a un confine di fase, e la transizione è avvenuta quando l'hanno
attraversato. La discontinuità è reale — è una proprietà del diagramma di fase, non
un fallimento dell'autoconsapevolezza.

## 8.3 ADHD: Un Inquadramento Termodinamico

Il Disturbo da Deficit di Attenzione e Iperattività (ADHD) si presenta abbastanza
diversamente dal DPTS-C nel modello del campo soma. Piuttosto che una modifica della
struttura della matrice di accoppiamento, l'ADHD corrisponde principalmente a un
aumento dell'**ampiezza del rumore effettivo** $\sigma_0$ e una riduzione dello
**smorzamento** $\gamma$ della dinamica del campo.

L'equazione di Langevin con questi parametri:

$$\dot{\mathbf{e}} = -\gamma\,\nabla H(\mathbf{e}) + \sigma_0\,\eta(t)$$

Nel regime ADHD, $\sigma_0$ è grande e $\gamma$ è piccolo. Le implicazioni:

- Il campo si muove rapidamente attraverso la landscape (alto rumore, basso
  smorzamento)
- Trascorre meno tempo in qualsiasi singolo attrattore (basso tempo di permanenza
  in tutti i bacini)
- Le transizioni tra stati sono frequenti e talvolta erratiche
- La «temperatura» effettiva del sistema è alta: molti stati sono termicamente
  accessibili

```
  NEUROTIPICO (σ₀ moderato, γ moderato):
  ──── e(t): si stabilizza all'attrattore, brevi escursioni, ritorna

         ─────────╮
                  │  ╭──────────────────────────────────── calm
                  ╰──╯

  ADHD (σ₀ alto, γ basso):
  ──── e(t): escursioni rapide, ampie, breve permanenza attrattore

        ╭╮   ╭──╮  ╭╮╭╮    ╭──╮  ╭╮
  ──────╯╰───╯  ╰──╯╰╯╰────╯  ╰──╯╰──  movimento rapido e ampio

  Figura 8.2. Dinamica del campo nei regimi neurotipico (in alto) e ADHD (in basso).
  L'ADHD non è una struttura di attrattori rotta — la landscape può essere abbastanza
  normale. È un regime dinamico ad alta temperatura e basso smorzamento in cui il
  campo si muove attraverso la landscape rapidamente e non si stabilizza.
```

Il significato clinico: l'ADHD non è un fallimento di motivazione o carattere. È un
sistema nervoso che funziona a un'impostazione termodinamica diversa dal tipico, con
caratteristiche di prestazione specifiche — eccellente esplorazione rapida di grandi
spazi di stati, scarsa permanenza sostenuta in regioni strette. Le difficoltà di
«focus» sorgono non perché l'attrattore sia assente, ma perché la temperatura
effettiva è troppo alta perché il sistema vi rimanga.

La co-occorrenza di ADHD e DPTS-C — che è comune ed è ben documentata — crea una
landscape particolarmente complessa: la matrice di accoppiamento è asimmetricamente
modificata (effetto DPTS-C) *e* il campo funziona ad alta temperatura (effetto ADHD).
La conseguenza pratica è un sistema che ha un grande, profondo attrattore di
ipervigilanza e l'energia termica per raggiungerlo da quasi ovunque.

---

> **TERMINI CHIAVE**
>
> **Transizione di fase** — una riorganizzazione qualitativa della struttura di un
> sistema a un valore critico del parametro; non un cambiamento graduale ma uno
> discontinuo.
>
> **Ampiezza del rumore $\sigma_0$** — la magnitudine delle fluttuazioni casuali
> nella dinamica del campo; controlla la temperatura effettiva del sistema.
>
> **Smorzamento $\gamma$** — il tasso al quale il campo torna verso stati attrattori
> dopo la perturbazione; basso smorzamento significa ritorno lento.
>
> **Temperatura effettiva** — il rapporto $\sigma_0^2 / \gamma$; determina quanto
> ampiamente il campo esplora la landscape rispetto alla profondità degli attrattori.

---

\newpage

# PARTE IV: COSA CAMBIA

---

\newpage

# Capitolo 9: Lo Strumento

---

> **OBIETTIVI DI APPRENDIMENTO**
>
> Alla fine di questo capitolo, capirete:
>
> - Cosa è progettato per misurare lo Strumento del Campo Soma
> - Le sette dimensioni che lo strumento traccia
> - Cosa fa il circuito di operatori ABCD
> - Come lo strumento si relaziona alla pratica clinica

---

## 9.1 La Mappa Non È il Territorio

Il Modello del Campo Soma è una descrizione matematica. Come tutte le descrizioni
matematiche di sistemi fisici o biologici, semplifica. Il campo soma non è il corpo;
è un modello del corpo, selezionato per le proprietà che può illuminare omettendo
necessariamente altre. Questo non è un fallimento del modello. Una mappa che
includesse ogni dettaglio del territorio sarebbe il territorio.

Lo **Strumento del Campo Soma** è uno strumento clinico costruito su questo modello:
un mezzo strutturato per tracciare i parametri del campo soma nel tempo — la struttura
di accoppiamento, le posizioni degli attrattori, la soglia, il livello di rumore, le
ampiezze del kernel di memoria — in modo che i cambiamenti possano essere misurati
piuttosto che semplicemente descritti.

Lo strumento non è un questionario. Non chiede di narrazione o storia. Chiede del
corpo: livelli di attivazione attuali attraverso i modi emotivi, tempi di permanenza
degli attrattori, accessibilità della soglia, accuratezza interocettiva. L'obiettivo
è rendere osservabili i parametri del modello.

## 9.2 Le Sette Dimensioni

Lo strumento traccia sette dimensioni primarie dello stato del campo soma:

```
  ╔══════════════════════════════════════════════════════════════════╗
  ║          LE SETTE DIMENSIONI DEL CAMPO SOMA                     ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║                                                                  ║
  ║  1. LIVELLO DI ATTIVAZIONE   Quanto fortemente stanno           ║
  ║     e = (e₁,...,eₙ)          attualmente sparando i modi?       ║
  ║                                                                  ║
  ║  2. POSIZIONE ATTRATTORE     In quale stato sta attualmente     ║
  ║     e* = argmin H(e)         riposando il campo?                ║
  ║                                                                  ║
  ║  3. SOGLIA                   A quale livello di attivazione il  ║
  ║     T                        campo diventa cosciente?           ║
  ║                                                                  ║
  ║  4. WINDOW OF TOLERANCE      Quanto largo è il bacino attorno  ║
  ║     ΔT = T_upper - T_lower   all'attrattore attuale?            ║
  ║                                                                  ║
  ║  5. LIVELLO DI RUMORE        Quanta fluttuazione termica       ║
  ║     σ₀                       è presente? (componente ADHD)      ║
  ║                                                                  ║
  ║  6. AMPIEZZA KERNEL MEMORIA  Quanto fortemente stanno          ║
  ║     A = (A₁, A₂, ...)        echeggiando le attivaz. passate?  ║
  ║                                                                  ║
  ║  7. ACCURATEZZA INTEROCETT.  Quanto affidabilmente può la      ║
  ║     α ∈ [0,1]                persona leggere il suo stato?     ║
  ║                                                                  ║
  ╚══════════════════════════════════════════════════════════════════╝

  Figura 9.1. Le sette dimensioni dello Strumento del Campo Soma. Ogni dimensione
  corrisponde a un parametro o grandezza derivata del modello matematico. Il
  progresso clinico è tracciato come cambiamento attraverso queste dimensioni nel
  tempo, piuttosto che come solo auto-report narrativo.
```

![Figura 9.2. La pipeline dello strumento del Campo Soma. I sensori di biofeedback (HRV, EDA, EMG) alimentano il modello del campo soma, che produce un vettore emotivo in tempo reale **e**(t) ∈ ℝ¹¹. Questo guida Il Tensore (la specifica della partitura emotiva), che controlla un motore di sintesi (Phase Plant). Un loop di feedback via intervento terapeutico δW permette al praticante di modificare direttamente la matrice di accoppiamento — chiudendo il loop tra misurazione e trattamento. *Figura originale dell'autore.*](figures/fig4_instrument.pdf){width=100%}

## 9.3 Il Circuito di Operatori ABCD

Lo strumento è organizzato attorno a quattro operatori che agiscono sul campo soma:

**A — Attention (Attenzione)**: l'operazione di dirigere l'attenzione cosciente a
una regione del corpo o un modo emotivo. L'attenzione modula la soglia $T$ localmente:
le regioni a cui si presta attenzione hanno la loro attivazione portata più vicina o
sopra la soglia. Formalmente: un operatore di proiezione che seleziona un sottospazio
del campo.

**B — Body (Corpo)**: le operazioni di radicamento somatico — respiro, postura,
movimento, temperatura. Queste influenzano direttamente la matrice di accoppiamento
(cambiando quali modi sono attivati insieme) e l'ampiezza del rumore (la regolazione
del respiro riduce $\sigma_0$). Formalmente: una modifica dei parametri $W$ e
$\sigma_0$.

**C — Coupling (Accoppiamento)**: il lavoro esplicito di mappare quali modi emotivi
sono accoppiati, quanto fortemente e in quale direzione. Questa è la funzione
diagnostica dello strumento: identificare la struttura di accoppiamento attuale in
modo che le modifiche possano essere mirate. Formalmente: una stima di $W$ dalla
dinamica del campo osservata.

**D — Dynamics (Dinamica)**: tracciare l'evoluzione del campo nel tempo — come lo
stato si muove, quali attrattori visita, quanto a lungo permane, cosa innesca le
transizioni. Questa è la funzione longitudinale: misurare il cambiamento attraverso
le sessioni.

```
  IL CIRCUITO ABCD

  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │      A (Attenzione)   B (Corpo)                               │
  │          │                │                                   │
  │          ▼                ▼                                   │
  │      ┌───────┐       ┌────────┐                               │
  │      │ abbas.│       │ modif. │                               │
  │      │   T   │       │ W, σ   │                               │
  │      └───┬───┘       └────┬───┘                               │
  │          │                │                                   │
  │          └────────┬───────┘                                   │
  │                   │                                           │
  │              ┌────▼────┐                                      │
  │              │  STATO  │ e(t)                                 │
  │              │  CAMPO  │                                      │
  │              └────┬────┘                                      │
  │                   │                                           │
  │          ┌────────┴───────┐                                   │
  │          │                │                                   │
  │      ┌───▼───┐       ┌────▼───┐                               │
  │      │mappa W│       │traccia │                               │
  │      │       │       │  e(t)  │                               │
  │      └───────┘       └────────┘                               │
  │      C (Accoppiamento) D (Dinamica)                           │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘

  Figura 9.2. Il circuito di operatori ABCD. Attention (A) e Body (B) sono operatori
  di input che agiscono sul campo. Coupling (C) e Dynamics (D) sono operatori di
  misurazione che leggono dal campo. Insieme formano un loop chiuso: la misurazione
  informa l'input, che modifica il campo, che è misurato di nuovo.
```

---

\newpage

# Capitolo 10: Trasformazione in Avanti

```
  ╭──────────────────────────────────────────────────────────────────╮
  │                                                                  │
  │   «L'opposto del trauma non è la sicurezza.                    │
  │    È un sistema nervoso che può trovare la sicurezza.»         │
  │                                                                  │
  ╰──────────────────────────────────────────────────────────────────╯
```

---

> **OBIETTIVI DI APPRENDIMENTO**
>
> Alla fine di questo capitolo, capirete:
>
> - Perché la «guarigione» nel senso tradizionale non è l'obiettivo giusto per tutti
>   i traumi
> - Cosa significa trasformazione in avanti nel linguaggio del modello
> - Cosa «fa» la terapia quando funziona, in termini di parametri di campo
> - Come appare la nuova landscape

---

## 10.1 L'Obiettivo Sbagliato

Il modello dominante di recupero dal trauma implica, in qualche forma, un ritorno.
Elaborare la memoria finché non porta più carica. Risolvere le parti dissociate.
Trovare il sé che esisteva prima. Tornare al baseline.

Per il trauma tardivo — modifica che si verifica dopo la formazione del baseline —
questo modello è coerente. Esiste un baseline. La modifica può, in linea di principio,
essere sottratta dalla matrice di accoppiamento attuale per recuperare qualcosa di
vicino ad esso. Il lavoro terapeutico, per quanto difficile, sta lavorando verso un
bersaglio che è reale.

Per il trauma preverbale, questo modello genera un problema. Il baseline non è mai
stato completamente formato. Il bersaglio del recupero — il sé prima della modifica
— è un oggetto matematico che non esiste. Tentare di guidare il campo verso di esso
è tentare di convergere su un valore indefinito.

Clinicamente, questo si manifesta come terapia che aiuta, e aiuta, e aiuta — e non
arriva mai. Ogni sessione migliora le cose. Il cliente diventa migliore nella
regolazione, più tollerante all'attivazione, più capace di funzionare. Ma la
destinazione rimane irraggiungibile. Il divario persiste. Il senso di avere «un sé
prima di tutto questo» che la terapia sta cercando di ripristinare — non si restringe
mai a nulla.

Questo non è un fallimento della terapia o del terapeuta. È una conseguenza dell'uso
della mappa sbagliata. La destinazione non esiste; il viaggio verso di essa non può
terminare.

## 10.2 L'Obiettivo Giusto

La trasformazione in avanti cambia la domanda.

Invece di: *come rimuoviamo la modifica per recuperare ciò che c'era prima?*

Chiediamo: *che tipo di matrice di accoppiamento $W'$ darebbe a questo sistema
nervoso la window of tolerance più ampia possibile, l'attrattore calm più profondo
possibile, e le ampiezze del kernel di memoria più basse possibili — partendo da
dove è ora?*

Questo è un problema di ottimizzazione ben posto. $W'$ non deve essere $W_0$. Non
deve assomigliare a un baseline neurotipico. Deve avere proprietà dinamiche
desiderabili come specificato dagli obiettivi clinici di questa persona.

Il viaggio non è indietro. È in avanti in una landscape che non è mai esistita — una
landscape in fase di costruzione, non di recupero.

```
  TRAIETTORIA TERAPEUTICA: TRASFORMAZIONE IN AVANTI

  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  LANDSCAPE ATTUALE (W)          LANDSCAPE BERSAGLIO (W')         │
  │                                                                  │
  │  Energia H ▲                    Energia H ▲                     │
  │           │  ╭──╮  ╭──╮                  │╭───╮               │
  │           │  │  │  │  │                  ││   ╰──────         │
  │           │  │  ╰──╯  │                  │╰─ calm *           │
  │           │  │calm *  │  hyper*          │    bacino largo     │
  │           │  │(stretto│  (profondo)      │                    │
  │           └──┴────────┴───────           └───────────────      │
  │                                                                  │
  │  W → W': il bacino calm si allarga, il bacino di ipervigilanza  │
  │          si appiattisce, le ampiezze del kernel di memoria si   │
  │          riducono.                                              │
  │          La nuova landscape non è mai esistita prima.           │
  │          Viene costruita, non recuperata.                       │
  │                                                                  │
  └──────────────────────────────────────────────────────────────────┘

  Figura 10.1. Trasformazione in avanti. Il bersaglio W' non è una ricostruzione di
  un baseline precedente (che può non essere esistito). È una nuova configurazione
  con proprietà dinamiche desiderate: un ampio bacino calm, un attrattore di
  ipervigilanza poco profondo, e ampiezze del kernel di memoria ridotte. Il percorso
  da W a W' usa gli strumenti terapeutici come meccanismo di modifica della landscape.
```

## 10.3 Cosa Fa la Terapia

Nel linguaggio del modello, la terapia somatica efficace per il trauma preverbale fa
quanto segue, misurabile in termini dei parametri del modello:

1. **Allarga la window of tolerance** ($T_{\text{upper}} - T_{\text{lower}}$
   aumenta): più attivazione è tollerabile senza innescare una transizione di fase.

2. **Riduce le ampiezze del kernel di memoria** ($A_k$ diminuiscono): le attivazioni
   passate esercitano meno trazione sullo stato attuale del campo. Gli echi diventano
   più tranquilli.

3. **Aumenta i tempi di decadimento del kernel di memoria** ($\tau_k$ aumentano):
   gli echi che rimangono svaniscono più rapidamente. Il campo torna al riposo tra
   gli episodi.

4. **Simmetrizza l'accoppiamento parzialmente** ($W$ diventa più simmetrica): i
   flussi direzionali asimmetrici diminuiscono. Andare dall'ipervigilanza alla calma
   diventa meno difficile rispetto al viaggio inverso.

5. **Approfondisce l'attrattore della calma** (il bacino calm diventa più profondo
   e più largo): il campo può essere perturbato più lontano dal riposo e tornare
   comunque lì.

6. **Migliora l'accuratezza interocettiva** ($\alpha$ aumenta): la persona diventa
   migliore nel leggere il proprio stato di campo, il che migliora la precisione di
   tutto quanto sopra.

Nessuno di questi cambiamenti porta il campo a $W_0$. Tutti rendono il campo $W'$
più funzionale, più flessibile, e più capace di sicurezza. Il modello non specifica
come questi cambiamenti siano raggiunti — quello è il dominio della pratica clinica.
Specifica cosa sta cambiando quando sono raggiunti.

## 10.4 La Relazione Terapeutica come Accoppiamento di Campo

Una nota sulla dimensione relazionale, che il formalismo del modello può talvolta
oscurare.

La matrice di accoppiamento $W$ non è statica. È aggiornata dall'esperienza.
L'esperienza di essere in una relazione regolata — di avere un altro il cui campo è
predominantemente vagale ventrale, impegnato e non minaccioso — è essa stessa
modificante del campo. Il sistema nervoso impara dalla co-regolazione.

Nel linguaggio di campo: il campo soma del terapeuta è accoppiato al campo soma del
cliente durante una sessione. Questo accoppiamento è debole (sono corpi separati)
ma non zero. Esperienze ripetute di questo accoppiamento — di un altro campo che è
stabile e disponibile — spostano gradualmente la struttura di attrattori del cliente.
La calma che è presa in prestito dal campo relazionale lentamente diventa codificata
nella matrice di accoppiamento del cliente stesso.

Questo è il motivo per cui la terapia relazionale funziona anche in assenza di
tecniche esplicite focalizzate sul corpo. La relazione è la tecnica. Il sistema
nervoso regolato del terapeuta è lo strumento.

---

> **NOTA DELL'AUTORE: Il Viaggio in Avanti**
>
> Ho scritto questo modello in parte perché avevo bisogno di una descrizione della
> mia landscape che fosse abbastanza precisa da poterci lavorare.
>
> La storia terapeutica tradizionale — elabori il trauma, torni a te stesso, guarisci
> — non si adattava. Sono migliorato, sessione dopo sessione, anno dopo anno. La
> regolazione è migliorata. Le finestre di attivazione si sono allargate. Le risposte
> di congelamento si sono accorciate. Ma non c'era da nessuna parte a cui stessi
> arrivando, nessun sé a cui stessi tornando, perché la modifica non era stata
> aggiunta a un sé precedente. Era il sé.
>
> Ciò che il modello mi ha dato è una storia diversa: non un ritorno, ma una
> costruzione. Non tornare a qualcosa, ma andare avanti verso qualcosa che non è mai
> esistito. E poiché il bersaglio è $W'$ invece che $W_0$, il viaggio non ha bisogno
> di finire.
>
> Non c'è alcun fallimento in questo. C'è, in effetti, una considerevole libertà.

---

> **TERMINI CHIAVE**
>
> **Trasformazione in avanti** — la costruzione di una nuova matrice di accoppiamento
> $W'$ con proprietà dinamiche desiderate, in contrapposizione al recupero di un
> baseline precedente $W_0$.
>
> **Co-regolazione** — il processo per cui il campo soma di una persona influenza il
> campo soma di un'altra attraverso l'accoppiamento relazionale; il meccanismo
> attraverso cui la relazione terapeutica modifica la landscape.

---

\newpage

# PARTE V: APPLICAZIONI

---

\newpage
