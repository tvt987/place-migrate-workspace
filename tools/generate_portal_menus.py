#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trích xuất và chuẩn hóa menu từ xmlMenuFiles.xml sang screen-menu.json và screen-titles.json
theo đúng tiêu chuẩn DC Web Gold Standard cho:
- cci-store-location-web
- cci-scm-web
- cci-income-web
"""

import os
import sys
import json
import re
import xml.etree.ElementTree as ET

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

WORKSPACE_DIR = r'e:\Work\Place_Migrate'

def slugify(text):
    t = text.lower()
    t = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', t)
    t = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', t)
    t = re.sub(r'[ìíịỉĩ]', 'i', t)
    t = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', t)
    t = re.sub(r'[ùúụủũưừứựửữ]', 'u', t)
    t = re.sub(r'[ỳýỵỷỹ]', 'y', t)
    t = re.sub(r'[đ]', 'd', t)
    t = re.sub(r'[^a-z0-9]+', '-', t)
    return t.strip('-')

def camel_to_kebab(s):
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s)
    return s.lower()

def extract_for_portal(portal_name, xml_rel_path, root_slug_map, custom_screen_rules=None):
    portal_dir = os.path.join(WORKSPACE_DIR, portal_name)
    xml_path = os.path.join(portal_dir, xml_rel_path)
    config_dir = os.path.join(portal_dir, '03_qa', 'config')
    os.makedirs(config_dir, exist_ok=True)
    
    out_menu_json = os.path.join(config_dir, 'screen-menu.json')
    out_titles_json = os.path.join(config_dir, 'screen-titles.json')
    
    print(f"\n==========================================")
    print(f"[*] Processing Portal: {portal_name}")
    print(f"    XML Path: {xml_path}")
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    menus = []
    for m in root.findall('Menu'):
        mid = (m.findtext('MenuID') or '').strip()
        pid = (m.findtext('ParentID') or '').strip()
        title = (m.findtext('Title') or '').strip()
        ctrl = (m.findtext('Controller') or '').strip()
        act = (m.findtext('Action') or '').strip()
        bc = (m.findtext('BreadCrumbDefaultLink') or '').strip()
        menus.append({
            'id': mid,
            'parent': pid,
            'title': title,
            'controller': ctrl,
            'action': act,
            'breadcrumb': bc
        })
        
    parent_map = {m['id']: m for m in menus}
    
    def get_root_menu(mid):
        curr = parent_map.get(mid)
        while curr and curr['parent'] != '0':
            p = parent_map.get(curr['parent'])
            if not p:
                break
            curr = p
        return curr

    # Build action/breadcrumb lookup
    # key: normalized kebab string -> (root_slug, title)
    lookup = {}
    for m in menus:
        rm = get_root_menu(m['id'])
        if not rm:
            continue
        r_id = rm['id']
        r_slug = root_slug_map.get(r_id, slugify(rm['title']))
        title = m['title']
        
        candidates = []
        for path_str in [m['action'], m['breadcrumb']]:
            if path_str and path_str != '#':
                clean = path_str.strip('/').split('?')[0]
                candidates.append(clean)
                parts = clean.split('/')
                # add controller only
                if parts:
                    candidates.append(parts[0])
                # add full path as kebab
                kebab_path = '-'.join(camel_to_kebab(p) for p in parts)
                candidates.append(kebab_path)
        
        for cand in candidates:
            k = cand.lower().replace('/', '-').replace('_', '-')
            k = re.sub(r'-+', '-', k).strip('-')
            if k and (k not in lookup or len(title) > len(lookup[k][1])):
                lookup[k] = (r_slug, title)

    # Get all screens from compare-dim-latest.json
    dim_path = os.path.join(portal_dir, '03_qa', 'reports', 'details', 'compare-dim-latest.json')
    screens = set()
    if os.path.exists(dim_path):
        with open(dim_path, 'r', encoding='utf-8-sig') as f:
            d = json.load(f)
            for t in d.get('tests', []):
                s = t.get('screen')
                if s:
                    screens.add(s)

    # Also get all screens from portal-screen-catalog.json
    cat_path = os.path.join(portal_dir, '03_qa', 'portal-screen-catalog.json')
    if os.path.exists(cat_path):
        with open(cat_path, 'r', encoding='utf-8-sig') as f:
            d = json.load(f)
            for s in d.get('screens', []):
                k = s.get('key') or s.get('screen')
                if k:
                    screens.add(k)

    screens = sorted(list(screens))
    print(f"    Total unique screens to map: {len(screens)}")

    screen_menu_map = {
        "(unknown)": "he-thong",
        "home": "he-thong",
        "login": "he-thong",
        "error-pages": "he-thong"
    }
    screen_titles_map = {
        "(unknown)": "Chung / SSO",
        "home": "Trang chủ",
        "login": "Đăng nhập",
        "error-pages": "Trang thông báo lỗi"
    }

    unmapped = []
    for sc in screens:
        norm_sc = sc.lower().replace('/', '-').replace('_', '-')
        norm_sc = re.sub(r'-+', '-', norm_sc).strip('-')
        
        # Check custom rules first
        matched = None
        if custom_screen_rules:
            for pattern, (c_slug, c_title) in custom_screen_rules.items():
                if re.search(pattern, sc, re.IGNORECASE):
                    matched = (c_slug, c_title)
                    break
                    
        # Check direct lookup
        if not matched and norm_sc in lookup:
            matched = lookup[norm_sc]
            
        # Check base screen without -create/-edit/-detail
        if not matched:
            base_sc = re.sub(r'-(create|edit|detail|import|view).*$', '', norm_sc)
            if base_sc in lookup:
                r_slug, orig_title = lookup[base_sc]
                suffix = "Tạo mới " if "create" in sc else ("Cập nhật " if "edit" in sc else ("Nhập Excel " if "import" in sc else ""))
                matched = (r_slug, f"{suffix}{orig_title}")

        # Check partial matching against lookup keys
        if not matched:
            best_match = None
            best_len = 0
            for lk, (r_slug, l_title) in lookup.items():
                if len(lk) >= 4 and (lk in norm_sc or norm_sc.startswith(lk)):
                    if len(lk) > best_len:
                        best_len = len(lk)
                        best_match = (r_slug, l_title)
            if best_match:
                matched = best_match

        if matched:
            screen_menu_map[sc] = matched[0]
            screen_titles_map[sc] = matched[1]
        else:
            # Fallback
            screen_menu_map[sc] = "he-thong"
            screen_titles_map[sc] = sc.replace('-', ' ').title()
            unmapped.append(sc)

    print(f"    Mapped: {len(screens) - len(unmapped)} | Unmapped (fallback): {len(unmapped)}")
    if unmapped:
        print(f"    Sample unmapped: {unmapped[:5]}")

    # Write files with UTF-8 BOM
    with open(out_menu_json, 'w', encoding='utf-8-sig', newline='') as f:
        json.dump(screen_menu_map, f, indent=2, ensure_ascii=False)
        
    with open(out_titles_json, 'w', encoding='utf-8-sig', newline='') as f:
        json.dump(screen_titles_map, f, indent=2, ensure_ascii=False)

    print(f"    Saved: {out_menu_json}")
    print(f"    Saved: {out_titles_json}")
    return screen_menu_map, screen_titles_map


def main():
    # 1. Store Location
    place_roots = {
        "01": "mat-bang",
        "03": "danh-gia",
        "04": "phan-cong",
        "05": "phan-quyen",
        "10": "tien-ich",
        "11": "dia-danh"
    }
    place_rules = {
        r"location-list": ("mat-bang", "Danh sách mặt bằng"),
        r"location-add": ("mat-bang", "Thêm mới mặt bằng"),
        r"location-edit": ("mat-bang", "Chỉnh sửa mặt bằng"),
        r"location-detail": ("mat-bang", "Chi tiết mặt bằng"),
        r"location-refer": ("mat-bang", "Mặt bằng tham khảo"),
        r"location-signed": ("mat-bang", "Mặt bằng ký thành công"),
        r"scope-list": ("mat-bang", "Danh sách phạm vi"),
        r"scope-research": ("mat-bang", "Phạm vi tìm hiểu"),
        r"scope-target-yearly": ("phan-cong", "Mục tiêu theo năm"),
        r"scope-target-monthly": ("phan-cong", "Target nhân viên theo tháng"),
        r"target-yearly": ("phan-cong", "Target nhân viên theo năm"),
        r"place-role-user": ("phan-quyen", "Vai trò theo nhân viên"),
        r"role-list": ("phan-quyen", "Danh sách vai trò"),
        r"contract-status": ("mat-bang", "Danh sách tình trạng hợp đồng"),
        r"leasing-status": ("mat-bang", "Danh sách tình trạng cho thuê"),
        r"location-status": ("mat-bang", "Danh sách trạng thái mặt bằng"),
        r"location-type": ("mat-bang", "Danh sách loại mặt bằng"),
        r"location-action": ("mat-bang", "Danh sách hoạt động mặt bằng"),
        r"population-density": ("mat-bang", "Mật độ dân số"),
        r"district-summary": ("dia-danh", "Tổng quan quận huyện"),
        r"ward-detail": ("dia-danh", "Chi tiết phường xã"),
        r"street-list": ("dia-danh", "Danh sách tuyến đường"),
        r"cache-storerages": ("he-thong", "Quản lý Cache"),
        r"cache-manager": ("he-thong", "Quản lý Cache")
    }
    extract_for_portal('cci-store-location-web', '02_target/CoC.Web.Place/Menu/xmlMenuFiles.xml', place_roots, place_rules)

    # 2. SCM Web
    scm_roots = {
        "1": "xuat-hang",
        "2000": "nhap-hang",
        "3000": "chuyen-kho",
        "4000": "dong-tien",
        "7000": "yctt",
        "5000": "khuyen-mai",
        "6000": "tien-ich"
    }
    scm_rules = {
        r"bonus-output": ("xuat-hang", "Xuất thưởng NCC"),
        r"output-orders": ("xuat-hang", "Phiếu xuất hàng"),
        r"input-orders": ("nhap-hang", "Phiếu nhập hàng"),
        r"purchase-orders": ("nhap-hang", "Đơn đặt hàng mua (PO)"),
        r"sale-orders": ("xuat-hang", "Đơn hàng bán"),
        r"transfers": ("chuyen-kho", "Điều phối chuyển kho"),
        r"inventory": ("chuyen-kho", "Quản lý tồn kho"),
        r"promotions": ("khuyen-mai", "Chương trình khuyến mãi"),
        r"mini-games": ("khuyen-mai", "Mini Game & Sự kiện"),
        r"vouchers": ("khuyen-mai", "Quản lý Voucher"),
        r"cash-flow": ("dong-tien", "Dòng tiền & Kế toán"),
        r"accounting": ("dong-tien", "Quy trình kế toán"),
        r"customer-taxes": ("dong-tien", "Thuế khách hàng"),
        r"cache-manager": ("he-thong", "Quản lý Cache"),
        r"cache-storerages": ("he-thong", "Quản lý Cache Storage")
    }
    extract_for_portal('cci-scm-web', '02_target/CoC.Web.SCM/Menu/xmlMenuFiles.xml', scm_roots, scm_rules)

    # 3. Income Web
    income_roots = {
        "1": "bao-cao-dashboard",
        "2000": "bao-cao-dashboard",
        "3000": "bao-cao-dashboard",
        "4000": "bao-cao-dashboard",
        "5000": "bao-cao-dashboard",
        "6000": "bao-cao-dashboard"
    }
    income_rules = {
        r"dashboards$": ("bao-cao-dashboard", "Dashboard Tổng quan Doanh thu"),
        r"dashboards-detail-voucher": ("bao-cao-dashboard", "Chi tiết Voucher Doanh thu"),
        r"dashboards-detail-voucher-cate": ("bao-cao-dashboard", "Chi tiết Ngành hàng Voucher"),
        r"dashboards-monthly-voucher": ("bao-cao-dashboard", "Voucher Doanh thu theo tháng"),
        r"dashboards-monthly-voucher-sal-group": ("bao-cao-dashboard", "Doanh thu theo nhóm bán hàng"),
        r"dashboards-salary-daily": ("bao-cao-dashboard", "Thu nhập hàng ngày nhân viên"),
        r"cache-storerages": ("he-thong", "Quản lý Cache Storage"),
        r"debug-dp": ("he-thong", "Kiểm tra DataProtection"),
        r"home": ("he-thong", "Trang chủ Doanh thu"),
        r"login": ("he-thong", "Đăng nhập Hệ thống")
    }
    extract_for_portal('cci-income-web', '02_target/CoC.Web.INC/Menu/xmlMenuFiles.xml', income_roots, income_rules)

if __name__ == '__main__':
    main()
