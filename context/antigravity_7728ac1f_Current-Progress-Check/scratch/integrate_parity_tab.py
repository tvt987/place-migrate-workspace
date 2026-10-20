import os

APP_JS = r"e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"
STYLES_CSS = r"e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\styles.css"

with open(APP_JS, "r", encoding="utf-8") as f:
    js = f.read()

# 1. Update TAB_PANELS
js = js.replace(
    'var TAB_PANELS = ["detail", "defect", "blocked", "registry"];',
    'var TAB_PANELS = ["detail", "defect", "blocked", "registry", "parity"];'
)

# 2. Add compareDim state
old_store = 'var defectRegistry = (window.__REPORT_DATA__ && window.__REPORT_DATA__.defectRegistry) ? window.__REPORT_DATA__.defectRegistry : { defects: [] };'
new_store = '''var defectRegistry = (window.__REPORT_DATA__ && window.__REPORT_DATA__.defectRegistry) ? window.__REPORT_DATA__.defectRegistry : { defects: [] };
  var compareDim = (window.__REPORT_DATA__ && window.__REPORT_DATA__.compareDim) ? window.__REPORT_DATA__.compareDim : null;'''

if old_store in js and 'var compareDim' not in js:
    js = js.replace(old_store, new_store)

# 3. Add parity fetch in refreshFromServer
target_hook = 'renderRegistryTab(payloadById(state.pid));'
fetch_compare_hook = '''renderRegistryTab(payloadById(state.pid));
      }
    }).catch(function () {});

    fetch("api/compare-dim", { cache: "no-store" }).then(function (r) {
      return r.ok ? r.json() : null;
    }).then(function (data) {
      if (data && data.matrix) {
        compareDim = data;
        renderParityTab(payloadById(state.pid));
      }
    }).catch(function () {});'''

if target_hook in js and 'api/compare-dim' not in js:
    # replace first occurrence after defectRegistry
    idx = js.find('fetch("api/defect-registry"')
    if idx != -1:
        reg_sub = js[idx:]
        reg_sub_replaced = reg_sub.replace(
            '''renderRegistryTab(payloadById(state.pid));
      }
    }).catch(function () {});''',
            fetch_compare_hook,
            1
        )
        js = js[:idx] + reg_sub_replaced

# 4. Parity tab implementation code
parity_impl = '''
  var VERDICT_META = {
    "PARITY_OK": { label: "PARITY OK", desc: "Cả 2 pass, request khớp", color: "#2b8a3e", bg: "#e9f5ec", border: "#bfe0c7" },
    "CONTENT_DIFF": { label: "CONTENT DIFF", desc: "Cả 2 pass nhưng request/nội dung lệch", color: "#6741d9", bg: "#f3f0ff", border: "#d0bfff" },
    "MIGRATE_BUG": { label: "MIGRATE BUG", desc: "STG4 pass, STG10 fail", color: "#c92a2a", bg: "#fdecec", border: "#f1b6b6" },
    "IMPROVED": { label: "IMPROVED", desc: "STG4 fail/skip, STG10 pass", color: "#0c8599", bg: "#e3fafc", border: "#99e9f2" },
    "ORIGIN_SAME": { label: "ORIGIN SAME", desc: "Cả 2 cùng fail (lỗi gốc NET4)", color: "#495057", bg: "#f1f3f5", border: "#ced4da" },
    "BOTH_SKIP": { label: "BOTH SKIP", desc: "Cả 2 cùng skip (lỗ hổng)", color: "#b15c00", bg: "#fff3e2", border: "#ffe0b2" },
    "HOLE": { label: "HOLE", desc: "0 test case", color: "#868e96", bg: "#fafafa", border: "#dee2e6" }
  };

  var parityState = {
    filterMode: "ALL", // ALL | DIFF_ONLY | FAIL_ONLY
    search: "",
    selectedScreen: null,
    selectedDim: null,
    selectedTestKey: null
  };

  function renderParityTab(p) {
    var panel = document.getElementById("panel-parity");
    if (!panel) return;

    if (!compareDim || !compareDim.matrix) {
      panel.innerHTML = '<section class="parity-tab"><h2 class="dim-section-title">So Sánh Parity (STG4 vs STG10)</h2>' +
        '<p class="ov-line">Chưa có dữ liệu so sánh parity theo dimension. Chạy <code>python 03_qa/scripts/compare-dim.py</code> để sinh dữ liệu.</p></section>';
      return;
    }

    var summary = compareDim.summary || {};
    var verdicts = summary.verdicts || {};
    var matrix = compareDim.matrix || [];
    var dims = compareDim.dimensionOrder || ["LOAD", "FLOW", "VALIDATION", "AUTH", "PERM", "STATE", "EDGE"];

    // KPIs Header
    var kpisHtml = '<div class="parity-kpis-bar">' +
      '<div class="pkpi pkpi-total"><span class="pkpi-num">' + (summary.totalTests || 0) + '</span><span class="pkpi-lbl">Tổng Test Cases</span></div>' +
      '<div class="pkpi pkpi-ok"><span class="pkpi-num" style="color:#2b8a3e">' + (verdicts.PARITY_OK || 0) + '</span><span class="pkpi-lbl">PARITY OK</span></div>' +
      '<div class="pkpi pkpi-diff"><span class="pkpi-num" style="color:#6741d9">' + (verdicts.CONTENT_DIFF || 0) + '</span><span class="pkpi-lbl">CONTENT DIFF</span></div>' +
      '<div class="pkpi pkpi-improved"><span class="pkpi-num" style="color:#0c8599">' + (verdicts.IMPROVED || 0) + '</span><span class="pkpi-lbl">IMPROVED</span></div>' +
      '<div class="pkpi pkpi-bug"><span class="pkpi-num" style="color:#c92a2a">' + (verdicts.MIGRATE_BUG || 0) + '</span><span class="pkpi-lbl">MIGRATE BUG</span></div>' +
      '<div class="pkpi pkpi-origin"><span class="pkpi-num" style="color:#495057">' + (verdicts.ORIGIN_SAME || 0) + '</span><span class="pkpi-lbl">ORIGIN SAME</span></div>' +
      '<div class="pkpi pkpi-skip"><span class="pkpi-num" style="color:#b15c00">' + (verdicts.BOTH_SKIP || 0) + '</span><span class="pkpi-lbl">BOTH SKIP</span></div>' +
      '<div class="pkpi pkpi-case"><span class="pkpi-num" style="color:#e03131">' + (summary.caseMismatches || 0) + '</span><span class="pkpi-lbl">Linux Case Mismatch</span></div>' +
    '</div>';

    // Filter toolbar
    var toolbarHtml = '<div class="parity-toolbar">' +
      '<div class="parity-search-box">' +
        '<input type="search" id="paritySearchInput" placeholder="Tìm kiếm màn hình (route)..." value="' + esc(parityState.search) + '">' +
      '</div>' +
      '<div class="parity-filter-buttons">' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "ALL" ? " active" : "") + '" data-mode="ALL">Tất cả màn hình (' + matrix.length + ')</button>' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "DIFF_ONLY" ? " active" : "") + '" data-mode="DIFF_ONLY">Chỉ ô lệch (CONTENT_DIFF + BUG)</button>' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "FAIL_ONLY" ? " active" : "") + '" data-mode="FAIL_ONLY">Chỉ màn có lỗi</button>' +
      '</div>' +
      '<div class="parity-legend">' +
        Object.keys(VERDICT_META).map(function (v) {
          var m = VERDICT_META[v];
          return '<span class="legend-badge" style="background:' + m.bg + ';color:' + m.color + ';border:1px solid ' + m.border + '" title="' + esc(m.desc) + '">' + esc(m.label) + '</span>';
        }).join(" ") +
      '</div>' +
    '</div>';

    // Filter matrix rows
    var filteredRows = matrix.filter(function (row) {
      if (parityState.search && row.screen.toLowerCase().indexOf(parityState.search.toLowerCase()) < 0) return false;
      if (parityState.filterMode === "DIFF_ONLY") {
        var hasDiff = dims.some(function (d) {
          var v = (row.dimensions[d] && row.dimensions[d].verdict) || "HOLE";
          return v === "MIGRATE_BUG" || v === "CONTENT_DIFF";
        });
        if (!hasDiff) return false;
      }
      if (parityState.filterMode === "FAIL_ONLY") {
        var hasFail = dims.some(function (d) {
          var counts = (row.dimensions[d] && row.dimensions[d].counts) || {};
          return counts.MIGRATE_BUG > 0 || counts.ORIGIN_SAME > 0;
        });
        if (!hasFail) return false;
      }
      return true;
    });

    // Build 3D Matrix Table
    var tableHeader = '<thead><tr><th class="col-screen">Màn hình (Route)</th>' +
      dims.map(function (d) { return '<th class="col-dim">' + esc(d) + '</th>'; }).join("") +
      '</tr></thead>';

    var tableBody = '<tbody>' + filteredRows.map(function (row) {
      var isScSelected = parityState.selectedScreen === row.screen;
      var cellsHtml = dims.map(function (d) {
        var c = row.dimensions[d] || { verdict: "HOLE", total: 0 };
        var v = c.verdict;
        var meta = VERDICT_META[v] || VERDICT_META["HOLE"];
        var isSelected = isScSelected && parityState.selectedDim === d;

        var content = "—";
        if (c.total > 0) {
          content = '<span class="v-label">' + esc(meta.label) + '</span> <span class="v-count">(' + c.total + ')</span>';
        }

        return '<td class="parity-cell cell-' + esc(v.toLowerCase()) + (isSelected ? ' selected-cell' : '') + '" ' +
          'data-screen="' + esc(row.screen) + '" data-dim="' + esc(d) + '" ' +
          'style="background:' + meta.bg + ';color:' + meta.color + ';border-color:' + meta.border + '" ' +
          'title="Màn: ' + esc(row.screen) + ' | Dim: ' + esc(d) + ' | ' + esc(meta.desc) + '">' +
          content + '</td>';
      }).join("");

      return '<tr class="parity-row' + (isScSelected ? ' selected-row' : '') + '" data-screen="' + esc(row.screen) + '">' +
        '<td class="screen-label" data-screen="' + esc(row.screen) + '"><strong>' + esc(row.screen) + '</strong></td>' +
        cellsHtml +
      '</tr>';
    }).join("") + '</tbody>';

    var matrixTableHtml = '<div class="parity-table-container">' +
      '<table class="parity-table">' + tableHeader + tableBody + '</table>' +
    '</div>';

    // Drill-Down Drawer / Inspector
    var drillDownHtml = '<div class="parity-drilldown" id="parityDrillDown">' +
      renderDrillDownContent(compareDim) +
    '</div>';

    panel.innerHTML = '<section class="parity-tab">' +
      '<div class="parity-tab-hdr">' +
        '<div>' +
          '<h2 class="dim-section-title">Ma Trận So Sánh Parity 3 Chiều (STG4 vs STG10)</h2>' +
          '<p class="parity-sub">Đối chiếu 559 test cases trên 45 màn hình theo 5 Dimension cốt lõi: LOAD · FLOW · VALIDATION · AUTH · PERM · STATE · EDGE</p>' +
        '</div>' +
        '<div class="parity-sources">' +
          '<span class="source-tag">STG4 (Origin NET4): ' + esc(compareDim.sourceNet4 || "test-net4-report-latest.json") + '</span>' +
          '<span class="source-tag">STG10 (Target NET10): ' + esc(compareDim.sourceMssql || "test-mssql-report-latest.json") + '</span>' +
        '</div>' +
      '</div>' +
      kpisHtml +
      toolbarHtml +
      matrixTableHtml +
      drillDownHtml +
    '</section>';

    bindParityEvents(panel, compareDim);
  }

  function renderDrillDownContent(comp) {
    if (!parityState.selectedScreen) {
      return '<div class="empty-drilldown">👉 Bấm vào bất kỳ ô nào trên bảng ma trận để kiểm tra chi tiết các Test Cases và so sánh Network Requests STG4 vs STG10.</div>';
    }

    var screen = parityState.selectedScreen;
    var dim = parityState.selectedDim;
    var allTests = comp.tests || [];

    var tests = allTests.filter(function (t) {
      if (t.screen !== screen) return false;
      if (dim && t.dimension !== dim) return false;
      return true;
    });

    if (!tests.length) {
      return '<div class="empty-drilldown">Không có test case nào cho màn <strong>' + esc(screen) + '</strong> (' + esc(dim || "Tất cả dimension") + ').</div>';
    }

    if (!parityState.selectedTestKey || !tests.some(function (t) { return t.key === parityState.selectedTestKey; })) {
      parityState.selectedTestKey = tests[0].key;
    }

    var selectedTest = tests.find(function (t) { return t.key === parityState.selectedTestKey; }) || tests[0];

    // Build tests list on left side of drilldown
    var testListHtml = tests.map(function (t) {
      var isSel = t.key === selectedTest.key;
      var meta = VERDICT_META[t.verdict] || VERDICT_META["HOLE"];
      return '<button type="button" class="drill-test-item' + (isSel ? ' active' : '') + '" data-key="' + esc(t.key) + '">' +
        '<span class="drill-v-chip" style="background:' + meta.bg + ';color:' + meta.color + ';border:1px solid ' + meta.border + '">' + esc(meta.label) + '</span>' +
        '<span class="drill-tc-title">' + esc(t.scenario || t.tc) + '</span>' +
        (t.tc ? '<span class="drill-tc-code">' + esc(t.tc) + '</span>' : '') +
      '</button>';
    }).join("");

    // Build right side deep comparison for selectedTest
    var selMeta = VERDICT_META[selectedTest.verdict] || VERDICT_META["HOLE"];
    var diffAlertHtml = "";
    if (selectedTest.diffReason) {
      diffAlertHtml = '<div class="drill-diff-alert" style="border-left:4px solid ' + selMeta.color + '">' +
        '<strong>' + esc(selMeta.label) + ':</strong> ' + esc(selectedTest.diffReason) +
      '</div>';
    }

    var caseMismatchHtml = "";
    if (selectedTest.caseMismatches && selectedTest.caseMismatches.length) {
      caseMismatchHtml = '<div class="case-mismatch-box">' +
        '<strong>⚠️ Phát hiện sai lệch hoa-thường Linux (Case-Sensitivity Mismatch):</strong>' +
        '<ul>' + selectedTest.caseMismatches.map(function (m) {
          return '<li>STG4: <code>' + esc(m.stg4) + '</code> &harr; STG10: <code>' + esc(m.stg10) + '</code></li>';
        }).join("") + '</ul></div>';
    }

    // Side-by-side status card
    var statusComparisonHtml = '<div class="drill-side-comparison">' +
      '<div class="side-col side-stg4">' +
        '<div class="side-hdr">STG4 (NET4 Origin)</div>' +
        '<div class="side-status"><span class="pill ' + esc(selectedTest.stg4.status) + '">' + esc(selectedTest.stg4.status) + '</span> (' + fmtMs(selectedTest.stg4.durationMs) + ')</div>' +
        '<div class="side-reqs">Số request: ' + selectedTest.stg4.reqCount + '</div>' +
        (selectedTest.stg4.error ? '<pre class="side-err">' + esc(selectedTest.stg4.error) + '</pre>' : '') +
      '</div>' +
      '<div class="side-col side-stg10">' +
        '<div class="side-hdr">STG10 (NET10 Target)</div>' +
        '<div class="side-status"><span class="pill ' + esc(selectedTest.stg10.status) + '">' + esc(selectedTest.stg10.status) + '</span> (' + fmtMs(selectedTest.stg10.durationMs) + ')</div>' +
        '<div class="side-reqs">Số request: ' + selectedTest.stg10.reqCount + '</div>' +
        (selectedTest.stg10.error ? '<pre class="side-err">' + esc(selectedTest.stg10.error) + '</pre>' : '') +
      '</div>' +
    '</div>';

    // Aligned request table
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
    }

    return '<div class="drill-hdr-bar">' +
      '<div>' +
        '<h3 class="drill-title">Kiểm tra chi tiết: <strong>' + esc(screen) + '</strong> (' + esc(dim || "Tất cả") + ') — ' + tests.length + ' test cases</h3>' +
        '<p class="drill-sub">Bấm chọn từng test case để so sánh chi tiết giữa STG4 và STG10</p>' +
      '</div>' +
      '<button type="button" class="btn-close-drill" id="btnCloseDrill">&times; Đóng</button>' +
    '</div>' +
    '<div class="drill-body-layout">' +
      '<div class="drill-test-sidebar">' + testListHtml + '</div>' +
      '<div class="drill-test-inspector">' +
        '<div class="inspector-hdr">' +
          '<span class="drill-v-chip-lg" style="background:' + selMeta.bg + ';color:' + selMeta.color + ';border:1px solid ' + selMeta.border + '">' + esc(selMeta.label) + '</span>' +
          '<h4 class="inspector-title">' + esc(selectedTest.scenario) + '</h4>' +
          (selectedTest.tc ? '<span class="inspector-tc">Mã TC: ' + esc(selectedTest.tc) + '</span>' : '') +
          '<span class="inspector-file">' + esc(selectedTest.file) + '</span>' +
        '</div>' +
        diffAlertHtml +
        caseMismatchHtml +
        statusComparisonHtml +
        reqRowsHtml +
      '</div>' +
    '</div>';
  }

  function bindParityEvents(panel, comp) {
    var searchInput = panel.querySelector("#paritySearchInput");
    if (searchInput) {
      searchInput.addEventListener("input", function () {
        parityState.search = searchInput.value;
        renderParityTab(payloadById(state.pid));
      });
    }

    panel.querySelectorAll(".btn-parity-filter").forEach(function (btn) {
      btn.addEventListener("click", function () {
        parityState.filterMode = btn.getAttribute("data-mode");
        renderParityTab(payloadById(state.pid));
      });
    });

    panel.querySelectorAll(".parity-cell").forEach(function (cell) {
      cell.addEventListener("click", function () {
        var sc = cell.getAttribute("data-screen");
        var dm = cell.getAttribute("data-dim");
        parityState.selectedScreen = sc;
        parityState.selectedDim = dm;
        parityState.selectedTestKey = null;
        renderParityTab(payloadById(state.pid));
        var dd = document.getElementById("parityDrillDown");
        if (dd) dd.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });

    panel.querySelectorAll(".screen-label").forEach(function (lbl) {
      lbl.addEventListener("click", function () {
        var sc = lbl.getAttribute("data-screen");
        parityState.selectedScreen = sc;
        parityState.selectedDim = null;
        parityState.selectedTestKey = null;
        renderParityTab(payloadById(state.pid));
        var dd = document.getElementById("parityDrillDown");
        if (dd) dd.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });

    panel.querySelectorAll(".drill-test-item").forEach(function (btn) {
      btn.addEventListener("click", function () {
        parityState.selectedTestKey = btn.getAttribute("data-key");
        var dd = document.getElementById("parityDrillDown");
        if (dd) dd.innerHTML = renderDrillDownContent(comp);
        bindParityEvents(panel, comp);
      });
    });

    var closeBtn = panel.querySelector("#btnCloseDrill");
    if (closeBtn) {
      closeBtn.addEventListener("click", function () {
        parityState.selectedScreen = null;
        parityState.selectedDim = null;
        parityState.selectedTestKey = null;
        renderParityTab(payloadById(state.pid));
      });
    }
  }
'''

if 'renderParityTab' not in js:
    js = js.replace('  function renderAll() {', parity_impl + '\n  function renderAll() {')

# Add renderParityTab(p) call inside renderAll
if 'renderParityTab(p);' not in js:
    js = js.replace('renderRegistryTab(p);', 'renderRegistryTab(p);\n    renderParityTab(p);')

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(js)
print("Updated app.js successfully.")

# 5. Append CSS styles for Parity Tab to styles.css
with open(STYLES_CSS, "r", encoding="utf-8") as f:
    css = f.read()

parity_styles = '''
/* ---------- 3D Parity Matrix & Drilldown Styles ---------- */
.parity-tab {
  padding: 16px 20px 60px;
  max-width: 1500px;
  margin: 0 auto;
}

.parity-tab-hdr {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 16px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--line);
}

.parity-sub {
  margin: 4px 0 0;
  color: var(--ink-3);
  font-size: 13px;
}

.parity-sources {
  display: flex;
  flex-direction: column;
  gap: 4px;
  align-items: flex-end;
}

.source-tag {
  background: var(--surface-2);
  border: 1px solid var(--line);
  font-family: var(--mono);
  font-size: 11px;
  color: var(--ink-2);
  padding: 2px 8px;
  border-radius: 4px;
}

.parity-kpis-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 18px;
}

.pkpi {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 8px 14px;
  min-width: 100px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}

.pkpi-num {
  font-size: 18px;
  font-weight: 700;
  display: block;
  line-height: 1.2;
}

.pkpi-lbl {
  font-size: 10.5px;
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.parity-toolbar {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 12px 16px;
  margin-bottom: 18px;
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
  justify-content: space-between;
}

.parity-search-box input {
  padding: 6px 12px;
  border: 1px solid var(--line);
  border-radius: 6px;
  font-size: 13px;
  width: 250px;
}

.parity-filter-buttons {
  display: flex;
  gap: 8px;
}

.btn-parity-filter {
  background: var(--surface-2);
  border: 1px solid var(--line);
  color: var(--ink-2);
  border-radius: 6px;
  padding: 5px 12px;
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-parity-filter:hover {
  background: var(--hover-bg);
}

.btn-parity-filter.active {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}

.parity-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.legend-badge {
  font-size: 10.5px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 4px;
  letter-spacing: 0.03em;
}

/* Parity Table */
.parity-table-container {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  overflow-x: auto;
  box-shadow: 0 1px 4px rgba(0,0,0,0.03);
  margin-bottom: 24px;
}

.parity-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12.5px;
}

.parity-table th {
  background: var(--surface-2);
  color: var(--ink-2);
  padding: 10px 12px;
  font-weight: 650;
  text-align: center;
  border-bottom: 1px solid var(--line);
  border-right: 1px solid var(--line);
}

.parity-table th.col-screen {
  text-align: left;
  min-width: 180px;
}

.parity-table td {
  padding: 8px 10px;
  border-bottom: 1px solid var(--line);
  border-right: 1px solid var(--line);
  text-align: center;
  transition: all 0.15s;
}

.screen-label {
  text-align: left !important;
  color: var(--ink);
  cursor: pointer;
}

.screen-label:hover {
  color: var(--accent);
  background: var(--hover-bg);
}

.parity-cell {
  cursor: pointer;
  font-weight: 600;
  font-size: 11px;
}

.parity-cell:hover {
  filter: brightness(0.95);
  box-shadow: inset 0 0 0 2px rgba(0,0,0,0.2);
}

.parity-cell.selected-cell {
  box-shadow: inset 0 0 0 2px var(--ink) !important;
  font-weight: 700;
}

.parity-row.selected-row {
  background: rgba(28, 95, 214, 0.05);
}

.v-label {
  font-weight: 700;
}

.v-count {
  font-size: 10px;
  opacity: 0.85;
}

/* Drill Down Drawer */
.parity-drilldown {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.empty-drilldown {
  padding: 30px 20px;
  text-align: center;
  color: var(--ink-3);
  font-size: 14px;
}

.drill-hdr-bar {
  background: var(--surface-2);
  padding: 12px 18px;
  border-bottom: 1px solid var(--line);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.drill-title {
  margin: 0;
  font-size: 14.5px;
  color: var(--ink);
}

.drill-sub {
  margin: 2px 0 0;
  font-size: 12px;
  color: var(--ink-3);
}

.btn-close-drill {
  background: none;
  border: 1px solid var(--line);
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 12px;
  color: var(--ink-2);
  cursor: pointer;
}

.btn-close-drill:hover {
  background: var(--hover-bg);
}

.drill-body-layout {
  display: grid;
  grid-template-columns: 320px 1fr;
  min-height: 400px;
}

@media (max-width: 900px) {
  .drill-body-layout {
    grid-template-columns: 1fr;
  }
}

.drill-test-sidebar {
  border-right: 1px solid var(--line);
  overflow-y: auto;
  max-height: 600px;
  background: #fbfcfd;
}

.drill-test-item {
  width: 100%;
  padding: 10px 12px;
  text-align: left;
  border: none;
  border-bottom: 1px solid var(--line);
  background: transparent;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: background 0.15s;
}

.drill-test-item:hover {
  background: var(--hover-bg);
}

.drill-test-item.active {
  background: #eef4ff;
  border-left: 3px solid var(--accent);
}

.drill-v-chip {
  font-size: 10px;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 3px;
  align-self: flex-start;
}

.drill-v-chip-lg {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
}

.drill-tc-title {
  font-size: 12.5px;
  color: var(--ink);
  font-weight: 500;
  line-height: 1.35;
}

.drill-tc-code {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--ink-3);
}

.drill-test-inspector {
  padding: 16px 20px;
  overflow-y: auto;
  max-height: 600px;
}

.inspector-hdr {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.inspector-title {
  margin: 0;
  font-size: 15px;
  font-weight: 650;
  color: var(--ink);
  flex: 1;
}

.inspector-tc {
  font-family: var(--mono);
  font-size: 12px;
  background: var(--surface-2);
  padding: 2px 8px;
  border-radius: 4px;
}

.inspector-file {
  font-size: 11.5px;
  color: var(--ink-3);
  font-family: var(--mono);
}

.drill-diff-alert {
  background: #f8f9fa;
  padding: 8px 12px;
  border-radius: 4px;
  font-size: 12.5px;
  margin-bottom: 12px;
}

.case-mismatch-box {
  background: #fff5f5;
  border: 1px solid #ffc9c9;
  border-radius: 6px;
  padding: 10px 14px;
  margin-bottom: 12px;
  font-size: 12.5px;
  color: #c92a2a;
}

.case-mismatch-box ul {
  margin: 6px 0 0;
  padding-left: 20px;
}

.drill-side-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 16px;
}

.side-col {
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 12px;
  background: var(--surface-2);
}

.side-stg4 .side-hdr {
  color: #1c5fd6;
  font-weight: 700;
  font-size: 12px;
  margin-bottom: 6px;
  text-transform: uppercase;
}

.side-stg10 .side-hdr {
  color: #2b8a3e;
  font-weight: 700;
  font-size: 12px;
  margin-bottom: 6px;
  text-transform: uppercase;
}

.side-status {
  font-size: 13px;
  margin-bottom: 4px;
}

.side-reqs {
  font-size: 12px;
  color: var(--ink-3);
}

.side-err {
  background: var(--code-bg);
  color: #ff8585;
  padding: 8px;
  border-radius: 4px;
  font-family: var(--mono);
  font-size: 11px;
  white-space: pre-wrap;
  word-break: break-all;
  margin-top: 8px;
  max-height: 120px;
  overflow-y: auto;
}

.aligned-reqs-section {
  margin-top: 16px;
}

.reqs-title {
  margin: 0 0 8px;
  font-size: 13.5px;
  font-weight: 650;
}

.aligned-reqs-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 11.5px;
  border: 1px solid var(--line);
}

.aligned-reqs-table th {
  background: var(--surface-2);
  padding: 6px 8px;
  border-bottom: 1px solid var(--line);
  text-align: left;
}

.aligned-reqs-table td {
  padding: 6px 8px;
  border-bottom: 1px solid var(--line);
}

.row-req-diff {
  background: #fff0f6;
}

.req-match-ok {
  color: var(--pass);
  font-weight: 700;
}

.req-match-diff {
  color: #c92a2a;
  font-weight: 700;
}
'''

if '3D Parity Matrix & Drilldown Styles' not in css:
    css += parity_styles
    with open(STYLES_CSS, "w", encoding="utf-8", newline="\n") as f:
        f.write(css)
    print("Updated styles.css with Parity styles successfully.")
