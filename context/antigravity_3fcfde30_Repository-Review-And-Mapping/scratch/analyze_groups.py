import json
import sys

def main():
    with open(r'E:\Work\Place_Migrate\cci-scm-web\03_qa\reports\details\parity-summary.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    regressions = data.get('regressions', [])
    print(f'Total regressions: {len(regressions)}')

    categories = {}
    for r in regressions:
        stg4_status = r.get('stg4_status', '')
        stg10_status = r.get('stg10_status', '')
        stg10_err = r.get('stg10_error', '') or ''
        screen = r.get('screen', '')
        tc = r.get('tc', '')
        
        if stg10_status == 'skipped':
            cat = 'STG10 Skipped (Điều kiện tiền đề/seed data không thoả trên STG10)'
        elif 'timeout' in stg10_err.lower() or 'timedout' in stg10_status.lower():
            cat = 'Timeout (Chờ API/grid load quá 30s-120s)'
        elif '500' in stg10_err or 'internal server error' in stg10_err.lower():
            cat = 'HTTP 500 (Lỗi code backend/API/ModelBinding)'
        elif 'expect' in stg10_err.lower() or 'assert' in stg10_err.lower():
            cat = 'UI Assertion / Selector (Grid render lệch cấu trúc hoặc thiếu row)'
        else:
            cat = f'Khác ({stg10_status})'
            
        categories.setdefault(cat, []).append(r)

    for cat, items in sorted(categories.items()):
        print(f'\n=== {cat} ({len(items)} ca) ===')
        screens = sorted(set(x.get('screen', '') for x in items))
        print(f'Số màn hình bị ảnh hưởng: {len(screens)}')
        print('Các màn hình tiêu biểu:', ', '.join(screens[:10]))
        for item in items[:4]:
            err_short = (item.get('stg10_error') or '').strip().split('\n')[0][:100]
            print(f"  - [{item.get('screen')}] {item.get('tc')}: STG4={item.get('stg4_status')} -> STG10={item.get('stg10_status')} | {err_short}")

if __name__ == '__main__':
    main()
