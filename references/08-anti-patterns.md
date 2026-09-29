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

## AP-17: Impalcatura a comando al posto dell'esperienza

**❌ Sbagliato**
> "Smetti di mettere due strati di fondotinta. Inizia a curare la pelle."

**✅ Giusto**
> "Mettevo due strati di fondotinta ogni mattina. Adesso esco con la crema e basta."

**🔍 Perche'**
`Smetti di X. Inizia a Y.` trasforma chi parla in un istruttore e toglie la
prova, cioe' cosa e' successo davvero a lui. L'imperativo resta legittimo nella
CTA e nelle istruzioni d'uso: il problema e' l'impalcatura che regge tutto il
body. Regola in `references/02-writing-principles.md` principio 20.

---

## AP-18: Serie di frammenti senza montaggio che la regga

**❌ Sbagliato**
> "Niente appuntamenti fissati. Niente lead magnet. Niente DM. Solo contenuti
> buttati nel vuoto."
> *(nessuno stacco dichiarato, nessun testo on-screen, un solo piano)*

**✅ Giusto**
> "Non avevano appuntamenti fissati, lead magnet, DM, niente: solo contenuti
> buttati nel vuoto."
> *oppure* la stessa serie tenuta, con Note per Editor: "quattro stacchi
> rapidi, un frammento per clip, testo on-screen su ognuna".

**🔍 Perche'**
Le frasi senza verbo sono normali nel parlato, e in uno script possono essere la
struttura giusta quando il montaggio fa il lavoro dell'intonazione. Senza stacco
diventano una cadenza meccanica. Il test e' di produzione: ogni frammento ha la
sua clip? Regola in `references/02-writing-principles.md` principio 21.

**Soglia.** Vale da **tre frammenti di fila in su**. Una frase senza verbo
dentro una battuta e' libera e non richiede nota. Vedi
`references/10-parlato-ritmo-e-ponti.md` R7.

---

## AP-19: Falso contrasto

**❌ Sbagliato**
> "Non e' una crema qualunque. E' un trattamento."
> "Il punto non e' avere un prodotto in piu', ma togliere un passaggio."
> "Non solo idrata, protegge anche."

**✅ Giusto**
> "E' un trattamento che lavora di notte."
> "Togli un passaggio dalla routine della sera."

**🔍 Perche'**
Il falso contrasto nega un'alternativa che nessuno aveva proposto, poi arriva
all'informazione vera. La frase funziona anche senza la meta' negata. Unica
eccezione: la negazione risponde a un'obiezione posta davvero e nominata nello
script ("Troppo pesante per l'estate?" "No: ..."). `voice-lint.py` intercetta le
varianti ad alta precisione. Regola completa nello standard del Brain,
`landi-system/docs/anti-ai-slop-writing-standard.md` regola 6.

---

## AP-20: Numeri di risultato lasciati nudi

**❌ Sbagliato**
> "Tremila visualizzazioni. Dodici like. Zero ordini."

**✅ Giusto**
> "Con tremila visualizzazioni e dodici like non ho ricevuto un ordine."

**🔍 Perche'**
Dati d'offerta e numeri di risultato non si trattano allo stesso modo. Prezzo,
durata, dose e tempi di consegna restano neutri, perche' servono a decidere
(AP-03 resta valido: niente numeri inventati). I numeri che raccontano un
risultato dentro una storia vogliono la lettura di chi parla, altrimenti sono un
elenco che chi guarda deve interpretare da solo, e in un video non ha tempo.
Regola nello standard del Brain, regola 8.

---

## AP-21: Aforisma o frase a effetto nel body

**❌ Sbagliato**
> "Non e' una minaccia. E' matematica."
> "Il rischio non cresce con te. Si moltiplica per te."

**✅ Giusto**
> "Pensa a cosa succede nella pratica. Un errore su un immobile lo gestisci. Ma
> se quell'errore ce l'hai su 60 immobili, lo stai pagando 60 volte."

**🔍 Perche'**
L'aforisma funziona nei copy scritti. Detto in camera suona recitato, e
comprimendo il concetto porta via la prova: resta la sentenza, spariscono il
gesto, il numero e la conseguenza. Si riconosce cosi': frase corta, simmetrica,
astratta, che potrebbe stare su qualsiasi prodotto. Il primo esempio e' anche un
falso contrasto (`AP-19`) e lo becca `voice-lint.py`; il secondo no, perche'
l'aforisma per parallelismo non ha la meta' negata. Resta ammesso nella CTA che
chiude un open loop e nel tag comico di un personaggio che parla cosi'. Regola
in `references/10-parlato-ritmo-e-ponti.md` R4.

---

## AP-22: Blocchi corretti ma scollegati (bullet point letti ad alta voce)

**❌ Sbagliato**
> Body 1 `Problem`: "Gestire 60 immobili a mano porta errori."
> Body 2 `Discredit Alternative`: "I software gestionali costano centinaia di
> euro al mese."
> Body 3 `Solution`: "Il nostro sistema calcola tutto da solo."

**✅ Giusto**
> Body 1 `Problem`: "Gestire 60 immobili a mano porta errori."
> Body 2 `Discredit Alternative`: "E lo sai qual e' il rimedio che ti propongono
> tutti? Un gestionale da centinaia di euro al mese."
> Body 3 `Solution`: "Io ho fatto un'altra cosa. Ho messo il calcolo dentro un
> sistema che lo fa da solo."

**🔍 Perche'**
Le fasi narrative sono giuste in entrambe le versioni: il problema, lo
screditamento dell'alternativa, la soluzione. Nella prima manca la giuntura,
quindi ogni blocco nasce da se stesso e il risultato sono voci di un elenco
lette ad alta voce. Succede quando il brief viene letto come una lista di
funzioni da coprire. Il test: copri la colonna `Selling Block` e leggi solo il
parlato di fila; se si sente dove inizia un blocco nuovo, manca il ponte.
Regola in `references/10-parlato-ritmo-e-ponti.md` R2 e R3.

---

## AP-23: Passivo o nominalizzazione dentro il parlato

**❌ Sbagliato**
> "La gestione inefficiente delle risorse comporta un incremento del rischio
> operativo."
> "Il prodotto viene applicato la sera sulla pelle asciutta."

**✅ Giusto**
> "Piu' cose gestisci male, piu' il rischio cresce. E cresce moltiplicandosi,
> non sommandosi."
> "La sera lo metti sulla pelle asciutta."

**🔍 Perche'**
Passivo e nome astratto sono forme scritte: togliono il soggetto che agisce e
mettono distanza tra chi parla e quello che dice. Si riscrive rimettendo chi fa
la cosa e trasformando il nome nel verbo che contiene ("la gestione comporta"
diventa "se gestisci male"). Il passivo impersonale resta quando l'agente e'
davvero irrilevante o quando serve il registro di un personaggio tecnico
(principio 18). Regola in `references/10-parlato-ritmo-e-ponti.md` R8.

---

## AP-24: Ritmo piatto, tutte le frasi della stessa lunghezza

**❌ Sbagliato**
> "Il problema nasce presto. Nessuno rivede le configurazioni. Ogni immobile
> aggiunge un errore. Il costo cresce ogni mese."

**✅ Giusto**
> "E li' e' dove inizia il problema. Perche' le configurazioni che hai messo in
> piedi quando gestivi 10 immobili nessuno le ha mai riviste, e ogni immobile
> che aggiungi le rende piu' costose da correggere."

**🔍 Perche'**
Il parlato non ha ritmo uniforme: la frase breve colpisce, la lunga spiega e
accumula. Quattro frasi della stessa misura di fila diventano un metronomo e chi
ascolta smette di seguire. Vale anche tra blocchi: se ogni Body occupa lo stesso
numero di righe, il montaggio diventa uniforme. Le fasce di lunghezza e il
pattern (breve, breve, lunga, media, breve) sono in `formats-guide.md` sez. 2.1.
Regola in `references/10-parlato-ritmo-e-ponti.md` R5.

---

## Come aggiungere un anti-pattern nuovo

1. Trovi un output sbagliato in produzione → screenshot o paste testo
2. Aggiungi voce qui con `❌ / ✅ / 🔍`
3. Se il pattern e' comune, crea fixture in `fixtures/` che lo triggeri
4. Aggiungi eval in `evals/run.py` che verifica il linter lo becca
5. Commit: `anti-pattern: <breve descrizione>`

Vivo il file: no pattern speculativi, solo cose viste davvero.
