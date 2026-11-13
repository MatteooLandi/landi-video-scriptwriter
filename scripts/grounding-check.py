#!/usr/bin/env python3
"""grounding-check: fact-vs-flavor scan sul brief (Gate 4).

Regola cardinale (references/07-review-gates.md § Grounding):
- FACT (numeri, %, prezzi, spec, claim prodotto) non tracciato → FINDING (bounce).
- FLAVOR (linguaggio customer, frase 'sounds like customer') non tracciato →
  NOTE (warning), aggiungi label 'illustrativo' nel brief. Non blocca.
- Se verbatim.md e' vuoto/template (< 20 righe utili) → salta check flavor,
  solo fact-check attivo.

Uso:
    python3 grounding-check.py DRAFT_FILE [BRAND_ROOT]

BRAND_ROOT default: dir del draft. Cerca brand-context/ dentro.
Exit 0 nessun fact-finding, 1 fact non tracciato.
"""
import os
import re
import sys

RECEIPTS = [
    "Format Review",
    "Hook Review",
    "Voice Review",
    "Grounding Review",
]


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def load_brand_vault(brand_root):
    """Carica tutti gli .md sotto brand-context/ in {path: text_norm}."""
    vault = {}
    root = os.path.join(brand_root, "brand-context")
    if not os.path.isdir(root):
        root = brand_root  # fallback
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8") as f:
                    vault[os.path.relpath(p, brand_root)] = norm(f.read())
            except OSError:
                pass
    return vault


# Righe e blocchi che elencano numeri o frasi da NON riusare non sono una fonte:
# un numero citato solo li' non e' tracciato. Un titolo con il marcatore esclude
# il blocco fino al titolo successivo.
BAN_MARKERS = re.compile(
    r"non riusare|non usare|non citare|da non (?:riusare|usare|citare)|senza fonte",
    re.I)


def load_fact_vault(brand_root):
    """Come load_brand_vault, ma senza le righe di divieto (vedi BAN_MARKERS)."""
    vault = {}
    root = os.path.join(brand_root, "brand-context")
    if not os.path.isdir(root):
        root = brand_root
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8") as f:
                    raw = f.read().splitlines()
            except OSError:
                continue
            kept, block_banned = [], False
            for line in raw:
                if line.lstrip().startswith("#"):
                    block_banned = bool(BAN_MARKERS.search(line))
                    if block_banned:
                        continue
                elif block_banned or BAN_MARKERS.search(line):
                    continue
                kept.append(line)
            vault[os.path.relpath(p, brand_root)] = norm("\n".join(kept))
    return vault


def verbatim_populated(brand_root):
    """True se verbatim.md ha almeno 20 righe utili non-template."""
    candidates = []
    root = os.path.join(brand_root, "brand-context")
    if not os.path.isdir(root):
        root = brand_root
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn == "verbatim.md" or fn.endswith("-verbatim.md"):
                candidates.append(os.path.join(dirpath, fn))
    total_useful = 0
    for p in candidates:
        try:
            with open(p, encoding="utf-8") as f:
                for line in f:
                    s = line.strip()
                    if not s:
                        continue
                    if s.startswith("#") or s.startswith("<!--"):
                        continue
                    if s in ("(compilare)", "{compilare}") or "compilare" in s.lower():
                        continue
                    if len(s) < 8:
                        continue
                    total_useful += 1
        except OSError:
            pass
    return total_useful >= 20


def extract_spoken_lines(text):
    """Estrae le frasi dalla colonna 'Cosa devi dire' delle tabelle."""
    spoken = []
    lines = text.splitlines()
    header_seen = False
    said_col_idx = None
    for i, line in enumerate(lines, 1):
        h = line.strip().strip("|").strip()
        if re.match(r"^\s*Module\s*\|", h):
            cols = [c.strip().lower() for c in h.split("|")]
            if "cosa devi dire" in cols:
                said_col_idx = cols.index("cosa devi dire")
                header_seen = True
            continue
        if header_seen and line.strip().count("|") >= 2:
            if re.match(r"^\s*\|?\s*:?-+", line):
                continue
            cs = [c.strip() for c in line.strip().strip("|").split("|")]
            if said_col_idx is not None and said_col_idx < len(cs):
                said = cs[said_col_idx]
                if said and said not in ("", "-", "—"):
                    spoken.append((i, said))
        elif header_seen and not line.strip():
            continue
        elif header_seen and (line.strip().startswith("#") or line.strip().startswith("|--")):
            if line.strip().startswith("#"):
                header_seen = False
                said_col_idx = None
    return spoken


# Pattern per estrarre fatti (numeri, %, prezzi, spec).
FACT_PATTERNS = [
    (re.compile(r"\b\d+(?:[.,]\d+)?\s*%"), "percentuale"),
    (re.compile(r"€\s*\d+(?:[.,]\d+)?|\d+(?:[.,]\d+)?\s*(?:euro|dollari|USD|EUR)\b", re.I),
     "prezzo"),
    (re.compile(r"\b\d+(?:[.,]\d+)?\s*(?:kg|g|mg|litri|ml|cm|mm|km|"
                r"anni|mesi|giorni|ore|minuti|secondi|volte|clienti|"
                r"utenti|persone|paesi)\b", re.I), "misura/spec"),
    # Un numero con separatore delle migliaia (20.000) e' un solo fatto, non
    # due frammenti (20 e 000) da cercare in file non correlati.
    (re.compile(r"(?<![\d.,])\d{1,3}(?:\.\d{3})+(?![\d])|(?<![\d.,])\d{2,}(?![\d])"),
     "numero grezzo"),
]


def extract_facts(said):
    facts = []
    for rx, kind in FACT_PATTERNS:
        for m in rx.finditer(said):
            facts.append((kind, m.group(0).strip()))
    return facts


def find_in_vault(needle, vault):
    n = norm(needle)
    for path, hay in vault.items():
        if n in hay:
            return path
    return None


def find_words_in_vault(needle, vault, min_ratio=0.5):
    """Match sostanziale: cerca almeno 50% delle parole (>=4 lett.) in ordine."""
    words = re.findall(r"[a-zà-ù]{4,}", norm(needle))
    if not words:
        return None
    for path, hay in vault.items():
        hits = sum(1 for w in words if w in hay)
        if hits / len(words) >= min_ratio:
            return path
    return None


def main(argv):
    if len(argv) < 2:
        print("usage: grounding-check.py DRAFT_FILE [BRAND_ROOT]")
        return 2
    draft = argv[1]
    brand_root = argv[2] if len(argv) > 2 else os.path.dirname(
        os.path.abspath(draft))
    with open(draft, encoding="utf-8") as f:
        text = f.read()

    vault = load_brand_vault(brand_root)
    fact_vault = load_fact_vault(brand_root)
    verbatim_ok = verbatim_populated(brand_root)

    findings = []  # fact non tracciato = bounce
    notes = []     # flavor non tracciato = warning

    print(f"grounding-check: brand vault = {len(vault)} file, "
          f"verbatim populated = {verbatim_ok}")
    if not verbatim_ok:
        print("  NOTE: verbatim sottopopolato — controllo flavor saltato; "
              "solo fact-check attivo")

    spoken = extract_spoken_lines(text)
    print(f"  righe parlato analizzate: {len(spoken)}")

    for lineno, said in spoken:
        # Fact check hard
        facts = extract_facts(said)
        for kind, evidence in facts:
            path = find_in_vault(evidence, fact_vault)
            if path:
                print(f"  L{lineno} FACT-TRACED [{kind}] '{evidence}' -> {path}")
            else:
                findings.append((lineno, kind, evidence))
                print(f"  L{lineno} FACT-UNTRACED [{kind}] '{evidence}' — "
                      f"nessuna corrispondenza in brand-context")

        # Flavor check soft (solo se verbatim popolato)
        if verbatim_ok:
            # cerca match sostanziale per righe > 6 parole
            said_words = re.findall(r"[a-zà-ù]{4,}", said.lower())
            if len(said_words) >= 6:
                path = find_words_in_vault(said, vault, min_ratio=0.5)
                if path:
                    print(f"  L{lineno} FLAVOR-TRACED -> {path}")
                else:
                    notes.append((lineno, said[:60]))
                    print(f"  L{lineno} FLAVOR-UNTRACED '{said[:60]}...' — "
                          f"aggiungi label 'illustrativo' se non e' claim")

    # Receipts
    print("receipts:")
    for r in RECEIPTS:
        mark = "present" if r.lower() in text.lower() else "ABSENT"
        print(f"  {mark:8} {r}")

    print(f"grounding-check: {len(findings)} fact-finding(s), "
          f"{len(notes)} flavor-note(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
