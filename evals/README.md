# Evals

Test di regressione per la skill. Gira i 4 linter sui fixture in `../fixtures/`
e verifica che l'exit code combaci con quello atteso dichiarato nel frontmatter.

## Uso

```bash
# Tutti i test
python3 evals/run.py

# Verbose (mostra output dei linter)
python3 evals/run.py --verbose

# Un solo fixture
python3 evals/run.py fixtures/01-ugc-clean.md
```

## Quando lanciarli

- **Prima di ogni push** alla skill.
- **Prima di modificare** un linter Python.
- **Dopo aver aggiornato** references/07-review-gates.md (le regole cambiano).

## Cosa fanno

Per ogni fixture in `fixtures/`:
1. Legge il blocco `fixture:` dal frontmatter (exit code attesi).
2. Esegue ogni linter Python.
3. Confronta exit code effettivo con atteso.
4. Pass/Fail per ogni check, riepilogo finale.

## Aggiungere un nuovo test

1. Crea un fixture in `../fixtures/NN-descrizione.md` con frontmatter:
   ```yaml
   ---
   fixture:
     format-lint: 0
     hook-lint: 0
     voice-lint: 0
     grounding-check: 0
   notes: descrizione di cosa dimostra
   ---
   ```
2. Scrivi il brief nel corpo del file.
3. Lancia `python3 evals/run.py fixtures/NN-descrizione.md` e verifica risultato.
4. Se atteso ≠ effettivo, decidi: e' un bug del linter (fixa) o l'atteso e'
   sbagliato (aggiorna frontmatter).
