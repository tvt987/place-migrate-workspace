with open('e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update 2.2 section
sec_22_target = """- **Kiểm Thử Nghiệm Thu Mục Tiêu Sau Khi Dập Khuôn (Rule 13):**
  - Đã kích hoạt chạy targeted test suite xác nhận chức năng bị ảnh hưởng: `e2e/home` (Home Dashboard, API data fetching, URL normalize) và `e2e/login` (Keycloak SSO auth, Session persistence, Cookie `.PlaceWeb`).
  - Kết quả: **33 Passed, 1 Skipped, 0 Failed** (Thời gian: 2.3 phút). Nghiệm thu đạt 100%!"""

sec_22_replacement = """- **Kiểm Thử Nghiệm Thu Mục Tiêu Sau Khi Dập Khuôn (Rule 13):**
  - Đã kích hoạt chạy targeted test suite xác nhận chức năng bị ảnh hưởng: `e2e/home` (Home Dashboard, API data fetching, URL normalize) và `e2e/login` (Keycloak SSO auth, Session persistence, Cookie `.PlaceWeb`).
  - Kết quả: **33 Passed, 1 Skipped, 0 Failed** (Thời gian: 2.3 phút). Nghiệm thu đạt 100%!
- **Nâng Cấp Báo Cáo Local & Sổ Theo Dõi Lỗi (Rule 14 - Đã Triển Khai Tiên Phong Cho Place Web):**
  - Xây dựng sổ theo dõi lỗi tập trung `03_qa/reports/defect-registry.json` gom toàn bộ 9 nhóm lỗi đã khắc phục và dập khuôn từ trước đến nay (Redis Keyring, URL Normalization, Fallback ApisUrl 404, Fallback IDSUrl TC-FUNC-005, FormOptions ValueCountLimit, Directives Boundary Guard, ReturnUrl Same-Origin, Case-Insensitive Linux Static Files, EPPlus DataValidation Order).
  - Nâng cấp bộ sinh báo cáo `03_qa/scripts/generate-report.js`:
    + Render giao diện HTML local tương tác 3 Tabs: Chi tiết Test Cases, Phân loại nhóm lỗi & So sánh Code Cũ vs Mới, Đối chiếu Parity NET4 vs NET10.
    + Khối so sánh Code Cũ (Gây lỗi) vs Code Mới (Đã fix) trực quan, có liên kết 2 chiều từ từng test case sang mã lỗi đã fix.
    + Bổ sung section tổng hợp nhóm lỗi & tình trạng fix vào file markdown `fail-list-*.md`.
    + Giữ nguyên 100% tính tương thích với luồng đẩy dữ liệu lên server portal report."""

if sec_22_target in text:
    text = text.replace(sec_22_target, sec_22_replacement)
    print("Sec 2.2 updated successfully")
else:
    print("Sec 2.2 target not found")

# 2. Update Section 3
sec_3_target = "- **Job 3 (Targeted Regression Verification - Rule 13):** Sau mỗi lần dập khuôn và push code, kích hoạt ngay test case của module bị ảnh hưởng trực tiếp (Targeted Test) để nghiệm thu nhanh chóng mà không cần chạy lại toàn bộ suite từ đầu."
sec_3_replacement = """- **Job 3 (Targeted Regression Verification - Rule 13):** Sau mỗi lần dập khuôn và push code, kích hoạt ngay test case của module bị ảnh hưởng trực tiếp (Targeted Test) để nghiệm thu nhanh chóng mà không cần chạy lại toàn bộ suite từ đầu.
- **Job 4 (Local Defect Matrix & Code Comparison Report - Rule 14):** Tích hợp sổ theo dõi lỗi (`defect-registry.json`) vào báo cáo local HTML/Markdown, phân loại nhóm lỗi, hiển thị code diff cũ vs mới, liên kết 2 chiều giữa test cases và mã bug fix."""

if sec_3_target in text:
    text = text.replace(sec_3_target, sec_3_replacement)
    print("Sec 3 updated successfully")
else:
    print("Sec 3 target not found")

with open('e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md', 'wb') as f:
    f.write(bytes([0xEF, 0xBB, 0xBF]) + text.encode('utf-8'))
print("WORKSPACE_PROGRESS.md updated cleanly with UTF-8 BOM")
