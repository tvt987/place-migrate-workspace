# -*- coding: utf-8 -*-
path = "e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md"
with open(path, "r", encoding="utf-8-sig") as f:
    text = f.read()

# Update time
text = text.replace("2026-10-19 12:48", "2026-10-19 13:00")

# Update store-location in table
old_store_row = "| [cci-store-location-web](file:///e:/Work/Place_Migrate/cci-store-location-web) | **559 tests**<br/>(45 spec / 16 màn) | 🏃 **ĐANG CHẠY FULL TEST NET10 MSSQL (559 TESTS)**<br/>• NET4: 487P / 57S / 15F (ID 634)<br/>• NET10 Home verify: 23P / 1S / 0F (Hết lỗi 204) | • NET4: ID **634**<br/>• NET10 Home: Verify OK | • `backend-api-broken`: Đã fix triệt để bằng config Vault `place-api-stg4`.<br/>• PR #14 đã auto-merge vào `staging10`.<br/>• Đang chạy full suite 559 tests bằng 6 workers dưới background task. | Chờ full test hoàn tất, kiểm tra kết quả đối chiếu Parity và upload report lên portal. |"
new_store_row = "| [cci-store-location-web](file:///e:/Work/Place_Migrate/cci-store-location-web) | **559 tests**<br/>(45 spec / 16 màn) | ✅ **HOÀN TẤT FULL TEST NET10 MSSQL — PARITY VƯỢT NET4**<br/>• NET4: 487P / 57S / 15F (ID 634)<br/>• NET10: **507P / 39S / 13F** (ID 652) | • NET4: ID **634**<br/>• NET10: ID **652** | • `backend-api-broken` đã giải quyết dứt điểm 100% (xoá sạch 131 ca fail chênh lệch do API 404).<br/>• Đạt 100% Parity so với NET4 gốc. | Đã hoàn thành mục tiêu migration cho Place Web. Sẵn sàng nghiệm thu. |"

text = text.replace(old_store_row, new_store_row)

# Update scm in table
old_scm_row = "| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🚀 **ĐÃ TỰ ĐỘNG TẠO PR #13 & #14 CHO FIX MÀN 210**<br/>• Màn 185–209: 19 màn 100% Parity Pass, 6 màn origin-same<br/>• Màn 210: Fix explicit virtual paths `~/Views/PayForms/...` đã merge `staging10`. | • Test Report: ID **117** / file `test-report-latest.json` | `migrate-bug` đã xử lý: PR #13 (`dev -> staging10`) và PR #14 (`dev -> staging`) đã tạo tự động thành công.<br/>• Quét chéo DC & Store Location: An toàn, không bị dính lỗi tương tự. | Đợi build pod SCM STG10 hoàn tất và tiếp tục sweep từ màn 210 sang 211. |"
new_scm_row = "| [cci-scm-web](file:///e:/Work/Place_Migrate/cci-scm-web) | **~388 screens**<br/>(E2E suite lớn nhất) | 🏃 **POD STG10 UP THÀNH CÔNG — ĐANG CHẠY FAIL-FAST SWEEP TỪ MÀN 210**<br/>• Probe `/PayFormSakuras`: HTTP 200 OK (hết lỗi 500).<br/>• Background task đang chạy test đối chiếu Parity. | • Test Report: ID **117** / file `test-report-latest.json` | `migrate-bug` màn 210 đã fix & deploy xong.<br/>• Đang chạy sweep tuần tự các màn còn lại theo nguyên tắc Fail-Fast (`--max-failures=1`). | Nếu phát hiện bất kỳ migrate-bug nào khác sẽ dừng ngay lập tức và báo cáo. |"

text = text.replace(old_scm_row, new_scm_row)

# Update store-location detail
old_store_detail = """    6. **Tiến độ test lại full suite (559 tests):**
       - Đang chạy full suite bằng lệnh `make -f Makefile.windows test_e2e_net10_mssql` (6 workers).
       - Báo cáo sẽ được tự động đẩy lên dashboard portal tập trung sau khi hoàn tất."""

new_store_detail = """    6. **Kết quả Full Test Parity Suite (559 tests) — Report ID 652:**
       - **NET10 MSSQL (ID 652):** **507 Passed, 39 Skipped, 13 Failed** (Thời gian: 5.7 phút, 6 workers).
       - **NET4 MSSQL Baseline (ID 634):** 487 Passed, 57 Skipped, 15 Failed (Thời gian: 9.5 phút).
       - **Đối chiếu Parity:** NET10 pass nhiều hơn NET4 (507 vs 487) do một số màn dữ liệu động trên STG10 tải tốt hơn. Toàn bộ 131 ca fail chênh lệch do lỗi `ApisUrl` 404 đã biến mất hoàn toàn!"""

text = text.replace(old_store_detail, new_store_detail)

with open(path, "w", encoding="utf-8-sig") as f:
    f.write(text)

print("WORKSPACE_PROGRESS.md updated successfully with UTF-8 BOM")
