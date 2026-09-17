#!/usr/bin/env python3
"""Classify OWASP ZAP findings against the predefined TFM experimental scope.

A mapped security finding is experimental evidence, not a technical execution
failure. Therefore this classifier returns a non-zero status only when the
report cannot be read/parsed or another classification error occurs.

The workflow separately enforces that the safe `calibration` and `pilot`
phases contain no mapped D01/D02/D04 findings. In `proposed-definitive`, mapped
findings are preserved as results without turning successful tool execution
into a CI infrastructure failure.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

RELEVANT = {
    "40012": {"defect": "D01", "asvs": "v5.0.0-1.2.1", "expected_name": "Cross Site Scripting (Reflected)"},
    "40014": {"defect": "D01", "asvs": "v5.0.0-1.2.1", "expected_name": "Cross Site Scripting (Persistent)"},
    "40018": {"defect": "D02", "asvs": "v5.0.0-1.2.4", "expected_name": "SQL Injection"},
    "10202": {"defect": "D04", "asvs": "v5.0.0-3.5.1", "expected_name": "Absence of Anti-CSRF Tokens"},
}


def flatten_alerts(report: dict) -> list[dict]:
    rows: list[dict] = []
    for site in report.get("site", []):
        site_name = site.get("@name") or site.get("name") or ""
        for alert in site.get("alerts", []):
            plugin_id = str(alert.get("pluginid", ""))
            instances = alert.get("instances") or []
            rows.append({
                "site": site_name,
                "plugin_id": plugin_id,
                "name": alert.get("alert", ""),
                "risk": alert.get("riskdesc", ""),
                "confidence": alert.get("confidence", ""),
                "instance_count": len(instances),
                "urls": sorted({str(i.get("uri", "")) for i in instances if i.get("uri")}),
            })
    return rows


def aggregate(rows: list[dict]) -> list[dict]:
    grouped: dict[tuple[str, str], dict] = {}
    for row in rows:
        key = (row["plugin_id"], row["name"])
        if key not in grouped:
            grouped[key] = {**row, "instance_count": 0, "urls": []}
        grouped[key]["instance_count"] += row["instance_count"]
        grouped[key]["urls"] = sorted(set(grouped[key]["urls"]).union(row["urls"]))
    return sorted(grouped.values(), key=lambda item: (item["plugin_id"], item["name"]))


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: check_zap_relevant_findings.py <zap-report.json> <classification-output.json>", file=sys.stderr)
        return 2

    report_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    if not report_path.is_file():
        print(f"ZAP report not found: {report_path}", file=sys.stderr)
        return 2

    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
        alerts = aggregate(flatten_alerts(report))
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"Unable to classify ZAP report: {exc}", file=sys.stderr)
        return 2

    relevant_findings: list[dict] = []
    additional_findings: list[dict] = []
    for alert in alerts:
        scope = RELEVANT.get(alert["plugin_id"])
        if scope:
            relevant_findings.append({**alert, **scope})
        else:
            additional_findings.append(alert)

    result = {
        "execution_status": "success",
        "security_result": "mapped_findings_present" if relevant_findings else "no_mapped_findings",
        "scope_plugin_ids": sorted(RELEVANT),
        "mapped_finding_type_count": len(relevant_findings),
        "additional_finding_type_count": len(additional_findings),
        "relevant_findings": relevant_findings,
        "additional_findings": additional_findings,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("ZAP findings classification")
    print("===========================")
    if alerts:
        for alert in alerts:
            marker = "MAPPED" if alert["plugin_id"] in RELEVANT else "additional"
            print(f"[{marker}] {alert['plugin_id']} | {alert['risk']} | {alert['name']} | instances={alert['instance_count']}")
    else:
        print("No ZAP alerts were reported.")

    if relevant_findings:
        print()
        print(f"Security result: {len(relevant_findings)} mapped alert type(s) detected. Classification completed successfully.")
    else:
        print()
        print("Security result: no mapped D01/D02/D04 alert types detected. Classification completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
