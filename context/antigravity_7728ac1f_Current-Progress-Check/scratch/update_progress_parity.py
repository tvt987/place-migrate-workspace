import os
import sys

progress_path = r"E:\Work\Place_Migrate\WORKSPACE_PROGRESS.md"

with open(progress_path, "r", encoding="utf-8-sig") as f:
    content = f.read()

# Replace or insert updates under section 2.2
target_marker = "    - PR #24 (`dev -> staging` - Visual Defect Map & Code Diff): https://bitbucket.org/concung/cci-store-location-web/pull-requests/24\n"
new_prs = target_marker + (
    "    - PR #25 (`dev -> staging10` - 3D Parity Comparator & Interactive Viewer Matrix): https://bitbucket.org/concung/cci-store-location-web/pull-requests/25\n"
    "    - PR #26 (`dev -> staging` - 3D Parity Comparator & Interactive Viewer Matrix): https://bitbucket.org/concung/cci-store-location-web/pull-requests/26\n"
)

content = content.replace(target_marker, new_prs)

# Add section for 3D Parity Comparator
parity_marker = "- **Nâng Cấp Báo Cáo Local & Sổ Theo Dõi Lỗi (Rule 14 - Đã Triển Khai Tiên Phong Cho Place Web):**\n"
parity_section = (
    "- **Hệ Thống Đối Chiếu Parity Đa Chiều (3D Parity Matrix Viewer - Triển Khai Tiên Phong Cho Place Web theo PLAN_PARITY_COMPARE_LOCAL_REPORT.md):**\n"
    "  - **Stage G1 (Bộ Sinh & Đối Chiếu Dữ Liệu Parity Đa Chiều `compare-dim.py`):**\n"
    "    + Đối chiếu tự động giữa 2 bản chạy gần nhất: `test-net4-report-latest.json` (STG4) vs `test-mssql-report-latest.json` (STG10).\n"
    "    + Khớp chính xác 559 test cases trên 45 màn qua match key `(screen, tc, file, scenario)`.\n"
    "    + Áp dụng quy tắc lọc nhiễu chuẩn (§4):\n"
    "      * Lọc bỏ hoàn toàn các request SSO (`/accounts/login`, `/accounts/callback`, `/realms/master`, v.v.).\n"
    "      * Tách biệt các static assets (`.css`, `.js`, font, `/content/`, `/bundles/`) và đối chiếu phân biệt chữ hoa/thường trên Linux filesystem (`CASE_MISMATCH`).\n"
    "      * Masking động các token ngẫu nhiên (`__RequestVerificationToken`, GUID, ISO Timestamps) trước khi đối chiếu hash/path.\n"
    "    + **Kết quả Tổng Quan 3D Parity Store Location:**\n"
    "      * `PARITY_OK`: **405** (72.5%) — Hành vi STG4 và STG10 hoàn toàn khớp.\n"
    "      * `CONTENT_DIFF`: **81** (14.5%) — Cả 2 đều PASS nhưng có sự sai khác về số lượng hoặc URL chức năng.\n"
    "      * `BOTH_SKIP`: **39** (7.0%) — Cả 2 đều SKIP.\n"
    "      * `IMPROVED`: **21** (3.8%) — STG4 FAIL/SKIP nhưng STG10 đã xử lý PASS thành công.\n"
    "      * `ORIGIN_SAME`: **9** (1.6%) — Lỗi hệ thống gốc từ thời .NET 4.\n"
    "      * `MIGRATE_BUG`: **4** (0.7%) — STG4 PASS nhưng STG10 FAIL (đã phân loại điều tra).\n"
    "      * Chiều `AUTH` đạt tỷ lệ Parity xuất sắc **98%** (50/51 pass).\n"
    "      * Phát hiện **1,584** điểm lệch chữ hoa/thường giữa tài nguyên tĩnh Windows vs Linux.\n"
    "  - **Stage G2 (Giao Diện Tab 'So Sánh Parity (STG4 ↔ STG10)' trên Report Viewer Local):**\n"
    "    + Thêm tab chuyên biệt **'So Sánh Parity (STG4 ↔ STG10)'** trên thanh điều hướng của Web Viewer (`http://localhost:8932/`).\n"
    "    + **Ma Trận Parity 3D (Screen × Dimension × Verdict):** Bảng tổng hợp trực quan 45 màn × 7 chiều kỹ thuật (`LOAD`, `FLOW`, `VALIDATION`, `AUTH`, `PERM`, `STATE`, `EDGE`) với các badge màu sắc chuẩn hoá (Xanh lá: OK, Tím: Content Diff, Đỏ: Migrate Bug, Xanh lam: Improved, Cam: Origin Same, Xám: Skip, Trắng: Hole).\n"
    "    + **Bộ Lọc Phân Tích Thông Minh:** Thanh toolbar cho phép tìm kiếm nhanh theo tên màn, lọc theo nhóm trạng thái (Tất cả, Cần chú ý [Migrate Bug + Content Diff], Chỉ Migrate Bug, Chỉ Lệch Request).\n"
    "    + **Ngăn So Soi Chi Tiết (Drill-Down Inspector):** Click vào bất kỳ ô ma trận nào sẽ mở ngay Drawer chi tiết bên dưới:\n"
    "      * Danh sách các test case thuộc ô được chọn kèm badge verdict.\n"
    "      * Khối so sánh trạng thái song song STG4 vs STG10 (Status, Duration, Request Count, Error Logs).\n"
    "      * Cảnh báo `CASE_MISMATCH` nếu phát hiện tài nguyên tĩnh bị lệch chữ hoa/thường trên Linux.\n"
    "      * Bảng đối chiếu song song từng cặp HTTP Request (Method, Path, Status, Khớp/Lệch) sau khi đã làm sạch token nhiễu.\n"
    "    + **Backend Daemon Endpoint:** Bổ sung `GET /api/compare-dim` trên `serve.py` và nhúng sẵn dữ liệu vào `data.js` để viewer hoạt động độc lập không phụ thuộc backend.\n"
)

content = content.replace(parity_marker, parity_section + parity_marker)

# Update timestamp in header
import re
content = re.sub(
    r">\s*\*\*Cập nhật mới nhất:\*\*.*?\n",
    "> **Cập nhật mới nhất:** 2026-10-19 16:58:00 (Đã hoàn tất Triển khai 3D Parity Comparator & Interactive Viewer Matrix cho Place Web)\n",
    content,
    count=1
)

# Write back with UTF-8 BOM
with open(progress_path, "w", encoding="utf-8-sig") as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md successfully with UTF-8 BOM.")
