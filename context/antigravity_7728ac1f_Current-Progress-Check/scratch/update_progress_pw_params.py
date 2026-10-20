import os

FILE = r"E:\Work\Place_Migrate\WORKSPACE_PROGRESS.md"

with open(FILE, "r", encoding="utf-8-sig") as f:
    content = f.read()

# Update timestamp and PRs
old_ts = "> **Cập nhật mới nhất:** 2026-10-19 17:10:00 (Đã hoàn tất Daily 17:00 Commit Sync & Auto-Healing Fix Lỗi Xuất Excel SCM Màn 315)"
new_ts = "> **Cập nhật mới nhất:** 2026-10-19 17:35:00 (Hoàn tất Trực Quan Hoá Tham Số Playwright, Đối Chiếu Request Parity & Sửa Lỗi Asset 404 Trên QA Viewer)"

content = content.replace(old_ts, new_ts)

old_prs = """    - PR #27 (`dev -> staging10` - Fix renderParityTab ReferenceError): https://bitbucket.org/concung/cci-store-location-web/pull-requests/27
    - PR #28 (`dev -> staging` - Fix renderParityTab ReferenceError): https://bitbucket.org/concung/cci-store-location-web/pull-requests/28"""

new_prs = """    - PR #27 (`dev -> staging10` - Fix renderParityTab ReferenceError): https://bitbucket.org/concung/cci-store-location-web/pull-requests/27
    - PR #28 (`dev -> staging` - Fix renderParityTab ReferenceError): https://bitbucket.org/concung/cci-store-location-web/pull-requests/28
    - PR #29 (`dev -> staging10` - Playwright Input Parameters & Parity Request Diff UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/29
    - PR #30 (`dev -> staging` - Playwright Input Parameters & Parity Request Diff UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/30"""

content = content.replace(old_prs, new_prs)

# Add section description of the new features under 2.2
old_stage_g2 = """    + **Ngăn So Soi Chi Tiết (Drill-Down Inspector):** Click vào bất kỳ ô ma trận nào sẽ mở ngay Drawer chi tiết bên dưới:
      * Danh sách các test case thuộc ô được chọn kèm badge verdict.
      * Khối so sánh trạng thái song song STG4 vs STG10 (Status, Duration, Request Count, Error Logs).
      * Cảnh báo `CASE_MISMATCH` nếu phát hiện tài nguyên tĩnh bị lệch chữ hoa/thường trên Linux.
      * Bảng đối chiếu song song từng cặp HTTP Request (Method, Path, Status, Khớp/Lệch) sau khi đã làm sạch token nhiễu."""

new_stage_g2 = """    + **Ngăn So Soi Chi Tiết (Drill-Down Inspector) & Trực Quan Hoá Tham Số Playwright:**
      * **🎯 Hộp Tham Số & Thao Tác Playwright (Playwright Context & Input Parameters):** Tự động bóc tách các hành động Playwright (`Fill`, `Click`, `SelectOption`, `Goto`), hiển thị bảng chi tiết gồm Thao tác, Tham số/Giá trị nhập vào (`.pw-val-badge`), Phần tử đích (Selector) và Thời gian thực thi.
      * **⚡ Khối Đối Chiếu Tham Số Network STG4 ↔ STG10 (Deep Parameter Diff Table):** Bảng so sánh từng cặp HTTP Request kèm chi tiết tham số query string (`?param=...`) và body payload (`paramDiffs`), hiển thị rõ ràng từng tham số `✓ Khớp` hoặc `≠ Lệch` với badge trực quan.
      * **Tích Hợp Trực Tiếp Trên Cả 2 Tab:** Khối Tham số Playwright và Đối chiếu Parity STG4 ↔ STG10 được nhúng đồng bộ ngay trên tab **"Chi tiết"** (`renderTestDetail`) và tab **"So Sánh Parity"** (`renderDrillDownContent`), kèm nút chuyển tab 2 chiều thông minh.
      * **Khắc Phục Lỗi 404 Missing Screenshot Assets (`serve.py`):** Khi các screenshot cũ bị Playwright dọn dẹp giữa các đợt chạy mới, endpoint `/api/asset` tự động phản hồi ảnh SVG placeholder chuẩn HTTP 200, loại bỏ hoàn toàn lỗi đỏ 404 trong Console trình duyệt.
      * **Tự Động Khởi Tạo Trạng Thái Mặc Định:** Tab Parity tự động chọn màn đầu tiên thay vì để trống drill-down; bổ sung thanh điều hướng nhanh `[📊 Bảng Ma Trận] [🎯 Chi Tiết Tham Số]`.
      * Cảnh báo `CASE_MISMATCH` nếu phát hiện tài nguyên tĩnh bị lệch chữ hoa/thường trên Linux."""

content = content.replace(old_stage_g2, new_stage_g2)

# Write back with UTF-8 BOM
with open(FILE, "w", encoding="utf-8-sig") as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md preserving UTF-8 BOM.")
