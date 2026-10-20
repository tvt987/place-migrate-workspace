import codecs

PROGRESS_FILE = r"E:\Work\Place_Migrate\WORKSPACE_PROGRESS.md"

with codecs.open(PROGRESS_FILE, "r", "utf-8-sig") as f:
    content = f.read()

# 1. Update PR list in 2.2 cci-store-location-web
old_prs = '''    - PR #35 (`dev -> staging10` - Deep Request Payload & Response Body Inspector): https://bitbucket.org/concung/cci-store-location-web/pull-requests/35
    - PR #36 (`dev -> staging` - Deep Request Payload & Response Body Inspector): https://bitbucket.org/concung/cci-store-location-web/pull-requests/36'''

new_prs = '''    - PR #35 (`dev -> staging10` - Deep Request Payload & Response Body Inspector): https://bitbucket.org/concung/cci-store-location-web/pull-requests/35
    - PR #36 (`dev -> staging` - Deep Request Payload & Response Body Inspector): https://bitbucket.org/concung/cci-store-location-web/pull-requests/36
    - PR #37 (`dev -> staging10` - Pure Playwright Network Evidence Capture): https://bitbucket.org/concung/cci-store-location-web/pull-requests/37
    - PR #38 (`dev -> staging` - Pure Playwright Network Evidence Capture): https://bitbucket.org/concung/cci-store-location-web/pull-requests/38'''

if old_prs in content:
    content = content.replace(old_prs, new_prs)

# 2. Update description of Pure Playwright Evidence
old_desc = '''        * **⚡ Khối So Sánh Toàn Diện Request Payload & Response Body (Deep Request/Response Inspector):**
          - **Cột Endpoint & HTTP Method:** Badge chuẩn REST (`GET`, `POST`, `PUT`, `DELETE`) kèm đường dẫn API rõ ràng.
          - **Cột 📤 Request Payload (STG4 ↔ STG10):** Tự động liên kết dữ liệu nhập liệu từ Playwright Action (ví dụ: `Fill "4"` vào ô `#keyword`) thành payload tìm kiếm (`keyword="4"`) đối với các request AJAX POST; bóc tách query parameters đối với GET. Khắc phục triệt để tình trạng hiển thị nhầm "Không có query parameters / Request tĩnh".
          - **Cột 📥 Response (STG4 ↔ STG10):** Hiển thị rõ ràng HTTP Status Code (200 OK, 404, 500) và Content-Type (`application/json`, `text/html`).
          - **Ngăn Kéo DevTools Mở Rộng (`👁️ Chi tiết`):** Khi bấm nút `👁️ Chi tiết`, mở drawer 2 cột trực quan (Trái: Dữ liệu gửi đi gồm Method, Path, STG4 Payload, STG10 Payload; Phải: Phản hồi từ Server gồm Status, Content-Type, STG4 Response Body Preview, STG10 Response Body Preview).
          - **Bảo toàn giao diện tương thích:** Đóng gói hoàn chỉnh trong tab Parity, hoàn toàn không làm xáo trộn tab Chi tiết và các tab hiện hữu.'''

new_desc = '''        * **⚡ Khối So Sánh Toàn Diện Request Payload & Response Body (Deep Request/Response Inspector) — 100% Nguyên Bản Từ Playwright:**
          - **Loại Bỏ Hoàn Toàn Logic Giả Định / Suy Diễn:** Tuyệt đối không mock hay suy diễn payload từ Playwright flow steps. Mọi dữ liệu Request và Response được ghi nhận trực tiếp 100% từ network listener của Playwright (`req.postData()`, `req.url()`, `res.status()`, `await res.text()`).
          - **Cột Endpoint & HTTP Method:** Phân loại REST chuẩn (`GET`, `POST`, `PUT`, `DELETE`) với màu sắc trực quan.
          - **Cột 📤 Request Payload (STG4 ↔ STG10):** Thể hiện trung thực những gì gửi qua mạng. Với các request POST không truyền tham số qua body (như `/LocationTypeIndex/Search` gửi `{}` từ AngularJS do lọc phía client), Playwright ghi nhận trung thực là body rỗng; đối với GET hiển thị query parameters (`?param=...`).
          - **Cột 📥 Response (STG4 ↔ STG10):** Trích xuất HTTP Status Code và Response Body thực tế từ máy chủ. Đã đối chiếu thực tế giữa STG4 (ID 681) và STG10 (ID 680):
            + STG4 (.NET 4 Framework): Định dạng ngày tháng kiểu epoch `\\/Date(1615791125120)\\/`.
            + STG10 (.NET 10 System.Text.Json): Định dạng ngày tháng ISO chuẩn `2021-03-15T13:52:05.12`.
          - **Ngăn Kéo DevTools Mở Rộng (`👁️ Chi tiết`):** Bấm `👁️ Chi tiết` mở drawer 2 cột để xem toàn bộ Request Headers/Payload và Response Body JSON thực tế từ máy chủ.
          - **Bảo toàn giao diện tương thích:** Đóng gói hoàn chỉnh trong tab Parity, hoàn toàn không làm xáo trộn tab Chi tiết và các tab hiện hữu.'''

if old_desc in content:
    content = content.replace(old_desc, new_desc)

# 3. Update SCM sweep progress
old_scm = '''  - **Tiến trình quét tiếp theo:** Auto-Healing Runner (`task-4943`) đang quét fail-fast:
    + Màn 316 (`promotion-schemes`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 317 (`promotions-create`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 319 (`promotion-top-shows`): STG10 PASS.
    + Màn 320 (`province-symbol-taxs`): Both Failed (origin-same).
    + Màn 321 (`purchase-orders`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 322 (`purchase-orders-edit`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 323 (`receiving-reasons`): Both Failed (origin-same).
    + Màn 324 (`receiving-statuses`): Both Failed (origin-same).
    + Đang tiếp tục quét màn 325+ (`receiving-types`).'''

new_scm = '''  - **Tiến trình quét tiếp theo:** Auto-Healing Runner (`task-4943`) đang quét fail-fast:
    + Màn 316 (`promotion-schemes`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 317 (`promotions-create`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 319 (`promotion-top-shows`): STG10 PASS.
    + Màn 320 (`province-symbol-taxs`): Both Failed (origin-same).
    + Màn 321 (`purchase-orders`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 322 (`purchase-orders-edit`): **100% PARITY PASS (STG10=0, STG4=0)**.
    + Màn 323 (`receiving-reasons`): Both Failed (origin-same).
    + Màn 324 (`receiving-statuses`): Both Failed (origin-same).
    + Màn 325 (`receiving-types`): Both Failed (origin-same).
    + Màn 326 (`red-bill-cancel-reasons`): Both Failed (origin-same).
    + Màn 327 (`return-types`): Both Failed (origin-same).
    + Màn 328 (`sale-kpi-stores`): Both Failed (origin-same).
    + Màn 329 (`search-price`): Both Failed (origin-same).
    + Màn 330 (`shelf`): Both Failed (origin-same).
    + Đang tiếp tục quét màn 331+ (`slide-image-apps`).'''

if old_scm in content:
    content = content.replace(old_scm, new_scm)

with codecs.open(PROGRESS_FILE, "w", "utf-8-sig") as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md successfully with UTF-8 BOM!")
