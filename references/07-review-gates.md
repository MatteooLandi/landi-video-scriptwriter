# 07 - Review Gates

Sistema di enforcement in 4 gate per ogni brief script consegnato. I gate girano
in ordine, ognuno ha un linter meccanico + un reviewer che giudica. Design:
**avvisatorio di default, bloccante solo su fabricated facts o density alta**.

> **Regola cardinale del gate Grounding:** `fact` vs `flavor`. I prezzi, gli
> spec e i claim di prodotto inventati tracciano o fanno bounce. I **numeri e le
> percentuali senza fonte** non fanno piu' bounce silenzioso: attivano il
> **claim flag** (due versioni, scelta a Matteo — vedi Gate 4 e
> `docs/claim-strategy.md` del Brain). Il linguaggio del cliente non tracciato è
> solo un warning con label "illustrativo", **non** blocca la consegna. Una
> singola frase parlata non perfettamente coperta da `verbatim.md` non ferma
> tutto.

---

## Ordine di esecuzione

```
Format → Hook → Voice → Grounding
```

- **Format** è precondizione: se il brief non ha le tabelle giuste, i gate a
  valle non possono nemmeno leggerlo. Bounce di Format ferma la catena.
- **Hook** e **Voice** sono indipendenti: si possono eseguire in parallelo dopo
  Format ok, ma di norma si esegue Hook prima (le riscritture voice possono
  toccare le stesse righe).
- **Grounding** è ultimo: giudica dati e fonti su script formattato e voiceato,
  perché una riscrittura voice può togliere una frase inventata.

---

## Gate 1 - Format (contratto tabelle)

**Linter:** `scripts/format-lint.py <draft>`
**Reviewer indipendente:** non necessario (deterministico, solo tabelle).
**Riferimento regole:** `references/03-output-contract.md`.

**Bounce (finding):**
- Header Tabella 1 diverso da `Module | Cosa devi dire | Cosa far vedere | Note per Editor`
- Header Tabella 2 diverso da `Module | Selling Block | Cosa devi dire | Cosa far vedere | Note per Editor`
- Header Tabella 3 (se presente) diverso da `Clip | Funzione narrativa | Indicazioni per il creator`
- CTA mancante in Tabella 2
- Placeholder non compilati (`{compilare}`, `TBD`, `TODO`, `___`, `[insert`, `<insert`, `[nome]`, `[brand]`)
- Sintassi `Testo on-screen:` senza contenuto dopo i due punti
- Naming Module fuori pattern (`Hook \d+( \(per editor\))?`, `Body \d+`, `CTA`)

**Warning (passa con nota):**
- Cella "Cosa devi dire" > 40 parole (brief scannerizzabile)
- Selling Block tag fuori libreria (elenco in `03-output-contract.md`)
- "Cosa far vedere" contiene indicazioni editor (`sfx:`, `text overlay:`, `fade to`)

**Ricevuta:** blocco `## Format Review: ships | bounced` in coda al brief.

---

## Gate 2 - Hook (regole hook system)

**Linter:** `scripts/hook-lint.py <draft>`
**Reviewer indipendente:** non necessario finché sono regole deterministiche.
**Riferimento regole:** `references/01-hook-system.md` § 2, 4, 5, 8, 10.

**Bounce (finding):**
- Numero hook base ≠ 3 (default) senza richiesta esplicita
- Testo on-screen mancante in "Note per Editor" per una riga hook
- Testo on-screen copiato dal parlato (similarity > 90%)
- Lunghezza testo on-screen fuori range 1-14 parole
- Brand/prodotto (da `_manifest.md`) nel "Cosa devi dire" dell'hook (primi 3s regola)
- Ricombinazione senza `(per editor)` nel Module

**Warning (passa con nota):**
- Diversità tra hook 1-2-3 sotto soglia (Jaccard > 0.6 su parole ≥ 4 lettere)
- Segnali audience assenti (nessun marker Target/Problema/Categoria)
- Prime 3 parole da throat-clearing italiano ("allora", "quindi", "insomma", "beh")
- Aggancio Body 1 non verificabile senza indicazione taglio in "Note per Editor"

**Ricevuta:** `## Hook Review: ships | bounced` con lista warning se ci sono.

---

## Gate 3 - Voice (anti-AI-slop parlato)

**Linter:** `scripts/voice-lint.py <draft>`
**Reviewer indipendente:** agent `voice-reviewer-landi` (contesto fresco,
non ha scritto il draft).
**Riferimento regole:** `references/02-writing-principles.md` non-negoziabili 1-4.

### Soglie

- **Density < 0.3 flag/riga** (flag per riga non vuota) → passa
- **Density ≥ 0.3** → flagged, il reviewer decide se rerun
- **Cluster: 3+ tell nella stessa riga hook** → flagged sempre, rerun quell'hook
- **Verbatim exemption:** se una frase è esatta match in
  `brand-context/verbatim.md`, non è flag anche se contiene parola dalla lista
  banned. Il reviewer verifica il match e mantiene la frase.

### Bounce (reviewer verdict `flagged`):

- Trattino lungo `—`, oppure trattino medio `–` usato come punteggiatura. Il
  trattino medio resta ammesso per intervalli e coppie reali, per esempio
  `15–20 secondi` o `origine–destinazione`.
- Cluster di tell in un hook
- Pattern "non è solo X, è Y" e varianti
- Falso contrasto in tutte le sue forme: "Non è X. È Y.", "il punto non è X, ma
  Y", "non si tratta di X, ma di Y", "non stiamo dicendo X, stiamo dicendo Y",
  "sembra X e invece è Y". Passa solo se risponde a un'obiezione nominata
  davvero nello script
- Impalcatura a comando fuori da CTA e istruzioni d'uso: "Smetti di X, inizia a
  Y", "Basta con X", "Devi smettere di X", "Non fare X, fai Y"
- Serie di tre o più frasi senza verbo che non corrisponde a stacchi, clip o
  beat dichiarati nelle Note per Editor
- Enfasi in maiuscolo dentro il parlato: va spostata in Note per Editor come
  indicazione di delivery
- Domande retoriche auto-poste
- Puffery / brochure register
- CTA da ad-speak
- Ponti signposted
- Category entry point implicito quando regge il messaggio: un neofita deve
  capire occasione, categoria e azione senza avere il brief davanti
- Formula generica che sostituisce l'informazione concreta, per esempio "buon
  punto di partenza", "momento giusto", "informazioni utili" o "opzione piu'
  adatta"
- Residuo conversazionale dell'assistente dentro il deliverable
- Traduzione grammaticalmente corretta ma generica o non nativa nel mercato di
  destinazione
- Density complessiva alta

### Warning (passa con label):

- Singolo tell isolato in body (< 3 nella riga)
- Vocabolario "importance-inflator" senza altri tell nella riga
- Tre o più frasi di fila che iniziano con la stessa parola dentro lo stesso
  blocco: warning al reviewer, che decide se è anafora voluta o piattume

**Ricevuta:** `## Voice Review: ships | flagged` con density prima/dopo e lista
flag risolti.

### Lista pattern (bozza, da validare)

Elenco patterns per `voice-lint.py`. **Questa lista è la fonte unica di verità.**
Modificarla qui = modificare il linter (i pattern nel Python sono generati da
qui, non duplicare).

#### Vocabolario flaggato (density flag)

**Importance-inflator:**
`cruciale`, `fondamentale`, `essenziale`, `indispensabile`, `primario`,
`vitale`, `imprescindibile`

**Texture words:**
`armonioso`, `sinergico`, `olistico`, `meticoloso`, `meticolosamente`,
`raffinato`, `sofisticato`, `impeccabile`, `sfaccettato`, `poliedrico`

**Transformation verbs:**
`trasformare`, `trasforma`, `rivoluziona`, `rivoluzionare`, `sblocca`,
`sbloccare`, `potenzia`, `potenziare`, `eleva`, `elevare`, `amplifica`,
`amplificare`, `ottimizza`, `ottimizzare`, `massimizza`, `massimizzare`

**Brochure adjectives:**
`rinomato`, `impareggiabile`, `senza pari`, `senza precedenti`, `pluripremiato`,
`straordinario`, `eccezionale`, `curato`, `su misura`, `esclusivo`

#### Pattern regex

**Negative parallelism** ("non è solo X, è Y" — non-negoziabile #1 bis):
- `non è solo`, `non è soltanto`
- `non solo ... ma anche`
- `non solo ... ma addirittura`
- `più che X, è Y`
- `non un semplice X, ma un Y`

**Inflated significance:**
- `rappresenta una svolta`
- `segna un punto di svolta`
- `apre un nuovo capitolo`
- `un nuovo modo di`
- `una nuova era`

**Manufactured-intimacy opener:**
- `posso essere onesto con te`
- `parliamoci chiaro`
- `diciamocelo`
- `te lo dico chiaramente`
- `voglio essere sincero`

**Rhetorical self-question:**
- `Sembra familiare?`
- `Assurdo, vero?`
- `Ti dice qualcosa?`
- `Sai qual è la cosa peggiore?`
- `Onestamente?`
- `Sai cosa penso?`

**Throat-clearing opener:**
- `Nel mondo di oggi`
- `In un mondo dove`
- `Ai giorni nostri`
- `Immagina di`
- `Immagina questo:`
- `Diciamocelo:`

**Puffery / brochure register:**
- `esperienza premium`
- `esperienza unica`
- `curato nei minimi dettagli`
- `attenzione al dettaglio`
- `impegno per l'eccellenza`
- `nel cuore di`

**Signposted transition:**
- `Ecco la verità:`
- `Ecco perché:`
- `Ecco il punto:`
- `La cosa migliore?`
- `Il segreto?`
- `E qui viene il bello:`
- `Il risultato?`

**Pristine CTA (ad-speak):**
- `Non aspettare oltre`
- `Non perdere tempo`
- `Cambia la tua vita`
- `Meriti di`
- `Unisciti a migliaia`
- `Scopri di più oggi`
- `Ordina ora`

**Audience enumeration:**
- `che tu sia X o Y`
- `sia se X sia se Y`

**Balanced triplet:**
- tre elementi nella stessa frase, stessa lunghezza, coordinati (regex
  generica funziona su italiano)

**Copula avoidance:**
- `offre un'esperienza`
- `offre una gamma`
- `garantisce risultati`
- `fornisce una soluzione`

**Astrazioni vuote:**
- `la nostra soluzione`, `la vostra esperienza`, `il tuo percorso`,
  `il tuo viaggio` senza sostantivo concreto adiacente

**Impalcatura generica / specificita' apparente:**
- `un buon punto di partenza`
- `questo e' il momento giusto`, `e' un buon momento`
- `inizia a prendere forma`
- `dai una prima occhiata`, `dai un'altra occhiata`
- `fa parte dei tuoi programmi`
- `aggiungilo al tuo itinerario`
- `informazioni utili`
- `l'opzione piu' adatta`
- `tutto quello che ti serve`

**Residui dell'assistente:**
- `Certo, ecco...`
- `Di seguito trovi...`
- `Come richiesto...`

**Calchi / impalcatura inglese da controllare in output US:**
- `a good place to start`
- `start with the...`
- `take a first look`, `take another look`, `one more look`
- `part of your plans`
- `fits into your trip/journey/routine`
- `useful information`, `useful updates`
- `the option that fits your...`

**Curly/straight quote mix:** stesso pattern Slagle.

**Em-dash cadence:** stesso pattern Slagle (2+ trattini nella stessa riga).

**Falso contrasto (regex, alta precisione):**
- `non e'/è un|una|uno ... . E'/È ...`
- `il punto non e'/è ... ma`
- `non si tratta di ... ma`
- `non stiamo dicendo ... stiamo dicendo`
- `sembra ... e invece e'/è`
- non flaggare la risposta a un'obiezione nominata ("Troppo pesante per
  l'estate? No: ...")

**Impalcatura a comando (regex, alta precisione):**
- `smetti/smettila/smettetela di|con`
- `basta con il|la|i|le|gli|lo|l'`
- `devi smettere di`
- `non <verbo>are ..., <imperativo>`
- non flaggare CTA e istruzioni d'uso ("Link in bio, usa SARA20", "Ne metti due
  gocce la sera")

**Giudizio del reviewer, non del linter:** serie di frammenti senza montaggio
che la regga, varietà degli attacchi di frase, enfasi da spostare nelle note.
Sono valutazioni di contesto e di produzione, quindi restano al Voice reviewer.

**Trattino lungo e trattino medio:**
- `—` presente ovunque: flag
- ` – ` tra due proposizioni: flag
- intervalli numerici e coppie reali senza spazi: non flaggare

### Pattern da NON flaggare (falsi positivi comuni italiano)

- `praticamente`, `sostanzialmente`, `letteralmente` — spesso naturali nel
  parlato spontaneo, flaggare solo se in cluster
- `insomma`, `comunque` — legittimi nel parlato, warning solo se apertura hook
- Verbatim customer che contengono parole flaggate → esente per definizione
- Trattino medio in un intervallo o in una coppia reale (`15–20`,
  `origine–destinazione`)

---

## Gate 4 - Grounding (fact vs flavor)

**Linter:** `scripts/grounding-check.py <draft> brand-context/`
**Reviewer indipendente:** agent `grounding-reviewer-landi` (contesto fresco).
**Riferimento regole:** `references/00-brand-lookup.md`, questo doc,
`docs/claim-strategy.md` del Brain (nel cliente: `landi-system/.../docs/claim-strategy.md`).

### Regola cardinale: fact vs flavor

- **FLAVOR** (linguaggio, tono, modo di dire, frase "sounds like customer"):
  se non traccia a `verbatim.md` → **WARNING**, aggiungi label
  `Tono: illustrativo — non verbatim verificato` sulla riga. Non blocca.
- **FACT** (numeri, %, prezzi, spec prodotto, claim performance, health claim):
  se non traccia a nessun file `brand-context/*.md` → **BOUNCE**.
  Rerun senza il fatto, o con fonte verificata.

### Fallback verbatim sottopopolato

Se `brand-context/verbatim.md` (e i `products/*/verbatim.md`) hanno **meno di
~20 righe utili di contenuto** o sono al livello template `(compilare)`:

- Il gate **salta** il controllo flavor.
- Emette nota: `verbatim sottopopolato — controllo flavor saltato; solo
  fact-check attivo`.
- Nessun bounce per assenza tracciamento flavor.
- Reviewer segnala nel receipt: `UNVERIFIED VOICE: skipped (verbatim empty)`.

### Bounce (finding fact):

- Claim prodotto specifico senza corrispondenza in `positioning.md` o
  `{prodotto}-positioning.md`
- Named result (nome persona + risultato) non tracciato
- File brand-context cited che non esiste

> I **numeri/percentuali senza fonte** non sono piu' qui: vanno al claim flag
> sotto (non bounce).

### Claim flag — numeri senza fonte (claim-strategy attivo)

Quando un numero o una percentuale nel brief non ha fonte in `brand-context`, il
gate **non lo spedisce in silenzio e non lo cancella**: emette un **claim flag**
(vedi `docs/claim-strategy.md` del Brain). Per ogni claim numerico scoperto:

- scrive **due versioni** della riga: quella **sicura** (qualitativa, senza il
  numero) come default, e quella **aggressiva** con il numero, marcata;
- se il claim regge come esperienza in prima persona, aggiunge una terza
  versione **come testimonianza / commento cliente** — solo con verbatim reale
  (`brand-context/verbatim.md`): un numero inventato resta inventato anche tra
  virgolette di un cliente;
- spiega in **una frase semplice** perche' lo segnala (niente gergo, niente
  "tipo rischio");
- la scelta resta a Matteo. Il flag e' **interno**, non entra mai nell'asset.

**Categorie regolate** (salute, medico, finanza): flag **sempre**, default piu'
sicuro, ma la versione aggressiva viene comunque proposta con una riga che
ricorda che qui il rischio e' piu' alto e dipende dal brand. Nessuno stop duro.

Gli altri fact non numerici inventati (nome persona, claim prodotto, file
inesistente) restano **bounce**: il claim flag riguarda i numeri come leva
persuasiva, non la fabbricazione di fatti verificabili di prodotto.

**Ricevuta claim flag:** blocco `## Claim Flag` in coda, una voce per claim con
le due/tre versioni e la frase di spiegazione.

### Warning (label, non bounce):

- Frase "sounds like customer" non tracciata in verbatim (aggiungi label)
- Verbatim untraceable ma register-coherent (label illustrativo)

**Ricevuta:** `## Grounding Review: grounded | bounced` con:
- `FABRICATED FACTS: <lista o "none">`
- `UNVERIFIED VOICE: <lista o "none / skipped">`
- `REQUIRED TO RE-SHIP: <shortlist>`

---

## Modalità di enforcement (Stop hook)

Il file `.claude/hooks/gate-check.py` verifica in modalità **advisory**:

- Detecta output-shape brief-Landi (header "Tabella 1 - Hooks" o
  `Module | Cosa devi dire`).
- Se rilevato + mancano tutti e 4 i receipts:
  - **Non blocca** la consegna.
  - Emette systemMessage in testa: `⚠ Brief consegnato senza receipts. Voice/Grounding/Format/Hook Review non allegati. Considera rerun con gate attivi.`
  - Utente vede sia il brief sia la nota, decide.

### Upgrade a bloccante

Quando ti fidi delle soglie e vuoi enforcement duro:

1. Apri `.claude/hooks/gate-check.py`
2. Sostituisci `"decision": null, "systemMessage": ...` con
   `"decision": "block", "reason": ...`
3. Il turn viene rifiutato, il modello riesegue i gate prima di riconsegnare.

Non c'è configurazione via env: modifica esplicita perché sia decisione tua.

---

## Override manuale (utente)

Se un gate boccia e sei sicuro che sia falso positivo (pattern deliberato,
riferimento brand corretto, etc.):

Inserisci nel brief, prima delle ricevute:

```
Override: <gate>: <motivo breve>
```

Esempio:
```
Override: voice: "Trasformazione" è parola-chiave del brand, non copywriter tell
```

Il reviewer lo rispetta e passa a `ships` con nota. L'override resta nella
storia del brief per audit.

---

## Manutenzione

- Modifica pattern voice: qui, sezione "Lista pattern". Il codice Python li
  legge/genera da questo file.
- Nuovo pattern non-italiano: aggiungi in `04-bilingual-it-us.md` + linka qui.
- Nuova soglia: qui, non nel codice.
- Nuova regola hook: `01-hook-system.md` + aggiorna Gate 2 sopra.
- Nuova regola format: `03-output-contract.md` + aggiorna Gate 1 sopra.

Vedi `UPDATE-MAP.md` per la governance completa.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
