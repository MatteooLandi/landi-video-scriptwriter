# Fixtures

Esempi sanitizzati di output "gold standard". Servono a:

1. **Riferimento**: quando aggiungi una nuova regola o modifichi la skill,
   confronta l'output atteso con questi esempi.
2. **Test regressione**: il runner in `evals/` gira i linter su questi file e
   verifica exit code atteso. Se dopo una modifica un fixture cambia
   inaspettatamente, la modifica ha rotto qualcosa.
3. **Few-shot mentale**: la skill puo' leggerne uno se serve un esempio di
   struttura tabellare corretta.

## File presenti

| File | Cosa dimostra | Format-lint | Hook-lint | Voice-lint | Grounding |
|---|---|:---:|:---:|:---:|:---:|
| `01-ugc-clean.md` | Brief UGC ben scritto, con 3 hook diversi, testo on-screen, receipts finali | ✓ pass | ✓ pass | ✓ pass | ✓ pass |
| `02-vsl-slop.md` | VSL con em-dash, triplette AI, hook simili, testo on-screen mancante | ✗ fail | ✗ fail | ✗ fail | ✗ fail |
| `03-founder-mixed.md` | Founder ad tecnicamente corretto ma con 1 flavor non tracciato + 1 tell voice | ✓ pass | ✓ pass | ⚠ warn | ⚠ warn |
| `04-context-slop.md` | Category entry point implicito, impalcatura generica, residuo assistente, calco EN e trattino medio come punteggiatura | n/a | n/a | ✗ fail | n/a |
| `05-command-contrast-slop.md` | Impalcatura a comando e falso contrasto nel parlato, con in coda i casi legittimi che devono restare puliti (CTA, istruzione d'uso, obiezione nominata) | n/a | n/a | ✗ fail | n/a |

## Convenzione

- Nome file: `NN-formato-stato.md` (es: `01-ugc-clean.md`, `02-vsl-slop.md`)
- Header YAML frontmatter con exit code atteso per ogni linter:

```yaml
---
fixture:
  format-lint: 0    # 0 = pass, 1 = fail
  hook-lint: 0
  voice-lint: 0
  grounding-check: 0
---
```

- Sanitizzato: no brand reali, no persone reali, no numeri di clienti veri.
  Usa nomi tipo "Prodotto Alfa", "Persona Beta", numeri arrotondati fittizi.
