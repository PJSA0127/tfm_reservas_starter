#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

EXPECTED = {
    "tfm.asvs.v121.jinja-safe-filter",
    "tfm.asvs.v121.explicit-markup",
    "tfm.asvs.v124.raw-sql-fstring",
    "tfm.asvs.v124.raw-sql-concatenation",
    "tfm.asvs.v351.csrf-exempt-route",
    "tfm.asvs.v353.get-route-commits-state",
}


def normalize_rule_id(check_id: str) -> str:
    """Normalize Semgrep IDs that are namespaced by the config file path."""
    for expected in EXPECTED:
        if check_id == expected or check_id.endswith("." + expected):
            return expected
    return check_id


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_semgrep_rule_validation.py <semgrep-json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Semgrep JSON not found: {path}", file=sys.stderr)
        return 2

    report = json.loads(path.read_text(encoding="utf-8"))
    results = report.get("results") or []
    errors = report.get("errors") or []

    actual = {normalize_rule_id(str(r.get("check_id", ""))) for r in results}
    actual.discard("")

    missing = sorted(EXPECTED - actual)
    unexpected = sorted(actual - EXPECTED)

    print("Semgrep synthetic rule validation")
    print("================================")
    print(f"Findings total : {len(results)}")
    print(f"Unique rules   : {len(actual)}")
    print(f"Errors         : {len(errors)}")

    for rule_id in sorted(actual):
        print(f"PASS: {rule_id}")

    if missing:
        print("\nMissing expected rules:")
        for rule_id in missing:
            print(f"  - {rule_id}")

    if unexpected:
        print("\nUnexpected rules:")
        for rule_id in unexpected:
            print(f"  - {rule_id}")

    if errors:
        print("\nSemgrep reported engine/parser errors.")

    if missing or unexpected or errors or len(results) != 6:
        print("\nSynthetic rule gate: FAIL")
        return 1

    print("\nSynthetic rule gate: PASS (6/6 rules detected exactly once).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
