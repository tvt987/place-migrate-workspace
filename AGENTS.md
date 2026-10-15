# AGENTS.md (workspace root)

**Trước mọi thao tác git** (pull/push/merge/tag/PR) trong workspace này, đọc `GIT_RULES.md` ở cùng thư mục, rồi đọc lại:
`cci-dc-web/DEV_GUIDE.md`, `cci-dc-web/DEV_HANDBOOK.md`, `cci-dc-web/FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md`, và `AGENTS.md` của project đang làm.

Tóm tắt không thay cho việc đọc:

- Mỗi lần pull/push phải chọn mode: **1** (git từng project `cci-*`, Bitbucket), **2** (git workspace, GitHub `tvt987`) hoặc **both**. Dùng `tools/git-sync.ps1`.
- **Không** merge/push thẳng `staging`, `staging10`; chỉ tạo Pull Request `dev → staging10` và `dev → staging`, hệ thống tự auto-merge + build.
- Fix bug ở `cci-scm-web` / `cci-dc-web` / `cci-store-location-web` ⇒ quét lại cả 3 project tìm lỗi tương tự, fix và push cùng đợt.
- Report web: https://report-web-testing-uat.concung.vn ; kiểm tra `03_qa/.env` để có credential upload khi chạy `make test-*`. Không commit `.env`.
