import re

progress_path = r"E:\Work\Place_Migrate\WORKSPACE_PROGRESS.md"

with open(progress_path, "r", encoding="utf-8-sig") as f:
    content = f.read()

# Update header timestamp
content = re.sub(
    r">\s*\*\*Cập nhật mới nhất:\*\*.*?\n",
    "> **Cập nhật mới nhất:** 2026-10-19 17:10:00 (Đã hoàn tất Daily 17:00 Commit Sync & Auto-Healing Fix Lỗi Xuất Excel SCM Màn 315)\n",
    content,
    count=1
)

# Update Status Matrix for SCM
old_scm_row = "| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🏃 **MÀN 210 & 260 PASS — BACKGROUND SWEEP ĐANG QUÉT MÀN 275+**<br/>• Màn 210–274: Parity Pass 100% (0 migrate bugs)<br/>• Đang chạy sweep ngầm tuần tự (task-3316)<br/>• **Đã dập khuôn HRM/MBM:** Redis DataProtection + UrlNormalize + EPPlus DataValidation order (PR #15 & #16). | • Test Report: ID **117** / file `test-report-latest.json` | Họ màn `pay-forms` (`PayFormSakuras`, `PayForms`) đã fix dứt điểm lỗi Razor 500.<br/>• Màn 260 sau deploy STG10 đã pass 100% parity.<br/>• Đang chạy sweep ngầm tuần tự theo Rule 11. | Tiếp tục tự động quét các màn còn lại, phát hiện migrate-bug sẽ tự fix hoặc báo cáo. |"
new_scm_row = "| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🛠️ **ĐÃ FIX MIGRATE-BUG MÀN 315 (XUẤT EXCEL) — ĐANG CHỜ K8S ROLLOUT PR #17**<br/>• Màn 210–314: Parity Pass 100% (55+ màn pass, các màn fail đều origin-same)<br/>• Màn 315 (`promotions`): Fix lỗi thiếu return ActionResult xuất Excel (PR #17 & #18)<br/>• Auto-healing runner (task-4558) đang chờ rollout để re-verify & quét tiếp màn 316–396. | • Test Report: ID **117** / file `test-report-latest.json` | • Màn 315 xuất Excel 0-byte: Đã fix dứt điểm trên 7 controllers.<br/>• Đã tạo PR #17 & #18, chờ K8s rollout 15 phút. | Tự động re-test màn 315 và quét cạn các màn từ 316 đến 396. |"

if old_scm_row in content:
    content = content.replace(old_scm_row, new_scm_row)

# Update SCM detail section
scm_detail_marker = "    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-scm-web/pull-requests/16\n"
scm_new_details = scm_detail_marker + (
    "    - PR #17 (`dev -> staging10` - Fix Return File Excel Export): https://bitbucket.org/concung/cci-scm-web/pull-requests/17\n"
    "    - PR #18 (`dev -> staging` - Fix Return File Excel Export): https://bitbucket.org/concung/cci-scm-web/pull-requests/18\n"
    "- **Khắc Phục Migrate-Bug Phát Hiện Lúc Sweep Màn 315 (`promotions`) - Continuous Auto-Healing (Rule 11):**\n"
    "  - **Triệu chứng lỗi:** Chạy fail-fast test màn 315 (`promotions`), ca test `TC-SCM-227-014` (Export Excel download) trên STG4 PASS (tải file .xlsx hợp lệ) nhưng trên STG10 FAIL với lỗi: `Error: download '20261019_DSKhuyenMaiDangChay.xlsx' size=0 (min 1024)`.\n"
    "  - **Nguyên nhân gốc rễ:** Trong ASP.NET Core (.NET 10), helper xuất Excel `ResponseExcelAjax` trả về `ActionResult` (`File(bytes, ...)`). Tuy nhiên các action trong controller gọi `ResponseExcelAjax(...)` nhưng bỏ quên từ khóa `return`, rồi ở cuối action lại `return new EmptyResult();`. Hậu quả là HTTP Response trả về body rỗng (0 bytes).\n"
    "  - **Phạm vi khắc phục đồng bộ (7 controllers):** Đã bổ sung `return` cho toàn bộ các action xuất Excel / download template tại:\n"
    "    1. `PromotionsController.cs` (lines 639, 643, 1173, 1178, 1182, 3987, 4124, 4258)\n"
    "    2. `EWalletPromotionsController.cs` (lines 173, 275, 378)\n"
    "    3. `IVENInputOrdersController.cs` (line 163)\n"
    "    4. `OutputUsesController.cs` (line 467)\n"
    "    5. `OutputOrdersController.cs` (line 663)\n"
    "    6. `IVENOutputOrdersController.cs` (line 560)\n"
    "    7. `POSMsController.cs` (line 554)\n"
    "  - **Biên dịch & Git:** `dotnet build` đạt 0 Error(s). Đã merge `--no-ff` vào `dev`, gắn tag `fix/return-excel-file-result-promotions-and-templates`, push lên `origin/dev` và tự động tạo PR #17 & #18.\n"
    "  - **Tiến trình tự động:** Auto-Healing Runner (task-4558) đang chạy ngầm, chờ 15 phút Kubernetes rollout pod mới trên `scm-stg10.concung.vn`, sau đó tự động kích hoạt test lại màn 315 và tiếp tục quét tuần tự từ màn 316 đến 396.\n"
)

if scm_detail_marker in content:
    content = content.replace(scm_detail_marker, scm_new_details)

# Update Section 3: Daily Commit Sync 17:00 Run
sync_marker = "- **Job 1 (Cron 17:00 Hằng Ngày - task-3348):**"
sync_update = (
    "- **Lần chạy Daily Incremental Commit Sync 17:00:** 2026-10-19 17:02:14 (Hoàn tất thành công)\n"
    "  - Đã fetch & pull 6 repo tham chiếu (`cci-hrm-web`, `cci-mbm-web`, `cci-timekeeping-web`, `cci-supplier-web`, `cci-common-web`, `cci-hrm-api`).\n"
    "  - Trích xuất 150 commit gần nhất, phân tích và gom nhóm 8 danh mục kỹ thuật.\n"
    "  - Đối chiếu với 3 portal đang thao tác (DC, Place, SCM): Tất cả các giải pháp kỹ thuật trọng yếu (Redis DataProtection Keyring, NormalizeUrl, EPPlus DataValidation) đều đã được áp dụng đầy đủ và đồng bộ, không phát sinh giải pháp mới cần dập khuôn thêm.\n\n"
)

content = content.replace(sync_marker, sync_update + sync_marker)

# Ensure single UTF-8 BOM
content = content.lstrip('\ufeff')
with open(progress_path, "w", encoding="utf-8-sig", newline='\n') as f:
    f.write(content)

print("WORKSPACE_PROGRESS.md successfully updated with UTF-8 BOM.")
