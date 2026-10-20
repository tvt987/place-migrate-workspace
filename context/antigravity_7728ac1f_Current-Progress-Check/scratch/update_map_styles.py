import os

STYLES_CSS = r"e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\styles.css"

with open(STYLES_CSS, "r", encoding="utf-8") as f:
    css = f.read()

map_styles = '''
/* ---------- Visual Defect Architecture Map Styles ---------- */
.defect-map-section {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 20px;
  margin-bottom: 24px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.03);
}

.map-section-hdr {
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--line);
}

.map-section-title {
  margin: 0 0 4px;
  font-size: 16px;
  font-weight: 700;
  color: var(--ink);
}

.map-section-sub {
  margin: 0;
  font-size: 13px;
  color: var(--ink-3);
}

.defect-map-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
}

.cat-map-card {
  background: var(--surface-2);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 14px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
}

.cat-map-card:hover {
  background: var(--surface);
  border-color: var(--accent);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.08);
}

.cat-map-card.active-card {
  background: var(--surface);
  border-color: var(--accent);
  box-shadow: 0 0 0 2px var(--accent);
}

.cat-map-hdr {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.cat-map-icon {
  font-size: 24px;
  background: var(--surface);
  border: 1px solid var(--line);
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.cat-map-title-box {
  flex: 1;
}

.cat-map-name {
  font-weight: 700;
  font-size: 14px;
  color: var(--ink);
  line-height: 1.3;
}

.cat-map-count {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--pass);
  margin-top: 2px;
}

.cat-map-body {
  font-size: 12.5px;
  line-height: 1.45;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}

.cat-map-row {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.cat-map-tag {
  font-weight: 700;
  font-size: 10.5px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  display: inline-block;
  align-self: flex-start;
  padding: 1px 6px;
  border-radius: 3px;
}

.tag-what { background: #e3f2fd; color: #1565c0; }
.tag-cause { background: #ffebee; color: #c62828; }
.tag-sol { background: #e8f5e9; color: #2e7d32; }

.cat-map-desc {
  color: var(--ink-2);
}

.cat-map-footer {
  margin-top: 14px;
  padding-top: 10px;
  border-top: 1px solid var(--line);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cat-map-fixes {
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
}

.map-fix-pill {
  background: var(--surface);
  border: 1px solid var(--line);
  font-family: var(--mono);
  font-size: 10.5px;
  font-weight: 700;
  color: var(--accent);
  padding: 1px 6px;
  border-radius: 4px;
}

.btn-filter-cat {
  background: none;
  border: none;
  color: var(--accent);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  padding: 2px 4px;
}

.btn-filter-cat:hover {
  text-decoration: underline;
}

.list-section-hdr {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--line);
}

.list-section-title {
  margin: 0;
  font-size: 15px;
  font-weight: 700;
  color: var(--ink);
}

.active-cat-name {
  color: var(--accent);
}
'''

if 'Visual Defect Architecture Map Styles' not in css:
    css += map_styles

with open(STYLES_CSS, "w", encoding="utf-8", newline="\n") as f:
    f.write(css)

print("Updated styles.css with Map styles successfully.")
