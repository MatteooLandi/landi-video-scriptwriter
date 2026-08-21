#!/usr/bin/env python3
"""
Test regressione per la skill video-ads-script-writer.

Legge tutti i fixture in ../fixtures/, estrae exit code atteso dal frontmatter,
esegue i 4 linter e verifica che l'exit code combaci.

Uso:
    python3 evals/run.py                 # esegue tutti i test
    python3 evals/run.py --verbose       # mostra output linter
    python3 evals/run.py fixtures/01-ugc-clean.md  # solo un file

Exit code:
    0 = tutti i test passati
    1 = almeno un test fallito
"""

import re
import subprocess
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
FIXTURES_DIR = SKILL_ROOT / "fixtures"
SCRIPTS_DIR = SKILL_ROOT / "scripts"
BRAND_CONTEXT = SKILL_ROOT / "brand-context"

LINTERS = [
    ("format-lint",     ["python3", str(SCRIPTS_DIR / "format-lint.py"), None]),
    ("hook-lint",       ["python3", str(SCRIPTS_DIR / "hook-lint.py"), None, str(SKILL_ROOT)]),
    ("voice-lint",      ["python3", str(SCRIPTS_DIR / "voice-lint.py"), None]),
    ("grounding-check", ["python3", str(SCRIPTS_DIR / "grounding-check.py"), None, str(SKILL_ROOT)]),
]

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def parse_frontmatter(path: Path) -> dict:
    """Extract fixture: {...} block from YAML frontmatter."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    fm = match.group(1)
    expected = {}
    in_fixture = False
    for line in fm.splitlines():
        stripped = line.strip()
        if stripped == "fixture:":
            in_fixture = True
            continue
        if in_fixture:
            if not line.startswith("  "):
                break
            m = re.match(r"\s+([a-z-]+):\s*(\d+)", line)
            if m:
                expected[m.group(1)] = int(m.group(2))
    return expected


def run_linter(name: str, cmd_template: list, fixture_path: Path, verbose: bool) -> int:
    """Run one linter on fixture, return actual exit code."""
    cmd = [str(fixture_path) if arg is None else arg for arg in cmd_template]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if verbose:
        print(f"    {BLUE}[{name}]{RESET} exit={result.returncode}")
        if result.stdout:
            print("    " + result.stdout.replace("\n", "\n    "))
    return result.returncode


def test_fixture(fixture_path: Path, verbose: bool) -> tuple[int, int]:
    """Run all linters on one fixture. Return (passed, total)."""
    expected = parse_frontmatter(fixture_path)
    if not expected:
        print(f"  {YELLOW}skip{RESET} (no fixture: block in frontmatter)")
        return (0, 0)

    passed = 0
    total = 0
    for name, cmd in LINTERS:
        if name not in expected:
            continue
        total += 1
        actual = run_linter(name, cmd, fixture_path, verbose)
        exp = expected[name]
        if actual == exp:
            print(f"  {GREEN}pass{RESET}  {name:<18} exit={actual} (expected {exp})")
            passed += 1
        else:
            print(f"  {RED}FAIL{RESET}  {name:<18} exit={actual} (expected {exp})")
    return (passed, total)


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("-")]

    if args:
        fixtures = [Path(a) for a in args]
    else:
        fixtures = sorted(FIXTURES_DIR.glob("*.md"))
        fixtures = [f for f in fixtures if f.name != "README.md"]

    if not fixtures:
        print(f"{RED}Nessun fixture trovato in {FIXTURES_DIR}{RESET}")
        sys.exit(1)

    print(f"Running {len(fixtures)} fixture(s) against {len(LINTERS)} linter(s)\n")

    tot_passed = 0
    tot_total = 0
    failed_files = []
    for fx in fixtures:
        print(f"{BLUE}{fx.name}{RESET}")
        p, t = test_fixture(fx, verbose)
        tot_passed += p
        tot_total += t
        if p < t:
            failed_files.append(fx.name)
        print()

    print("=" * 60)
    if tot_passed == tot_total:
        print(f"{GREEN}✓ {tot_passed}/{tot_total} check(s) passed{RESET}")
        sys.exit(0)
    else:
        print(f"{RED}✗ {tot_passed}/{tot_total} passed. Fixtures falliti:{RESET}")
        for f in failed_files:
            print(f"  - {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()
