# Changelog

Tutte le modifiche notabili a questa skill sono registrate qui.

Formato: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versionamento: [Semantic Versioning](https://semver.org/lang/it/).

Regola dei numeri:
- **MAJOR** (1.x.x → 2.0.0) — breaking change nel workflow o nel contratto di output.
  Serve migration.
- **MINOR** (x.1.x → x.2.0) — nuova feature retro-compatibile (nuovo format, nuovo
  linter, nuovo reference).
- **PATCH** (x.x.1 → x.x.2) — bugfix, typo, tuning soglia linter, aggiornamento
  fixture.

---

## [Unreleased]

### Added
- feat(voice): nuova regola sulla persona del parlato. Prima di scrivere si
  definisce chi parla in base a format e interprete: brand, founder, narratore,
  creator che testimonia davvero o creator che interpreta un cliente. La prima
  persona non e' piu' il default, ma una scelta coerente con il ruolo. Le
  esperienze inventate non possono essere presentate come recensioni reali.
  Allineati `SKILL.md`, `AGENTS.md`, `references/02-writing-principles.md` §1.1
  e `UPDATE-MAP.md`. `[dichiarato: Matteo, 2026-10-08]`
- feat(parlato): nuovo `references/10-parlato-ritmo-e-ponti.md`, il file della
  continuita' del discorso. Dieci regole: la domanda unica prima di ogni blocco,
  fasi narrative con giunture che non si sentono, lista bianca dei ponti ammessi,
  divieto di aforismi nel body, alternanza delle lunghezze, struttura interna del
  blocco, frammento singolo libero, passivo e nominale fuori dal parlato, termini
  tecnici sempre spiegati, test di lettura ad alta voce.
  `[dichiarato: Matteo, 2026-09-25]`
- feat(parlato): lista bianca dei ponti (`Senti,`, `Guarda,`, `E sai qual e' il
  punto?`, `E li' e' dove cambia tutto.` e le altre 12) esente dai pattern
  `signposted transition` e `rhetorical self-question`, in
  `07-review-gates.md` e in `scripts/voice-lint.py`.
- feat(parlato): sei non-negoziabili nuovi in `SKILL.md` e `AGENTS.md` (discorso
  non elenco, niente aforismi, ritmo alternato, passivo fuori dal parlato,
  lettura ad alta voce obbligatoria, soglia dei frammenti a tre di fila).
- feat(parlato): il test di lettura ad alta voce diventa il passo 0 del QA e
  lascia la riga `Lettura ad alta voce: eseguita su N blocchi, M riscritti` nella
  ricevuta Voice. Senza quella riga il brief non e' consegnabile.
- feat(output-contract): tag Selling Block `Villain` nel gruppo apertura, per la
  fase del nemico comune che il workflow usava senza avere un tag.
- feat(anti-patterns): AP-21 (aforisma nel body), AP-22 (blocchi corretti ma
  scollegati), AP-23 (passivo e nominalizzazione), AP-24 (ritmo piatto).
- feat(voice-lint): quattro check nuovi come warning che non contano nella
  density e non bloccano: aforisma per eco, ritmo piatto, passivo e
  nominalizzazione, ponte mancante tra i blocchi (check di documento).
- test: fixture `06-ponti-ritmo-clean.md`, i ponti della lista bianca e il
  frammento singolo devono restare puliti. Eval 15/15.

### Changed
- `references/02-writing-principles.md` principio 21: la soglia del vincolo di
  montaggio passa dal frammento singolo alla serie da tre di fila.
- `references/formats-guide.md`: rimossi i 31 trattini lunghi dal corpo del file
  (restano le due righe in cui il trattino e' l'oggetto del discorso), riscritti
  gli esempi che insegnavano ponti vietati (`Ecco la verita':`) e triplette
  bilanciate (`e' efficace, e' sicuro, e' garantito`).
- `SKILL.md`: `references/08-anti-patterns.md` era assente dalla mappa dei
  reference file, quindi una sessione che si fidava della mappa non lo apriva mai.
- feat(voice): collegamento esplicito allo standard anti AI-slop del Brain
  (`landi-system/docs/anti-ai-slop-writing-standard.md`) in `SKILL.md`,
  `AGENTS.md`, `02-writing-principles.md` e `UPDATE-MAP.md`, cosi' un
  aggiornamento dello standard sa quali file toccare qui.
- feat(voice): principi 20-23 in `02-writing-principles.md`: afferma invece di
  comandare, frammenti validi solo se il montaggio li regge, varieta' degli
  attacchi di frase nel body, enfasi come marca di delivery nelle Note per
  Editor con obbligo delle due versioni finche' Matteo non fissa la linea.
- feat(voice): anti-pattern AP-17 (comando), AP-18 (frammenti senza montaggio),
  AP-19 (falso contrasto completo), AP-20 (numeri di risultato nudi).
- feat(voice-lint): pattern `false contrast` e `command scaffold`, con voci nel
  Gate 3 di `07-review-gates.md`. Frammenti, attacchi ed enfasi restano al
  reviewer.
- test: fixture `05-command-contrast-slop.md` (9 flag attesi, CTA, istruzione
  d'uso e obiezione nominata restano pulite). Eval 14/14.
- feat(formats): unify Podcast Reale/Fake into single format
- feat(hooks): `01-hook-system.md` §4, nuova sezione "Come scrivere il testo
  on-screen" (da una revisione manuale verificata indipendentemente): nomina
  l'oggetto concreto non il meccanismo tecnico, formula causa-effetto per
  overlay legati a un oggetto specifico, ancora tematica prima di ogni
  domanda retorica, stesso lessico verbatim del parlato, coerenza tra
  overlay dell'hook e scena Body a cui si aggancia quando annotato con
  punto di ingresso (§8a/8b).
- feat(hooks): nuovo `references/hook-swipe-file.md`, swipe file hook in
  inglese (dialogo per format Podcast/Street Interview/Skit/POV/Organic +
  ~450 formule per categoria General/Pet/Jewelry/Fashion/Home/Beauty/
  Wellness), con sintesi dei meccanismi psicologici sottostanti per scrivere
  hook italiani nativi (non tradotti alla lettera). Aggiunte 3 tecniche
  nuove in `01-hook-system.md` §4: filtro esplicito come hook intero,
  target del regalo (buyer diverso da chi usa), GRWM come veicolo per la
  curiosita'. Mappa reference aggiornata in `SKILL.md` e `AGENTS.md`.
- feat(dialogue): tecniche avanzate per dialoghi a botta e risposta in
  `formats-guide.md` §5.7 (avversativa in apertura turno, claim specifico vs
  lessico di personaggio, nota di delivery per imperfezioni fonetiche, tag
  retorico per format comici, coerenza lessico/meccanismo reale, cambio di
  persona segnalato nel visual, dettagli anagrafici/numerici verificati,
  completezza dei pronomi nel parlato); regola di continuita' multi-speaker
  hook to body in `01-hook-system.md` §8a; principi 18-19 in
  `02-writing-principles.md` (lessico preciso come voce di personaggio,
  delivery note per imperfezioni scritte foneticamente)

### Changed
- Gate Grounding: i numeri/percentuali senza fonte attivano il **claim flag**
  (scrive versione sicura + aggressiva + eventuale versione come testimonianza,
  scelta all'utente) invece del bounce silenzioso. Categorie regolate flaggate
  sempre, nessuno stop duro. Vedi `docs/claim-strategy.md` del Brain.
- Il Voice gate ora include test del neofita, category entry point esplicito,
  impalcatura generica, specificita' apparente e residui conversazionali.
- La transcreation IT/US deve reggere senza l'originale e usare lessico di
  categoria nativo, non limitarsi alla correttezza grammaticale.
- Il trattino lungo resta sempre vietato. Il trattino medio e' vietato come
  punteggiatura, ma ammesso in intervalli e coppie reali.

### Fixed
- —

---

## [1.2.0] — 2026-08-27

### Added
- **`references/02-writing-principles.md` §11-14** — quattro principi nuovi:
  - §11 Concretezza prima delle astrazioni: nomina gesto/oggetto/risultato osservabile invece di "esperienza", "trasformazione", "soluzione".
  - §12 Chiarezza prima dell'eleganza: frasi semplici, una idea per volta, non dimostrare bravura.
  - §13 Quota controllata di imperfezione: ripetizioni, frammenti, "quindi"/"cioe'"/"ok" deliberati rendono il parlato credibile; grammatica troppo uniforme e' segnale AI.
  - §14 Testo pulito ma generico e' comunque un fallimento: linter misura density AI, non certifica voce; serve piu' corpus verbatim.

---

## [1.1.0] — 2026-08-22

### Added
- Sezione **"Quando NON usare questa skill"** in `SKILL.md` — anti-trigger espliciti
  per evitare attivazione su blog post, copy statici, email, landing SEO, script
  >90s, lingue diverse da IT/US-EN, post-production, media planning. Include
  edge case (attiva con warning).
- **`references/08-anti-patterns.md`** — galleria di 12 anti-pattern (em-dash, hook
  simili, numeri inventati, brand-name-3s, on-screen literal, AI voice tells,
  puffery, CTA generica, founder senza founder, testo scritto vs parlato, verbatim
  come slogan, format sbagliato). Ogni voce con `❌ / ✅ / 🔍`.
- **`.github/workflows/evals.yml`** — CI GitHub Actions che lancia `evals/run.py` a
  ogni push/PR sui path skill-critici (scripts, fixtures, evals, references,
  SKILL.md).
- **`CHANGELOG.md`** — questo file, con SemVer.
- **`CONTRIBUTING.md`** — guida per contributor futuri (branching, commit style,
  evals pre-push, come aggiungere reference/format/fixture/anti-pattern/linter).

### Changed
- `README.md` — rimossi riferimenti a `PORTABLE-master-prompt.md` e
  `PORTABLE-BUNDLE.md` (deprecati), aggiunta sezione "Bundle per LLM esterni" che
  rimanda a `bundle-skill.sh` nel brain, aggiunte referenze a CHANGELOG e
  CONTRIBUTING.

---

## [1.0.1] — 2026-08-21

### Changed
- Split di `references/formats-guide.md` (5632 → 2844 righe). La Parte 4 (dettaglio
  format) e' stata spostata in `references/formats/*.md` (14 file, uno per
  format). Aggiornato `references/05-format-selector.md` con nota "carica SOLO il
  file del format scelto".
- `SKILL.md` frontmatter description compattato (15 → 7 righe).

### Added
- `fixtures/` con 3 fixture gold standard:
  - `01-ugc-clean.md` — UGC well-formed (expected: all pass).
  - `02-vsl-slop.md` — VSL rotto intenzionalmente (expected: 4 linter fail).
  - `03-founder-mixed.md` — Founder con 2 warning intenzionali (expected: pass con
    note).
- `evals/README.md` + `evals/run.py` — regression suite. `python3 evals/run.py`
  ritorna "✓ 12/12 checks passed".

### Removed
- `PORTABLE-master-prompt.md` e `PORTABLE-BUNDLE.md` — sostituiti da
  `bundle-skill.sh` nel brain `landi-brain` (genera prompt on-demand, no
  duplicazione).

---

## [1.0.0] — 2026-08-20

### Added
- Prima release skill `video-ads-script-writer` (poi rinominata skill repo su
  GitHub a `landi-video-scriptwriter`).
- `SKILL.md` (196 righe) — workflow passo-passo Claude Code.
- `AGENTS.md` — variante Codex CLI del workflow.
- `references/` (10 file):
  - `00-brand-lookup.md` — come caricare brand-context.
  - `01-hook-system.md` — teoria hook a 4 layer.
  - `02-writing-principles.md` — regole anti-AI writing.
  - `03-output-contract.md` — specifica formato output tabellare.
  - `04-bilingual-it-us.md` — regole IT/US-EN.
  - `05-format-selector.md` — quale format quando.
  - `06-broll-generation.md` — hint visivi.
  - `07-review-gates.md` — policy 4-gate QA.
  - `formats-guide.md` — parti 1-3 e 5-6 (strategia, stile, sintassi, blocchi di
    vendita, framework).
  - `hook-types-library.md` — 20 archetipi di hook.
- `scripts/` (4 linter Python):
  - `format-lint.py` — contratto tabellare.
  - `hook-lint.py` — regole hook.
  - `voice-lint.py` — AI-writing tells.
  - `grounding-check.py` — fact vs flavor.
- `.claude/agents/`:
  - `voice-reviewer-landi.md` — reviewer indipendente voice.
  - `grounding-reviewer-landi.md` — reviewer indipendente grounding.
- `.claude/hooks/gate-check.py` — Stop hook advisory mode.
- `.claude/settings.json` — wiring hook.
- `.gitignore` — esclude brand-context locale, runs/, settings.local.json.
