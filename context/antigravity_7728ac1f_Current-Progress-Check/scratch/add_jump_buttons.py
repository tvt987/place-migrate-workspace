import os

APP_JS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"
STYLES_CSS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\styles.css"
INDEX_HTML = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\index.html"

# 1. Update app.js
with open(APP_JS, "r", encoding="utf-8") as f:
    js = f.read()

# Add jump button into toolbarHtml
old_toolbar = """      '<div class="parity-filter-buttons">' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "ALL" ? " active" : "") + '" data-mode="ALL">Tất cả màn hình (' + matrix.length + ')</button>' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "DIFF_ONLY" ? " active" : "") + '" data-mode="DIFF_ONLY">Chỉ ô lệch (CONTENT_DIFF + BUG)</button>' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "FAIL_ONLY" ? " active" : "") + '" data-mode="FAIL_ONLY">Chỉ màn có lỗi</button>' +
      '</div>' +"""

new_toolbar = """      '<div class="parity-filter-buttons">' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "ALL" ? " active" : "") + '" data-mode="ALL">Tất cả màn hình (' + matrix.length + ')</button>' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "DIFF_ONLY" ? " active" : "") + '" data-mode="DIFF_ONLY">Chỉ ô lệch (CONTENT_DIFF + BUG)</button>' +
        '<button type="button" class="btn-parity-filter' + (parityState.filterMode === "FAIL_ONLY" ? " active" : "") + '" data-mode="FAIL_ONLY">Chỉ màn có lỗi</button>' +
      '</div>' +
      '<button type="button" class="btn-jump-inspector" id="btnJumpInspector" title="Cuộn ngay tới Bảng So Sánh Tham Số & Payload">🎯 Xem So Sánh Tham Số &amp; Payload (Inspector) &darr;</button>' +"""

if old_toolbar in js:
    js = js.replace(old_toolbar, new_toolbar)
    print("Added btnJumpInspector to toolbarHtml.")

# Add floating button to panel.innerHTML in renderParityTab
old_panel_html = """      matrixTableHtml +
      drillDownHtml +
    '</section>';"""

new_panel_html = """      matrixTableHtml +
      drillDownHtml +
      '<button type="button" class="floating-jump-btn" id="btnFloatingInspector" title="Cuộn tới Bảng So Sánh Tham Số & Payload">🎯 So Sánh Tham Số &amp; Payload &darr;</button>' +
    '</section>';"""

if old_panel_html in js:
    js = js.replace(old_panel_html, new_panel_html)
    print("Added floating-jump-btn to renderParityTab.")

# Bind click events for jump buttons in bindParityEvents
old_bind = """    var closeBtn = panel.querySelector("#btnCloseDrill");
    if (closeBtn) {
      closeBtn.addEventListener("click", function () {
        parityState.selectedScreen = null;
        parityState.selectedDim = null;
        parityState.selectedTestKey = null;
        renderParityTab(payloadById(state.pid));
      });
    }"""

new_bind = """    var closeBtn = panel.querySelector("#btnCloseDrill");
    if (closeBtn) {
      closeBtn.addEventListener("click", function () {
        parityState.selectedScreen = null;
        parityState.selectedDim = null;
        parityState.selectedTestKey = null;
        renderParityTab(payloadById(state.pid));
      });
    }

    function scrollDownToInspector() {
      var dd = document.getElementById("parityDrillDown");
      if (dd) dd.scrollIntoView({ behavior: "smooth", block: "start" });
    }
    var jBtn = panel.querySelector("#btnJumpInspector");
    if (jBtn) jBtn.addEventListener("click", scrollDownToInspector);
    var fBtn = panel.querySelector("#btnFloatingInspector");
    if (fBtn) fBtn.addEventListener("click", scrollDownToInspector);"""

if old_bind in js:
    js = js.replace(old_bind, new_bind)
    print("Bound jump buttons events in bindParityEvents.")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(js)

# 2. Update styles.css
with open(STYLES_CSS, "r", encoding="utf-8") as f:
    css = f.read()

btn_styles = """
/* Jump buttons for Parity Parameter Inspector */
.btn-jump-inspector {
  background: #094294;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 6px 14px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s, transform 0.1s;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12);
  margin-left: auto;
}
.btn-jump-inspector:hover {
  background: #073270;
  transform: translateY(-1px);
}
.floating-jump-btn {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #1c5fd6;
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  padding: 10px 18px;
  border-radius: 30px;
  box-shadow: 0 4px 14px rgba(28,95,214,0.35);
  border: none;
  cursor: pointer;
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
}
.floating-jump-btn:hover {
  background: #154bb3;
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(28,95,214,0.45);
}
"""

if ".btn-jump-inspector" not in css:
    css += "\n" + btn_styles
    with open(STYLES_CSS, "w", encoding="utf-8") as f:
        f.write(css)
    print("Added jump button styles to styles.css.")

# 3. Bump cache buster in index.html to v=20261019l
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("styles.css?v=20261019k", "styles.css?v=20261019l")
html = html.replace("app.js?v=20261019k", "app.js?v=20261019l")

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("Bumped cache buster in index.html to v=20261019l.")
