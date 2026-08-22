# Mappa Dipendenze

Quando modifichi un reference file, questi file dipendenti devono essere aggiornati automaticamente (se rilevante per il contenuto).

---

## Reference Files → Dipendenti

| Reference File | Dipendenti | Note |
|---|---|---|
| `references/00-brand-lookup.md` | SKILL.md (step 2), PORTABLE-BUNDLE.md, PORTABLE-master-prompt.md, AGENTS.md | Lookup, manifest, priorità verbatim |
| `references/01-hook-system.md` | SKILL.md (step 5), PORTABLE-BUNDLE.md, PORTABLE-master-prompt.md, UPDATE-MAP.md, scripts/hook-lint.py, .claude/agents/voice-reviewer-landi.md | Sistema layer, tipi, archetipi, testo on-screen, ricombinazione |
| `references/02-writing-principles.md` | SKILL.md (non-negoziabili), PORTABLE-BUNDLE.md, PORTABLE-master-prompt.md, UPDATE-MAP.md, .claude/agents/voice-reviewer-landi.md | Scrittura parlata, anti-AI, E-R-C scoring, producibilità |
| `references/03-output-contract.md` | SKILL.md (step 7), PORTABLE-BUNDLE.md, PORTABLE-master-prompt.md, UPDATE-MAP.md, scripts/format-lint.py, .claude/agents/voice-reviewer-landi.md | Tabelle, colonne, selling block, comprensibilità |
| `references/04-bilingual-it-us.md` | SKILL.md (step 1), PORTABLE-BUNDLE.md, PORTABLE-master-prompt.md, UPDATE-MAP.md, scripts/voice-lint.py | Regole italiano/inglese US, keyword, slang |
| `references/05-format-selector.md` | SKILL.md (step 4), PORTABLE-BUNDLE.md, PORTABLE-master-prompt.md, UPDATE-MAP.md | 15 format, quando usare, durata, costo |
| `references/06-broll-generation.md` | SKILL.md (step 7), PORTABLE-BUNDLE.md, PORTABLE-master-prompt.md, UPDATE-MAP.md | Indicazioni B-roll, prompt AI |
| `references/07-review-gates.md` | SKILL.md (step 8), PORTABLE-BUNDLE.md, PORTABLE-master-prompt.md, UPDATE-MAP.md, scripts/format-lint.py, scripts/hook-lint.py, scripts/voice-lint.py, scripts/grounding-check.py, .claude/agents/voice-reviewer-landi.md, .claude/agents/grounding-reviewer-landi.md, .claude/hooks/gate-check.py | Gate regole, soglie, pattern voice-lint, fact-vs-flavor |
| `references/09-standard-broll-library.md` | SKILL.md (modalita library), AGENTS.md, UPDATE-MAP.md, `build-broll-library` | Libreria standard senza concept, naming e priorita freestyle |
| `references/formats-guide.md` | PORTABLE-BUNDLE.md (se appendice completa), PORTABLE-master-prompt.md (se appendice) | Guida strategia/stile per i 15 format (file esterno, NON incluso nei PORTABLE per size) |

---

## Orchestrazione Files

### SKILL.md
- Contiene il workflow (step 1-8)
- Cita tutti i reference file (00-07)
- **Aggiorna quando:** un reference file cambia le regole del workflow generale
- **Sezioni chiave:** frontmatter `description`, workflow numerato, "I non-negoziabili"

### PORTABLE-BUNDLE.md
- Master prompt + appendice con 00-07 completo
- **Aggiorna quando:** modifichi 00-07 (propaga la sezione rilevante in appendice)
- **Aggiorna anche:** il riassunto nel master prompt (all'inizio) se la modifica è strutturale

### PORTABLE-master-prompt.md
- Master prompt soltanto (no appendice)
- **Aggiorna quando:** modifichi un reference file con impatto sul prompt di sistema
- **Sezioni:** RUOLO, REGOLA SORGENTE, NON-NEGOZIABILI, WORKFLOW (numerato)

### UPDATE-MAP.md
- Mappa di quali file toccare per quale modifica
- **Aggiorna quando:** crei un nuovo reference file o cambi la categorizzazione di una modifica
- **Tabella "Dove aggiornare cosa":** aggiungi riga se il reference file è nuovo

### AGENTS.md
- Elenca gli agent custom (.claude/agents/*.md)
- **Aggiorna quando:** credi un nuovo agent o cambiano le responsabilità di uno
- Poco dipendente dai reference file

### README.md
- Overview pubblico
- **Aggiorna quando:** l'architettura o il workflow cambia radicalmente
- Non dipende direttamente dai reference file

---

## Scripts Python

### scripts/format-lint.py
- Linter delle tabelle (contratto output)
- **Aggiorna quando:** modifichi `03-output-contract.md` o `07-review-gates.md` (Gate 1)
- **Cosa controllare:** header tabelle, CTA, placeholder, Testo on-screen syntax

### scripts/hook-lint.py
- Linter regole hook
- **Aggiorna quando:** modifichi `01-hook-system.md` o `07-review-gates.md` (Gate 2)
- **Cosa controllare:** numero hook, testo on-screen, diversità, aggancio Body

### scripts/voice-lint.py
- Linter anti-AI, tell detection
- **Aggiorna quando:** modifichi `02-writing-principles.md` o `07-review-gates.md` (Gate 3)
- **Cosa controllare:** lista pattern vocabolario flaggato, regex, densità

### scripts/grounding-check.py
- Linter fact-vs-flavor
- **Aggiorna quando:** modifichi `00-brand-lookup.md` o `07-review-gates.md` (Gate 4)
- **Cosa controllare:** brand-context lookup, verbatim matching, fact checking

---

## Agents Custom

### .claude/agents/voice-reviewer-landi.md
- Reviewer indipendente per Gate 3 (Voice)
- **Aggiorna quando:** modifichi `02-writing-principles.md`, `01-hook-system.md`, o `07-review-gates.md` (soglie voice)
- **Cosa controllare:** istruzioni anti-AI, E-R-C scoring, lista pattern

### .claude/agents/grounding-reviewer-landi.md
- Reviewer indipendente per Gate 4 (Grounding)
- **Aggiorna quando:** modifichi `00-brand-lookup.md` o `07-review-gates.md` (fact-vs-flavor)
- **Cosa controllare:** istruzioni fact-check, verbatim lookup, regola cardinale

---

## Stop Hook

### .claude/hooks/gate-check.py
- Advisory hook (controlla receipts QA assenti)
- **Aggiorna quando:** modifichi `07-review-gates.md` (soprattutto soglie o modalità enforcement)
- **Cosa controllare:** output-shape detection, decision logic, messaggio advisory

---

## Flusso di Modifica Consigliato

1. **Brainstorm:** Discuti il miglioramento (niente modifiche file).
2. **Richiesta esplicita:** "Modifica X in `references/YY.md`".
3. **Io eseguo:**
   - Modifica il reference file
   - Consulto questa tabella DEPENDENCIES.md
   - Aggiorno automaticamente tutti i dipendenti rilevanti
   - Niente domande, niente "vuoi che aggiorno anche...?"
4. **Verifica:** Rileggi gli aggiornamenti se serve.

---

*Creato per evitare modifiche incomplete e garantire propagazione automatica.*
