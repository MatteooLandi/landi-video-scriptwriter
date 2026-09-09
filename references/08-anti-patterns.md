# Anti-Patterns: cosa NON produrre mai

Galleria di output sbagliati, con perche' sono sbagliati e cosa fare invece.
Da usare come check finale prima di consegnare, e come input per nuove fixture
di regressione in `fixtures/`.

> **Come leggere questo file.** Ogni voce ha tre blocchi:
> `❌ Sbagliato` (l'output problematico), `✅ Giusto` (versione corretta),
> `🔍 Perche'` (la regola sottostante — il valore didattico e' qui).

---

## AP-01: Trattino lungo o trattino medio usato come punteggiatura

**❌ Sbagliato**
> Ho passato tre anni — davvero, tre anni — a coprire le occhiaie ogni mattina.
> Testo on-screen: "Cedolare sul NETTO – legale, previsto dalla normativa"

**✅ Giusto**
> Pagare la cedolare sul NETTO legalmente: come farlo

**🔍 Perche'**
Il trattino lungo e il trattino medio usato come pausa sono tell riconoscibili.
Nel parlato reale nessuno pausa cosi', e nei testi on-screen creano lo stesso
pattern. `voice-lint.py` blocca sempre `—` e blocca ` – ` come punteggiatura.
Il trattino medio senza spazi resta ammesso in intervalli e coppie reali, per
esempio `15–20 secondi` o `origine–destinazione`. Vale per ogni campo
dell'output. Regola in `references/02-writing-principles.md`.

---

## AP-02: Hook troppo simili tra loro

**❌ Sbagliato**
> Hook 1: "Sei stanca della pelle spenta?"
> Hook 2: "Sei stufa della pelle opaca?"
> Hook 3: "Sei stanca di avere la pelle senza luce?"

**✅ Giusto**
> Hook 1: "Sei stanca della pelle spenta?" *(domanda diretta)*
> Hook 2: "Il 73% delle donne over 40 lo scopre troppo tardi." *(dato / curiosity gap)*
> Hook 3: "Ho smesso di usare il tonico. Ecco cosa e' successo." *(contrarian / storia)*

**🔍 Perche'**
Tre hook servono a testare tre leve psicologiche diverse. Se sono varianti
della stessa parola, stai testando il vocabolario non l'angolo.
`hook-lint.py` controlla diversita' di tipo. Regola in
`references/01-hook-system.md`.

---

## AP-03: Numero inventato per "sembrare autorevole"

**❌ Sbagliato**
> "Il 78% delle donne che l'hanno provata ha visto risultati in 7 giorni."
> *(nessuna fonte, nessun dato reale nel brand-context)*

**✅ Giusto**
> "Le clienti che l'hanno provata ci scrivono che vedono risultati in pochi giorni."
> *(linguaggio derivato da verbatim reali, senza numero fabbricato)*

**🔍 Perche'**
Regola cardinale: **fatti inventati bounciano**. `grounding-check.py` confronta
numeri e claim con `brand-context/verbatim.md` e `products/`. Se non c'e'
fonte, il numero salta o viene sostituito con linguaggio qualitativo.
Dettaglio in `references/07-review-gates.md` sezione Grounding.

---

## AP-04: Brand name nei primi 3 secondi

**❌ Sbagliato**
> "Ciao, sono Sara di AcmeCosmetics e oggi ti parlo della nostra crema..."

**✅ Giusto**
> "Ho passato tre anni a coprire le occhiaie. Poi ho scoperto una cosa."
> *(Brand name arriva a ~15s, dentro la soluzione, non nell'hook)*

**🔍 Perche'**
Nei primi 3 secondi il viewer decide se scrollare. Un brand name in apertura
= "pubblicita'" = scroll. Regola hook: **problema/promessa prima, brand dopo**.
`hook-lint.py` flagga brand nei primi 3s. Vedi `references/01-hook-system.md`.

---

## AP-05: On-screen text = trascrizione del parlato

**❌ Sbagliato**
> Parlato: "Ho passato tre anni a coprire le occhiaie."
> On-screen: "Ho passato tre anni a coprire le occhiaie"

**✅ Giusto**
> Parlato: "Ho passato tre anni a coprire le occhiaie."
> On-screen: "3 anni di fondotinta pesante"

**🔍 Perche'**
On-screen text ha ruolo diverso dal parlato: **rinforza, non ripete**. Ripetere
annulla il doppio canale di attenzione. Formato: brevi (max 6 parole),
keyword, cifre. `format-lint.py` controlla che non sia copia letterale.

---

## AP-06: Voice AI-tell: "unlock", "trasforma", "svela", "elevate"

**❌ Sbagliato**
> "Sblocca il potere della tua pelle e trasforma la tua routine skincare."

**✅ Giusto**
> "Cambi una sola cosa nella tua routine, e la pelle inizia a cambiare davvero."

**🔍 Perche'**
"Sblocca / trasforma / svela / eleva" sono parole da ChatGPT default. Un
venditore reale non parla cosi'. `voice-lint.py` ha una blacklist. Sostituire
con verbi concreti dell'italiano parlato.

---

## AP-07: Puffery vuoto — "il migliore", "rivoluzionario", "unico"

**❌ Sbagliato**
> "La nostra crema rivoluzionaria e' l'unica sul mercato che davvero funziona."

**✅ Giusto**
> "Non uso piu' il fondotinta. Prima ne mettevo due strati, mentre ora sono riuscito ad evitarlo totalmente."
> *(dimostrazione via cambio comportamento, non aggettivo)*

**🔍 Perche'**
Aggettivi assoluti (migliore/unico/rivoluzionario) non trasmettono nulla e
attivano il BS-detector del viewer. Mostra il cambiamento, non nominarlo.
`voice-lint.py` misura densita' puffery.

---

## AP-08: CTA generica finale — "Scopri di piu'"

**❌ Sbagliato**
> "Scopri di piu' sul nostro sito."

**✅ Giusto**
> "Link in bio, 20% di sconto oggi solo con SARA20."
> *(azione concreta + incentivo + urgenza + tracciabilita')*

**🔍 Perche'**
"Scopri di piu'" non produce click misurabili. CTA efficace = azione specifica
+ reason-to-act-now. `format-lint.py` controlla presenza CTA e minimum
specificity.

---

## AP-09: Founder Ad senza founder identificabile

**❌ Sbagliato**
> "Noi di AcmeCosmetics abbiamo creato questa crema perche' crediamo nella
> bellezza autentica."
> *(chi e' "noi"? nessun nome, nessun volto, nessuna storia personale)*

**✅ Giusto**
> "Sono Maria, ho fondato Acme dopo che mia madre a 45 anni ha smesso di uscire di casa per le rughe."
> *(nome + relazione personale + trigger emotivo specifico)*

**🔍 Perche'**
Il format Founder Ad richiede founder reale con storia reale. Senza founder
identificabile e' un UGC generico travestito. Vedi
`references/formats/09-founder-ad.md`.

---

## AP-10: Script che sembra scritto, non parlato

**❌ Sbagliato**
> "Inoltre, e' importante sottolineare come, in ultima analisi, il prodotto
> rappresenti una soluzione ottimale."

**✅ Giusto**
> "Poi c'e' la cosa che conta davvero: funziona. Punto e stop."

**🔍 Perche'**
Script = testo detto ad alta voce. "Inoltre / in ultima analisi /
rappresenta" sono connettori scritti. Leggi il testo ad alta voce: se ti
inceppi, riscrivi. `voice-lint.py` conta densita' connettori formali.

---

## AP-11: Verbatim usato come slogan invece che come voce

**❌ Sbagliato**
> `brand-context/verbatim.md`: "finalmente una crema che non tira"
> Uso nello script: "Finalmente una crema che non tira!" *(headline)*

**✅ Giusto**
> "Le clienti ci scrivono cose tipo 'finalmente non mi tira piu''. E' il commento piu' frequente."
> *(verbatim citato come evidenza, non copiato come claim)*

**🔍 Perche'**
Verbatim e' materia prima per capire come parla il cliente, non copy pronto.
Copiarlo come slogan lo rende fake. `grounding-check.py` flagga verbatim usato
fuori dal suo contesto.

---

## AP-12: Format sbagliato per il messaggio

**❌ Sbagliato**
> Prodotto tecnico complesso con 4 differenziatori → format Skit da 15s
> *(non c'e' spazio per spiegare nulla)*

**✅ Giusto**
> Prodotto tecnico complesso → format VSL 60-90s *(spazio per problema,
> meccanismo, prova, offerta)*, o Founder Ad se c'e' una storia forte

**🔍 Perche'**
Ogni format ha una durata e un ritmo. Vedi `references/05-format-selector.md`.
Forzare messaggio ricco in format corto = perdi il messaggio. Selezione format
prima, scrittura dopo.

---

## AP-13: Category entry point lasciato nel brief

**❌ Sbagliato**
> "Sistema tutto mentre organizzi il viaggio."
> "Aggiungilo al tuo itinerario."

**✅ Giusto**
> "Weekend sulla neve? Prenota il parcheggio vicino agli impianti."

**🔍 Perche'**
Il copywriter conosce il contesto, il viewer no. `Viaggio` e `itinerario` non
dicono dove sta andando, perche' gli serve il prodotto o quale azione deve fare.
Se un neofita puo' chiedere "per cosa?", il category entry point va esplicitato.

---

## AP-14: Impalcatura da assistente al posto del parlato

**❌ Sbagliato**
> "Un buon punto di partenza."
> "Questo e' il momento giusto."
> "Dai un'altra occhiata."

**✅ Giusto**
> "Controlla il costo per le date che hai scelto."

**🔍 Perche'**
Sono ponti educati ma intercambiabili. Non aggiungono informazione e rendono il
testo levigato, anonimo e prevedibile. Taglia il ponte e nomina verbo, oggetto e
condizione.

---

## AP-15: Specificita' apparente

**❌ Sbagliato**
> "Ricevi informazioni utili e trova l'opzione piu' adatta."

**✅ Giusto**
> "Ricevi disponibilita' e orari aggiornati."

**🔍 Perche'**
La frase sembra informativa, ma non dice quali informazioni o quale criterio di
scelta. Non basta cambiare aggettivo: serve il referente concreto disponibile
nel brief.

---

## AP-16: Residui della conversazione nel deliverable

**❌ Sbagliato**
> "Certo, ecco i copy richiesti."
> "Di seguito trovi tre proposte."

**✅ Giusto**
> Il deliverable comincia direttamente dal primo hook o dalla prima sezione
> prevista dal contratto di output.

**🔍 Perche'**
Saluti automatici, riepiloghi del compito e meta-commenti appartengono alla chat,
non allo script o al brief consegnato.

---

## Come aggiungere un anti-pattern nuovo

1. Trovi un output sbagliato in produzione → screenshot o paste testo
2. Aggiungi voce qui con `❌ / ✅ / 🔍`
3. Se il pattern e' comune, crea fixture in `fixtures/` che lo triggeri
4. Aggiungi eval in `evals/run.py` che verifica il linter lo becca
5. Commit: `anti-pattern: <breve descrizione>`

Vivo il file: no pattern speculativi, solo cose viste davvero.
