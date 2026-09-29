---
fixture:
  voice-lint: 0
notes: Fixture mirata alle regole di references/10-parlato-ritmo-e-ponti.md.
       I ponti della lista bianca (R3) devono restare puliti anche se
       appartengono alla famiglia dei pattern 'signposted transition' e
       'rhetorical self-question'. Il frammento singolo dentro una battuta
       (R7) non e' flag. Le ultime righe sono i casi che il linter deve
       continuare a segnalare come warning di ritmo, senza far fallire il
       gate: aforisma per eco, ritmo piatto, passivo, nominalizzazione.
       Se questo fixture inizia a fallire, un pattern nuovo ha mangiato la
       lista bianca.
---

# Fixture ponti ammessi e ritmo

Ponti della lista bianca, devono restare puliti:

Senti, la cosa che nessuno ti dice e' che le configurazioni non le rivede mai nessuno.

Guarda, l'ho fatto anche io per due anni.

Ti spiego una cosa. Il costo non sta nel software, sta nel tempo che ci metti.

Pensa a questo. Un errore su un immobile lo gestisci in dieci minuti.

E sai qual e' il punto? Su sessanta immobili quei dieci minuti diventano una giornata.

Cioe', nella pratica, ogni riga sbagliata la paghi sessanta volte.

Ti faccio un esempio. Il mese scorso ho trovato tre canoni fuori posto.

E questo significa che il conto lo scopri a fine anno, non a gennaio.

Il punto e' che nessuno te lo dice prima.

E li' e' dove cambia tutto.

Ma c'e' un altro aspetto.

E questo porta a un altro problema.

E sai qual e' la cosa interessante? Il calcolo lo fa da solo.

Ed e' esattamente per questo che ho smesso di farlo a mano.

E sai cosa succede? Che a giugno il numero torna.

E il conto arriva sempre.

Frammento singolo dentro una battuta, ammesso da R7:

Ho aperto il file di gennaio e ho contato gli errori. Sessanta, uno per immobile. E li' ho capito che il problema non era il file.

Righe da warning di ritmo, non devono far fallire il gate:

Il rischio non cresce con te. Si moltiplica per te.

Il problema nasce presto. Nessuno rivede le configurazioni. Ogni immobile aggiunge un errore. Il costo cresce ogni mese.

Il documento viene firmato in agenzia.

La gestione delle scadenze porta via due giorni al mese.
