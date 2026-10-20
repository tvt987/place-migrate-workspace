import os

path = r'e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md'
with open(path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

old_prs = """    - PR #19 (`dev -> staging10` - Report Serve Script): https://bitbucket.org/concung/cci-store-location-web/pull-requests/19
    - PR #20 (`dev -> staging` - Report Serve Script): https://bitbucket.org/concung/cci-store-location-web/pull-requests/20"""

new_prs = """    - PR #19 (`dev -> staging10` - Report Serve Script): https://bitbucket.org/concung/cci-store-location-web/pull-requests/19
    - PR #20 (`dev -> staging` - Report Serve Script): https://bitbucket.org/concung/cci-store-location-web/pull-requests/20
    - PR #21 (`dev -> staging10` - Defect Registry Viewer): https://bitbucket.org/concung/cci-store-location-web/pull-requests/21
    - PR #22 (`dev -> staging` - Defect Registry Viewer): https://bitbucket.org/concung/cci-store-location-web/pull-requests/22"""

content = content.replace(old_prs, new_prs)

old_upgrade = """    + Bổ sung local HTTP report server chạy ngầm tại Port **8080** (`npm run report:serve`), truy cập nhanh tại: `http://localhost:8080/` (hoặc mở trực tiếp file `03_qa/reports/test-mssql-report-latest.html`)."""

new_upgrade = """    + **Tích hợp trực tiếp vào Web Report Viewer chuẩn (`.report/viewer` - Port 8932):**
      - Bổ sung tab **"Nhóm Lỗi & So Sánh Code (9)"** ngay trên thanh tab bar song song với "Chi tiết", "Lỗi (DEFECT)", "Bị chặn (BLOCKED)".
      - Bảng phân loại nhóm lỗi kỹ thuật, filter theo Category, hiển thị chi tiết mức độ, trạng thái, triệu chứng, nguyên nhân gốc, đã fix được gì, file nguồn, commit & PR link.
      - **Khối Split Diff Code Cũ (Origin) vs Code Mới (Target)** trực quan cho từng mã fix `FIX-01` đến `FIX-09`.
      - **Liên kết 2 chiều thông minh:** Test case nào thuộc diện đã fix sẽ hiện badge `Fix` ở cột giữa, và hiện hộp thoại callout `🛠️ ĐÃ KHẮC PHỤC` ở panel chi tiết bên phải với nút click nhảy thẳng tới card so sánh code của mã lỗi đó.
      - Phục vụ trực tiếp qua local daemon: **`http://localhost:8932/`** (hoặc mở file tĩnh qua `data.js`)."""

content = content.replace(old_upgrade, new_upgrade)

with open(path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md successfully.")
