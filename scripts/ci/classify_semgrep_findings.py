#!/usr/bin/env python3
"""Classify Semgrep JSON without conflating findings with tool execution errors."""
from __future__ import annotations
import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: classify_semgrep_findings.py <semgrep-report.json> <classification-output.json>", file=sys.stderr)
        return 2
    report_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    if not report_path.is_file():
        print(f"Semgrep report not found: {report_path}", file=sys.stderr)
        return 2
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read Semgrep report: {exc}", file=sys.stderr)
        return 2
    results = report.get("results") or []
    errors = report.get("errors") or []
    classified = {
        "execution_status": "error" if errors else "success",
        "security_result": "findings_present" if results else "no_findings",
        "finding_count": len(results),
        "error_count": len(errors),
        "rule_ids": sorted({str(r.get("check_id", "")) for r in results if r.get("check_id")}),
        "errors": errors,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(classified, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Semgrep findings: {len(results)}")
    print(f"Semgrep errors  : {len(errors)}")
    if errors:
        print("Semgrep classification: technical execution/parser errors present.", file=sys.stderr)
        return 2
    print("Semgrep classification completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
