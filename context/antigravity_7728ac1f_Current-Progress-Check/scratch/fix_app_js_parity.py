import os
import re

APP_JS = r"e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"

with open(APP_JS, "r", encoding="utf-8") as f:
    js = f.read()

# Load integrate_parity_tab.py to get the exact parity_impl string
SCRIPT_PATH = r"C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\7728ac1f-b786-4675-a12f-920ecbd68eb6\scratch\integrate_parity_tab.py"
with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    script_content = f.read()

# Extract parity_impl between parity_impl = ''' and '''\n\nif 'renderParityTab' not in js:
start_marker = "parity_impl = '''\n"
end_marker = "'''\n\nif 'renderParityTab' not in js:"
start_idx = script_content.find(start_marker) + len(start_marker)
end_idx = script_content.find(end_marker)
parity_impl = script_content[start_idx:end_idx]

# Remove renderDimMatrix(p); from renderAll if present
js = js.replace("    renderDimMatrix(p);\n", "")
js = js.replace("    renderParityTab(p);\n    renderDimMatrix(p);", "    renderParityTab(p);")

# Insert parity_impl right before function renderAll() {
target_render_all = re.search(r"[ \t]*function renderAll\(\) \{", js)
if not target_render_all:
    print("Error: could not find function renderAll() { in app.js")
    exit(1)

render_all_pos = target_render_all.start()

# Check if renderParityTab is already defined
if "function renderParityTab(" not in js:
    js = js[:render_all_pos] + "\n" + parity_impl + "\n\n  " + js[render_all_pos:].lstrip()
    print("Inserted parity_impl before renderAll.")
else:
    print("renderParityTab is already defined.")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(js)

print("app.js updated successfully.")
