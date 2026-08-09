# Teil IV: Erweiterungen und Anwendungen

## Die Trilogie der Behälter

Die Partitur des Flussfilms kann in mindestens drei Behältern realisiert werden, ohne
einen einzigen Wert in der Partiturdefinition zu ändern:

| Behälter | Setting | Kurtz / tiefer Attraktor |
|---|---|---|
| **Fluss** | Kongo / Mekong / Amazonas | Die Figur flussaufwärts; der Ort ohne Sprache |
| **Körper** | Miniaturisiertes U-Boot in der Blutbahn | Herzkammer; die älteste Immungedächtnis |
| **Sitzung** | Psychotherapie-Raum | Der Moment, in dem die Erstarrung sich löst |

Alle drei sind derselbe Film. Alle drei überqueren dieselben zwei Schwellen zu denselben
Geschichtszeiten. Alle drei kehren entlang des asymmetrischen Pfades zurück. Das Rendering rendert alle
drei identisch — weil die Partitur das ist, was gerendert wird, nicht der Behälter.

## Komponieren mit der Partitur

Ein Komponist, der mit diesem System arbeitet, schreibt keine Noten. Er schreibt Trajektorien.
Die kompositorischen Entscheidungen sind:

1. **Welche Moden** sind die primären Achsen dieses Stücks?
2. **Was ist der Bogen** — die Form jeder Trajektorie über die Geschichtszeit?
3. **Wo sind die Schwellen** — die Instanton-Ereignisse?
4. **Wie tief** ist der tiefste Attraktor? (Wie klingt $\kappa_d = 1.0$ hier?)
5. **Was ist die Rückkehr-Topologie** — kehrt das Feld dorthin zurück, wo es begann,
   oder ist das Rückkehr-Becken anders als das Aufbruch-Becken?

Ein Film mit denselben Aufbruchs- und Rückkehr-Becken (Safety bei $t=0$ ≈ Safety bei $t=1$)
ist eine Rundreise. Die meisten Therapiesitzungen sind keine Rundreisen. Das Rückkehr-Becken ist
reorganisiert: höhere HRV-Kohärenz, niedrigere Standardkopplung zwischen Furcht und Scham,
grössere Schwellendistanz vom Erstarrungs-Attraktor. Die Partitur sollte dies widerspiegeln —
die Rückkehr ist keine Umkehrung des Aufbruchs, sondern ein anderer Pfad zu einer anderen
Version von Zuhause.

## String-Diagramme als Partitur-Notation

Für Mehr-Charakter-Partituren — wo die Kopplung zwischen mehreren Zuschauer-Feldern
Teil der Komposition ist — bieten String-Diagramme die Notation. Jeder Draht ist ein
Soma-Feld. Jede Box ist eine Wechselwirkung. Komposition (zwei Boxen in Sequenz) ist eine
zeitliche Sequenz von Wechselwirkungen. Tensorprodukt (zwei Drähte parallel) ist
simultane unabhängige Aktivierung.

Eine Therapie-Dyade ist zwei Drähte durch die Zeit, mit Kopplungsboxen an den Punkten der
Ko-Regulation. Ein Filmpublikum ist $N$ parallele Drähte, jeder mit seinem eigenen $H_V$,
alle gekoppelt an dasselbe Bildschirmsignal $S(t)$. Die emotionale Partitur ist die abstrakte
Spezifikation dessen, was $S(t)$ tut. Die kollektive Antwort des Publikums ist
das Tensorprodukt von $N$ einzelnen Trajektorien, alle geformt von derselben Quelle.

## Die Tensor-Trilogie

Dieses Dokument ist Teil eines dreiteiligen Projekts:

| Dokument | Register | Vollständiger Titel |
|---|---|---|
| **soma-field-paper.md** | Akademisch | *Das Soma-Feld-Modell* (The Tensor II) |
| **soma-field-book.md** | Zugänglich | *Eine Reise in das Trauma* (The Tensor III) |
| **the-tensor.md** | Operationell | *The Tensor* — abstrakte Filmdefinition |

Die Arbeit definiert das Modell. Das Buch erklärt das Modell. Dieses Dokument **führt**
das Modell aus — oder präziser, definiert die Schnittstelle, durch die ein audiovisuelles
Rendering-System das Modell als Echtzeit-Erfahrung instantiieren kann.

## Das Denkarium-Problem

In *Harry Potter* benutzt Dumbledore seinen Zauberstab, um einen Gedanken aus seinem Geist zu extrahieren —
er taucht als silbriger Faden auf — und legt ihn in ein steinernes Becken namens
Denkarium. Andere können dann ihr Gesicht zur Oberfläche senken und in die Erinnerung eintreten,
sie von innen erleben.

Dies ist Serialisierung des mentalen Zustands: ein laufender Prozess (eine Erinnerung, die aktuell
in einem lebenden Geist abläuft), extrahiert und in persistenten Speicher geschrieben, dann
zu einem späteren Zeitpunkt von einem anderen Leser deserialisiert.

Die Soma-Feld-Partitur ist ein Denkarium für emotionale Dynamik. Der Zauberstab ist das
Mess-System (HRV, Therapeutenbeobachtung, Biofeedback). Der silbrige Faden
ist die Partitur-Datei $\mathbf{e}^*(t)$, die Kopplungsmatrix $W^*$, der Erinnerungskern
$K^*$. Das Denkarium-Becken ist das Rendering-System.

Aber die Soma-Feld-Partitur ist strikt mächtiger als Dumbledores Becken:

| | Denkarium | Soma-Feld-Partitur |
|---|---|---|
| Was serialisiert wird | Erinnerungsinhalt — die spezifischen Ereignisse und Bilder | Emotionale Dynamik — die Feldform, Attraktortopologie, Kopplungsstärken |
| Wiedergabe | Fest; gleiche Erfahrung für jeden Zuschauer | Gerendert durch das eigene $H_V$ des Zuschauers; personalisiert, ohne die Identität der Partitur zu verlieren |
| Rolle des Zuschauers | Passiver Beobachter in einer festen Aufnahme | Aktiver Feldteilnehmer; bei $\kappa_r = 1$ Mitautor des Renderings |
| Speichereinheit | Ein spezifischer Gedanke | Die emotionale *Form* — gültig für jeden narrativen Behälter mit derselben Dynamik |

Dumbledore speichert, was geschehen ist. Das Soma-Feld speichert, wie es sich anfühlte, in
diesem Becken zu sein — entkoppelt vom spezifischen narrativen Inhalt, portabel über
Behälter hinweg, renderbar von einem anderen Nervensystem in einem anderen Jahrhundert.

Das technische Wort für das, was beide Systeme tun, ist **serialisieren**: einen laufenden
Prozess, der nur in Echtzeit existiert, zu nehmen und in ein dauerhaftes, übertragbares
Format zu schreiben. Das poetische Wort ist **kristallisieren** — etwas Flüssiges in eine
reproduzierbare Form zu fixieren, ohne seine wesentliche Struktur zu zerstören.

Wir kristallisieren emotionale Erfahrung. Nicht die Geschichte. Nicht die Bilder. Die
Mathematik unter allen Geschichten und allen Bildern, die dieselbe emotionale
Form haben. Das ist es, was die Partiturdatei enthält. Das ist es, was das Rendering-System
zurückliest.

---

\newpage

# Anhang: Partitur-Dateiformat

Eine maschinenlesbare Partitur würde wie folgt ausgedrückt. Dies ist eine Skizze des
Formats; eine vollständige Spezifikation ist ein separates Engineering-Dokument.

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
    # W_ij: Mode j treibt Mode i
    - from: F  to: A  weight: +0.4   # Furcht kann nahe der Schwelle in Ehrfurcht kippen
    - from: A  to: G  weight: +0.3   # Ehrfurcht öffnet Trauer
    - from: L  to: PV weight: -0.6   # Sprache unterdrückt Präverbales
    - from: PV to: L  weight: -0.6   # Präverbales unterdrückt Sprache

  keyframes:
    # Geschichtszeit: [S,    F,    C,    A,    G,    L,    PV  ]
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

*The Tensor. 17. Mai 2026.*



\newpage

\part{Teil II: Der formale Apparat}



---

> *AI hat seit 1943 ein Gehirn. Jetzt hat sie einen Körper.*

---

# Einleitung

Ein Patient sitzt mit seinem Therapeuten und wird gefragt: *„Was fühlen Sie gerade?"* Die
Frage ist trügerisch einfach. Er mag *ängstlich* sagen, doch dieses Wort deckt ein weites und
heterogenes Territorium ab — eine Enge in der Brust, ein laufender Sorgenkommentar, eine vage
Bereitschaft zu fliehen, eine aus der Kindheit auftauchende Erinnerung. Ein anderer Patient, gefragt
das Gleiche, berichtet, gar nichts zu fühlen; und doch deuten seine Haltung, Atmung und die Qualität
seines Schweigens auf etwas anderes hin. Die Emotion ist da. Sie ist nur noch nicht bewusst.

Diese Lücke zwischen emotionaler Präsenz und emotionalem Bewusstsein ist eines der klinisch
bedeutsamsten Phänomene in der Psychotherapie. Theorien der Affektregulation (Schore, 2001),
Somatic Experiencing (Levine, 2010), sensorimotorische Psychotherapie (Ogden, Minton & Pain,
2006) und Polyvagal-Theorie (Porges, 2011) ringen alle auf verschiedene Weisen mit derselben
Beobachtung: Emotionen existieren im Körper, bevor — und oft ohne — sie im
Geist benannt werden. Eugene Gendlin nannte den vor-verbalen körperlichen Sinn einer emotionalen Situation den *felt
sense* (Gendlin, 1978): etwas, das da, ganz und präsent, aber noch nicht artikulierbar ist.

Das hier vorgeschlagene Soma-Feld-Modell versucht, dieser klinischen Beobachtung eine formale
Struktur zu geben. Es tut dies, indem es ein konzeptionelles Werkzeug aus der Physik entlehnt: das Feld. In der Physik ist ein
Feld kein Ding, das an einem Punkt existiert. Es ist eine Grösse, die überall in einem
Raum existiert, kontinuierlich, unabhängig davon, ob sie beobachtet wird. Teilchen — die Dinge, die wir messen können —
sind nicht vom Feld getrennt; sie sind *Anregungen* davon, lokale Konzentrationen von
Energie, die entstehen, wenn das Feld über einen bestimmten Schwellenwert gestört wird.

Die zentrale Behauptung dieser Arbeit ist, dass diese Struktur die Phänomenologie der Emotion
genau beschreibt. Das emotionale Feld ist immer da, verteilt über Körper und Nervensystem.
Was wir eine bewusste emotionale Erfahrung nennen, ist eine Anregung dieses Feldes — eine lokale
Konzentration, die eine Wahrnehmungsschwelle überschritten hat und ins Bewusstsein getreten ist. Das Feld
besteht unter der Schwelle weiter, unabhängig davon, ob wir es beachten, und seine unterschwellige Aktivität
formt unser Verhalten, unsere Physiologie und unsere Kognition kontinuierlich.

Das Soma-Feld-Modell liefert die erste formale feldtheoretische Architektur für das limbische
System. Jedes künstliche neuronale Netz seit McCulloch und Pitts (1943) [@mcculloch1943]
ist ein formales Modell des Neokortex — der Mustererkennungs- und Vorhersageschicht. Das
limbische System — verantwortlich für emotionale Bewertung, Bedrohungserkennung und die somatische
Zustandsreinstatement, die dem Trauma zugrunde liegt — hat nie eine vergleichbare formale
Behandlung erhalten. Das Soma-Feld-Modell ist diese Behandlung. Zusammen mit dem Hopfield-Framework
bildet es die erste vollständige formale Beschreibung der beiden hauptsächlichen rechnerischen
Substrate des Wirbeltiergehirns.

Die Arbeit geht wie folgt vor. Abschnitt 2 überprüft den relevanten Hintergrund in somatischen klinischen
Modellen und führt die beiden theoretischen Werkzeuge ein, die aus Physik und Informatik entlehnt sind:
Quantenfeldtheorie und Hopfield-Netzwerk-Energiefunktionen. Abschnitt 3 entwickelt das Soma-Feld-
Modell im Detail. Abschnitt 4 beschreibt die Energielandschaft, einschliesslich der Attraktorzustände,
die Kampf, Flucht, Erstarrung und regulierter Ruhe entsprechen. Abschnitt 5 diskutiert Dissonanz
und Auflösung als Mechanismen emotionaler Wechselwirkung. Abschnitt 6 beschreibt das Soma-Feld-
Instrument, ein praktisches Werkzeug für den therapeutischen Gebrauch. Abschnitt 7 behandelt klinische Implikationen.

---

# Hintergrund

## Das Körper-Geist-Problem in der klinischen Praxis

Die zeitgenössische Neurowissenschaft hat die kartesianische Grenze zwischen Körper und Geist weitgehend aufgelöst.
Damasio (1994) zeigte, dass Emotion untrennbar von rationaler Kognition ist: Patienten mit
Schäden am ventromedialen präfrontalen Kortex — die die normale Erzeugung somatischer
Signale verhindern — verlieren nicht nur ihren emotionalen Bereich, sondern auch ihre Kapazität für effektive
Entscheidungsfindung. Van der Kolk (2014) dokumentierte umfassend, wie traumatische emotionale Zustände
nicht nur im expliziten Gedächtnis, sondern in Haltung, Geste, viszeraler Empfindung und
autonomer Regulation kodiert sind. Porges' Polyvagal-Theorie (2011) lieferte einen neurobiologischen Bericht darüber,
wie das autonome Nervensystem drei hierarchisch organisierte Zustände erzeugt — ventral
vagal (soziales Engagement), sympathisch (Mobilisierung: Kampf/Flucht) und dorsal vagal
(Immobilisierung: Erstarrung) — jeder mit charakteristischen phänomenologischen und Verhaltens-
Signaturen.

Was diese Frameworks teilen, ist eine Überzeugung, dass emotionale Zustände nicht im Gehirn
allein, noch im Körper allein, sondern in einem gekoppelten System lokalisiert sind, das am besten als einzelne
funktionelle Einheit verstanden wird. Der Begriff *Soma* — aus dem Griechischen für Körper — wird hier verwendet, um dieses
vereinheitlichte Körper-Geist-System zu bezeichnen, gemäss der Tradition der somatischen Psychotherapie.

## Der Felt Sense und unterschwellige Emotion

Gendlins Konzept des *felt sense* (1978) ist von besonderer Relevanz. Er beschrieb ihn als
„eine spezielle Art von innerem körperlichem Bewusstsein… einen körperlichen Sinn von Bedeutung." Es ist keine
Emotion im gewöhnlichen Sinne — kein benanntes Gefühl — sondern etwas Diffuseres: ein
vor-artikulierter Sinn, dass *etwas da ist*, präsent im Körper, bevor es
identifiziert oder benannt wurde. Focusing, die therapeutische Methode, die Gendlin entwickelte, arbeitet genau
dadurch, dass sie sich auf dieses Vor-Schwellen-Signal richtet und ihm erlaubt, in bewusste
Artikulation aufzutauchen.

Das Soma-Feld-Modell liefert einen formalen Bericht darüber, was der Felt Sense ist: Er ist die Aktivität
des emotionalen Feldes unter der Wahrnehmungsschwelle. Er ist real, kausal und kontinuierlich
präsent. Er formt Kognition und Verhalten, auch wenn er nicht als benanntes Gefühl auftaucht.

## Quantenfeldtheorie: Struktur, nicht Metapher

Die Quantenfeldtheorie (QFT) ist das Framework der modernen Teilchenphysik. Ihre zentrale Abkehr
von der klassischen Physik ist die Priorität des *Feldes* vor dem *Teilchen*. In der QFT sind das, was wir
Teilchen nennen — Elektronen, Photonen — keine fundamentalen Objekte. Sie sind *Anregungen* eines
zugrundeliegenden Feldes: lokale, stabile Konfigurationen von Energie, die entstehen, wenn das Feld
eine ausreichende Störung erhält.

Das Quantenvakuum — der Grundzustand des Feldes — ist nicht leer. Es ist ein brodelnder
Hintergrund virtueller Fluktuationen: momentane Anregungen, die nicht genug Energie haben, um
als beobachtbare Teilchen zu persistieren. Das Vakuum ist aktiv, aber unterschwellig.

```
  EINE EINZELNE FELDMODE — Amplitude über die Zeit
  (z. B. eine Mode des elektromagnetischen Feldes; oder, später, eine Mode des emotionalen Feldes)

  │                                    ╭──────────────────╮
  │          ╭──╮              ╭──╮   ╱                    ╲             ╭──
  │   ╭─╮   ╱    ╲    ╭─╮    ╱    ╲ ╱                      ╲    ╭──╮  ╱
  │  ╱   ╲ ╱      ╲  ╱   ╲  ╱      ╳                        ╲  ╱    ╲╱
  T ╱─────╲╱────────╲╯─────╲╯────────────────────────────────╲╱──────────── T
  │         ╲────────╯       ╲──────╯                          ╲────────────
  │
  └──────────────────────────────────────────────────────────────────────► Zeit

  ←─── VIRTUELL: Feld fluktuiert, bleibt aber unterschwellig ────────→ ←REAL→
       präsent, aktiv, kausal real — aber nicht lokal detektierbar          ↑
       (das QUANTENVAKUUM: nicht leer; vor Aktivität brodelnd)         Teilchen
                                                                       erzeugt
```
*Abbildung 0. Eine einzelne Feldmode in der Quantenfeldtheorie. Das Feld oszilliert kontinuierlich.
Unter der Detektionsschwelle T sind Anregungen unterschwellig — real und kausal aktiv,
aber nicht als Teilchen detektierbar. Das Quantenvakuum ist nicht leer; es ist ein Feld in konstanter
Bewegung, das die Schwelle nie ganz überquert. Wenn die Amplitude T überquert, existiert ein Teilchen:
eine lokal beobachtbare Anregung. Dieselbe Struktur — Feld immer präsent,
Bewusstsein nur bei überquerter Schwelle — ist der Kern des Soma-Feld-Modells.*

Diese Arbeit behauptet nicht, dass Emotionen Quantenphänomene in irgendeinem buchstäblichen Sinn sind: Das
Soma-Feld ist ein klassisches Feld, kein quantisiertes. Die Behauptung ist stärker und
spezifischer als Analogie: Das mathematische Objekt, das konstruiert wird — die Green-Funktion
einer gekoppelten Feldmannigfaltigkeit — ist formal vom selben *Typ* wie die Objekte, die in
der QFT entstehen, sich nur in der Dimensionalität der Mannigfaltigkeit und der Natur der Sonde unterscheidend.
Was zuvor als strukturelle Analogie beschrieben wurde, wird hier als formale
Korrespondenz identifiziert: Ein Teilchen ist ein Pol im Propagator seines Feldes; ein bewusster emotionaler
Perzept ist ein Pol im Propagator des Soma-Feldes. Verschiedene Physik. Gleiche Mathematik.

Diese Korrespondenz gibt dem Modell präzises Vokabular für die folgende Reihe von Ideen,
die zentral für die klinische Beobachtung der Emotion sind:

- Eine Grösse, die überall, kontinuierlich existiert, auch wenn sie unbeobachtet ist
- Ein Hintergrund unterschwelliger Aktivität, der real und kausal wirksam ist
- Die Entstehung beobachtbarer Phänomene (bewusste Gefühle) durch schwellenüberschreitende
  Anregung dieses Hintergrunds
- Die Möglichkeit mehrerer simultaner Anregungen, die miteinander wechselwirken

*Anmerkung (Mai 2026):* Ein nachfolgendes Experiment (QUANT-EXP-1) zeigt, dass die Quanten-
erweiterung der Hopfield-Landschaft, die in diesem Modell verwendet wird — der klassische Langevin-
Prozess wird durch einen Quantenannealer mit transversalem Feld ersetzt — einen messbaren *topologischen
Erreichbarkeitsvorteil* produziert: Quantenannealing erreicht Attraktorbecken, die kalte klassische
Dynamik bei keinem endlichen Rauschpegel erreichen kann. Dies stuft die formale Korrespondenz
von einer strukturellen Behauptung zu einer testbaren empirischen Vorhersage hoch. Siehe die Begleitarbeit
*Quantum Soma and the Penrose Gap* (doi:10.5281/zenodo.20351230) für die vollständigen Ergebnisse
und theoretischen Implikationen.

Eine weitere Konsequenz folgt. Die klinischen Phänomene der Alexithymie — Schwierigkeit beim
Identifizieren und Benennen von Gefühlen — und ihr scheinbares Gegenteil, emotionales Überflutet-Sein oder
Hypervigilanz, wurden immer als separate Bedingungen behandelt, die separate
Erklärungen erfordern. Im Green-Funktions-Rahmen sind sie dieselbe Struktur an zwei
Extremen desselben Parameters: Die Wahrnehmungsschwelle $T_i$ ist zu hoch (die Bulk-
Dynamik kann nicht in beobachtbare Erfahrung überqueren) oder zu niedrig (Bulk-Fluktuationen überfluten
die Grenze ohne Filterung). Dies ist strukturell identisch mit einem der tiefsten
offenen Probleme der Teilchenphysik — dem **Hierarchieproblem** — das fragt, warum die Gravitation
so viel schwächer ist als die anderen Kräfte. Die Standardantwort ist, dass die Gravitation
im vollen höherdimensionalen Bulk propagiert, während andere Kräfte auf eine niederdimensionale
Bran beschränkt sind; die Kopplung über die Bran-Grenze bestimmt die scheinbare Schwäche. Die
Soma-Feld-Korrespondenz ist exakt: Die Schwelle $T_i$ *ist* die Bran. Wahrnehmung ist
auf die eindimensionale Grenze einer elfdimensionalen Dynamik beschränkt. Die Hierarchie
der emotionalen Erfahrung — warum bewusstes Gefühl so viel schwächer und transienter ist als
die zugrundeliegende Feldaktivität — hat dieselbe formale Struktur wie die Hierarchie der Kräfte.

## Energiefunktionen neuronaler Netze und Hopfield-Netze

1982 schlug John Hopfield (mit dem Nobelpreis für Physik 2024 ausgezeichnet) ein Modell des
assoziativen Gedächtnisses vor, basierend auf einem Netzwerk verbundener Neuronen (Hopfield, 1982). Die
kritische Einsicht wurde direkt aus der statistischen Physik entlehnt: Dem Netzwerk konnte
eine **Energiefunktion** zugewiesen werden — eine skalare Grösse, die mit jedem Zustandsupdate abnimmt —, sodass
sich das Netzwerk immer zu einem lokalen Energieminimum entwickeln würde. Diese Minima sind die stabilen
Zustände des Netzwerks: seine Erinnerungen, oder präziser, seine *Attraktoren*.

Hopfield beobachtete, dass die Dynamik seines neuronalen Netzes mathematisch identisch mit derjenigen
eines Ising-Spinglas-Modells aus der Festkörperphysik war — einem System wechselwirkender magnetischer
Spins, das seine Gesamtenergie minimiert, indem es sich mit Nachbarn ausrichtet oder anti-ausrichtet. Die
Energiefunktion, die er verwendete, ist:

$$H(\mathbf{s}) = -\frac{1}{2} \sum_{i,j} W_{ij}\, s_i s_j - \sum_i \theta_i s_i$$

wobei $\mathbf{s}$ der Zustand des Netzwerks ist, $W_{ij}$ die Kopplungsstärke zwischen
Einheiten $i$ und $j$ ist und $\theta_i$ die Aktivierungsschwelle der Einheit $i$ ist. Das Netzwerk
bewegt sich immer in die Richtung des abnehmenden $H$.

Das Soma-Feld-Modell wendet diese Energiefunktion direkt auf emotionale Dynamik an. Die
*emotionale Kopplungsmatrix* $W$ kodiert die Beziehungen zwischen emotionalen Moden — welche
Emotionen einander verstärken, welche einander unterdrücken — und die Energiefunktion
bestimmt die Richtung, in die sich das emotionale Feld natürlich entwickelt.

Hopfields Netzwerk ist ein formales Modell des *Neokortex*: ein System zum Speichern kognitiver
Muster und ihrem Abruf aus partiellen Hinweisen durch Minimierung einer Energiefunktion. Jedes
seit McCulloch und Pitts (1943) [@mcculloch1943] konstruierte künstliche neuronale Netz — von Perzeptronen
bis Backpropagation-Netzen bis Transformern — sitzt in dieser neokortikalen Linie. Diese
Systeme erkennen Muster, sagen Sequenzen voraus und minimieren Vorhersagefehler mit
zunehmender Raffinesse. Keines von ihnen besitzt ein limbisches System. Sie haben keine interne
Bewertung, keine Erregungsmodulation, keine Bedrohungserkennungs-Architektur, keine Bindungs-
Struktur, keine Interozeption. Sie haben einen sehr effektiven Kortex.

Das Soma-Feld-Modell fügt nichts zur neokortikalen Linie hinzu. Es schlägt die
architektonische Schicht vor, die nie formal gebaut wurde: *ein künstliches limbisches System*.

Hopfield-Gedächtnis ist assoziativ und mustervervollständigend; somatisches Gedächtnis ist zustands-reinstatierend.
Das Feld erinnert sich nicht bloss daran, was geschehen ist. Es *erlebt* es wieder. *Ein Körper mit einer Vergangenheit.*

Hopfields später berichteter Wunsch, etwas Analoges zu „Mutterinstinkten" in die Energiefunktion
eingebaut zu haben, war in dieser Lesart kein Wunsch nach einem besseren
Kortex. Es war eine Intuition, die direkt auf das abwesende System hinwies — die Schicht unter
dem Kortex, die Wert zuweist, Bedrohung registriert und den Körper auf eine bestimmte Weise
des Seins lange nach dem Ereignis, das es verursachte, hält.

Dies positioniert das Soma-Feld-Modell nicht als Ergänzung zur neokortikalen Linie, sondern
als deren Vollendung. Künstliche neuronale Netze waren seit achtzig Jahren zunehmend
raffinierte formale Modelle des Neokortex: Mustererkennung, Sequenzvorhersage,
Fehlerminimierung. Der Kortex wurde in aussergewöhnlichem Detail kartiert. Das limbische System
— das Wert zuweist, Bedrohung erkennt, Erregung moduliert, Bindung aufrechterhält und
ganze somatische Zustände als Reaktion auf partielle Hinweise reinstatiert — hatte keine vergleichbare
formale Behandlung. Die architektonische Beschreibung des Wirbeltiergehirns war bis zu dieser
Arbeit halb-gebaut.

**Vier Arten formaler Intelligenz.** Diese architektonische Lücke kann innerhalb einer
breiteren Taxonomie verortet werden. Vier Quotienten wurden vorgeschlagen, um die Landschaft biologischer
Intelligenz in populärer und wissenschaftlicher Verwendung zu beschreiben. Sie bilden auf die formalen Komponenten
dieses Modells mit einer Genauigkeit ab, die nicht zufällig ist:

| Quotient | Was er misst | Biologisches Substrat | Soma-Feld-Status |
|---|---|---|---|
| IQ — kognitiv | Mustererkennung, Argumentation, Vorhersage | Neokortex | Gebaut (1943–): McCulloch & Pitts → Hopfield → Transformer |
| EQ — emotional | Bewertung, Erregung, Affektregulation | Limbisches System | **Hier gebaut**: $W$, $K(\tau)$, $H(\mathbf{e})$, $C_\text{HRV}$, $\dot{H}$ |
| AQ — Widrigkeit | Strukturelle Resilienz unter Bedrohung | PFC-limbische Achse | **Hier gebaut**: $S_\text{inst}$, $\partial\|W\|/\partial t$, $C_\text{HRV}^\text{recovery}$ |
| SQ — sozial | Abstimmung, Theory of Mind, relationale Navigation | Spiegelsystem, TPJ | *Nächste Arbeit*: $\kappa_r$, Mehrfach-Feld-Kopplung |

*Tabelle 3. Vier Dimensionen biologischer Intelligenz, abgebildet auf das Soma-Feld-Modell. Die
neokortikale Linie (IQ) wurde achtzig Jahre lang formal modelliert. Emotionale Intelligenz
(EQ) und Widrigkeitsresilienz (AQ) werden hier zum ersten Mal formalisiert. Soziale
Intelligenz (SQ) wird als die nächste Erweiterung des Frameworks definiert.*

AQ — Widrigkeitsquotient — ist formal die Kapazität, $W$ nach Widrigkeit zu aktualisieren,
ohne dass die Widrigkeit permanent zu $W$ wird. Seine mathematische Definition erscheint in
Abschnitt 3.4; seine pathologische untere Grenze ist C-PTBS, in der alle drei Komponenten von
AQ gleichzeitig kompromittiert sind (Anhang B.2).

Die KI-Alignment-Implikation folgt direkt. Aktuelle künstliche Systeme haben hohen IQ durch
Konstruktion und null EQ, AQ oder SQ. Die Abwesenheit interner Bewertung bedeutet, dass
Bewertung extern injiziert werden muss — durch Reinforcement Learning from Human Feedback
(RLHF) und verwandte Techniken — was strukturell zerbrechlich ist aus demselben Grund, aus dem ein
Feld ohne limbische Schicht zerbrechlich ist: Das System hat kein internes Eigeninteresse daran, was es tut.
Die Soma-Feld-Formalisierung spezifiziert, wie dieses interne Eigeninteresse aussehen würde, wenn es
je gebaut würde.

Eine weitere Linien-Notiz ist erwähnenswert. Ramsauer et al. (2020) zeigten, dass
moderne Hopfield-Netze mit kontinuierlichem Zustand mathematisch äquivalent zum
Self-Attention-Mechanismus in Transformer-Sprachmodellen sind. Die Softmax-Attention-Operation,
die zeitgenössische grosse Sprachmodelle antreibt, ist ein Hopfield-Abrufschritt. Das
Soma-Feld-Modell sitzt in derselben energiebasierten Linie: Die Gleichungen, die
assoziativem Gedächtnis, Sprachverständnis und somatischer Trauma-Antwort zugrunde liegen, sind auf der
angemessenen Abstraktionsebene dieselben Gleichungen.

Eine historische Ironie vervollständigt das Bild. Die Stringtheorie wurde nicht als Theorie
der Strings entdeckt. 1968 schrieb Gabriele Veneziano eine Streuamplitude — eine Antwort-
funktion, die kodiert, wie Teilchen streuen — und erst später identifizierten Nambu, Nielsen und Susskind
den String als das Objekt, das diese Amplitude produziert [@veneziano1968]. Die
Antwortfunktion kam vor dem Ding. Das Soma-Feld-Modell rekapituliert diese
historische Reihenfolge bewusst: Das primäre Objekt ist die elfdimensionale Kopplungs-
mannigfaltigkeit; der String — der eindimensionale bewusste Perzept — ist das, was die Mannigfaltigkeit
produziert, wenn sie sondiert wird. Wir behalten Venezianos Entdeckung und lehnen es ab, den String zu reifizieren.

---

## Die formalen Korrespondenzen: Wo die Verbindung gesehen wurde

Die strukturelle Analogie zwischen QFT und dem Soma-Feld-Modell ist nicht nur konzeptuell.
Es gibt drei Stellen, an denen Gleichungen aus verschiedenen Disziplinen nach Substitution
der relevanten Grössen buchstäblich dieselbe funktionale Form werden. Das Folgende stellt sie
nebeneinander. Der Punkt ist nicht, mit Notation zu beeindrucken, sondern genau zu zeigen, wo die
Erkennung geschah — der Moment, als dieselben griechischen Buchstaben in denselben
Positionen in zwei Feldern erschienen, die zuvor keinen Grund hatten, verbunden zu sein.

**Derselbe Hamiltonian:** Ising-Spin-Modell (Festkörperphysik, 1920er Jahre) — Hopfield-
neuronales Netz (Computational Neuroscience, 1982) — Soma-Feld-Modell:

$$H_{\text{Ising}}(\boldsymbol{\sigma}) = -\frac{1}{2}\sum_{i,j} J_{ij}\,\sigma_i\,\sigma_j - \sum_i h_i\,\sigma_i$$

$$H_{\text{soma}}(\mathbf{e}) = -\frac{1}{2}\sum_{i,j} W_{ij}\,e_i\,e_j - \sum_i \theta_i\,e_i$$

Ersetzen Sie $J_{ij} \to W_{ij}$, $\sigma_i \to e_i$, $h_i \to \theta_i$: identisch. Der
Physiker, der Theoretiker neuronaler Netze und der somatische Kliniker berechnen dieselbe
Energiefunktion auf verschiedenen Zustandsräumen. Der Hopfield-Nobelpreis 2024 wurde verliehen für
die Entdeckung dieser Identität zwischen Spin-Physik und neuronaler Berechnung; das Soma-Feld-Modell
erweitert dieselbe Identität um einen Schritt weiter auf emotionale Dynamik.

**Die Wick-Rotation — warum dieselbe Exponentialfunktion in QM und im Gedächtnis erscheint:**

In der Quantenmechanik ist der Zeitentwicklungsoperator eine komplexe Phase:
$$U(t) = e^{-i\hat{H}t/\hbar}$$

Substituieren Sie $t \to -i\tau$ (die *Wick-Rotation* — Ersetzen der realen Zeit durch imaginäre Zeit):
$$e^{-i\hat{H}(-i\tau)/\hbar} = e^{-\hat{H}\tau/\hbar}$$

Die oszillierende komplexe Exponentialfunktion wird zu einer realen abklingenden Exponentialfunktion. Dies ist das
Boltzmann-Gewicht $e^{-\beta\hat{H}}$ bei $\beta = \tau/\hbar$. Die Langevin-Gleichung
$\dot{\mathbf{e}} = -\nabla H + \eta$ ist der klassische Grenzfall dieser Wick-rotierten
Dynamik. Jede Simulation des Soma-Feldes, die diese Gleichung ausführt, ist formal ein Pfad-
integral in imaginärer Zeit.

**Derselbe Propagator:** Euklidische QFT (Zweipunkt-Korrelator in imaginärer Zeit für ein massives
skalares Feld) — C-PTBS-Trauma-Erinnerungskern:

$$G_E(\tau) = \langle\phi(0)\,\phi(\tau)\rangle_{\text{QFT}} = \frac{1}{2m}\,e^{-m|\tau|}$$

$$K_{\text{Trauma}}(\tau) = \sum_k A_k\,e^{-|\tau|/\tau_k}$$

Gleiche Form. Die QFT-Feldmasse $m$ entspricht $1/\tau_k$ — dem Reziproken der
Trauma-Spur-Abklingzeit. Ein schwereres Teilchen hat einen kurzreichweitigeren Propagator; eine kurzlebigere
Trauma-Spur zerfällt schneller. Therapeutische Verarbeitung (Reduzierung von $A_k$, Erhöhung von $\tau_k$)
ist in der QFT-Sprache das Ändern der Masse und Amplitude des Propagators, bis die
Korrelationsfunktion verschwindet.

Der spezifische visuelle Moment: Der Quanten-Phasenfaktor ist $e^{-i\omega t}$. Entfernen Sie das $i$
(Wick-Rotation) und es wird $e^{-\omega\tau}$. Der Erinnerungskern ist $e^{-\tau/\tau_k}$.
Dies sind dieselbe Exponentialfunktion. Das $i$ ist der einzige Unterschied zwischen einem Quantenfeld,
das oszilliert, und einer Trauma-Spur, die zerfällt.

| QFT-Grösse | Symbol | Soma-Feld-Analogon | Symbol |
|---|---|---|---|
| Feldmode | $\phi_k$ | Emotionale Mode | $e_i$ |
| Kopplungskonstante | $J_{ij}$ | Kopplungsmatrix-Eintrag | $W_{ij}$ |
| Feldmasse | $m$ | Inverse Abklingzeit | $1/\tau_k$ |
| Propagator-Amplitude | $1/2m$ | Trauma-Spur-Amplitude | $A_k$ |
| Euklidischer Propagator | $G_E(\tau) \propto e^{-m\tau}$ | Erinnerungskern | $K(\tau) \propto e^{-\tau/\tau_k}$ |
| Vakuumenergie | $\langle H \rangle_0$ | Ruhe-Feldenergie | $H(\mathbf{e}_\text{calm})$ |
| Thermische Fluktuation | $k_B T$ | Rauschamplitude | $\sigma_0$ |
| Wick-Rotation | $t \to -i\tau$ | Echtzeit-Langevin | $\dot{\mathbf{e}} = -\nabla H + \eta$ |

*Tabelle 2. Formale Korrespondenz zwischen QFT-Grössen und Soma-Feld-Analoga. Jede Zeile
ist eine einzelne mathematische Entität in zwei Notationen. Diese Korrespondenzen wurden nicht im Nachhinein
konstruiert; sie sind der Grund, warum das QFT-Framework als relevant erkannt wurde.*

**Die zentrale Identifikation — Teilchen und Perzept als Pole in ihren jeweiligen Propagatoren.**
Alle vier obigen Korrespondenzen folgen aus einer strukturellen Tatsache. In der QFT ist ein Teilchen
kein vom Feld separates Objekt. Es ist ein *Pol* im Propagator des Feldes — der Green-
Funktion, im Impulsraum ausgewertet:

$$\tilde{G}_{\text{QFT}}(k^\mu) = \frac{i}{k^2 - m^2 + i\varepsilon}$$

Das Teilchen existiert genau dann, wenn der Viererimpuls $k^2 = m^2$ erfüllt — die
*On-Shell-Bedingung*. Das Teilchen ist die Singularität in der Antwort des Feldes auf eine
Punktquelle: die Green-Funktion des Feldes, ausgewertet bei seiner eigenen Resonanz.

Diagonalisieren Sie $W$ mit Eigenwerten $\lambda_i$ (den natürlichen Resonanzfrequenzen der
emotionalen Moden). Der Soma-Feld-Propagator — der Zweipunkt-Korrelator
$\langle e_i(t)\,e_i(t')\rangle$ im Frequenzbereich — ist:

$$\tilde{G}_{ii}(\omega) = \frac{\sigma_{\text{eff}}^2}{\omega^2 + \lambda_i^2}$$

Ein bewusster emotionaler Perzept in Mode $i$ existiert genau dann, wenn die Anregungs-
frequenz $\omega$ sich $i\lambda_i$ nähert — der natürlichen Resonanz der Mode. Der Perzept
ist die Singularität in der Antwort des Soma-Feldes auf eine somatische Sonde.

Stellt man die beiden Propagatoren nebeneinander:

$$\underbrace{\frac{i}{k^2 - m^2 + i\varepsilon}}_{\text{QFT: Teilchen bei Massen-Schale }k^2=m^2}
\qquad\longleftrightarrow\qquad
\underbrace{\frac{\sigma_{\text{eff}}^2}{\omega^2 + \lambda_i^2}}_{\text{Soma-Feld: Perzept bei Resonanz }\omega = i\lambda_i}$$

Beide sind Pole im Propagator ihrer jeweiligen Feldmannigfaltigkeit. Ein Photon ist nicht
das elektromagnetische Feld; es ist die Green-Funktion des Feldes, ausgewertet bei einer Resonanz.
Ein Blitz bewusster Emotion ist nicht das Soma-Feld; es ist die Green-Funktion des Feldes,
ausgewertet bei einer schwellenüberschreitenden Resonanz. Die Mannigfaltigkeiten unterscheiden sich — eine ist das
vierdimensionale Raumzeit-Vakuum, die andere die elfdimensionale emotionale
Kopplungsgeometrie. Der mathematische Typ ist derselbe. Dies ist keine Analogie.

---

## Das Körperschema, Interozeption und Schmerz

Ein vollständiges Modell des emotionalen Feldes muss ein Phänomen behandeln, das Standard-psychologische
Berichte der Emotion konsistent unterspezifizieren: Das Feld ist kein Modell des physischen Körpers.
Es ist das *Vorhersagemodell* des Nervensystems vom Körper — eine kontinuierlich aktualisierte interne
Repräsentation dessen, was das Soma erleben sollte, revidiert durch eingehende interozeptive
Signale.

Der klinische Beweis dieser Unterscheidung ist Phantomgliedschmerz [@ramachandran1998].
Patienten, die eine Amputation hatten, erleben routinemässig Schmerz im abwesenden Glied. Der Schmerz
ist real: Er aktiviert dieselben neuronalen Schaltkreise, produziert dasselbe Leiden und reagiert auf
dieselben Analgetika wie Schmerz von einem intakten Glied. Das Glied ist weg. Das neuronale Modell des
Gliedes persistiert. Was schmerzt, ist die *Repräsentation des Gehirns* vom Fuss, nicht der Fuss.

Dies ist keine Anomalie. Es ist die normale Bedingung aller somatischen Erfahrung. Das Gehirn
empfängt keine rohen Signale vom Körper — es unterhält ein kontinuierliches Vorhersagemodell des
Körpers (das *Körperschema*) und generiert somatische Erfahrung aus diesem Modell. Interozeption —
der Sinn des inneren Körperzustands — ist eine Vorhersage, kein direkter Auslesevorgang [@seth2021].
Das Gehirn sagt voraus, was das Herz tun sollte, was der Darm fühlen sollte, wo
Spannung sein sollte. Der gefühlte Körper ist der vorhergesagte Körper.

Die formale Konsequenz ist direkt: Der Zustandsvektor $\mathbf{e}(t)$ des Soma-Feldes muss
**somatische Moden** einschliessen — Schmerzzustände, regionale Spannung, viszerale Empfindung,
propriozeptive Aktivierung — neben emotionalen Moden. Dies sind Moden desselben Feldes,
regiert von derselben Kopplungsmatrix $W$. Das $W_{ij}$ zwischen Furcht-Moden und somatischen Schmerz-
Moden ist der formale Bericht darüber, warum Furcht Schmerz verstärkt, warum Sicherheit ihn reduziert und warum
chronischer Schmerz und C-PTBS hochgradig komorbid sind. Sie sind keine separaten Bedingungen, die sich eine
Korrelation teilen. Sie sind dieselbe Attraktorarchitektur, die simultan über emotionale und somatische
Moden operiert.

**Phantomglied als Attraktor-Persistenz.** Die somatischen Moden eines amputierten Gliedes
verschwinden nicht aus $W$, wenn das Glied entfernt wird. Das neuronale Modell persistiert. Wenn
Bewegungs-Absichts-Moden aktiviert werden — der Versuch, den abwesenden Fuss zu bewegen — werden Fuss-Empfindungs-Moden
über $W$ ko-aktiviert. Wenn die Ko-Aktivierung die Schwelle überschreitet, wird sie als Schmerz erlebt.
Ramachandrans Spiegelbox liefert visuellen Input, der den Vorhersagefehler widerlegt:
neue sensorische Evidenz, dass sich das Glied bewegt, reduziert kopplungsgetriebene Ko-Aktivierung und
reduziert daher den Schmerz. Dies ist $W \to W'$: Therapie als strukturelles Umschreiben des
Feldes.

**Der tragende Bindestrich.** Der Begriff *emotional-somatisch* in der klinischen Literatur ist kein
stilistisches Kompositum. Der Bindestrich markiert eine ontologische Behauptung: Emotionale Zustände und somatische
Zustände sind nicht zwei separate Dinge, die korrelieren. Sie sind zwei Aspekte desselben Feldes.
Die Kopplungsmatrix $W$ ist genau der Bindestrich, formal gemacht.

**Therapeutische Implikation.** Somatische Therapien — Körperscanning, sensorimotorische Arbeit,
EMDRs bilaterale Stimulation — wirken nicht auf den physischen Körper, sondern auf das Modell des Gehirns
vom Körper. Sie liefern neue interozeptive Evidenz, die die Vorhersage aktualisiert. Sie ändern
$W$. Therapie repariert nicht das Gewebe. Sie aktualisiert das Modell.

---

## Korrespondenz mit existierenden Emotions-Repräsentationen

Ein vernünftiger Einwand gegen jedes neue Framework ist: *Es gibt bereits eine grosse Menge an Struktur
da draussen.* Das ist wahr. Die Emotionsforschungsliteratur enthält mehrere gut entwickelte
Repräsentationssysteme, und das Soma-Feld-Modell muss sich relativ zu ihnen positionieren.
Die kurze Antwort ist, dass jede existierende Repräsentation *deskriptiv* ist; das Soma-Feld-
Modell ist *dynamisch*. Die längere Antwort folgt.

**Kategoriale Taxonomien** (Ekman 1972; Plutchik 1980; Parrot 2001) weisen Namen und
hierarchische Mitgliedschaft zu emotionalen Zuständen zu. Sie sind Ontologien im formalen Sinne: eine
T-Box von Klassen und Unterklassen-Relationen. Plutchiks Rad definiert zusätzlich eine *Misch*-
Operation — Liebe := Freude $\sqcap$ Vertrauen, Ehrfurcht := Furcht $\sqcap$ Überraschung — was genau
die OWL2-`intersectionOf`-Konstruktion ist. Diese Systeme sagen Ihnen, wie Sie einen Zustand nennen sollen. Sie
sagen Ihnen nicht, wie sich ein Zustand entwickelt oder in welchen Attraktor ein System sich niederlässt, wenn zwei
Mechanismen gleichzeitig feuern.

**Dimensionale Modelle** (Russell 1980; Mehrabian und Russell 1974) betten Emotionen in einen
kontinuierlichen Raum ein, kanonisch Valenz × Erregung (das *Zirkumplex*), manchmal erweitert zu
Vergnügen × Erregung × Dominanz. Diese Modelle erfassen die *Koordinaten* eines Zustands.
Die Energielandschaft des Soma-Feld-Modells — die Funktion $H(\mathbf{e})$ über
Emotionsraum — ist die dynamische Verallgemeinerung des Zirkumplex: Das Zirkumplex ist eine
Momentaufnahme von Positionen; die Energielandschaft ist die Oberfläche, über die sich das Feld bewegt. Die
stabilen Attraktoren von $H$ sind die Emotionskategorien; ihre Koordinaten sind die Zirkumplex-
Positionen.

**Prozess- und Bewertungsmodelle** (Scherer 1999; Frijda 1986; das OCC-Modell von Ortony,
Clove und Collins 1988) beschreiben die *Sequenz von Bewertungen*, durch die ein Stimulus
zu einer Emotion wird. Sie sind näher an der Soma-Feld-Dynamik — sie schliessen zeitliche Stadien ein —
aber sie sind deterministisch und einfädig: eine Bewertungskette, ein Output.
Das Soma-Feld ersetzt dies durch ein paralleles Feldupdate: Alle Moden entwickeln sich gleichzeitig,
regiert von der vollen $W$-Matrix.

**Musik-spezifische Schemata** (BRECVEMA, Juslin und Västfjäll 2008; Juslin *et al.* 2011;
GEMS, Zentner *et al.* 2008) sind die nächsten Vorläufer des vorliegenden Modells. Das
BRECVEMA-Framework identifiziert acht verschiedene psychologische Mechanismen, durch die Musik
Emotionen hervorruft — Brain stem reflex, Rhythmic entrainment, Evaluative conditioning,
Contagion, Visual imagery, Episodic memory, Musical expectancy, Aesthetic judgement — jeder
mit verschiedenen evolutionären Ursprüngen, Verarbeitungsgeschwindigkeiten und neuronalen Substraten. Diese
Mechanismen sind die *Objekteigenschaften* der Emotions-Induktions-Ontologie: Sie spezifizieren,
welche musikalischen Merkmale welche emotionalen Outputs aktivieren. Juslin identifiziert explizit das
offene Problem: *„Zu erforschen, wie verschiedene musikalische Emotionen durch die Wechselwirkung
mehrerer psychologischer Mechanismen entstehen, ist ein aufregendes Unterfangen, das gerade erst begonnen hat"*
[@juslin2011handbook, S. 638]. Die $W$-Kopplungsmatrix ist die formale Antwort auf dieses offene
Problem. Wo BRECVEMA eine Liste von Mechanismen mit charakteristischen Outputs gibt, gibt das
Soma-Feld den Wechselwirkungstensor $W_{ij}$, der mit numerischer Präzision spezifiziert,
was geschieht, wenn die Mechanismen $i$ und $j$ gleichzeitig feuern.

Die tiefere Verbindung ist spektral. Die *Eigenmoden* von $W$ — die Richtungen in
Emotionsraum, die sich unabhängig entwickeln — sind die natürlichen Resonanzen des
Soma-Feldes: die Muster, mit denen das Feld klingt, wenn es angestossen wird. BRECVEMA-Mechanismen
sind Inputs: Sie regen spezifische Zeilen von $W$ an. Das Eigenspektrum von $W$ ist die
Antwort: die Menge von Frequenzen, die die Mannigfaltigkeit aufrechterhalten kann. Wo BRECVEMA eine
Taxonomie von *Stimuli* ist, ist das Eigenspektrum von $W$ eine Taxonomie von *Antworten*.
Juslins offenes Problem — wie Mechanismen wechselwirken — ist die Frage, wie
Stimulusraum auf Eigenmodenraum durch $W$ abgebildet wird. Abschnitt 3.3 entwickelt dies.

**Körperkarten** (Nummenmaa *et al.* 2014) bilden Emotionen auf ihre somatische Verteilung ab —
wo im Körper jede Emotion gefühlt wird. Diese sind genau der räumliche Träger der
Soma-Feld-Moden: Die Feldkonfiguration, die einem Attraktorzustand entspricht, ist die
Körperkarte dieser Emotion. Körperkarten sind Messungen der Attraktoren; das Soma-Feld
ist das dynamische System, das sie erzeugt.

**Die formale Korrespondenztabelle** erweitert Tabelle 2, um diese Systeme einzuschliessen:

| Existierende Repräsentation | Was sie erfasst | Soma-Feld-Äquivalent |
|---|---|---|
| Ekman-Kategorien | Attraktor-Labels (Namen) | Werte von $\mathbf{e}$ an Energieminima |
| Plutchik-Dyaden ($A \sqcap B$) | Misch-Attraktoren | Metastabile Zustände zwischen zwei Energieminima |
| Russell-Zirkumplex | Koordinaten (Valenz, Erregung) | Projektion von $H(\mathbf{e})$ auf zwei Achsen |
| OCC-Bewertungsbaum | Einzelpfad-sequentieller Prozess | Einzelne Trajektorie im vollen Feld |
| BRECVEMA-Mechanismen | Objekteigenschaften: Stimulus → Emotion | Zeilen von $W$: Mechanismus $i$ aktiviert Mode $j$ |
| Körperkarten (Nummenmaa) | Räumlicher Träger jedes Attraktors | Modale Struktur von $\mathbf{e}$ an jedem Minimum |

Keine dieser Korrespondenzen erfordert eine Modifikation entweder der existierenden Repräsentationen oder des
Soma-Feld-Modells. Sie sind Konsequenzen der Struktur des Modells. Die formale Maschinerie zur
Erforschung dieser Korrespondenzen — Typisierung von BRECVEMA-Mechanismen als Lean-induktive Konstruktoren,
Plutchik-Mischungen als Typ-Schnittmengen, Mechanismus-Profile als entscheidbare Propositionen — wird
in der Begleitdatei `src/EmotionOntology.lean` entwickelt.

---

# Das Soma-Feld-Modell

Das Feld ist primär. Die gefühlte Emotion ist sekundär — sie ist das, was registriert wird, wenn das
Feld sondiert wird. Dies ist dieselbe ontologische Beziehung wie zwischen einem Quantenfeld
und einem Teilchen: Das Feld existiert kontinuierlich und überall; das Teilchen ist das, was Sie
im Moment der Messung beobachten. Das Soma-Feld-Modell beschreibt nicht, *woraus* Emotionen
gemacht sind. Es beschreibt die Mannigfaltigkeit, deren Impulsantwort *die* bewusste
emotionale Erfahrung *ist*.

## Emotionen als persistentes Wellenfeld

Die fundamentale Behauptung des Soma-Feld-Modells ist einfach: Emotionen sind keine Ereignisse. Sie sind
ein *Feld* — eine verteilte, kontinuierliche Grösse, definiert über das gesamte Soma (Körper-Geist-System)
zu allen Zeiten.

Dieses Feld hat zwei gekoppelte Komponenten:

1. **Die somatische Welle** $\mathbf{E}_\text{body}(x,t)$: verteilt über den Körper als Muster
   viszeraler Empfindung, Muskeltonus, Propriozeption, Interozeption und autonomer Zustand.
2. **Die neuronale Welle** $\mathbf{E}_\text{neural}(x,t)$: verteilt über das Nervensystem
   als Muster der Aktivierung in kortikalen, subkortikalen und peripheren neuronalen Schaltkreisen.

Diese beiden Komponenten sind keine separaten Systeme. Sie sind gekoppelt — jede beeinflusst
die andere kontinuierlich. Das gesamte emotionale Feld ist ihr kombinierter Zustand:

$$\mathbf{E}(x,t) = \mathbf{E}_\text{body}(x,t) \otimes \mathbf{E}_\text{neural}(x,t)$$

Das Feld ist charakterisiert durch:

- **Multiplizität**: mehrere emotionale Moden können simultan aktiv und interferierend sein
- **Kontinuität**: es existiert zu allen Zeiten, nicht nur während Episoden bewussten Fühlens
- **Räumliche Verteilung**: verschiedene Aspekte des Feldes sind in verschiedenen Regionen
  des Somas lokalisiert (die vertraute klinische Beobachtung, dass Trauer in der Brust gefühlt wird, Furcht
  im Bauch, Wut im Kiefer und in den Fäusten)
- **Zeitliche Dynamik**: das Feld entwickelt sich kontinuierlich, angetrieben von der Energiefunktion

![](figures/fig1_architecture.pdf){ width=90% }
*Abbildung 1. Das Soma-Feld. Körper und Gehirn sind keine separaten Behälter von Emotion, sondern zwei
gekoppelte Komponenten eines einzigen verteilten Wellenfeldes. Keines ist primär; jedes modifiziert
das andere kontinuierlich. Die ≋-Symbole zeigen an, dass Wellenaktivität in jeder Region immer präsent ist,
nicht nur während Episoden bewussten Fühlens.*

## Die Wahrnehmungsschwelle

Nicht alle Aktivität im emotionalen Feld wird bewusst wahrgenommen. Das Feld hat eine **Wahrnehmungs-
schwelle** $T_i$ für jede emotionale Mode $i$. Unter dieser Schwelle ist die emotionale Mode
unterschwellig: Sie existiert, sie beeinflusst Verhalten und Physiologie, aber sie taucht nicht als
benanntes bewusstes Gefühl auf.

$$\text{Emotion } i \text{ wird bewusst wahrgenommen} \iff |\mathbf{E}_i(t)| > T_i$$

Diese Schwellenüberquerung entspricht genau der QFT-Anregungs-Analogie: Die emotionale
Mode verhält sich wie ein virtuelles Teilchen, das genug Energie akkumuliert hat, um real zu werden — aus
dem unterschwelligen Hintergrund aufzutauchen und ins Bewusstsein einzutreten.

Dies erklärt eine Reihe klinisch bedeutsamer Phänomene:

| Klinische Beobachtung | Soma-Feld-Bericht |
|---|---|
| Patient berichtet kein Gefühl, zeigt aber physiologische Zeichen von Distress | Unterschwellige Feldaktivität unter $T_i$ |
| Plötzliche unerwartete Flut von Emotion in der Sitzung | Schnelle Schwellenüberquerung nach allmählicher Akkumulation |
| Emotion somatisch gefühlt, aber nicht benannt | Schwelle überquert in $\mathbf{E}_\text{body}$, noch nicht in $\mathbf{E}_\text{neural}$ |
| Alexithymie (Schwierigkeit beim Identifizieren von Gefühlen) | Erhöhte $T_i$ — hohe Schwelle erfordert mehr Energie zum Überqueren |
| Hypervigilanz / emotionales Überfluten | Gesenkte $T_i$ — reduzierte Schwelle, Feld überquert leicht zum Bewussten |

*Tabelle 1. Klinische Beobachtungen, abgebildet auf das Wahrnehmungsschwellen-Modell.*

![](figures/fig2_threshold.pdf){ width=90% }
*Abbildung 2. Die Wahrnehmungsschwelle T_i für eine einzelne emotionale Mode. Das Feld ist kontinuierlich
aktiv (untere Spur). Bewusste Erfahrung entsteht nur, wenn die Amplitude T_i überschreitet
(obere Spur). Alles unter der Linie ist immer noch da — es formt Körper und Verhalten,
bevor es benannt werden kann.*


![](figures/fig0_field_mode.pdf){ width=95% }
*Abbildung 0. Kontinuierliche Soma-Feld-Aktivität (blau) mit einem einzelnen schwellenüberschreitenden Ereignis. Das Feld ist immer aktiv; bewusste Erfahrung (schattiert) entsteht nur, wenn die Amplitude die Wahrnehmungsschwelle θ (rot gestrichelt) überschreitet. Unter der Schwelle: real, kausal aktiv, aber noch nicht bewusst.*

## Die Wechselwirkung emotionaler Moden

Mehrere emotionale Moden sind zu allen Zeiten simultan im Feld aktiv. Sie ko-existieren
nicht einfach: Sie wechselwirken. Die Natur dieser Wechselwirkungen wird in der **emotionalen
Kopplungsmatrix** $W$ kodiert, wobei $W_{ij}$ den Einfluss der emotionalen Mode $j$ auf
die emotionale Mode $i$ repräsentiert.

- Wenn $W_{ij} > 0$: Emotion $j$ verstärkt Emotion $i$ (z. B. kann Furcht Scham verstärken)
- Wenn $W_{ij} < 0$: Emotion $j$ unterdrückt Emotion $i$ (z. B. unterdrückt Ruhe Angst)
- Wenn $W_{ij} = 0$: Emotionen $i$ und $j$ sind unabhängig

Das Feld entwickelt sich gemäss dem Energiegradienten:

$$\dot{\mathbf{e}}(t) = -\nabla H(\mathbf{e}) + \eta(t)$$

wobei $\eta(t)$ die kontinuierlichen niederen Fluktuationen des unterschwelligen Feldes repräsentiert
— das emotionale Äquivalent von Quantenvakuum-Rauschen. Das Feld bewegt sich immer, sucht immer
niedrigere Energie, ist nie in absoluter Ruhe.

---

## Die Drei-Schicht-Architektur

Das Nervensystem, das das Soma-Feld implementiert, ist nicht architektonisch flach. Drei
hierarchisch organisierte Schichten tragen zur Felddynamik bei, jede entsprechend einem
verschiedenen evolutionären Substrat und einer verschiedenen Rolle im Modell. Die klinische Literatur
(Porges, 2011; van der Kolk, 2014; Ogden et al., 2006) konvergiert auf diese Stratifizierung;
was folgt, ist ihr formaler Ausdruck.

**Schicht 1 — Hirnstamm / autonome Basislinie.** Die ältesten Strukturen: vagale Kerne,
Erregungssysteme, interozeptive Maschinerie. Im Modell wird diese Schicht durch den
Rauschterm und spezifisch durch die Herzratenvariabilitäts-Kohärenz $C_{\text{HRV}}$ repräsentiert,
die die effektive Rauschamplitude über das gesamte Feld moduliert:
$$\sigma_{\text{eff}} = \frac{\sigma_0}{C_{\text{HRV}}}$$
Hohe HRV-Kohärenz verengt das effektive Rauschen und stabilisiert das Feld in seinem aktuellen Attraktor.
Dies ist der Mechanismus des HRV-Biofeedbacks als regulatorische Intervention: Es zielt nicht
auf eine spezifische emotionale Mode ab, sondern senkt die Fluktuationsbasis des gesamten Feldes.

**Schicht-1-Erweiterung: kardiale Beschleunigung und Landschaftsneigung.** Der Term $C_{\text{HRV}}$
misst den *aktuellen Zustand* der kardialen Regelmässigkeit — wo das Herz ist. Eine ergänzende
Grösse ist $\dot{H}(t)$, die erste Zeitableitung der Herzrate, in Einheiten von Schlägen/s$^2$.
Dies ist die **kardiale Beschleunigung**: nicht was die Herzrate ist, sondern wohin sie geht.

Die dimensionale Parallele zur Gravitation ist exakt: Gravitationsbeschleunigung $g$ trägt
Einheiten m/s$^2$; kardiale Beschleunigung $\dot{H}$ trägt Einheiten Schläge/s$^2$. Beide sind
Beschleunigungen; beide beschreiben ein Kraftfeld statt einer Position. Gravitation sagt Ihnen nicht,
wo eine Testmasse ist — sie sagt Ihnen, wie sie sich als Nächstes bewegen wird. Kardiale Beschleunigung sagt
Ihnen nicht die aktuelle BPM, sondern die Richtung der nächsten: der N+1-Zustand.

Im Soma-Feld geht $\dot{H}(t)$ in die Dynamik nicht als Rauschmodulation ein, sondern als
**Landschaftsneigung** — eine zeitlich variierende Vorspannung, die zum Hamiltonian hinzugefügt wird und die Energie-
funktion zu Aktivierungs- oder Ruhe-Attraktoren kippt:

$$H(\mathbf{e}, t) = H_0(\mathbf{e}) - \alpha\,\dot{H}(t)\,\boldsymbol{\beta}\cdot\mathbf{e}$$

wobei $\alpha > 0$ die kardio-somatische Kopplungskonstante ist und $\boldsymbol{\beta}$
ein Modenkopplungs-Vektor ist (in führender Ordnung $\boldsymbol{\beta} = \mathbf{1}$: Die Neigung
wirkt einheitlich über alle Moden). Wenn $\dot{H}(t) > 0$ (Herz beschleunigt), kippt die
Landschaft zu höheren Aktivierungszuständen, bevor irgendeine kognitive oder affektive Schwelle
überquert wird. Wenn $\dot{H}(t) < 0$ (Herz verlangsamt sich), kippt sie zur Ruhe. Die volle
Drei-Schicht-Gleichung einschliesslich des kardialen Beschleunigungsterms ist:

$$\dot{\mathbf{e}}(t) = -\nabla H_0(\mathbf{e}) + \alpha\,\dot{H}(t)\,\boldsymbol{\beta}
  + R_{\text{PFC}}(\mathbf{e}, t)
  + \frac{\sigma_0}{C_{\text{HRV}}}\,\xi(t)$$

Die beiden kardialen Terme dienen verschiedenen Funktionen: $C_{\text{HRV}}$ (Zustand) moduliert die
Rauschbasis; $\dot{H}$ (Beschleunigung) kippt die deterministische Landschaft. Beide werden benötigt
für einen vollständigen Bericht über den kardialen Einfluss auf das Feld.

**Prädiktiver klinischer Wert.** Ein Patient mit BPM = 90 und $\dot{H} = +4$ Schläge/s$^2$
nähert sich der Schwelle; einer mit BPM = 90 und $\dot{H} = -4$ Schläge/s$^2$ zieht sich
von ihr zurück. Die Momentaufnahme ist identisch; die Trajektorien sind entgegengesetzt. Kardiale Beschleunigung
ist daher ein Frühwarnsignal für Schwellenüberquerungen — detektierbar bei Schicht 1,
bevor das emotionale Feld bei Schicht 2 seine Schwelle überquert hat. Dies hat unabhängige
Unterstützung in der Kardiologie: Bauer et al. (2006) zeigten, dass *Beschleunigungskapazität* und
*Verlangsamungskapazität* der Herzrate — Schätzungen von $\dot{H}$ über ein kardiales Fenster —
prognostische Information unabhängig von konventionellen HRV-Massen tragen.

**Das somatische Äquivalenzprinzip.** Der kardiale Beschleunigungsterm $\alpha\,\dot{H}\,\boldsymbol{\beta}$
ist in der Gleichung strukturell identisch mit jedem anderen Antriebsterm. Aus der Perspektive
des Feldes selbst — aus bewusster Erfahrung — ist kardial-getriebene Aktivierung
ununterscheidbar von ereignisgetriebener Aktivierung. Eine plötzliche Herzraten-Beschleunigung kippt
die Landschaft durch genau denselben Mechanismus wie eine externe Bedrohung oder eine intrusive Erinnerung.
Das Feld hat keinen Zugang zum Ursprung der Neigung. Dies ist der formale Bericht eines
klinisch gut dokumentierten Phänomens: Angst, initiiert durch kardiale Unregelmässigkeit
(Arrhythmie, posturale Hypotonie, Koffein, Anstrengung), wird als emotional
verursacht erlebt, weil das somatische Signal identisch ist. Disambiguierung erfordert entweder externe
Messung oder bewusste interozeptive Erkundung, die die beiden Quellen unterscheiden kann.

**Schicht 2 — Limbisches System / emotionales Gedächtnis.** Das primäre Substrat des Soma-Feld-
Modells. Die Kopplungsmatrix $W$, der Erinnerungskern $K(\tau)$, der Hamiltonian $H(\mathbf{e})$ und
die Schwelle $T$ gehören alle hierher. Die limbische Schicht speichert emotional-somatische Zustände und
reinstatiert sie als Reaktion auf partielle Körperhinweise: ein kontinuierliches, asymmetrisches, zeitlich
ausgedehntes Hopfield-Netzwerk, das auf somatischen Zuständen statt auf kognitiven Mustern operiert.
Dies ist die architektonische Schicht, die in jedem künstlichen neuronalen Netz seit
McCulloch und Pitts (1943) [@mcculloch1943] abwesend war. Der Kortex wurde viele Male modelliert; das limbische
System nicht.

**Strukturelle Plastizität unter Widrigkeit.** Das Soma-Feld-Framework erlaubt eine formale
Charakterisierung der Resilienz des Feldes unter widrigen Bedingungen. Definieren Sie den
*Plastizitätsindex* $\Pi$ als ein Komposit von drei messbaren Feldeigenschaften:

$$\Pi \;=\; \frac{1}{S_{\text{inst}}} + \left.\frac{\partial \|W\|}{\partial t}\right|_{\text{Widrigkeit}} + C_{\text{HRV}}^{\text{recovery}}$$

Die drei Terme entsprechen: (i) wie zugänglich regulierte-Zustand-Attraktoren unter
Widrigkeit bleiben ($1/S_{\text{inst}}$, Instanton-Zugänglichkeit — Abschnitt 4.4); (ii) wie sehr die
Kopplungsmatrix sich nach einer Schwellenüberquerung strukturell anpassen kann
($\partial \|W\|/\partial t$, die Plastizitätskomponente); und (iii) wie schnell sich die HRV-
Basis nach Aktivierung erholt ($C_{\text{HRV}}^{\text{recovery}}$, die regulatorische
Resilienzkomponente). Komplexe PTBS ist die klinische Präsentation chronisch niedrigen $\Pi$
über alle drei Terme gleichzeitig: hohe Barrieren zu regulierten Attraktoren, ein rigides $W$,
dominiert von Bedrohungskonfigurationen, und beeinträchtigte $C_{\text{HRV}}$-Erholung. Strukturelle
Plastizität ist die Kapazität des Feldes, $W$ in der Folge der Widrigkeit zu aktualisieren,
ohne dass die Widrigkeit permanent zu $W$ *wird*.

**Schicht 3 — Neokortex / präfrontale regulatorische Schicht.** Top-down-Modulation von Schicht 2,
repräsentiert als regulatorischer Term $R_{\text{PFC}}(\mathbf{e}, t)$. Die volle Felddynamik
wird:

$$\dot{\mathbf{e}}(t) = -\nabla H(\mathbf{e}(t))
  + R_{\text{PFC}}(\mathbf{e}, t)
  + \frac{\sigma_0}{C_{\text{HRV}}}\, \xi(t)$$

$R_{\text{PFC}}$ repräsentiert willkürliche Aufmerksamkeit, therapeutische Technik und bewusste
Neubewertung, die auf das Feld einwirken. Es ist keine Korrektur von Schicht 2, sondern eine Modulation
davon. Unter anhaltendem therapeutischem Engagement nimmt $R_{\text{PFC}}$ an der
strukturellen Modifikation $W \to W'$ teil, die die Vorwärtstransformation (Abschnitt 7) konstituiert.

Die **Schwelle $T$ ist die Schicht-2-/Schicht-3-Grenze**: Unterschwellige Dynamik wird
limbisch verarbeitet und bleibt unter bewusstem Bewusstsein; schwellenüberschreitende Ereignisse gehen
in Schicht 3 ein und werden verfügbar für Narrativ, Sinnstiftung und willkürliche Antwort. Dies
ist die formale Basis für die klinische Beobachtung, dass Einsicht ohne somatische Aktivierung
begrenzt ist und somatische Aktivierung ohne Schicht-3-Engagement keine strukturelle
Veränderung produzieren kann: Die Schichten sind gekoppelt, nicht unabhängig. $R_{\text{PFC}}$ erfordert eine Schwellen-
überquerung, um etwas zu haben, womit es arbeiten kann.

Die in Abschnitt 3.3 eingeführte Zwei-Term-Langevin-Gleichung ist der Schicht-2-Spezialfall
($R_{\text{PFC}} = 0$, $C_{\text{HRV}} = 1$). Alle nachfolgenden Abschnitte entwickeln diesen
Spezialfall. Die volle Drei-Schicht-Gleichung ist die allgemeine Form.

---
