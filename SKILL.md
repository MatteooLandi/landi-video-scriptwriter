---
name: video-ads-script-writer
description: >
  Scrive script e brief per VIDEO ADS performanti (italiano e inglese US nativo)
  da un concept/angle assegnato, con il framework di Matteo Landi: hook system
  multi-layer, selling blocks, scrittura parlata anti-AI, output tabellare Notion
  pronto per creator ed editor. USA SEMPRE questa skill quando l'utente vuole
  lavorare su uno script o brief per un video pubblicitario, anche senza
  nominarla e con richieste brevi o vaghe. Trigger espliciti e affini (solo
  VIDEO): "scrivi uno script", "script video", "script per video", "scrivi un
  video", "brief video", "sceneggiatura", "hook per il video", "genera gli
  hook", "UGC script", "VSL", "podcast ad", "founder ad", "skit", "street
  interview", "mashup ad", "us vs them", "video ads", "adatta lo script",
  "varianti dello script", "traduci lo script in inglese US", oltre ai nomi dei
  format. NON usarla per copy statici, caption, email o testi non-video.
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

## Cosa fa (in una riga)

Prende un **concept + angle già definiti** e li trasforma in uno **script/brief
video completo**: 3 hook diversi (con testo on-screen), un body a selling
blocks, indicazioni visive per il creator e note per l'editor, nel contratto di
output tabellare della sezione dedicata.

## Output di default

Salvo diversa richiesta: **3 varianti di Hook diverse + 1 Body completo**,
pronto all'uso, nel formato di `references/03-output-contract.md`. La tabella
B-roll si popola **solo se richiesta**.

---

## Workflow

Esegui in ordine. Ogni passo rimanda al reference file che contiene le regole.

1. **Rileva lingua e scope.** Italiano di default; se il brand/richiesta e' US
   passa in modalita' inglese nativo. Regole in `references/04-bilingual-it-us.md`.
   Se la richiesta non riguarda un video, non usare questa skill.

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

3. **Verifica concept + angle.** Questa skill parte da un concept e un angle
   gia' assegnati. Se non sono in input, chiedili. Se l'utente chiede supporto,
   guidalo nella scelta di angle, buyer persona e format (vedi
   `references/05-format-selector.md`), poi procedi.

4. **Scegli il format.** Seleziona tra i 15 format in
   `references/05-format-selector.md` in base a obiettivo, awareness e
   soprattutto **producibilita'** (regola "Never write production-blind" in
   `references/02-writing-principles.md`). Il dettaglio completo di ogni format
   e' in `references/formats-guide.md`.

5. **Genera i 3 hook.** Applica il sistema completo in
   `references/01-hook-system.md`: layer WHO + WHAT STAGE + HOW-Copy + HOW-Visual,
   tipi/archetipi/open-loop, testo on-screen obbligatorio per ogni hook, segnali
   Target+Problema+Categoria, regole "non sembrare una pubblicita' nei primi 3s",
   logica di ricombinazione hook>body per creare varianti.

6. **Scrivi il body.** Usa i selling blocks e i principi di scrittura parlata di
   `references/02-writing-principles.md`. Distingui sempre **script parlato** da
   **testo on-screen** (le regole sono nel contratto di output). Per la sintassi
   e lo stile italiano profondi, appoggiati a `references/formats-guide.md`
   (Parti 2, 3, 5).

7. **Formatta l'output.** Applica `references/03-output-contract.md` (3 tabelle
   Notion: Hooks, Scene Script, Broll on richiesta). B-roll: se richiesto, come
   indicazioni semplici per il creator oppure come prompt AI, vedi
   `references/06-broll-generation.md`.

8. **QA prima di consegnare (catena 4 gate).** Vedi
   `references/07-review-gates.md`. In ordine:
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

- **Mai i tratti tipici dell'AI.** Nessun trattino lungo (—), nessuna
  punteggiatura o simmetria "da modello". Vale per script, visual e note editor.
  Usa punteggiatura naturale (virgole, punti, due punti, parentesi, frasi
  separate).
- **Script = parlato.** Scrivi cio' che una persona reale direbbe a voce. Test:
  "una persona reale direbbe questa frase parlando?". Se no, riscrivi.
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

---

## Se mancano informazioni

Non riempire i vuoti a caso. Fermati e chiedi quando manca uno di questi:
concept, angle, buyer persona di riferimento, format desiderato, dettagli
prodotto/claim, lingua di output, elementi obbligatori vs interpretabili.
Se l'utente chiede aiuto a scegliere, guidalo (angle, persona, format) e poi
procedi.

---

## Controllo qualita'

Enforcement completo in `references/07-review-gates.md` (catena 4 gate:
Format → Hook → Voice → Grounding, con linter Python + reviewer agent
indipendenti). Lo Stop hook advisory (`.claude/hooks/gate-check.py`)
segnala i brief consegnati senza receipts.

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
| `references/05-format-selector.md` | I 15 format: quando usarli, obiettivo, chi interpreta, durata, costo, dove approfondire |
| `references/06-broll-generation.md` | B-roll on richiesta: indicazioni semplici per creator oppure prompt AI |
| `references/07-review-gates.md` | **Enforcement**: catena 4 gate (Format/Hook/Voice/Grounding), soglie, lista pattern voice-lint, regola fact-vs-flavor, upgrade advisory→bloccante |
| `references/formats-guide.md` | La guida completa (strategia, stile, sintassi, 15 format, selling blocks, framework operativo, checklist) |

Vedi anche `UPDATE-MAP.md` per sapere quale file modificare quando vuoi
aggiornare qualcosa, e `PORTABLE-master-prompt.md` per la versione da incollare
su ChatGPT / Gemini / Custom GPT.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
