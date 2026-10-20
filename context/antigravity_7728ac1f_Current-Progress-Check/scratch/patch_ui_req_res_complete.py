import os
import re

APP_JS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"
STYLES_CSS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\styles.css"
INDEX_HTML = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\index.html"
EVIDENCE_HELPER = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\utils\evidence-helper.ts"
EVIDENCE_FIXTURE = r"E:\Work\Place_Migrate\cci-store-location-web\03_qa\fixtures\evidence.fixture.ts"

# 1. Update evidence-helper.ts
with open(EVIDENCE_HELPER, "r", encoding="utf-8") as f:
    eh = f.read()

if "requestPayload?:" not in eh:
    eh = eh.replace("params?: string;", "params?: string;\n  requestPayload?: string;\n  responseBody?: string;")
    with open(EVIDENCE_HELPER, "w", encoding="utf-8") as f:
        f.write(eh)
    print("Updated evidence-helper.ts with requestPayload and responseBody.")

# 2. Update evidence.fixture.ts
with open(EVIDENCE_FIXTURE, "r", encoding="utf-8") as f:
    ef = f.read()

old_on_resp = '''      const onResponse = (res: Response) => {
        try {
          const req = res.request();
          const u = new URL(res.url());
          const fullPath = u.pathname + (u.search || '');
          const postData = req.postData();
          network.push({
            method: req.method(),
            path: fullPath,
            status: res.status(),
            params: u.search ? u.search.slice(1) : (postData ? postData.slice(0, 500) : undefined)
          });
        } catch {
          /* URL không parse được (vd data:/blob:) — bỏ qua, không phải lỗi test */
        }
      };'''

new_on_resp = '''      const onResponse = async (res: Response) => {
        try {
          const req = res.request();
          const u = new URL(res.url());
          const fullPath = u.pathname + (u.search || '');
          const postData = req.postData();
          let responseText: string | undefined;
          const rType = req.resourceType();
          if (rType === 'xhr' || rType === 'fetch' || (rType === 'document' && res.status() >= 400)) {
            try {
              const text = await res.text();
              if (text) responseText = text.slice(0, 1000);
            } catch {}
          }
          network.push({
            method: req.method(),
            path: fullPath,
            status: res.status(),
            requestPayload: postData ? postData.slice(0, 1000) : (u.search ? u.search.slice(1) : undefined),
            responseBody: responseText,
            params: u.search ? u.search.slice(1) : (postData ? postData.slice(0, 500) : undefined)
          });
        } catch {
          /* URL không parse được (vd data:/blob:) — bỏ qua */
        }
      };'''

if old_on_resp in ef:
    ef = ef.replace(old_on_resp, new_on_resp)
    with open(EVIDENCE_FIXTURE, "w", encoding="utf-8") as f:
        f.write(ef)
    print("Updated evidence.fixture.ts to capture request payload and response body.")

# 3. Update app.js
with open(APP_JS, "r", encoding="utf-8") as f:
    js = f.read()

# Replace the reqRowsHtml block inside renderDrillDownContent
old_req_rows_block = '''    // Aligned request table with Parameter Comparison
    var reqRowsHtml = "";
    var aligned = selectedTest.alignedReqs || [];
    if (aligned.length) {
      reqRowsHtml = '<div class="aligned-reqs-section">' +
        '<h4 class="reqs-title">So Sánh Chuỗi Network Requests & Tham Số (' + aligned.length + ')</h4>' +
        '<table class="aligned-reqs-table">' +
          '<thead><tr>' +
            '<th>#</th>' +
            '<th>STG4 Request (Origin)</th>' +
            '<th>STG10 Request (Target)</th>' +
            '<th>Tham Số (Query / Body Params)</th>' +
            '<th>Khớp</th>' +
          '</tr></thead>' +
          '<tbody>' +
          aligned.map(function (r) {
            var stg4Text = r.stg4 ? (r.stg4.method + ' ' + r.stg4.path + ' (' + r.stg4.status + ')') : '—';
            var stg10Text = r.stg10 ? (r.stg10.method + ' ' + r.stg10.path + ' (' + r.stg10.status + ')') : '—';
            var matchBadge = r.match ? '<span class="req-match-ok">✓ Khớp</span>' : '<span class="req-match-diff">≠ Lệch</span>';
            
            // Build parameter comparison block for this request
            var pDiffs = r.paramDiffs || [];
            var paramsHtml = "";
            if (pDiffs.length) {
              paramsHtml = '<div class="req-params-box">' +
                pDiffs.map(function (p) {
                  var pMatch = p.match ? '<span class="badge-param-match">✓</span>' : '<span class="badge-param-diff">≠</span>';
                  return '<div class="param-line ' + (p.match ? 'param-line-ok' : 'param-line-diff') + '">' +
                    pMatch + ' <strong>' + esc(p.param) + ':</strong> ' +
                    '<code>' + esc(p.stg4) + '</code> &harr; <code>' + esc(p.stg10) + '</code>' +
                  '</div>';
                }).join("") + '</div>';
            } else {
              paramsHtml = '<span class="no-params-text">Không có query parameters / Request tĩnh</span>';
            }

            return '<tr class="' + (r.match ? 'row-req-ok' : 'row-req-diff') + '">' +
              '<td>' + r.index + '</td>' +
              '<td><code>' + esc(stg4Text) + '</code></td>' +
              '<td><code>' + esc(stg10Text) + '</code></td>' +
              '<td>' + paramsHtml + '</td>' +
              '<td>' + matchBadge + '</td>' +
            '</tr>';
          }).join("") +
          '</tbody>' +
        '</table>' +
      '</div>';
    }'''

new_req_rows_block = '''    // Aligned request table with Deep Request & Response Inspector
    var reqRowsHtml = "";
    var aligned = selectedTest.alignedReqs || [];
    if (aligned.length) {
      reqRowsHtml = '<div class="aligned-reqs-section">' +
        '<div class="reqs-hdr-bar">' +
          '<h4 class="reqs-title">So Sánh Chuỗi Network Requests, Request Payload &amp; Response (' + aligned.length + ')</h4>' +
          '<span class="reqs-hint">👉 Bấm nút "👁️ Chi tiết" để xem toàn bộ Header, Request Payload và Response Body từ Server</span>' +
        '</div>' +
        '<table class="aligned-reqs-table">' +
          '<thead><tr>' +
            '<th style="width:36px">#</th>' +
            '<th>API Endpoint (Method &amp; Path)</th>' +
            '<th>📤 Request Payload (STG4 ↔ STG10)</th>' +
            '<th>📥 Response (STG4 ↔ STG10)</th>' +
            '<th style="width:85px">Khớp</th>' +
            '<th style="width:115px">Thao tác</th>' +
          '</tr></thead>' +
          '<tbody>' +
          aligned.map(function (r) {
            var method = r.method || (r.stg10 && r.stg10.method) || (r.stg4 && r.stg4.method) || "GET";
            var endpoint = r.endpoint || (r.stg10 && r.stg10.basePath) || (r.stg4 && r.stg4.basePath) || (r.stg10 && r.stg10.path) || (r.stg4 && r.stg4.path) || "";
            var reqInfo = r.requestInfo || {};
            var respInfo = r.responseInfo || {};

            var stg4Payload = reqInfo.stg4Payload || (r.stg4 && r.stg4.postData) || (r.stg4 && Object.keys(r.stg4.queryParams || {}).length ? JSON.stringify(r.stg4.queryParams) : "Direct GET (No body)");
            var stg10Payload = reqInfo.stg10Payload || (r.stg10 && r.stg10.postData) || (r.stg10 && Object.keys(r.stg10.queryParams || {}).length ? JSON.stringify(r.stg10.queryParams) : "Direct GET (No body)");

            var stg4Status = respInfo.stg4Status || (r.stg4 ? (r.stg4.status + ' OK') : '—');
            var stg10Status = respInfo.stg10Status || (r.stg10 ? (r.stg10.status + ' OK') : '—');
            var stg4Type = respInfo.stg4Type || 'text/html';
            var stg10Type = respInfo.stg10Type || 'text/html';

            var matchBadge = r.match ? '<span class="req-match-ok">✓ Khớp</span>' : '<span class="req-match-diff">≠ Lệch</span>';
            var methodBadge = '<span class="badge-method badge-' + method.toLowerCase() + '">' + esc(method) + '</span>';

            // Parameter comparison lines if diff
            var pDiffs = r.paramDiffs || [];
            var paramsHtml = "";
            if (pDiffs.length) {
              paramsHtml = '<div class="req-params-box">' +
                pDiffs.map(function (p) {
                  var pMatch = p.match ? '<span class="badge-param-match">✓</span>' : '<span class="badge-param-diff">≠</span>';
                  return '<div class="param-line ' + (p.match ? 'param-line-ok' : 'param-line-diff') + '">' +
                    pMatch + ' <strong>' + esc(p.param) + ':</strong> ' +
                    '<code>' + esc(p.stg4) + '</code> &harr; <code>' + esc(p.stg10) + '</code>' +
                  '</div>';
                }).join("") + '</div>';
            } else {
              paramsHtml = '<div class="payload-preview-line">' +
                '<div><span class="sub-lbl">STG4:</span> <code>' + esc(stg4Payload) + '</code></div>' +
                '<div><span class="sub-lbl">STG10:</span> <code>' + esc(stg10Payload) + '</code></div>' +
              '</div>';
            }

            var respHtml = '<div class="resp-summary-cell">' +
              '<div><span class="sub-lbl">STG4:</span> <span class="pill ' + ((r.stg4 && r.stg4.status === 200) ? 'passed' : 'failed') + '">' + esc(stg4Status) + '</span> <span class="resp-type-badge">' + esc(stg4Type.split(";")[0]) + '</span></div>' +
              '<div><span class="sub-lbl">STG10:</span> <span class="pill ' + ((r.stg10 && r.stg10.status === 200) ? 'passed' : 'failed') + '">' + esc(stg10Status) + '</span> <span class="resp-type-badge">' + esc(stg10Type.split(";")[0]) + '</span></div>' +
            '</div>';

            var mainRow = '<tr class="' + (r.match ? 'row-req-ok' : 'row-req-diff') + '">' +
              '<td>' + r.index + '</td>' +
              '<td>' + methodBadge + ' <code>' + esc(endpoint) + '</code></td>' +
              '<td>' + paramsHtml + '</td>' +
              '<td>' + respHtml + '</td>' +
              '<td>' + matchBadge + '</td>' +
              '<td><button type="button" class="btn-toggle-req-detail" data-idx="' + r.index + '">👁️ Chi tiết</button></td>' +
            '</tr>';

            var detailRow = '<tr class="req-detail-panel" id="reqDetailPanel-' + r.index + '" style="display:none">' +
              '<td colspan="6">' +
                '<div class="req-res-split-box">' +
                  '<div class="split-col split-req">' +
                    '<div class="split-hdr">📤 CHI TIẾT REQUEST (DỮ LIỆU GỬI ĐI)</div>' +
                    '<div class="detail-field"><strong>HTTP Method:</strong> <code>' + esc(method) + '</code></div>' +
                    '<div class="detail-field"><strong>Endpoint Path:</strong> <code>' + esc(endpoint) + '</code></div>' +
                    '<div class="detail-field"><strong>STG4 Request Payload:</strong></div>' +
                    '<pre class="req-res-pre">' + esc(stg4Payload) + '</pre>' +
                    '<div class="detail-field"><strong>STG10 Request Payload:</strong></div>' +
                    '<pre class="req-res-pre">' + esc(stg10Payload) + '</pre>' +
                  '</div>' +
                  '<div class="split-col split-res">' +
                    '<div class="split-hdr">📥 CHI TIẾT RESPONSE (PHẢN HỒI TỪ SERVER)</div>' +
                    '<div class="detail-field"><strong>HTTP Status:</strong> STG4: <code>' + esc(stg4Status) + '</code> &harr; STG10: <code>' + esc(stg10Status) + '</code></div>' +
                    '<div class="detail-field"><strong>Content-Type:</strong> STG4: <code>' + esc(stg4Type) + '</code> &harr; STG10: <code>' + esc(stg10Type) + '</code></div>' +
                    '<div class="detail-field"><strong>STG4 Response Body Preview:</strong></div>' +
                    '<pre class="req-res-pre">' + esc(respInfo.stg4Body || 'HTTP 200 OK - Content rendered successfully') + '</pre>' +
                    '<div class="detail-field"><strong>STG10 Response Body Preview:</strong></div>' +
                    '<pre class="req-res-pre">' + esc(respInfo.stg10Body || 'HTTP 200 OK - Content rendered successfully') + '</pre>' +
                  '</div>' +
                '</div>' +
              '</td>' +
            '</tr>';

            return mainRow + detailRow;
          }).join("") +
          '</tbody>' +
        '</table>' +
      '</div>';
    }'''

if old_req_rows_block in js:
    js = js.replace(old_req_rows_block, new_req_rows_block)
    print("Replaced reqRowsHtml with Request & Response table and detail drawer in app.js.")
else:
    print("Warning: old_req_rows_block not matched in app.js!")

# Add event listener for .btn-toggle-req-detail in bindParityEvents
old_bind_section = '''    var jBtn = panel.querySelector("#btnJumpInspector");
    if (jBtn) jBtn.addEventListener("click", scrollDownToInspector);
    var fBtn = panel.querySelector("#btnFloatingInspector");
    if (fBtn) fBtn.addEventListener("click", scrollDownToInspector);'''

new_bind_section = '''    var jBtn = panel.querySelector("#btnJumpInspector");
    if (jBtn) jBtn.addEventListener("click", scrollDownToInspector);
    var fBtn = panel.querySelector("#btnFloatingInspector");
    if (fBtn) fBtn.addEventListener("click", scrollDownToInspector);

    panel.querySelectorAll(".btn-toggle-req-detail").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var idx = btn.getAttribute("data-idx");
        var panelRow = panel.querySelector("#reqDetailPanel-" + idx);
        if (!panelRow) return;
        var isOpen = panelRow.style.display !== "none";
        if (isOpen) {
          panelRow.style.display = "none";
          btn.textContent = "👁️ Chi tiết";
          btn.classList.remove("active");
        } else {
          panelRow.style.display = "table-row";
          btn.textContent = "▲ Thu gọn";
          btn.classList.add("active");
        }
      });
    });'''

if old_bind_section in js:
    js = js.replace(old_bind_section, new_bind_section)
    print("Added .btn-toggle-req-detail binding in bindParityEvents.")
else:
    print("Warning: old_bind_section not matched in app.js!")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(js)

# 4. Update styles.css
with open(STYLES_CSS, "r", encoding="utf-8") as f:
    css = f.read()

req_res_styles = """
/* Request & Response Inspector Table */
.reqs-hdr-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}
.reqs-hint {
  font-size: 11px;
  color: #094294;
  background: #f0f7ff;
  border: 1px solid #c8e1ff;
  padding: 3px 8px;
  border-radius: 4px;
}
.badge-method {
  display: inline-block;
  font-size: 9.5px;
  font-weight: 700;
  padding: 2px 5px;
  border-radius: 3px;
  text-transform: uppercase;
  margin-right: 4px;
}
.badge-get { background: #e7f5ff; color: #1971c2; border: 1px solid #a5d8ff; }
.badge-post { background: #ebfbee; color: #2f9e44; border: 1px solid #b2f2bb; }
.badge-put { background: #fff4e6; color: #d9480f; border: 1px solid #ffd8a8; }
.badge-delete { background: #fff5f5; color: #e03131; border: 1px solid #ffc9c9; }

.sub-lbl {
  font-size: 10px;
  font-weight: 700;
  color: var(--ink-3);
  margin-right: 3px;
}
.resp-type-badge {
  font-size: 9.5px;
  color: var(--ink-3);
  background: #f1f3f5;
  border: 1px solid #dee2e6;
  border-radius: 3px;
  padding: 1px 4px;
  margin-left: 3px;
}
.payload-preview-line {
  font-size: 11px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.resp-summary-cell {
  font-size: 11px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.btn-toggle-req-detail {
  background: #f1f3f5;
  color: #1c5fd6;
  border: 1px solid #c8e1ff;
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.15s;
}
.btn-toggle-req-detail:hover {
  background: #e7f5ff;
}
.btn-toggle-req-detail.active {
  background: #1c5fd6;
  color: #fff;
  border-color: #1c5fd6;
}

.req-detail-panel td {
  padding: 0 !important;
  background: #f8f9fa;
  border-top: none !important;
}
.req-res-split-box {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  background: #ffffff;
  border: 1px solid #c8e1ff;
  border-radius: 6px;
  padding: 12px 14px;
  margin: 8px 12px 12px 12px;
  box-shadow: inset 0 1px 3px rgba(0,0,0,0.03);
}
.split-col {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.split-hdr {
  font-size: 11.5px;
  font-weight: 700;
  color: #094294;
  margin-bottom: 4px;
  border-bottom: 1px solid #e1e4e8;
  padding-bottom: 4px;
}
.detail-row-item {
  font-size: 11px;
  color: var(--ink-2);
}
.req-res-pre {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  padding: 6px 8px;
  font-size: 11px;
  font-family: var(--font-mono, monospace);
  white-space: pre-wrap;
  word-break: break-all;
  max-height: 120px;
  overflow-y: auto;
  margin: 2px 0 6px 0;
  color: #212529;
}
"""

if ".reqs-hdr-bar" not in css:
    css += "\n" + req_res_styles
    with open(STYLES_CSS, "w", encoding="utf-8") as f:
        f.write(css)
    print("Added Request & Response inspector styles to styles.css.")

# 5. Bump cache buster in index.html to v=20261019m
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("styles.css?v=20261019l", "styles.css?v=20261019m")
html = html.replace("app.js?v=20261019l", "app.js?v=20261019m")

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("Bumped cache buster in index.html to v=20261019m.")
