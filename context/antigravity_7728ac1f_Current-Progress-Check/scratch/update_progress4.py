# -*- coding: utf-8 -*-
path = "e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md"
with open(path, "r", encoding="utf-8-sig") as f:
    text = f.read()

# Update time
text = text.replace("2026-10-19 13:00", "2026-10-19 13:20")

# Update table SCM
old_scm_row = "| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🏃 **POD STG10 UP THÀNH CÔNG — ĐANG CHẠY FAIL-FAST SWEEP TỪ MÀN 210**<br/>• Probe `/PayFormSakuras`: HTTP 200 OK (hết lỗi 500).<br/>• Background task đang chạy test đối chiếu Parity. | • Test Report: ID **117** / file `test-report-latest.json` | `migrate-bug` màn 210 đã fix & deploy xong.<br/>• Đang chạy sweep tuần tự các màn còn lại theo nguyên tắc Fail-Fast (`--max-failures=1`). | Nếu phát hiện bất kỳ migrate-bug nào khác sẽ dừng ngay lập tức và báo cáo. |"
new_scm_row = "| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🏃 **MÀN 210 VERIFY PASS — ĐANG TỰ ĐỘNG SWEEP TIẾP TỤC**<br/>• Màn 210–215: Parity Pass 100%<br/>• Màn 216, 219, 221, 222: origin-same<br/>• Background task đang quét tiếp tục màn 223+ | • Test Report: ID **117** / file `test-report-latest.json` | Họ màn `pay-forms` (`PayFormSakuras`, `PayForms`) đã fix dứt điểm lỗi Razor 500.<br/>• Đang chạy sweep ngầm tuần tự theo Rule 11. | Tiếp tục tự động quét các màn còn lại, phát hiện migrate-bug sẽ tự fix hoặc báo cáo. |"

text = text.replace(old_scm_row, new_scm_row)

# Update detail SCM
old_scm_detail = """    - **Nguyên nhân gốc và giải pháp khắc phục Bug Màn 210:**"""
new_scm_detail = """    - **Kết quả verify màn 210 sau khi deploy PR #13 / #14:**
      - Probe HTTP: `https://scm-stg10.concung.vn/PayFormSakuras` trả về **HTTP 200 OK** (hết hoàn toàn lỗi 500).
      - Test Parity: Màn 210 (`pay-form-sakuras`), 211 (`pay-form-sakuras-create`), 212 (`pay-form-sakuras-edit`), 213 (`pay-forms-create`), 214 (`pay-forms-edit`), 215 (`pay-forms-edit-cc-app`) đều đã **vượt qua kiểm tra Parity thành công**!
    - **Nguyên nhân gốc và giải pháp khắc phục Bug Màn 210:**"""

text = text.replace(old_scm_detail, new_scm_detail)

# Add Cron & Workflow section to Section 3
old_sec_3 = """## 3. NGUYÊN TẮC CẬP NHẬT TIẾN ĐỘ (LƯU Ý DÀNH CHO AGENT)"""
new_sec_3 = """## 3. HỆ THỐNG CRON & WORKFLOW TỰ ĐỘNG HOÁ TOÀN CỤC (GLOBAL AUTOMATION)

- **Job 1 (Cron 17:00 Hằng Ngày):** Tự động kéo commit `dev` mới nhất của `cci-hrm-web` & `cci-mbm-web`, trích xuất commit fix bug/build, phân tích gom nhóm và đối chiếu để dập khuôn giải pháp chuẩn mực cho 3 portal web (`dc`, `store-location`, `scm`). Mã task: `task-2731`.
- **Job 2 (Continuous Auto-Healing Sweep):** Chạy ngầm test đối chiếu Parity (Fail-Fast `--max-failures=1`). Khi phát hiện `migrate-bug`, tự động dừng, phân loại, tách nhánh `fix/*`, sửa code, quét chéo, merge `dev`, tạo PR Bitbucket, chờ 15 phút K8s rollout và re-test verify.
- **Quy chuẩn dập khuôn từ HRM:**
  1. **Redis & DataProtection Keyring:** Bổ sung package `Microsoft.AspNetCore.DataProtection.StackExchangeRedis` 10.0.0, lưu key ring và session vào Redis, có `try/catch` fallback về MemoryCache an toàn.
  2. **Excel Export:** Chuẩn hoá MIME type `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, loại bỏ UTF-8 BOM khỏi file zip/binary, bổ sung header `FileName` và `Access-Control-Expose-Headers`.
  3. **ApiHelper 204 Guard:** Kiểm tra `content == null || content.Headers.ContentLength == 0` trả về `default(T)` tránh lỗi deserialization chuỗi rỗng.

---

## 4. NGUYÊN TẮC CẬP NHẬT TIẾN ĐỘ (LƯU Ý DÀNH CHO AGENT)"""

text = text.replace(old_sec_3, new_sec_3)

with open(path, "w", encoding="utf-8-sig") as f:
    f.write(text)

print("WORKSPACE_PROGRESS.md updated cleanly with UTF-8 BOM")
