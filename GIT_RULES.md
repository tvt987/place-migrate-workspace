# GIT_RULES – Quy tắc git toàn cục cho workspace `E:\Work\Place_Migrate`

Áp dụng cho **mọi** người và **mọi** coding agent (Claude, Codex, Cursor, Antigravity, OpenCode…) thao tác git trong thư mục này, ở cả local lẫn trên git. File này nằm ở root workspace và được nhân bản sang repo workspace trên GitHub (`tvt987`). Khi mâu thuẫn với `DEV_GUIDE.md` thì **file này thắng** (xem mục 3).

## 0. Mỗi lần thao tác git: nạp lại context trước

Trước **bất kỳ** lệnh git nào (pull, push, merge, tag, tạo PR) phải đọc lại đủ 3 file dưới đây, không dựa vào trí nhớ của phiên chat cũ:

1. `E:\Work\Place_Migrate\cci-dc-web\DEV_GUIDE.md`
2. `E:\Work\Place_Migrate\cci-dc-web\DEV_HANDBOOK.md`
3. `E:\Work\Place_Migrate\cci-dc-web\FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md`

Sau đó đọc `AGENTS.md` / `README.md` của chính project sắp thao tác (hai file này ưu tiên hơn guide). Làm đúng quy trình trong các file đó: một bug = một mã `<Test case ID>-<slug>` = một commit `fix(<mã>): ...` + hồ sơ `04_critical_change/` + tag `fix/<mã>`; chỉ sửa `02_target/`; không force-push; không đưa secret/`.env` vào commit.

`tools\git-sync.ps1` luôn in lại nhắc nhở này và danh sách file cần đọc; dùng nó làm cửa vào duy nhất cho pull/push.

## 1. Hai mode (chọn mỗi lần pull/push)

Mỗi project `cci-*` có git riêng (remote Bitbucket `concung`), còn workspace này có một git khác (GitHub `tvt987`). Để không nhầm, mỗi lần pull/push **phải chọn mode**: `1`, `2` hoặc `both`. Không chọn thì không làm.

| Mode | Tên | Repo | Remote | Dùng cho |
|---|---|---|---|---|
| **1** | PROJECTS | từng thư mục `cci-*` (git riêng của chúng) | Bitbucket `concung/cci-*` | Code app, fix bug, deploy staging |
| **2** | CONTEXT | repo ở root `E:\Work\Place_Migrate` | GitHub `tvt987/<repo workspace>` | Rule, tool, handbook, lịch sử chat Antigravity, snapshot context |
| **both** | Cả hai | lần lượt mode 1 rồi mode 2 | | Cuối ngày / sau khi xong một đợt fix |

Lệnh:

```powershell
# hỏi mode tương tác
powershell -File E:\Work\Place_Migrate\tools\git-sync.ps1 -Action pull
powershell -File E:\Work\Place_Migrate\tools\git-sync.ps1 -Action push
# hoặc chỉ định
... -Action pull -Mode 1 -Repos cci-dc-web,cci-scm-web
... -Action push -Mode 2 -Message "docs: cap nhat context"
... -Action status -Mode both
```

Quy tắc theo mode:

- **Mode 1** chỉ đụng git của từng `cci-*`; không bao giờ `git add` file của mode 2 và ngược lại. Mode 2 bỏ qua (`.gitignore`) toàn bộ `cci-*/`.
- Repo đang có thay đổi chưa commit thì **không pull**; hỏi người dùng trước.
- Không `--force`, không `reset --hard`, không xoá nhánh/tag khi chưa được yêu cầu rõ.
- Trước khi push mode 2: quét secret (`.env`, token, password trong transcript) và file > 95 MB; có thì dừng.

## 2. Không merge/push thẳng vào `staging` và `staging10` – chỉ tạo Pull Request

- Commit fix lên `dev` (theo DEV_GUIDE), push `dev`.
- Muốn đưa lên staging: **tạo Pull Request** `dev → staging10` và `dev → staging` trên Bitbucket (cho mỗi repo liên quan). **Không** `git merge dev` rồi `git push origin staging|staging10`, không bấm Build tay: hệ thống **tự auto-merge và tự build**.
- Link tạo PR: `https://bitbucket.org/concung/<repo>/pull-requests/new?source=dev&dest=staging10` (đổi `dest=staging` cho nhánh còn lại). `git-sync.ps1` in sẵn link này và **từ chối** push khi nhánh hiện tại là `staging`, `staging10`, `staging4`, `master`, `main`.
- Sau khi PR được auto-merge và build xong thì mới test lại trên staging, ghi SHA + link report vào hồ sơ (DEV_GUIDE mục 5.7–5.8).

## 3. Chỗ DEV_GUIDE cũ bị thay thế

DEV_GUIDE V6 (mục 0, 4.2, A7) ghi "dev tự merge vào staging rồi bấm Build Jenkins". **Bỏ** cách đó; thay bằng mục 2 ở trên. Các phần khác của DEV_GUIDE (đặt tên, hồ sơ, tag, 7 luật, hậu kiểm) giữ nguyên.

## 4. Portal report test của web

- Dashboard: **https://report-web-testing-uat.concung.vn** (report test của các project web).
- Mỗi lần pull code mới về, **kiểm tra `03_qa/.env`** của project để có credential upload report. Report được đẩy lên khi chạy các lệnh `make test-*` (xem Makefile trong `03_qa/`).
- Không commit `.env`. Hồ sơ bug phải ghi link report + SHA (DEV_GUIDE mục 3, 5.6).

## 5. Quét chéo 3 project web khi fix bug

Ba project web: **`cci-scm-web`**, **`cci-dc-web`**, **`cci-store-location-web`** (Place web).

Mỗi lần fix một bug ở **một** trong ba project này, bắt buộc:

1. Từ nguyên nhân gốc, rút ra mẫu lỗi (pattern: lớp/hàm/đoạn razor/JS, kiểu serialize, cấu hình, case-sensitivity…).
2. Quét **cả 3 project** (`02_target/` và test liên quan) xem có lỗi tương tự không: `tools\git-sync.ps1 -Action scan -Pattern "<regex>"` (liệt kê kết quả ở cả 3).
3. Có chỗ giống thì **fix luôn** ở project đó, mỗi project một commit/hồ sơ/tag theo quy ước riêng của nó, và **push cùng đợt** (mode 1), rồi PR theo mục 2.
4. Trong hồ sơ bug ghi rõ: đã quét cả 3 project, kết quả (có/không có chỗ tương tự, file nào).
5. Không có chỗ tương tự vẫn phải ghi "đã quét, không có".

## 6. Áp dụng ở local và trên git

- Local: file này + `AGENTS.md` + `CLAUDE.md` ở root workspace; agent mở workspace tự đọc được.
- Git (mode 2): các file này, `tools/`, và context nằm trong repo workspace trên GitHub `tvt987`, nên máy khác clone về cũng có rule.
- Sửa rule: sửa file này, rồi push mode 2.
