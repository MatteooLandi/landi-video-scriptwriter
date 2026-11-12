# 05 - Selettore di Format

Come scegliere il format. Prima definisci Message/Angle/Concept, poi scegli il
format di esecuzione (concept != format). E ricorda la producibilita': non
scegliere un format che la produzione non puo' realizzare bene.

Il dettaglio completo di ogni format (Cos'e', Perche' funziona, Come funziona,
Struttura, Esempio di script, Do's & Don'ts) e' in `references/formats/`, un
file per format. Qui c'e' la mappa di selezione.

> **Regola di lettura.** Non caricare tutti i format. Usa la mappa qui sotto per
> scegliere UNO (o due) format candidati; poi apri SOLO il file corrispondente in
> `formats/`. Questo mantiene il context leggero.

> Il "chi interpreta" deriva dalla natura del format descritta nella guida. Se in
> un caso specifico non e' chiaro, chiedilo all'utente invece di assumere.

---

## Mappa rapida

| Format | Quando usarlo | Chi interpreta | Costo | Durata | File dettaglio |
|---|---|---|---|---|---|
| Mashup Ads | Qualsiasi brand consumer | Piu' clip/creator montati | 0 EUR | 45-90s | `formats/01-mashup-ads.md` |
| Narrator / Story Ads | Prodotti che richiedono spiegazione | 2 attori | 100-500 EUR | 60-120s | `formats/02-narrator-story.md` |
| POV Ads | Engagement immediato | 1 creator, prima persona | 0-100 EUR | 15-45s | `formats/03-pov.md` |
| Educational VSL | Prodotti complessi (salute, tech, finanza) | Voce narrante / spokesperson autorevole | 200-1000 EUR | 90-180s | `formats/04-educational-vsl.md` |
| Non-Narrated Ads | Prodotti visivi (fashion, beauty, gadget) | Solo visual, no voce narrante | 0-100 EUR | 15-60s | (vedi nota) |
| Skit Conversation | Identificazione, aspirazione | 2 attori (conversazione sceneggiata) | 100-500 EUR | 45-90s | `formats/05-skit-conversation.md` |
| Podcast Ads (Reale/Fake) | Costruire fiducia (reale) o pattern interrupt nativo social (fake) | 2 speaker: attori reali, o soggetti AI/animati/villain nella variante fake | 0-300 EUR | 45-90s | `formats/06-podcast-ads.md` |
| UGC Tradizionale | Demo prodotto dirette | 1 creator | 50-200 EUR | 30-60s | `formats/07-ugc-tradizionale.md` |
| Story UGC | Engagement, storytelling naturale | 1 creator | 100-300 EUR | 45-90s | `formats/08-ugc-story.md` |
| UGC Mashup | Prova sociale massiccia | Piu' clip UGC | 0 EUR | 30-60s | `formats/09-ugc-mashup.md` |
| Street Interviews | Autenticita', reazioni genuine | Intervistatore + intervistati | 50-200 EUR | 30-60s | `formats/10-street-interviews.md` |
| Founder Ads | Connessione personale, trust | Il fondatore | 0-100 EUR | 60-120s | `formats/11-founder-ads.md` |
| Ugly Ads | Pattern interrupt, autenticita' | 1 creator, low-fi (screenshot, notes app, selfie) | 0 EUR | 15-30s | `formats/12-ugly-ads.md` |
| Us vs. Them | Differenziazione, decisione semplificata | 1 creator/voce + confronto visivo | 0-100 EUR | 30-60s | `formats/13-us-vs-them.md` |
| Yapper Ad | Racconto lungo in prima persona di una conversione al prodotto, con vendita diretta. Criteri di scelta: da definire con Matteo | 1 creator che recita un testo scritto | da definire con Matteo | da 90s a oltre 4 min (guida) | `formats/14-yapper-ad.md` |
| AI Animation (proposta) | Problema con una causa interna che non si vede da fuori. Criteri di scelta: da definire con Matteo | Voce narrante + animazione AI | da definire con Matteo | da definire con Matteo | `formats/15-ai-animation.md` |
| Song Ads (proposta) | Da definire con Matteo | Da definire con Matteo | da definire con Matteo | da definire con Matteo | `formats/16-song-ads.md` |

> **Nota su Non-Narrated Ads.** E' nella mappa ma la guida non ha un file
> dedicato. Non invento la struttura: se serve questo format, chiedi all'utente i
> dettagli o aggiungiamo un file apposta.

---

## Densita visuale e B-roll

Il format decide quante clip separate servono. Non assegnare un B-roll a ogni
blocco per abitudine.

| Famiglia | Format indicativi | Densita B-roll di partenza | Regola |
|---|---|---|---|
| **Raw o camera-led** | Founder, Podcast reale/fake, Street Interview, Ugly Ads, Yapper Ad (proposta, da confermare) | assente o bassa | La take principale e il visual. Aggiungi B-roll solo se chiarisce prodotto, prova o contesto. |
| **Conversazionale o recitato** | Story UGC, Skit Conversation | bassa | Mantieni la scena e la relazione tra personaggi. Non spezzare il flusso con inserti inutili. |
| **Demo naturale** | UGC Tradizionale, POV | bassa o media | Usa clip separate per utilizzo, dettaglio prodotto o problema difficile da mostrare parlando. |
| **Costruito o esplicativo** | Narrator, Educational VSL, Us vs. Them, AI Animation (proposta) | media o alta | Visualizza causa, meccanismo, confronto e prova. Ogni clip deve aggiungere informazione. |
| **Montaggio visuale** | Mashup, UGC Mashup, Non-Narrated, Song Ads (proposta) | alta per natura | Le clip sono il format, ma devono seguire l'arco narrativo e non essere riempitivi. |

Questa e una base, non una quota. Concept, budget, materiale disponibile e ritmo
possono cambiare la densita. Nei format con creator on-camera, il B-roll non
dovrebbe superare il 60% della durata salvo scelta esplicita.

---

## Come scegliere (in pratica)

1. **Awareness dell'audience.** Unaware/Problem-Aware favoriscono Story, Founder,
   Educational, POV "prima"; Solution/Product-Aware favoriscono Us vs Them,
   Ugly, Reaction, comparativi. (Mappa awareness>hook in `hook-types-library.md`.) Problem-Aware che ha i sintomi ma li considera normali:
   Educational con la Struttura 4 (3 segni, non è normale, vera causa, prodotto).
2. **Obiettivo.** Trust > Founder / Podcast. Prova sociale > UGC Mashup / Mashup.
   Spiegazione > Narrator / Educational VSL. Pattern interrupt > Ugly. Demo >
   UGC Tradizionale. Differenziazione > Us vs Them.
3. **Producibilita' (decisivo).** Quanti attori/take/location servono? Il creator
   disponibile ce la fa? C'e' materiale/B-roll? Budget editing e turnaround?
   Un conversazionale richiede clip e momenti di registrazione separati: se la
   produzione vuole un unico body, valuta un format a 1 attore.
4. **Concept riutilizzabile.** Lo stesso concept puo' generare esecuzioni diverse
   (statico, UGC, founder, motion, carosello). Scegli il format sulla base di
   audience + obiettivo + produzione, non per abitudine.

---

## Guidare l'utente (quando chiede supporto)

Se l'utente non arriva con concept/angle/format definiti e chiede aiuto, guidalo
in quest'ordine, poi procedi con lo script:

1. **Angle / concept:** qual e' il pain o la leva principale? (usa verbatim e
   angle bank del brand)
2. **Buyer persona:** a chi parliamo, a che awareness?
3. **Format:** scegli con la mappa sopra in base a obiettivo + producibilita'.

Non procedere alla scrittura finche' questi tre non sono chiari (dati o decisi
insieme).

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
