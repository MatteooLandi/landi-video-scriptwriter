# 06 - Visual creator e B-roll

Questo riferimento decide quando mostrare il creator in camera e quando chiedere
una clip B-roll registrata separatamente. Il B-roll si genera solo su richiesta o
quando il format lo richiede davvero.

## Distinzione operativa

- **Camera:** il creator parla o agisce direttamente nella take principale.
- **B-roll separato:** clip silenziosa registrata a parte, montata sopra il
  parlato o la voce narrante.
- **Note editor:** testo on-screen, effetti, layout, timing, transizioni e
  montaggio. Non appartengono alla shot list creator.

Un visual non deve diventare automaticamente un B-roll. In un format raw, una
persona che parla in camera puo essere il visual corretto per molti blocchi
consecutivi.

## La densita dipende dal format

Consulta `references/05-format-selector.md`, sezione `Densita visuale e B-roll`.

- Format genuino, raw o conversazionale: pochi B-roll o nessuno.
- Format dimostrativo: B-roll selettivi su problema, utilizzo e risultato.
- Format costruito, educational o comparativo: piu B-roll, purche ogni clip
  abbia una funzione narrativa.

Non applicare mai la regola `una frase = una scena` o `un blocco = un B-roll`.
Prima scegli il format, poi la densita visuale.

## Prerequisito per una shot list

Il comando `broll {nome concept}` o una richiesta equivalente richiede un brief
gia completo con:

- concept e angle;
- script, hook e CTA;
- pubblico;
- prodotto e meccanismo;
- format;
- indicazioni gia definite per creator ed editor.

La shot list esegue la strategia. Non cambia concept, angle o format. Se il brief
non e completo, fermati e chiedi il pezzo mancante.

## Library standard vs shot list del brief

- `b-roll-library.md` contiene la banca interna permanente, costruita dalla
  ricerca e indipendente dal concept.
- La shot list del brief seleziona soltanto le clip pertinenti al singolo script
  e aggiunge eventuali richieste specifiche mancanti.
- Dal file interno esporta il naming insieme alle istruzioni; il creator lo usa
  come nome file. Versione AI, evidenze e riutilizzi restano interni.
- Al creator consegna `Clip`, `Funzione narrativa` e `Indicazioni per il
  creator`.

## Lettura narrativa dello script

Dividi lo script per funzione, non per frase:

- problema;
- causa;
- agitazione o conseguenza;
- desiderio;
- soluzione;
- meccanismo;
- beneficio;
- prova o autorevolezza;
- utilizzo del prodotto;
- risultato finale.

Un blocco semplice puo non richiedere B-roll. Per riprese affidate a un creator,
un blocco puo chiedere al massimo una o due mini clip nello stesso luogo. Se il
blocco richiede altre immagini o un altro luogo, spostale nella sezione
`B-roll utili extra` in fondo al brief.

Questo limite logistico non si applica ai contenuti generati con AI: un blocco
denso puo produrre fino a tre B-roll AI, anche in luoghi differenti, quando ogni
clip rende visibile una parte narrativa distinta.

L'arco complessivo dovrebbe coprire, quando presente nello script:

`problema -> causa -> agitazione -> meccanismo -> soluzione -> risultato`

Non accumulare clip esteticamente interessanti che non accompagnano questo
percorso.

## Priorita dell'hook

Quando il format prevede B-roll, ogni hook ha almeno una proposta dedicata. La
clip deve visualizzare il punto d'ingresso specifico dell'hook, non riciclare un
visual generico del body.

Eccezione: nei format deliberatamente raw o camera-led, l'hook puo restare in
camera. In quel caso cura setting, gesto, oggetto o movimento della take
principale senza inventare un B-roll separato.

## Funzione di ogni clip

Un B-roll deve fare almeno una di queste cose:

- rendere concreto un concetto astratto;
- mostrare il problema o la trasformazione;
- aggiungere contesto;
- dimostrare l'utilizzo o il meccanismo;
- aumentare l'emozione;
- sostenere la credibilita;
- creare attenzione utile al messaggio.

Non limitarti a ripetere letteralmente il parlato. Le metafore visuali sono
ammesse per problema, agitazione e soluzione solo se restano immediate e
comprensibili.

## Continuita del personaggio

- Script in prima persona: mantieni lo stesso avatar nelle scene, salvo scelta
  esplicita del concept.
- Script rivolto a `tu`, `loro` o a un pubblico generale: puoi mostrare persone
  diverse che rappresentano segmenti pertinenti.
- Mantieni coerenti eta, genere, aspetto e identita dello stesso personaggio
  lungo la shot list.

## Producibilita

Ogni voce deve chiarire in poco spazio:

- chi appare;
- cosa fa;
- dove si trova;
- quale oggetto usa;
- quale risultato deve essere visibile.

Usa luoghi accessibili e props realistici. Di norma chiedi una registrazione per
blocco. Per il creator vale una regola netta:

- un solo luogo per blocco;
- massimo una o due mini clip in quel luogo;
- mai chiedere nello stesso blocco riprese in due luoghi diversi;
- le riprese ulteriori vanno in `B-roll utili extra` alla fine del brief.

Una voce corretta descrive una scena eseguibile:

> Persona davanti allo specchio del bagno. Avvicina il viso e tocca la zona
> arrossata della guancia. Ripresa verticale con luce naturale.

Una voce insufficiente nomina soltanto un concetto:

> B-roll del problema della pelle.

## Prima, dopo e trasformazioni

- Mantieni abbastanza continuita da far capire che si tratta della stessa
  persona e della stessa trasformazione.
- Cambia leggermente angolo o inquadratura tra problema e risultato.
- Non simulare due immagini artificialmente identiche cambiando soltanto un
  dettaglio superficiale.
- Non promettere trasformazioni che il contesto non supporta.

## Output A - Indicazioni semplici per creator

Colonne: `Clip | Funzione narrativa | Indicazioni per il creator`.

Le indicazioni usano una scena concreta secondo le regole sopra. Non includono
istruzioni di montaggio, evidenze di ricerca, prompt AI o note sul riutilizzo.
Il creator deve esportare ogni file usando il valore della colonna `Clip`.

Se servono riprese supplementari non legate a un singolo blocco, aggiungi:

```markdown
## B-roll utili extra

| Clip | Funzione narrativa | Indicazioni per il creator |
|---|---|---|
| `b-roll_{categoria}_001` | B-roll utile extra | {clip riutilizzabile + luogo} |
```

Questa sezione non autorizza richieste dispersive: ogni clip deve essere
riutilizzabile e utile a piu momenti del brief.

## Output B - Prompt per B-roll generati con AI

Usa questa modalita solo se l'utente chiede B-roll generati con AI.

### Progettazione dello shot

Un solo soggetto, una sola azione e un solo movimento di camera. Definisci:
soggetto, setting, azione, inquadratura, movimento, luce, durata da 1 a 5 secondi
e aspect ratio, di default 9:16.

### Struttura del prompt

```text
[Soggetto] + [Azione]. [Setting]. [Inquadratura + movimento]. [Luce e mood]. [Stile].
```

Regole:

- guida col soggetto;
- resta sotto 50 parole;
- non generare testo o logo nell'immagine;
- usa un solo movimento di camera;
- mantieni avatar e stile coerenti con le altre scene;
- indica l'aspect ratio nelle impostazioni di generazione.

Se esiste un tool di generazione collegato, prepara la shot list e la stima dei
crediti e chiedi approvazione prima di generare media.

I limiti `un luogo per blocco` e `massimo due mini clip` non si applicano ai
B-roll AI. Restano obbligatori coerenza narrativa, continuita dei personaggi e
una funzione precisa per ogni clip.

## Checklist finale

- [ ] Densita B-roll coerente col format
- [ ] Nessuna corrispondenza automatica frase-scena
- [ ] Hook prioritari quando il format usa B-roll
- [ ] Ogni clip aggiunge informazione o funzione narrativa
- [ ] Arco dello script coperto senza clip decorative
- [ ] Avatar coerente con la grammatica dello script
- [ ] Scene producibili e descritte come azioni concrete
- [ ] Per il creator: un luogo e massimo due mini clip per blocco
- [ ] Eventuali riprese creator supplementari raccolte in `B-roll utili extra`
- [ ] Creator ed editor tenuti separati
- [ ] Prima/dopo credibili
- [ ] B-roll non superiore al 60% nei format con creator on-camera, salvo scelta
  esplicita del format

---

*Skill di Matteo Landi. LinkedIn: https://www.linkedin.com/in/matteolandidigital/*
