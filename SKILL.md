---
name: video-ads-script-writer
description: >
  Scrive script e brief per video ads (IT + EN US) da concept/angle assegnato,
  con framework Matteo Landi: hook multi-layer, selling blocks, scrittura
  parlata anti-AI, output tabellare pronto per creator ed editor. Genera anche
  librerie B-roll standard quando richieste da build-broll-library. Attiva su
  richieste di script, hook, brief video, scene creator, shot list B-roll,
  sceneggiatura, varianti, traduzione EN o nomi dei 14 format supportati. NON
  usare per copy statici, caption o email.
---

# Video Ads Script Writer

Skill per scrivere script e brief di **video ads** in italiano (principale) e
inglese US (secondario), con il framework di Matteo Landi. Produce output
tabellari pronti per la produzione, non semplici bozze di testo.

> **Regola sorgente (vincolante).** Questa skill usa i propri file di reference
> e gli input dell'utente. Non inventa dati mancanti: se manca un'informazione
> necessaria (concept, angle, buyer persona, format, dettagli prodotto), si
> ferma e la chiede. Vedi "Se mancano informazioni".

---

## Modalita

1. **Script video** (default): prende un concept + angle gia definiti e li
   trasforma in 3 hook, un body completo e indicazioni produttive.
2. **Libreria B-roll standard**: costruisce la footage library permanente del
   brand, indipendente da un concept, con almeno cinque scene per categoria
   narrativa. Si usa quando la invoca `build-broll-library`.

## Output di default

Salvo diversa richiesta: **3 varianti di Hook diverse + 1 Body completo**,
pronto all'uso, nel formato di `references/03-output-contract.md`. La tabella
B-roll si popola **solo se richiesta**.

Eccezione: in modalita `libreria B-roll standard`, applica esclusivamente
`references/09-standard-broll-library.md`.

---

## Quando NON usare questa skill

Questa skill genera **script/brief per video ads short-form** (UGC, VSL, Founder
Ad, Skit, Mashup, Us-vs-Them, ecc., 15-90s). NON attivarla quando la richiesta
riguarda:

- **Blog post, articoli, contenuti long-form scritti** — questa skill assume
  cadenza parlata, non prosa scritta.
- **Copy statici per ad** (headline + subhead, senza script) — craft diverso,
  nessun hook system, nessun B-roll.
- **Email marketing / sequenze DM** — struttura e pacing diversi.
- **Landing page SEO / product description e-commerce** — scritte per la
  ricerca, non per il parlato.
- **Caption organiche non-ad** (post social organici puri) — intent diverso, no
  framing direct-response.
- **Script video long-form > 90s** (documentario, tutorial, podcast, webinar) —
  la format library di questa skill copre solo ads short-form.
- **Lingue diverse da IT o US-EN** — `references/04-bilingual-it-us.md` copre
  solo queste due.
- **Post-production / editing brief timeline** — la skill produce script +
  hint B-roll, non timeline editoriali.
- **Strategia ads / media planning / segmentazione audience** — la skill
  esegue su un angle gia' definito, non pianifica la campagna.

La generazione della libreria scene per un brief prodotto finale e un'eccezione
esplicita: resta lavoro video-produttivo e segue il contratto dedicato.

**Se la richiesta rientra qui:** rispondi in chiaro "questa non e' una task da
video-ads-script-writer, la skill non aiuta" e suggerisci l'approccio giusto
(altra skill, lavoro manuale, altro tool). Non forzare il contratto di output
della skill sul tipo di contenuto sbagliato.

**Edge case — attiva con warning:**
- Script video 90-180s → attiva ma nota che la format library punta a durate
  minori, alcune sezioni possono non tornare.
- Script per contenuto organic-looking ma pagato → attiva (e' ancora un ad).
- Rewrite di script esistente → attiva, tratta l'input come draft e applica i
  review gate.

---

## Workflow

Esegui in ordine. Ogni passo rimanda al reference file che contiene le regole.

0. **Rileva la modalita.** Se la richiesta arriva da `build-broll-library` o
   chiede la footage library standard del brand, leggi
   `references/09-standard-broll-library.md`, produci quel solo output e salta i
   passaggi 3-8 del workflow script. Concept, angle e format non sono necessari
   in questa modalita.

1. **Rileva lingua e scope.** Italiano di default; se il brand/richiesta e' US
   passa in modalita' inglese nativo. Regole in `references/04-bilingual-it-us.md`.
   Se la richiesta non riguarda video o scene da registrare, non usare questa
   skill.

2. **Carica il contesto brand + info topic.** 
   a. Chiedi sempre: "carica brand-context / positioning / verbatim / topic
      specifics?" Se utente carica → usa quelli. Se dice no → ricerca web su
      autorizzazione (vedi sotto).
   b. Protocollo di lookup, schema `_manifest.md`, precedenza prodotto>brand:
      `references/00-brand-lookup.md`.
   c. **Priorità verbatim:** il linguaggio reale dell'audience (frasi da review,
      comment, call, surveys) e' la fonte primaria per hook, pain, obiezioni,
      desideri, claim, vocabolario. Sempre cercare verbatim reale; flavor
      illustrativo (frasi create che suonano customer) e' fallback.
   d. **Ricerca web (fallback):** se mancano info (brand sconosciuto, topic
      specifico richiede validazione numero/claim/trend/normativa), ricerca web
      automatica su autorizzazione utente. Se attivata: dichiara "ricerca web
      attivata per [X]" nel brief + allega `## Fonti ricerca web` in footer con
      URL delle fonti che hanno generato concetti nel copy.
   e. **Angle Villain/Us-vs-Them/Reframe, prova esterna sul villain:** non basta
      che il brand-context abbia prove sul prodotto (es. studio clinico). Se
      `{prodotto}-villain.md` manca o non contiene una prova indipendente
      (normativa, scientifica, giornalistica) sul villain stesso, non saltare
      l'archetipo Authority/Statistic per questo: segnalalo all'utente, oppure
      fai una ricerca web mirata (stessa autorizzazione del punto d) prima di
      chiudere gli hook. Una prova indipendente sul villain e' spesso l'hook
      piu' forte disponibile, non solo un dettaglio di contorno. Se il brand ha
      gia' un villain.md aggiornato (`/research-villain`), usa quello prima di
      ricercare da zero.

3. **Verifica concept + angle.** Questa skill parte da un concept e un angle
   gia' assegnati. Se non sono in input, chiedili. Se l'utente chiede supporto,
   guidalo nella scelta di angle, buyer persona e format (vedi
   `references/05-format-selector.md`), poi procedi.

4. **Scegli il format e chi parla.** Seleziona tra i 14 format in
   `references/05-format-selector.md` in base a obiettivo, awareness e
   soprattutto **producibilita'** (regola "Never write production-blind" in
   `references/02-writing-principles.md`). Definisci anche voce e persona
   grammaticale coerenti con format e interprete: brand, founder, narratore,
   creator che testimonia davvero o creator che interpreta un cliente. La prima
   persona non e' il default. Il dettaglio completo di ogni format e' in
   `references/formats/<nome-format>.md` — carica SOLO il file del format scelto,
   non tutti.

5. **Genera i 3 hook.** Applica il sistema completo in
   `references/01-hook-system.md`: layer WHO + WHAT STAGE + HOW-Copy + HOW-Visual,
   tipi/archetipi/open-loop, testo on-screen obbligatorio per ogni hook, segnali
   Target+Problema+Categoria, regole "non sembrare una pubblicita' nei primi 3s",
   logica di ricombinazione hook>body per creare varianti.

6. **Scrivi il body.** Usa i selling blocks e i principi di scrittura parlata di
   `references/02-writing-principles.md`, piu' i vincoli di continuita' e ritmo
   di `references/10-parlato-ritmo-e-ponti.md`: ogni blocco tiene il suo
   obiettivo narrativo e la sua prima frase nasce dall'ultima del blocco
   precedente. Distingui sempre **script parlato** da **testo on-screen** (le
   regole sono nel contratto di output). Per la sintassi italiana profonda, i
   selling blocks avanzati e i pattern di scrittura, appoggiati a
   `references/formats-guide.md` (Parti 2, 3, 5).

7. **Formatta l'output.** Applica `references/03-output-contract.md` (3 tabelle
   Notion: Hooks, Scene Script, Broll on richiesta). B-roll: se richiesto, come
   indicazioni semplici per il creator oppure come prompt AI, vedi
   `references/06-broll-generation.md`.

8. **QA prima di consegnare (catena 4 gate).** Vedi
   `references/07-review-gates.md`. In ordine:
   0. **Leggi ogni blocco ad alta voce**, una volta sola, senza fermarti
      (`references/10-parlato-ritmo-e-ponti.md` R10). Se ti blocchi su una
      parola, se devi riprendere fiato a meta' frase, se non ti viene naturale
      dirlo, riscrivi prima di far girare i linter. L'esito va nella ricevuta
      Voice come riga `Lettura ad alta voce: eseguita su N blocchi, M riscritti`.
   a. `python3 scripts/format-lint.py <draft>` — contratto tabelle. Bounce
      qui ferma la catena.
   b. `python3 scripts/hook-lint.py <draft> .` — regole hook (3 hook,
      testo on-screen, brand nei primi 3s, diversita').
   c. `python3 scripts/voice-lint.py <draft>` — tell AI meccanici (evidenza,
      non verdetto).
   d. `python3 scripts/grounding-check.py <draft> .` — fact vs flavor.
   e. Spawn agent `grounding-reviewer-landi` (contesto fresco).
   f. Spawn agent `voice-reviewer-landi` (contesto fresco).
   g. Se tutti `ships/grounded` → allega 4 receipts (`## Format Review`,
      `## Hook Review`, `## Voice Review`, `## Grounding Review`) in coda al
      brief, consegna.
   h. Se un gate bouncia → rerun mirato solo del gate affetto, torna al
      passo affetto.
   i. **Regola cardinale grounding:** flavor untraced non e' bounce, aggiungi
      label `Tono: illustrativo — non verbatim verificato`.
   j. Lo scoring E-R-C (Emotion, Relevance, Compression) resta parte del
      Voice Review, non ripeterlo separatamente.

---

## I non-negoziabili (valgono sempre, ovunque)

Questi vincono su tutto il resto. Dettaglio in `references/02-writing-principles.md`.

> **Fonte a monte.** Questi vincoli sono la specializzazione per il parlato
> dello standard di scrittura del Brain,
> `landi-system/docs/anti-ai-slop-writing-standard.md`. Quando lo standard
> cambia, i file da riallineare qui sono elencati in `UPDATE-MAP.md`. In caso
> di conflitto vale la versione piu' restrittiva.

- **Mai i tratti tipici dell'AI.** Nessun trattino lungo (—), nessuna
  punteggiatura o simmetria "da modello". Vale per script, visual e note editor.
  Usa punteggiatura naturale (virgole, punti, due punti, parentesi, frasi
  separate).
- **Category entry point esplicito quando regge il messaggio.** Se lo script
  dipende da un'occasione, un problema o un momento d'uso, nomina il contesto
  che permette anche a un neofita di capire "per cosa?". `Viaggio`, `percorso`,
  `esperienza`, `programmi`, `opzioni` e `dettagli` senza referente concreto non
  bastano.
- **Zero impalcatura da assistente.** Taglia formule intercambiabili come "un
  buon punto di partenza", "e' il momento giusto", "inizia a prendere forma",
  "dai un'occhiata" e promesse vaghe come "informazioni utili". Porta in primo
  piano occasione, oggetto e azione concreta.
- **Script = parlato.** Scrivi cio' che una persona reale direbbe a voce. Test:
  "una persona reale direbbe questa frase parlando?". Se no, riscrivi.
- **Persona del parlato scelta, non preimpostata.** Prima di scrivere definisci
  chi parla. Brand, narratore, founder, creator che testimonia e creator che
  interpreta un cliente non usano automaticamente la stessa persona. La prima
  persona vale solo quando e' coerente con un'esperienza attribuibile a chi la
  pronuncia; vedi `references/02-writing-principles.md` §1.1.
- **Script != testo on-screen.** Sono due cose diverse, non copiare l'uno
  nell'altro. Il testo on-screen va in "Note per Editor" con la dicitura
  "Testo on-screen:".
- **Hook = sempre testo on-screen.** Ogni hook ha un testo a schermo, diverso
  dal parlato.
- **Producibilita' prima di tutto.** Uno script performante che non si puo'
  produrre bene non e' performante. Considera creator, take, location, attori,
  materiale, B-roll, budget editing, turnaround.
- **Brief scannerizzabile.** Una informazione per riga. Niente paragrafoni,
  niente placeholder vuoti, niente aria da template auto-compilato.
- **Concept != Format.** Prima Message/Angle/Concept, poi si sceglie il format
  di esecuzione.
- **Afferma, non comandare.** Fuori dalla CTA e dalle istruzioni, niente
  impalcatura `Smetti di X, inizia a Y`. Chi parla dice cosa ha visto e cosa
  gli e' successo, e lascia la conclusione a chi guarda.
- **Frammenti solo se il montaggio li regge.** Il vincolo scatta da tre frasi
  senza verbo di fila ("Niente X. Niente Y. Niente Z."): passano se ogni
  frammento e' uno stacco, una clip o un beat dichiarato nelle note, altrimenti
  si ricuce. Un frammento singolo dentro una battuta e' libero.
- **Lo script e' un discorso, non un elenco.** Le fasi narrative restano (il
  problema, il nemico comune, lo screditamento delle alternative, la soluzione,
  il prodotto), ma le cuciture non si devono sentire: la prima frase di ogni
  blocco nasce dall'ultima del blocco precedente. Test: copri la colonna
  `Selling Block` e leggi il parlato di fila.
- **Niente aforismi nel body.** Le frasi a effetto, corte e simmetriche, che
  sembrano una citazione ("Il rischio non cresce con te. Si moltiplica per
  te.") restano fuori. Si sostituiscono col fatto concreto che volevano
  riassumere. Restano ammesse nella CTA che chiude un open loop e nel tag comico
  di un personaggio con quella voce.
- **Ritmo alternato.** Frasi brevi e frasi lunghe si alternano, dentro il blocco
  e tra blocchi. Quattro frasi della stessa misura di fila sono un metronomo.
- **Passivo e nominalizzazione fuori dal parlato.** "Viene applicato" e "la
  gestione comporta" sono forme scritte: rimetti il soggetto che agisce.
- **Test di lettura ad alta voce obbligatorio.** Nessuno script si consegna
  senza essere stato detto a voce, blocco per blocco. La ricevuta Voice lo
  dichiara.

---

## Se mancano informazioni

Non riempire i vuoti a caso. Fermati e chiedi quando manca uno di questi:
concept, angle, buyer persona di riferimento, format desiderato, dettagli
prodotto/claim, lingua di output, elementi obbligatori vs interpretabili.
Se l'utente chiede aiuto a scegliere, guidalo (angle, persona, format) e poi
procedi.

In modalita `libreria B-roll standard`, concept, angle e format non servono.
Sono invece obbligatori ricerca completata e brand context consolidato.

---

## Controllo qualita'

Enforcement completo in `references/07-review-gates.md` (catena 4 gate:
Format → Hook → Voice → Grounding, con linter Python + reviewer agent
indipendenti). Lo Stop hook advisory (`.claude/hooks/gate-check.py`)
segnala i brief consegnati senza receipts.

La ricevuta Voice contiene sempre la riga `Lettura ad alta voce: eseguita su N
blocchi, M riscritti`. Senza quella riga il brief non e' consegnabile, anche con
tutti i linter clean.

Sotto la catena, ogni script/concept deve comunque superare lo scoring E-R-C
applicato dal Voice Reviewer:

- **Emotion:** genera una reazione?
- **Relevance:** quella reazione porta naturalmente al prodotto?
- **Compression:** posso dire la stessa cosa con meno parole senza perdere forza?

E le checklist di `references/formats-guide.md` (sezione 6.2: Hook, Body,
Problema/Agitazione, Soluzione/Meccanismo, Benefici, Obiezioni, Prova
sociale, CTA, Sintassi italiana, Generale).

---

## Mappa dei reference file

| File | Contiene |
|---|---|
| `references/00-brand-lookup.md` | Come trovare e usare la knowledge di brand, manifest, precedenza prodotto>brand, uso dei verbatim, learnings |
| `references/01-hook-system.md` | Sistema hook completo: layer, tipi, archetipi, open loop, testo on-screen, ricombinazione hook>body |
| `references/02-writing-principles.md` | Scrittura parlata, anti-AI, script vs on-screen, scoring E-R-C, producibilita', concept!=format, verbatim-first |
| `references/03-output-contract.md` | Formato di output tabellare (3 tabelle Notion), colonne, selling block, note editor vs visual creator, override per-format |
| `references/04-bilingual-it-us.md` | Regole italiano nativo + inglese US nativo (keyword, unita', phrasal verb, slang, modali) |
| `references/05-format-selector.md` | I 14 format: quando usarli, obiettivo, chi interpreta, durata, costo, dove approfondire |
| `references/06-broll-generation.md` | B-roll on richiesta: indicazioni semplici per creator oppure prompt AI |
| `references/07-review-gates.md` | **Enforcement**: catena 4 gate (Format/Hook/Voice/Grounding), soglie, lista pattern voice-lint, regola fact-vs-flavor, upgrade advisory→bloccante |
| `references/08-anti-patterns.md` | Galleria degli output sbagliati (AP-01 ... AP-24) con ❌ / ✅ / 🔍. Check finale prima di consegnare e sorgente delle fixture di regressione |
| `references/09-standard-broll-library.md` | Modalita senza concept: libreria B-roll standard permanente del brand |
| `references/10-parlato-ritmo-e-ponti.md` | Continuita' del discorso: fasi narrative e giunture, lista bianca dei ponti, divieto aforismi, alternanza delle lunghezze, struttura del blocco, passivo e nominale, test di lettura ad alta voce |
| `references/formats-guide.md` | Strategia, stile, sintassi italiana, selling blocks avanzati, framework operativo, checklist. **Non contiene piu' i format** (spostati in `formats/`). |
| `references/formats/*.md` | Un file per format (14 file): Cos'e', Perche' funziona, Come funziona, Struttura, Esempio, Do's & Don'ts. Carica SOLO il file del format scelto. |
| `references/hook-types-library.md` | Libreria dei 20 tipi di hook (preset di apertura) |
| `references/hook-swipe-file.md` | Swipe file hook in inglese (dialogo per format + ~450 formule per categoria/nicchia) + principi psicologici estratti per scrivere hook italiani nativi (non tradotti alla lettera) |

Vedi anche `UPDATE-MAP.md` per sapere quale file modificare quando vuoi
aggiornare qualcosa. Per usare la skill su ChatGPT/Gemini, genera il bundle
con lo script `scripts/bundle-skill.sh` dal brain landi-brain.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
