# -*- coding: utf-8 -*-
import sys

# 1. Update AGENTS.md
agents_path = "e:/Work/Place_Migrate/AGENTS.md"
with open(agents_path, "r", encoding="utf-8") as f:
    agents_text = f.read()

rule_9_target = "- **9. Test Fail-Fast & Dừng Ngay Khi Gặp Lỗi Migrate (Áp dụng cho TẤT CẢ các Portal):** Khi chạy test E2E (đặc biệt các bộ test lớn như SCM với ~388 màn), BẮT BUỘC chạy ở chế độ Fail-Fast (`--max-failures=1`). Khi phát hiện bất kỳ lỗi nào hoặc `migrate-bug` (NET4 đạt mà NET10 lỗi, lỗi 500, crash, sai lệch dữ liệu): **PHẢI DỪNG TEST NGAY LẬP TỨC VÀ BÁO CÁO (REPORT) LIỀN**, tuyệt đối không chạy tiếp đến hết suite làm mất thời gian chờ đợi. Sau khi báo cáo và fix xong mới tiếp tục chạy các màn tiếp theo."

rules_additional = """- **9. Test Fail-Fast & Dừng Ngay Khi Gặp Lỗi Migrate (Áp dụng cho TẤT CẢ các Portal):** Khi chạy test E2E (đặc biệt các bộ test lớn như SCM với ~388 màn), BẮT BUỘC chạy ở chế độ Fail-Fast (`--max-failures=1`). Khi phát hiện bất kỳ lỗi nào hoặc `migrate-bug` (NET4 đạt mà NET10 lỗi, lỗi 500, crash, sai lệch dữ liệu): **PHẢI DỪNG TEST NGAY LẬP TỨC VÀ BÁO CÁO (REPORT) LIỀN**, tuyệt đối không chạy tiếp đến hết suite làm mất thời gian chờ đợi. Sau khi báo cáo và fix xong mới tiếp tục chạy các màn tiếp theo.
- **10. Ưu tiên tuyệt đối Subagents & Background Tasks:** Mọi tác vụ tốn thời gian (chạy test suite lớn, fail-fast sweep, clone repo, quét commit, phân tích chuyên sâu) BẮT BUỘC chạy dưới dạng Subagents hoặc Background Tasks. Tuyệt đối không treo tiến trình ở foreground làm block khung chat, giữ khung chat luôn sẵn sàng để nhận lệnh mới từ người dùng bất cứ lúc nào.
- **11. Workflow Tự Động Khắc Phục Lỗi Toàn Diện (Continuous Auto-Healing Migration Loop):** Khi test suite chạy ngầm phát hiện `migrate-bug`:
  - Dừng test ngay lập tức theo Rule 9, trích xuất log lỗi, đối chiếu `01_origin` vs `02_target` để phân loại nguyên nhân gốc.
  - Nếu lỗi thuộc phạm vi code web migration có thể tự fix được:
    1. Tách nhánh `fix/<mã-fix>` từ `dev` mới nhất.
    2. Sửa code trong `02_target/` (bảo toàn UTF-8 BOM, không watermark AI).
    3. Quét lỗi đồng bộ chéo 2 repo còn lại theo Rule 4 (`Cross-Portal Bug Sweep`).
    4. Test verify đạt trên nhánh fix.
    5. Merge `--no-ff` vào `dev`, gắn tag `fix/<mã-fix>`, push lên `origin/dev`.
    6. Tự động tạo cặp Pull Request (`dev → staging10` và `dev → staging`) bằng `tools/bitbucket_pr.py`.
    7. Tự động chuyển runner sang trạng thái chờ 15 phút để CI/CD auto-merge và Kubernetes rollout pod mới.
    8. Chạy lại test case đó trên `staging10` để nghiệm thu đạt.
    9. Tiếp tục chạy các màn tiếp theo cho đến khi toàn bộ portal đạt 100% Parity.
  - Nếu là lỗi hạ tầng/SSO/DB/backend API: Không sửa bậy code web để che lỗi, ghi nhận hồ sơ rõ ràng.
- **12. Đồng Bộ & Dập Khuôn Thông Minh Hằng Ngày Lúc 17:00 (Daily Commit Sync & Smart Replication):** Đã thiết lập Cron Job định kỳ 17:00 hằng ngày tự động kéo nhánh `dev` mới nhất của `cci-hrm-web` và `cci-mbm-web`, trích xuất các commit fix bug/build mới, phân tích gom nhóm và đối chiếu với `cci-dc-web`, `cci-store-location-web`, `cci-scm-web`. Chỉ dập khuôn các giải pháp kỹ thuật đã kiểm chứng (như Redis DataProtection, Excel export sạch không BOM, ApiHelper 204 guard), tránh dập khuôn mù quáng gây xung đột môi trường."""

if rule_9_target in agents_text:
    agents_text = agents_text.replace(rule_9_target, rules_additional)
    with open(agents_path, "w", encoding="utf-8") as f:
        f.write(agents_text)
    print("AGENTS.md updated successfully with Rules 10, 11, 12")
else:
    print("AGENTS.md target NOT found!")

# 2. Update GIT_RULES.md
git_path = "e:/Work/Place_Migrate/GIT_RULES.md"
with open(git_path, "r", encoding="utf-8") as f:
    git_text = f.read()

git_additional = """

## 8. Ưu tiên tuyệt đối Subagents & Background Tasks

- Mọi tác vụ tốn thời gian (chạy suite test E2E dài, fail-fast sweep, clone repo, phân tích git commit, chờ deploy) BẮT BUỘC khởi chạy dưới dạng Background Task / Subagent.
- Giữ khung chat chính luôn trống để người dùng có thể prompt, tra cứu hoặc chỉ đạo bất kỳ lúc nào mà không bị gián đoạn.

## 9. Chu trình Tự Động Hoá Khắc Phục Lỗi Migration (Auto-Healing Loop)

1. Test ngầm tuần tự các portal (Fail-Fast `--max-failures=1`).
2. Phát hiện `migrate-bug` $\\rightarrow$ dừng ngay, phân tích nguyên nhân gốc giữa `01_origin` và `02_target`.
3. Nếu tự fix được: Tách nhánh `fix/*` $\\rightarrow$ Sửa `02_target/` $\\rightarrow$ Quét chéo 3 portal $\\rightarrow$ Verify $\\rightarrow$ Merge `dev` $\\rightarrow$ Tự động tạo PR Bitbucket $\\rightarrow$ Chờ 15 phút K8s rollout $\\rightarrow$ Test lại nghiệm thu $\\rightarrow$ Tiếp tục quét các màn kế tiếp cho đến khi 100% Parity.

## 10. Job Đồng Bộ & Dập Khuôn Kỹ Thuật Định Kỳ 17:00 Hằng Ngày

- Hằng ngày vào lúc 17:00, cron job tự động fetch/pull nhánh `dev` của `cci-hrm-web` và `cci-mbm-web`.
- Lập danh sách commit fix bug/migration mới, gom nhóm phân loại, đối chiếu chéo xem 3 project (`dc`, `store-location`, `scm`) có bị vấn đề tương tự không.
- Tiến hành dập khuôn các giải pháp chuẩn mực (Redis DataProtection keyring, xử lý file Excel nhị phân không BOM, ApiHelper 204 guard, v.v.), commit và mở PR theo đúng quy trình."""

git_text = git_text.rstrip() + git_additional + "\n"
with open(git_path, "w", encoding="utf-8") as f:
    f.write(git_text)
print("GIT_RULES.md updated successfully with Sections 8, 9, 10")
