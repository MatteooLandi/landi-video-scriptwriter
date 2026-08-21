# Video Ads Script Writer

Skill per scrivere script e brief di video ads (italiano principale, inglese US
secondario) con il framework di Matteo Landi. Stessa skill, tre modi d'uso.
Ogni ambiente ha il suo file di ingresso; il "cervello" e' sempre `references/`.

## Struttura

```
video-ads-script-writer/
├── README.md                    questo file
├── SKILL.md                     ingresso per Claude (skill / project)
├── AGENTS.md                    ingresso per Codex e agenti che leggono AGENTS.md
├── PORTABLE-master-prompt.md    ingresso per ChatGPT/Gemini (system prompt sintetico)
├── PORTABLE-BUNDLE.md           tutto-in-uno per ChatGPT senza filesystem
├── UPDATE-MAP.md                come aggiornare la skill (e miglioramento continuo)
├── references/                  il cervello: regole complete
│   ├── 00-brand-lookup.md
│   ├── 01-hook-system.md
│   ├── 02-writing-principles.md
│   ├── 03-output-contract.md
│   ├── 04-bilingual-it-us.md
│   ├── 05-format-selector.md
│   ├── 06-broll-generation.md
│   ├── formats-guide.md         guida completa dei format (grande)
│   └── hook-types-library.md    20 tipi di hook
└── brand-context/               TEMPLATE della knowledge di brand (da compilare)
    ├── _manifest.md
    ├── positioning.md, buyer-personas.md, tone-of-voice.md, verbatim.md, ...
    └── products/PRODOTTO-ESEMPIO/...
```

## Uso in CLAUDE

Due opzioni:
- **Skill installata:** salva il file `.skill` (pacchetto) dal profilo, oppure
  importa questa cartella come skill. Claude legge `SKILL.md` e carica i
  `references/` da solo, quando servono.
- **Project:** metti questa cartella (o i suoi file) in un project Claude. La
  knowledge di brand va in `brand-context/` (o nel project stesso).

Non devi incollare nulla a mano: i reference vengono letti su richiesta.

## Uso in CODEX (e agenti che leggono AGENTS.md)

Apri questa cartella come repo. L'agente legge `AGENTS.md`, che rimanda ai file in
`references/` con percorsi relativi. Tieni la knowledge di brand in
`brand-context/` dentro lo stesso repo (o collegala via Git). Anche qui i
reference si leggono dal filesystem, senza incollarli.

## Uso in CHATGPT / GEMINI / CUSTOM GPT

Non c'e' filesystem, quindi il contenuto va fornito:
- **Rapido:** incolla `PORTABLE-master-prompt.md` come istruzioni. Format
  riassunti a una riga.
- **Completo:** usa `PORTABLE-BUNDLE.md` (istruzioni + tutti i reference in un
  unico file) e aggiungi `references/formats-guide.md` per il dettaglio dei
  format. Su Custom GPT: bundle nelle Instructions o come Knowledge, guida e file
  di brand come Knowledge.

## Knowledge di brand

`brand-context/` e' un template. Compila i file (o punta ai tuoi) seguendo
`references/00-brand-lookup.md`: manifest, convenzione nomi, precedenza
prodotto>brand, schema dei learnings. Il file `verbatim.md` (linguaggio reale
dell'audience) e' la fonte primaria per hook, pain, obiezioni, desideri e claim.

## Aggiornare la skill

Vedi `UPDATE-MAP.md`: dice quale file toccare per ogni tipo di modifica e come far
entrare performance e feedback nei learnings.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
