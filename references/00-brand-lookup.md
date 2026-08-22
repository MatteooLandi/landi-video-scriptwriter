# 00 - Brand Lookup

Come la skill trova e usa la knowledge di brand per adattare linguaggio,
posizionamento e angoli al target. Il linguaggio dell'audience (verbatim) e' la
fonte primaria per hook, pain, obiezioni, desideri, claim e vocabolario.

---

## Struttura cartelle di brand

```
brand-context/
├── _manifest.md              indice: brand, mono/multi-prodotto, file presenti
├── brand-visual-dna.md       guidelines visive (font, colori, abbinamenti)
├── positioning.md            posizionamento a livello brand
├── buyer-personas.md         persona a livello brand
├── tone-of-voice.md          tono di voce, guardrail comunicativi
├── verbatim.md               linguaggio reale di clienti/audience
├── learnings.md              apprendimenti nel tempo (schema sotto)
├── resources.md              fonti
├── prodotto-spiegato-semplice.md  brief creator finale (solo mono-prodotto)
├── b-roll-library.md         footage library standard (solo mono-prodotto)
├── brief-creators-freestyle.md  derivato creator con B-roll prioritari
├── angle-bank.md             solo se azienda mono-prodotto (altrimenti nel prodotto)
└── products/
    └── {prodotto}/
        ├── {prodotto}-positioning.md
        ├── {prodotto}-buyer-personas.md
        ├── {prodotto}-verbatim.md
        ├── {prodotto}-learnings.md
        ├── prodotto-spiegato-semplice.md
        ├── b-roll-library.md
        ├── brief-creators-freestyle.md
        └── {prodotto}-angle-bank.md    banca angoli, specifica per prodotto
```

Convenzione nomi: minuscolo, trattini, niente spazi. Rende affidabile il lookup.

> **angle-bank.** Genera angoli per un prodotto specifico, quindi vive nella
> cartella prodotto. Sta a livello brand solo se l'azienda e' mono-prodotto.

---

## `_manifest.md` (indice del brand)

Dichiara cosa esiste, cosi' il lookup e' deterministico e la skill e' portabile
(su LLM senza filesystem, incolli il manifest piu' i file che ti servono).

Schema:

```markdown
# Manifest - {Nome Brand}

- Brand: {nome}
- Tipo: mono-prodotto | multi-prodotto
- Lingua principale: it | en-US
- Prodotti: {prodotto-1}, {prodotto-2}, ...

## File a livello brand
- positioning.md
- buyer-personas.md
- tone-of-voice.md
- verbatim.md
- brand-visual-dna.md
- learnings.md
- resources.md
- angle-bank.md            (presente solo se mono-prodotto)

## File per prodotto (products/{prodotto}/)
- {prodotto}-positioning.md
- {prodotto}-buyer-personas.md
- {prodotto}-verbatim.md
- {prodotto}-learnings.md
- {prodotto}-angle-bank.md
```

---

## Protocollo di lookup

1. **Con filesystem (project Claude o cartella locale/Git):** leggi `_manifest.md`
   se presente; altrimenti cerca i file per nome secondo la convenzione sopra.
2. **Senza filesystem (ChatGPT/Gemini/Custom GPT):** usa il manifest e i file che
   l'utente ha incollato nel contesto.
3. **Multi-prodotto:** identifica il prodotto in oggetto e carica i suoi file.
4. **Se un file necessario non c'e':** non inventare. Chiedi all'utente il dato
   mancante (persona, positioning, verbatim, angle) prima di procedere.

---

## Regola di precedenza: prodotto > brand

Se esiste il file a livello prodotto, quello **vince** per quel prodotto; il file
a livello brand riempie i vuoti. Esempio: se c'e' `{prodotto}-positioning.md`,
usa quello per il positioning; usa `positioning.md` brand per cio' che manca.

---

## Uso dei file nello script

- **verbatim.md:** fonte primaria del linguaggio. Prima di inventare una frase,
  controlla se il target l'ha gia' detta meglio.
- **buyer-personas.md:** definisce WHO e awareness per gli hook.
- **positioning.md:** claim, meccanismo unico, differenziatori per il body.
- **tone-of-voice.md:** registro e guardrail; vince sui default stilistici in caso
  di conflitto.
- **brand-visual-dna.md:** guida le indicazioni visive e (se generi B-roll AI) lo
  stile.
- **angle-bank.md:** angoli gia' validati da cui partire.
- **prodotto-spiegato-semplice.md:** snapshot creator-ready generato solo dopo
  che ricerca e brand context sono completi. Se presente, usalo come indice
  rapido dei fatti prodotto; i file sorgente restano canonici in caso di
  conflitto.
- **b-roll-library.md:** banca interna di scene standard, indipendente dal
  concept. Nel singolo brief seleziona solo le righe pertinenti e passa al
  creator naming da usare in export, funzione narrativa e indicazioni
  operative. Versione AI, evidenze e riutilizzi restano interni.
- **brief-creators-freestyle.md:** derivato non canonico generato via script da
  prodotto semplice e library. Usalo come deliverable generale per creator,
  non come fonte per riscrivere dati prodotto o strategia.

---

## `learnings.md` (schema e governance)

File di apprendimenti che deve essere sempre consultato e che nel tempo puo'
modificare gli altri file di contesto. Riceve **solo**: pattern ricorrenti,
opportunita' strategiche, warning. Spiega cosa va e cosa non va, per mantenere
efficienza. Niente copie di canonici, niente ripetizioni. Mantiene un backlog
della storicita' delle modifiche.

Schema:

```markdown
# Learnings - {Brand o Prodotto}

## Pattern ricorrenti
- [data] {pattern osservato} -> {implicazione operativa}

## Opportunita' strategiche
- [data] {opportunita'} -> {azione}

## Warning
- [data] {cosa evitare} -> {perche'}

## Changelog
- [data] {modifica applicata e a quale file di contesto}
```

Quando la skill riceve feedback su performance di uno script, propone
l'aggiornamento qui (vedi `UPDATE-MAP.md`, miglioramento continuo).

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
