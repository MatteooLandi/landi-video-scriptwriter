---
fixture:
  format-lint: 0
  hook-lint: 0
  voice-lint: 0
  grounding-check: 0
notes: Founder ad tecnicamente OK. Contiene 1 warning voice (parola "cambia"
       nel body) e 1 warning grounding (frase flavor non tracciata in verbatim).
       Nessun bounce hard atteso. Serve a verificare che i linter distinguano
       warning da finding.
---

# Brief Founder Ad - Prodotto Gamma (60s)

Format: Founder Ads
Concept: perche' abbiamo creato il prodotto
Angle: il fondatore aveva lo stesso problema del cliente
Target: professionista 30-40

## Tabella 1 - Hooks

| Module | Cosa devi dire | Cosa far vedere | Note per Editor |
|---|---|---|---|
| Hook 1 | Tre anni fa avevo un problema che nessuno riusciva a risolvermi. | Founder in ufficio, camera fissa. | Testo on-screen: cosa non funzionava nella mia agenzia |
| Hook 2 | Se lavori in questo settore probabilmente lo hai visto anche tu, e nessuno ne parla. | Founder che guarda la camera. | Testo on-screen: il problema silenzioso del settore |
| Hook 3 | Ho speso quattromila euro in consulenti prima di capire una cosa. | Ricevute e appunti sul tavolo. | Testo on-screen: quanto costa non sapere la risposta |

## Tabella 2 - Body Script

| Module | Selling Block | Cosa devi dire | Cosa far vedere | Note per Editor |
|---|---|---|---|---|
| Body 1 | Problem | Ogni mese perdevo giorni interi a fare la stessa cosa, in modo diverso ogni volta, senza mai un metodo chiaro. | B-roll ufficio. | |
| Body 2 | Human Entry | Ho parlato con altre trenta persone del settore. Tutte con lo stesso problema. Nessuna con una soluzione. | Chiamate video, meeting. | |
| Body 3 | Solution | Cosi' abbiamo costruito Prodotto Gamma. Serve a chi vuole cambiare la propria routine di lavoro senza cambiare tool. | Demo del prodotto. | Nota: "cambiare" e' parola da valutare, se voice-lint la flagga considera "cambiare" |
| Body 4 | Proof of Result | I primi che l'hanno usato ci hanno detto "finalmente qualcosa che parla la mia lingua". | Screenshot recensioni. | Tono: illustrativo , verbatim non tracciato, e' un modo di dire plausibile |
| CTA | Low-Friction CTA | Provalo gratis per due settimane. Link in bio. | Landing page trial. | Testo on-screen: 14 giorni gratis |

## Format Review: ships
## Hook Review: ships
## Voice Review: ships con nota , parola "cambiare" nel Body 3 e' borderline (voice-lint warning). Approvato perche' usata in contesto tecnico ("routine di lavoro"), non copywriter puffery.
## Grounding Review: grounded , flavor "finalmente qualcosa che parla la mia lingua" etichettato come illustrativo (non in verbatim.md). Fact "4000 euro" tracciato in brand-context/positioning.md riga 8.
