# 03 - Contratto di Output

Formato standard dell'output. Riferimento canonico: la struttura Notion a 3
tabelle. Le colonne sono in italiano.

Default consegnato: **3 hook + 1 body completo**. La tabella B-roll si popola
**solo su richiesta**.

---

## Tabella 1 - Hooks

Colonne: **Module | Cosa devi dire | Cosa far vedere | Note per Editor**

- **Module:** identificativo dell'hook con etichetta descrittiva del suo angolo o
  persona. Esempio: `Hook 1 - proprietario stanco`, `Hook 2 - proprietario con
  property manager`.
- **Cosa devi dire:** il parlato dell'hook (script, non testo a schermo).
- **Cosa far vedere:** indicazione visiva per il creator (vedi regole sotto).
  Puo' essere vuota se coincide con quanto ovvio dal parlato.
- **Note per Editor:** qui va **sempre** il testo on-screen dell'hook, con la
  dicitura `Testo on-screen:`, piu' eventuali indicazioni di editing (vedi
  regole). Esempi visti: `Testo on-screen (IG response): "Non sapevo di poter
  risparmiare cosi' tante tasse sul mio affitto breve"`, `Testo su sfondo: "Stai
  pagando il 20-30% al tuo property manager?"`.

### Righe di ricombinazione ("per editor")

> **Nota (correzione vs variante).** Se uno dei 3 hook base non aggancia bene il
> Body 1, il taglio va scritto in "Note per Editor" della **sua stessa riga**
> (correzione di aggancio, vedi `01-hook-system.md` §8a). Le righe Hook 4/5/6
> servono solo per **varianti creative aggiuntive**, non per rimediare a hook
> mal costruiti.

Dopo gli hook reali, puoi aggiungere righe che descrivono **varianti di montaggio**
combinando un hook con un pezzo di body. Servono all'editor per assemblare
creative diverse dallo stesso materiale.

- `Hook 4 (per editor)` con contenuto `Body 1` = variante che usa quel blocco.
- `Hook 5 (per editor)` con contenuto `Hook 1 + parti da body 3`.
- `Hook 6 (per editor)` con contenuto `Hook 2 -> body 4`.

Regola di notazione (vedi anche `01-hook-system.md`, sez. 8):
- Un solo blocco eliminato: indica il blocco e da dove partire (`parti da body 1`).
- Piu' di 2/3 blocchi eliminati: elenca la sequenza dei blocchi, uno per riga.

---

## Tabella 2 - Scene Script (il body)

Colonne: **Module | Selling Block | Cosa devi dire | Cosa far vedere | Note per Editor**

- **Module:** `Body 1`, `Body 2`, ... e infine `CTA`.
- **Selling Block:** uno o piu' tag dalla libreria sotto (in Notion sono tag
  colorati). Un blocco puo' avere piu' tag (es. `Showcase` + `Handle objection`).
- **Cosa devi dire:** il parlato di quel blocco.
- **Cosa far vedere:** indicazione visiva per il creator (regole sotto).
- **Note per Editor:** presente **solo quando serve**. Contiene testo on-screen
  (`Testo on-screen: ...`) per evidenziare un problema/rischio/beneficio/feature,
  ed eventuali indicazioni di editing (sfx, layout, grafiche).

> La colonna "Note per Editor" nel body non e' obbligatoria riga per riga: si usa
> nei punti dove un testo a schermo o un'istruzione di montaggio aggiunge valore.

---

## Tabella 3 - Broll Shots / Contenuti (solo su richiesta)

Colonne: **Scene | Visual**

- **Scene:** numero progressivo.
- **Visual:** descrizione della clip B-roll da registrare a parte.

Si popola solo quando l'utente la richiede, in una di due modalita' (vedi
`06-broll-generation.md`):
1. indicazioni semplici per il creator, oppure
2. prompt specifici per generare i B-roll con l'AI.

---

## Cosa far vedere: regole (indicazioni visive per il creator)

Il "cosa far vedere" puo' essere: una **clip B-roll** da registrare a parte
(silenziosa, che aggancerete in editing) oppure **movenze/gesti/contesto** da
applicare durante il parlato. In entrambi i casi:

- Semplici da capire per una persona poco scolarizzata: cosa deve fare, come, in
  che contesto.
- **Non sono indicazioni di editing.** Non spieghi come le clip si legano tra
  loro. Dai solo indicazioni al creator/attore per un output il piu' vicino
  possibile a cio' che vuoi comunicare.
- Spiegate brevemente.
- **Una registrazione per blocco.** Non chiedere 2 clip in contesti diversi per
  una sola frase o un solo blocco, a meno che il blocco sia lungo e con piu'
  step: in quel caso le clip possono aumentare leggermente.
- Tutto realizzabile da una persona normale, senza budget, con doti di recitazione
  e materiali quotidiani presenti in tutte le case del target (oltre a prodotto e
  props specifici forniti dal brand). Luoghi comuni e raggiungibili: auto, parco,
  supermercato, una o piu' stanze di casa. Mai studi o set cinematografici.

### Cosa NON va in "Cosa far vedere"

Non vanno qui: grafiche animate, motion graphics, testi che compaiono a
schermo, split screen, transizioni, sfx, layout di editing, timing di post.
Tutto questo e' lavoro dell'editor, va in **"Note per Editor"**.

Regola pratica: **se non lo puo' fare il creator con la sua camera in quel
momento, non e' "Cosa far vedere"**.

Esempi:

| Elemento | Dove va | Perche' |
|---|---|---|
| Talent indica una lavagna con due colonne scritte a mano | Cosa far vedere | Lo fa il creator in ripresa |
| Barra animata che cresce da "3%" a "15,5%" a lato dello schermo | Note per Editor | E' motion graphic in post |
| Screenshot mostrato sul laptop del talent (schermo acceso in ripresa) | Cosa far vedere | Il laptop c'e' sul set |
| Screenshot messo in overlay dall'editor sopra la clip | Note per Editor | E' composizione in post |
| Talent scrive numeri a mano su un blocco, zoom sui numeri | Cosa far vedere | Ripresa reale, lo zoom e' movimento camera |
| Numeri che pulsano in bold on-screen | Note per Editor | E' motion in post |

---

## Note per Editor: regole (sono un'altra cosa)

Le note per l'editor sono **diverse** dalle indicazioni visive per il creator.
L'editor e' una persona diversa dal creator. Le note lo aiutano a migliorare
l'editing in post-produzione: sfx, layout di schermo, testi on-screen, stile
grafico.

- Massima precisione con il minimo testo necessario.
- Ordine consigliato quando serve: **Visual / B-roll > Text overlay > Motion >
  Timing > Transition.**
- Non descrivere cinematograficamente ogni secondo se non serve.

---

## Comprensibilita' istruzioni produttive

Le colonne "Cosa far vedere" e "Note per Editor" sono lette da creator e editor,
non da strategist. Devono essere comprensibili al primo passaggio, senza
interpretazione.

### Regole

- **Una azione per frase.** Ogni frase contiene un solo soggetto e un solo verbo
  imperativo o descrittivo. Se servono due azioni, due frasi.
- **Zero pronomi vaghi.** Mai "questo", "quello", "cio'" senza referente
  esplicito nella stessa frase. Riformula con il sostantivo.
- **Zero acronimi senza definizione.** La prima occorrenza di un acronimo non
  standard (fuori da CTA, UGC, B-roll, VO) va scritta per esteso.
- **Dire cosa fare, non cosa non fare.** Istruzioni positive: "Inquadra il
  prodotto da vicino", non "Non inquadrare da lontano".
- **Niente catene di subordinate.** Massimo una subordinata per frase. Se la
  frase ha bisogno di due "che" o due "quando", spezzala.
- **Verbi concreti.** "Mostra", "Inquadra", "Tiene in mano", "Scrivi a schermo".
  Mai "Comunica l'idea di", "Evoca il concetto di", "Rappresenta".

### Target di leggibilita'

Indice Flesch-Vacca (adattamento italiano del Flesch Reading Ease) tra **60 e
90** sulle celle "Cosa far vedere" e "Note per Editor". Sotto 60 = troppo
complesso per il creator medio. Sopra 90 = probabilmente troppo scarno (manca
informazione).

| Fascia | Significato | Azione |
|---|---|---|
| 90-100 | Elementare | Verifica che l'istruzione sia completa |
| 60-90 | **Target operativo** | OK |
| < 60 | Troppo complesso | Riscrivi: spezza frasi, semplifica vocabolario |

---

## Libreria Selling Block

Tag operativi da usare nella colonna "Selling Block". Questa libreria e'
**compilata dai tuoi materiali** (guida 5.5, tag dei tuoi Notion, e
`formattazione ads`) ed e' **estendibile**: aggiungi o rinomina i tag quando
serve, questo file e' il punto unico dove aggiornarli.

**Apertura / identificazione**
- `Problem` - nomina il problema con linguaggio del cliente
- `Human Entry` - hook narrativo, nomina una persona e un conflitto reale
- `Relatable Struggle` - accumulo di micro-frustrazioni ("sono io")
- `Agitation` - amplifica il peso del problema (tempo, stress, famiglia, soldi)

**Ponte / soluzione**
- `Discredit Alternative` - screditare la soluzione standard / vecchio modo
- `Bridge / Discovery` - introduce la possibilita' di soluzione senza vendere
- `Solution` - il prodotto entra come scoperta, non come pitch

**Prodotto / meccanismo**
- `Unique` / `Unique Mechanism` - perche' e' diverso da tutte le alternative
- `Showcase` - mostra il prodotto in azione
- `Feature` - una caratteristica concreta
- `Benefit` / `Benefit Translation` - traduce la feature in vita migliore

**Obiezioni / prova**
- `Handle objection` - anticipa e neutralizza un'obiezione
- `Skeptical Dialogue` - dialogo scettico (adatto a 2 attori)
- `Proof of Result` / `increase % achievement` - risultato specifico, dato o %
- `Increase perceived value` - alza il valore percepito

**Chiusura**
- `Verbalized Desire` - lo spettatore verbalizza il desiderio
- `CTA` / `Low-Friction CTA` - azione chiara, attrito ridotto, curiosity
  continuation quando adatta

> Nota sui due sistemi di naming. La guida descrive 10 selling block concettuali
> (Human Entry, Relatable Struggle, Agitation Without Selling, Bridge/Discovery,
> Skeptical Dialogue, Unique Mechanism, Benefit Translation, Verbalized Desire,
> Proof of Result, Low-Friction CTA). Nei tuoi Notion usi tag operativi piu'
> granulari (Problem, Discredit Alternative, Solution, Showcase, Handle
> objection, Benefit, Feature, Unique, increase % achievement, Increase perceived
> value). Nella tabella vanno i **tag operativi**; i 10 blocchi concettuali
> restano la logica sottostante (approfondimento in `formats-guide.md`, sez 5.5).

---

## Override di formattazione per-format

Alcuni format richiedono una formattazione diversa o piu' semplice del default a
3 tabelle. Meccanismo: il file del format in `references/formats-guide.md` (o una
nota dedicata) puo' dichiarare un blocco `Regole di formattazione specifiche` che
sovrascrive questo contratto per quel format. Se presente, quelle regole vincono.

> Stato attuale: nessun override definito. Verranno aggiunti quando indicherai
> quali format li richiedono e come.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
