# Workspace Rules — Place_Migrate

## 1. Giới hạn phạm vi thao tác code (Target Projects Only)
- **CHỈ ĐƯỢC PHÉP** làm việc và sửa mã nguồn/fix code trên các project web sau:
  - `cci-store-location-web`
  - `cci-dc-web`
  - `cci-scm-web`
  - `cci-oneteam-web`: **TẠM THỜI PENDING** do team migrate chưa triển khai xong; không đụng vào code lúc này.
- **TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP SỬA** các project khác trong workspace (bao gồm toàn bộ repo `-api`: `cci-dc-api`, `cci-scm-api`, `cci-store-location-api`; các repo khác: `cci-mbm-web`, `cci-report-web`, v.v.). Các project này chỉ dùng để lấy context tham chiếu, phục vụ việc đối chiếu, chạy môi trường và build test cho các project web được liệt kê ở trên.

## 2. Quy trình Git, Nhánh và Triển khai (Bám sát DEV_HANDBOOK.md & FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md)
- Luôn luôn bám sát và tuân thủ các quy tắc trong:
  - `cci-dc-web/DEV_HANDBOOK.md`
  - `cci-dc-web/FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md`
  - `GIT_RULES.md`
- **Quy tắc tạo nhánh (Branching Workflow):**
  - **TUYỆT ĐỐI KHÔNG** commit trực tiếp trên nhánh `dev`.
  - Mọi thao tác sửa lỗi bắt buộc phải tách một nhánh riêng `fix/<mã-fix>` từ `dev` mới nhất (ví dụ: `fix/TC-PLACE-auth-idsurl-fallback`).
  - Mọi thao tác sửa script test E2E hoặc cập nhật tài liệu tách nhánh `chore/*` từ `dev`.
  - Sau khi kiểm thử và xác minh fix đạt yêu cầu trên nhánh làm việc: merge nhánh vào `dev` bằng `git merge --no-ff`, xoá nhánh làm việc (cả local và remote nếu có), và gắn tag `fix/<mã-fix>`.
- **RÀNG BUỘC BẮT BUỘC VỚI `staging` VÀ `staging10`:**
  - **TUYỆT ĐỐI KHÔNG** merge thủ công hoặc push trực tiếp lên `staging` và `staging10`.
  - **CHỈ TẠO PULL REQUEST:** `dev → staging10` và `dev → staging`. Hệ thống CI/CD đã có trigger auto-merge và auto-build tự động từ PR.

## 3. Quét lỗi đồng bộ xuyên Portal (Cross-Portal Bug Sweep)
- Mỗi khi phát hiện và fix một lỗi tại bất kỳ portal nào (ví dụ: lỗi cấu hình fallback `IDSUrl`, redirect SSO, selector select2, modal jConfirm, data table, v.v.):
  - **BẮT BUỘC** phải chủ động rà soát, quét toàn bộ các portal web đang thao tác còn lại (`cci-store-location-web`, `cci-dc-web`, `cci-scm-web`).
  - Kiểm tra xem các portal khác có đang áp dụng cùng pattern hoặc gặp lỗi tương tự hay không.
  - Sửa lỗi đồng bộ trên tất cả các repo bị ảnh hưởng, tạo nhánh và PR cùng đợt để đảm bảo tính nhất quán trên toàn hệ thống.

## 4. Nhớ lại context sau mỗi nhiệm vụ
- Mỗi khi thực hiện xong một nhiệm vụ, agent phải tự động đối chiếu và nhớ lại context bên trong các handbook (`DEV_HANDBOOK.md`, `FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md`, playbook, quy tắc parity) để đảm bảo không bị trôi ngữ cảnh và không làm sai quy trình ở các bước tiếp theo.

## 5. Bảo toàn mã hoá UTF-8 BOM
- Mọi file sửa đổi (`.cs`, `.cshtml`, `.json`, `.xml`, `.config`, `.sql`, v.v.) nếu ban đầu có UTF-8 BOM thì phải bảo toàn 100% UTF-8 BOM, kiểm tra lại bằng `git diff` trước khi commit.

## 6. Quản lý & Cập nhật kết quả Test Report của từng Portal
- Mọi đợt chạy test E2E trên từng portal (`cci-scm-web`, `cci-dc-web`, `cci-store-location-web`, v.v.) phải luôn đảm bảo kết quả report được tự động đẩy lên Dashboard UAT tập trung: **https://report-web-testing-uat.concung.vn** (qua GCS và bảng `test_report` trong database `ReportTest`).
- Sau mỗi lần chạy test, kiểm tra xác nhận output có `uploaded ... test_report_id=...` để đảm bảo dữ liệu report đã ghi nhận thành công lên hệ thống quản lý tập trung phục vụ kiểm soát tiến độ.
- Luôn kiểm tra file `03_qa/.env` của portal đang thao tác để có đầy đủ cấu hình DB và SSO credential phục vụ upload report. Tuyệt đối không commit file `.env`.

## 7. Đối chiếu Parity & Phân loại lỗi Migration sau mỗi đợt Test
Sau mỗi đợt chạy test đối chiếu giữa bản gốc (`NET4` / `staging4`) và bản migrate (`NET10` / `staging10` / `staging`), **BẮT BUỘC** phải so sánh kết quả và phân loại rõ ràng theo quy chuẩn mục 6.3 của `DEV_HANDBOOK.md`:
1. **Lỗi Migration (`migrate-bug`)**:
   - **Đặc điểm:** Bản gốc `NET4` chạy ĐẠT nhưng bản `NET10` chạy LỖI (hoặc NET10 có hành vi khác lệch so với NET4).
   - **Xử lý:** Đây là lỗi do mã nguồn migrate trên .NET 10 gây ra. Bắt buộc tạo hồ sơ theo dõi trong `04_critical_change/` (`<Test case ID>-<slug>.md`), tạo nhánh `fix/<mã fix>`, sửa đúng nguyên nhân trong `02_target/`, chạy test verify đạt trên local/staging rồi mới merge vào `dev` và tạo PR sang `staging`/`staging10`.
2. **Không phải lỗi Migration (Lỗi ngoại vi / Gốc / Môi trường):**
   - **`origin-same` / `oracle-broken`:** Bản gốc `NET4` cũng chạy lỗi y hệt (dữ liệu staging rỗng, form không có data, chức năng gốc đã lỗi từ trước). $\rightarrow$ Không sửa code .NET 10 để che lỗi, ghi chú rõ tình trạng vào hồ sơ.
   - **`backend-api-broken`:** Web lỗi do API backend trả về 500 / 404 / sai schema contract. $\rightarrow$ Chuyển issue cho team phụ trách API, không sửa web.
   - **`sso-broken` / `env-broken`:** Lỗi hạ tầng, timeout redirect Keycloak, mất kết nối DB. $\rightarrow$ Ghi nhận issue, chuyển DevOps / SysAdmin.
   - **`test-bug`:** Script test E2E viết chưa chuẩn (sai selector, timeout ngắn, prefix title chưa normalize). $\rightarrow$ Sửa script test trong `03_qa/` trên nhánh `chore/*`, không coi là lỗi sản phẩm.

## 8. Duy trì & Cập nhật File Tiến độ Global (`WORKSPACE_PROGRESS.md`)
- Sau mỗi lần chạy test, fix lỗi, push code, cập nhật PR hoặc có bất kỳ diễn biến mới nào về tiến độ, **BẮT BUỘC** phải cập nhật trực tiếp vào file [WORKSPACE_PROGRESS.md](file:///e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md) ở thư mục gốc workspace.
- **Quy tắc:** Không tạo file tiến độ theo ngày hoặc theo version (tránh sinh rác); luôn luôn cập nhật đè trạng thái mới nhất vào file duy nhất này để dễ dàng kiểm soát, truy xuất nhanh và tránh bị quên bối cảnh.

## 9. Commit Message Sạch & Chuyên Nghiệp (TUYỆT ĐỐI CẤM "Co-Authored-By")
- **TUYỆT ĐỐI KHÔNG** thêm bất kỳ dòng trailer, watermark hay chữ ký AI nào như `Co-Authored-By: ...`, `Co-authored-by: Claude`, `Co-authored-by: Gemini`, `Co-authored-by: Antigravity` vào commit message, tag message hoặc nội dung Pull Request.
- Mọi commit message phải sạch sẽ, chuẩn mực kỹ sư theo định dạng Conventional Commits (`fix(...)`, `feat(...)`, `chore(...)`, `test(...)`, `docs(...)`) theo quy định trong `DEV_HANDBOOK.md`.
- Giữ lịch sử Git sạch sẽ, chuyên nghiệp, bảo mật quy trình làm việc và không để lại dấu vết bot/AI attribution.

## 10. Test Fail-Fast & Dừng Ngay Khi Gặp Lỗi Migrate (Áp dụng cho TẤT CẢ các Portal)
- Khi chạy test E2E (đặc biệt là các bộ test quy mô lớn như SCM với ~388 màn), **BẮT BUỘC** phải chạy ở chế độ **Fail-Fast** (`--max-failures=1`).
- Khi phát hiện bất kỳ lỗi nào hoặc `migrate-bug` (ví dụ: NET4 đạt mà NET10 lỗi, lỗi 500, crash, sai lệch dữ liệu, timeout không mong muốn):
  - **PHẢI DỪNG TEST NGAY LẬP TỨC VÀ BÁO CÁO (REPORT) LIỀN**.
  - Tuyệt đối không treo hoặc tiếp tục chạy đến hết suite làm mất thời gian chờ đợi.
  - Phân tích nguyên nhân, lập hồ sơ và fix dứt điểm xong mới tiếp tục chạy các màn tiếp theo.

