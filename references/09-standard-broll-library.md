# 09 - Libreria B-roll standard

Modalita usata da `build-broll-library` per costruire la footage library minima
del brand dopo ricerca e strategia complete. Non produce uno script e non parte
da un concept specifico.

## Scopo

Creare scene riusabili che coprano i principali archi narrativi emersi dallo
studio di mercato, audience, problemi, cause profonde, feature, benefici, casi
d'uso, prove e risultati gia ottenuti.

La library e la base di partenza. Quando un brief non necessita di uno shot
specifico, puo selezionare una scena da questa banca.

## Input richiesti

- prodotto spiegato semplice;
- positioning;
- buyer personas;
- analisi delle cause profonde;
- tone of voice;
- learnings;
- verbatim e output di ricerca;
- risultati documentati del brand, se presenti.

Se il contesto non e consolidato, non generare scene generiche.

## Contratto

Raggruppa le scene per categoria e genera almeno cinque righe per ciascuna
categoria obbligatoria definita da `build-broll-library`.

| Clip | Indicazioni creator | Versione AI | Evidenza dalla ricerca | Riutilizzabile per |
|---|---|---|---|---|
| `b-roll_{categoria}_001` | {scena concreta} | {declinazione sintetica o Non adatta} | {fonte + insight} | {segmenti, cause, benefici o blocchi} |

## Naming

- Pattern: `b-roll_{categoria}_{numero a tre cifre}`.
- Usa underscore dentro categorie composte.
- La numerazione riparte da `001` per ogni categoria.
- In update non rinumerare né riciclare identificativi.
- Ordina le righe dalla piu utile e riusabile alla meno prioritaria. Le prime
  tre di ogni categoria alimentano il brief creator freestyle.

## Indicazioni creator

Ogni cella descrive:

- chi appare;
- una sola azione principale;
- un luogo;
- l'oggetto usato, se necessario;
- il risultato visibile.

La descrizione deve essere eseguibile senza conoscere la ricerca sottostante.
Non inserire parlato, testo on-screen o istruzioni di montaggio.

## Versione AI

La colonna contiene una declinazione breve della stessa funzione narrativa,
non un prompt completo. Usa l'AI quando permette di mostrare contesti, metafore
o situazioni difficili da produrre. Scrivi `Non adatta` quando serve il prodotto
reale, una prova autentica o una persona specifica.

## Evidenza e riutilizzo

- `Evidenza dalla ricerca` spiega in una riga da quale insight nasce la scena.
- `Riutilizzabile per` indica segmenti, cause profonde, benefici, casi d'uso o
  funzioni narrative compatibili.
- Non legare la scena a un singolo concept se puo restare utile in piu brief.

## Uso nel singolo brief

Il brief specifico sceglie soltanto le scene necessarie in base a concept,
script e format. Al creator mostra:

| Clip | Funzione narrativa | Indicazioni per il creator |
|---|---|---|
| `b-roll_{categoria}_001` | {categoria} | {indicazione della clip scelta} |

Il creator usa `Clip` come nome file in export. Versione AI, evidenza e
riutilizzi restano nella library interna.

Se la library non copre uno shot indispensabile, genera una richiesta specifica
nel brief applicando `references/06-broll-generation.md`.

## Controlli

- Almeno cinque clip distinte per categoria obbligatoria.
- Scene fondate su ricerca o contesto consolidato.
- Naming valido e stabile.
- Nessuna descrizione astratta come `B-roll del problema`.
- Versione AI breve o `Non adatta`.
- Nessuna versione AI, evidenza o nota di riutilizzo esportata al creator.

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
