import os
import re

APP_JS = r"e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"
STYLES_CSS = r"e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\styles.css"

# 1. Update app.js
with open(APP_JS, "r", encoding="utf-8") as f:
    js_content = f.read()

# Replace TAB_PANELS
js_content = js_content.replace(
    'var TAB_PANELS = ["detail", "defect", "blocked"];',
    'var TAB_PANELS = ["detail", "defect", "blocked", "registry"];'
)

# Add defectRegistry state near top of IIFE
old_store = 'var store = (window.__REPORT_DATA__ && window.__REPORT_DATA__.payloads) ? window.__REPORT_DATA__ : { payloads: [], sources: [] };'
new_store = '''var store = (window.__REPORT_DATA__ && window.__REPORT_DATA__.payloads) ? window.__REPORT_DATA__ : { payloads: [], sources: [] };
  var defectRegistry = (window.__REPORT_DATA__ && window.__REPORT_DATA__.defectRegistry) ? window.__REPORT_DATA__.defectRegistry : { defects: [] };

  function findDefectsForTest(t) {
    if (!t || !defectRegistry || !defectRegistry.defects) return [];
    var tcCode = (t.tc || "").trim().toUpperCase();
    var scenario = (t.scenario || "").toLowerCase();
    var route = (t.route || t.screen || "").toLowerCase();
    return defectRegistry.defects.filter(function (d) {
      if (d.relatedTestCases && d.relatedTestCases.some(function (c) { return tcCode && c.toUpperCase() === tcCode; })) return true;
      return false;
    });
  }'''

if old_store in js_content and 'findDefectsForTest' not in js_content:
    js_content = js_content.replace(old_store, new_store)

# Update renderTestList to add tc-fix-badge
old_tcrow = '''        body += '<button type="button" class="tcrow' + cls + '" data-key="' + esc(key) + '"' + (sel ? ' aria-current="true"' : "") + ">" +
          '<span class="pill ' + esc(t.status) + '">' + esc(t.status) + "</span>" +
          '<span class="tc-name" title="' + esc(t.scenario) + '">' + esc(t.scenario.replace(/\\s*\\[[A-Z-]+\\]\\s*$/, "")) + "</span>" +
          (t.tc ? '<span class="tc-sub">' + esc(t.tc) + "</span>" : "") +
          "</button>";'''

new_tcrow = '''        var hasFix = findDefectsForTest(t).length > 0;
        body += '<button type="button" class="tcrow' + cls + '" data-key="' + esc(key) + '"' + (sel ? ' aria-current="true"' : "") + ">" +
          '<span class="pill ' + esc(t.status) + '">' + esc(t.status) + "</span>" +
          '<span class="tc-name" title="' + esc(t.scenario) + '">' + esc(t.scenario.replace(/\\s*\\[[A-Z-]+\\]\\s*$/, "")) + "</span>" +
          (hasFix ? '<span class="tc-fix-badge" title="Đã có giải pháp fix trong Defect Registry">Fix</span>' : "") +
          (t.tc ? '<span class="tc-sub">' + esc(t.tc) + "</span>" : "") +
          "</button>";'''

if old_tcrow in js_content:
    js_content = js_content.replace(old_tcrow, new_tcrow)

# Update renderTestDetail to inject tc-fix-callout and button listeners
old_render_detail_start = '''    var html = '<div class="ep-head"><h2><span class="pill ' + esc(t.status) + '">' + esc(t.status) + "</span> " + esc(t.scenario) + "</h2>" +
      '<button type="button" class="copyctx" title="Copy đủ context (file nguồn, route, flow, network, console, error) để hỏi nguyên nhân lỗi" ' +
      'aria-label="Copy context để hỏi nguyên nhân lỗi">' + COPY_SVG + " Copy context</button></div>" +
      '<p class="dsub">' + esc(epLabel(ep)) +
      (t.observedRoute || t.route ? " · observed " + esc(t.observedRoute || t.route) : "") +
      (t.disposition ? " · " + esc(t.disposition) : "") +
      " · " + meta.join(" · ") + "</p>" +
      '<dl class="kv">' +'''

new_render_detail_start = '''    var matchedFixes = findDefectsForTest(t);
    var fixCalloutHtml = "";
    if (matchedFixes.length) {
      fixCalloutHtml = matchedFixes.map(function (f) {
        return '<div class="tc-fix-callout">' +
          '<div class="fix-callout-hdr">' +
            '<span class="fix-callout-badge">🛠️ ĐÃ KHẮC PHỤC (' + esc(f.id) + ')</span>' +
            '<span class="fix-callout-status">' + esc(f.status) + '</span>' +
          '</div>' +
          '<div class="fix-callout-title">' + esc(f.title) + '</div>' +
          '<div class="fix-callout-desc">' + esc(f.fixedWhat) + '</div>' +
          '<button type="button" class="btn-jump-fix" data-fix="' + esc(f.id) + '">Xem chi tiết fix &amp; so sánh code &rarr;</button>' +
        '</div>';
      }).join("");
    }

    var html = '<div class="ep-head"><h2><span class="pill ' + esc(t.status) + '">' + esc(t.status) + "</span> " + esc(t.scenario) + "</h2>" +
      '<button type="button" class="copyctx" title="Copy đủ context (file nguồn, route, flow, network, console, error) để hỏi nguyên nhân lỗi" ' +
      'aria-label="Copy context để hỏi nguyên nhân lỗi">' + COPY_SVG + " Copy context</button></div>" +
      '<p class="dsub">' + esc(epLabel(ep)) +
      (t.observedRoute || t.route ? " · observed " + esc(t.observedRoute || t.route) : "") +
      (t.disposition ? " · " + esc(t.disposition) : "") +
      " · " + meta.join(" · ") + "</p>" +
      fixCalloutHtml +
      '<dl class="kv">' +'''

if old_render_detail_start in js_content:
    js_content = js_content.replace(old_render_detail_start, new_render_detail_start)

# Add event listener for .btn-jump-fix inside renderTestDetail
old_detail_ev = '''    els.detail.querySelectorAll(".copypath").forEach(function (btn) {
      btn.addEventListener("click", function () {
        copyText(btn.getAttribute("data-path") || "", btn, "Copied ✓");
      });
    });'''

new_detail_ev = '''    els.detail.querySelectorAll(".copypath").forEach(function (btn) {
      btn.addEventListener("click", function () {
        copyText(btn.getAttribute("data-path") || "", btn, "Copied ✓");
      });
    });
    els.detail.querySelectorAll(".btn-jump-fix").forEach(function (btn) {
      btn.addEventListener("click", function () {
        jumpToFix(btn.getAttribute("data-fix"));
      });
    });'''

if old_detail_ev in js_content:
    js_content = js_content.replace(old_detail_ev, new_detail_ev)

# Add renderRegistryTab, jumpToFix, jumpToTestByCode before renderAll
registry_code = '''
  var registryFilterCategory = "ALL";
  function jumpToFix(fixId) {
    registryFilterCategory = "ALL";
    switchTab("registry");
    var p = payloadById(state.pid);
    if (p) renderRegistryTab(p);
    setTimeout(function () {
      var card = document.getElementById("card-fix-" + fixId);
      if (card) {
        card.scrollIntoView({ behavior: "smooth", block: "center" });
        card.classList.add("card-highlight");
        setTimeout(function () { card.classList.remove("card-highlight"); }, 2500);
      }
    }, 60);
  }
  window.__jumpToFix = jumpToFix;

  function jumpToTestByCode(tcCode) {
    switchTab("detail");
    var p = payloadById(state.pid);
    if (!p) return;
    var matchedScreen = null;
    var matchedTest = null;
    allScreens(p).some(function (s) {
      return (s.tests || []).some(function (t) {
        if (t.tc && t.tc.toUpperCase() === tcCode.toUpperCase()) {
          matchedScreen = s;
          matchedTest = t;
          return true;
        }
        return false;
      });
    });
    if (matchedScreen && matchedTest) {
      state.selectedEp = epLabel(matchedScreen);
      state.selectedTest = testKey(matchedTest);
      renderList(p);
      renderDetail(p);
    }
  }

  function renderRegistryTab(p) {
    var panel = document.getElementById("panel-registry");
    if (!panel) return;
    var defects = (defectRegistry && defectRegistry.defects) ? defectRegistry.defects : [];
    var countEl = document.getElementById("defectRegistryCount");
    if (countEl) countEl.textContent = defects.length;

    if (!defects.length) {
      panel.innerHTML = '<section class="registry-tab"><h2 class="dim-section-title">Nhóm Lỗi &amp; So Sánh Code (Defect Registry)</h2>' +
        '<p class="ov-line">Chưa có dữ liệu sổ lỗi (defect-registry.json). Chạy test hoặc cập nhật defect-registry.json để xem.</p></section>';
      return;
    }

    var categories = Array.from(new Set(defects.map(function (d) { return d.category; })));
    var catCounts = {};
    categories.forEach(function (c) { catCounts[c] = 0; });
    defects.forEach(function (d) { catCounts[d.category] = (catCounts[d.category] || 0) + 1; });

    var catButtons = '<button type="button" class="cat-chip' + (registryFilterCategory === "ALL" ? " active" : "") + '" data-cat="ALL">Tất cả (' + defects.length + ')</button>' +
      categories.map(function (c) {
        return '<button type="button" class="cat-chip' + (registryFilterCategory === c ? " active" : "") + '" data-cat="' + esc(c) + '">' +
          esc(c) + ' (' + catCounts[c] + ')</button>';
      }).join("");

    var filtered = registryFilterCategory === "ALL" ? defects : defects.filter(function (d) { return d.category === registryFilterCategory; });

    var cardsHtml = filtered.map(function (d) {
      var sevCls = (d.severity || "").toLowerCase();
      var prLinks = (d.pullRequests || []).map(function (u) {
        var num = u.split("/").pop();
        return '<a href="' + esc(u) + '" target="_blank" rel="noopener" class="pr-link">PR #' + esc(num) + ' &nearr;</a>';
      }).join(" ");
      var commitBadges = (d.commits || []).map(function (cm) {
        return '<span class="commit-tag" title="' + esc(cm.message || "") + '">' + esc(cm.hash ? cm.hash.slice(0, 7) : "-") + '</span>';
      }).join(" ");
      var tcBadges = (d.relatedTestCases || []).map(function (tc) {
        return '<button type="button" class="tc-tag" data-tc="' + esc(tc) + '" title="Bấm để chuyển tới chi tiết test case">' + esc(tc) + '</button>';
      }).join(" ");

      var codeComp = d.codeComparison || {};
      var oldCode = codeComp.oldCodeSnippet || "// Không có code cũ";
      var newCode = codeComp.newCodeSnippet || "// Không có code mới";
      var explanation = codeComp.explanation || "";

      return '<div class="defect-card" id="card-fix-' + esc(d.id) + '">' +
        '<div class="defect-card-header">' +
          '<div class="defect-header-left">' +
            '<span class="fix-id-badge">' + esc(d.id) + '</span>' +
            '<span class="fix-sev-badge sev-' + esc(sevCls) + '">' + esc(d.severity) + '</span>' +
            '<span class="fix-status-badge">' + esc(d.status) + '</span>' +
            '<h3 class="fix-title">' + esc(d.title) + '</h3>' +
          '</div>' +
          '<span class="fix-cat-tag">' + esc(d.category) + '</span>' +
        '</div>' +
        '<div class="defect-card-body">' +
          '<div class="defect-grid-info">' +
            '<div class="defect-info-item"><span class="info-lbl">Triệu chứng:</span> <span class="info-val">' + esc(d.symptoms) + '</span></div>' +
            '<div class="defect-info-item"><span class="info-lbl">Nguyên nhân gốc:</span> <span class="info-val">' + esc(d.rootCause) + '</span></div>' +
            '<div class="defect-info-item"><span class="info-lbl">Đã khắc phục:</span> <span class="info-val font-semibold text-pass">' + esc(d.fixedWhat) + '</span></div>' +
            (codeComp.filePath ? '<div class="defect-info-item"><span class="info-lbl">File nguồn:</span> <code class="file-code">' + esc(codeComp.filePath) + '</code></div>' : '') +
            '<div class="defect-meta-row">' +
              (tcBadges ? '<div class="meta-item"><span class="meta-lbl">Test Cases:</span> ' + tcBadges + '</div>' : '') +
              (prLinks ? '<div class="meta-item"><span class="meta-lbl">Pull Requests:</span> ' + prLinks + '</div>' : '') +
              (commitBadges ? '<div class="meta-item"><span class="meta-lbl">Commits:</span> ' + commitBadges + '</div>' : '') +
            '</div>' +
          '</div>' +
          '<div class="code-diff-box">' +
            '<div class="diff-header-bar">' +
              '<span class="diff-title">So Sánh Code Cũ (Gây Lỗi) vs Code Mới (Đã Fix)</span>' +
            '</div>' +
            '<div class="diff-columns">' +
              '<div class="diff-col diff-col-old">' +
                '<div class="diff-col-hdr">❌ Code Cũ (Gây lỗi / Origin)</div>' +
                '<pre class="diff-pre"><code>' + esc(oldCode) + '</code></pre>' +
              '</div>' +
              '<div class="diff-col diff-col-new">' +
                '<div class="diff-col-hdr">✅ Code Mới (Đã khắc phục / Target)</div>' +
                '<pre class="diff-pre"><code>' + esc(newCode) + '</code></pre>' +
              '</div>' +
            '</div>' +
            (explanation ? '<div class="diff-footer-expl"><strong>💡 Rationale:</strong> ' + esc(explanation) + '</div>' : '') +
          '</div>' +
        '</div>' +
      '</div>';
    }).join("");

    panel.innerHTML = '<section class="registry-tab">' +
      '<div class="registry-tab-hdr">' +
        '<div>' +
          '<h2 class="dim-section-title">Nhóm Lỗi Kỹ Thuật Đã Khắc Phục &amp; So Sánh Code Cũ vs Mới</h2>' +
          '<p class="registry-sub">Tổng hợp ' + defects.length + ' lỗi và giải pháp dập khuôn chuẩn hóa trên Store Location Web (' + categories.length + ' nhóm kỹ thuật)</p>' +
        '</div>' +
        '<div class="registry-kpi-summary">' +
          '<div class="reg-kpi"><span class="num">' + defects.length + '</span><span class="lbl">Tổng mã fix</span></div>' +
          '<div class="reg-kpi"><span class="num text-pass">' + defects.length + '</span><span class="lbl">Đã giải quyết</span></div>' +
          '<div class="reg-kpi"><span class="num text-accent">' + categories.length + '</span><span class="lbl">Nhóm lỗi</span></div>' +
        '</div>' +
      '</div>' +
      '<div class="cat-filter-bar">' + catButtons + '</div>' +
      '<div class="defect-cards-list">' + cardsHtml + '</div>' +
    '</section>';

    panel.querySelectorAll(".cat-chip").forEach(function (btn) {
      btn.addEventListener("click", function () {
        registryFilterCategory = btn.getAttribute("data-cat");
        renderRegistryTab(p);
      });
    });

    panel.querySelectorAll(".tc-tag").forEach(function (tag) {
      tag.addEventListener("click", function () {
        var tcCode = tag.getAttribute("data-tc");
        if (tcCode) jumpToTestByCode(tcCode);
      });
    });
  }
'''

if 'renderRegistryTab' not in js_content:
    js_content = js_content.replace('  function renderAll() {', registry_code + '\n  function renderAll() {')

# Add renderRegistryTab(p) inside renderAll
old_render_all = '''  function renderAll() {
    var p = payloadById(state.pid);
    if (!p) return;
    renderKpis(p);
    updateVisLabel();
    renderFeatureFilter(p);
    renderDefectTab(p);
    renderBlockedTab(p);
    renderDimMatrix(p);
    renderList(p);
    renderDetail(p);
    renderCompare();
  }'''

new_render_all = '''  function renderAll() {
    var p = payloadById(state.pid);
    if (!p) return;
    renderKpis(p);
    updateVisLabel();
    renderFeatureFilter(p);
    renderDefectTab(p);
    renderBlockedTab(p);
    renderRegistryTab(p);
    renderDimMatrix(p);
    renderList(p);
    renderDetail(p);
    renderCompare();
  }'''

if old_render_all in js_content:
    js_content = js_content.replace(old_render_all, new_render_all)

# Update refreshFromServer to also fetch api/defect-registry
old_refresh = '    if (window.location.protocol === "file:") return;'
new_refresh = '''    if (window.location.protocol === "file:") return;
    fetch("api/defect-registry", { cache: "no-store" }).then(function (r) {
      return r.ok ? r.json() : null;
    }).then(function (reg) {
      if (reg && reg.defects) {
        defectRegistry = reg;
        var countEl = document.getElementById("defectRegistryCount");
        if (countEl) countEl.textContent = reg.defects.length;
        renderRegistryTab(payloadById(state.pid));
      }
    }).catch(function () {});'''

if old_refresh in js_content and 'api/defect-registry' not in js_content:
    js_content = js_content.replace(old_refresh, new_refresh)

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(js_content)
print("Updated app.js successfully.")

# 2. Update styles.css
with open(STYLES_CSS, "r", encoding="utf-8") as f:
    css_content = f.read()

styles_to_append = '''
/* ---------- Defect Registry & Code Comparison Styles ---------- */
.registry-tab {
  padding: 16px 20px 40px;
  max-width: 1400px;
  margin: 0 auto;
}

.registry-tab-hdr {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--line);
}

.registry-sub {
  margin: 4px 0 0;
  color: var(--ink-3);
  font-size: 13px;
}

.registry-kpi-summary {
  display: flex;
  gap: 12px;
}

.reg-kpi {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 8px 16px;
  text-align: center;
  min-width: 90px;
}

.reg-kpi .num {
  font-size: 20px;
  font-weight: 700;
  display: block;
  line-height: 1.2;
}

.reg-kpi .lbl {
  font-size: 11px;
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.text-pass { color: var(--pass) !important; }
.text-accent { color: var(--accent) !important; }
.font-semibold { font-weight: 600; }

.cat-filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
}

.cat-chip {
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--ink-2);
  border-radius: 20px;
  padding: 5px 14px;
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s ease;
}

.cat-chip:hover {
  background: var(--hover-bg);
  border-color: var(--hover-line);
}

.cat-chip.active {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}

.defect-cards-list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.defect-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  transition: border-color 0.2s, box-shadow 0.2s;
}

.defect-card.card-highlight {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(28, 95, 214, 0.35);
}

.defect-card-header {
  background: var(--surface-2);
  padding: 12px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid var(--line);
}

.defect-header-left {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.fix-id-badge {
  background: var(--accent);
  color: #fff;
  font-family: var(--mono);
  font-size: 12px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
}

.fix-sev-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 4px;
  text-transform: uppercase;
}

.sev-critical { background: var(--fail-bg); color: var(--fail); border: 1px solid var(--fail-line); }
.sev-high { background: var(--timeout-bg); color: var(--timeout); }
.sev-medium { background: var(--accent-bg); color: var(--accent-deep); }

.fix-status-badge {
  background: var(--pass-bg);
  color: var(--pass);
  border: 1px solid var(--pass-line);
  font-size: 11px;
  font-weight: 600;
  padding: 2px 7px;
  border-radius: 4px;
}

.fix-title {
  margin: 0;
  font-size: 15px;
  font-weight: 650;
  color: var(--ink);
}

.fix-cat-tag {
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--ink-2);
  font-size: 12px;
  padding: 3px 10px;
  border-radius: 12px;
  white-space: nowrap;
}

.defect-card-body {
  padding: 16px 18px;
}

.defect-grid-info {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
  font-size: 13.5px;
}

.defect-info-item {
  display: flex;
  gap: 8px;
  line-height: 1.45;
}

.info-lbl {
  font-weight: 600;
  color: var(--ink-2);
  min-width: 130px;
  flex-shrink: 0;
}

.info-val {
  color: var(--ink);
  flex: 1;
}

.file-code {
  background: var(--surface-2);
  padding: 1px 6px;
  border-radius: 4px;
  font-family: var(--mono);
  font-size: 12px;
  color: var(--ink-2);
}

.defect-meta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 6px;
  padding-top: 8px;
  border-top: 1px dashed var(--line);
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12.5px;
}

.meta-lbl {
  font-weight: 600;
  color: var(--ink-3);
}

.pr-link {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
  background: var(--accent-bg);
  padding: 2px 8px;
  border-radius: 4px;
}

.pr-link:hover {
  text-decoration: underline;
}

.commit-tag {
  background: var(--surface-2);
  border: 1px solid var(--line);
  font-family: var(--mono);
  font-size: 11px;
  padding: 2px 6px;
  border-radius: 4px;
}

.tc-tag {
  background: #eef4ff;
  border: 1px solid #c7dcff;
  color: var(--accent-deep);
  font-family: var(--mono);
  font-size: 11px;
  padding: 2px 6px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.15s;
}

.tc-tag:hover {
  background: var(--accent);
  color: #fff;
}

/* Code Diff Box */
.code-diff-box {
  background: #14171c;
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid #232a35;
}

.diff-header-bar {
  background: #1e242e;
  padding: 8px 14px;
  border-bottom: 1px solid #2d3542;
  font-size: 12px;
  font-weight: 600;
  color: #9eb0c6;
}

.diff-columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: #2d3542;
}

@media (max-width: 960px) {
  .diff-columns {
    grid-template-columns: 1fr;
  }
}

.diff-col {
  background: #14171c;
  display: flex;
  flex-direction: column;
}

.diff-col-hdr {
  padding: 6px 12px;
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.diff-col-old .diff-col-hdr {
  background: rgba(201, 42, 42, 0.2);
  color: #ff8585;
  border-bottom: 1px solid rgba(201, 42, 42, 0.3);
}

.diff-col-new .diff-col-hdr {
  background: rgba(43, 138, 62, 0.2);
  color: #69db7c;
  border-bottom: 1px solid rgba(43, 138, 62, 0.3);
}

.diff-pre {
  margin: 0;
  padding: 12px;
  font-family: var(--mono);
  font-size: 12px;
  line-height: 1.5;
  color: #e6edf3;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-all;
  flex: 1;
}

.diff-footer-expl {
  background: #1a2029;
  padding: 8px 14px;
  border-top: 1px solid #2d3542;
  font-size: 12px;
  color: #aab8cc;
}

/* Callout in Test Detail Panel */
.tc-fix-callout {
  background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%);
  border: 1px solid #a5d6a7;
  border-radius: var(--radius);
  padding: 12px 14px;
  margin: 12px 0 16px;
}

.fix-callout-hdr {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4px;
}

.fix-callout-badge {
  font-weight: 700;
  font-size: 12px;
  color: #1b5e20;
}

.fix-callout-status {
  font-size: 11px;
  font-weight: 600;
  color: #2e7d32;
  background: #fff;
  padding: 1px 6px;
  border-radius: 4px;
  border: 1px solid #c8e6c9;
}

.fix-callout-title {
  font-size: 13.5px;
  font-weight: 650;
  color: #1b5e20;
  margin-bottom: 4px;
}

.fix-callout-desc {
  font-size: 12.5px;
  color: #2e7d32;
  margin-bottom: 8px;
  line-height: 1.4;
}

.btn-jump-fix {
  background: #2e7d32;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 4px 10px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

.btn-jump-fix:hover {
  background: #1b5e20;
}

/* Fix Badge in Middle Panel Test List */
.tc-fix-badge {
  background: #e8f5e9;
  color: #2e7d32;
  border: 1px solid #a5d6a7;
  font-size: 10px;
  font-weight: 700;
  padding: 1px 5px;
  border-radius: 3px;
  margin-left: 4px;
  flex-shrink: 0;
}
'''

if 'Defect Registry & Code Comparison Styles' not in css_content:
    css_content += styles_to_append
    with open(STYLES_CSS, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated styles.css successfully.")
