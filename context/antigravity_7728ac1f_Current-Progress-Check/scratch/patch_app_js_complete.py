import os
import re

APP_JS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"

with open(APP_JS, "r", encoding="utf-8") as f:
    code = f.read()

# Helper functions to inject before renderTestDetail
helpers = '''
  function parsePlaywrightAction(title) {
    if (!title) return null;
    var mFill = /Fill\s+"([^"]*)"\s+locator\(([^)]+)\)/i.exec(title);
    if (mFill) return { type: "FILL", value: mFill[1], target: mFill[2].trim(), cls: "pw-action-fill" };
    var mClick = /Click\s+locator\(([^)]+)\)/i.exec(title);
    if (mClick) return { type: "CLICK", value: "Thực hiện Click", target: mClick[1].trim(), cls: "pw-action-click" };
    var mSelect = /SelectOption\s+"([^"]*)"\s+locator\(([^)]+)\)/i.exec(title);
    if (mSelect) return { type: "SELECT", value: mSelect[1], target: mSelect[2].trim(), cls: "pw-action-select" };
    var mGoto = /goto\(([^)]+)\)/i.exec(title);
    if (mGoto) return { type: "GOTO", value: mGoto[1].trim(), target: "Trình duyệt", cls: "pw-action-goto" };
    return { type: "ACTION", value: title, target: "—", cls: "pw-action-other" };
  }

  function playwrightParamsBlock(t) {
    var steps = t.flow || [];
    var parsedActions = [];
    steps.forEach(function (s) {
      var act = parsePlaywrightAction(s.title);
      if (act) {
        act.durationMs = s.durationMs;
        parsedActions.push(act);
      }
    });

    var rowsHtml = "";
    if (parsedActions.length) {
      rowsHtml = '<table class="pw-param-table">' +
        '<thead><tr><th>#</th><th>Thao Tác</th><th>Tham Số / Giá Trị Nhập Vào</th><th>Phần Tử Đích (Selector)</th><th>Thời Gian</th></tr></thead>' +
        '<tbody>' +
        parsedActions.map(function (a, i) {
          var valDisplay = (a.type === "FILL" || a.type === "SELECT" || a.type === "GOTO")
            ? '<span class="pw-val-badge">' + esc(a.value) + '</span>'
            : '<span class="pw-click-text">' + esc(a.value) + '</span>';
          return '<tr>' +
            '<td>' + (i + 1) + '</td>' +
            '<td><span class="pw-action-tag ' + a.cls + '">' + esc(a.type) + '</span></td>' +
            '<td>' + valDisplay + '</td>' +
            '<td><code>' + esc(a.target) + '</code></td>' +
            '<td>' + fmtMs(a.durationMs) + '</td>' +
          '</tr>';
        }).join("") +
        '</tbody>' +
      '</table>';
    } else {
      rowsHtml = '<div class="pw-no-actions">Direct Page Load / GET tĩnh — Không có tham số gõ phím hoặc tương tác form</div>';
    }

    return '<div class="pw-inputs-card">' +
      '<div class="pw-card-hdr">' +
        '<div class="pw-card-title">🎯 Tham Số &amp; Thao Tác Playwright (Playwright Context &amp; Input Parameters)</div>' +
        '<span class="dim-tag">' + esc(dimensionOf(t)) + '</span>' +
      '</div>' +
      '<div class="pw-inputs-grid">' +
        '<div><span class="pw-lbl">Observed Route:</span> <code>' + esc(t.observedRoute || t.route || "—") + '</code></div>' +
        '<div><span class="pw-lbl">Scenario:</span> <strong>' + esc(t.scenario) + '</strong></div>' +
        (t.tc ? '<div><span class="pw-lbl">Mã TC:</span> <code>' + esc(t.tc) + '</code></div>' : '') +
      '</div>' +
      rowsHtml +
    '</div>';
  }

  function findCompareDimTest(t) {
    if (!compareDim || !compareDim.tests) return null;
    var tc = (t.tc || "").trim().toUpperCase();
    var sc = (t.scenario || "").trim().toLowerCase();
    for (var i = 0; i < compareDim.tests.length; i++) {
      var ct = compareDim.tests[i];
      if (tc && ct.tc && ct.tc.trim().toUpperCase() === tc) return ct;
      if (sc && ct.scenario && ct.scenario.trim().toLowerCase() === sc) return ct;
    }
    return null;
  }

  function parityCompareBlock(t) {
    var ct = findCompareDimTest(t);
    if (!ct) return "";

    var selMeta = VERDICT_META[ct.verdict] || VERDICT_META["HOLE"];
    var aligned = ct.alignedReqs || [];
    var reqRowsHtml = "";

    if (aligned.length) {
      reqRowsHtml = '<table class="aligned-reqs-table" style="margin-top:8px">' +
        '<thead><tr><th>#</th><th>STG4 Request (Origin)</th><th>STG10 Request (Target)</th><th>Tham Số So Sánh (Query / Body Params)</th><th>Khớp</th></tr></thead>' +
        '<tbody>' +
        aligned.map(function (r) {
          var stg4Text = r.stg4 ? (r.stg4.method + ' ' + r.stg4.path + ' (' + r.stg4.status + ')') : '—';
          var stg10Text = r.stg10 ? (r.stg10.method + ' ' + r.stg10.path + ' (' + r.stg10.status + ')') : '—';
          var matchBadge = r.match ? '<span class="req-match-ok">✓ Khớp</span>' : '<span class="req-match-diff">≠ Lệch</span>';
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
      '</table>';
    }

    return '<div class="detail-parity-box">' +
      '<div class="detail-parity-hdr">' +
        '<div class="detail-parity-title">' +
          '⚡ Đối Chiếu Parity STG4 ↔ STG10: <span class="drill-v-chip" style="background:' + selMeta.bg + ';color:' + selMeta.color + ';border:1px solid ' + selMeta.border + '">' + esc(selMeta.label) + '</span>' +
        '</div>' +
        '<button type="button" class="btn-jump-parity" data-screen="' + esc(ct.screen) + '" data-dim="' + esc(ct.dimension) + '" data-key="' + esc(ct.key) + '">👉 Mở Trong Ma Trận Parity &rarr;</button>' +
      '</div>' +
      '<div class="detail-parity-grid">' +
        '<div class="detail-parity-col parity-col-stg4">' +
          '<div class="parity-col-hdr">STG4 (Origin NET4)</div>' +
          '<div>Trạng thái: <span class="pill ' + esc(ct.stg4.status) + '">' + esc(ct.stg4.status) + '</span> (' + fmtMs(ct.stg4.durationMs) + ')</div>' +
          '<div>Số request: ' + ct.stg4.reqCount + '</div>' +
          (ct.stg4.error ? '<pre class="side-err">' + esc(ct.stg4.error) + '</pre>' : '') +
        '</div>' +
        '<div class="detail-parity-col parity-col-stg10">' +
          '<div class="parity-col-hdr">STG10 (Target NET10)</div>' +
          '<div>Trạng thái: <span class="pill ' + esc(ct.stg10.status) + '">' + esc(ct.stg10.status) + '</span> (' + fmtMs(ct.stg10.durationMs) + ')</div>' +
          '<div>Số request: ' + ct.stg10.reqCount + '</div>' +
          (ct.stg10.error ? '<pre class="side-err">' + esc(ct.stg10.error) + '</pre>' : '') +
        '</div>' +
      '</div>' +
      reqRowsHtml +
    '</div>';
  }
'''

# Check if helper already in code
if "function parsePlaywrightAction" not in code:
    target_pos = code.find("/* ---------- cột 3: detail 1 test case đang chọn ---------- */")
    if target_pos >= 0:
        code = code[:target_pos] + helpers + "\n  " + code[target_pos:]
        print("Injected helper functions before renderTestDetail.")
    else:
        print("ERROR: could not find target position for helpers.")

# Inject blocks into renderTestDetail
old_detail_render = '''    if (t.error) {
      html += isSkipped(t)
        ? '<div class="note"><strong>Lý do skip:</strong> ' + esc(truncateError(t.error)) + "</div>"
        : '<div class="err"><strong>Lỗi:</strong> ' + esc(truncateError(t.error)) + "</div>";
    }
    html += flowBlock(t);'''

new_detail_render = '''    if (t.error) {
      html += isSkipped(t)
        ? '<div class="note"><strong>Lý do skip:</strong> ' + esc(truncateError(t.error)) + "</div>"
        : '<div class="err"><strong>Lỗi:</strong> ' + esc(truncateError(t.error)) + "</div>";
    }
    html += playwrightParamsBlock(t);
    html += parityCompareBlock(t);
    html += flowBlock(t);'''

if old_detail_render in code:
    code = code.replace(old_detail_render, new_detail_render)
    print("Injected playwrightParamsBlock & parityCompareBlock into renderTestDetail.")
else:
    print("Warning: old_detail_render snippet not found or already replaced.")

# Add event listener for .btn-jump-parity in renderTestDetail
old_btn_binding = '''    els.detail.querySelectorAll(".btn-jump-fix").forEach(function (btn) {
      btn.addEventListener("click", function () {
        jumpToFix(btn.getAttribute("data-fix"));
      });
    });'''

new_btn_binding = '''    els.detail.querySelectorAll(".btn-jump-fix").forEach(function (btn) {
      btn.addEventListener("click", function () {
        jumpToFix(btn.getAttribute("data-fix"));
      });
    });
    els.detail.querySelectorAll(".btn-jump-parity").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var sc = btn.getAttribute("data-screen");
        var dm = btn.getAttribute("data-dim");
        var key = btn.getAttribute("data-key");
        switchTab("parity");
        parityState.selectedScreen = sc;
        parityState.selectedDim = dm;
        parityState.selectedTestKey = key;
        renderParityTab(payloadById(state.pid));
        var dd = document.getElementById("parityDrillDown");
        if (dd) dd.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });'''

if old_btn_binding in code:
    code = code.replace(old_btn_binding, new_btn_binding)
    print("Bound .btn-jump-parity event listeners.")

# Enhance renderParityTab default selection and quick nav
old_parity_open = '''    if (!compareDim || !compareDim.matrix) {
      panel.innerHTML = '<section class="parity-tab"><h2 class="dim-section-title">So Sánh Parity (STG4 ↔ STG10)</h2><p class="ov-line">Chưa nạp được dữ liệu ma trận so sánh. Vui lòng chạy <code>python 03_qa/scripts/compare-dim.py</code>.</p></section>';
      return;
    }'''

new_parity_open = '''    if (!compareDim || !compareDim.matrix) {
      panel.innerHTML = '<section class="parity-tab"><h2 class="dim-section-title">So Sánh Parity (STG4 ↔ STG10)</h2><p class="ov-line">Chưa nạp được dữ liệu ma trận so sánh. Vui lòng chạy <code>python 03_qa/scripts/compare-dim.py</code>.</p></section>';
      return;
    }
    if (!parityState.selectedScreen && compareDim.matrix.length) {
      parityState.selectedScreen = compareDim.matrix[0].screen;
    }'''

if old_parity_open in code:
    code = code.replace(old_parity_open, new_parity_open)
    print("Enhanced renderParityTab with default screen selection.")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully updated app.js!")
