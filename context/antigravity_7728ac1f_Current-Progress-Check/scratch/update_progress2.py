# -*- coding: utf-8 -*-
path = "e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md"
with open(path, "r", encoding="utf-8-sig") as f:
    text = f.read()

# Update time
text = text.replace("2026-10-19 12:00", "2026-10-19 12:48")

# Update store-location in table
old_store_row = "| [cci-store-location-web](file:///e:/Work/Place_Migrate/cci-store-location-web) | **559 tests**<br/>(45 spec / 16 màn) | ⏳ **ĐÃ TỰ ĐỘNG TẠO PR #14 - CHỜ K8S ROLLOUT POD**<br/>• NET4: 487P / 57S / 15F (ID 634)<br/>• NET10 Home: 16P / 1S / 7F (Error 204 cũ) | • NET4: ID **634**<br/>• NET10: ID **636** | • `backend-api-broken`: Đã sửa dòng 83 trong Vault sang `place-api-stg4` (commit `77cb8fc`).<br/>• Đã tạo PR #14 (`dev -> staging10`) tự động bằng script.<br/>• Đang đợi CI/CD auto-merge và k8s rollout pod mới. | Sau khi rollout xong, chạy lại test đối chiếu Parity (kỳ vọng pass ~487 tests như NET4). |"
new_store_row = "| [cci-store-location-web](file:///e:/Work/Place_Migrate/cci-store-location-web) | **559 tests**<br/>(45 spec / 16 màn) | 🏃 **ĐANG CHẠY FULL TEST NET10 MSSQL (559 TESTS)**<br/>• NET4: 487P / 57S / 15F (ID 634)<br/>• NET10 Home verify: 23P / 1S / 0F (Hết lỗi 204) | • NET4: ID **634**<br/>• NET10 Home: Verify OK | • `backend-api-broken`: Đã fix triệt để bằng config Vault `place-api-stg4`.<br/>• PR #14 đã auto-merge vào `staging10`.<br/>• Đang chạy full suite 559 tests bằng 6 workers dưới background task. | Chờ full test hoàn tất, kiểm tra kết quả đối chiếu Parity và upload report lên portal. |"

text = text.replace(old_store_row, new_store_row)

# Update scm in table
old_scm_row = "| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | ✅ **ĐÃ TÌM RA NGUYÊN NHÂN GỐC & FIX XONG LỖI MÀN 210 (`pay-form-sakuras`)**<br/>• Màn 185–209: 19 màn 100% Parity Pass, 6 màn origin-same<br/>• Màn 210: Đã fix lỗi relative partial views khiến Razor ném 500 khi tái sử dụng view `PayForms`. | • Test Report: ID **117** / file `test-report-latest.json` | `migrate-bug` đã xử lý: Chuyển toàn bộ relative partial views trong `Views/PayForms/*.cshtml` (`IndexOutputCache`, `CreateOutputCache`, `EditOutputCache`, `EditCCAppOutputCache`) sang virtual path tuyệt đối `~/Views/PayForms/...` để các controller phân hệ khác (`PayFormSakuras`, `PayFormCCIs`, `PayFormCMTCs`, `PayFormANCs`) render bình thường. | Đã merge `dev` và push tag `fix/SCM-210-pay-form-sakuras-partial-path`. Tạo PR sang `staging10` & `staging` và tiếp tục sweep từ màn 211. |"
new_scm_row = "| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🚀 **ĐÃ TỰ ĐỘNG TẠO PR #13 & #14 CHO FIX MÀN 210**<br/>• Màn 185–209: 19 màn 100% Parity Pass, 6 màn origin-same<br/>• Màn 210: Fix explicit virtual paths `~/Views/PayForms/...` đã merge `staging10`. | • Test Report: ID **117** / file `test-report-latest.json` | `migrate-bug` đã xử lý: PR #13 (`dev -> staging10`) và PR #14 (`dev -> staging`) đã tạo tự động thành công.<br/>• Quét chéo DC & Store Location: An toàn, không bị dính lỗi tương tự. | Đợi build pod SCM STG10 hoàn tất và tiếp tục sweep từ màn 210 sang 211. |"

text = text.replace(old_scm_row, new_scm_row)

# Update store-location detail
old_store_detail = """    4. **Tự động tạo PR Bitbucket (Đã tạo):**
       - PR #14 (`dev -> staging10`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/14
       - PR #13 (`dev -> staging`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/13 (Merged)
    5. Đang chờ CI/CD auto-merge PR #14 và rollout pod k8s với config `place-api-stg4` trên `place-stg10.concung.vn`."""

new_store_detail = """    4. **Tự động tạo PR Bitbucket:**
       - PR #14 (`dev -> staging10`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/14 (Auto-merged)
       - PR #13 (`dev -> staging`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/13 (Merged)
    5. **Kết quả verify nhanh Home Spec (`e2e/home/home.e2e.spec.ts`):**
       - Đạt **23 Passed, 1 Skipped, 0 Failed** (khắc phục hoàn toàn lỗi 204 cũ).
    6. **Tiến độ test lại full suite (559 tests):**
       - Đang chạy full suite bằng lệnh `make -f Makefile.windows test_e2e_net10_mssql` (6 workers).
       - Báo cáo sẽ được tự động đẩy lên dashboard portal tập trung sau khi hoàn tất."""

text = text.replace(old_store_detail, new_store_detail)

# Update scm detail
old_scm_detail = """    - **Link tạo PR Bitbucket:** `https://bitbucket.org/concung/cci-scm-web/pull-requests/new?source=dev&t=1`"""
new_scm_detail = """    - **Tự động tạo PR Bitbucket (Đã hoàn tất):**
      - PR #13 (`dev -> staging10`): https://bitbucket.org/concung/cci-scm-web/pull-requests/13 (Auto-merged)
      - PR #14 (`dev -> staging`): https://bitbucket.org/concung/cci-scm-web/pull-requests/14 (Auto-merged)
    - **Kết quả quét chéo xuyên Portal (Cross-Portal Bug Sweep):**
      - `cci-dc-web`: Đã quét toàn bộ Controllers và Views. Không có controller nào render chéo view khác folder; partial view tương đối đều có file cục bộ tương ứng hoặc trong `Views/Shared/`. Kết luận: **An toàn 100%**.
      - `cci-store-location-web`: Đã quét toàn bộ Controllers và Views. Toàn bộ partial views đều đã được viết dưới dạng đường dẫn ảo tuyệt đối `~/Views/...`. Kết luận: **An toàn 100%**."""

text = text.replace(old_scm_detail, new_scm_detail)

with open(path, "w", encoding="utf-8-sig") as f:
    f.write(text)

print("WORKSPACE_PROGRESS.md updated cleanly with UTF-8 BOM")
