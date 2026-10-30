#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

def run_eval(suite_path, out_html):
    with open(suite_path, "r", encoding="utf-8") as f:
        suite = json.load(f)

    tests = suite.get("eval_cases", [])
    passed = 0
    results = []

    for t in tests:
        name = t.get("case_name")
        output = t.get("mock_model_output", {})
        req_keys = t.get("required_json_keys", [])

        missing = [k for k in req_keys if k not in output]
        ok = (len(missing) == 0)
        if ok:
            passed += 1

        results.append({
            "case": name,
            "status": "PASS" if ok else "FAIL",
            "missing_keys": missing
        })

    pass_rate = (passed / max(len(tests), 1)) * 100
    rows = "".join([f"<tr><td>{r['case']}</td><td><strong style='color:{'green' if r['status']=='PASS' else 'red'}'>{r['status']}</strong></td><td>{r['missing_keys']}</td></tr>" for r in results])
    html = f"""<!DOCTYPE html><html><head><meta charset='utf-8'><title>Prompt Regression Report</title><style>body{{font-family:sans-serif;padding:2rem;background:#0f172a;color:#fff}}table{{width:100%;border-collapse:collapse}}th,td{{padding:10px;border:1px solid #334155}}th{{background:#0284c7}}</style></head><body><h1>Marketing Prompt Regression Evaluation Suite</h1><p>Pass Rate: <strong>{round(pass_rate, 1)}%</strong> ({passed}/{len(tests)} cases passed)</p><table><tr><th>Test Case</th><th>Status</th><th>Defects</th></tr>{rows}</table></body></html>"""
    Path(out_html).parent.mkdir(parents=True, exist_ok=True)
    Path(out_html).write_text(html, encoding="utf-8")
    return {"passed": passed, "total": len(tests), "pass_rate": pass_rate}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--suite", required=True)
    p.add_argument("--report", default="reports/sample_eval_report.html")
    args = p.parse_args()

    r = run_eval(args.suite, args.report)
    print(f"Prompt regression eval complete: {r} -> {args.report}")

if __name__ == "__main__":
    main()
