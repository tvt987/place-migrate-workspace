# BÁO CÁO ĐỒNG BỘ COMMIT & DẬP KHUÔN THÔNG MINH (DAILY COMMIT SYNC)

> **Thời gian thực hiện:** 2026-10-27 07:40:57 (Kích hoạt tự động lúc 17:00)
> **Phạm vi kiểm tra:** 6 Repo tham chiếu (`cci-hrm-web`, `cci-mbm-web`, `cci-timekeeping-web`, `cci-supplier-web`, `cci-common-web`, `cci-hrm-api`)
> **Portal đích đối chiếu:** 3 Portal đang thao tác (`cci-dc-web`, `cci-store-location-web`, `cci-scm-web`)

---

## 1. TRẠNG THÁI SYNC CỦA CÁC REPO THAM CHIẾU

| Repo | Nhánh | Trạng thái Git | Commit mới nhất trên dev |
|---|:---:|:---:|---|
| `cci-hrm-web` | `dev` | ✅ synced | e39a6d4 - tringuyen-spec, 14 hours ago : refactor: clean up and optimize employee import and document handling modules |
| `cci-mbm-web` | `dev` | ✅ synced | fefdd61 - Long Phan, 11 hours ago : fix(38-openxml-writer-duplicate-row-calcpr-order): OpenXML writer: moi hang mot <row> dung thu tu, calcPr sau sheets (Excel xuat ra khong mo duoc) |
| `cci-timekeeping-web` | `dev` | ✅ synced | 2406989 - Long Phan, 2 days ago : fix(qa): uploader tu ap rule report_skips roi ghi thang qua SP moi (test_report_upsert_raw) |
| `cci-supplier-web` | `dev` | ✅ synced | 9cf34bb - Long Phan, 2 days ago : fix(qa): web khong ap rule report_skips, ghi thang so tho bang test_report_upsert_raw |
| `cci-common-web` | `dev` | ✅ synced | 481a5e6 - Long Phan, 2 days ago : fix(qa): web khong ap rule report_skips, ghi thang so tho bang test_report_upsert_raw |
| `cci-hrm-api` | `dev` | ✅ synced | 4bafdc66 - Long Phan, 23 hours ago : qa: cap nhat test-data 2026-09-25 (dof/hrm/tkp) + calibrate-latest |

---

## 2. PHÂN LOẠI & GOM NHÓM CÁC GIẢI PHÁP KỸ THUẬT TỪ REPO THAM CHIẾU

### 2.1. Redis & DataProtection / Session (7 commits)
- [`cci-timekeeping-web`] `3039fb1` - chore(skills): sync .agents/.claude tu root (IDS/MDM single source rule, playbook 17) *(Long Phan, Sun Oct 18 00:51:05 2026 +0700)*
- [`cci-timekeeping-web`] `66a90a6` - chore(origin): dua config 01_origin ve dung moi truong stg *(Long Phan, Sat Oct 17 15:46:54 2026 +0700)*
- [`cci-timekeeping-web`] `bc18bb8` - fix(config): dong bo Redis + Kibana host/credential voi vaults-gitops, them TimeOffLogin *(Long Phan, Wed Oct 7 21:51:36 2026 +0700)*
- [`cci-common-web`] `cf89753` - chore(skills): sync .agents/.claude tu root (IDS/MDM single source rule, playbook 17) *(Long Phan, Sun Oct 18 00:52:01 2026 +0700)*
- [`cci-common-web`] `fbdc132` - chore(origin): dua config 01_origin ve dung moi truong stg *(Long Phan, Sat Oct 17 15:46:58 2026 +0700)*
- [`cci-common-web`] `2d021dd` - chore(origin): pull master10 e65e46f8 (truoc: 16ec9e97) + config stg *(Long Phan, Fri Oct 16 04:48:37 2026 +0700)*
- [`cci-common-web`] `c805113` - fix(qa): upload-report lay token thuc qua side-channel ids1 login *(Long Phan, Fri Oct 9 12:54:23 2026 +0700)*

### 2.2. API Client & Endpoint Normalization (15 commits)
- [`cci-hrm-web`] `15e0286` - fix(qa): web khong ap rule report_skips, ghi thang so tho bang test_report_upsert_raw *(Long Phan, Sun Oct 25 10:51:09 2026 +0700)*
- [`cci-mbm-web`] `8f10c46` - fix(qa): web khong ap rule report_skips, ghi thang so tho bang test_report_upsert_raw *(Long Phan, Sun Oct 25 10:51:08 2026 +0700)*
- [`cci-timekeeping-web`] `2020408` - fix(qa): Makefile.windows upload-report luon chay bat ke exit code test *(Long Phan, Fri Oct 9 10:43:48 2026 +0700)*
- [`cci-supplier-web`] `9cf34bb` - fix(qa): web khong ap rule report_skips, ghi thang so tho bang test_report_upsert_raw *(Long Phan, Sun Oct 25 10:51:06 2026 +0700)*
- [`cci-supplier-web`] `cf1b774` - feat(qa): W2 batch 2 — E2E in phiếu giao hàng đơn dự trữ PQT (TC-SUP-23) *(nqdthuancc, Wed Oct 21 13:34:02 2026 +0700)*
- [`cci-supplier-web`] `01c0036` - feat(qa): W2 — E2E chi tiết & in đơn cho 7 module (SUP-15..SUP-22) *(nqdthuancc, Wed Oct 21 12:49:36 2026 +0700)*
- [`cci-supplier-web`] `8546c45` - feat(qa): W0 blueprints - chi tiet/in 8 man don hang + ra soat 11 blueprint stale *(nqdthuancc, Wed Oct 21 11:56:58 2026 +0700)*
- [`cci-supplier-web`] `b26635b` - feat(qa): W0+W1 — blueprint chi tiet/in don NCC + 14 test route/permission *(nqdthuancc, Wed Oct 21 11:13:46 2026 +0700)*
- *... và 7 commits khác.*

### 2.3. Excel Export & EPPlus / ClosedXML (27 commits)
- [`cci-hrm-web`] `e39a6d4` - refactor: clean up and optimize employee import and document handling modules *(tringuyen-spec, Mon Oct 26 17:11:01 2026 +0700)*
- [`cci-hrm-web`] `de9fca6` - refactor: enhance report viewer and build process with new features and improvements *(tringuyen-spec, Mon Oct 26 10:01:01 2026 +0700)*
- [`cci-hrm-web`] `38d8d2d` - Merge remote-tracking branch 'origin/dev' into dev *(Long Phan, Sun Oct 25 01:17:38 2026 +0700)*
- [`cci-hrm-web`] `2062910` - refactor: enhance file upload handling and improve data retrieval in controllers and modules *(tringuyen-spec, Sat Oct 24 15:06:06 2026 +0700)*
- [`cci-hrm-web`] `f85b0dd` - refactor: enhance report viewer with screen count display and improved UI elements *(tringuyen-spec, Sat Oct 24 13:36:24 2026 +0700)*
- [`cci-hrm-web`] `4aa0674` - refactor: improve working allocation module to skip unconfigured rows during updates *(tringuyen-spec, Thu Oct 22 23:48:52 2026 +0700)*
- [`cci-hrm-web`] `5bc840b` - refactor: update EmployeeBankSearchRes to allow nullable BankID for improved data handling *(tringuyen-spec, Thu Oct 22 22:41:28 2026 +0700)*
- [`cci-hrm-web`] `abbc251` - refactor: enhance export functionality and improve data handling in employee modules *(tringuyen-spec, Thu Oct 22 18:34:25 2026 +0700)*
- *... và 19 commits khác.*

### 2.4. Authentication / Keycloak / SSO / Cookie (59 commits)
- [`cci-hrm-web`] `f0b5a06` - fix(qa): khoi phuc ban upload-report.js goc cua app -web, chi them SP summary *(Long Phan, Sun Oct 25 01:53:58 2026 +0700)*
- [`cci-hrm-web`] `d533b22` - feat(qa): upload-report.js goi SP test_report_upsert thay insert thang *(Long Phan, Sun Oct 25 01:39:23 2026 +0700)*
- [`cci-hrm-web`] `b6a23d2` - feat(qa): upload-report.js ghi passed/failed/skipped vao test_report *(Long Phan, Sun Oct 25 01:13:25 2026 +0700)*
- [`cci-mbm-web`] `342c39b` - docs(36-timespan-newtonsoft-cast-cham-cong): them ho so 36 vao chi muc 04_critical_change *(nqdthuancc, Mon Oct 26 17:10:12 2026 +0700)*
- [`cci-mbm-web`] `703ecbe` - fix(36-timespan-newtonsoft-cast-cham-cong): doc TimeSpan cham cong bang Newtonsoft *(nqdthuancc, Mon Oct 26 17:10:12 2026 +0700)*
- [`cci-mbm-web`] `69f8741` - docs(34-csrf-mailbox-mutation): ket qua chay local voi stg10 cho csrf va trustHtml *(nqdthuancc, Mon Oct 26 16:59:58 2026 +0700)*
- [`cci-mbm-web`] `f409336` - fix(34-csrf-mailbox-mutation-r2): cookie CC.AF SameAsRequest de localhost HTTP phat token *(nqdthuancc, Mon Oct 26 16:59:52 2026 +0700)*
- [`cci-mbm-web`] `c37e14a` - docs(34-csrf-mailbox-mutation): bao cao cto lo hong hop thu *(nqdthuancc, Mon Oct 26 16:13:44 2026 +0700)*
- *... và 51 commits khác.*

### 2.5. Database / MSSQL / PostgreSQL / Dapper / EF (3 commits)
- [`cci-hrm-api`] `69d9b5dc` - qa-skip-tag: trace script -> wrapper bản chuẩn skill, ghi lại trace-baseline (skipTag) *(Long Phan, Sat Oct 24 13:21:31 2026 +0700)*
- [`cci-hrm-api`] `61b1cc11` - qa-skip-tag: guard chuẩn N18 + NET10 config trỏ appsettings.json thật *(Long Phan, Sat Oct 24 13:20:50 2026 +0700)*
- [`cci-hrm-api`] `d7f06c01` - no message *(Tran Duy, Thu Oct 22 09:44:20 2026 +0700)*

### 2.6. Razor Views / Bundles / Partial Views (2 commits)
- [`cci-hrm-web`] `061c686` - refactor: enhance report viewer with improved UI and functionality *(tringuyen-spec, Fri Oct 23 10:55:14 2026 +0700)*
- [`cci-mbm-web`] `407d648` - Merge branch 'fix/all' into dev *(nqdthuancc, Mon Oct 26 17:21:53 2026 +0700)*

### 2.7. E2E QA Testing & Stability Utilities (9 commits)
- [`cci-hrm-web`] `aad4819` - feat: add QA evidence helper, JSON reporter, and sample fixtures for test automation *(ToanHuynhIT, Sun Oct 25 15:52:47 2026 +0700)*
- [`cci-timekeeping-web`] `453b8da` - feat(qa): add UploadReport parameter to run-e2e.win.ps1 for conditional report uploading *(tringuyen-spec, Fri Oct 9 18:22:07 2026 +0700)*
- [`cci-supplier-web`] `36ed0a0` - test(qa): trạng thái rỗng không còn skip — search từ khoá không khớp *(nqdthuancc, Thu Oct 22 18:22:11 2026 +0700)*
- [`cci-supplier-web`] `44afd2f` - feat(qa): hướng 1 — spec dùng account có dữ liệu + lọc khoảng ngày trước khi đếm dòng *(nqdthuancc, Thu Oct 22 18:18:53 2026 +0700)*
- [`cci-supplier-web`] `715b591` - chore(qa): khai báo sẵn 4 env OID đơn dự trữ PQT + sửa fallback ?? ->  *(nqdthuancc, Wed Oct 21 19:05:44 2026 +0700)*
- [`cci-supplier-web`] `a10c219` - Merge branch 'fix/all' into dev *(nqdthuancc, Tue Oct 20 19:29:35 2026 +0700)*
- [`cci-common-web`] `7586ab5` - test(TC-COMMON-74-007): chi bat buoc redirect/4xx khi BASE khong phai localhost *(nqdthuancc, Tue Oct 13 17:58:49 2026 +0700)*
- [`cci-common-web`] `51dcab4` - test(TC-COMMON-25-007): chon tinh dau tien chua co cau hinh va co cua hang hoat dong *(nqdthuancc, Tue Oct 13 17:58:48 2026 +0700)*
- *... và 1 commits khác.*

### 2.8. Other Fixes / Migration Build (28 commits)
- [`cci-hrm-web`] `9e5225a` - refactor: remove scenario description card styles and related HTML for cleaner report viewer *(tringuyen-spec, Thu Oct 22 15:26:50 2026 +0700)*
- [`cci-hrm-web`] `679f25f` - fix: resolve Web Report Viewer data path issues and enhance standalone serving *(tringuyen-spec, Thu Oct 22 11:30:36 2026 +0700)*
- [`cci-hrm-web`] `37def70` - (...) update *(ToanHuynhIT, Thu Oct 22 11:12:11 2026 +0700)*
- [`cci-mbm-web`] `3d1f799` - Merge branch 'dev' into fix/all *(nqdthuancc, Mon Oct 26 17:20:40 2026 +0700)*
- [`cci-mbm-web`] `9c65b4f` - Merge branch 'fix/chamcong' into dev *(nqdthuancc, Mon Oct 26 17:14:03 2026 +0700)*
- [`cci-mbm-web`] `6bf5b05` - Merge branch 'dev' into fix/all *(nqdthuancc, Mon Oct 26 16:23:07 2026 +0700)*
- [`cci-mbm-web`] `3baa80b` - Merge branch 'fix/all' into dev *(nqdthuancc, Fri Oct 23 14:32:30 2026 +0700)*
- [`cci-mbm-web`] `1cf9a91` - README.md edited online with Bitbucket *(Phan Ngo Hoang Long, Fri Oct 23 06:38:19 2026 +0000)*
- *... và 20 commits khác.*

---

## 3. MA TRẬN ĐỐI CHIẾU DẬP KHUÔN TRÊN 3 PORTAL ĐÍCH

| Hạng mục kỹ thuật | cci-dc-web | cci-store-location-web | cci-scm-web | Đánh giá & Khuyến nghị |
|---|:---:|:---:|:---:|---|
| **Redis DataProtection Keyring** | ĐÃ ÁP DỤNG (Pass) | ĐÃ ÁP DỤNG (Pass) | ĐÃ ÁP DỤNG (Pass) | ✅ Cả 3 portal đã cấu hình chuẩn theo mẫu HRM (`DataProtection-Keys:<Prefix>`) kèm fallback an toàn. |
| **API Client NormalizeUrl** | ĐÃ ÁP DỤNG (Pass) | ĐÃ ÁP DỤNG (Pass) | ĐÃ ÁP DỤNG (Pass) | ✅ Đã áp dụng xử lý double slash (//) trên toàn bộ các phương thức gọi API backend. |
| **EPPlus DataValidation Order** | KHÔNG SỬ DỤNG (N/A) | ĐÃ FIX THỨ TỰ (RenderSheetMasterDataHelper.cs) | ĐÃ FIX THỨ TỰ (AccountingProcessDepartmentsController.cs) | ✅ Đã khắc phục triệt để trên SCM. DC và Place không dùng DataValidation nên không bị ảnh hưởng. |
| **Branch HEAD & Trạng thái PR** | [dev] e022cd7 Merge branch 'fix/dc-kestrel-utf8-and-linux-excel-compat' into dev | [dev] 6dbb83f Merge branch 'fix/place-kestrel-utf8-and-model-binding-limits' into dev | [dev] ce7b8340 Merge branch 'fix/scm-kestrel-utf8-and-model-binding-limits' into dev | ✅ Đã merge dev sạch và tạo các cặp PR Bitbucket chuẩn mực. |

---

## 4. KẾT LUẬN & ĐỀ XUẤT HÀNH ĐỘNG
- **Toàn bộ các giải pháp kỹ thuật cốt lõi (Redis DataProtection, URL normalize, Excel validation) đã được dập khuôn đồng bộ 100% trên cả 3 portal web.**
- **Không phát hiện thêm giải pháp mới nào trong các repo tham chiếu cần phải dập khuôn thêm vào thời điểm hiện tại.** Các commit mới nhất trong HRM/Timekeeping chủ yếu là logic kiểm thử E2E riêng biệt của từng nghiệp vụ (StoreCVSL, WorkShiftSupportPolicies) và HRM-API backend logic.
- **Tiếp tục duy trì trạng thái ổn định cho 3 portal web.**