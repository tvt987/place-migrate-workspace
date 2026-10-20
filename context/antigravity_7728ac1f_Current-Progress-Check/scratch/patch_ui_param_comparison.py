import os
import re

APP_JS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"
STYLES_CSS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\styles.css"

# 1. Update app.js
with open(APP_JS, "r", encoding="utf-8") as f:
    js = f.read()

# Replace the Aligned request table section in app.js
old_req_block = '''    // Aligned request table
    var reqRowsHtml = "";
    var aligned = selectedTest.alignedReqs || [];
    if (aligned.length) {
      reqRowsHtml = '<div class="aligned-reqs-section">' +
        '<h4 class="reqs-title">So Sánh Chuỗi Network Requests (' + aligned.length + ')</h4>' +
        '<table class="aligned-reqs-table">' +
          '<thead><tr><th>#</th><th>STG4 Request (Origin)</th><th>STG10 Request (Target)</th><th>Khớp</th></tr></thead>' +
          '<tbody>' +
          aligned.map(function (r) {
            var stg4Text = r.stg4 ? (r.stg4.method + ' ' + r.stg4.path + ' (' + r.stg4.status + ')') : '—';
            var stg10Text = r.stg10 ? (r.stg10.method + ' ' + r.stg10.path + ' (' + r.stg10.status + ')') : '—';
            var matchBadge = r.match ? '<span class="req-match-ok">✓ Khớp</span>' : '<span class="req-match-diff">≠ Lệch</span>';
            return '<tr class="' + (r.match ? 'row-req-ok' : 'row-req-diff') + '">' +
              '<td>' + r.index + '</td>' +
              '<td><code>' + esc(stg4Text) + '</code></td>' +
              '<td><code>' + esc(stg10Text) + '</code></td>' +
              '<td>' + matchBadge + '</td>' +
            '</tr>';
          }).join("") +
          '</tbody>' +
        '</table>' +
      '</div>';
    }'''

new_req_block = '''    // Playwright Execution Context & Input Parameters Box
    var pwActions = selectedTest.playwrightInputs || [];
    var pwActionsHtml = "";
    if (pwActions.length) {
      pwActionsHtml = '<ul class="pw-actions-list">' +
        pwActions.map(function (act) {
          var title = (typeof act === "string") ? act : (act.title || "");
          return '<li><span class="pw-action-badge">Playwright Action</span> <code>' + esc(title) + '</code></li>';
        }).join("") + '</ul>';
    } else {
      pwActionsHtml = '<div class="pw-no-actions">Không có hành động gõ phím/click tương tác form trong flow (Direct Page Load / Read-only)</div>';
    }

    var pwContextHtml = '<div class="drill-pw-inputs-box">' +
      '<div class="pw-box-title">🎯 Tham Số & Đầu Vào Playwright (Playwright Context & Input Parameters)</div>' +
      '<div class="pw-inputs-grid">' +
        '<div><span class="pw-lbl">Observed Route:</span> <code>' + esc(selectedTest.observedRoute || "—") + '</code></div>' +
        '<div><span class="pw-lbl">Dimension:</span> <span class="dim-tag">' + esc(selectedTest.dimension || "FLOW") + '</span></div>' +
        '<div><span class="pw-lbl">Scenario:</span> <strong>' + esc(selectedTest.scenario) + '</strong></div>' +
        (selectedTest.tc ? '<div><span class="pw-lbl">Mã TC:</span> <code>' + esc(selectedTest.tc) + '</code></div>' : '') +
      '</div>' +
      '<div class="pw-actions-wrap">' +
        '<div class="pw-actions-title">Các bước tương tác Playwright đã ghi nhận (' + pwActions.length + '):</div>' +
        pwActionsHtml +
      '</div>' +
    '</div>';

    // Aligned request table with Parameter Comparison
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

js = js.replace(old_req_block, new_req_block)

# Update return layout to include pwContextHtml
old_layout = '''        diffAlertHtml +
        caseMismatchHtml +
        statusComparisonHtml +
        reqRowsHtml +'''

new_layout = '''        pwContextHtml +
        diffAlertHtml +
        caseMismatchHtml +
        statusComparisonHtml +
        reqRowsHtml +'''

js = js.replace(old_layout, new_layout)

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(js)

print("Updated app.js with Playwright inputs and param diff table.")

# 2. Update styles.css
with open(STYLES_CSS, "r", encoding="utf-8") as f:
    css = f.read()

param_styles = '''
/* Playwright Inputs Box */
.drill-pw-inputs-box {
  background: #f0f7ff;
  border: 1px solid #c8e1ff;
  border-radius: 6px;
  padding: 12px 14px;
  margin-bottom: 12px;
}
.pw-box-title {
  font-size: 13px;
  font-weight: 700;
  color: #094294;
  margin-bottom: 8px;
}
.pw-inputs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 8px;
  font-size: 12px;
  margin-bottom: 8px;
}
.pw-lbl {
  color: var(--ink-3);
  font-weight: 600;
  margin-right: 4px;
}
.pw-actions-wrap {
  border-top: 1px dashed #c8e1ff;
  padding-top: 8px;
  margin-top: 6px;
}
.pw-actions-title {
  font-size: 11.5px;
  font-weight: 600;
  color: #094294;
  margin-bottom: 4px;
}
.pw-actions-list {
  margin: 0;
  padding-left: 18px;
  font-size: 11.5px;
  color: var(--ink-2);
}
.pw-actions-list li {
  margin-bottom: 3px;
}
.pw-action-badge {
  background: #094294;
  color: #fff;
  font-size: 9.5px;
  font-weight: 700;
  padding: 1px 5px;
  border-radius: 3px;
  margin-right: 4px;
}
.pw-no-actions {
  font-size: 11.5px;
  color: var(--ink-3);
  font-style: italic;
}

/* Parameters Comparison Styling */
.req-params-box {
  font-size: 11px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.param-line {
  padding: 2px 4px;
  border-radius: 3px;
}
.param-line-ok {
  background: rgba(43, 138, 62, 0.08);
}
.param-line-diff {
  background: rgba(201, 42, 42, 0.1);
  border: 1px solid #ffa8a8;
}
.badge-param-match {
  color: #2b8a3e;
  font-weight: 700;
  margin-right: 2px;
}
.badge-param-diff {
  color: #c92a2a;
  font-weight: 700;
  margin-right: 2px;
}
.no-params-text {
  color: var(--ink-3);
  font-size: 10.5px;
  font-style: italic;
}
'''

if ".drill-pw-inputs-box" not in css:
    css += "\n" + param_styles
    with open(STYLES_CSS, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated styles.css with param styles.")
else:
    print("styles.css already has param styles.")
