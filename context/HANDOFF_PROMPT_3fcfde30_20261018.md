# HANDOFF — tiếp tục từ conversation "Repository Review And Mapping"

> **Cách dùng:** mở phiên chat MỚI trong Antigravity IDE (workspace `E:\Work\Place_Migrate`), copy toàn bộ file này paste vào tin nhắn đầu tiên. Phiên cũ (`3fcfde30-4110-403c-8f9f-a4ed95abc9e6`) đã bị server xoá prefix do quá dài, không prompt tiếp được.

Bạn đang tiếp nhận công việc từ một phiên chat trước đó đã hết context. Dưới đây là toàn bộ bối cảnh cần thiết. Đọc hết, xác nhận lại trạng thái thực tế bằng `git status` / `git log` trước khi làm gì, rồi tiếp tục từ mục **Next steps**.

---

## 1. Bối cảnh dự án

- **Workspace:** `E:\Work\Place_Migrate` (nhiều repo Bitbucket của hệ thống Con Cung, org `concung`).
- **Mục tiêu chung:** migrate các web app legacy (DC, SCM, Store Location/Place, OneTeam, MBM) sang stack mới (.NET 10 + MSSQL/PostgreSQL), và **đảm bảo parity 100%** giữa bản gốc và bản migrate bằng bộ test E2E Playwright nằm ở `03_qa/` của từng repo.
- **Phiên gốc bắt đầu 2026-09-28** bằng yêu cầu: clone `cci-store-location-web`, review tổng thể + kiến trúc, tạo file mindmap. Sau đó mở rộng thành toàn bộ công việc QA/migration parity cho nhiều repo.
- Mindmap/kiến trúc đã có: `context/MINDMAP_ARCHITECTURE.md`, `context/PROJECTS_MAP.md`.

### Các repo trong workspace (branch + commit mới nhất tại 2026-10-18)

| Repo | Branch | Commit mới nhất | Dirty |
|---|---|---|---|
| `cci-scm-web` | `dev` | `d009a7b7` 2026-10-15 — test(qa): fix pay-forms create init confirm, select2 masks, locator imports and timeouts | 1 untracked (`03_qa/reports/details/`) |
| `cci-scm-api` | `staging4` | `0a09d95` 2026-09-21 | clean |
| `cci-dc-web` | `dev` | `60a2abf` 2026-10-15 — test(qa): auto detect APP_ENV for report upload and preserve UTF-8 BOM | clean |
| `cci-dc-api` | `dev` | `2e43752` 2026-10-14 | clean |
| `cci-store-location-web` | `dev` | `bf6f4d0` 2026-10-15 — test(qa): add report upload harness, auth token caching and git path detection | 3 modified + 12 untracked |
| `cci-store-location-api` | `dev` | `1753474` 2026-10-14 | clean |
| `cci-oneteam-web` | `dev` | `22fffcf` 2026-10-01 | 5 modified + 3 untracked |
| `cci-mbm-web` | `dev` | `1aac189` 2026-10-08 | clean |
| `cci-report-web` | `codebase/003` | `f4a5ce3` 2026-08-26 | clean |

### Môi trường test

- SCM: STG10 `https://scm-stg10.concung.vn/`, STG4 `https://scm-stg4.concung.vn/`
- Dashboard report test: `https://report-web-testing-uat.concung.vn`
- Credential report + IDS1 nằm trong `03_qa/.env` của từng repo (**đã có sẵn, không ghi ra tài liệu**).

---

## 2. Trạng thái công việc

### 2.1 SCM E2E parity sweep (việc chính, dở dang)

Yêu cầu gốc của user: *"ok chạy all hết, không phải đợi"* — tự động chạy và verify toàn bộ bộ E2E qua **~388 folder screen** trong `cci-scm-web/03_qa/e2e/`, theo thứ tự alphabet, chế độ unattended fail-fast, giữ **parity 100% giữa STG10 và STG4**.

- **Đã xong: screen 1–140** (commit `ac131298` ngày 2026-10-14 "complete screens 115-140 and pre-patch output-screens with 100% parity across STG10 and STG4").
- Commit `d009a7b7` (2026-10-15) tiếp tục fix nhóm `pay-forms*`: init confirm khi create, select2 mask, locator import, timeout.
- **Screen 130 `output-sale-charities`** là screen cuối được chạy có log đầy đủ (task-18241 trên STG10, 15 tests).
- Đã pre-patch sẵn (title prefix + select2 cleanup) cho: `output-sale-check-in-gift-groups`, `output-sale-check-in-product-limits`, `output-sale-check-in-purchases`, `output-sale-check-in-store-limits`, `output-sale-check-in-types`.
- PR Bitbucket cần giữ đồng bộ: [PR #4](https://bitbucket.org/concung/cci-scm-web/pull-requests/4) (`dev -> staging`) và [PR #9](https://bitbucket.org/concung/cci-scm-web/pull-requests/9) (`dev -> staging10`).

### 2.2 Push report lên dashboard (yêu cầu mới nhất của user, 2026-10-15)

Nguyên văn yêu cầu:

> `https://report-web-testing-uat.concung.vn` => dashboard report test của web. "mọi người pull code mới về check 03_qa/.env để có credential push report lên theo lệnh make test-*" — leader báo như trên, chạy cho **dc** và **place** để push phần report lên, **SCM đã push rồi không cần chạy lại**, lưu ý **chỉ phần web, không phải api**.

Tình trạng tới 2026-10-15 15:45:
- `cci-scm-web/03_qa/scripts/upload-report.js` + `reports/details/*.json` — đã chạy, report mới nhất `test-report-20261015-152056.json`.
- `cci-dc-web/03_qa/scripts/upload-report.js` + `run-e2e.win.ps1` đã cập nhật; có report `test-mssql-report-20261015-135934.json` và `test-pgsql-report-20261015-135959.json`.
- `cci-store-location-web/03_qa/scripts/upload-report.js` + `run-e2e.win.ps1` đã cập nhật; có report `test-mssql-report-20261015-134741.json` và `test-net4-report-20261015-135304.json`.
- `cci-store-location-web/03_qa/.env` đã thêm `TESTREPORTER_PLATFORM=web` và block `IDS1_*` (chưa commit).
- **Chưa xác nhận** là report của DC và Place đã lên dashboard thành công hay chưa → **việc đầu tiên cần verify**.

### 2.3 Việc dở dang chưa commit

- `cci-store-location-web`: `00_docs/00_screen/.oracle-lock.json`, `03_qa/.env`, `04_critical_change/SESSION_CONTEXT_SUMMARY_20260930.md` (modified); các file untracked gồm `DEV_GUIDE.md`, `DEV_HANDBOOK.md`, `FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md`, `MINDMAP_ARCHITECTURE.md`, `16_qa_web_playbook.md`, `04_critical_change/COMPLETE_SESSION_HANDOVER_20260930.md`, `tests/reports/test-report-2026093*.md`, và một file rác tên `enva` (nên xoá).
- `cci-oneteam-web`: `appSetting.config` (01_origin + 02_target), `Makefile` (root + 02_target), `02_target/tests/SmokeTests.cs`; file rác `_build_probe_controllers.txt`, `_dev.err`, `_run.err`.
- Từ 2026-10-16 đến 2026-10-18 **không có file nào trên đĩa bị thay đổi** — phiên cũ ngày 18/10 chỉ quay vòng rồi bị server restart (`[Notice] All your subagents and background tasks have been stopped due to server restart`), không tạo ra kết quả nào. Không cần tìm lại gì từ ngày đó.

---

## 3. Fix pattern tái sử dụng được (rút ra từ 140 screen đã làm)

1. **`jConfirm("Bạn có chắc muốn tạo mới?")` bật ngay khi load form create**
   Gặp ở `output-orders-create`, `output-order-destroys-create`, `output-use-create`, `bonus-output-sales-creates`, `pay-forms*`… (chỉ bỏ qua khi `DataSetting.strHost == "localhost"`).
   Fix: override `open()` trong module, click `Đồng ý` trên `#MsgBoxBack` nếu có:
   ```ts
   override async open(route: string, loadEndpoints: string[] = []) {
     const res = await super.open(route, loadEndpoints);
     const confirm = this.ui.confirmBox();
     const btn = confirm.getByText('Đồng ý', { exact: true });
     if (await btn.isVisible({ timeout: 5000 }).catch(() => false)) {
       await btn.click().catch(() => {});
       await this.page.waitForTimeout(1000);
     }
     return res;
   }
   ```
2. **Nút submit bị `ng-disabled` khi grid rỗng** (vd `output-orders-create-multi` có `ng-disabled="PnProduct.Lst.length == 0"`). Playwright `click()` sẽ chờ tới hết timeout.
   Fix: kiểm tra `if (!(await submit.isEnabled().catch(() => false)))` ở cả test validation và save:
   - validation: `expect(guard.blocked, 'không được gửi request ghi khi submit disabled').toEqual([]); return;`
   - save: `test.skip(true, 'nút submit bị disabled khi chưa nạp dữ liệu — N/A save'); return;`
3. **`save for real` + `TEST_ALLOW_WRITE=1`**: `.env` set `TEST_ALLOW_WRITE=1` nên `test.skip(...)` không bỏ qua; khi form thiếu dữ liệu thì client-side validation chặn, không có POST → `page.waitForResponse` treo tới timeout.
   Fix: bọc `page.waitForResponse` trong `try { ... } catch { ... }` với timeout 5000ms.
4. **Title parity DC vs SCM**: luôn dùng `expected.replace(/^(DC|SCM)\s*-\s*/i, '')` và `/(DC|SCM)/i.test(title)` để tránh fail giả.
5. **select2 drop mask**: nhiều screen cần cleanup mask của select2 trước khi assert/click.

---

## 4. Ràng buộc bắt buộc (user đã chốt, đừng hỏi lại)

- **Không dừng lại hỏi xác nhận** — chạy unattended, fail-fast, liên tục.
- Mọi lệnh test SCM phải có đủ flag:
  ```powershell
  $env:LOCAL_BASE_URL=""; $env:BASE_URL="https://scm-stg10.concung.vn/"; $env:UPLOAD_REPORT="0"; npx playwright test e2e/<screen>/<screen>.e2e.spec.ts --project=e2e --workers=1 --max-failures=1
  ```
  (chạy STG10 trước, rồi đổi `BASE_URL` sang `https://scm-stg4.concung.vn/`)
- **Giữ nguyên UTF-8 BOM** trên mọi file đã sửa; verify bằng `git diff -U0` trước khi commit.
- Phân loại chênh lệch rõ ràng: `migrate-bug` / `oracle-broken` / `test-bug`.
- Commit & push `origin/dev` mỗi 10–15 screen để PR #4 và PR #9 luôn tươi.
- Cwd mặc định cho SCM QA: `E:\Work\Place_Migrate\cci-scm-web\03_qa`.

---

## 5. Next steps (làm theo thứ tự)

1. **Verify report dashboard**: xác nhận report của `cci-dc-web` và `cci-store-location-web` (chỉ web, không api) đã push lên `https://report-web-testing-uat.concung.vn` thành công. Nếu chưa, chạy lại `make test-*` theo credential trong `03_qa/.env` của từng repo.
2. **Commit dọn dẹp**: commit `03_qa/.env` + docs của `cci-store-location-web`, xoá file rác (`enva`, `_dev.err`, `_run.err`, `_build_probe_controllers.txt`).
3. **Tiếp tục SCM sweep từ screen 131** theo thứ tự alphabet, mỗi screen chạy STG10 → STG4:
   `output-sale-check-in-gift-groups` → `output-sale-check-in-product-limits` → `output-sale-check-in-purchases` → `output-sale-check-in-store-limits` → `output-sale-check-in-types` → `output-sale-check-ins` → `output-sale-clear-stock-attributes` → `output-sale-clear-stock-groups` → `output-sale-clear-stock-images` → `output-sale-clear-stock-prizes` → …
   (trước khi chạy, đối chiếu lại `git log` nhóm `pay-forms*` ở commit `d009a7b7` để biết screen nào đã được fix sẵn)
4. Commit & push định kỳ, giữ PR #4 / PR #9 đồng bộ.

---

## 6. Tài liệu tham chiếu (đã trích xuất từ phiên cũ)

| File | Nội dung |
|---|---|
| `context/HANDOFF_LAST_CHECKPOINT_3fcfde30_20261014.md` | Checkpoint/compaction summary cuối cùng của phiên cũ (2026-10-14), đầy đủ, kèm danh sách 102 artifact |
| `context/HANDOFF_ALL_CHECKPOINTS_3fcfde30.md` | Toàn bộ 44 checkpoint summary theo thời gian — lịch sử tiến độ chi tiết nhất |
| `context/HANDOFF_USER_REQUESTS_3fcfde30.md` | 185 yêu cầu của user theo thứ tự thời gian (28/09 → 18/10) |
| `context/antigravity_3fcfde30_Repository-Review-And-Mapping/` | Bản copy brain folder phiên cũ: `scratch/` (85 script đã dùng), `.system_generated/logs/transcript_full.jsonl` (32MB transcript đầy đủ), `.system_generated/tasks/*.log` |
| `context/MINDMAP_ARCHITECTURE.md`, `context/PROJECTS_MAP.md` | Mindmap kiến trúc + map các project |

Transcript gốc (còn sống) ở: `C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\`
**Lưu ý:** nội dung transcript chỉ còn đầy đủ tới `2026-10-15T02:33Z`; các step sau đó đã bị server đánh dấu `CLEARED` (rỗng). Đừng cố đọc phần đó, dùng git log + file trên đĩa làm nguồn sự thật.

---

**Việc đầu tiên:** chạy `git status` + `git log --oneline -5` trên `cci-scm-web`, `cci-dc-web`, `cci-store-location-web` để xác nhận trạng thái khớp với mô tả trên, rồi bắt đầu từ Next step 1.
