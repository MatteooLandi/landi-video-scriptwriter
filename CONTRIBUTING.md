# Contributing

Guida per chi contribuisce alla skill `landi-video-scriptwriter`.

Al momento la skill ha un unico maintainer (Matteo). Questo documento serve per
quando il team crescera' — cosi' chi entra sa esattamente come muoversi senza
dover chiedere.

---

## Setup locale

```bash
# 1. Clona il repo
cd ~/Desktop/Claude
git clone https://github.com/MatteooLandi/landi-video-scriptwriter.git
cd landi-video-scriptwriter

# 2. Verifica che gli evals passino subito
python3 evals/run.py
# atteso: "✓ 12/12 check(s) passed"
```

Se gli evals non passano al primo colpo, apri issue prima di modificare
qualsiasi cosa.

---

## Branching

- **`main`** — sempre stabile. Ogni commit su main deve passare CI.
- **`feature/<breve-descrizione>`** — nuova feature retro-compatibile (nuovo
  format, nuovo linter, nuovo reference).
- **`fix/<breve-descrizione>`** — bugfix, tuning, typo, aggiornamento fixture.
- **`docs/<breve-descrizione>`** — modifiche solo a README/CHANGELOG/CONTRIBUTING
  o commenti.
- **`refactor/<breve-descrizione>`** — split file, riorganizzazione, senza
  cambio di comportamento.

Un branch = una PR = una feature/fix. Niente branch giganti che toccano tutto.

---

## Commit style

Format: `<tipo>: <descrizione breve, minuscolo, imperativo>`

Tipi ammessi:

| Tipo | Quando |
|---|---|
| `feat` | Nuova feature (nuovo format, nuovo linter, nuovo reference, ecc.) |
| `fix` | Bugfix in linter, script, workflow, fixture |
| `docs` | Modifiche a README, CHANGELOG, CONTRIBUTING, commenti |
| `refactor` | Riorganizzazione senza cambio comportamento |
| `test` | Nuove fixture, nuovi eval, o modifica a evals/ |
| `chore` | Bump versione, aggiornamento .gitignore, config |
| `anti-pattern` | Nuovo pattern in `references/08-anti-patterns.md` |

Esempi buoni:

```
feat: aggiunge format "podcast-clip" in references/formats/
fix: voice-lint soglia em-dash da 0.5 a 0.3
docs: aggiorna sezione CI in CONTRIBUTING
test: aggiunge fixture 04-skit-broken per regressione hook-lint
anti-pattern: AP-13 CTA doppia in Founder Ad
```

Esempi cattivi:

```
update stuff
WIP
fix bug
```

---

## Pre-push checklist

Prima di ogni `git push`, corri questi:

```bash
# 1. Evals passano
python3 evals/run.py

# 2. Se hai modificato SKILL.md o AGENTS.md, verifica coerenza tra i due
diff <(grep -E "^##" SKILL.md) <(grep -E "^##" AGENTS.md)

# 3. Se hai aggiunto un file in references/, aggiornalo nella mappa in SKILL.md
grep -c "$(basename references/nuovo-file.md)" SKILL.md
# atteso: >= 1

# 4. Se hai fatto un breaking change, aggiungi entry in CHANGELOG.md sotto
#    [Unreleased] con tag MAJOR
```

CI (`.github/workflows/evals.yml`) fa girare gli evals a ogni push/PR sui path
skill-critici. Se rompi CI su main, la skill viene considerata rotta finche' non
fixi.

---

## Come aggiungere...

### ...un nuovo reference file

1. Nome: `NN-topic-in-kebab-case.md`, dove `NN` e' il prossimo numero libero
   (guarda `references/` per l'ultimo usato).
2. Aggiungi la voce nella tabella "Mappa dei reference file" in `SKILL.md`.
3. Se il reference introduce una regola che va enforced, aggiungi il check nel
   linter Python corrispondente e aggiungi un caso in `evals/run.py`.
4. Se il reference cambia un contratto esistente, aggiungi entry in CHANGELOG
   con tag MAJOR e apri migration guide nel commit body.

### ...un nuovo format

1. Nuovo file `references/formats/NN-nome-format.md`. Segui la struttura degli
   altri: Cos'e', Perche' funziona, Come funziona, Struttura, Esempio, Do's &
   Don'ts.
2. Aggiungi voce in `references/05-format-selector.md`.
3. Aggiungi almeno una fixture in `fixtures/` che usa il format.
4. Aggiungi caso in `evals/run.py`.
5. Commit: `feat: aggiunge format <nome>`.

### ...un nuovo linter

1. Nuovo script Python in `scripts/NAME-lint.py`. Segue convenzioni degli altri:
   exit code 0 = pass, 1 = fail, stdout = report leggibile.
2. Aggiungi step di chiamata in `references/07-review-gates.md`.
3. Aggiungi step in `evals/run.py`.
4. Aggiorna `.github/workflows/evals.yml` sezione "Verify linter scripts exist".
5. Commit: `feat: aggiunge linter <nome>`.

### ...un nuovo reviewer sub-agent

1. Nuovo file `.claude/agents/<nome>-reviewer-landi.md`. Segui convenzione degli
   esistenti (`voice-reviewer-landi.md`, `grounding-reviewer-landi.md`).
2. Aggiungi step di spawn in `SKILL.md` workflow (passo 8 QA).
3. Documenta il format di output atteso nel file agent stesso.
4. Commit: `feat: aggiunge reviewer <nome>`.

### ...un nuovo anti-pattern

1. Trova un output sbagliato in produzione (o durante testing).
2. Aggiungi voce in `references/08-anti-patterns.md` con `❌ / ✅ / 🔍`.
3. Se il pattern e' comune, crea fixture in `fixtures/` che lo triggeri.
4. Aggiungi caso in `evals/run.py` che verifica che il linter lo becchi.
5. Commit: `anti-pattern: <breve descrizione>`.

### ...una nuova fixture

1. Nome: `NN-nome-descrittivo.md` in `fixtures/`. Nome dice cosa testa (es.
   `04-skit-broken-hook.md`).
2. Frontmatter YAML con expected exit codes per ogni linter:
   ```yaml
   ---
   name: skit-broken-hook
   description: Skit format con hook che viola diversity rule
   expected:
     format-lint: 0
     hook-lint: 1
     voice-lint: 0
     grounding-check: 0
   ---
   ```
3. Corpo con contenuto che triggeri esattamente i fail attesi (ne' piu' ne' meno).
4. Aggiungi caso in `evals/run.py`.
5. Verifica: `python3 evals/run.py` deve passare.
6. Commit: `test: aggiunge fixture <nome>`.

---

## PR review

Ogni PR va reviewed da un altro membro prima del merge. Checklist review:

- [ ] Evals passano in CI (verde)
- [ ] Se breaking change → entry CHANGELOG con MAJOR
- [ ] Se nuovo reference → voce nella mappa in SKILL.md
- [ ] Se nuovo format/linter/reviewer → tutti i punti della sezione "Come
      aggiungere" sopra
- [ ] Commit message rispetta il format
- [ ] Nessun file `brand-context/` reale committato (solo template)
- [ ] Nessun output generato committato (`runs/`, `bundles/`)

---

## Release

Quando fai release nuova, in ordine:

1. Aggiorna `CHANGELOG.md`: sposta contenuto da `[Unreleased]` in nuova sezione
   `[X.Y.Z] — YYYY-MM-DD`.
2. Commit: `chore: release vX.Y.Z`.
3. Tag: `git tag vX.Y.Z && git push --tags`.
4. Se breaking change: crea file in `migrations/vX.Y.Z.md` nel brain (non nella
   skill) con istruzioni upgrade per chi usa versioni vecchie.
5. Se skill e' usata come submodule (es. dentro `landi-brain`): esegui `git
   submodule update --remote skills/landi-video-scriptwriter` nel repo che la
   include, poi commit + push.

---

## Domande

Se qualcosa non e' chiaro qui, apri issue con label `question`. Meglio
domandare una volta che rompere main.
