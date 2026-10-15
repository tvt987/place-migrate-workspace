import os
import subprocess
import sys
import json

# Danh sách các màn đã chạy ở Wave A, B, C, D (không cần chạy lại)
ALREADY_TESTED = {
    'login', 'home', 'journeys',
    'output-orders', 'purchase-orders', 'store-change-requests', 'input-orders', 'invoices'
}

def get_remaining_screens():
    e2e_dir = os.path.join(os.getcwd(), 'e2e')
    folders = sorted(os.listdir(e2e_dir))
    remaining = []
    for f in folders:
        spec_path = os.path.join(e2e_dir, f, f"{f}.e2e.spec.ts")
        if os.path.exists(spec_path) and f not in ALREADY_TESTED:
            remaining.append((f, spec_path))
    return remaining

if __name__ == '__main__':
    screens = get_remaining_screens()
    print(f"Total remaining screens for Wave E: {len(screens)}")
    # In ra 10 màn đầu tiên để kiểm tra thứ tự
    for name, path in screens[:10]:
        print(f" - {name}")
