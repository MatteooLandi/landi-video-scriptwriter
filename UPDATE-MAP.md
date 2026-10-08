# Mappa di Aggiornamento

Risposta breve alla domanda "cosa posso aggiornare?": **tutto**. Niente e'
bloccato. L'architettura a file separati esiste proprio per farti modificare una
cosa senza toccarne altre.

Distinzione utile:
- **Modifica locale:** tocchi un solo file, zero effetti sul resto.
- **Modifica strutturale:** tocchi l'orchestrazione in `SKILL.md` (il workflow, i
  trigger, i non-negoziabili). Si puo' fare, ma cambia il comportamento generale,
  quindi valutala con piu' attenzione.

---

## Dove aggiornare cosa

| Vuoi aggiornare... | Apri | Tipo |
|---|---|---|
| Un format esistente (struttura, esempio, do/don't) | `references/formats-guide.md` | locale |
| Aggiungere un nuovo format | `references/formats-guide.md` + una riga in `references/05-format-selector.md` | locale |
| Regole/logiche degli hook | `references/01-hook-system.md` (e `hook-types-library.md` per i tipi) | locale |
| Swipe file hook (formule EN, principi IT) | `references/hook-swipe-file.md` | `01-hook-system.md` §4 se introduce una tecnica nuova, `SKILL.md`/`AGENTS.md` mappa reference |
| Regole di scrittura, anti-AI, scoring, produzione | `references/02-writing-principles.md` | locale |
| Voce e persona del parlato (brand, founder, narratore, creator cliente o attore) | `references/02-writing-principles.md` §1.1 | `SKILL.md` e `AGENTS.md` se cambia il vincolo generale |
| Continuita' del discorso, giunture tra blocchi, ritmo, aforismi, passivo, struttura del blocco, lettura ad alta voce | `references/10-parlato-ritmo-e-ponti.md` | `SKILL.md` non-negoziabili, `AGENTS.md`, `references/07-review-gates.md`, `references/08-anti-patterns.md`, `scripts/voice-lint.py`, fixture `06-ponti-ritmo-clean.md` |
| Lista bianca dei ponti ammessi nel parlato | `references/10-parlato-ritmo-e-ponti.md` R3 | `references/07-review-gates.md` sez. Lista pattern + `APPROVED_BRIDGES` in `scripts/voice-lint.py`, che devono restare identici |
| Galleria degli anti-pattern (AP-NN) | `references/08-anti-patterns.md` | `references/07-review-gates.md`, `scripts/voice-lint.py` se il pattern e' deterministico, fixture in `fixtures/` |
| Standard anti AI-slop del Brain aggiornato (`landi-system/docs/anti-ai-slop-writing-standard.md`) | `references/02-writing-principles.md` (principi 15-17 e 20-23) | `SKILL.md` non-negoziabili, `AGENTS.md`, `references/08-anti-patterns.md`, `references/07-review-gates.md`, `scripts/voice-lint.py` per i pattern deterministici, fixture in `fixtures/` |
| Category entry point, formule generiche, residui assistente | `references/08-anti-patterns.md` | `SKILL.md`, `AGENTS.md`, `02-writing-principles.md`, `07-review-gates.md`, reviewer Voice, `scripts/voice-lint.py`, fixture |
| Formato di output, colonne, selling block | `references/03-output-contract.md` | locale |
| Comprensibilita' istruzioni produttive, Flesch-Vacca, regole visual/editor | `references/03-output-contract.md` sez. "Comprensibilita'" | locale |
| Formattazione speciale per un certo format | blocco `Regole di formattazione specifiche` nel format + nota in `03-output-contract.md` | locale |
| Regole italiano/inglese US, keyword, slang | `references/04-bilingual-it-us.md` | locale |
| Qualita' transcreation IT/US | `references/04-bilingual-it-us.md` | `02-writing-principles.md`, `07-review-gates.md`, reviewer Voice, `scripts/voice-lint.py` per pattern ad alta precisione |
| Struttura brand, manifest, learnings, priorità verbatim | `references/00-brand-lookup.md` | locale |
| B-roll (indicazioni o prompt AI) | `references/06-broll-generation.md` | locale |
| Libreria B-roll standard del brand | `references/09-standard-broll-library.md` | locale |
| Ricerca web, fonte attribution, fallback info mancanti | questo file (`SKILL.md` step 2 sez. d + `AGENTS.md` mirror) | locale |
| Gate review, lista pattern voice, soglie, fact-vs-flavor | `references/07-review-gates.md` | locale (i linter Python leggono da qui) |
| Claim flag (numeri/% senza fonte) | `references/07-review-gates.md` §Gate 4 + `docs/claim-strategy.md` (Brain) | reviewer Grounding, receipt `## Claim Flag` |
| Linter meccanici (parole flaggate, pattern regex) | `scripts/{voice,hook,format}-lint.py` — sincronizzare con `07-review-gates.md` | locale |
| Reviewer agent (voice/grounding) | `.claude/agents/voice-reviewer-landi.md`, `.claude/agents/grounding-reviewer-landi.md` | locale |
| Enforcement Stop hook (advisory ↔ bloccante) | `.claude/hooks/gate-check.py` — vedi `07-review-gates.md` sez "Upgrade a bloccante" | strutturale |
| Come si attiva la skill (trigger, parole affini) | `SKILL.md` (frontmatter `description`) | strutturale |
| Il workflow o i non-negoziabili | `SKILL.md` | strutturale |
| La versione per ChatGPT/Gemini | `PORTABLE-master-prompt.md` | locale |

Regola pratica: dopo aver modificato un reference file, se hai cambiato qualcosa
che riguarda il workflow generale, riallinea `SKILL.md` e
`PORTABLE-master-prompt.md`.

---

## Aggiungere un nuovo format (checklist)

1. Scrivi la sezione nel formats-guide (Cos'e', Perche' funziona, Come funziona,
   Struttura, Esempio, Do's & Don'ts, chi interpreta).
2. Aggiungi una riga in `05-format-selector.md` (quando usarlo, chi interpreta,
   costo, durata, sezione).
3. Se richiede una formattazione di output diversa, aggiungi il blocco
   `Regole di formattazione specifiche`.

---

## Miglioramento continuo (da performance e feedback)

La skill e' pensata per migliorare con i tuoi dati reali:

1. Condividi uno script con la sua performance o un feedback.
2. La skill estrae solo cio' che e' generalizzabile: pattern ricorrenti,
   opportunita' strategiche, warning.
3. Propone di scriverlo in `learnings.md` (brand o prodotto) secondo lo schema in
   `00-brand-lookup.md`, con changelog.
4. Se un apprendimento e' cosi' solido da diventare regola, si promuove nel
   reference file giusto (es. una regola hook in `01-hook-system.md`).

Cosi' i learnings restano puliti (niente copie, niente ripetizioni) e le regole
evolvono in modo tracciato.

---

## Cosa NON e' "non aggiornabile", ma va maneggiato con cura

Nessun file e' immutabile. Gli unici punti che, se cambi, hanno effetti a catena:
- i **trigger** in `SKILL.md` (se li tocchi male, la skill smette di attivarsi
  quando serve o si attiva a sproposito);
- i **non-negoziabili** (sono i vincoli che tengono coerente ogni output);
- il **contratto di output** (se lo cambi, cambiano tutti i brief prodotti).
Puoi modificarli quando vuoi: sappi solo che si riflettono su tutto.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
