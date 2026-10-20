import os

FILE = r"E:\Work\Place_Migrate\WORKSPACE_PROGRESS.md"

with open(FILE, "r", encoding="utf-8-sig") as f:
    content = f.read()

# Update table row for SCM
old_scm_row = """| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🛠️ **ĐÃ FIX MIGRATE-BUG MÀN 315 (XUẤT EXCEL) — ĐANG CHỜ K8S ROLLOUT PR #17**<br/>• Màn 210–314: Parity Pass 100% (55+ màn pass, các màn fail đều origin-same)<br/>• Màn 315 (`promotions`): Fix lỗi thiếu return ActionResult xuất Excel (PR #17 & #18)<br/>• Auto-healing runner (task-4558) đang chờ rollout để re-verify & quét tiếp màn 316–396. | • Test Report: ID **117** / file `test-report-latest.json` | • Màn 315 xuất Excel 0-byte: Đã fix dứt điểm trên 7 controllers.<br/>• Đã tạo PR #17 & #18, chờ K8s rollout 15 phút. | Tự động re-test màn 315 và quét cạn các màn từ 316 đến 396. |"""

new_scm_row = """| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🏃 **MÀN 315 ĐÃ NGHIỆM THU ĐẠT 100% PARITY — BACKGROUND SWEEP ĐANG QUÉT MÀN 316+**<br/>• Màn 315 (`promotions`): Đã verify đạt 100% Parity (14P / 1S / 0F), xuất file Excel $\\ge 1\\text{ KB}$ thành công.<br/>• Tiến trình sweep ngầm tuần tự đang quét từ màn 316 (`promotion-schemes`) đến 396.<br/>• **Đã dập khuôn HRM/MBM:** Redis DataProtection + UrlNormalize + EPPlus DataValidation order (PR #15 & #16) + Fix Excel Return (PR #17 & #18). | • Test Report: ID **117** / file `test-report-latest.json` | • Màn 315 xuất Excel 0-byte: Đã fix dứt điểm và nghiệm thu đạt 100% Parity.<br/>• Tiến trình quét ngầm tuần tự (task-4943) đang chạy từ màn 316. | Tiếp tục tự động quét các màn còn lại đến 396 theo Rule 9 & 11. |"""

content = content.replace(old_scm_row, new_scm_row)

# Update Section 2.3 for SCM
old_sec_scm = """  - **Tiến trình tự động:** Auto-Healing Runner (task-4558) đang chạy ngầm, chờ 15 phút Kubernetes rollout pod mới trên `scm-stg10.concung.vn`, sau đó tự động kích hoạt test lại màn 315 và tiếp tục quét tuần tự từ màn 316 đến 396."""

new_sec_scm = """  - **Kết quả nghiệm thu thực tế sau rollout STG10 (19/10/2026 20:26):**
    + Chạy lại kiểm thử màn 315 (`promotions`): **14 Passed, 1 Skipped, 0 Failed** (Thời gian: 2.6 phút).
    + So sánh với STG4 Baseline: **14 Passed, 1 Skipped, 0 Failed** (Thời gian: 2.8 phút).
    + Đối chiếu Parity: **Đạt 100% Parity**, ca test `TC-SCM-227-014` (Export Excel download) đã tải file Excel thành công kích thước $\\ge 1\\text{ KB}$.
    + Bug xuất Excel 0-byte đã được giải quyết dứt điểm hoàn toàn!
  - **Tiến trình quét tiếp theo:** Auto-Healing Runner (`task-4943`) đang tiếp tục quét fail-fast từ màn 316 (`promotion-schemes`) đến màn 396."""

content = content.replace(old_sec_scm, new_sec_scm)

# Write back with UTF-8 BOM
with open(FILE, "w", encoding="utf-8-sig") as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md with SCM screen 315 verification and active sweep.")
