import os
import json
import subprocess
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

WORKSPACE_DIR = r'e:\Work\Place_Migrate'

def enrich_portal(portal):
    portal_dir = os.path.join(WORKSPACE_DIR, portal)
    menu_path = os.path.join(portal_dir, '03_qa', 'config', 'screen-menu.json')
    if not os.path.exists(menu_path):
        print(f"[-] No screen-menu.json for {portal}")
        return

    with open(menu_path, 'r', encoding='utf-8-sig') as f:
        menu_map = json.load(f)

    details_dir = os.path.join(portal_dir, '03_qa', 'reports', 'details')
    if not os.path.exists(details_dir):
        print(f"[-] No details dir for {portal}")
        return

    for fname in os.listdir(details_dir):
        if fname.endswith('-latest.json'):
            fpath = os.path.join(details_dir, fname)
            try:
                with open(fpath, 'r', encoding='utf-8-sig') as f:
                    data = json.load(f)

                data['screenMenuMap'] = menu_map
                # Enrich screens
                if 'screens' in data and isinstance(data['screens'], list):
                    for sc in data['screens']:
                        k = sc.get('screen') or sc.get('key') or ''
                        sc['menu'] = menu_map.get(k) or menu_map.get(k.lower()) or 'he-thong'

                # Enrich tests in compare-dim-latest
                if 'tests' in data and isinstance(data['tests'], list):
                    for t in data['tests']:
                        k = t.get('screen') or ''
                        t['menu'] = menu_map.get(k) or menu_map.get(k.lower()) or 'he-thong'

                with open(fpath, 'w', encoding='utf-8-sig', newline='\n') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"[+] Enriched {portal}: {fname}")
            except Exception as ex:
                print(f"[-] Error enriching {fpath}: {ex}")

    # Rebuild data.js
    build_script = os.path.join(portal_dir, '.report', 'viewer', 'tools', 'build_data.py')
    if os.path.exists(build_script):
        print(f"[*] Rebuilding viewer data for {portal}...")
        res = subprocess.run([sys.executable, build_script], cwd=portal_dir, capture_output=True, text=True, encoding='utf-8', errors='replace')
        print(f"    Exit code: {res.returncode}")
        if res.stdout:
            print("    " + "\n    ".join(res.stdout.strip().split('\n')[:5]))
        if res.stderr:
            print("    ERR: " + res.stderr.strip()[:200])

for p in ['cci-store-location-web', 'cci-scm-web', 'cci-income-web']:
    enrich_portal(p)
