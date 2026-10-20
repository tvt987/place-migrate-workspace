import os
import json
import re
from collections import Counter, defaultdict

NET4_PATH = r"e:\Work\Place_Migrate\cci-store-location-web\03_qa\reports\details\test-net4-report-latest.json"
MSSQL_PATH = r"e:\Work\Place_Migrate\cci-store-location-web\03_qa\reports\details\test-mssql-report-latest.json"

SSO_PREFIXES = ("/accounts/login", "/accounts/callback", "/accounts/refreshtoken", "/realms/master", "/protocol/openid-connect")
STATIC_EXTS = (".css", ".js", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".woff", ".woff2", ".ttf", ".eot", ".ico")
STATIC_PREFIXES = ("/content/", "/script-handler/", "/bundles/", "/scripts/", "/assets/")

def is_sso(path):
    p = (path or "").lower()
    return any(p.startswith(x) for x in SSO_PREFIXES)

def is_static(path):
    p = (path or "").lower()
    if any(p.startswith(x) for x in STATIC_PREFIXES):
        return True
    ext = os.path.splitext(p.split("?")[0])[1]
    return ext in STATIC_EXTS

def clean_req(r):
    p = r.get("path") or ""
    # Mask dynamic query params if needed
    p = re.sub(r"__RequestVerificationToken=[^&]+", "__RequestVerificationToken=MASKED", p)
    p = re.sub(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", "GUID", p)
    return {
        "method": (r.get("method") or "GET").upper(),
        "path": p,
        "status": r.get("status")
    }

def load_tests(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    tests = {}
    for s in data.get("screens", []):
        screen = s.get("screen") or "unknown"
        for t in s.get("tests", []):
            key = (screen, t.get("tc") or "", t.get("file") or "", t.get("scenario") or "")
            tests[key] = {
                "screen": screen,
                "tc": t.get("tc") or "",
                "file": t.get("file") or "",
                "scenario": t.get("scenario") or "",
                "dimension": t.get("dimension") or "CHUA-TAG",
                "status": t.get("status"),
                "durationMs": t.get("durationMs"),
                "error": t.get("error"),
                "network": t.get("network") or []
            }
    return data.get("summary", {}), tests

s4, t4 = load_tests(NET4_PATH)
s10, t10 = load_tests(MSSQL_PATH)

verdicts = Counter()
dim_verdicts = defaultdict(Counter)
case_mismatches = []
content_diffs = []

all_keys = sorted(set(t4.keys()).union(set(t10.keys())))

for k in all_keys:
    test4 = t4.get(k)
    test10 = t10.get(k)

    dim = (test10 or test4).get("dimension") or "CHUA-TAG"

    st4 = test4.get("status") if test4 else "MISSING"
    st10 = test10.get("status") if test10 else "MISSING"

    v = "UNKNOWN"
    diff_reason = ""

    if st4 == "skipped" and st10 == "skipped":
        v = "BOTH_SKIP"
    elif st4 in ("failed", "timedOut") and st10 in ("failed", "timedOut"):
        v = "ORIGIN_SAME"
    elif st4 == "passed" and st10 in ("failed", "timedOut"):
        v = "MIGRATE_BUG"
    elif st4 in ("failed", "timedOut") and st10 == "passed":
        v = "IMPROVED"
    elif st4 == "passed" and st10 == "passed":
        # Compare network
        net4 = [clean_req(r) for r in (test4.get("network") or []) if not is_sso(r.get("path"))]
        net10 = [clean_req(r) for r in (test10.get("network") or []) if not is_sso(r.get("path"))]

        # Check static case sensitivity
        stat4 = [r for r in net4 if is_static(r["path"])]
        stat10 = [r for r in net10 if is_static(r["path"])]
        stat4_paths = {r["path"].lower(): r["path"] for r in stat4}
        for r in stat10:
            low = r["path"].lower()
            if low in stat4_paths and stat4_paths[low] != r["path"]:
                case_mismatches.append((k, stat4_paths[low], r["path"]))

        # Filter to functional requests
        fn4 = [r for r in net4 if not is_static(r["path"])]
        fn10 = [r for r in net10 if not is_static(r["path"])]

        # Compare functional
        if len(fn4) != len(fn10):
            v = "CONTENT_DIFF"
            diff_reason = f"Request count mismatch: STG4={len(fn4)} vs STG10={len(fn10)}"
        else:
            mismatch = False
            for r4, r10 in zip(fn4, fn10):
                if r4["method"] != r10["method"] or r4["path"] != r10["path"] or r4["status"] != r10["status"]:
                    mismatch = True
                    diff_reason = f"Req diff: STG4={r4['method']} {r4['path']} ({r4['status']}) vs STG10={r10['method']} {r10['path']} ({r10['status']})"
                    break
            if mismatch:
                v = "CONTENT_DIFF"
            else:
                v = "PARITY_OK"
    else:
        v = "MISMATCH_STATUS"

    verdicts[v] += 1
    dim_verdicts[dim][v] += 1
    if v == "CONTENT_DIFF":
        content_diffs.append((k, diff_reason))

print("=== OVERALL VERDICTS ===")
for v, cnt in verdicts.most_common():
    print(f"  {v}: {cnt}")

print("\n=== VERDICTS BY DIMENSION ===")
for dim, cnts in sorted(dim_verdicts.items()):
    print(f"  Dimension: {dim} (Total: {sum(cnts.values())})")
    for v, c in cnts.most_common():
        print(f"     {v}: {c}")

print(f"\nCase mismatches count: {len(case_mismatches)}")
for m in case_mismatches[:5]:
    print("  ", m)

print(f"\nContent diffs count: {len(content_diffs)}")
for d in content_diffs[:5]:
    print("  ", d)
