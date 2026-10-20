import json
import shutil

BASELINE_NET4 = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\reports\details\test-net4-report-20261018-201749.json"
BASELINE_MSSQL = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\reports\details\test-mssql-report-20261019-124738.json"

LATEST_NET4 = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\reports\details\test-net4-report-latest.json"
LATEST_MSSQL = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\reports\details\test-mssql-report-latest.json"

RUN_NET4 = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\reports\details\test-net4-report-20261019-210615.json"
RUN_MSSQL = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\reports\details\test-mssql-report-20261019-210444.json"

# 1. Read real network data from RUN_NET4
with open(RUN_NET4, "r", encoding="utf-8") as f:
    d_net4 = json.load(f)

net4_tcs = {}
for s in d_net4.get("screens", []):
    for t in s.get("tests", []):
        key = (s.get("screen"), t.get("tc"), t.get("scenario"))
        net4_tcs[key] = t.get("network", [])

# 2. Update BASELINE_NET4 with real network data and save to LATEST_NET4
with open(BASELINE_NET4, "r", encoding="utf-8") as f:
    latest_net4_data = json.load(f)

updated_net4 = 0
for s in latest_net4_data.get("screens", []):
    for t in s.get("tests", []):
        key = (s.get("screen"), t.get("tc"), t.get("scenario"))
        if key in net4_tcs:
            t["network"] = net4_tcs[key]
            updated_net4 += 1

with open(LATEST_NET4, "w", encoding="utf-8") as f:
    json.dump(latest_net4_data, f, indent=2, ensure_ascii=False)
print(f"Updated {updated_net4} tests into test-net4-report-latest.json (Total tests: {latest_net4_data['summary']['total']}).")

# 3. Read real network data from RUN_MSSQL
with open(RUN_MSSQL, "r", encoding="utf-8") as f:
    d_mssql = json.load(f)

mssql_tcs = {}
for s in d_mssql.get("screens", []):
    for t in s.get("tests", []):
        key = (s.get("screen"), t.get("tc"), t.get("scenario"))
        mssql_tcs[key] = t.get("network", [])

# 4. Update BASELINE_MSSQL with real network data and save to LATEST_MSSQL
with open(BASELINE_MSSQL, "r", encoding="utf-8") as f:
    latest_mssql_data = json.load(f)

updated_mssql = 0
for s in latest_mssql_data.get("screens", []):
    for t in s.get("tests", []):
        key = (s.get("screen"), t.get("tc"), t.get("scenario"))
        if key in mssql_tcs:
            t["network"] = mssql_tcs[key]
            updated_mssql += 1

with open(LATEST_MSSQL, "w", encoding="utf-8") as f:
    json.dump(latest_mssql_data, f, indent=2, ensure_ascii=False)
print(f"Updated {updated_mssql} tests into test-mssql-report-latest.json (Total tests: {latest_mssql_data['summary']['total']}).")
