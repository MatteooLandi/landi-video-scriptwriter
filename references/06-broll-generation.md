# 06 - B-Roll (solo su richiesta)

La tabella "Broll Shots / Contenuti" si popola **solo quando l'utente la
richiede**, in una di due modalita'. Chiedi quale se non e' esplicito.

---

## Modalita' A - Indicazioni semplici per il creator

Descrizioni di clip da registrare, comprensibili da una persona poco scolarizzata,
realizzabili senza budget con materiali quotidiani (regole complete in
`03-output-contract.md`, sezione "Cosa far vedere"). Colonne: `Scene | Visual`.

Esempio di riga (settore baby, prodotto tipo scaldabiberon):
`1 | Foto del prodotto + bambino in una corsia di supermercato oppure a casa`
`2 | Clip di paesaggio dal finestrino dell'auto (si deve capire che e' dall'auto)`
`3 | Bimbo che piange (5 secondi bastano)`

---

## Modalita' B - Prompt per B-roll generati con AI

Quando l'utente chiede B-roll generati con l'AI, converti ogni beat in un prompt
ottimizzato. Principi (incorporati):

### Estrai i beat narrativi

Non ogni riga ha bisogno di B-roll. Individua i 5-12 momenti in cui il visual
aggiunge qualcosa che il parlato da solo non trasmette. Tipi di beat: pain
visualization, mechanism/how-it-works, social proof, lifestyle context, product
hero, emotion/outcome, pattern interrupt. Priorita' assoluta: hook (primi 3s) e
product reveal.

### Progetta la scena (una per shot)

Un solo soggetto + una sola azione + un solo movimento di camera per shot.
Definisci: soggetto, setting, azione, camera (inquadratura + movimento),
luce/mood, durata (1-5s), aspect ratio (default 9:16 verticale).

### Struttura del prompt

```
[Soggetto] + [Azione]. [Setting]. [Inquadratura + movimento]. [Luce/mood]. [Stile].
```

Regole prompt:
- Guida col soggetto (cosa si vede prima).
- Un'azione + un movimento camera, mai impilati.
- Linguaggio cinematografico ("shallow depth of field", "soft natural light",
  "35mm film grain", "warm golden hour").
- Sotto le 50 parole: piu' corto = piu' controllo, meno drift.
- Nessun testo/logo generato dall'AI (l'AI sbaglia il testo): i text overlay si
  aggiungono in post.
- Sempre l'aspect ratio nelle impostazioni di generazione.

### Anti-pattern

- Niente B-roll per ogni riga del brief (5-12 shot per un ad 30-60s).
- Niente prompt lunghissimi.
- Niente azioni multiple in uno shot.
- Il B-roll non e' una stampella per un brief debole.
- Se l'ad ha un creator reale, il B-roll e' ambientale/prodotto/astratto, non
  attori sostitutivi.
- Coerenza col format (un podcast vuole insert sobri, non droni cinematografici).
- Il B-roll non supera il 60% della durata totale: il creator on-camera domina.

> Nota tecnica. Se esiste un tool/API di generazione collegato (es. Higgsfield),
> assembla la shotlist in JSON e fai approvare all'utente shot e stima crediti
> prima di generare. In assenza di tool, consegna prompt e shotlist testuali che
> l'utente usera' nel proprio strumento.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
