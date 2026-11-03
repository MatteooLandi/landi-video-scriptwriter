#!/usr/bin/env python3
"""voice-lint: scan meccanico dei tell AI nella scrittura italiana.

Gate 3 della catena di review (references/07-review-gates.md). Fonte pattern:
references/07-review-gates.md sezione 'Lista pattern'. Adattamento italiano di
voice-lint.py di Slagle.

Scope: solo il parlato ("Cosa devi dire") e il testo on-screen. Non girare
contro doc di sistema, context o istruzioni.

Layer deterministico. Il reviewer (creative-voice-review) decide quali flag
sono reali: una parola isolata e' rumore, un cluster e' segnale. I verbatim
customer sono esenti (li verifica il reviewer).

Uso:
    python3 voice-lint.py DRAFT_FILE

Exit 0 clean (mechanical), 1 flag trovati.
"""
import re
import sys

# ---- Vocabolario flaggato (density) ---------------------------------
# Modificare in references/07-review-gates.md prima; sincronizzare qui.

FLAGGED_WORDS = {
    # importance-inflator
    "cruciale", "cruciali", "fondamentale", "fondamentali", "essenziale",
    "essenziali", "indispensabile", "indispensabili", "primario", "primaria",
    "vitale", "vitali", "imprescindibile", "imprescindibili",
    # texture
    "armonioso", "armoniosa", "sinergico", "sinergica", "sinergia",
    "olistico", "olistica", "meticoloso", "meticolosa", "meticolosamente",
    "raffinato", "raffinata", "sofisticato", "sofisticata", "impeccabile",
    "sfaccettato", "sfaccettata", "poliedrico", "poliedrica",
    # transformation verbs
    "trasforma", "trasformare", "trasformato", "trasformata",
    "rivoluziona", "rivoluzionare", "rivoluzionario", "rivoluzionaria",
    "sblocca", "sbloccare", "sblocchi",
    "potenzia", "potenziare", "potenziato",
    "eleva", "elevare", "elevato",
    "amplifica", "amplificare", "amplificato",
    "ottimizza", "ottimizzare", "ottimizzato",
    "massimizza", "massimizzare", "massimizzato",
    # brochure adjectives
    "rinomato", "rinomata", "impareggiabile", "impareggiabili",
    "pluripremiato", "pluripremiata",
    "straordinario", "straordinaria", "eccezionale", "eccezionali",
    "curato", "curata",
}

# Espressioni banned multi-parola (case-insensitive).
FLAGGED_PHRASES = [
    "senza pari",
    "senza precedenti",
    "su misura",
]

# ---- Pattern regex --------------------------------------------------

PATTERNS = [
    ("negative parallelism", re.compile(
        r"\bnon\s+(?:e'|è|era|erano)\s+(?:solo|soltanto|semplicemente|"
        r"unicamente)\b"
        r"|\bnon\s+solo\b[^.\n]{3,80}\bma\s+(?:anche|addirittura|pure)\b"
        r"|\bpiù\s+che\s+\w+[,\s]+(?:e'|è)\b"
        r"|\bnon\s+un\s+semplice\s+\w+[,\s]+ma\s+un\b", re.I),
     "frame 'non e' solo X, e' Y' — costruzione firma AI"),
    ("false contrast", re.compile(
        r"\bnon\s+(?:e'|è)\s+(?:un|una|uno)\b[^.!?\n]{0,60}[.!?]\s*"
        r"(?:e'|È|è)\s"
        r"|\bil\s+punto\s+non\s+(?:e'|è)[^.\n]{0,80}\bma\b"
        r"|\bnon\s+si\s+tratta\s+di\b[^.\n]{0,80}\bma\b"
        r"|\bnon\s+stiamo\s+dicendo\b[^\n]{0,80}\bstiamo\s+dicendo\b"
        r"|\bsembra\s+[^.\n]{0,40}\se\s+invece\s+(?:e'|è)\s", re.I),
     "falso contrasto \u2014 nega un'alternativa che nessuno aveva proposto; "
     "ammesso solo se risponde a un'obiezione nominata nello script"),
    ("command scaffold", re.compile(
        r"\bsmett(?:i|ila|etela)\s+(?:di|con)\b"
        r"|\bbasta\s+con\s+(?:il|la|i|le|gli|lo|l')\b"
        r"|\bdevi\s+smettere\s+di\b"
        r"|\bnon\s+\w+are\s+[^.!?\n]{0,40},\s+\w+a\b", re.I),
     "impalcatura a comando 'Smetti di X, inizia a Y' \u2014 nel parlato serve "
     "l'esperienza di chi parla; l'imperativo vive nella CTA"),
    ("inflated significance", re.compile(
        r"\b(?:rappresenta|segna|apre|inaugura)\s+(?:un(?:a|')?)\s+"
        r"(?:svolta|punto\s+di\s+svolta|nuovo\s+capitolo|nuova\s+era|"
        r"nuovo\s+modo)\b"
        r"|\bun\s+nuovo\s+modo\s+di\s+\w+"
        r"|\buna\s+nuova\s+era\b"
        r"|\bsi\s+erge\s+come\b"
        r"|\bsi\s+distingue\s+come\b", re.I),
     "importance-inflation invece di claim piano"),
    ("manufactured-intimacy opener", re.compile(
        r"\b(?:posso\s+essere\s+(?:onesto|sincero|onesta|sincera)"
        r"|parliamoci\s+chiaro"
        r"|diciamocelo"
        r"|te\s+lo\s+dico\s+chiaramente"
        r"|voglio\s+essere\s+(?:sincero|onesta|sincera|onesto))\b", re.I),
     "manufactured-intimacy — vulnerabilita' performata; entra sulla "
     "confessione, non sulla richiesta di farla"),
    ("rhetorical self-question", re.compile(
        r"(?:sembra\s+familiare\?"
        r"|assurdo,?\s+vero\?"
        r"|ti\s+dice\s+qualcosa\?"
        r"|sai\s+qual['e' ]+(?:e'|è)\s+la\s+cosa\s+peggiore\?"
        r"|sai\s+cosa\s+penso\?"
        r"|\bonestamente\?"
        r"|\bseriamente\?)", re.I),
     "domanda che il parlante non sta davvero facendo — ammesso solo come "
     "question-hook in apertura, mai nel body"),
    ("throat-clearing opener", re.compile(
        r"\b(?:nel\s+mondo\s+di\s+oggi"
        r"|in\s+un\s+mondo\s+(?:dove|in\s+cui)"
        r"|ai\s+giorni\s+nostri"
        r"|immagina\s+(?:di|questo|per\s+un\s+attimo)"
        r"|diciamocelo:"
        r"|ammettiamolo)\b", re.I),
     "apertura spesa a vuoto — la prima riga e' la piu' cara"),
    ("puffery register", re.compile(
        r"\b(?:esperienza\s+(?:premium|unica|indimenticabile|senza\s+eguali)"
        r"|curato\s+nei\s+minimi\s+dettagli"
        r"|attenzione\s+al\s+dettaglio"
        r"|impegno\s+per\s+l['e' ]?eccellenza"
        r"|nel\s+cuore\s+di"
        r"|di\s+altissima\s+qualità"
        r"|di\s+altissimo\s+livello)\b", re.I),
     "brochure register che nessuno dice a voce"),
    ("signposted transition", re.compile(
        r"\b(?:ecco\s+(?:la\s+verità|il\s+punto|perché):?"
        r"|la\s+cosa\s+migliore\?"
        r"|il\s+segreto\?"
        r"|e\s+qui\s+viene\s+il\s+bello:?"
        r"|il\s+risultato\?"
        r"|indovina\s+un\s+po['?])", re.I),
     "ponte formulaico — nel parlato si taglia, non si annuncia"),
    ("pristine CTA", re.compile(
        r"\b(?:non\s+aspettare\s+oltre"
        r"|non\s+perdere\s+(?:tempo|(?:questa\s+)?occasione)"
        r"|cambia\s+la\s+tua\s+vita"
        r"|meriti\s+di"
        r"|unisciti\s+a\s+(?:migliaia|milioni)"
        r"|scopri\s+di\s+più\s+oggi"
        r"|ordina\s+(?:ora|il\s+tuo\s+oggi)"
        r"|approfitta\s+(?:ora|subito|oggi\s+stesso))\b", re.I),
     "CTA command-close ad-speak — chiudi come farebbe un amico"),
    ("audience enumeration", re.compile(
        r"\bche\s+tu\s+sia\s+\w+[^.\n]{1,60}\s+o\s+\w+"
        r"|\bsia\s+se\s+\w+[^.\n]{1,60}\s+sia\s+se\s+\w+", re.I),
     "'che tu sia X o Y' — nomina tutti, atterra su nessuno"),
    ("copula avoidance", re.compile(
        r"\b(?:offr(?:e|ono)\s+(?:un['a']?)\s+(?:esperienza|gamma|selezione|"
        r"varietà)"
        r"|garantisc(?:e|ono)\s+risultati"
        r"|fornisc(?:e|ono)\s+(?:una\s+soluzione|un\s+servizio\s+"
        r"impeccabile))", re.I),
     "'offre/garantisce/fornisce X' dove 'e''/'ha' basterebbe"),
    ("astrazione vuota", re.compile(
        r"\b(?:la\s+(?:nostra|vostra|tua)\s+(?:soluzione|esperienza)"
        r"|il\s+(?:tuo|vostro)\s+(?:percorso|viaggio))\b"
        r"(?!\s+(?:di|verso|per|con|nel|nell|al|alla)\s+\w+)", re.I),
     "astrazione senza sostantivo concreto — di che percorso? di che "
     "esperienza? nomina la cosa reale"),
    ("impalcatura generica", re.compile(
        r"\b(?:un\s+buon\s+punto\s+di\s+partenza"
        r"|(?:questo\s+)?e['è]\s+(?:il\s+momento\s+giusto|un\s+buon\s+momento)"
        r"|inizi(?:a|ano)\s+a\s+prendere\s+forma"
        r"|dai\s+(?:una\s+prima|un['’]altra)\s+occhiata"
        r"|fa\s+(?:ancora\s+)?parte\s+dei\s+tuoi\s+programmi"
        r"|aggiung(?:i|ilo)\s+[^.\n]{0,40}\s+al\s+tuo\s+itinerario)\b", re.I),
     "ponte generico — nomina occasione, oggetto e azione concreta"),
    ("specificita' apparente", re.compile(
        r"\b(?:informazioni\s+utili"
        r"|l['’]opzione\s+piu['ù]\s+adatta"
        r"|tutto\s+(?:quello|cio['ò])\s+che\s+ti\s+serve)\b", re.I),
     "sembra specifico ma manca il referente — indica quali informazioni, "
     "quale criterio o quale risultato"),
    ("residuo assistente", re.compile(
        r"\b(?:certo[,.:!]?(?:\s+ecco)?|ecco\s+(?:i|le)\s+"
        r"(?:copy|proposte)|di\s+seguito\s+trovi|come\s+richiesto)\b", re.I),
     "meta-testo della conversazione — rimuovilo dal deliverable"),
    ("generic scaffold EN", re.compile(
        r"\b(?:a\s+good\s+place\s+to\s+start"
        r"|start\s+with\s+the\b"
        r"|take\s+(?:a\s+first|another|one\s+more)\s+look"
        r"|part\s+of\s+your\s+plans"
        r"|fits?\s+into\s+your\s+(?:trip|journey|routine|day)"
        r"|useful\s+(?:information|updates)"
        r"|the\s+option\s+that\s+fits\s+your)\b", re.I),
     "formula inglese grammaticalmente corretta ma generica — transcreate "
     "con category entry point e azione concreti"),
]


# ---- Ponti ammessi (lista bianca) -----------------------------------
# Fonte: references/10-parlato-ritmo-e-ponti.md R3, decisi da Matteo il
# 2026-09-25. Una riga che contiene uno di questi ponti non viene flaggata
# come 'signposted transition' ne' come 'rhetorical self-question'.
# Ripetizione e accumulo restano giudizio del reviewer.

APPROVED_BRIDGES = [
    "senti,", "guarda,", "ti spiego una cosa", "pensa a questo",
    "e sai qual e' il punto", "cioe', nella pratica",
    "ti faccio un esempio", "e questo significa che", "il punto e' che",
    "e li' e' dove cambia tutto", "ma c'e' un altro aspetto",
    "e questo porta a un altro problema",
    "e sai qual e' la cosa interessante",
    "ed e' esattamente per questo che", "e sai cosa succede",
    "e il conto arriva sempre",
]

BRIDGE_EXEMPT = {"signposted transition", "rhetorical self-question"}

# Connettivi che aprono un blocco collegandolo al precedente (check di
# documento, non di riga).
OPENING_CONNECTIVE = re.compile(
    r"^(?:e\b|ma\b|perche'|quindi\b|poi\b|allora\b|senti\b|guarda\b|"
    r"cioe'|ed\b|pensa\b|ti\s+spiego|ti\s+faccio|il\s+punto\s+e')", re.I)

# Etichetta di chi parla a inizio cella (dialogo a due voci): "A:", "**B:**".
SPEAKER_LABEL = re.compile(r"^\W*[A-Z]\s*:")

ACCENTS = str.maketrans({
    "\u00e0": "a'", "\u00e8": "e'", "\u00e9": "e'", "\u00ec": "i'",
    "\u00f2": "o'", "\u00f3": "o'", "\u00f9": "u'", "\u2019": "'",
})

# ---- Passivo e nominalizzazione (warning) ---------------------------

PASSIVE_PATTERNS = [
    ("passivo", re.compile(
        r"\b(?:viene|vengono)\s+\w+(?:at[oaie]|ut[oaie]|it[oaie])\b", re.I),
     "passivo con 'venire' — rimetti chi fa la cosa "
     "(10-parlato-ritmo-e-ponti.md R8)"),
    ("passivo", re.compile(
        r"\b(?:e'|\u00e8|sono|era|erano)\s+stat[oaie]\s+"
        r"\w+(?:at[oaie]|ut[oaie]|it[oaie])\b", re.I),
     "passivo con 'essere' — nel parlato il soggetto agisce (R8)"),
    ("nominalizzazione", re.compile(
        r"\b(?:la|il|lo|l')\s*(?!momento\b|commento\b)"
        r"\w{2,}(?:ione|mento|enza|anza)\s+"
        r"(?:di|del|della|dei|delle|degli|dell')\b", re.I),
     "nome astratto al posto del verbo — 'la gestione comporta' diventa "
     "'se gestisci male' (R8)"),
]

WARNING_NAMES = {"passivo", "nominalizzazione", "aforisma per eco",
                 "ritmo piatto", "ponte mancante tra i blocchi"}

SENTENCE_SPLIT = re.compile(r"[.!?\u2026]+")


def normalize(text):
    """lowercase + accenti resi come nei reference (e' invece di e)."""
    return " ".join(text.lower().translate(ACCENTS).split())


def spoken_cell(line):
    """Estrae la colonna del parlato da una riga di tabella.

    Tabella 1: Module | Cosa devi dire | ...
    Tabella 2: Module | Selling Block | Cosa devi dire | ...
    Fuori tabella restituisce la riga intera.
    """
    stripped = line.strip()
    if not stripped.startswith("|"):
        return stripped
    cells = [c.strip() for c in stripped.strip("|").split("|")]
    if len(cells) < 3 or set(stripped) <= set("|-: "):
        return ""
    if cells[1].lower().startswith("cosa devi dire"):
        return ""
    return cells[2] if len(cells) >= 5 else cells[1]


def sentences(text):
    return [s.strip() for s in SENTENCE_SPLIT.split(text) if s.strip()]


def last_word(sentence):
    words = re.findall(r"[a-z\u00e0-\u00f9']{2,}", sentence.lower())
    return words[-1] if words else ""


def check_rhythm(cell):
    """Warning di ritmo sul solo parlato: aforisma per eco e ritmo piatto."""
    flags = []
    sents = sentences(cell)
    counts = [len(s.split()) for s in sents]
    for i in range(len(sents) - 1):
        if counts[i] <= 9 and counts[i + 1] <= 9:
            a, b = last_word(sents[i]), last_word(sents[i + 1])
            if a and a == b:
                flags.append((
                    "aforisma per eco",
                    f"{sents[i]}. {sents[i + 1]}.",
                    "due frasi brevi che chiudono sulla stessa parola — "
                    "verifica se e' un aforisma (AP-21) o ripetizione voluta"))
                break
    if len(counts) >= 4 and max(counts) - min(counts) <= 2:
        flags.append((
            "ritmo piatto",
            f"{len(counts)} frasi da {min(counts)}-{max(counts)} parole",
            "alterna frasi brevi e lunghe (AP-24, "
            "10-parlato-ritmo-e-ponti.md R5)"))
    return flags


def check_bridges(lines):
    """Check di documento: nessun blocco dopo Body 1 apre con un connettivo.

    Si salta nei dialoghi: se la maggior parte dei blocchi apre con l'etichetta
    di chi parla (A:, B:), il collegamento e' la risposta all'altro e lo giudica
    il reviewer (10-parlato-ritmo-e-ponti.md R3).
    """
    bodies = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 3:
            continue
        m = re.match(r"body\s*(\d+)$", cells[0], re.I)
        if m and int(m.group(1)) >= 2:
            cell = spoken_cell(line)
            if cell:
                bodies.append(cell)
    if len(bodies) < 2:
        return []
    labelled = sum(1 for c in bodies if SPEAKER_LABEL.match(c))
    if labelled * 2 >= len(bodies):
        return []
    if any(OPENING_CONNECTIVE.match(normalize(c)) for c in bodies):
        return []
    return [("ponte mancante tra i blocchi",
             f"{len(bodies)} blocchi dopo Body 1",
             "nessun blocco apre collegandosi al precedente: leggi le "
             "giunture (AP-22, 10-parlato-ritmo-e-ponti.md R2)")]


def check_line(line):
    flags = []
    low = line.lower()
    words = re.findall(r"[a-zà-ù'-]+", low)
    hits = sorted({w for w in words if w in FLAGGED_WORDS})
    if hits:
        flags.append(("vocabolario AI", ", ".join(hits),
                      "flagged-word — giudica densita', non un colpo singolo"))
    for phrase in FLAGGED_PHRASES:
        if phrase in low:
            flags.append(("frase brochure", phrase,
                          "espressione tipica da copywriter/brochure"))
    norm = normalize(line)
    bridge_exempt = any(b in norm for b in APPROVED_BRIDGES)
    for name, rx, note in PATTERNS:
        m = rx.search(line)
        if m:
            if bridge_exempt and name in BRIDGE_EXEMPT:
                continue
            flags.append((name, m.group(0).strip(), note))
    cell = spoken_cell(line)
    if cell:
        for name, rx, note in PASSIVE_PATTERNS:
            m = rx.search(cell)
            if m:
                flags.append((name, m.group(0).strip(), note))
        flags.extend(check_rhythm(cell))
    # em-dash cadence: 2+ trattini in una riga
    if line.count("—") + line.count(" – ") >= 2:
        flags.append(("em-dash cadence", "—…—",
                      "clausole drammatiche impilate sui trattini"))
    # trattino lungo singolo — non-negoziabile #1
    if "—" in line:
        flags.append(("em-dash", "—",
                      "trattino lungo (non-negoziabile 02-writing-principles §2)"))
    # En-dash: ammesso in intervalli e coppie reali, vietato come pausa.
    if " – " in line:
        flags.append(("en-dash di punteggiatura", " – ",
                      "usa virgola, punto o due punti; conserva l'en-dash "
                      "solo in intervalli o coppie senza spazi"))
    # triplet bilanciato: X, Y e Z di lunghezza simile
    trip = re.search(
        r"\b([a-zà-ù]{3,13}),\s+([a-zà-ù]{3,13})\s+e\s+([a-zà-ù]{3,13})\b",
        line, re.I)
    if trip:
        lens = [len(g) for g in trip.groups()]
        if max(lens) - min(lens) <= 3:
            flags.append(("triplet bilanciato", trip.group(0),
                          "rule-of-three troppo pulita — spezza il ritmo se "
                          "la lista e' reale"))
    # quote mix curly/straight (solo virgolette doppie, non apostrofi)
    has_curly_double = "“" in line or "”" in line
    has_straight_double = '"' in line
    if has_curly_double and has_straight_double:
        flags.append(("quote mix", "virgolette miste",
                      "scegli uno stile virgolette (curly o dritte)"))
    return flags


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[0])
        print("usage: voice-lint.py DRAFT_FILE")
        return 2
    with open(argv[1], encoding="utf-8") as f:
        text = f.read()
    total, report, warnings = 0, [], []
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        for name, evidence, note in check_line(line):
            entry = f'  L{i} [{name}] "{evidence}" — {note}'
            if name in WARNING_NAMES:
                warnings.append(entry)
            else:
                total += 1
                report.append(entry)
    for name, evidence, note in check_bridges(lines):
        warnings.append(f'  [{name}] "{evidence}" — {note}')
    n_lines = max(1, sum(1 for l in lines if l.strip()))
    density = total / n_lines
    print(f"voice-lint: {total} flag(s) su {n_lines} righe non-vuote "
          f"(density {density:.2f})")
    for r in report:
        print(r)
    if total == 0:
        print("  clean al layer meccanico — il judgment pass resta")
    if warnings:
        print(f"voice-lint: {len(warnings)} warning(s) di ritmo e forma "
              f"(non contano nella density, non bloccano)")
        for w in warnings:
            print(w)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
