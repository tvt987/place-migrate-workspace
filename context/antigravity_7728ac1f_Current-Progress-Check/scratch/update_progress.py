# -*- coding: utf-8 -*-
path = "e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md"
with open(path, "r", encoding="utf-8-sig") as f:
    text = f.read()

# Replace time
text = text.replace("2026-10-19 10:15", "2026-10-19 12:00")

# Update table line 13
old_table_row = "| [cci-store-location-web](file:///e:/Work/Place_Migrate/cci-store-location-web) | **559 tests**<br/>(45 spec / 16 màn) | ⏳ **ĐÃ PUSH CODE & VAULT GITOPS - CHỜ TẠO PR ĐỂ K8S BUILD POD**<br/>• NET4: 487P / 57S / 15F (ID 634)<br/>• NET10 Home: 16P / 1S / 7F (Error 204 cũ) | • NET4: ID **634**<br/>• NET10: ID **636** | • `backend-api-broken`: Đã sửa dòng 83 trong Vault sang `place-api-stg4` (commit `77cb8fc`).<br/>• Code `02_target/.../appsettings.json` đã cập nhật mặc định sang `place-api-stg4` (commit `1c9586c`), merge vào `dev` (`c065f17`) và push tag `fix/fallback-apisurl-stg4`.<br/>• Pod K8s STG10 chưa tự động reload nên cần tạo PR để CI/CD build và rollout pod mới. | Tạo PR (`dev -> staging10` và `dev -> staging`) để CI/CD build pod mới, sau đó chạy lại test đối chiếu Parity. |"
new_table_row = "| [cci-store-location-web](file:///e:/Work/Place_Migrate/cci-store-location-web) | **559 tests**<br/>(45 spec / 16 màn) | ⏳ **ĐÃ TỰ ĐỘNG TẠO PR #14 - CHỜ K8S ROLLOUT POD**<br/>• NET4: 487P / 57S / 15F (ID 634)<br/>• NET10 Home: 16P / 1S / 7F (Error 204 cũ) | • NET4: ID **634**<br/>• NET10: ID **636** | • `backend-api-broken`: Đã sửa dòng 83 trong Vault sang `place-api-stg4` (commit `77cb8fc`).<br/>• Đã tạo PR #14 (`dev -> staging10`) tự động bằng script.<br/>• Đang đợi CI/CD auto-merge và k8s rollout pod mới. | Sau khi rollout xong, chạy lại test đối chiếu Parity (kỳ vọng pass ~487 tests như NET4). |"

text = text.replace(old_table_row, new_table_row)

old_store_pr = """    4. **Link tạo PR Bitbucket:** `https://bitbucket.org/concung/cci-store-location-web/pull-requests/new?source=dev&t=1`
    5. Sau khi tạo PR và merge vào `staging10`, pipeline CI/CD sẽ build image mới và rollout pod k8s với config `place-api-stg4`."""

new_store_pr = """    4. **Tự động tạo PR Bitbucket (Đã tạo):**
       - PR #14 (`dev -> staging10`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/14
       - PR #13 (`dev -> staging`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/13 (Merged)
    5. Đang chờ CI/CD auto-merge PR #14 và rollout pod k8s với config `place-api-stg4` trên `place-stg10.concung.vn`."""

text = text.replace(old_store_pr, new_store_pr)

# Write back with UTF-8 BOM
with open(path, "w", encoding="utf-8-sig") as f:
    f.write(text)

print("WORKSPACE_PROGRESS.md updated with UTF-8 BOM successfully")
