import os

path = r'e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md'
with open(path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

old_prs = """    - PR #21 (`dev -> staging10` - Defect Registry Viewer): https://bitbucket.org/concung/cci-store-location-web/pull-requests/21
    - PR #22 (`dev -> staging` - Defect Registry Viewer): https://bitbucket.org/concung/cci-store-location-web/pull-requests/22"""

new_prs = """    - PR #21 (`dev -> staging10` - Defect Registry Viewer): https://bitbucket.org/concung/cci-store-location-web/pull-requests/21
    - PR #22 (`dev -> staging` - Defect Registry Viewer): https://bitbucket.org/concung/cci-store-location-web/pull-requests/22
    - PR #23 (`dev -> staging10` - Visual Defect Map & Code Diff): https://bitbucket.org/concung/cci-store-location-web/pull-requests/23
    - PR #24 (`dev -> staging` - Visual Defect Map & Code Diff): https://bitbucket.org/concung/cci-store-location-web/pull-requests/24"""

content = content.replace(old_prs, new_prs)

old_text = "      - Bảng phân loại nhóm lỗi kỹ thuật, filter theo Category, hiển thị chi tiết mức độ, trạng thái, triệu chứng, nguyên nhân gốc, đã fix được gì, file nguồn, commit & PR link."

new_text = """      - **Bản Đồ Tổng Quan Các Nhóm Lỗi (Visual Defect Map):** Bố trí dạng lưới card trực quan ngay trên đầu tab, mô tả rõ ràng từng nhóm lỗi là gì, nguyên nhân gốc rễ phát sinh khi migrate sang .NET 10 trên Linux/Kubernetes và giải pháp cốt lõi. Bấm vào bất kỳ card nhóm lỗi nào sẽ lọc và cuộn mượt đến ngay chi tiết.
      - **Khối So Sánh Code Cũ (Gây lỗi) vs Code Mới (Đã fix):** Đã sửa hiển thị đầy đủ các đoạn code C# / JSON cấu hình thực tế cho toàn bộ 9 mã lỗi (không bị rỗng)."""

content = content.replace(old_text, new_text)

with open(path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md with Visual Map PRs.")
