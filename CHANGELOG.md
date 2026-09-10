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
- feat(formats): unify Podcast Reale/Fake into single format

### Changed
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
