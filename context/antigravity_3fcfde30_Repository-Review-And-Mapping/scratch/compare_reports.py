import json
import glob
import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def find_latest_report(details_dir, prefix):
    files = sorted(glob.glob(os.path.join(details_dir, f"{prefix}-report-*.json")))
    if not files:
        latest = os.path.join(details_dir, f"{prefix}-report-latest.json")
        if os.path.exists(latest):
            return latest
        return None
    return files[-1]

def extract_tests(report_path):
    with open(report_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    tests = {}
    for screen in data.get("screens", []):
        screen_name = screen.get("screen", "")
        for t in screen.get("tests", []):
            tc = t.get("tc") or ""
            scenario = t.get("scenario") or ""
            file_path = t.get("file") or ""
            key = f"{screen_name} | {tc} | {scenario}"
            tests[key] = {
                "screen": screen_name,
                "tc": tc,
                "scenario": scenario,
                "file": file_path,
                "status": t.get("status"),
                "durationMs": t.get("durationMs"),
                "error": t.get("error")
            }
    return data.get("summary", {}), tests

def compare(net4_path, mssql_path):
    s_net4, t_net4 = extract_tests(net4_path)
    s_mssql, t_mssql = extract_tests(mssql_path)

    print(f"=== SUMMARY ===")
    print(f"NET4 (Origin STG4): Total={s_net4.get('total')}, Passed={s_net4.get('passed')}, Failed={s_net4.get('failed')}, Skipped={s_net4.get('skipped')}")
    print(f"MSSQL (Target STG10): Total={s_mssql.get('total')}, Passed={s_mssql.get('passed')}, Failed={s_mssql.get('failed')}, Skipped={s_mssql.get('skipped')}")
    print()

    regressions = []
    origin_fails = []
    improvements = []
    both_passed = []
    both_skipped = []

    all_keys = set(t_net4.keys()).union(set(t_mssql.keys()))

    for k in sorted(all_keys):
        n4 = t_net4.get(k)
        m10 = t_mssql.get(k)

        st4 = n4["status"] if n4 else "MISSING"
        st10 = m10["status"] if m10 else "MISSING"

        if st4 == "passed" and st10 in ("failed", "timedOut"):
            regressions.append((k, n4, m10))
        elif st4 in ("failed", "timedOut") and st10 in ("failed", "timedOut"):
            origin_fails.append((k, n4, m10))
        elif st4 in ("failed", "timedOut") and st10 == "passed":
            improvements.append((k, n4, m10))
        elif st4 == "passed" and st10 == "passed":
            both_passed.append(k)
        elif st4 == "skipped" and st10 == "skipped":
            both_skipped.append(k)
        else:
            # any other status differences
            regressions.append((k, n4, m10))

    out_lines = []
    def log(msg=""):
        print(msg)
        out_lines.append(msg)

    log("=== COMPARISON BREAKDOWN ===")
    log(f"1. REGRESSIONS (Lỗi Migrate: STG4 PASS nhưng STG10 FAIL/TIMEOUT/DIFF): {len(regressions)}")
    for k, n4, m10 in regressions:
        st4 = n4["status"] if n4 else "MISSING"
        st10 = m10["status"] if m10 else "MISSING"
        log(f"   [REGRESSION] {k}")
        log(f"      Status: STG4={st4} -> STG10={st10}")
        if m10:
            err_line = (m10.get('error') or '').split('\n')[0][:150]
            log(f"      STG10 Error: {err_line}")

    log()
    log(f"2. ORIGIN FAILS (Lỗi môi trường/nghiệp vụ: CẢ STG4 VÀ STG10 ĐỀU FAIL): {len(origin_fails)}")
    for k, n4, m10 in origin_fails:
        log(f"   [ORIGIN_FAIL] {k}")

    log()
    log(f"3. IMPROVEMENTS (STG4 FAIL nhưng STG10 PASS): {len(improvements)}")
    for k, n4, m10 in improvements:
        log(f"   [IMPROVEMENT] {k}")

    log()
    log(f"4. BOTH PASSED (Tương đồng thành công 1:1): {len(both_passed)}")
    log(f"5. BOTH SKIPPED (Kịch bản cùng skip): {len(both_skipped)}")

    out_path = os.path.join(details_dir, "migration_compare_result.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))
    print(f"\nWritten result to: {out_path}")

if __name__ == "__main__":
    details_dir = r"E:\Work\Place_Migrate\cci-dc-web\03_qa\reports\details"
    net4 = find_latest_report(details_dir, "test-net4")
    mssql = find_latest_report(details_dir, "test-mssql")
    print(f"Comparing:")
    print(f"  NET4 : {net4}")
    print(f"  MSSQL: {mssql}")
    print()
    compare(net4, mssql)
