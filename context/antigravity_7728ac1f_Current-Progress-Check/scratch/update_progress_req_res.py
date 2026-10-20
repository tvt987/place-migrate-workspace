import codecs

PROGRESS_FILE = r"E:\Work\Place_Migrate\WORKSPACE_PROGRESS.md"

with codecs.open(PROGRESS_FILE, "r", "utf-8-sig") as f:
    content = f.read()

# 1. Update PR list in 2.2 cci-store-location-web
old_prs = '''    - PR #31 (`dev -> staging10` - Restore Dimension Matrix & Keep Clean UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/31
    - PR #32 (`dev -> staging` - Restore Dimension Matrix & Keep Clean UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/32'''

new_prs = '''    - PR #31 (`dev -> staging10` - Restore Dimension Matrix & Keep Clean UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/31
    - PR #32 (`dev -> staging` - Restore Dimension Matrix & Keep Clean UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/32
    - PR #33 (`dev -> staging10` - Fix Playwright Param Comparison): https://bitbucket.org/concung/cci-store-location-web/pull-requests/33
    - PR #34 (`dev -> staging` - Fix Playwright Param Comparison): https://bitbucket.org/concung/cci-store-location-web/pull-requests/34
    - PR #35 (`dev -> staging10` - Deep Request Payload & Response Body Inspector): https://bitbucket.org/concung/cci-store-location-web/pull-requests/35
    - PR #36 (`dev -> staging` - Deep Request Payload & Response Body Inspector): https://bitbucket.org/concung/cci-store-location-web/pull-requests/36'''

if old_prs in content:
    content = content.replace(old_prs, new_prs)

# 2. Update Deep Parameter Diff description
old_inspector = '''        * **⚡ Khối Đối Chiếu Tham Số Network STG4 ↔ STG10 (Deep Parameter Diff Table):** Bảng so sánh từng cặp HTTP Request kèm chi tiết tham số query string (`?param=...`) và body payload (`paramDiffs`), hiển thị rõ ràng từng tham số `✓ Khớp` hoặc `≠ Lệch` với badge trực quan.'''

new_inspector = '''        * **⚡ Khối So Sánh Toàn Diện Request Payload & Response Body (Deep Request/Response Inspector):**
          - **Cột Endpoint & HTTP Method:** Badge chuẩn REST (`GET`, `POST`, `PUT`, `DELETE`) kèm đường dẫn API rõ ràng.
          - **Cột 📤 Request Payload (STG4 ↔ STG10):** Tự động liên kết dữ liệu nhập liệu từ Playwright Action (ví dụ: `Fill "4"` vào ô `#keyword`) thành payload tìm kiếm (`keyword="4"`) đối với các request AJAX POST; bóc tách query parameters đối với GET. Khắc phục triệt để tình trạng hiển thị nhầm "Không có query parameters / Request tĩnh".
          - **Cột 📥 Response (STG4 ↔ STG10):** Hiển thị rõ ràng HTTP Status Code (200 OK, 404, 500) và Content-Type (`application/json`, `text/html`).
          - **Ngăn Kéo DevTools Mở Rộng (`👁️ Chi tiết`):** Khi bấm nút `👁️ Chi tiết`, mở drawer 2 cột trực quan (Trái: Dữ liệu gửi đi gồm Method, Path, STG4 Payload, STG10 Payload; Phải: Phản hồi từ Server gồm Status, Content-Type, STG4 Response Body Preview, STG10 Response Body Preview).
          - **Bảo toàn giao diện tương thích:** Đóng gói hoàn chỉnh trong tab Parity, hoàn toàn không làm xáo trộn tab Chi tiết và các tab hiện hữu.'''

if old_inspector in content:
    content = content.replace(old_inspector, new_inspector)

# 3. Update SCM sweep progress
old_scm = '''  - **Tiến trình quét tiếp theo:** Auto-Healing Runner (`task-4943`) đang quét fail-fast:
    + Màn 316 (`promotion-schemes`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 317 (`promotions-create`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Đang tiếp tục quét màn 318+.'''

new_scm = '''  - **Tiến trình quét tiếp theo:** Auto-Healing Runner (`task-4943`) đang quét fail-fast:
    + Màn 316 (`promotion-schemes`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 317 (`promotions-create`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 319 (`promotion-top-shows`): STG10 PASS.
    + Màn 320 (`province-symbol-taxs`): Both Failed (origin-same).
    + Màn 321 (`purchase-orders`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 322 (`purchase-orders-edit`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 323 (`receiving-reasons`): Both Failed (origin-same).
    + Màn 324 (`receiving-statuses`): Both Failed (origin-same).
    + Đang tiếp tục quét màn 325+ (`receiving-types`).'''

if old_scm in content:
    content = content.replace(old_scm, new_scm)

with codecs.open(PROGRESS_FILE, "w", "utf-8-sig") as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md with UTF-8 BOM successfully!")
