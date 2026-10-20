import os

COMPARE_SCRIPT = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\scripts\compare-dim.py"

with open(COMPARE_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update clean_req
old_clean = '''def clean_req(r: dict) -> dict:
    p = r.get("path") or ""
    # Mask dynamic query tokens
    p = re.sub(r"__RequestVerificationToken=[^&]+", "__RequestVerificationToken=MASKED", p)
    p = re.sub(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", "GUID-MASKED", p)
    p = re.sub(r"\\b20\\d{2}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?Z?\\b", "TIMESTAMP-MASKED", p)
    return {
        "method": (r.get("method") or "GET").upper(),
        "path": p,
        "rawPath": r.get("path") or "",
        "status": r.get("status")
    }'''

new_clean = '''def clean_req(r: dict) -> dict:
    p = r.get("path") or ""
    # Mask dynamic query tokens
    p = re.sub(r"__RequestVerificationToken=[^&]+", "__RequestVerificationToken=MASKED", p)
    p = re.sub(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", "GUID-MASKED", p)
    p = re.sub(r"\\b20\\d{2}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?Z?\\b", "TIMESTAMP-MASKED", p)

    query_params = {}
    base_path = p
    if "?" in p:
        base_path, qs = p.split("?", 1)
        for part in qs.split("&"):
            if "=" in part:
                k, v = part.split("=", 1)
                query_params[k] = v
            elif part:
                query_params[part] = ""

    post_data = r.get("postData") or r.get("params") or ""

    return {
        "method": (r.get("method") or "GET").upper(),
        "path": p,
        "basePath": base_path,
        "queryParams": query_params,
        "postData": str(post_data),
        "rawPath": r.get("path") or "",
        "status": r.get("status")
    }'''

code = code.replace(old_clean, new_clean)

# 2. Update load_report
old_load = '''                "durationMs": t.get("durationMs"),
                "error": t.get("error") or "",
                "network": t.get("network") or [],
                "disposition": t.get("disposition") or ""'''

new_load = '''                "durationMs": t.get("durationMs"),
                "error": t.get("error") or "",
                "observedRoute": t.get("observedRoute") or "",
                "flow": t.get("flow") or [],
                "network": t.get("network") or [],
                "disposition": t.get("disposition") or ""'''

code = code.replace(old_load, new_load)

# 3. Update compare_network aligned building
old_aligned = '''        aligned.append({
            "index": idx + 1,
            "stg4": r4,
            "stg10": r10,
            "match": match
        })'''

new_aligned = '''        param_diffs = []
        if r4 and r10:
            keys = sorted(set(r4.get("queryParams", {}).keys()).union(set(r10.get("queryParams", {}).keys())))
            for k in keys:
                v4 = r4.get("queryParams", {}).get(k)
                v10 = r10.get("queryParams", {}).get(k)
                param_diffs.append({
                    "param": k,
                    "type": "QUERY",
                    "stg4": v4 if v4 is not None else "(none)",
                    "stg10": v10 if v10 is not None else "(none)",
                    "match": (v4 == v10)
                })
            pd4 = r4.get("postData") or ""
            pd10 = r10.get("postData") or ""
            if pd4 or pd10:
                param_diffs.append({
                    "param": "BODY_PAYLOAD",
                    "type": "BODY",
                    "stg4": pd4 if pd4 else "(none)",
                    "stg10": pd10 if pd10 else "(none)",
                    "match": (pd4 == pd10)
                })

        aligned.append({
            "index": idx + 1,
            "stg4": r4,
            "stg10": r10,
            "match": match,
            "paramDiffs": param_diffs
        })'''

code = code.replace(old_aligned, new_aligned)

# 4. Update t_res in main()
old_tres = '''        t_res = {
            "key": k,
            "screen": screen,
            "tc": tc,
            "scenario": scenario,
            "file": file_path,
            "dimension": dim,
            "verdict": verdict,'''

new_tres = '''        playwright_inputs = []
        for step in (ref.get("flow") or []):
            title = step.get("title") or ""
            if title:
                playwright_inputs.append({
                    "title": title,
                    "category": step.get("category") or "",
                    "durationMs": step.get("durationMs") or 0
                })

        t_res = {
            "key": k,
            "screen": screen,
            "tc": tc,
            "scenario": scenario,
            "file": file_path,
            "dimension": dim,
            "observedRoute": ref.get("observedRoute") or "",
            "playwrightInputs": playwright_inputs,
            "verdict": verdict,'''

code = code.replace(old_tres, new_tres)

with open(COMPARE_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated compare-dim.py with parameter comparison successfully.")
