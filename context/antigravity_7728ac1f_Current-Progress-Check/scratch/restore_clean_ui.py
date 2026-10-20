import os

APP_JS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"

with open(APP_JS, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Restore renderDimMatrix(p) in renderAll()
old_render_all = """  function renderAll() {
    var p = payloadById(state.pid);
    if (!p) return;
    renderKpis(p);
    updateVisLabel();
    renderFeatureFilter(p);
    renderDefectTab(p);
    renderBlockedTab(p);
    renderRegistryTab(p);
    renderParityTab(p);
    renderList(p);
    renderDetail(p);
    renderCompare();
  }"""

new_render_all = """  function renderAll() {
    var p = payloadById(state.pid);
    if (!p) return;
    renderKpis(p);
    updateVisLabel();
    renderFeatureFilter(p);
    renderDefectTab(p);
    renderBlockedTab(p);
    renderDimMatrix(p);
    renderRegistryTab(p);
    renderParityTab(p);
    renderList(p);
    renderDetail(p);
    renderCompare();
  }"""

if old_render_all in code:
    code = code.replace(old_render_all, new_render_all)
    print("Restored renderDimMatrix(p) in renderAll().")
else:
    print("Warning: old_render_all not found!")

# 2. In renderTestDetail: remove playwrightParamsBlock(t) and parityCompareBlock(t)
old_detail_blocks = """    if (t.error) {
      html += isSkipped(t)
        ? '<div class="note"><strong>Lý do skip:</strong> ' + esc(truncateError(t.error)) + "</div>"
        : '<div class="err"><strong>Lỗi:</strong> ' + esc(truncateError(t.error)) + "</div>";
    }
    html += playwrightParamsBlock(t);
    html += parityCompareBlock(t);
    html += flowBlock(t);"""

new_detail_blocks = """    if (t.error) {
      html += isSkipped(t)
        ? '<div class="note"><strong>Lý do skip:</strong> ' + esc(truncateError(t.error)) + "</div>"
        : '<div class="err"><strong>Lỗi:</strong> ' + esc(truncateError(t.error)) + "</div>";
    }
    html += flowBlock(t);"""

if old_detail_blocks in code:
    code = code.replace(old_detail_blocks, new_detail_blocks)
    print("Removed injected blocks from renderTestDetail.")
else:
    print("Warning: old_detail_blocks not found!")

# 3. Remove .btn-jump-parity binding from renderTestDetail
old_jump_binding = """    els.detail.querySelectorAll(".btn-jump-fix").forEach(function (btn) {
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
    });"""

new_jump_binding = """    els.detail.querySelectorAll(".btn-jump-fix").forEach(function (btn) {
      btn.addEventListener("click", function () {
        jumpToFix(btn.getAttribute("data-fix"));
      });
    });"""

if old_jump_binding in code:
    code = code.replace(old_jump_binding, new_jump_binding)
    print("Removed .btn-jump-parity binding from renderTestDetail.")
else:
    print("Warning: old_jump_binding not found!")

# 4. Remove unused helper functions parsePlaywrightAction, playwrightParamsBlock, findCompareDimTest, parityCompareBlock
# They are between line 765 and renderTestDetail
helper_pattern = r"\n  function parsePlaywrightAction\(title\) \{[\s\S]*?renderTestDetail\(p, ep, tests\) \{"
replacement = "\n  function renderTestDetail(p, ep, tests) {"

if "function parsePlaywrightAction" in code:
    import re
    code = re.sub(helper_pattern, replacement, code, count=1)
    print("Removed unused detail helper functions.")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully cleaned app.js!")
