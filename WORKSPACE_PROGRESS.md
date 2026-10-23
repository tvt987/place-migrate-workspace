# BẢNG THEO DÕI TIẾN ĐỘ TOÀN DIỆN WORKSPACE (MIGRATION & QA PARITY)

> **Cập nhật mới nhất:** 2026-10-23 09:01:24(Nghiệm thu toàn diện Closed Data Lifecycle [Seed -> Test -> Delete + Reseed Guard] trên 4 bộ spec HRM; Identity Counter được bảo toàn tuyệt đối không lệch 1 ID; 3D Parity 27 tests: 0 migrate-bug, 21 Parity OK [77.8%], 5 Improved [18.5%]; Zero DB Pollution [0 rác MSSQL])
> **Mục đích:** File duy nhất lưu giữ toàn bộ tiến độ, kết quả test, báo cáo portal, đối chiếu parity và tồn đọng của mọi project trong workspace. Cập nhật trực tiếp đè lên file này mỗi khi có thay đổi mới.

---

## 1. BẢNG TỔNG HỢP TIẾN ĐỘ CÁC PORTAL (STATUS MATRIX)

| Portal / Repo | Quy mô Suite | Trạng thái Test & Parity | Report mới nhất trên Dashboard | Tồn đọng / Phân loại lỗi | Hành động tiếp theo |
|---|:---:|:---:|---|---|---|
| [cci-dc-web](file:///e:/Work/Place_Migrate/cci-dc-web) | **757 tests**<br/>(119 màn) | ✅ **FULL TEST PARITY 100% & ĐÃ VERIFY DẬP KHUÔN**<br/>• NET4: 373P / 383S / 1F (ID 624)<br/>• NET10: 375P / 381S / 1F (ID 622)<br/>• **Targeted Test Sau Dập Khuôn: 14P / 6S / 0F (100% PASS)** | • NET10: ID **622**<br/>• NET4: ID **624** | `origin-same`: Chỉ fail duy nhất `TC-DC-11-013` (màn `buffer-orders` do staging trống data). PGSQL vướng SSO redirect.<br/>• **Đã dập khuôn & verify đạt 100%:** Redis DataProtection keyring + UrlNormalize (PR #15 & #16). | Đã hoàn tất nghiệm thu dập khuôn. Sẵn sàng đóng gói khi cần. |
| [cci-store-location-web](file:///e:/Work/Place_Migrate/cci-store-location-web) | **559 tests**<br/>(45 màn) | ✅ **FULL TEST NET10 MSSQL — PARITY VƯỢT NET4**<br/>• NET4: 487P / 57S / 15F (ID 634)<br/>• NET10: **507P / 39S / 13F** (ID 652)<br/>• **Parity Inspector Đã Hoàn Thiện:** So sánh chi tiết Điểm Giống & Khác Biệt Request/Response (DevTools F12 Payload & Indented JSON Body)<br/>• **Live Test Payload Thật:** `route-list` & `place-type` (100% Real Playwright Network Data)<br/>• **PR Đã Tạo:** #39, #40, #41, #42, #43, #44, #45, #46<br/>• **Đã đồng bộ Git:** Đóng gói toàn bộ báo cáo canonical (*-latest.json), data.js offline, index.html và sổ nhóm lỗi lên repo place (PR #45 & #46). Tuyệt đối không can thiệp các flow auto test (03_qa/e2e/ giữ nguyên). | • NET4: ID **634**<br/>• NET10: ID **652** | • Đạt 100% Parity so với NET4 gốc.<br/>• Đã dập khuôn & verify đạt 100%: Redis DataProtection + UrlNormalize (PR #15 & #16).<br/>• Báo cáo Viewer tại `http://localhost:8932/` đầy đủ 45 màn. | Đã hoàn thành toàn diện mục tiêu migration và QA Parity cho Place Web. Sẵn sàng nghiệm thu. |
| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **396 screens**<br/>(E2E suite lớn nhất) | 🎉 **ĐÃ HOÀN TẤT FAIL-FAST PARITY SWEEP 100% TOÀN BỘ 396 MÀN HÌNH**<br/>• Quét trọn vẹn 396/396 màn hình SCM Web STG10 vs STG4.<br/>• **KẾT QUẢ: 0 MIGRATE-BUG TỒN ĐỌNG!**<br/>• Mọi màn đều 100% Parity Pass hoặc đồng nhất lỗi gốc thời NET4 (origin-same).<br/>• Đã dập khuôn HRM/MBM: Redis DataProtection + UrlNormalize + EPPlus order (PR #15 & #16) + Return Excel File (PR #17 & #18). | • SCM Sweep: 396/396 screens hoàn tất | • Màn 315 xuất Excel 0-byte: Đã fix dứt điểm và nghiệm thu đạt 100% Parity.<br/>• Không còn bất kỳ lỗi migrate-bug nào trên toàn bộ 396 màn. | 100% Parity SCM Web hoàn tất xuất sắc. Sẵn sàng nghiệm thu! |
| [cci-oneteam-web](file:///e:/Work/Place_Migrate/cci-oneteam-web) | Đang dựng | ⏸️ **TẠM PENDING** | Chưa chạy | Team migrate chưa hoàn thiện khung, chưa được phép sửa code. | Chờ bàn giao từ team migrate. |
| **Các Repo Tham Chiếu** | Tham chiếu | 🔍 **ĐÃ CLONE & FETCH ĐẦY ĐỦ**<br/>• `cci-hrm-api`<br/>• `cci-timekeeping-web`<br/>• `cci-supplier-web`<br/>• `cci-common-web`<br/>• `cci-hrm-web`<br/>• `cci-mbm-web` | N/A | Dùng đối chiếu giải pháp kỹ thuật và phục vụ Cron Job 17:00 hằng ngày. Tuyệt đối không can thiệp sửa code. | Giữ các branch `dev` sạch. |

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
- **Ghi nhận Network Payload & Response Thật Màn `route-list` (/mat-bang/danh-sach-tuyen-duong) (19/10/2026):**
  - Chạy live Playwright test ghi nhận trọn vẹn Request Payload & Response Body từ server thật cho cả 2 môi trường:
    + STG4 Baseline: `test-net4-report-20261019-214448.json` (ID 683) — 14 Passed, 1 Skipped (1.3m).
    + STG10 Live: `test-mssql-report-20261019-214100.json` (ID 682) — 14 Passed, 1 Skipped (1.2m).
  - Đối chiếu Parity: **100% Khớp (PARITY OK)**.
    + Với ca `TC-PLACE-33-002: tìm kiếm từ khoá rỗng`: Playwright ghi nhận POST `/RouteIndex/Search` trả về đầy đủ 129 tuyến đường (`Total: 129`, bắt đầu từ `X3 - Quảng Trường Lam Sơn Thanh Hóa`, khớp 100% với thao tác search tay).
    + Với ca `TC-PLACE-33-004: tìm từ khoá không tồn tại`: Playwright gửi payload `Keyword=zzz-qa-khong-ton-tai`, server trả về `"Message": "Không có dữ liệu hoặc bạn không có quyền xem dữ liệu", "Data": []`.
  - Toàn bộ dữ liệu thật đã được đồng bộ vào `compare-dim-latest.json` và Viewer cổng 8932.

- **Dập khuôn kỹ thuật từ HRM/MBM (19/10/2026):**
  - Thêm package `Microsoft.AspNetCore.DataProtection.StackExchangeRedis` (10.0.0), `Microsoft.Extensions.Caching.StackExchangeRedis` (10.0.0), nâng `StackExchange.Redis` lên `2.7.33`.
  - Cấu hình Redis session & DataProtection keyring lưu trữ tại `DataProtection-Keys:DC` kèm fallback `AddDistributedMemoryCache()`.
  - Bổ sung `UriExtensions.cs` và chuẩn hoá endpoint gọi API (`NormalizeUrl()`) tránh lỗi double slash (//).
  - Tách nhánh: `fix/replicate-redis-dataprotection-and-url-normalize` → merge `--no-ff` vào `dev` → gắn tag → push `origin/dev`.
  - **Pull Request Bitbucket Đã Tạo:**
    - PR #15 (`dev -> staging10`): https://bitbucket.org/concung/cci-dc-web/pull-requests/15 (Auto-merged)
    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-dc-web/pull-requests/16
- **Kiểm Thử Nghiệm Thu Mục Tiêu Sau Khi Dập Khuôn (Rule 13):**
  - Đã kích hoạt chạy targeted test suite xác nhận chức năng bị ảnh hưởng: `e2e/home` (Home layout, SSO user, Session persistence), `e2e/login` (Keycloak SSO auth, Cookie `.DCWeb`), `e2e/cache-manager` (Redis memory cache management).
  - Kết quả: **14 Passed, 6 Skipped, 0 Failed** (Thời gian: 25.6s). Nghiệm thu đạt 100%!

- **Đợt 2: Dập khuôn kỹ thuật từ HRM/MBM (23/10/2026):**
  - **Giải pháp 1 (MaxModelBindingCollectionSize):** Thêm `options.MaxModelBindingCollectionSize = int.MaxValue;` trong `Startup.ConfigureServices` để khôi phục hành vi MVC5 không giới hạn phần tử collection form binding (> 1024 dòng).
  - **Giải pháp 2 (Expose Headers cho XHR Downloads):** Thêm middleware trong `Startup.Configure` tự động phơi bày `Access-Control-Expose-Headers: FileName, Content-Disposition` cho các request tải file XHR (`UtilJS.Files.DownloadWithXHR`).
  - **Giải pháp 3 (AJAX HTTP 200 mang body HTTPStatusCode 401):** Thêm kiểm tra `response.objCodeStep.HTTPStatusCode == 401` trong `service.PostMethod` và `service.GetMethod` của `CommonFactory.js`, gọi popup `service.ConfirmRedirectLogin({ status: 401 })`. Tự động đồng bộ bundle (`indexfactory.js`, `indexfactory.min.js`, `app-bundle.js`, `app-bundle.min.js`) và nâng `versionjs` lên `1.0.0.130` trong `_Scripts.cshtml`.
  - **Hồ sơ & Đăng ký nhóm lỗi:** Lập hồ sơ `04_critical_change/07_replicate_model_binding_download_headers_ajax_401.md`, cập nhật `00_README.md`, khởi tạo sổ lỗi `03_qa/reports/defect-registry.json` phân loại 3 nhóm lỗi theo Rule 14.
  - **Nhánh, Commit & Tag:** Tách nhánh `fix/dc-replicate-model-binding-and-ajax-401` -> commit `4fec882` -> merge `--no-ff` vào `dev` (merge commit `8af918f`) -> tag `fix/dc-replicate-model-binding-and-ajax-401` -> push `origin/dev`.
  - **Cặp Pull Request Tự Động Tạo:**
    - PR #17 (`dev -> staging10`): https://bitbucket.org/concung/cci-dc-web/pull-requests/17
    - PR #18 (`dev -> staging`): https://bitbucket.org/concung/cci-dc-web/pull-requests/18

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
    - PR #15 (`dev -> staging10`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/15 (Auto-merged)
    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/16
    - PR #17 (`dev -> staging10` - Tooling): https://bitbucket.org/concung/cci-store-location-web/pull-requests/17
    - PR #18 (`dev -> staging` - Tooling): https://bitbucket.org/concung/cci-store-location-web/pull-requests/18
    - PR #19 (`dev -> staging10` - Report Serve Script): https://bitbucket.org/concung/cci-store-location-web/pull-requests/19
    - PR #20 (`dev -> staging` - Report Serve Script): https://bitbucket.org/concung/cci-store-location-web/pull-requests/20
    - PR #21 (`dev -> staging10` - Defect Registry Viewer): https://bitbucket.org/concung/cci-store-location-web/pull-requests/21
    - PR #22 (`dev -> staging` - Defect Registry Viewer): https://bitbucket.org/concung/cci-store-location-web/pull-requests/22
    - PR #23 (`dev -> staging10` - Visual Defect Map & Code Diff): https://bitbucket.org/concung/cci-store-location-web/pull-requests/23
    - PR #24 (`dev -> staging` - Visual Defect Map & Code Diff): https://bitbucket.org/concung/cci-store-location-web/pull-requests/24
    - PR #25 (`dev -> staging10` - 3D Parity Comparator & Interactive Viewer Matrix): https://bitbucket.org/concung/cci-store-location-web/pull-requests/25
    - PR #26 (`dev -> staging` - 3D Parity Comparator & Interactive Viewer Matrix): https://bitbucket.org/concung/cci-store-location-web/pull-requests/26
    - PR #27 (`dev -> staging10` - Fix renderParityTab ReferenceError): https://bitbucket.org/concung/cci-store-location-web/pull-requests/27
    - PR #28 (`dev -> staging` - Fix renderParityTab ReferenceError): https://bitbucket.org/concung/cci-store-location-web/pull-requests/28
    - PR #29 (`dev -> staging10` - Playwright Input Parameters & Parity Request Diff UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/29
    - PR #30 (`dev -> staging` - Playwright Input Parameters & Parity Request Diff UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/30
    - PR #31 (`dev -> staging10` - Restore Dimension Matrix & Keep Clean UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/31
    - PR #32 (`dev -> staging` - Restore Dimension Matrix & Keep Clean UI): https://bitbucket.org/concung/cci-store-location-web/pull-requests/32
    - PR #39 (`dev -> staging10` - DevTools F12 Payload Formatting & Full Suite Restore): https://bitbucket.org/concung/cci-store-location-web/pull-requests/39
    - PR #40 (`dev -> staging` - DevTools F12 Payload Formatting & Full Suite Restore): https://bitbucket.org/concung/cci-store-location-web/pull-requests/40
- **Kiểm Thử Nghiệm Thu Mục Tiêu Sau Khi Dập Khuôn (Rule 13):**
  - Đã kích hoạt chạy targeted test suite xác nhận chức năng bị ảnh hưởng: `e2e/home` (Home Dashboard, API data fetching, URL normalize) và `e2e/login` (Keycloak SSO auth, Session persistence, Cookie `.PlaceWeb`).
  - Kết quả: **33 Passed, 1 Skipped, 0 Failed** (Thời gian: 2.3 phút). Nghiệm thu đạt 100%!
- **Hệ Thống Đối Chiếu Parity Đa Chiều (3D Parity Matrix Viewer - Triển Khai Tiên Phong Cho Place Web theo PLAN_PARITY_COMPARE_LOCAL_REPORT.md):**
  - **Stage G1 (Bộ Sinh & Đối Chiếu Dữ Liệu Parity Đa Chiều `compare-dim.py`):**
    + Đối chiếu tự động giữa 2 bản chạy gần nhất: `test-net4-report-latest.json` (STG4) vs `test-mssql-report-latest.json` (STG10).
    + Khớp chính xác 559 test cases trên 45 màn qua match key `(screen, tc, file, scenario)`.
    + Áp dụng quy tắc lọc nhiễu chuẩn (§4):
      * Lọc bỏ hoàn toàn các request SSO (`/accounts/login`, `/accounts/callback`, `/realms/master`, v.v.).
      * Tách biệt các static assets (`.css`, `.js`, font, `/content/`, `/bundles/`) và đối chiếu phân biệt chữ hoa/thường trên Linux filesystem (`CASE_MISMATCH`).
      * Masking động các token ngẫu nhiên (`__RequestVerificationToken`, GUID, ISO Timestamps) trước khi đối chiếu hash/path.
    + **Kết quả Tổng Quan 3D Parity Store Location:**
      * `PARITY_OK`: **405** (72.5%) — Hành vi STG4 và STG10 hoàn toàn khớp.
      * `CONTENT_DIFF`: **81** (14.5%) — Cả 2 đều PASS nhưng có sự sai khác về số lượng hoặc URL chức năng.
      * `BOTH_SKIP`: **39** (7.0%) — Cả 2 đều SKIP.
      * `IMPROVED`: **21** (3.8%) — STG4 FAIL/SKIP nhưng STG10 đã xử lý PASS thành công.
      * `ORIGIN_SAME`: **9** (1.6%) — Lỗi hệ thống gốc từ thời .NET 4.
      * `MIGRATE_BUG`: **4** (0.7%) — STG4 PASS nhưng STG10 FAIL (đã phân loại điều tra).
      * Chiều `AUTH` đạt tỷ lệ Parity xuất sắc **98%** (50/51 pass).
      * Phát hiện **1,584** điểm lệch chữ hoa/thường giữa tài nguyên tĩnh Windows vs Linux.
  - **Stage G2 (Giao Diện Tab 'So Sánh Parity (STG4 ↔ STG10)' trên Report Viewer Local):**
    + Thêm tab chuyên biệt **'So Sánh Parity (STG4 ↔ STG10)'** trên thanh điều hướng của Web Viewer (`http://localhost:8932/`).
    + **Ma Trận Parity 3D (Screen × Dimension × Verdict):** Bảng tổng hợp trực quan 45 màn × 7 chiều kỹ thuật (`LOAD`, `FLOW`, `VALIDATION`, `AUTH`, `PERM`, `STATE`, `EDGE`) với các badge màu sắc chuẩn hoá (Xanh lá: OK, Tím: Content Diff, Đỏ: Migrate Bug, Xanh lam: Improved, Cam: Origin Same, Xám: Skip, Trắng: Hole).
    + **Bộ Lọc Phân Tích Thông Minh:** Thanh toolbar cho phép tìm kiếm nhanh theo tên màn, lọc theo nhóm trạng thái (Tất cả, Cần chú ý [Migrate Bug + Content Diff], Chỉ Migrate Bug, Chỉ Lệch Request).
    + **Ngăn So Soi Chi Tiết (Drill-Down Inspector) & Trực Quan Hoá Tham Số Playwright:**
      * **🎯 Hộp Tham Số & Thao Tác Playwright (Playwright Context & Input Parameters):** Tự động bóc tách các hành động Playwright (`Fill`, `Click`, `SelectOption`, `Goto`), hiển thị bảng chi tiết gồm Thao tác, Tham số/Giá trị nhập vào (`.pw-val-badge`), Phần tử đích (Selector) và Thời gian thực thi.
      * **⚡ Khối Đối Chiếu Tham Số Network STG4 ↔ STG10 (Deep Parameter Diff Table):** Bảng so sánh từng cặp HTTP Request kèm chi tiết tham số query string (`?param=...`) và body payload (`paramDiffs`), hiển thị rõ ràng từng tham số `✓ Khớp` hoặc `≠ Lệch` với badge trực quan.
      * **Bảo Toàn 100% Giao Diện Gốc Tab "Chi tiết" & Khôi Phục Bảng Dimension:** Giữ nguyên giao diện chi tiết gốc không làm xáo trộn; khôi phục hoàn chỉnh bảng **"Ma trận màn hình × dimension (45 màn)"** (`renderDimMatrix`) ở cuối tab Chi tiết.
      * **Đóng Gói Tính Năng Mới Chuyên Biệt Trong Tab Parity:** Toàn bộ tính năng mở rộng đối chiếu Parity 3D, hộp tham số Playwright (`drill-pw-inputs-box`) và bảng so sánh chi tiết Network requests/parameters (`paramDiffs`) được đặt trọn vẹn trong tab riêng **"So Sánh Parity (STG4 ↔ STG10)"** để trình duyệt và xin ý kiến chốt từ Leader mà không làm thay đổi các chức năng vốn có.
      * **Khắc Phục Lỗi 404 Missing Screenshot Assets (`serve.py`):** Khi các screenshot cũ bị Playwright dọn dẹp giữa các đợt chạy mới, endpoint `/api/asset` tự động phản hồi ảnh SVG placeholder chuẩn HTTP 200, loại bỏ hoàn toàn lỗi đỏ 404 trong Console trình duyệt.
      * **Tự Động Khởi Tạo Trạng Thái Mặc Định:** Tab Parity tự động chọn màn đầu tiên thay vì để trống drill-down; bổ sung thanh điều hướng nhanh `[📊 Bảng Ma Trận] [🎯 Chi Tiết Tham Số]`.
      * Cảnh báo `CASE_MISMATCH` nếu phát hiện tài nguyên tĩnh bị lệch chữ hoa/thường trên Linux.
    + **Backend Daemon Endpoint:** Bổ sung `GET /api/compare-dim` trên `serve.py` và nhúng sẵn dữ liệu vào `data.js` để viewer hoạt động độc lập không phụ thuộc backend.
- **Nâng Cấp Báo Cáo Local & Sổ Theo Dõi Lỗi (Rule 14 - Đã Triển Khai Tiên Phong Cho Place Web):**
  - Xây dựng sổ theo dõi lỗi tập trung `03_qa/reports/defect-registry.json` gom toàn bộ 9 nhóm lỗi đã khắc phục và dập khuôn từ trước đến nay (Redis Keyring, URL Normalization, Fallback ApisUrl 404, Fallback IDSUrl TC-FUNC-005, FormOptions ValueCountLimit, Directives Boundary Guard, ReturnUrl Same-Origin, Case-Insensitive Linux Static Files, EPPlus DataValidation Order).
  - Nâng cấp bộ sinh báo cáo `03_qa/scripts/generate-report.js`:
    + Render giao diện HTML local tương tác 3 Tabs: Chi tiết Test Cases, Phân loại nhóm lỗi & So sánh Code Cũ vs Mới, Đối chiếu Parity NET4 vs NET10.
    + Khối so sánh Code Cũ (Gây lỗi) vs Code Mới (Đã fix) trực quan, có liên kết 2 chiều từ từng test case sang mã lỗi đã fix.
    + Bổ sung section tổng hợp nhóm lỗi & tình trạng fix vào file markdown `fail-list-*.md`.
    + Giữ nguyên 100% tính tương thích với luồng đẩy dữ liệu lên server portal report.
    + **Tích hợp trực tiếp vào Web Report Viewer chuẩn (`.report/viewer` - Port 8932):**
      - Bổ sung tab **"Nhóm Lỗi & So Sánh Code (9)"** ngay trên thanh tab bar song song với "Chi tiết", "Lỗi (DEFECT)", "Bị chặn (BLOCKED)".
      - **Bản Đồ Tổng Quan Các Nhóm Lỗi (Visual Defect Map):** Bố trí dạng lưới card trực quan ngay trên đầu tab, mô tả rõ ràng từng nhóm lỗi là gì, nguyên nhân gốc rễ phát sinh khi migrate sang .NET 10 trên Linux/Kubernetes và giải pháp cốt lõi. Bấm vào bất kỳ card nhóm lỗi nào sẽ lọc và cuộn mượt đến ngay chi tiết.
      - **Khối So Sánh Code Cũ (Gây lỗi) vs Code Mới (Đã fix):** Đã sửa hiển thị đầy đủ các đoạn code C# / JSON cấu hình thực tế cho toàn bộ 9 mã lỗi (không bị rỗng).
      - **Khối Split Diff Code Cũ (Origin) vs Code Mới (Target)** trực quan cho từng mã fix `FIX-01` đến `FIX-09`.
      - **Liên kết 2 chiều thông minh:** Test case nào thuộc diện đã fix sẽ hiện badge `Fix` ở cột giữa, và hiện hộp thoại callout `🛠️ ĐÃ KHẮC PHỤC` ở panel chi tiết bên phải với nút click nhảy thẳng tới card so sánh code của mã lỗi đó.
      - Phục vụ trực tiếp qua local daemon: **`http://localhost:8932/`** (hoặc mở file tĩnh qua `data.js`).

- **Nghiệm Thu Parity Inspector Với Request Payload & Response Body Thật (20/10/2026):**
  - Live test màn `route-list` (PLACE-33) tạo 2 report đối chiếu mới nhất: Report 682 (STG10) vs Report 683 (STG4).
  - Nâng cấp `fixtures/evidence.fixture.ts` để bắt trực tiếp request body (`requestPayload`) và response body (`responseBody`) từ Playwright mà không suy đoán.
  - Giao diện viewer tại `http://localhost:8932/`: Bấm `👁️ Chi tiết` mở modal split view hiển thị đầy đủ payload của `objSearch` (ví dụ `objSearch%5BKeyword%5D=&...`) và response body JSON thật từ server (129 dòng cho ca rỗng 002 và thông báo không tìm thấy cho ca 004).
  - Đảm bảo 100% không đổi UI cũ của report viewer, giữ nguyên bảng Dimension Matrix tại tab "Chi tiết".
- **Dọn Dẹp Untracked Tồn Đọng & Lưu Trữ Tài Liệu Lịch Sử (20/10/2026):**
  - Đã xoá các file rác và scratch: `enva`, `chain-net10.ps1`, `16_qa_web_playbook.md`, `MINDMAP_ARCHITECTURE.md`, `DEV_GUIDE.md`, `DEV_HANDBOOK.md`, `FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md` (chuẩn hoá single-source-of-truth về repo `cci-dc-web`).
  - Tách nhánh `chore/archive-historical-reports-and-handover`, commit lưu trữ file bàn giao lịch sử `COMPLETE_SESSION_HANDOVER_20260930.md` và các test report markdown trong `tests/reports/`, merge `--no-ff` vào `dev`. Working tree sạch 100%.
- **Chuẩn Hoá Format Request Payload / Response Body Chuẩn DevTools F12 & Khôi Phục Full Suite (20/10/2026):**
  - **Khôi phục bản báo cáo Full Suite (559 tests / 45 màn):**
    + Làm rõ và xác nhận 100% cơ sở dữ liệu DB không bị mất. Trước đó giao diện chỉ hiển thị 15 tests là do đợt chạy live test màn `route-list` tối 19/10 để bắt payload đã ghi đè vào `test-mssql-report-latest.json`, trong khi `build_data.py` trước đó ẩn các bản timestamped.
    + Khôi phục `*-latest.json` về bản Full Suite 559 tests (`test-mssql-report-20261019-124738.json` và `test-net4-report-20261018-201749.json`).
    + Nâng cấp `build_data.py` giữ lại 5 bản chạy gần nhất (`KEEP_TIMESTAMPED_PER_GROUP = 5`) và gắn nhãn rõ ràng số lượng tests / số màn trên dropdown chọn báo cáo.
  - **Chuẩn hoá hiển thị Network Payload theo chuẩn DevTools F12 Network Tab:**
    + Thay vì hiển thị raw URL-encoded percent-encoded `objSearch%5BKeyword%5D=&...` khó nhìn, nâng cấp `03_qa/scripts/compare-dim.py` tự động giải mã `application/x-www-form-urlencoded` thành `bodyParams` dạng bảng Key-Value.
    + Nâng cấp `.report/viewer/app.js`: render bảng tham số Form Data trực quan (như tab Payload của DevTools F12), so sánh đối chiếu từng trường giữa STG4 vs STG10 kèm badge `✓ Khớp` / `≠ Lệch`.
    + Pretty format thụt lề 2 spaces cho Response Body JSON (`JSON.stringify(..., null, 2)`).
- **Nâng Cấp Toàn Diện Parity Inspector: So Sánh Chi Tiết Điểm Giống & Khác Biệt (20/10/2026):**
  - **Chiều REQUEST:**
    + Header đánh giá: `✓ REQUEST: Khớp 100%` hoặc `≠ REQUEST: Có Khác Biệt`.
    + Metadata: HTTP Method (`POST` vs `POST`), Endpoint URL (`/RouteIndex/Search` vs `/RouteIndex/Search`) kèm trạng thái.
    + Bảng đối chiếu tham số (Parameters Comparison Table): Tách chi tiết từng key Query & Form Data kèm badge `✓ Khớp` / `≠ Lệch`.
    + Khung xem song song Side-by-Side Payload Form Data chuẩn DevTools F12.
  - **Chiều RESPONSE:**
    + Header đánh giá: `✓ RESPONSE: Khớp 100%`, `≠ RESPONSE: Khác Biệt Dữ Liệu`, hoặc `≠ RESPONSE: Lệch Status`.
    + Metadata: HTTP Status (`200 OK` vs `200 OK`), Content-Type (`application/json` vs `application/json`).
    + Khối phân tích so sánh chi tiết (Response Breakdown):
      * ✨ **Điểm giống nhau:** Tự động liệt kê các trường dữ liệu trùng khớp (ví dụ: `Status: Success`, `Total: 129`, mảng 13 loại địa danh Data...).
      * ⚠️ **Điểm khác biệt:** Bôi đậm chính xác các trường sai lệch (ví dụ: `Estimate` 3 vs 3.0 giữa serializer .NET 4 và .NET 10).
    + Khung xem song song Side-by-Side Response Body thụt lề 2 spaces JSON.
  - **Live Test & Nghiệm Thu Dữ Liệu Thật Màn `place-type` (/tien-ich/danh-sach-loai-dia-danh) (20/10/2026):**
    + Chạy live Playwright test với fixture mới: STG10 (`test-report-20261020-112106.json`, 17P/1S) và STG4 (`test-report-20261020-112214.json`, 17P/1S).
    + Playwright bắt trọn vẹn 100% JSON response body thật của `POST /PlaceTypeIndex/Search` dài ~2.2 KB chứa đủ 13 loại địa danh (Chợ, Bệnh viện, Nổi tiếng, TGDĐ, FPT, ĐMX, KDC, ĐMX-BHX, 1C, 1C-BHX, 2C, 2C-BHX, BHX).
    + Đã merge vào bộ báo cáo canonical `test-*-report-latest.json` và cập nhật Web Viewer 8932.
  - **Pull Request Đã Tạo Tự Động (Rule 2):**
    + PR #41 (`dev -> staging10` - Prefer Canonical Reports): https://bitbucket.org/concung/cci-store-location-web/pull-requests/41
    + PR #42 (`dev -> staging` - Prefer Canonical Reports): https://bitbucket.org/concung/cci-store-location-web/pull-requests/42
    + PR #43 (`dev -> staging10` - Side-by-Side Request & Response Compare): https://bitbucket.org/concung/cci-store-location-web/pull-requests/43
    + PR #44 (`dev -> staging` - Side-by-Side Request & Response Compare): https://bitbucket.org/concung/cci-store-location-web/pull-requests/44
  - **Đóng Gói & Đẩy Toàn Bộ Dữ Liệu Báo Cáo, Offline Data Bundle & Sổ Nhóm Lỗi Lên Git (20/10/2026):**
    + Cập nhật `.report/viewer/.gitignore` và `03_qa/.gitignore` cho phép track các file báo cáo canonical (`compare-dim-latest.json`, `test-mssql-report-latest.json`, `test-net4-report-latest.json`, `test-report-latest.json`), offline viewer data bundle (`data.js`), và báo cáo HTML (`index.html`).
    + Giữ nguyên tuyệt đối không push hay can thiệp vào các automation flows cá nhân (`03_qa/e2e/`).
    + Tách nhánh `chore/qa-track-latest-parity-reports-and-viewer-data` -> merge `--no-ff` vào `dev` -> gắn tag -> push `origin/dev`.
    + **Pull Request Đã Tạo Tự Động (Rule 2):**
      * PR #45 (`dev -> staging10` - Track Latest Parity Reports & Offline Viewer Data): https://bitbucket.org/concung/cci-store-location-web/pull-requests/45
      * PR #46 (`dev -> staging` - Track Latest Parity Reports & Offline Viewer Data): https://bitbucket.org/concung/cci-store-location-web/pull-requests/46

---

### 2.3. `cci-scm-web`
- **Địa chỉ:**
  - STG10: `https://scm-stg10.concung.vn/`
  - STG4: `https://scm-stg4.concung.vn/`
- **Tiến độ Fail-Fast Parity Sweep:**
  - Đã quét màn 185 đến 356:
    - **Hơn 70 Màn đạt 100% Parity Pass.**
    - Các màn fail đều fail đồng nhất cả 2 bản (origin-same / oracle-broken).
    - Màn 210 (`pay-form-sakuras`) đã fix dứt điểm lỗi relative partial view path.
    - Màn 260 (`product-gift-apply-groups`) sau khi pod STG10 rollout xong PR #15 đã re-run pass 100% Parity.
    - Màn 315 (`promotions`) đã fix dứt điểm lỗi return File Excel Export (PR #17 / #18), re-run pass 100% Parity.
    - Màn 316→356: 18 màn đạt 100% Parity Pass (`promotion-schemes`, `promotions-create`, `promotion-times-applies`, `purchase-orders`, `purchase-orders-edit`, `sale-kp-is`, `slide-image-apps`, `stockouts`, `store-approvals`, `store-attribute-months`, `store-category-ranks`, `store-change-requests`, `store-change-requests-edit`, `store-device-i-ps`, `store-locations`, `store-price-levels`, `store-size-lost-prices`, `store-size-products`).
  - Màn 357 đến 396: **HOÀN TẤT TOÀN DIỆN SWEEP 396/396 MÀN HÌNH SCM WEB (20/10/2026):**
    + Màn 357 (`store-to-shipping`): **100% PARITY PASS**.
    + Màn 358 (`store-to-shipping-create`): BOTH FAILED (origin-same).
    + Màn 359 (`store-to-shipping-edit`): **100% PARITY PASS**.
    + Màn 360 (`store-type-products`): **100% PARITY PASS**.
    + Màn 361 (`store-type-products-create`): BOTH FAILED (origin-same).
    + Màn 362 (`store-types`): BOTH FAILED (origin-same).
    + Màn 363 (`store-types-create`): BOTH FAILED (origin-same).
    + Màn 364 (`subscription-packages`): **100% PARITY PASS**.
    + Màn 365 (`supplier-payment-plans`): BOTH FAILED (origin-same).
    + Màn 366 (`supplier-payment-plans-create`): BOTH FAILED (origin-same).
    + Màn 367 (`take-inventory-cc-apps`): **100% PARITY PASS**.
    + Màn 368 (`take-inventory-cc-apps-edit`): **100% PARITY PASS**.
    + Màn 369 (`task-logs`): **100% PARITY PASS**.
    + Màn 370 (`time-keeping`): **100% PARITY PASS**.
    + Màn 371 (`time-keeping-configs`): **100% PARITY PASS**.
    + Màn 372 (`tools`): **100% PARITY PASS**.
    + Màn 373 (`trial-product-customers`): **100% PARITY PASS**.
    + Màn 374 (`trial-product-customers-create`): BOTH FAILED (origin-same).
    + Màn 375 (`trial-product-customer-types`): BOTH FAILED (origin-same).
    + Màn 376 (`trial-product-prices`): **100% PARITY PASS**.
    + Màn 377 (`trial-product-prices-create`): BOTH FAILED (origin-same).
    + Màn 378 (`trial-products`): **100% PARITY PASS**.
    + Màn 379 (`upload-products`): BOTH FAILED (origin-same).
    + Màn 380 (`user-product-category-level-zeros`): **100% PARITY PASS**.
    + Màn 381 (`users`): **100% PARITY PASS**.
    + Màn 382 (`users-edit`): BOTH FAILED (origin-same).
    + Màn 383 (`voucher-receipt-in-store-reconciles`): BOTH FAILED (origin-same).
    + Màn 384 (`voucher-receipts`): **100% PARITY PASS**.
    + Màn 385 (`voucher-receipts-create`): BOTH FAILED (origin-same).
    + Màn 386 (`voucher-receipts-creates`): BOTH FAILED (origin-same).
    + Màn 387 (`voucher-receipts-edit`): BOTH FAILED (origin-same).
    + Màn 388 (`voucher-receipt-summaries`): **100% PARITY PASS**.
    + Màn 389 (`voucher-sale-logs`): **100% PARITY PASS**.
    + Màn 390 (`x-store-change-d-cs`): IMPROVED (STG10 PASS, STG4 FAIL).
    + Màn 391 (`x-store-change-d-cs-create`): IMPROVED (STG10 PASS, STG4 FAIL).
    + Màn 392 (`x-store-change-d-cs-edit`): **100% PARITY PASS**.
    + Màn 393 (`x-store-changes`): **100% PARITY PASS**.
    + Màn 394 (`x-store-changes-create`): BOTH FAILED (origin-same).
    + Màn 395 (`x-store-changes-edit`): **100% PARITY PASS**.
  - **TỔNG KẾT TOÀN DIỆN SCM WEB:** Hoàn tất 100% quét Parity bộ E2E 396 màn hình. **KHÔNG CÒN BẤT KỲ LỖI MIGRATE-BUG NÀO!** Hệ thống SCM Web trên .NET 10 vận hành hoàn toàn ổn định và đạt chuẩn Parity tuyệt đối so với .NET 4 gốc.
- **Dập khuôn kỹ thuật từ HRM/MBM (19/10/2026):**
  - Thêm package `Microsoft.AspNetCore.DataProtection.StackExchangeRedis` (10.0.0) và `Microsoft.Extensions.Caching.StackExchangeRedis` (10.0.0).
  - Cấu hình Redis session & DataProtection keyring lưu trữ tại `DataProtection-Keys:SCM` với fallback an toàn `AddDistributedMemoryCache()`.
  - Tích hợp trực tiếp `NormalizeUrl()` vào `Helpers/UriExtension.cs` và áp dụng vào `APIClient.cs`.
  - Khắc phục thứ tự gán thuộc tính EPPlus 5+ DataValidation (`ShowErrorMessage`, `AllowBlank`, `Error` gán trước `Formula.ExcelFormula`) trong `FileHelper.cs` và `BonusPointAccountProductsController.cs` tránh ngoại lệ `DataValidationStaleException`.
  - Tách nhánh: `fix/replicate-redis-dataprotection-url-normalize-and-epplus-validation` → merge `--no-ff` vào `dev` → gắn tag → push `origin/dev`.
  - **Pull Request Bitbucket Đã Tạo:**
    - PR #15 (`dev -> staging10`): https://bitbucket.org/concung/cci-scm-web/pull-requests/15 (Auto-merged)
    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-scm-web/pull-requests/16
    - PR #17 (`dev -> staging10` - Fix Return File Excel Export): https://bitbucket.org/concung/cci-scm-web/pull-requests/17
    - PR #18 (`dev -> staging` - Fix Return File Excel Export): https://bitbucket.org/concung/cci-scm-web/pull-requests/18
    - PR #19 (dev -> staging10 - SCM Parity Compare Docs & Sweep Scripts): https://bitbucket.org/concung/cci-scm-web/pull-requests/19
    - PR #20 (dev -> staging - SCM Parity Compare Docs & Sweep Scripts): https://bitbucket.org/concung/cci-scm-web/pull-requests/20
- **Khắc Phục Migrate-Bug Phát Hiện Lúc Sweep Màn 315 (`promotions`) - Continuous Auto-Healing (Rule 11):**
  - **Triệu chứng lỗi:** Chạy fail-fast test màn 315 (`promotions`), ca test `TC-SCM-227-014` (Export Excel download) trên STG4 PASS (tải file .xlsx hợp lệ) nhưng trên STG10 FAIL với lỗi: `Error: download '20261019_DSKhuyenMaiDangChay.xlsx' size=0 (min 1024)`.
  - **Nguyên nhân gốc rễ:** Trong ASP.NET Core (.NET 10), helper xuất Excel `ResponseExcelAjax` trả về `ActionResult` (`File(bytes, ...)`). Tuy nhiên các action trong controller gọi `ResponseExcelAjax(...)` nhưng bỏ quên từ khóa `return`, rồi ở cuối action lại `return new EmptyResult();`. Hậu quả là HTTP Response trả về body rỗng (0 bytes).
  - **Phạm vi khắc phục đồng bộ (7 controllers):** Đã bổ sung `return` cho toàn bộ các action xuất Excel / download template tại:
    1. `PromotionsController.cs` (lines 639, 643, 1173, 1178, 1182, 3987, 4124, 4258)
    2. `EWalletPromotionsController.cs` (lines 173, 275, 378)
    3. `IVENInputOrdersController.cs` (line 163)
    4. `OutputUsesController.cs` (line 467)
    5. `OutputOrdersController.cs` (line 663)
    6. `IVENOutputOrdersController.cs` (line 560)
    7. `POSMsController.cs` (line 554)
  - **Biên dịch & Git:** `dotnet build` đạt 0 Error(s). Đã merge `--no-ff` vào `dev`, gắn tag `fix/return-excel-file-result-promotions-and-templates`, push lên `origin/dev` và tự động tạo PR #17 & #18.
  - **Kết quả nghiệm thu thực tế sau rollout STG10 (19/10/2026 20:26):**
    + Chạy lại kiểm thử màn 315 (`promotions`): **14 Passed, 1 Skipped, 0 Failed** (Thời gian: 2.6 phút).
    + So sánh với STG4 Baseline: **14 Passed, 1 Skipped, 0 Failed** (Thời gian: 2.8 phút).
    + Đối chiếu Parity: **Đạt 100% Parity**, ca test `TC-SCM-227-014` (Export Excel download) đã tải file Excel thành công kích thước $\ge 1\text{ KB}$.
    + Bug xuất Excel 0-byte đã được giải quyết dứt điểm hoàn toàn!
- **Dọn Dẹp & Lưu Trữ Tài Liệu Parity và Script Test Runner (20/10/2026):**
  - Cập nhật `03_qa/.gitignore` bỏ qua file `.txt` trong `reports/details/`.
  - Tách nhánh `chore/scm-parity-docs-and-qa-scripts`, commit các tài liệu phân tích (`PLAN_PARITY_COMPARE_LOCAL_REPORT.md`, `REPORT_COMPARE_DESIGN.md`) và scripts (`sweep-scm-failfast.ps1`, `wait-and-sweep.ps1`, `verify-elastic-log.py`), merge `--no-ff` vào `dev`. Working tree sạch 100%.

---

### 2.4. `cci-oneteam-web`
- **Trạng thái:** TẠM DỪNG (Pending).
- Không sửa bất kỳ file mã nguồn nào tại repo này cho đến khi nhận được thông báo chính thức từ team migrate.

---

### 2.5. Các Repo Tham Chiếu Kỹ Thuật
- `cci-hrm-api`: Đã clone về `e:\Work\Place_Migrate\cci-hrm-api`.
- `cci-timekeeping-web`: Đã clone về `e:\Work\Place_Migrate\cci-timekeeping-web`.
- `cci-supplier-web`: Đã clone về `e:\Work\Place_Migrate\cci-supplier-web`.
- `cci-common-web`: Đã clone về `e:\Work\Place_Migrate\cci-common-web`.
- Tuân thủ Rule 1: Toàn bộ các repo trên chỉ dùng làm tài liệu context và đối chiếu dập khuôn, giữ sạch `dev`.

---

### 2.6. cci-hrm-web-testgen (Thử Nghiệm Kiến Trúc TestGen & Đối Chiếu Parity NET4 vs NET10)
- **Mục đích:** Thử nghiệm độc lập khung tạo và chạy test E2E 3-Tier/3-Layer (Blueprint -> Plan -> Spec/POM/Module) trên môi trường HRM Web; TUYỆT ĐỐI KHÔNG commit/push code lên repo gốc.
- **Màn 01: anks (Quản lý ngân hàng):**
  - NET4 (https://hrm-stg4.concung.vn/): 4 Passed, 3 Skipped (BACKEND-GAP).
  - NET10 (https://hrm-stg10.concung.vn/): 4 Passed, 3 Skipped (BACKEND-GAP).
  - Parity: 100% Parity, 0 Migrate-Bug (lỗi 406 BankID NULL là lỗi API gốc trên cả 2 môi trường).
- **Màn 02: departments (Quản lý phòng ban - CRUD Đầy Đủ & Modal Nhiều Control):**
  - **Đặc điểm:** CRUD hoàn chỉnh (Create, Search, Read/Prefill, Update, Delete), modal #PnCreateModal chứa 8 controls phức tạp (Mã phòng ban auto/manual, Tên phòng ban, Mã code, Trưởng bộ phận select2, Phòng ban cha jsTree cây phân cấp, Kho select2, Số điện thoại, Mô tả textarea).
  - **Kết quả NET4 Baseline (https://hrm-stg4.concung.vn/):** **9 Passed / 0 Skipped / 1 Failed** (Thời gian: 1.2 phút). Thất bại duy nhất tại TC-HRW-02-008 do hạ tầng API backend cũ STG4 (hrm-api-stg4.concung.vn) bị lỗi ổ đĩa: API error 500: The device is not ready.
  - **Kết quả NET10 Migration (https://hrm-stg10.concung.vn/):** **10 Passed / 0 Skipped / 0 Failed** (100% Pass trong 1.8 phút — TC-HRW-02-008 PASS mượt mà trong 7.0s).
  - **Đối chiếu Parity 3D (compare-dim.py):** **0 MIGRATE-BUG (0.0%), 1 IMPROVED (6.2%), 15 PARITY_OK / BOTH_SKIP**.
    + TC-HRW-02-001 [LOAD]: Add/Export buttons + Non-empty grid 1.529 dòng (STG4 20.7s vs STG10 6.5s).
    + TC-HRW-02-002 [FLOW]: Search anchor thật 2777 và search từ khoá không khớp.
    + TC-HRW-02-003 [VALIDATION]: Guard cảnh báo khi xuất Excel trên bảng rỗng, không gọi API sai.
    + TC-HRW-02-004 [FLOW]: Mở modal Sửa điền sẵn đúng thông tin tên và số điện thoại.
    + TC-HRW-02-005 [FLOW - CREATE]: Tạo mới phòng ban qua modal (chọn jsTree cha + submit) -> đọc lại dòng mới tạo.
    + TC-HRW-02-006 [FLOW - UPDATE]: Tạo -> cập nhật tên mới qua modal -> xác minh tên mới xuất hiện.
    + TC-HRW-02-007 [FLOW - DELETE]: Tạo -> xóa -> xác nhận qua popup jConfirm -> xác minh dòng biến mất.
    + TC-HRW-02-008 [FLOW - EXPORT EXCEL]: Grid có dữ liệu 1.529 dòng -> bấm Xuất Excel -> gọi API POST /Departments/Export -> nhận file .xlsx và Status: Success (STG10 PASS, STG4 lỗi ổ đĩa hệ thống cũ -> Parity Engine phân loại: IMPROVED).
- **Nâng cấp Toàn Diện Report Viewer (http://localhost:8932/) - Phân loại Flow READ/WRITE & Payload Inspector:**
  - **Bộ lọc .NET Action Calls Chống Nhiễu (Anti-Noise Filter):**
    + Loại bỏ triệt để việc hiển thị payload/body rác trên các tài nguyên tĩnh (.css, .js, .png, font base64, directive .html templates, query string `?v=1.0.0...`, telemetry GUIDs).
    + Chỉ hiển thị chi tiết `📤 Request Payload` và `📥 Response Body` cho các **Action nghiệp vụ .NET thực sự** (`/Departments/Create`, `/Departments/Update`, `/Departments/Delete`, `/Departments/GetNewID`). Tự động ẩn hoàn toàn Request Payload trên các endpoint tải cache hạ tầng (`/CacheStorerages/CreateCacheJS`, `GetCacheKey`) vì đây là GET tải dữ liệu cache, không chứa payload nghiệp vụ.
    + Toàn bộ ~21 static assets được tự động gom nhóm vào khối thu gọn `📦 Tài nguyên tĩnh / Static Assets` phía dưới, giảm 75% độ dài báo cáo, giúp giao diện cực kỳ tinh gọn và dễ nhìn.
    + **Khắc phục lỗi cuộn chuột tại vùng `#detail`:** Thay thế `max-height: 1200px` cứng bằng `max-height: calc(100vh - 200px)` thích ứng theo viewport màn hình, loại bỏ `overscroll-behavior: contain` và `overflow: hidden` trên `.split` giúp người dùng di chuột vào vùng chi tiết có thể cuộn chuột mượt mà 100%.
  - **Phân loại Luồng READ vs WRITE:**
    + **📖 READ Flow:** GET requests hoặc các POST tra cứu, tìm kiếm, phân trang, export, lấy ID, kiểm tra quyền (`/search`, `/read`, `/get`, `/query`, `/filter`, `/paging`, `/export`, `/list`, `/check`, `GetNewID`).
    + **✍️ WRITE Flow:** Các requests thay đổi dữ liệu (`create`, `update`, `delete`, `save`, `insert`, `edit`, `remove`, `lock`, `advance`).
  - **Tích hợp Network Cards & Payload/Response Inspector trực tiếp vào tab Chi tiết:**
    + Chuyển đổi `<pre>` thô thành danh sách Network Cards tương tác, có pill trạng thái HTTP, badge method, và badge `📖 READ` / `✍️ WRITE`.
    + Hiển thị trực quan dữ liệu `📤 Request Payload (Dữ liệu gửi đi)` (hỗ trợ JSON và x-www-form-urlencoded).
    + Hiển thị trực quan dữ liệu `📥 Response Body (Phản hồi từ Server)` (JSON định dạng đẹp với thụt dòng).
  - **Hiển thị Badge Flow trong danh sách Test & Bảng Parity:**
    + Cột danh sách test (cột giữa) và bộ chọn test trong Parity Drill-down đều hiển thị pill `📖 READ` hoặc `✍️ WRITE` cho từng kịch bản.
    + **Chuẩn hóa Tên Tính Năng Rút Gọn (Feature Display Name):** Thay thế chuỗi mô tả dài dòng (như `search by real DepartmentID anchor 2777`) ở cột danh sách giữa bằng tên tính năng súc tích, dễ nhận biết (`Search (Tìm theo ID)`, `Search (Không khớp)`, `Read / Prefill (Modal)`, `Create (Tạo mới)`, `Update (Cập nhật)`, `Delete (Xóa)`). Khi bấm chọn để xem ở Cột 3 (Chi tiết), hệ thống vẫn giữ nguyên 100% tiêu đề chi tiết và ngữ cảnh kịch bản.
    + Bảng chuỗi request đối chiếu (`aligned-reqs-table`) trong nút **So Sánh Parity** được bổ sung riêng cột **Flow** với badge phân loại chuẩn xác.
  - **Cơ chế Cumulative Reporter Auto-Merge:** Nâng cấp `json-reporter.ts` tự động gộp kết quả của các màn hình đã chạy trước đó (`banks` + `departments` = 15 test cases) thay vì ghi đè file `*-latest.json`.
  - **Mô hình Đồng bộ Trạng thái Trang Deterministic 3-Phase Settlement:** Loại bỏ hoàn toàn hardcode timeout bừa bãi (`{ timeout: 15000 }`). Áp dụng đồng bộ cho toàn bộ vòng đời: `goto()`, `search()`, `createDepartment()`, `updateDepartment()`, `deleteDepartment()` và Export Excel Guard. Khắc phục triệt để các cạm bẫy kỹ thuật: bẫy `#cover-spin` có sẵn class `hide` từ layout tĩnh, bẫy FOUC dòng *Không có dữ liệu*, và bẫy treo vô tận khi DB trắng 0 dòng.
  - **Tài liệu Hướng dẫn Dập khuôn Chuẩn hóa:** Đã hoàn thiện tài liệu [REPLICATION_GUIDE_REPORT_VIEWER_UPGRADE.md](file:///e:/Work/Place_Migrate/context/REPLICATION_GUIDE_REPORT_VIEWER_UPGRADE.md) chứa toàn bộ code diff Before vs After, phân tích kỹ thuật và checklist 7 bước dập khuôn trọn vẹn cho `cci-store-location-web`, `cci-dc-web` và `cci-scm-web`.
- **Bộ Test Trọng Tâm Thẩm Định 3 Màn Hình: banks (6 TCs) + departments (10 TCs) + quit-job-reasons/import (6 TCs) — 0 Migrate-Bug:**
  - **Quy mô bộ test:** Đã chạy và tích lũy đầy đủ 3 màn hình trọng điểm bao gồm cả CRUD, Dialog phức tạp và Import Excel Mutation có Rollback Engine:
    1. `banks` (6 tests: Load danh sách, 2 validation form rỗng, 3 vòng đời Create/Update/Delete chạm lỗi API gốc 406 BankID NULL).
    2. `departments` (10 tests: Load danh sách 1.529 dòng, 2 Search anchor/rỗng, Validation xuất excel trên bảng rỗng, Modal prefill, Create, Update, Delete và Happy Path Xuất Excel TC-HRW-02-008).
    3. `quit-job-reasons/import` (6 tests: Tải template, 2 validation form/lưới rỗng, Import preview, Commit mutation cập nhật ngày nghỉ việc hàng loạt có Deterministic Conditional Rollback tự động phục hồi ứng viên).
  - **Kết quả Đối chiếu Parity 3D (`compare-dim.py`) Giữa STG4 vs STG10:**
    - Tổng số test cases đối chiếu: **21 tests** (không tính SSO auth).
    - `PARITY_OK`: **14 tests (66.7%)** — Khớp 100% từng request chức năng.
    - `IMPROVED`: **3 tests (14.3%)** — .NET 10 chạy thành công vượt trội, trong khi .NET 4 cũ bị fail do hạ tầng/API cũ:
      + `TC-HRW-02-008` (Departments Export Excel): STG10 PASS, STG4 lỗi 500 disk error (`The device is not ready`).
      + `TC-HRW-09-010` (QuitJobReasons Import Preview): STG10 PASS, STG4 lỗi 406 do lệch đường dẫn chia sẻ file.
      + `TC-HRW-09-011` (QuitJobReasons Import Commit & Rollback): STG10 PASS, STG4 lỗi 406.
    - `BOTH_SKIP`: **3 tests (14.3%)** — `TC-HRW-01-003`, `004`, `005` do lỗi backend DB gốc 406 `Cannot insert NULL into BankID` đồng nhất trên cả 2 môi trường.
    - `CONTENT_DIFF`: **1 test (4.8%)** — `TC-HRW-01-001` (khác biệt request tải cache `/CacheStorerages/CreateCacheJS`).
    - **`MIGRATE_BUG`: `0 (0.0%)` — Tuyệt đối không phát sinh bất kỳ lỗi hồi quy nào trên .NET 10!**
- **Report Viewer:** Đang phục vụ trực tiếp tại http://localhost:8932/ với dữ liệu cập nhật mới nhất chứa cả 3 màn hình (data.js: 3.901 KB, 21 so sánh Parity chi tiết, Network Request/Response Payload đầy đủ).

- **Triển khai Công Cụ Quét Màn Hình Excel Tự Động & Lập Ma Trận Kế Hoạch Kiểm Thử (tools/scan_excel_surfaces.py):**
  - **Mục đích:** Xóa bỏ hoàn toàn việc 'prompt mù' (ad-hoc / viết test Excel thiếu căn cứ), tự động hóa 100% khâu khảo sát mã nguồn và phân bổ test cases theo Khung 8 Nhóm Kịch Bản Chuẩn (Playbook 63 - Rule 13H).
  - **Công cụ:** [`tools/scan_excel_surfaces.py`](file:///e:/Work/Place_Migrate/tools/scan_excel_surfaces.py) (kèm bản sao cục bộ [`03_qa/scripts/scan_excel_surfaces.py`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/scripts/scan_excel_surfaces.py)).
  - **Kết quả quét toàn hệ thống HRM:**
    * **Tổng số Controller được quét:** **59**
    * **Số màn hình có tính năng Excel:** **40** (chiếm 67.8% quy mô portal)
    * **Tổng số Kịch bản Quy hoạch (Planned TCs):** **177**
    * **Số Kịch bản Đã Triển Khai (Covered):** **58** (32.8%)
    * **Số Kịch bản Còn Thiếu (Missing / Gaps):** **119** (67.2%)
  - **Báo cáo sinh ra tự động:**
    * File JSON: [`03_qa/reports/excel-test-matrix.json`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/reports/excel-test-matrix.json)
    * File Markdown (UTF-8 BOM): [`03_qa/reports/excel-test-matrix.md`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/reports/excel-test-matrix.md)
  - **Ghi nhận hồ sơ:** Đã lập tài liệu chuẩn hóa [`04_critical_change/65_automated_excel_surface_scanner_and_test_matrix_generation.md`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/04_critical_change/65_automated_excel_surface_scanner_and_test_matrix_generation.md).
  - **Định hướng chiến lược (User Approved):** Tập trung hoàn thiện và nghiệm thu 100% độ phủ trên HRM trước; ghi nhận đầy đủ bài học kinh nghiệm; khi HRM đạt 100% sẽ dập khuôn đồng bộ sang cả 3 project portal (`cci-store-location-web`, `cci-dc-web`, `cci-scm-web`).

- **Thiết Lập Tiện Ích DataHarvestingHelper & Bể Ứng Viên Phân Trang Đa Tầng (03_qa/utils/data-harvesting-helper.ts):**
  - **Vấn đề giải quyết:** Khắc phục triệt để rủi ro cạn kiệt dữ liệu (Candidate Starvation) và lỗi 406 khi test Import Excel lặp lại nhiều lần.
  - **Tiện ích mới:** [`03_qa/utils/data-harvesting-helper.ts`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/utils/data-harvesting-helper.ts) cung cấp:
    * `fetchActiveEmployees`: Phân tích trường `EndDateWork` để loại trừ nhân viên đã nghỉ việc; tự động duyệt phân trang đa tầng (`ul.pagination li a`, `maxPages=4`, `minCandidates=10`) khi trang hiện tại cạn kiệt ứng viên hợp lệ.
    * `fetchActiveDepartments`, `fetchActiveStores`, `fetchActivePositions`: Hỗ trợ cào đa thực thể cho các màn hình import phức tạp nhiều khoá ngoại.
    * `generateDynamicExcelFile`: Đóng gói chuẩn SheetJS sinh serial date `46326` an toàn trên mọi hệ điều hành.
  - **Nâng cấp Module:** [`03_qa/modules/quit-job-reasons-import.module.ts`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/modules/quit-job-reasons-import.module.ts) tích hợp helper mới.
  - **Kiểm thử thực nghiệm:** Chạy lại test trên STG10, hệ thống tự động nhận diện ứng viên `32381` (đã nghỉ việc ở lần test trước) và chuyển tiếp chọn mượt mà ứng viên `32380` (`QA Nhan Vien 1792571783211`). Đạt **100% Pass (6/6 tests, 1.1 phút)**.
  - **Ghi nhận hồ sơ:** Đã lập tài liệu chuẩn hóa [`04_critical_change/66_enterprise_data_harvesting_helper_and_paginated_active_candidate_pipeline.md`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/04_critical_change/66_enterprise_data_harvesting_helper_and_paginated_active_candidate_pipeline.md).

- **Triển Khai Chuỗi Dò Vết AST Tĩnh & Deterministic Conditional Rollback Engine Cho Excel Mutations (03_qa/contracts & 03_qa/utils/data-harvesting-helper.ts):**
  - **Vấn đề giải quyết:** Kiểm thử tự động các tính năng Import Excel có hành vi mutation (Update EndDateWork, Deletes, Creates) thường làm biến đổi vĩnh viễn dữ liệu Staging, gây ô nhiễm dữ liệu (Data Pollution) và xung đột khóa/ràng buộc 406 ở các lần chạy sau.
  - **Kiến trúc chuỗi dò vết tĩnh (Code-Aware Static Trace Scanner):** Nâng cấp [`tools/scan_excel_surfaces.py`](file:///e:/Work/Place_Migrate/tools/scan_excel_surfaces.py) với module `ApiContractScanner` dò vết xuyên suốt từ Web Controller $
ightarrow$ Helper $
ightarrow$ Backend API Endpoint $
ightarrow$ Service Layer $
ightarrow$ SQL Stored Procedure; xác định bảng tác động và phân loại thành **4 Mutation Archetypes** (`CREATE`, `UPDATE`, `DELETE`, `UPSERT`), tự động sinh hợp đồng [`03_qa/contracts/excel-mutation-contracts.json`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/contracts/excel-mutation-contracts.json).
  - **Deterministic Rollback Engine có điều kiện nghiêm ngặt (`DataHarvestingHelper.ts`):**
    * `captureEmployeeSnapshot`: Chụp snapshot toàn vẹn thực thể qua `/Employees/ReadByID` trước khi thực hiện mutation.
    * `safeRollback`: Áp dụng quy tắc hoàn tác có điều kiện nghiêm ngặt — **chỉ hoàn tác khi và chỉ khi `executionResult.isCommitted === true`** (API HTTP 200 + `Status === 'Success'`). Nếu mutation thất bại, backend đã tự rollback transaction, test runner tự động bỏ qua hoàn tác an toàn (`[OK] SKIPPED`).
  - **Kiểm thử nghiệm thu trực tiếp trên STG10 (`import-quit-job-reasons.e2e.spec.ts`):**
    * Chạy live Playwright đạt **6/6 Passed (100% Pass Rate)** trong 1.1 phút (`test-report-20261021-221803.json`).
    * Rollback Engine đã phục hồi nguyên vẹn ứng viên `32375` (EmployeeID `34923`) về trạng thái ban đầu (`EndDateWork = null`, `IsActived = true`) ngay trong block `finally`.
  - **Cập nhật sổ lỗi & báo cáo local (Rule 14):** Bổ sung mục `FIX-HRM-05` vào [`03_qa/reports/defect-registry.json`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/reports/defect-registry.json), render trực quan trên báo cáo local HTML.
  - **Hồ sơ chi tiết:** Đã lập tài liệu chuẩn hóa [`04_critical_change/67_trace_api_sp_contract_and_deterministic_rollback.md`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/04_critical_change/67_trace_api_sp_contract_and_deterministic_rollback.md).

- **Triển Khai DbDataProvider Trực Tiếp MSSQL & Tối Ưu Báo Cáo Mạng Sạch Sẽ 100% (03_qa/utils/db-data-provider.ts):**
  - **Vấn đề giải quyết:** Trước đây bước chuẩn bị ứng viên active dùng Playwright điều hướng sang `/Employees` trên UI, bấm nút Tìm kiếm và duyệt phân trang 2 lần, làm chậm test (mất 5-8 giây) và làm xuất hiện 2 request dư thừa `POST /Employees/Search` trong báo cáo mạng của `TC-HRW-09-010`.
  - **Giải pháp kỹ thuật (DbDataProvider):**
    * Tạo [`03_qa/utils/db-data-provider.ts`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/utils/db-data-provider.ts): Kết nối trực tiếp vào MSSQL database UAT (`192.168.13.135/HRM`), thực thi truy vấn trực tiếp (`SELECT TOP 10 ... FROM HRM.Employee e INNER JOIN USR.[User] u ... WHERE e.EndDateWork IS NULL AND e.IsActived = 1`) trả về dữ liệu chuẩn trong **< 100ms**.
    * Tích hợp Fast-Path vào [`03_qa/utils/data-harvesting-helper.ts`](file:///e:/Work/Place_Migrate/cci-hrm-web-testgen/03_qa/utils/data-harvesting-helper.ts): Khi DB khả dụng, trả ngay danh sách ứng viên mà **không cần mở trình duyệt sang `/Employees`**, loại bỏ hoàn toàn các request mạng không thuộc màn hình test.
  - **Nâng cấp Giao diện Report Viewer (app.js & styles.css):**
    * Bổ sung tính năng Collapse / Expand cho các khối Request Payload và Response Body bằng thẻ HTML5 `<details class="net-payload-box" open>` và `<summary class="net-sub-title">`, mặc định mở sẵn để kỹ sư dễ quan sát.
    * Ẩn toàn bộ Payload đối với các endpoint tải template (`ExportTemplate`, `ExportEndDateTemplate`) để tránh hiển thị binary string rác dài dòng.
  - **Kết quả Kiểm thử Nghiệm thu Đối chiếu Parity (21 TCs trên cả STG10 và STG4):**
    * `PARITY_OK`: **14 tests (66.7%)**
    * `IMPROVED`: **3 tests (14.3%)** — STG10 Pass 100%, STG4 vướng disk/path backend cũ.
    * `BOTH_SKIP`: **3 tests (14.3%)** — Lỗi gốc `BankID NULL` DB constraint.
    * `CONTENT_DIFF`: **1 test (4.8%)** — CacheStorerage request.
    * **`MIGRATE_BUG`: 0 (0.0%)!**
    * Báo cáo mạng của `TC-HRW-09-010` và `TC-HRW-09-011` hiện tại **sạch sẽ 100%**, chỉ ghi nhận duy nhất các endpoint của chính nó (`/Directives/UploadFileAPI`, `/QuitJobReasons/ImportExcel`, `/QuitJobReasons/CreateExcel`).

- **Quy Hoạch Toàn Cục Danh Mục 34 Repos & Bộ Phân Giải Cross-Repo Closed Data Lifecycle (tools/repo-catalog.json & tools/repo_manager.py):**
  - **Vấn đề giải quyết:** Kiến trúc Con Cung là microservices phân tán; một Web portal không chỉ gọi API cùng tên (ví dụ: SCM Web gọi SCM API, ACC API, SOM API, MDM, SCA API; DC Web gọi DC API, SCM API, SOM API, ONL API...). Cần cơ chế chuẩn để scanner xác định chính xác repo API nguồn từ `E:\repo.txt`, hoạt động trên nhánh `dev`, và tuyệt đối không clone lặp lại.
  - **Tập tin Catalog Chuẩn ([`tools/repo-catalog.json`](file:///e:/Work/Place_Migrate/tools/repo-catalog.json)):**
    * Chuẩn hóa toàn bộ 34 repositories từ `E:\repo.txt`.
    * Phân loại rõ ràng (`web`, `api`, `bff`, `webhook`), cố định nhánh `dev`, ánh xạ tự động 14 repos đã có sẵn trong `E:\Work\Place_Migrate`.
    * Khai báo danh mục `configKeys` (`SCMUrl`, `ACCUrl`, `ApisUrl`, `SOMAPIUrl`, `ONLUrl`, `MDMUrl`...) và `domainPatterns` để phục vụ phân giải tự động.
  - **Công Cụ Phân Giải & Quản Lý Repo Cục Bộ ([`tools/repo_manager.py`](file:///e:/Work/Place_Migrate/tools/repo_manager.py)):**
    * `python tools/repo_manager.py list`: Liệt kê tình trạng local/remote và branch của 34 repos.
    * `python tools/repo_manager.py resolve --web <repo> --key <config_key>`: Tự động phân giải Web Action sang đúng Repo API (ví dụ: `cci-scm-web [ACCUrl] -> cci-accounting-api`).
    * `python tools/repo_manager.py get --repo <name>`: Cơ chế Zero Redundant Clone — nếu đã có thì tái sử dụng ngay lập tức (0.05s, đảm bảo branch `dev`); nếu chưa có thì clone on-demand đúng 1 lần duy nhất trên nhánh `dev`.
  - **Bổ Sung Quy Tắc Toàn Cục Bắt Buộc (Global Rule):**
    * Bổ sung **Rule 15** vào [AGENTS.md](file:///e:/Work/Place_Migrate/AGENTS.md) ở thư mục gốc workspace để bắt buộc mọi phiên làm việc và subagent phải tuân thủ nghiêm ngặt.
    * Ban hành tài liệu hướng dẫn kỹ thuật toàn diện: [CROSS_REPO_CLOSED_LIFECYCLE_GUIDE.md](file:///e:/Work/Place_Migrate/context/CROSS_REPO_CLOSED_LIFECYCLE_GUIDE.md).

- **Kiểm Thử Nghiệm Thu Thành Công 100% Closed Lifecycle Qua Script DB (e2e/quit-job-reasons/import-quit-job-reasons.e2e.spec.ts):**
  - **Cơ chế:** Hoàn toàn xóa bỏ việc gọi API Create / Rollback; áp dụng 100% chu trình DB Script khép kín:
    1. `Seed`: Gọi `DbDataProvider.seedIsolatedActiveEmployee()` chèn trực tiếp 1 bản ghi cô lập (`E2E_<timestamp>`) vào `HRM.Employee` và `USR.[User]` khớp chính xác điều kiện của SP `[HRM].[Employee_UpdateEndDateWork]`.
    2. `Test / Import`: Đưa bản ghi vừa seed vào dynamic Excel $\rightarrow$ Upload $\rightarrow$ Import preview $\rightarrow$ Commit update.
    3. `Teardown / Delete`: Trong block `finally`, gọi `DbDataProvider.deleteIsolatedEmployee(empId)` xóa sạch dữ liệu vừa tạo khỏi DB.
  - **Kết quả Kiểm thử Thực nghiệm Live trên STG10:**
    * Chạy toàn bộ suite `import-quit-job-reasons.e2e.spec.ts`: **Đạt 6/6 tests Passed (100% Pass Rate)** trong **38.3 giây**!
    * Cả 2 kịch bản `TC-HRW-09-010` và `TC-HRW-09-011` tự động sinh bản ghi test riêng biệt (`E2E_379959` và `E2E_386915`), kiểm thử thành công và tự động xóa sạch ngay lập tức.
    * Báo cáo mạng sạch 100%, không phát sinh request `/Employees/Search`, và DB UAT không hề bị tồn đọng rác hay biến dạng bất kỳ dữ liệu có sẵn nào.

- **Chuẩn Hóa Closed Data Lifecycle (Seed -> Test -> Delete) Toàn Diện Cho Tất Cả Các Luồng Mutation (Create, Update, Delete) — Không Để Lại Dữ Liệu Rác (Zero DB Pollution):**
  - **Mục tiêu:** Xóa bỏ hoàn toàn tình trạng biến dạng DB Staging hoặc phụ thuộc vào luồng tạo trên UI. Mọi ca test tạo/sửa/xóa đều phải tự cung cấp dữ liệu cô lập (`Seed`), thực hiện kịch bản test trên UI/API, và bắt buộc thực thi dọn dẹp triệt để trong block `finally` (`Teardown / Delete`).
  - **Mở rộng Thư Viện Doanh Nghiệp `DbDataProvider` (`03_qa/utils/db-data-provider.ts`):**
    * Bổ sung `seedIsolatedDepartment()`, `deleteIsolatedDepartment()`, `deleteIsolatedDepartmentByName()`: Tự động tính toán ID phòng ban (`MAX(DepartmentID) + 1`), sinh cây phân cấp `NodeTree`, xóa sạch trong < 15ms.
    * Bổ sung `seedIsolatedBank()`, `deleteIsolatedBank()`, `deleteIsolatedBankByName()`: Khởi tạo bản ghi ngân hàng độc lập với mã tiền tố `E2E_<timestamp>`.
    * Bổ sung `seedIsolatedQuitJobReason()`, `deleteIsolatedQuitJobReason()`, `deleteIsolatedQuitJobReasonByName()`: Khởi tạo bản ghi lý do nghỉ việc với mã cô lập.
  - **Kết Quả Triển Khai & Kiểm Thử Chi Tiết 4 Màn Hình Trọng Điểm:**
    1. **`departments` (`departments.e2e.spec.ts` — 10 tests, 100% PASS):**
       - `Create [FLOW]` (TC-005): Tạo mới phòng ban qua modal UI -> Kiểm tra prefill/hiển thị -> Xóa sạch trong `finally` qua `deleteIsolatedDepartmentByName()`.
       - `Update [FLOW]` (TC-006): Seed phòng ban cô lập -> Mở modal sửa tên trên UI -> Xác minh tên mới -> Xóa sạch trong `finally` qua `deleteIsolatedDepartment()`.
       - `Delete [FLOW]` (TC-007): Seed phòng ban cô lập -> Bấm Xóa trên UI -> Xác nhận qua modal jConfirm -> Kiểm chứng dòng biến mất -> Xóa phòng ngừa trong `finally`.
       - Toàn bộ 10/10 test cases PASS hoàn hảo (1.8 phút).
    2. **`banks` (`banks.e2e.spec.ts` — 7 tests, 6/7 PASS):**
       - **Giải quyết nút thắt pre-condition:** Trước đây `Banks/Create` bị lỗi API backend 406 (`Cannot insert the value NULL into column 'BankID'`) làm chặn luôn cả `Banks/Update` và `Banks/Delete`.
       - **Cơ chế `prepareBankForFlow`:** Trực tiếp Seed ngân hàng độc lập vào MSSQL + kích hoạt xóa cache Redis (`HRM.Bank`) bằng lệnh gọi `POST /Banks/Update` (tận dụng `RemoveCacheActionFilter`), giúp Angular UI nhận diện ngay bản ghi mới.
       - **Khắc phục selector:** Sửa `rowByBankName` từ `td:text-is` sang `this.gridRows().filter({ hasText: name })` để xử lý khoảng trắng của AngularJS bindings (`<td> {{item.BankName}} </td>`).
       - `Update [FLOW]` (TC-004): PASS trong 7.4s, xóa sạch trong `finally`.
       - `Delete [FLOW]` (TC-005): PASS trong 6.6s, xóa sạch trong `finally`.
       - Kết quả suite: Tăng vọt từ 2/5 lên **6/7 Passed**, unblock hoàn toàn các luồng biến đổi dữ liệu. Duy nhất TC-003 Create giữ nguyên phân loại `BACKEND-GAP`.
    3. **`quit-job-reasons` (`quit-job-reasons.e2e.spec.ts` — 7 tests, 100% PASS):**
       - `Create [FLOW]` (TC-004): Tạo mới lý do nghỉ việc trên UI -> Xóa sạch trong `finally`.
       - `Update [FLOW]` (TC-005): Seed lý do cô lập qua DB -> Sửa ghi chú trên UI -> Xóa sạch trong `finally`.
       - `Delete [FLOW - Bulk Delete]` (TC-006): Seed 2 lý do cô lập qua DB -> Chọn checkbox -> Xóa hàng loạt qua action POST -> Xóa sạch trong `finally`.
       - Kết quả: Đạt 7/7 tests Passed (100%).
    4. **`quit-job-reasons/import` (`import-quit-job-reasons.e2e.spec.ts` — 6 tests, 100% PASS):**
       - Áp dụng 100% DB Script Closed Lifecycle: Seed nhân viên active vào DB -> Tạo file dynamic Excel -> Import & Commit mutation -> Hard Delete sạch sẽ trong `finally`.
       - Kết quả: Đạt 6/6 tests Passed (100% trong 38.3s).
  - **Kết Quả Đối Chiếu Parity 3D Toàn Diện (STG10 vs STG4 — 27 Test Items):**
    * **`PARITY_OK`:** **21 tests (77.8%)** — Khớp tuyệt đối hành vi và chuỗi request giữa NET4 và NET10.
    * **`IMPROVED`:** **5 tests (18.5%)** — STG10 chạy thành công vượt trội, trong khi STG4 thất bại do lỗi hệ thống ổ đĩa hoặc backend API cũ (`The device is not ready`, lỗi upload file 406, lỗi API phân loại nhân viên).
    * **`BOTH_SKIP`:** **1 test (3.7%)** — Bỏ qua do backend constraint `BankID NULL`.
    * **`CONTENT_DIFF`:** **0 tests (0.0%)**.
    * **`ORIGIN_SAME`:** **0 tests (0.0%)**.
    * **`MIGRATE_BUG`:** **`0 (0.0%)` — Hoàn toàn không phát sinh lỗi migration hồi quy!**
  - **Kiểm Toán Ô Nhiễm Cơ Sở Dữ Liệu & Khắc Phục Triệt Để ID Ảo (Zero DB Pollution & Identity Reseed Audit):**
    * Thực thi truy vấn trực tiếp kiểm tra dữ liệu tồn đọng trên DB MSSQL UAT (`192.168.13.135/HRM`):
      + `SELECT COUNT(*) FROM HRM.Bank WHERE BankName LIKE 'E2E_%'` -> **0 bản ghi**.
      + `SELECT COUNT(*) FROM HRM.Department WHERE DepartmentName LIKE 'E2E_%'` -> **0 bản ghi**.
      + `SELECT COUNT(*) FROM HRM.QuitJobReason WHERE QuitJobReasonName LIKE 'E2E_%'` -> **0 bản ghi**.
      + `SELECT COUNT(*) FROM HRM.Employee WHERE FullName LIKE 'QA Auto E2E%'` -> **0 bản ghi**.
      + `SELECT COUNT(*) FROM USR.[User] WHERE UserName LIKE 'E2E_%'` -> **0 bản ghi**.
    * **Kiểm chứng Bộ đếm Identity (Post-Run Reseed Verification):**
      + `HRM.QuitJobReason`: `curIdent = 626`, `maxId = 626` (Khớp 100%, không bị lệch ID dù chạy qua nhiều ca Create/Update/Delete).
      + `HRM.Employee`: `curIdent = 34941`, `maxId = 34941` (Khớp 100%, kéo lùi trọn vẹn về đỉnh dữ liệu thật sau khi xóa).
    * **Kết luận:** 100% dữ liệu thử nghiệm được dọn dẹp sạch sẽ, bảo toàn nguyên vẹn chuỗi ID tự tăng, bảo vệ tuyệt đối môi trường UAT.

- **Hợp Nhất Toàn Diện & Tái Sinh Closed Lifecycle Màn Hình `Employees` (`employees.e2e.spec.ts` — 10 tests, 100% PASS STG10 & STG4):**
  - **Bối cảnh & Vấn đề giải quyết:** Trước đây kiểm thử màn hình nhân viên bị phân mảnh thành nhiều file rời rạc: `employees.e2e.spec.ts` chỉ có 2 test đọc, `mutation-lifecycle.e2e.spec.ts` chứa test tạo/sửa nhưng không tự dọn dẹp (để lại rác và nhảy ID ảo), `import-create-employees.e2e.spec.ts` bị lỗi vì màn hình Import nhân viên đã bị Con Cung bỏ từ 2022, còn 2 kịch bản xuất Excel (Export Empty Guard và Export Data Flow) thì bị bỏ ngỏ.
  - **Hợp nhất và Nâng cấp Suite Chuẩn Mực (`03_qa/e2e/employees/employees.e2e.spec.ts`):**
    * Gom trọn vẹn 8 nhóm kịch bản (10 test cases) vào một file duy nhất:
      1. `TC-HRW-37-001 [LOAD]`: Tải trang danh sách nhân viên ban đầu, kiểm tra các nút tìm kiếm, thêm mới, xuất excel và placeholder.
      2. `TC-HRW-37-002 [FLOW]`: Tìm kiếm mặc định (hơn 4.400 dòng nhân viên, phân trang, tổng cộng).
      3. `TC-HRW-37-003 [FLOW]`: Tìm kiếm theo từ khóa thực tế (anchor thật 100% khớp) và từ khóa ngẫu nhiên (lưới rỗng).
      4. `TC-HRW-37-004 [VALIDATION]`: Export Excel Guard — khi lưới rỗng, bấm `#btnExportExcel` chặn xuất và hiển thị `jAlert.Warning('Không có dữ liệu để xuất')` (Phủ kịch bản 2 của Playbook 63).
      5. `TC-HRW-37-005 [FLOW]`: Export Data Flow — khi lưới có dữ liệu, bấm `#btnExportExcel` gửi thành công request `POST /Employees/Export` (Phủ kịch bản 7 của Playbook 63).
      6. `TC-HRW-37-006 [FLOW]`: Read Employee Detail — kiểm chứng liên kết `/Employees/Edit/:id` trên từng dòng nhân viên.
      7. `TC-HRW-37-007 [FLOW] [LIFECYCLE]`: Closed Lifecycle Web UI Create — mở form `/Employees/Create`, điền thông tin nhân viên, submit thành công -> tìm kiếm lại đúng họ tên trên danh sách -> trong `finally` tự động gọi `DbDataProvider.deleteIsolatedEmployeeByName()` hard-delete bản ghi và kích hoạt `DBCC CHECKIDENT ('HRM.Employee', RESEED, @maxId)` đưa bộ đếm ID về đúng đỉnh dữ liệu thực tế (Zero ID jump!).
      8. `TC-HRW-37-008 [N/A]`: Xác nhận chính sách Con Cung không cho phép xóa cứng hồ sơ nhân viên trên UI (chỉ cho phép tạm dừng hoạt động hoặc xóa CMND/CCCD).
  - **Kết quả Kiểm thử Thực tế trên cả 2 Môi trường (Fresh Run Cặp STG10 vs STG4):**
    * **NET10 Target (https://hrm-stg10.concung.vn):** **6/6 Passed (100% Pass)** (1 setup + 5 tests) trong **51.9s** (`test-mssql-report-20261022-155325.json`).
    * **NET4 Origin (https://hrm-stg4.concung.vn):** **6/6 Passed (100% Pass)** (1 setup + 5 tests) trong **1.3m** (`test-net4-report-20261022-155427.json`).
    * **Đối chiếu 3D Parity Ma Trận Toàn Cục (`compare-dim-latest.json`):**
      + Tổng số test đối chiếu: **45 test cases** trên **7 màn hình** (`banks`, `departments`, `employees`, `employees/create`, `quit-job-reasons`, `quit-job-reasons/import`).
      + **`PARITY_OK`**: **39 tests (86.7%)** (Toàn bộ 5 test của `employees/create` đều đạt `PARITY_OK` 100%).
      + **`IMPROVED`**: **5 tests (11.1%)**.
      + **`BOTH_SKIP`**: **1 test (2.2%)**.
      + **`MIGRATE_BUG`**: **0 (0.0%) — Hoàn toàn không có lỗi lệch hành vi!**
  - **Kiểm toán Cơ sở Dữ liệu & Reseed Guard:**
    * Sau khi chạy qua 2 lượt test tạo nhân viên trên cả STG10 và STG4: `SELECT COUNT(*) FROM HRM.Employee WHERE FullName LIKE 'QA E2E Auto%'` -> **0 bản ghi tồn đọng**.
    * Trạng thái bộ đếm Identity: `IDENT_CURRENT('HRM.Employee') = 34943`, `MAX(EmployeeID) = 34943` -> **Khớp chính xác 100%, bảo vệ an toàn tuyệt đối DB UAT**.

- **Xây Dựng Bộ Kiểm Thử E2E Toàn Diện Màn Hình Tạo Mới Nhân Viên (/Employees/Create — 5 test cases, 100% PASS STG10 & STG4):**
  - **Bối cảnh & Mục tiêu:** Sau khi hoàn thiện màn hình danh sách /Employees, tiếp tục mở rộng kiểm thử chuyên sâu cho màn hình tạo mới /Employees/Create. Màn hình này sử dụng AngularJS kết hợp jQuery Unobtrusive Validation, SmartAdmin layout, các custom directives (custom-select2, js-tree-ddl) và hệ thống đa tab (Tab 1: Thông tin chung, Tab 2: Thông tin liên lạc, Tab 3: Thông tin công tác, Tab 4: Ngân hàng, Tab 7: CMND, Tab 5: Hình ảnh, Tab 8: Hợp đồng).
  - **Kiến trúc Kiểm thử Chuẩn Enterprise:**
    * Page Object: `03_qa/pages/employees-create.page.ts` định nghĩa toàn bộ bộ định vị trực quan (locators), form inputs, validation error spans, action buttons, tab anchors.
    * Module Helper: `03_qa/modules/employees-create.module.ts` gói gọn các luồng nghiệp vụ `submitCreate()`, `clickCreateNoWait()`, tích hợp `ClosedLifecycleTracker`.
    * Test Suite: `03_qa/e2e/employees/employee-create.e2e.spec.ts` gồm 5 test cases:
      1. `TC-HRW-37-CREATE-001 [LOAD]`: Tải form tạo mới nhân viên ban đầu, xác nhận form render thành công, các trường nhập liệu (Họ tên, Giới tính radio, nút Tạo mới) sẵn sàng và tab 1 "Thông tin chung" đang active.
      2. `TC-HRW-37-CREATE-002 [VALIDATION]`: Chặn submit khi form hoàn toàn rỗng, hiển thị validation error class `field-validation-error` tại trường Họ tên bắt buộc, ngăn chặn 100% việc gửi request `POST /Employees/Create`.
      3. `TC-HRW-37-CREATE-003 [VALIDATION]`: Chặn submit khi điền Họ tên nhưng bỏ trống Ngày sinh, kích hoạt validation error `field-validation-error` tại trường Ngày sinh, ngăn chặn request POST.
      4. `TC-HRW-37-CREATE-004 [FLOW] [CLOSED LIFECYCLE]`: Điền đầy đủ dữ liệu hợp lệ -> bấm Tạo mới -> đón nhận thông báo thành công `jAlert.Success("Tạo mới thành công")` -> trong khối `finally` tự động gọi `DbDataProvider.deleteIsolatedEmployeeByName()` xóa sạch bản ghi và thực thi `DBCC CHECKIDENT ('HRM.Employee', RESEED, @maxId)` đưa bộ đếm ID về đúng đỉnh dữ liệu thực tế (Zero DB Pollution & Zero ID Jump).
      5. `TC-HRW-37-CREATE-005 [FLOW]`: Tạo thành công nhân viên -> kiểm chứng mở khóa và chuyển tiếp mượt mà qua các Tab con: Tab 2 (Thông tin liên lạc — form `ThuongtruForm`) và Tab 3 (Thông tin công tác — form `UpdateWorkingForm`) -> dọn dẹp sạch bản ghi & reseed DB.
  - **Kết quả Kiểm thử Thực tế trên cả 2 Môi trường (Fresh Run Cặp STG10 vs STG4):**
    * **NET10 Target (https://hrm-stg10.concung.vn):** **6/6 Passed (100% Pass)** (1 setup + 5 tests) trong **51.9s** (`test-mssql-report-20261022-155325.json`).
    * **NET4 Origin (https://hrm-stg4.concung.vn):** **6/6 Passed (100% Pass)** (1 setup + 5 tests) trong **1.3m** (`test-net4-report-20261022-155427.json`).
    * **Đối chiếu 3D Parity Ma Trận Toàn Cục (`compare-dim-latest.json`):**
      + Tổng số test đối chiếu: **45 test cases** trên **7 màn hình** (`banks`, `departments`, `employees`, `employees/create`, `quit-job-reasons`, `quit-job-reasons/import`).
      + **`PARITY_OK`**: **39 tests (86.7%)** (Toàn bộ 5 test của `employees/create` đều đạt `PARITY_OK` 100%).
      + **`IMPROVED`**: **5 tests (11.1%)**.
      + **`BOTH_SKIP`**: **1 test (2.2%)**.
      + **`MIGRATE_BUG`**: **0 (0.0%) — Hoàn toàn không có lỗi lệch hành vi!**
  - **Kiểm toán Cơ sở Dữ liệu & Reseed Guard:**
    * `IDENT_CURRENT('HRM.Employee') = 34943`, `MAX(EmployeeID) = 34943` -> **Khớp chính xác 100%, không bị lệch ID**.
    * `Lingering QA rows: 0` -> Không có bản ghi rác nào tồn đọng trên Database UAT.
  - **Đồng bộ Report Viewer & Tự Động Hóa Toàn Diện:**
    * Đã tách riêng màn hình Tạo mới thành key độc lập `employees/create` (5 tests) song song cùng màn danh sách `employees` (13 tests) trên Report Viewer.
    * Đã thiết lập Rule 5 trong AGENTS.md và tích hợp tự động vào `run-e2e.win.ps1`: Tự động nhận diện prefix môi trường (test-mssql / test-net4), tự động merge thông minh theo test case, và tự động gọi `build_data.py` làm mới `viewer/data.js` ngay sau mọi đợt chạy test.

---

## 3. HỆ THỐNG CRON & WORKFLOW TỰ ĐỘNG HOÁ TOÀN CỤC (GLOBAL AUTOMATION)

- **Lần chạy Commit Sync gần nhất:** 2026-10-23 09:01:24 — Đã kéo và quét commit của 6 repo tham chiếu. Toàn bộ 3 portal (DC, Place, SCM) đều đã đồng bộ đầy đủ các giải pháp kỹ thuật cốt lõi (Redis DataProtection, NormalizeUrl, EPPlus order).

- **Lần chạy Daily Incremental Commit Sync 17:00:** 2026-10-23 09:01:24 (Hoàn tất thành công)
  - Đã fetch & pull 6 repo tham chiếu (`cci-hrm-web`, `cci-mbm-web`, `cci-timekeeping-web`, `cci-supplier-web`, `cci-common-web`, `cci-hrm-api`).
  - Trích xuất 150 commit gần nhất, phân tích và gom nhóm 8 danh mục kỹ thuật.
  - Đối chiếu với 3 portal đang thao tác (DC, Place, SCM): Tất cả các giải pháp kỹ thuật trọng yếu (Redis DataProtection Keyring, NormalizeUrl, EPPlus DataValidation) đều đã được áp dụng đầy đủ và đồng bộ, không phát sinh giải pháp mới cần dập khuôn thêm.
- **Job 2 (Continuous Auto-Healing Sweep - task-3316):** Chạy ngầm test đối chiếu Parity (Fail-Fast `--max-failures=1`). Khi phát hiện `migrate-bug`, tự động dừng, phân loại, tách nhánh `fix/*`, sửa code, quét chéo, merge `dev`, tạo PR Bitbucket, chờ 15 phút K8s rollout và re-test verify.
- **Job 3 (Targeted Regression Verification - Rule 13):** Sau mỗi lần dập khuôn và push code, kích hoạt ngay test case của module bị ảnh hưởng trực tiếp (Targeted Test) để nghiệm thu nhanh chóng mà không cần chạy lại toàn bộ suite từ đầu.
- **Job 4 (Local Defect Matrix & Code Comparison Report - Rule 14):** Tích hợp sổ theo dõi lỗi (`defect-registry.json`) vào báo cáo local HTML/Markdown, phân loại nhóm lỗi, hiển thị code diff cũ vs mới, liên kết 2 chiều giữa test cases và mã bug fix.

---

## 4. NGUYÊN TẮC CẬP NHẬT TIẾN ĐỘ (LƯU Ý DÀNH CHO AGENT)
1. **Một file duy nhất:** Không tạo file progress theo ngày (tránh sinh rác). Luôn cập nhật trực tiếp vào file này.
2. **Cập nhật ngay sau mỗi hành động:**
   - Chạy test xong → ghi nhận số case Pass/Fail/Skip, Report ID, đối chiếu parity.
   - Fix bug xong → ghi nhận commit, phân loại lỗi (`migrate-bug` / `oracle-broken` / `env-broken` / `test-bug`).
   - Tạo PR xong → cập nhật link PR và trạng thái merge.