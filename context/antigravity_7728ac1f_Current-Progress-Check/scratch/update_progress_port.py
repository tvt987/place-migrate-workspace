import os

path = r'e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md'
with open(path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

old_str = """    - PR #17 (`dev -> staging10` - Tooling): https://bitbucket.org/concung/cci-store-location-web/pull-requests/17
    - PR #18 (`dev -> staging` - Tooling): https://bitbucket.org/concung/cci-store-location-web/pull-requests/18"""

new_str = """    - PR #17 (`dev -> staging10` - Tooling): https://bitbucket.org/concung/cci-store-location-web/pull-requests/17
    - PR #18 (`dev -> staging` - Tooling): https://bitbucket.org/concung/cci-store-location-web/pull-requests/18
    - PR #19 (`dev -> staging10` - Report Serve Script): https://bitbucket.org/concung/cci-store-location-web/pull-requests/19
    - PR #20 (`dev -> staging` - Report Serve Script): https://bitbucket.org/concung/cci-store-location-web/pull-requests/20"""

content = content.replace(old_str, new_str)

old_serv = "    + Giữ nguyên 100% tính tương thích với luồng đẩy dữ liệu lên server portal report."
new_serv = """    + Giữ nguyên 100% tính tương thích với luồng đẩy dữ liệu lên server portal report.
    + Bổ sung local HTTP report server chạy ngầm tại Port **8080** (`npm run report:serve`), truy cập nhanh tại: `http://localhost:8080/` (hoặc mở trực tiếp file `03_qa/reports/test-mssql-report-latest.html`)."""

content = content.replace(old_serv, new_serv)

with open(path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md successfully with UTF-8 BOM.")
