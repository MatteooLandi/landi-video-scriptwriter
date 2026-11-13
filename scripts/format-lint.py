#!/usr/bin/env python3
"""format-lint: verifica meccanica del contratto di output di references/03-output-contract.md.

Gate 1 della catena di review (references/07-review-gates.md). Deterministico:
cerca header tabelle esatti, presenza CTA, placeholder non compilati, tag
Selling Block validi, naming Module.

Non giudica lo stile, solo la struttura. Se questo linter boccia, i gate a
valle (Hook, Voice, Grounding) non girano finché la formattazione non e' ok.

Uso:
    python3 format-lint.py DRAFT_FILE

Exit 0 se solo warning, 1 se finding (bounce).
"""
import re
import sys

# Header tabelle attesi (esatti). Vedi 03-output-contract.md.
EXPECTED_HEADERS = {
    "hooks": "Module | Cosa devi dire | Cosa far vedere | Note per Editor",
    "script": (
        "Module | Selling Block | Cosa devi dire | Cosa far vedere | "
        "Note per Editor"
    ),
    "broll": "Clip | Funzione narrativa | Indicazioni per il creator",
}

# Libreria Selling Block valida (03-output-contract.md sez "Libreria Selling Block").
VALID_SELLING_BLOCKS = {
    "problem", "human entry", "relatable struggle", "agitation",
    "discredit alternative", "bridge / discovery", "bridge/discovery",
    "solution",
    "unique", "unique mechanism",
    "showcase", "feature", "benefit", "benefit translation",
    "handle objection", "skeptical dialogue",
    "proof of result", "increase % achievement",
    "increase perceived value",
    "verbalized desire",
    "cta", "low-friction cta",
}

# Placeholder pattern (template non compilato).
PLACEHOLDER_PATTERNS = [
    re.compile(r"\{compilare\}", re.I),
    re.compile(r"\{[a-z0-9 _-]{1,40}\}", re.I),  # {qualsiasi cosa}
    re.compile(r"\bTBD\b"),
    re.compile(r"\bTODO\b", re.I),
    re.compile(r"_{3,}"),  # ___
    re.compile(r"\[insert[^\]]*\]", re.I),
    re.compile(r"<insert[^>]*>", re.I),
    re.compile(r"\[nome\]|\[brand\]|\[prodotto\]|\[persona\]", re.I),
]

# Note editor markers che finiscono per errore in "Cosa far vedere".
EDITOR_MARKERS = [
    re.compile(r"\bsfx:", re.I),
    re.compile(r"\btext overlay:", re.I),
    re.compile(r"\btesto on-screen:", re.I),
    re.compile(r"\bfade (?:to|in|out)\b", re.I),
    re.compile(r"\btransition\b", re.I),
]

# Naming Module (Tabella 1 e 2).
MODULE_PATTERN = re.compile(
    # L'hook puo' avere un'etichetta descrittiva (03-output-contract.md, Module).
    r"^(Hook \d+( \(per editor\))?( [-:] .+)?|Body \d+|CTA)$", re.I
)


def parse_markdown_tables(text):
    """Estrae tabelle markdown come lista di (header_line, [rows])."""
    tables = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Header candidate: contiene almeno 2 pipe non escape.
        if line.count("|") >= 2 and not line.startswith("|--") \
                and "-" not in line.replace("|", "").strip()[:3]:
            # Prossima riga deve essere separatore |---|---|
            if i + 1 < len(lines) and re.match(
                    r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$", lines[i + 1]):
                header = line
                rows = []
                j = i + 2
                while j < len(lines) and lines[j].strip().count("|") >= 2 \
                        and not lines[j].strip().startswith("#"):
                    rows.append(lines[j])
                    j += 1
                tables.append((i + 1, header, rows))
                i = j
                continue
        i += 1
    return tables


def normalize_header(h):
    """Rimuove pipe leading/trailing e normalizza spazi."""
    return re.sub(r"\s+\|\s+", " | ", h.strip().strip("|").strip())


def classify_table(header_norm):
    """Ritorna tipo tabella ('hooks','script','broll') o None."""
    if header_norm == EXPECTED_HEADERS["hooks"]:
        return "hooks"
    if header_norm == EXPECTED_HEADERS["script"]:
        return "script"
    if header_norm == EXPECTED_HEADERS["broll"]:
        return "broll"
    # Fuzzy: se contiene "Module" e "Cosa devi dire" e' probabilmente
    # una tabella brief formattata male.
    if "Module" in header_norm and "Cosa devi dire" in header_norm:
        if "Selling Block" in header_norm:
            return "script?"
        return "hooks?"
    return None


def cells(row_line):
    """Splitta una riga markdown tabella in celle."""
    line = row_line.strip().strip("|")
    return [c.strip() for c in line.split("|")]


def main(argv):
    if len(argv) != 2:
        print("usage: format-lint.py DRAFT_FILE")
        return 2
    with open(argv[1], encoding="utf-8") as f:
        text = f.read()

    findings = []
    warnings = []
    tables = parse_markdown_tables(text)

    if not tables:
        findings.append((0, "nessuna tabella trovata — brief senza contratto output"))
        _report(findings, warnings)
        return 1

    types_seen = []
    hooks_table = script_table = None
    for lineno, header, rows in tables:
        h_norm = normalize_header(header)
        kind = classify_table(h_norm)
        types_seen.append(kind)
        if kind == "hooks":
            hooks_table = (lineno, header, rows)
        elif kind == "script":
            script_table = (lineno, header, rows)
        elif kind == "hooks?":
            findings.append((
                lineno,
                f"Tabella 1 header non conforme: '{h_norm}' — atteso "
                f"'{EXPECTED_HEADERS['hooks']}'"
            ))
            hooks_table = (lineno, header, rows)
        elif kind == "script?":
            findings.append((
                lineno,
                f"Tabella 2 header non conforme: '{h_norm}' — atteso "
                f"'{EXPECTED_HEADERS['script']}'"
            ))
            script_table = (lineno, header, rows)
        elif kind is None and (
            "Funzione narrativa" in h_norm
            or "Indicazioni per il creator" in h_norm
            or "Scene" in h_norm
            or "Visual" in h_norm
        ):
            if h_norm != EXPECTED_HEADERS["broll"]:
                findings.append((
                    lineno,
                    f"Tabella 3 header non conforme: '{h_norm}' — atteso "
                    f"'{EXPECTED_HEADERS['broll']}'"
                ))

    if not hooks_table:
        findings.append((0, "Tabella 1 (Hooks) mancante"))
    if not script_table:
        findings.append((0, "Tabella 2 (Scene Script) mancante"))

    # Verifica righe Tabella 1 (Hooks).
    if hooks_table:
        lineno, header, rows = hooks_table
        col_count = len(cells(header))
        for i, row in enumerate(rows, 1):
            row_lineno = lineno + 1 + i  # +1 separator
            cs = cells(row)
            if len(cs) != col_count:
                findings.append((
                    row_lineno,
                    f"riga hook con {len(cs)} celle, atteso {col_count}"
                ))
                continue
            module = cs[0]
            if not MODULE_PATTERN.match(module):
                findings.append((
                    row_lineno,
                    f"Module '{module}' fuori pattern "
                    f"'Hook N' o 'Hook N (per editor)'"
                ))

    # Verifica righe Tabella 2 (Scene Script).
    if script_table:
        lineno, header, rows = script_table
        col_count = len(cells(header))
        has_cta = False
        for i, row in enumerate(rows, 1):
            row_lineno = lineno + 1 + i
            cs = cells(row)
            if len(cs) != col_count:
                findings.append((
                    row_lineno,
                    f"riga body con {len(cs)} celle, atteso {col_count}"
                ))
                continue
            module = cs[0]
            selling = cs[1] if len(cs) > 1 else ""
            said = cs[2] if len(cs) > 2 else ""
            shown = cs[3] if len(cs) > 3 else ""
            if module.upper() == "CTA":
                has_cta = True
            elif not MODULE_PATTERN.match(module):
                findings.append((
                    row_lineno,
                    f"Module '{module}' fuori pattern 'Body N' o 'CTA'"
                ))
            # Selling Block validi (multi-tag possibile: split su + o virgola)
            if selling:
                for tag in re.split(r"\s*[+,/]\s*", selling):
                    if tag and tag.lower().strip() not in VALID_SELLING_BLOCKS:
                        warnings.append((
                            row_lineno,
                            f"Selling Block '{tag}' fuori libreria "
                            f"(vedi 03-output-contract.md)"
                        ))
            # Paragrafone
            if said and len(said.split()) > 40:
                warnings.append((
                    row_lineno,
                    f"'Cosa devi dire' > 40 parole ({len(said.split())}), "
                    f"spezza in blocchi (brief scannerizzabile)"
                ))
            # Editor markers in 'Cosa far vedere'
            for marker in EDITOR_MARKERS:
                if marker.search(shown):
                    warnings.append((
                        row_lineno,
                        f"'Cosa far vedere' contiene indicazione editor "
                        f"('{marker.pattern}'), spostala in Note per Editor"
                    ))
                    break
        if not has_cta:
            findings.append((
                script_table[0],
                "CTA mancante in Tabella 2 (Module='CTA' richiesto)"
            ))

    # Placeholder ovunque nel testo.
    for i, line in enumerate(text.splitlines(), 1):
        for p in PLACEHOLDER_PATTERNS:
            m = p.search(line)
            if m:
                findings.append((
                    i,
                    f"placeholder non compilato: '{m.group(0)}' — "
                    f"template incompleto"
                ))
                break

    # Sintassi 'Testo on-screen:' senza contenuto.
    for i, line in enumerate(text.splitlines(), 1):
        m = re.search(r"testo on-screen:\s*(.*)$", line, re.I)
        if m and not m.group(1).strip().strip("*_`"):
            findings.append((
                i,
                "'Testo on-screen:' senza contenuto dopo i due punti"
            ))

    _report(findings, warnings)
    return 1 if findings else 0


def _report(findings, warnings):
    print(f"format-lint: {len(findings)} finding(s), {len(warnings)} warning(s)")
    for lineno, msg in findings:
        prefix = f"L{lineno}" if lineno else "  "
        print(f"  FINDING {prefix}: {msg}")
    for lineno, msg in warnings:
        prefix = f"L{lineno}" if lineno else "  "
        print(f"  WARN    {prefix}: {msg}")
    if not findings and not warnings:
        print("  formattazione conforme al contratto")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
