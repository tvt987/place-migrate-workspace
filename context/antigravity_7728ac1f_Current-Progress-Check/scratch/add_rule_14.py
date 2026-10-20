with open('e:/Work/Place_Migrate/AGENTS.md', 'r', encoding='utf-8') as f:
    text = f.read()

rule_14 = """- **14. Phân Loại Nhóm Lỗi, So Sánh Code Cũ vs Mới & Tích Hợp Vào Báo Cáo Test Local (Defect Categorization & Code Comparison Report Rule):**
  - **Quy tắc bắt buộc mỗi khi fix bug hoặc dập khuôn:**
    1. **Phân loại nhóm lỗi:** Gán lỗi vào đúng nhóm danh mục kỹ thuật chuẩn (`Auth & Session / Redis Keyring`, `URL Normalization & Double Slash`, `EPPlus DataValidation Order`, `Routing & Config Fallback`, `FormOptions & Model Binding`, `File Upload & Directives`, `Linux Compatibility & Static Files`, `E2E Playwright Stability`).
    2. **Mô tả chi tiết giải pháp:** Mô tả rõ triệu chứng lỗi, nguyên nhân gốc rễ và đã fix được những gì.
    3. **Đối chiếu Code Cũ vs Code Mới (Before vs After Diff):** Ghi nhận rõ ràng đoạn code cũ viết như thế nào dẫn đến lỗi (Origin / Code cũ) và đoạn code mới đã sửa như thế nào để khắc phục (Target / Code mới), kèm mã commit hash và link PR liên quan.
    4. **Cập nhật dữ liệu vào sổ lỗi (Defect Registry) & Tự động gắn vào Báo cáo Test Local:** Sau mỗi lần fix bug và chạy test case, BẮT BUỘC cập nhật thông tin lỗi vào file registry tập trung của portal (`03_qa/reports/defect-registry.json`) để công cụ tạo báo cáo local (`generate-report.js`) tự động render bảng phân loại nhóm lỗi, tình trạng fix, và khối so sánh code trực quan ngay trên bản báo cáo HTML/Markdown local mà không làm ảnh hưởng đến luồng đẩy dữ liệu lên server portal report.
"""

if '- **14. Phân Loại Nhóm Lỗi' not in text:
    text = text.rstrip() + '\n' + rule_14
    with open('e:/Work/Place_Migrate/AGENTS.md', 'wb') as f:
        f.write(bytes([0xEF, 0xBB, 0xBF]) + text.encode('utf-8'))
    print('Rule 14 added to AGENTS.md successfully with UTF-8 BOM')
else:
    print('Rule 14 already exists in AGENTS.md')
