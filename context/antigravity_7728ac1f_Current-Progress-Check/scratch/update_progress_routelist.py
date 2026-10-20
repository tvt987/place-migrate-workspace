import sys

with open('WORKSPACE_PROGRESS.md', 'r', encoding='utf-8-sig') as f:
    text = f.read()

# Update timestamp
text = text.replace(
    '> **Cập nhật mới nhất:** 2026-10-19 20:36:00 (Hoàn tất Trực Quan Hoá Tham Số Playwright, Đối Chiếu Request Parity & Sửa Lỗi Asset 404 Trên QA Viewer)',
    '> **Cập nhật mới nhất:** 2026-10-19 21:48:00 (Đã hoàn tất chạy test live Playwright thu thập Payload & Response thật STG4 vs STG10 cho màn route-list [PLACE-33])'
)

# Add route-list live test run info in 2.2
insert_marker = '- **Dập khuôn kỹ thuật từ HRM/MBM (19/10/2026):**'
new_content = '''- **Ghi nhận Network Payload & Response Thật Màn `route-list` (/mat-bang/danh-sach-tuyen-duong) (19/10/2026):**
  - Chạy live Playwright test ghi nhận trọn vẹn Request Payload & Response Body từ server thật cho cả 2 môi trường:
    + STG4 Baseline: `test-net4-report-20261019-214448.json` (ID 683) — 14 Passed, 1 Skipped (1.3m).
    + STG10 Live: `test-mssql-report-20261019-214100.json` (ID 682) — 14 Passed, 1 Skipped (1.2m).
  - Đối chiếu Parity: **100% Khớp (PARITY OK)**.
    + Với ca `TC-PLACE-33-002: tìm kiếm từ khoá rỗng`: Playwright ghi nhận POST `/RouteIndex/Search` trả về đầy đủ 129 tuyến đường (`Total: 129`, bắt đầu từ `X3 - Quảng Trường Lam Sơn Thanh Hóa`, khớp 100% với thao tác search tay).
    + Với ca `TC-PLACE-33-004: tìm từ khoá không tồn tại`: Playwright gửi payload `Keyword=zzz-qa-khong-ton-tai`, server trả về `"Message": "Không có dữ liệu hoặc bạn không có quyền xem dữ liệu", "Data": []`.
  - Toàn bộ dữ liệu thật đã được đồng bộ vào `compare-dim-latest.json` và Viewer cổng 8932.

''' + insert_marker

text = text.replace(insert_marker, new_content, 1)

with open('WORKSPACE_PROGRESS.md', 'w', encoding='utf-8-sig') as f:
    f.write(text)

print('Updated WORKSPACE_PROGRESS.md successfully.')
