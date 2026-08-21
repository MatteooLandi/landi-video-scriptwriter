#!/usr/bin/env python3
"""Stop hook advisory: avverte quando un brief va out senza receipts dei 4 gate.

Contratto (references/07-review-gates.md): ogni brief consegnato ha 4 receipts
in coda:
  ## Format Review: ...
  ## Hook Review: ...
  ## Voice Review: ...
  ## Grounding Review: ...

Modalita' ADVISORY (scelta utente): non blocca il turn. Emette systemMessage
in testa alla risposta:
  ⚠ Brief consegnato senza receipts — <lista mancanti>. Considera rerun con
  gate attivi (references/07-review-gates.md).

Detection: solo se l'output ha shape brief-Landi (header 'Tabella 1' o riga
'Module | Cosa devi dire | Cosa far vedere | Note per Editor'). Conversazione
normale non trippa.

Per passare a bloccante: sostituisci `"decision": null` con `"decision":
"block"` e `"systemMessage"` con `"reason"`. Vedi 07-review-gates.md sez
'Upgrade a bloccante'.

Fails open su qualsiasi parse error — un hook rotto non deve mai bloccare
la chat.
"""

import json
import re
import sys


RECEIPT_HEADERS = {
    "Format Review": re.compile(r"##\s*Format Review\s*:", re.I),
    "Hook Review": re.compile(r"##\s*Hook Review\s*:", re.I),
    "Voice Review": re.compile(r"##\s*Voice Review\s*:", re.I),
    "Grounding Review": re.compile(r"##\s*Grounding Review\s*:", re.I),
}

BRIEF_MARKERS = [
    re.compile(r"##\s*Tabella\s*1\s*[-–—]?\s*Hook", re.I),
    re.compile(r"^\s*\|?\s*Module\s*\|\s*Cosa devi dire\s*\|\s*"
               r"Cosa far vedere", re.I | re.MULTILINE),
]


def last_assistant_text(transcript_path):
    text = None
    try:
        with open(transcript_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if entry.get("type") != "assistant":
                    continue
                msg = entry.get("message") or {}
                parts = msg.get("content")
                if isinstance(parts, str):
                    text = parts
                elif isinstance(parts, list):
                    chunks = [p.get("text", "") for p in parts
                              if isinstance(p, dict) and p.get("type") == "text"]
                    if chunks:
                        text = "\n".join(chunks)
    except OSError:
        return None
    return text


def looks_like_brief(text):
    for rx in BRIEF_MARKERS:
        if rx.search(text):
            return True
    return False


def missing_receipts(text):
    return [name for name, rx in RECEIPT_HEADERS.items() if not rx.search(text)]


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    if payload.get("stop_hook_active"):
        return 0

    text = payload.get("last_assistant_message")
    if not text:
        text = last_assistant_text(payload.get("transcript_path") or "")
    if not text:
        return 0

    if not looks_like_brief(text):
        return 0

    missing = missing_receipts(text)
    if not missing:
        return 0

    # Advisory: non blocca, appende systemMessage.
    msg = (
        f"⚠ Brief consegnato senza receipts — mancano: "
        f"{', '.join(missing)}. Il contratto (references/07-review-gates.md) "
        f"richiede tutti e 4 i gate prima della consegna. "
        f"Considera rerun con gate attivi (voice-lint, hook-lint, "
        f"format-lint, grounding-check + reviewer agent)."
    )
    print(json.dumps({
        "decision": None,
        "systemMessage": msg,
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
