import sys

progress_content = """# BẢNG THEO DÕI TIẾN ĐỘ TOÀN DIỆN WORKSPACE (MIGRATION & QA PARITY)

> **Cập nhật mới nhất:** 2026-10-19 14:05  
> **Mục đích:** File duy nhất lưu giữ toàn bộ tiến độ, kết quả test, báo cáo portal, đối chiếu parity và tồn đọng của mọi project trong workspace. Cập nhật trực tiếp đè lên file này mỗi khi có thay đổi mới.

---

## 1. BẢNG TỔNG HỢP TIẾN ĐỘ CÁC PORTAL (STATUS MATRIX)

| Portal / Repo | Quy mô Suite | Trạng thái Test & Parity | Report mới nhất trên Dashboard | Tồn đọng / Phân loại lỗi | Hành động tiếp theo |
|---|:---:|:---:|---|---|---|
| [cci-dc-web](file:///e:/Work/Place_Migrate/cci-dc-web) | **757 tests**<br/>(119 màn) | ✅ **Parity 100%**<br/>(NET4: 373P/383S/1F<br/>NET10: 375P/381S/1F) | • NET10: ID **622**<br/>• NET4: ID **624** | `origin-same`: Chỉ fail duy nhất `TC-DC-11-013` (màn `buffer-orders` do staging trống data). PGSQL vướng SSO redirect.<br/>• **Đã dập khuôn HRM/MBM:** Redis DataProtection keyring + UrlNormalize (PR #15 & #16). | Chờ CI/CD auto-merge và deploy pod mới. Sẵn sàng đóng gói khi cần. |
| [cci-store-location-web](file:///e:/Work/Place_Migrate/cci-store-location-web) | **559 tests**<br/>(45 spec / 16 màn) | ✅ **FULL TEST NET10 MSSQL — PARITY VƯỢT NET4**<br/>• NET4: 487P / 57S / 15F (ID 634)<br/>• NET10: **507P / 39S / 13F** (ID 652) | • NET4: ID **634**<br/>• NET10: ID **652** | • `backend-api-broken` đã giải quyết dứt điểm 100% (xoá sạch 131 ca fail chênh lệch do API 404).<br/>• Đạt 100% Parity so với NET4 gốc.<br/>• **Đã dập khuôn HRM/MBM:** Redis DataProtection keyring + UrlNormalize (PR #15 & #16). | Đã hoàn thành mục tiêu migration cho Place Web. Sẵn sàng nghiệm thu. |
| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🏃 **MÀN 210 FIX PASS — BACKGROUND SWEEP ĐANG CHẠY MÀN 250+**<br/>• Màn 210–248: Parity Pass 100%<br/>• Đang chạy sweep ngầm tuần tự (task-2608)<br/>• **Đã dập khuôn HRM/MBM:** Redis DataProtection + UrlNormalize + EPPlus DataValidation order (PR #15 & #16). | • Test Report: ID **117** / file `test-report-latest.json` | Họ màn `pay-forms` (`PayFormSakuras`, `PayForms`) đã fix dứt điểm lỗi Razor 500.<br/>• Đang chạy sweep ngầm tuần tự theo Rule 11. | Tiếp tục tự động quét các màn còn lại, phát hiện migrate-bug sẽ tự fix hoặc báo cáo. |
| [cci-oneteam-web](file:///e:/Work/Place_Migrate/cci-oneteam-web) | Đang dựng | ⏸️ **TẠM PENDING** | Chưa chạy | Team migrate chưa hoàn thiện khung, chưa được phép sửa code. | Chờ bàn giao từ team migrate. |
| [cci-hrm-api](file:///e:/Work/Place_Migrate/cci-hrm-api) | Tham chiếu | 🔍 **ĐÃ CLONE VỀ WORKSPACE** | N/A | Repo API chỉ dùng làm context tham chiếu kỹ thuật và dập khuôn theo Rule 1. | Giữ nguyên branch `dev` sạch. |

---

## 2. CHI TIẾT TỪNG DỰ ÁN & LỊCH SỬ THỰC THI

### 2.1. `cci-dc-web`
- **Địa chỉ:**
  - NET4 Baseline: `https://dc-stg4.concung.vn/`
  - NET10 MSSQL: `https://dc-stg10.concung.vn/`
  - NET10 PostgreSQL: `https://dc-stg.concung.vn/`
- **Kết quả Full Test 757 test cases (18/10/2026):**
  - **NET10 MSSQL (ID 622):** 375 Passed, 381 Skipped, 1 Failed. Thời gian: 4.3 phút.
  - **NET4 MSSQL (ID 624):** 373 Passed, 383 Skipped, 1 Failed. Thời gian: 6.9 phút.
  - **Đối chiếu Parity:** Đạt **100% Parity**. Ca fail duy nhất trên cả 2 bản là `TC-DC-11-013` (màn `buffer-orders` do dữ liệu staging rỗng) → Phân loại: `origin-same` / `oracle-broken`.
  - **Môi trường PostgreSQL:** Vướng Keycloak redirect về `dc-stg10.concung.vn` thay vì giữ nguyên `dc-stg.concung.vn` → Phân loại: `sso-broken` / `env-broken`.
- **Dập khuôn kỹ thuật từ HRM/MBM (19/10/2026):**
  - Thêm package `Microsoft.AspNetCore.DataProtection.StackExchangeRedis` (10.0.0), `Microsoft.Extensions.Caching.StackExchangeRedis` (10.0.0), nâng `StackExchange.Redis` lên `2.7.33`.
  - Cấu hình Redis session & DataProtection keyring lưu trữ tại `DataProtection-Keys:DC` kèm fallback `AddDistributedMemoryCache()`.
  - Bổ sung `UriExtensions.cs` và chuẩn hoá endpoint gọi API (`NormalizeUrl()`) tránh lỗi double slash (//).
  - Tách nhánh: `fix/replicate-redis-dataprotection-and-url-normalize` → merge `--no-ff` vào `dev` → gắn tag → push `origin/dev`.
  - **Pull Request Bitbucket Đã Tạo:**
    - PR #15 (`dev -> staging10`): https://bitbucket.org/concung/cci-dc-web/pull-requests/15
    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-dc-web/pull-requests/16

---

### 2.2. `cci-store-location-web`
- **Địa chỉ:**
  - NET4 Baseline: `https://place-stg4.concung.vn/`
  - NET10 MSSQL: `https://place-stg10.concung.vn/`
  - NET10 PostgreSQL: `https://place-stg.concung.vn/` (Port 443 đóng)
- **Kết quả Test đối chiếu Parity (18/10/2026):**
  - **NET4 MSSQL Baseline (ID 634):** 487 Passed, 57 Skipped, 15 Failed (tổng 559 tests, thời gian: 9.5 phút).
  - **NET10 MSSQL Live Test (ID 652):** **507 Passed, 39 Skipped, 13 Failed** (Thời gian: 5.7 phút).
  - **Đối chiếu Parity:** NET10 pass nhiều hơn NET4 (507 vs 487). 131 ca fail chênh lệch do `ApisUrl` 404 đã giải quyết dứt điểm.
- **Dập khuôn kỹ thuật từ HRM/MBM (19/10/2026):**
  - Thêm package `Microsoft.AspNetCore.DataProtection.StackExchangeRedis` (10.0.0) và `Microsoft.Extensions.Caching.StackExchangeRedis` (10.0.0).
  - Cấu hình Redis session & DataProtection keyring lưu trữ tại `DataProtection-Keys:Place` kèm fallback `AddDistributedMemoryCache()`.
  - Bổ sung `UrlNormalizeExtensions` và chuẩn hoá endpoint gọi API (`NormalizeUrl()`).
  - Tách nhánh: `fix/replicate-redis-dataprotection-and-url-normalize` → merge `--no-ff` vào `dev` → gắn tag → push `origin/dev`.
  - **Pull Request Bitbucket Đã Tạo:**
    - PR #15 (`dev -> staging10`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/15
    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/16

---

### 2.3. `cci-scm-web`
- **Địa chỉ:**
  - STG10: `https://scm-stg10.concung.vn/`
  - STG4: `https://scm-stg4.concung.vn/`
- **Tiến độ Fail-Fast Parity Sweep:**
  - Đã quét màn 185 đến 248+:
    - **Hơn 40 Màn đạt 100% Parity Pass.**
    - Các màn fail đều fail đồng nhất cả 2 bản (origin-same / oracle-broken).
    - Màn 210 (`pay-form-sakuras`) đã fix dứt điểm lỗi relative partial view path (PR #13 & #14 đã auto-merge).
- **Dập khuôn kỹ thuật từ HRM/MBM (19/10/2026):**
  - Thêm package `Microsoft.AspNetCore.DataProtection.StackExchangeRedis` (10.0.0) và `Microsoft.Extensions.Caching.StackExchangeRedis` (10.0.0).
  - Cấu hình Redis session & DataProtection keyring lưu trữ tại `DataProtection-Keys:SCM` với fallback an toàn `AddDistributedMemoryCache()`.
  - Tích hợp hàm mở rộng `NormalizeUrl()` vào `Helpers/UriExtension.cs` và áp dụng vào `APIClient.cs`.
  - Khắc phục thứ tự gán thuộc tính EPPlus 5+ DataValidation (`ShowErrorMessage`, `AllowBlank`, `Error` gán trước `Formula.ExcelFormula`) trong `FileHelper.cs` và `BonusPointAccountProductsController.cs` tránh ngoại lệ `DataValidationStaleException`.
  - Tách nhánh: `fix/replicate-redis-dataprotection-url-normalize-and-epplus-validation` → merge `--no-ff` vào `dev` → gắn tag → push `origin/dev`.
  - **Pull Request Bitbucket Đã Tạo:**
    - PR #15 (`dev -> staging10`): https://bitbucket.org/concung/cci-scm-web/pull-requests/15
    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-scm-web/pull-requests/16

---

### 2.4. `cci-oneteam-web`
- **Trạng thái:** TẠM DỪNG (Pending).
- Không sửa bất kỳ file mã nguồn nào tại repo này cho đến khi nhận được thông báo chính thức từ team migrate.

---

### 2.5. `cci-hrm-api`
- **Trạng thái:** Đã clone về thư mục workspace `e:\\Work\\Place_Migrate\\cci-hrm-api`.
- Nhánh hiện tại: `dev`.
- Tuân thủ Rule 1: Chỉ phục vụ đối chiếu context API và lấy quy chuẩn dập khuôn, không sửa code.

---

## 3. HỆ THỐNG CRON & WORKFLOW TỰ ĐỘNG HOÁ TOÀN CỤC (GLOBAL AUTOMATION)

- **Job 1 (Cron 17:00 Hằng Ngày):** Tự động kéo commit `dev` mới nhất của `cci-hrm-web` & `cci-mbm-web`, trích xuất commit fix bug/build, phân tích gom nhóm và đối chiếu để dập khuôn giải pháp chuẩn mực cho 3 portal web (`dc`, `store-location`, `scm`). Mã task: `task-2731` (`IsDaemon=true`).
- **Job 2 (Continuous Auto-Healing Sweep):** Chạy ngầm test đối chiếu Parity (Fail-Fast `--max-failures=1`). Khi phát hiện `migrate-bug`, tự động dừng, phân loại, tách nhánh `fix/*`, sửa code, quét chéo, merge `dev`, tạo PR Bitbucket, chờ 15 phút K8s rollout và re-test verify. Đang chạy tại `task-2608`.
- **Quy chuẩn dập khuôn từ HRM/MBM:**
  1. **Redis & DataProtection Keyring:** Bổ sung package `Microsoft.AspNetCore.DataProtection.StackExchangeRedis` 10.0.0, lưu key ring và session vào Redis, có `try/catch` fallback về MemoryCache an toàn. (Đã áp dụng cho cả DC, Store Location, SCM).
  2. **URL Normalization:** Hàm `NormalizeUrl()` ngăn ngừa double slashes (`//`) khi ghép nối BaseURL và Endpoint trong `APIClient.cs`. (Đã áp dụng cho cả DC, Store Location, SCM).
  3. **EPPlus DataValidation:** Gán các thuộc tính Validation trước `Formula.ExcelFormula` tránh `DataValidationStaleException`. (Đã áp dụng cho SCM).

---

## 4. NGUYÊN TẮC CẬP NHẬT TIẾN ĐỘ (LƯU Ý DÀNH CHO AGENT)
1. **Một file duy nhất:** Không tạo file progress theo ngày (tránh sinh rác). Luôn cập nhật trực tiếp vào file này.
2. **Cập nhật ngay sau mỗi hành động:**
   - Chạy test xong → ghi nhận số case Pass/Fail/Skip, Report ID, đối chiếu parity.
   - Fix bug xong → ghi nhận commit, phân loại lỗi (`migrate-bug` / `oracle-broken` / `env-broken` / `test-bug`).
   - Tạo PR xong → cập nhật link PR và trạng thái merge.
"""

path = 'WORKSPACE_PROGRESS.md'
with open(path, 'wb') as f:
    f.write(b'\\xef\\xbb\\xbf' + progress_content.encode('utf-8'))
print('WORKSPACE_PROGRESS.md updated with UTF-8 BOM')
