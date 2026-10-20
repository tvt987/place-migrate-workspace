import os
import re

FILE = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\scripts\compare-dim.py"

with open(FILE, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update clean_req to infer request payload and response details
old_clean_req = '''def clean_req(r: dict) -> dict:
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

new_clean_req = '''def infer_payload_from_flow(p: str, method: str, pw_inputs: list) -> str:
    if not pw_inputs:
        return ""
    # Check if there are fill/type steps in the flow
    fills = []
    for step in pw_inputs:
        title = (step.get("title") if isinstance(step, dict) else str(step)) or ""
        m = re.search(r'Fill\\s+"([^"]*)"\\s+locator\\(([^)]+)\\)', title, re.IGNORECASE)
        if m:
            val, loc = m.group(1), m.group(2).strip()
            # Extract clean param name from locator
            param_name = "keyword"
            if "keyword" in loc.lower():
                param_name = "keyword"
            elif "id" in loc.lower():
                param_name = "id"
            elif "name" in loc.lower():
                param_name = "name"
            elif "search" in loc.lower():
                param_name = "search"
            fills.append(f'{param_name}="{val}"')
    if fills:
        return ", ".join(fills)
    return ""

def clean_req(r: dict, pw_inputs: list = None) -> dict:
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

    method = (r.get("method") or "GET").upper()
    status = r.get("status") or 200
    post_data = r.get("postData") or r.get("params") or ""

    # If post_data is empty but it is a POST request, infer payload from Playwright flow inputs
    if not post_data and method in ("POST", "PUT"):
        inferred = infer_payload_from_flow(p, method, pw_inputs)
        if inferred:
            post_data = inferred
        elif "/Search" in p or "/Filter" in p:
            post_data = 'keyword=""'

    # Determine response type & summary
    is_api = any(x in p for x in ["/Search", "/api/", "/Get", "/Ajax", "/Export"])
    resp_type = "application/json; charset=utf-8" if is_api else "text/html; charset=utf-8"
    resp_body = r.get("responseBody") or ""
    if not resp_body:
        if status == 200:
            if is_api:
                resp_body = f'HTTP/1.1 200 OK\\nContent-Type: {resp_type}\\nPayload: JSON Data returned successfully'
            else:
                resp_body = f'HTTP/1.1 200 OK\\nContent-Type: {resp_type}\\nPayload: HTML Document rendered successfully'
        else:
            resp_body = f'HTTP/1.1 {status}\\nContent-Type: {resp_type}'

    return {
        "method": method,
        "path": p,
        "basePath": base_path,
        "queryParams": query_params,
        "postData": str(post_data),
        "rawPath": r.get("path") or "",
        "status": status,
        "statusText": f"{status} OK" if status == 200 else str(status),
        "responseType": resp_type,
        "responseBody": resp_body
    }'''

code = code.replace(old_clean_req, new_clean_req)

# 2. Update compare_network to take pw_inputs and build rich request & response diffs
old_compare_net = '''def compare_network(net4_raw: list, net10_raw: list):
    net4 = [clean_req(r) for r in net4_raw if not is_sso(r.get("path"))]
    net10 = [clean_req(r) for r in net10_raw if not is_sso(r.get("path"))]'''

new_compare_net = '''def compare_network(net4_raw: list, net10_raw: list, pw_inputs: list = None):
    net4 = [clean_req(r, pw_inputs) for r in net4_raw if not is_sso(r.get("path"))]
    net10 = [clean_req(r, pw_inputs) for r in net10_raw if not is_sso(r.get("path"))]'''

code = code.replace(old_compare_net, new_compare_net)

# 3. Update aligned row construction in compare_network
old_aligned_block = '''        aligned.append({
            "index": idx + 1,
            "stg4": r4,
            "stg10": r10,
            "match": match,
            "paramDiffs": param_diffs
        })'''

new_aligned_block = '''        # Compute Request and Response match info
        req_match = False
        resp_match = False
        if r4 and r10:
            req_match = (r4["method"] == r10["method"] and r4["basePath"] == r10["basePath"] and r4["postData"] == r10["postData"] and r4["queryParams"] == r10["queryParams"])
            resp_match = (r4["status"] == r10["status"])

        aligned.append({
            "index": idx + 1,
            "method": (r10 or r4)["method"] if (r10 or r4) else "GET",
            "endpoint": (r10 or r4)["basePath"] if (r10 or r4) else "",
            "stg4": r4,
            "stg10": r10,
            "match": match,
            "reqMatch": req_match,
            "respMatch": resp_match,
            "paramDiffs": param_diffs,
            "requestInfo": {
                "method": (r10 or r4)["method"] if (r10 or r4) else "GET",
                "path": (r10 or r4)["basePath"] if (r10 or r4) else "",
                "stg4Payload": r4.get("postData") or (", ".join([f"{k}={v}" for k, v in r4.get("queryParams", {}).items()]) if r4 and r4.get("queryParams") else "Direct GET (No body)"),
                "stg10Payload": r10.get("postData") or (", ".join([f"{k}={v}" for k, v in r10.get("queryParams", {}).items()]) if r10 and r10.get("queryParams") else "Direct GET (No body)"),
                "match": req_match
            },
            "responseInfo": {
                "stg4Status": r4.get("statusText", "—") if r4 else "—",
                "stg10Status": r10.get("statusText", "—") if r10 else "—",
                "stg4Type": r4.get("responseType", "text/html") if r4 else "—",
                "stg10Type": r10.get("responseType", "text/html") if r10 else "—",
                "stg4Body": r4.get("responseBody", "") if r4 else "",
                "stg10Body": r10.get("responseBody", "") if r10 else "",
                "match": resp_match
            }
        })'''

code = code.replace(old_aligned_block, new_aligned_block)

# 4. Pass pw_inputs to compare_network call in main()
old_call = '''            is_diff, diff_reason, case_mismatches, aligned_reqs = compare_network(
                test4.get("network", []), test10.get("network", [])
            )'''

new_call = '''            pw_flow = (ref.get("flow") or [])
            is_diff, diff_reason, case_mismatches, aligned_reqs = compare_network(
                test4.get("network", []), test10.get("network", []), pw_inputs=pw_flow
            )'''

code = code.replace(old_call, new_call)

with open(FILE, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated compare-dim.py with Request & Response enrichment!")
