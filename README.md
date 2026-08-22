# Landi Video Scriptwriter

Skill Claude/Codex per scrivere script e brief di **video ads short-form**
(italiano principale, inglese US secondario) con il framework di Matteo Landi.

Stessa skill, tre modi d'uso. Ogni ambiente ha il suo file di ingresso; il
"cervello" e' sempre `references/`.

---

## Struttura

```
landi-video-scriptwriter/
├── README.md                   questo file
├── SKILL.md                    ingresso per Claude Code
├── AGENTS.md                   ingresso per Codex CLI
├── CHANGELOG.md                storia delle versioni (SemVer)
├── CONTRIBUTING.md             guida per contributor
├── UPDATE-MAP.md               come aggiornare la skill (miglioramento continuo)
├── DEPENDENCIES.md             dipendenze esterne (Python, tool)
├── .github/workflows/
│   └── evals.yml               CI: linter regression a ogni push/PR
├── references/                 il cervello: regole complete
│   ├── 00-brand-lookup.md
│   ├── 01-hook-system.md
│   ├── 02-writing-principles.md
│   ├── 03-output-contract.md
│   ├── 04-bilingual-it-us.md
│   ├── 05-format-selector.md
│   ├── 06-broll-generation.md
│   ├── 07-review-gates.md
│   ├── 08-anti-patterns.md     galleria di output sbagliati (do NOT ship)
│   ├── 09-standard-broll-library.md  footage library senza concept
│   ├── formats-guide.md        guida completa (strategia, sintassi, blocchi)
│   ├── hook-types-library.md   20 tipi di hook
│   └── formats/                un file per format (14 file)
├── scripts/                    linter Python (4)
│   ├── format-lint.py
│   ├── hook-lint.py
│   ├── voice-lint.py
│   └── grounding-check.py
├── .claude/
│   ├── agents/                 reviewer sub-agent indipendenti
│   ├── hooks/gate-check.py     Stop hook advisory
│   └── settings.json           wiring hook
├── fixtures/                   gold-standard input per evals
├── evals/                      regression suite
│   ├── README.md
│   └── run.py                  `python3 evals/run.py` → 12/12 pass
└── brand-context/              TEMPLATE da compilare (dati cliente vanno FUORI)
```

---

## Uso in Claude Code

Due opzioni:

1. **Skill installata:** salva il file `.skill` (pacchetto) dal profilo, oppure
   importa questa cartella come skill. Claude legge `SKILL.md` e carica i
   `references/` da solo, quando servono.
2. **Project:** metti questa cartella (o i suoi file) in un project Claude. La
   knowledge di brand va in `brand-context/` (o nel project stesso).

Non devi incollare nulla a mano: i reference vengono letti su richiesta.

## Uso in Codex CLI (e agenti che leggono AGENTS.md)

Apri questa cartella come repo. L'agente legge `AGENTS.md`, che rimanda ai file
in `references/` con percorsi relativi. Tieni la knowledge di brand in
`brand-context/` dentro lo stesso repo (o collegala via Git). Anche qui i
reference si leggono dal filesystem, senza incollarli.

**Nessuna differenza operativa tra Claude Code e Codex CLI**: stesso workflow,
stesso output.

## Uso in ChatGPT / Gemini / interfacce web

Le web-UI non hanno filesystem. Serve un **bundle** — skill + reference +
brand-context concatenati in un unico documento markdown.

Il bundle NON e' in questo repo (evita duplicazione). E' generato on-demand da
`bundle-skill.sh` nel brain `landi-brain`:

```bash
cd ~/Desktop/Claude/landi-brain
./scripts/bundle-skill.sh landi-video-scriptwriter <nome-brand>
```

Output in `bundles/`. Incolla il file in:
- ChatGPT Project → Instructions / Files
- Claude.ai Project → Knowledge
- Gemini Gem → Instructions
- API → `system` message

---

## Knowledge di brand

`brand-context/` in questo repo e' un **template**. Compila i file (o punta ai
tuoi) seguendo `references/00-brand-lookup.md`: manifest, convenzione nomi,
precedenza prodotto>brand, schema dei learnings.

Il file `verbatim.md` (linguaggio reale dell'audience) e' la fonte primaria per
hook, pain, obiezioni, desideri e claim. Senza verbatim la skill genera con
warning "illustrativo".

**Dati brand reali NON vanno committati qui** — vanno nel loro brand workspace
dentro `landi-brain/brands/<nome>/brand-context/` (gitignored).

---

## Quality assurance

Ogni output passa per **4 gate** (dettaglio in `references/07-review-gates.md`):

1. **Format** — `scripts/format-lint.py`: contratto tabellare Notion.
2. **Hook** — `scripts/hook-lint.py`: 3 hook, on-screen text, no brand-3s,
   diversita'.
3. **Voice** — `scripts/voice-lint.py` + `voice-reviewer-landi` (sub-agent):
   AI-writing tells, scoring E-R-C.
4. **Grounding** — `scripts/grounding-check.py` + `grounding-reviewer-landi`
   (sub-agent): fact vs flavor, tracciamento verbatim.

Un **Stop hook** (`.claude/hooks/gate-check.py`) in advisory mode segnala brief
consegnati senza receipts di review.

Regressione automatica via **CI GitHub Actions** (`.github/workflows/evals.yml`)
a ogni push/PR sui path skill-critici.

Per lanciare la suite in locale:
```bash
python3 evals/run.py
```

---

## Aggiornare la skill

- Modifiche piccole (fix, tuning, nuovo anti-pattern): vedi `UPDATE-MAP.md`.
- Nuovo format / reference / linter / reviewer: vedi `CONTRIBUTING.md` sezione
  "Come aggiungere...".
- Release: vedi `CONTRIBUTING.md` sezione "Release" + aggiorna `CHANGELOG.md`.

---

## Anti-pattern

`references/08-anti-patterns.md` contiene esempi di **cosa NON produrre mai**,
con `❌ / ✅ / 🔍` per ogni caso. E' sia riferimento didattico sia sorgente per
nuove fixture di regressione.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
