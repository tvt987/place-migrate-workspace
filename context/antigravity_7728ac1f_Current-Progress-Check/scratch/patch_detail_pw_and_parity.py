import os
import re

APP_JS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"
STYLES_CSS = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\styles.css"
INDEX_HTML = r"E:\Work\Place_Migrate\cci-store-location-web\.report\viewer\index.html"

# 1. Update index.html cache busters to v=20261019j
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("styles.css?v=20261019i", "styles.css?v=20261019j")
html = html.replace("app.js?v=20261019i", "app.js?v=20261019j")

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html cache busters to v=20261019j.")

# 2. Add styles to styles.css
with open(STYLES_CSS, "r", encoding="utf-8") as f:
    css = f.read()

new_styles = '''
/* Playwright Inputs & Parameters Box in Detail View */
.pw-inputs-card {
  background: #f0f7ff;
  border: 1px solid #c8e1ff;
  border-radius: 6px;
  padding: 12px 14px;
  margin: 12px 0;
}
.pw-card-hdr {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}
.pw-card-title {
  font-size: 13px;
  font-weight: 700;
  color: #094294;
}
.pw-param-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 11.5px;
  margin-top: 8px;
  background: #fff;
  border-radius: 4px;
  overflow: hidden;
  border: 1px solid #d0e2ff;
}
.pw-param-table th {
  background: #e5f1ff;
  color: #094294;
  font-weight: 600;
  text-align: left;
  padding: 6px 8px;
  border-bottom: 1px solid #d0e2ff;
}
.pw-param-table td {
  padding: 6px 8px;
  border-bottom: 1px solid #edf5ff;
  vertical-align: middle;
}
.pw-param-table tr:last-child td {
  border-bottom: none;
}
.pw-action-tag {
  display: inline-block;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 3px;
  text-transform: uppercase;
}
.pw-action-fill { background: #e7f5ff; color: #1971c2; border: 1px solid #a5d8ff; }
.pw-action-click { background: #ebfbee; color: #2f9e44; border: 1px solid #b2f2bb; }
.pw-action-select { background: #fff4e6; color: #d9480f; border: 1px solid #ffd8a8; }
.pw-action-goto { background: #f3f0ff; color: #6741d9; border: 1px solid #d0bfff; }
.pw-action-other { background: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }

.pw-val-badge {
  font-family: var(--font-mono, monospace);
  font-weight: 600;
  background: #fff9db;
  color: #b25e00;
  padding: 2px 5px;
  border-radius: 3px;
  border: 1px solid #fcc419;
}

/* Detail Parity Comparison Box */
.detail-parity-box {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  padding: 12px 14px;
  margin: 12px 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.detail-parity-hdr {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}
.detail-parity-title {
  font-size: 13px;
  font-weight: 700;
  color: var(--ink-1);
}
.btn-jump-parity {
  background: #1c5fd6;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  cursor: pointer;
  transition: background 0.15s;
}
.btn-jump-parity:hover {
  background: #154bb3;
}
.detail-parity-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-bottom: 10px;
}
.detail-parity-col {
  padding: 8px 10px;
  border-radius: 4px;
  font-size: 11.5px;
}
.parity-col-stg4 { background: #f8f9fa; border: 1px solid #e9ecef; }
.parity-col-stg10 { background: #f0f7ff; border: 1px solid #d0e2ff; }
.parity-col-hdr { font-weight: 700; font-size: 11px; margin-bottom: 4px; color: var(--ink-2); }

/* Quick Nav in Parity Tab */
.parity-quick-nav {
  display: flex;
  gap: 8px;
  margin: 10px 0;
}
.btn-parity-nav {
  display: inline-block;
  background: #f1f3f5;
  color: #495057;
  padding: 5px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  text-decoration: none;
  border: 1px solid #ced4da;
  transition: all 0.15s;
}
.btn-parity-nav:hover {
  background: #e9ecef;
  color: #212529;
}
'''

if ".pw-inputs-card" not in css:
    css += "\n" + new_styles
    with open(STYLES_CSS, "w", encoding="utf-8") as f:
        f.write(css)
    print("Added new styles to styles.css.")
else:
    print("styles.css already has new styles.")
