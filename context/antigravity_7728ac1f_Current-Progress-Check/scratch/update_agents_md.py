with open('AGENTS.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith("- **12. Đồng Bộ & Dập Khuôn Thông Minh Hằng Ngày Lúc 17:00"):
        new_lines.append("- **12. Đồng Bộ & Dập Khuôn Thông Minh Hằng Ngày Lúc 17:00 (Daily Commit Sync & Smart Replication):** Đã thiết lập Cron Job định kỳ 17:00 hằng ngày tự động kéo nhánh `dev` mới nhất của các repo tham chiếu: `cci-hrm-web`, `cci-mbm-web`, `cci-timekeeping-web`, `cci-supplier-web`, và `cci-common-web`. Trích xuất các commit fix bug / migration build mới nhất, phân tích gom nhóm giải pháp kỹ thuật và đối chiếu với 3 portal đang thao tác (`cci-dc-web`, `cci-store-location-web`, `cci-scm-web`). Chỉ dập khuôn các giải pháp kỹ thuật đã kiểm chứng chuẩn mực (Redis DataProtection, URL normalize, Excel export sạch không BOM, ApiHelper 204 guard, EPPlus validation order), tránh dập khuôn mù quáng gây xung đột môi trường.\n")
        new_lines.append("- **13. Kiểm Thử Nghiệm Thu Mục Tiêu Sau Khi Dập Khuôn (Targeted Test Impact Analysis):** Sau mỗi lần dập khuôn và push code lên bất kỳ portal nào (ví dụ `cci-store-location-web`, `cci-dc-web`, `cci-scm-web`), BẮT BUỘC kích hoạt chạy lại test case nghiệm thu cho đúng phần dập khuôn đó. TUYỆT ĐỐI KHÔNG chạy lại toàn bộ test suite từ đầu gây lãng phí thời gian và nghẽn hệ thống. Phải phân tích rõ phần dập khuôn ảnh hưởng đến chức năng/module nào (ví dụ: dập khuôn Redis Session/DataProtection/Auth thì kích hoạt test các luồng Auth, Session, Home và tải API; dập khuôn xuất Excel thì kích hoạt test các ca Export/Import; dập khuôn ApiHelper thì kích hoạt test các màn gọi API tương ứng) và chỉ chạy các test spec mục tiêu đó để xác nhận hệ thống vận hành trơn tru.\n")
    else:
        new_lines.append(line)

with open('AGENTS.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("AGENTS.md updated successfully")
