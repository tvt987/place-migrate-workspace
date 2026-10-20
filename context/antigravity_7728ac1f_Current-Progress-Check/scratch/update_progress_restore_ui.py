import os

FILE = r"E:\Work\Place_Migrate\WORKSPACE_PROGRESS.md"

with open(FILE, "r", encoding="utf-8-sig") as f:
    content = f.read()

# Update timestamp
old_ts = "> **Cập nhật mới nhất:** 2026-10-19 17:35:00"
new_ts = "> **Cập nhật mới nhất:** 2026-10-19 20:36:00"
content = content.replace(old_ts, new_ts)

# Update PR list for store-location
old_prs = """    - PR #29 (`dev -> staging10` - Playwright Input Parameters & Parity Request Diff UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/29
    - PR #30 (`dev -> staging` - Playwright Input Parameters & Parity Request Diff UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/30"""

new_prs = """    - PR #29 (`dev -> staging10` - Playwright Input Parameters & Parity Request Diff UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/29
    - PR #30 (`dev -> staging` - Playwright Input Parameters & Parity Request Diff UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/30
    - PR #31 (`dev -> staging10` - Restore Dimension Matrix & Keep Clean UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/31
    - PR #32 (`dev -> staging` - Restore Dimension Matrix & Keep Clean UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/32"""

content = content.replace(old_prs, new_prs)

# Update section description under 2.2
old_desc = """      * **Tích Hợp Trực Tiếp Trên Cả 2 Tab:** Khối Tham số Playwright và Đối chiếu Parity STG4 ↔ STG10 được nhúng đồng bộ ngay trên tab **"Chi tiết"** (`renderTestDetail`) và tab **"So Sánh Parity"** (`renderDrillDownContent`), kèm nút chuyển tab 2 chiều thông minh."""

new_desc = """      * **Bảo Toàn 100% Giao Diện Gốc Tab "Chi tiết" & Khôi Phục Bảng Dimension:** Giữ nguyên giao diện chi tiết gốc không làm xáo trộn; khôi phục hoàn chỉnh bảng **"Ma trận màn hình × dimension (45 màn)"** (`renderDimMatrix`) ở cuối tab Chi tiết.
      * **Đóng Gói Tính Năng Mới Chuyên Biệt Trong Tab Parity:** Toàn bộ tính năng mở rộng đối chiếu Parity 3D, hộp tham số Playwright (`drill-pw-inputs-box`) và bảng so sánh chi tiết Network requests/parameters (`paramDiffs`) được đặt trọn vẹn trong tab riêng **"So Sánh Parity (STG4 ↔ STG10)"** để trình duyệt và xin ý kiến chốt từ Leader mà không làm thay đổi các chức năng vốn có."""

content = content.replace(old_desc, new_desc)

# Update SCM status
old_scm_text = "Auto-Healing Runner (`task-4943`) đang tiếp tục quét fail-fast từ màn 316 (`promotion-schemes`) đến màn 396."
new_scm_text = """Auto-Healing Runner (`task-4943`) đang quét fail-fast:
    + Màn 316 (`promotion-schemes`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 317 (`promotions-create`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Đang tiếp tục quét màn 318+."""

content = content.replace(old_scm_text, new_scm_text)

# Write back with UTF-8 BOM
with open(FILE, "w", encoding="utf-8-sig") as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md successfully.")
