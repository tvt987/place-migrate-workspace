# -*- coding: utf-8 -*-
import sys

# 1. Update AGENTS.md
agents_path = "e:/Work/Place_Migrate/AGENTS.md"
with open(agents_path, "r", encoding="utf-8") as f:
    agents_text = f.read()

agents_target = "- **2. Bám sát Handbook, Quy trình Tạo Nhánh & PR Staging:** Luôn bám sát `DEV_HANDBOOK.md` và `FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md`. TUYỆT ĐỐI KHÔNG commit trực tiếp trên `dev`. Mọi việc fix bug phải tách nhánh `fix/<mã-fix>` từ `dev` mới nhất (sửa script test/docs thì tách `chore/*`). Sau khi test verify đạt trên nhánh fix, merge nhánh vào `dev` (`git merge --no-ff`), xoá nhánh và gắn tag `fix/<mã-fix>`. Với 2 nhánh `staging` và `staging10`: TUYỆT ĐỐI KHÔNG merge hoặc push code thủ công lên `staging` và `staging10`; BẮT BUỘC CHỈ TẠO PULL REQUEST (`dev → staging10` và `dev → staging`) vì hệ thống CI/CD đã có cơ chế tự động auto-merge và auto-build từ PR."

agents_replacement = "- **2. Bám sát Handbook, Quy trình Tạo Nhánh & PR Staging (Tự Động Tạo PR):** Luôn bám sát `DEV_HANDBOOK.md` và `FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md`. TUYỆT ĐỐI KHÔNG commit trực tiếp trên `dev`. Mọi việc fix bug phải tách nhánh `fix/<mã-fix>` từ `dev` mới nhất (sửa script test/docs thì tách `chore/*`). Sau khi test verify đạt trên nhánh fix, merge nhánh vào `dev` (`git merge --no-ff`), xoá nhánh và gắn tag `fix/<mã-fix>`. Với 2 nhánh `staging` và `staging10`: TUYỆT ĐỐI KHÔNG merge hoặc push code thủ công lên `staging` và `staging10`; BẮT BUỘC CHỈ TẠO PULL REQUEST (`dev → staging10` và `dev → staging`) vì hệ thống CI/CD đã có cơ chế tự động auto-merge và auto-build từ PR. **QUY TẮC TỰ ĐỘNG TẠO PR:** Khi merge và push lên `dev` xong, Agent **TỰ ĐỘNG TẠO LUÔN CẶP PULL REQUEST** (dùng `python tools/bitbucket_pr.py --repo concung/<repo> --action create-pair ...`) mà **KHÔNG CẦN CHỜ XÁC NHẬN HAY ĐỢI USER CLICK TẠO**, chỉ cần xuất lại link PR đã tạo trong phản hồi cho user theo dõi."

if agents_target in agents_text:
    agents_text = agents_text.replace(agents_target, agents_replacement)
    with open(agents_path, "w", encoding="utf-8") as f:
        f.write(agents_text)
    print("AGENTS.md updated successfully")
else:
    print("AGENTS.md target NOT found!")

# 2. Update GIT_RULES.md
git_rules_path = "e:/Work/Place_Migrate/GIT_RULES.md"
with open(git_rules_path, "r", encoding="utf-8") as f:
    git_text = f.read()

git_target = """## 2. Không merge/push thẳng vào `staging` và `staging10` – chỉ tạo Pull Request

- Commit fix lên `dev` (theo DEV_GUIDE), push `dev`.
- Muốn đưa lên staging: **tạo Pull Request** `dev → staging10` và `dev → staging` trên Bitbucket (cho mỗi repo liên quan). **Không** `git merge dev` rồi `git push origin staging|staging10`, không bấm Build tay: hệ thống **tự auto-merge và tự build**.
- Link tạo PR: `https://bitbucket.org/concung/<repo>/pull-requests/new?source=dev&dest=staging10` (đổi `dest=staging` cho nhánh còn lại). `git-sync.ps1` in sẵn link này và **từ chối** push khi nhánh hiện tại là `staging`, `staging10`, `staging4`, `master`, `main`.
- Sau khi PR được auto-merge và build xong thì mới test lại trên staging, ghi SHA + link report vào hồ sơ (DEV_GUIDE mục 5.7–5.8)."""

git_replacement = """## 2. Không merge/push thẳng vào `staging` và `staging10` – chỉ tạo Pull Request

- Commit fix lên `dev` (theo DEV_GUIDE), push `dev`.
- Muốn đưa lên staging: **tạo Pull Request** `dev → staging10` và `dev → staging` trên Bitbucket (cho mỗi repo liên quan). **Không** `git merge dev` rồi `git push origin staging|staging10`, không bấm Build tay: hệ thống **tự auto-merge và tự build**.
- **Tự động tạo PR (Không cần đợi xác nhận):** Agent **tự động gọi công cụ tạo cặp PR** (`python tools/bitbucket_pr.py --repo concung/<repo> --action create-pair ...`) ngay sau khi push `dev` mà **KHÔNG CẦN CHỜ USER XÁC NHẬN HAY CLICK TẠO THỦ CÔNG**, chỉ cần xuất lại link PR đã tạo vào phản hồi cho user theo dõi.
- Sau khi PR được auto-merge và build xong thì mới test lại trên staging, ghi SHA + link report vào hồ sơ (DEV_GUIDE mục 5.7–5.8)."""

# Normalise newlines in target matching
git_target_crlf = git_target.replace("\r\n", "\n").replace("\n", "\r\n")
git_target_lf = git_target.replace("\r\n", "\n")

if git_target_crlf in git_text:
    git_text = git_text.replace(git_target_crlf, git_replacement.replace("\r\n", "\n").replace("\n", "\r\n"))
    with open(git_rules_path, "w", encoding="utf-8") as f:
        f.write(git_text)
    print("GIT_RULES.md updated successfully (CRLF)")
elif git_target_lf in git_text:
    git_text = git_text.replace(git_target_lf, git_replacement.replace("\r\n", "\n"))
    with open(git_rules_path, "w", encoding="utf-8") as f:
        f.write(git_text)
    print("GIT_RULES.md updated successfully (LF)")
else:
    print("GIT_RULES.md target NOT found!")
