# 10 - Parlato, ritmo e ponti tra blocchi

Lo script non e' un testo. E' un discorso.

Questo file contiene i vincoli che rendono uno script dicibile a voce: la
continuita' del ragionamento tra un blocco e il successivo, il ritmo delle
frasi, i ponti ammessi, il divieto di aforismi e il test di lettura ad alta
voce. `02-writing-principles.md` resta la sede dei principi generali di
scrittura; qui ci sono le regole che riguardano **come il discorso scorre**.

> **Provenienza.** Metodo dichiarato da Matteo il 2026-09-25, su documento suo.
> Le decisioni su ponti ammessi, aforismi e frammenti singoli sono sue
> `[dichiarato: Matteo, 2026-09-25]`. Se cambiano, `UPDATE-MAP.md` dice quali
> file riallineare.

---

## R1. Prima di ogni blocco, la domanda unica

**Questa frase la direbbe una persona vera davanti a una camera?**

Se la risposta e' no, si riscrive. Vale riga per riga, non a campione, e vale
anche quando il contenuto e' verificato al 100% (principio 1 di
`02-writing-principles.md`).

---

## R2. Le fasi narrative restano. Le cuciture non si devono sentire

Sono due livelli diversi e convivono.

**Livello struttura.** Ogni blocco ha un obiettivo preciso e il suo tag nella
colonna `Selling Block`: racconti il problema, lo agiti, nomini il nemico
comune, screditi le alternative, presenti la soluzione senza dire il brand,
poi nomini il prodotto, poi lo spieghi, poi porti prova e obiezioni, poi
chiudi. Questa sequenza e' il motore di vendita dello script e non si tocca.
La libreria completa dei tag sta in `03-output-contract.md`.

**Livello giuntura.** Il passaggio da una fase all'altra deve suonare come una
persona che sta ragionando davanti alla camera, non come qualcuno che gira
pagina. Chi guarda non deve sentire dove finisce "sto agitando" e dove inizia
"sto screditando le alternative".

**La regola operativa.** Ogni blocco tiene il suo obiettivo, e la sua prima
frase nasce dall'ultima del blocco precedente. I blocchi restano separati nella
tabella e nel montaggio: quello che si cuce e' il ragionamento.

**Il test.** Copri la colonna `Selling Block` e leggi solo il parlato di fila.
Se si sente dove inizia un blocco nuovo, manca il ponte.

**❌ Sbagliato** (tre fasi giuste, nessuna giuntura)
> Body 1: "Gestire 60 immobili a mano porta errori."
> Body 2: "I software gestionali costano centinaia di euro al mese."
> Body 3: "Il nostro sistema calcola tutto da solo."

**✅ Giusto** (stesse tre fasi, con le giunture)
> Body 1: "Gestire 60 immobili a mano porta errori."
> Body 2: "E lo sai qual e' il rimedio che ti propongono tutti? Un gestionale
> da centinaia di euro al mese."
> Body 3: "Io ho fatto un'altra cosa. Ho messo il calcolo dentro un sistema che
> lo fa da solo."

**Cosa sta sbagliando l'AI quando succede.** Legge il brief come un elenco di
funzioni da coprire e produce un blocco per funzione, autoconclusivo. Il
risultato sono bullet point letti ad alta voce: ogni riga e' corretta, il
discorso non esiste.

---

## R3. Ponti ammessi (lista bianca)

Queste formule sono **ammesse per nome** nel parlato. Non sono da flaggare come
ponti formulaici, e il reviewer Voice non le segna come tell.
`[dichiarato: Matteo, 2026-09-25]`

**Per aprire un blocco**
- "Senti,"
- "Guarda,"
- "Ti spiego una cosa."
- "Pensa a questo."
- "E sai qual e' il punto?"

**Per sviluppare**
- "Cioe', nella pratica,"
- "Ti faccio un esempio."
- "E questo significa che"
- "Il punto e' che"

**Per collegare due blocchi**
- "E li' e' dove cambia tutto."
- "Ma c'e' un altro aspetto."
- "E questo porta a un altro problema."
- "E sai qual e' la cosa interessante?"

**Per chiudere**
- "Ed e' esattamente per questo che"
- "E sai cosa succede?"
- "E il conto arriva sempre."

**Limiti della lista bianca.**
1. La lista e' chiusa. Una formula della stessa famiglia che non e' scritta qui
   resta soggetta ai pattern `ponte formulaico` e `domanda retorica auto-posta`
   di `07-review-gates.md`. Restano vietate, per esempio, "Ecco la verita':",
   "Ecco il punto:", "Il segreto?", "E qui viene il bello:", "Il risultato?",
   "Indovina un po'", "Sembra familiare?", "Assurdo, vero?".
2. Un ponte per blocco. Due ponti nella stessa battuta tornano a essere un tic.
3. Non si ripete lo stesso ponte due volte nello stesso script.
4. Il ponte non sostituisce il contenuto: se togliendo il ponte la battuta non
   dice piu' niente, il problema e' la battuta.

---

## R4. Niente aforismi, niente frasi a effetto

Gli aforismi funzionano nei copy scritti. Nei video suonano forzati e togliono
naturalezza: chi parla smette di raccontare e inizia a recitare una battuta.

Si riconoscono cosi': frase corta, simmetrica, astratta, che sembra una
citazione e che potrebbe stare su qualsiasi prodotto.

**❌ Sbagliato**
> "Non e' una minaccia. E' matematica."
> "Il rischio non cresce con te. Si moltiplica per te."

**✅ Giusto**
> "Pensa a cosa succede nella pratica. Un errore su un immobile lo gestisci. Ma
> se quell'errore ce l'hai su 60 immobili, lo stai pagando 60 volte."

**Come si riscrive.** Si sostituisce la frase a effetto con il fatto concreto
che la frase voleva riassumere: il gesto, il numero, la conseguenza osservabile.
L'aforisma comprime, e comprimendo toglie la prova.

**Dove l'aforisma resta ammesso.**
- Nella **CTA**, se chiude un open loop gia' aperto (principio 10 di
  `02-writing-principles.md`).
- Nel **tag comico** di un personaggio che parla cosi' ("Chissa' perche'!"),
  solo nei format comici e negli skit, come nella regola 9 di
  `formats-guide.md` sez. 2.8. Non in un testimonial serio, non in un
  educational.

**Rapporto con il falso contrasto.** Il primo esempio sbagliato qui sopra e'
anche un falso contrasto (`AP-19`), quindi lo becca il linter. Il secondo no:
l'aforisma per parallelismo non ha la meta' negata e passa ogni controllo
meccanico. E' la forma da guardare a mano.

---

## R5. Frasi brevi alternate a frasi lunghe

Il parlato non ha un ritmo uniforme. La frase breve crea impatto, la frase
lunga spiega e accumula. Servono entrambe, alternate.

**❌ Sbagliato:** frasi tutte della stessa lunghezza, ritmo piatto.

**✅ Giusto**
> "E li' e' dove inizia il problema. [breve] Perche' le configurazioni che hai
> messo in piedi quando gestivi 10 immobili nessuno le ha mai riviste, e ogni
> immobile che aggiungi le rende piu' costose da correggere. [lungo]"

**Controllo operativo.** Conta le parole delle frasi di un blocco. Se stanno
tutte nella stessa fascia, il blocco va rifatto. Le fasce e il pattern ritmico
completo (breve, breve, lunga, media, breve) sono in `formats-guide.md` sez.
2.1, con la distribuzione consigliata per sezione.

**Non vale solo dentro il blocco.** Anche i blocchi tra loro hanno lunghezze
diverse: se ogni Body occupa lo stesso numero di righe, il montaggio diventa
metronomico.

---

## R6. Struttura interna del blocco

Tre movimenti, nell'ordine.

1. **Apertura.** Aggancia con una domanda, un'osservazione o un fatto concreto.
   Nasce dall'ultima frase del blocco precedente (R2).
2. **Sviluppo.** Spiega il concetto con parole semplici, e con un esempio quando
   c'e' spazio.
3. **Chiusura.** O lascia una porta aperta verso il blocco dopo, o chiude con
   un'affermazione secca.

La struttura e' un default, non un obbligo riga per riga: un blocco da una
battuta sola resta legittimo. Quello che non e' legittimo e' una serie di
blocchi che aprono e chiudono tutti allo stesso modo.

---

## R7. Frammenti: il singolo e' libero, la serie no

Aggiornamento del principio 21 di `02-writing-principles.md`.
`[dichiarato: Matteo, 2026-09-25]`

- **Una frase senza verbo dentro una battuta e' libera.** Non serve
  giustificarla, non serve una nota. E' parlato normale ("E li' e' dove tutto
  cambia.").
- **Tre o piu' frasi senza verbo di fila** richiedono che ogni pezzo abbia il
  suo stacco, la sua clip o il suo beat, dichiarato nelle Note per Editor.
  Altrimenti si ricuce dentro una frase corrente, tenendo le stesse parole.

Il motivo resta quello di `AP-18`: la serie di frammenti funziona quando il
montaggio fa il lavoro dell'intonazione. Senza stacco e' cadenza meccanica.

---

## R8. Passivo e nominale fuori dal parlato

Le costruzioni passive ("viene applicato", "e' stato studiato") e le
nominalizzazioni ("la gestione delle scadenze comporta") sono forme scritte.
Nel parlato distanziano chi parla da quello che dice e togliono il soggetto.

**❌ Sbagliato:** "La gestione inefficiente delle risorse comporta un
incremento del rischio operativo."

**✅ Giusto:** "Piu' cose gestisci male, piu' il rischio cresce. E cresce
moltiplicandosi, non sommandosi."

**Come si riscrive.** Si rimette il soggetto che agisce e si trasforma il nome
astratto nel verbo che contiene: "la gestione comporta" diventa "se gestisci
male"; "viene applicato" diventa "lo metti".

**Eccezione.** Il passivo impersonale resta quando l'agente e' davvero ignoto o
irrilevante, e quando serve il registro tecnico di un personaggio (principio 18
di `02-writing-principles.md`).

---

## R9. Ogni termine tecnico si spiega, sempre

Un termine tecnico non spiegato perde il pubblico a meta' battuta, perche' chi
ascolta ha un solo passaggio e non puo' rileggere.

Pattern obbligatorio: **termine, poi traduzione in parole comuni, poi
beneficio tangibile** (uno dei due basta, entrambi e' meglio). Il pattern
completo con esempi e' la "Regola del Spiega Sempre" in `formats-guide.md`
sez. 2.5.

Vale anche per i meccanismi presi da `root-cause.md` e `positioning.md`:
prima si comprime la catena causale in una battuta, poi si spiega il termine
che resta (principio 1 di `02-writing-principles.md`).

---

## R10. Test finale: leggere ad alta voce

Prima di consegnare qualsiasi script, si legge **ogni blocco** ad alta voce,
una volta sola, senza fermarsi.

- Se ti blocchi su una parola, quella parola cambia.
- Se devi riprendere fiato a meta' frase, quella frase si spezza.
- Se non ti viene naturale dirlo, si riscrive.
- Se suona come uno spot, si riscrive.

Il test e' parte del Gate Voice e lascia una riga nella ricevuta
(`07-review-gates.md`, Gate 3). Non e' un controllo opzionale: senza quella
riga il brief non e' consegnabile.

Domande di verifica, dalla regola 5 di `formats-guide.md` sez. 2.8:
lo direi cosi' a un amico? Togliendo il nome del prodotto sembra ancora una
conversazione reale? C'e' almeno un marcatore di autenticita' per blocco?

---

## Riassunto operativo

| Controllo | Dove guarda | Chi lo fa |
|---|---|---|
| Direbbe questa frase una persona vera? | ogni riga | scrittore, poi reviewer Voice |
| Cuciture tra blocchi non si sentono | passaggio tra Body N e Body N+1 | test a tag coperto (R2) |
| Ponte dalla lista bianca, uno per blocco | apertura di ogni blocco | R3 |
| Nessun aforisma nel body | frasi corte e simmetriche | R4, a mano |
| Frasi di lunghezza alternata | dentro il blocco e tra blocchi | R5, warning del linter |
| Frammenti in serie con stacco dichiarato | Note per Editor | R7, linter |
| Nessun passivo o nominale nel parlato | ogni riga | R8, warning del linter |
| Termini tecnici spiegati | ogni occorrenza | R9 |
| Lettura ad alta voce eseguita | tutto lo script | R10, riga in ricevuta |

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
