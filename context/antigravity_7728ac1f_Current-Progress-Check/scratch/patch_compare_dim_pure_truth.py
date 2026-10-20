import re

FILE = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\scripts\compare-dim.py"

with open(FILE, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Replace infer_payload_from_flow + clean_req with pure Playwright extraction
old_clean_section = '''def infer_payload_from_flow(p: str, method: str, pw_inputs: list) -> str:
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

new_clean_section = '''def clean_req(r: dict) -> dict:
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

    # LẤY NGUYÊN GỐC TỪ PLAYWRIGHT, TUYỆT ĐỐI KHÔNG GIẢ ĐỊNH HOẶC TỰ BỊA DỮ LIỆU
    post_data = r.get("requestPayload") or r.get("postData") or r.get("params") or ""
    resp_body = r.get("responseBody") or ""

    is_api = any(x in p for x in ["/Search", "/api/", "/Get", "/Ajax", "/Export"])
    resp_type = "application/json" if is_api else "text/html"

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

if old_clean_section in code:
    code = code.replace(old_clean_section, new_clean_section)
    print("Replaced clean_req with pure Playwright extraction.")
else:
    print("Warning: old_clean_section not found!")

# 2. Update compare_network signature
old_sig = 'def compare_network(net4_raw: list, net10_raw: list, pw_inputs: list = None):'
new_sig = 'def compare_network(net4_raw: list, net10_raw: list):'
code = code.replace(old_sig, new_sig)
code = code.replace('clean_req(r, pw_inputs)', 'clean_req(r)')

# 3. Update requestInfo and responseInfo to strictly reflect Playwright reality
old_aligned_info = '''            "requestInfo": {
                "method": (r10 or r4)["method"] if (r10 or r4) else "GET",
                "path": (r10 or r4)["basePath"] if (r10 or r4) else "",
                "stg4Payload": (r4.get("postData") or (", ".join([f"{k}={v}" for k, v in r4.get("queryParams", {}).items()]) if r4.get("queryParams") else "Direct GET (No body)")) if r4 else "— (No request on STG4)",
                "stg10Payload": (r10.get("postData") or (", ".join([f"{k}={v}" for k, v in r10.get("queryParams", {}).items()]) if r10.get("queryParams") else "Direct GET (No body)")) if r10 else "— (No request on STG10)",
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
            }'''

new_aligned_info = '''            "requestInfo": {
                "method": (r10 or r4)["method"] if (r10 or r4) else "GET",
                "path": (r10 or r4)["basePath"] if (r10 or r4) else "",
                "stg4Payload": (r4.get("postData") or (("?" + "&".join([f"{k}={v}" for k, v in r4.get("queryParams", {}).items()])) if r4.get("queryParams") else ("GET (Không có query params)" if r4.get("method") == "GET" else "(Playwright ghi nhận: body rỗng / không có payload)"))) if r4 else "— (Không có request trên STG4)",
                "stg10Payload": (r10.get("postData") or (("?" + "&".join([f"{k}={v}" for k, v in r10.get("queryParams", {}).items()])) if r10.get("queryParams") else ("GET (Không có query params)" if r10.get("method") == "GET" else "(Playwright ghi nhận: body rỗng / không có payload)"))) if r10 else "— (Không có request trên STG10)",
                "match": req_match
            },
            "responseInfo": {
                "stg4Status": r4.get("statusText", "—") if r4 else "—",
                "stg10Status": r10.get("statusText", "—") if r10 else "—",
                "stg4Type": r4.get("responseType", "text/html") if r4 else "—",
                "stg10Type": r10.get("responseType", "text/html") if r10 else "—",
                "stg4Body": r4.get("responseBody", "") if (r4 and r4.get("responseBody")) else ("(Chưa có response body ghi nhận từ Playwright cho đợt test này)" if r4 else "—"),
                "stg10Body": r10.get("responseBody", "") if (r10 and r10.get("responseBody")) else ("(Chưa có response body ghi nhận từ Playwright cho đợt test này)" if r10 else "—"),
                "match": resp_match
            }'''

if old_aligned_info in code:
    code = code.replace(old_aligned_info, new_aligned_info)
    print("Replaced aligned_info with truthful Playwright representations.")
else:
    print("Warning: old_aligned_info not matched!")

# 4. In main(): remove pw_inputs=pw_flow
old_main_call = '''            pw_flow = (ref.get("flow") or [])
            is_diff, diff_reason, case_mismatches, aligned_reqs = compare_network(
                test4.get("network", []), test10.get("network", []), pw_inputs=pw_flow
            )'''
new_main_call = '''            is_diff, diff_reason, case_mismatches, aligned_reqs = compare_network(
                test4.get("network", []), test10.get("network", [])
            )'''
code = code.replace(old_main_call, new_main_call)

with open(FILE, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated compare-dim.py successfully.")
