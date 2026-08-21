#!/usr/bin/env python3
"""hook-lint: verifica meccanica delle regole hook (references/01-hook-system.md).

Gate 2 della catena di review (references/07-review-gates.md). Gira dopo il
format-lint (ha bisogno che le tabelle siano formattate correttamente).

Check duri (finding):
- Numero hook base ≠ 3 (default)
- Testo on-screen mancante in Note per Editor
- Testo on-screen copiato dal parlato (similarity > 0.9)
- Testo on-screen fuori range 1-14 parole
- Brand/prodotto nel parlato hook (regola "primi 3s non pubblicità")
- Ricombinazione senza '(per editor)'

Check soft (warning):
- Diversità hook (Jaccard > 0.6 su parole ≥ 4 lettere)
- Segnali audience assenti (euristica)
- Prime 3 parole da throat-clearing

Uso:
    python3 hook-lint.py DRAFT_FILE [BRAND_ROOT]

BRAND_ROOT default: cartella del file. Cerca _manifest.md per brand+prodotti.
Exit 0 solo warning, 1 finding.
"""
import os
import re
import sys

THROAT_CLEARING_OPENERS = {
    "allora", "quindi", "insomma", "beh", "ecco", "senti", "cioe'", "cioe",
}


def load_brand_names(brand_root):
    """Legge _manifest.md e ritorna set di nomi brand+prodotti (lower)."""
    names = set()
    manifest = os.path.join(brand_root, "brand-context", "_manifest.md")
    if not os.path.exists(manifest):
        # prova senza brand-context/
        manifest = os.path.join(brand_root, "_manifest.md")
    if not os.path.exists(manifest):
        return names
    try:
        with open(manifest, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^\s*-\s*Brand:\s*(.+?)\s*$", line, re.I)
                if m:
                    val = m.group(1).strip().strip("{}").lower()
                    if val and val != "nome brand":
                        names.add(val)
                m = re.match(r"^\s*-\s*Prodotti:\s*(.+?)\s*$", line, re.I)
                if m:
                    parts = re.split(r"[,;]", m.group(1))
                    for p in parts:
                        v = p.strip().strip("{}").lower()
                        if v and not v.startswith("prodotto-"):
                            names.add(v)
    except OSError:
        pass
    return {n for n in names if len(n) > 2}


def parse_hooks_table(text):
    """Trova la Tabella 1 (Hooks) e ritorna (start_lineno, header, [rows])."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        h = line.strip().strip("|").strip()
        if re.match(
                r"^\s*Module\s*\|\s*Cosa devi dire\s*\|\s*Cosa far vedere",
                h):
            if i + 1 < len(lines) and re.match(
                    r"^\s*\|?\s*:?-+", lines[i + 1]):
                rows = []
                j = i + 2
                while j < len(lines) and lines[j].strip().count("|") >= 2 \
                        and not lines[j].strip().startswith("#"):
                    rows.append(lines[j])
                    j += 1
                return i + 1, line, rows
    return None


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def words(s):
    return re.findall(r"[a-zà-ù][a-zà-ù'-]{3,}", s.lower())


def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 0.0
    return len(sa & sb) / max(1, len(sa | sb))


def similarity_ratio(a, b):
    """Similarity semplice: |intersect| / |min|."""
    sa, sb = set(a), set(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / min(len(sa), len(sb))


def extract_onscreen(note_cell):
    """Trova il testo dopo 'Testo on-screen:' in una cella note editor."""
    m = re.search(r"testo on-screen[^:]*:\s*(.+?)(?:$|\|)",
                  note_cell, re.I | re.S)
    if not m:
        return None
    text = m.group(1).strip().strip('"').strip('"').strip('"').strip("'")
    # Rimuovi eventuali code tra parentesi tonde tipo (IG response)
    text = re.sub(r"\(.*?\)", "", text).strip()
    return text


def main(argv):
    if len(argv) < 2:
        print("usage: hook-lint.py DRAFT_FILE [BRAND_ROOT]")
        return 2
    draft = argv[1]
    brand_root = argv[2] if len(argv) > 2 else os.path.dirname(
        os.path.abspath(draft))
    with open(draft, encoding="utf-8") as f:
        text = f.read()

    findings = []
    warnings = []
    brand_names = load_brand_names(brand_root)

    parsed = parse_hooks_table(text)
    if not parsed:
        findings.append((0, "Tabella 1 (Hooks) non trovata"))
        _report(findings, warnings)
        return 1

    start, header, rows = parsed

    hook_base = []   # (row_lineno, module, said, shown, note, onscreen)
    hook_extra = []  # righe (per editor)
    for i, row in enumerate(rows, 1):
        cs = cells(row)
        if len(cs) < 4:
            continue
        module, said, shown, note = cs[0], cs[1], cs[2], cs[3]
        onscreen = extract_onscreen(note)
        entry = (start + 1 + i, module, said, shown, note, onscreen)
        if "(per editor)" in module.lower():
            hook_extra.append(entry)
        else:
            hook_base.append(entry)

    # Numero hook base
    if len(hook_base) != 3:
        findings.append((
            start,
            f"hook base = {len(hook_base)}, atteso 3 (default). "
            f"Se voluto diverso, specificare nella richiesta"
        ))

    # Check ogni hook base
    for lineno, module, said, shown, note, onscreen in hook_base:
        # Testo on-screen presente?
        if onscreen is None:
            findings.append((
                lineno,
                f"{module}: 'Testo on-screen:' mancante in Note per Editor "
                f"(obbligatorio per ogni hook)"
            ))
        else:
            # Lunghezza 1-14 parole
            wc = len(onscreen.split())
            if wc < 1:
                findings.append((
                    lineno,
                    f"{module}: testo on-screen vuoto"
                ))
            elif wc > 14:
                findings.append((
                    lineno,
                    f"{module}: testo on-screen {wc} parole, atteso 1-14"
                ))
            # Similarity con parlato
            said_w = words(said)
            onscreen_w = words(onscreen)
            if said_w and onscreen_w:
                sim = similarity_ratio(said_w, onscreen_w)
                if sim > 0.9:
                    findings.append((
                        lineno,
                        f"{module}: testo on-screen ~identico al parlato "
                        f"(similarity {sim:.2f}) — deve essere diverso"
                    ))
        # Brand/prodotto nei primi 3s (parlato hook)
        said_low = said.lower()
        hit = next((n for n in brand_names if n in said_low), None)
        if hit:
            findings.append((
                lineno,
                f"{module}: nome brand/prodotto '{hit}' nel parlato hook — "
                f"regola 'primi 3s non pubblicità' (01-hook-system.md § 5)"
            ))
        # Throat-clearing opener
        first_word = re.match(r"[\"'\"]*([a-zà-ù']+)", said_low)
        if first_word and first_word.group(1) in THROAT_CLEARING_OPENERS:
            warnings.append((
                lineno,
                f"{module}: apertura con '{first_word.group(1)}' — "
                f"throat-clearing, la prima parola è la più cara"
            ))

    # Diversità tra hook base (Jaccard)
    if len(hook_base) >= 2:
        for a in range(len(hook_base)):
            for b in range(a + 1, len(hook_base)):
                wa = set(words(hook_base[a][2]))
                wb = set(words(hook_base[b][2]))
                if wa and wb:
                    j = jaccard(list(wa), list(wb))
                    if j > 0.6:
                        warnings.append((
                            hook_base[b][0],
                            f"{hook_base[a][1]} vs {hook_base[b][1]}: "
                            f"Jaccard {j:.2f} > 0.6, hook troppo simili — "
                            f"variazione drastica raccomandata"
                        ))

    # Hook extra (ricombinazione) - naming
    for lineno, module, said, shown, note, onscreen in hook_extra:
        if not re.match(r"^Hook \d+ \(per editor\)$", module, re.I):
            findings.append((
                lineno,
                f"riga extra '{module}' non segue pattern "
                f"'Hook N (per editor)'"
            ))

    _report(findings, warnings)
    return 1 if findings else 0


def _report(findings, warnings):
    print(f"hook-lint: {len(findings)} finding(s), {len(warnings)} warning(s)")
    for lineno, msg in findings:
        prefix = f"L{lineno}" if lineno else "  "
        print(f"  FINDING {prefix}: {msg}")
    for lineno, msg in warnings:
        prefix = f"L{lineno}" if lineno else "  "
        print(f"  WARN    {prefix}: {msg}")
    if not findings and not warnings:
        print("  hook conformi alle regole 01-hook-system.md")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
