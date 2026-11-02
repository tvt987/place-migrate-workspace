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
import glob
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

def extract_for_portal(portal_name, xml_rel_path, root_slug_map, custom_screen_rules=None, allowed_groups=None):
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
        if allowed_groups and r_slug not in allowed_groups:
            r_slug = "he-thong"
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

    screens = set()
    
    # 1. Get screens from 03_qa/e2e/ test directory
    e2e_dir = os.path.join(portal_dir, '03_qa', 'e2e')
    if os.path.exists(e2e_dir):
        for sf in glob.glob(os.path.join(e2e_dir, '**', '*.spec.ts'), recursive=True):
            rel = os.path.relpath(sf, e2e_dir)
            screen_slug = os.path.dirname(rel).replace('\\', '/').strip('/')
            if not screen_slug:
                screen_slug = os.path.splitext(os.path.basename(rel))[0]
                screen_slug = re.sub(r'\.(e2e\.)?spec$', '', screen_slug)
            if screen_slug:
                screens.add(screen_slug)

    # 2. Get all screens from compare-dim-latest.json
    dim_path = os.path.join(portal_dir, '03_qa', 'reports', 'details', 'compare-dim-latest.json')
    if os.path.exists(dim_path):
        with open(dim_path, 'r', encoding='utf-8-sig') as f:
            d = json.load(f)
            for t in d.get('tests', []):
                s = t.get('screen')
                if s:
                    screens.add(s)

    # 3. Get all screens from portal-screen-catalog.json
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
            group_id = matched[0]
            if allowed_groups and group_id not in allowed_groups:
                group_id = "he-thong"
            screen_menu_map[sc] = group_id
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
    place_allowed = {'mat-bang', 'danh-gia', 'phan-cong', 'phan-quyen', 'dia-danh', 'tien-ich', 'he-thong'}
    place_rules = {
        # System screens
        r"^(login|home|error-pages|cache-storerages|cache-manager)": ("he-thong", "Hệ thống"),
        r"^home$": ("he-thong", "Trang chủ Quản lý Mặt bằng"),
        r"^login$": ("he-thong", "Đăng nhập SSO"),
        r"^error-pages$": ("he-thong", "Trang thông báo lỗi"),
        r"^cache-": ("he-thong", "Quản lý Cache"),

        # Mặt bằng & Hợp đồng
        r"^location-list": ("mat-bang", "Danh sách mặt bằng"),
        r"^location-add": ("mat-bang", "Thêm mới mặt bằng"),
        r"^location-edit": ("mat-bang", "Chỉnh sửa mặt bằng"),
        r"^location-detail": ("mat-bang", "Chi tiết mặt bằng"),
        r"^location-refer": ("mat-bang", "Mặt bằng tham khảo"),
        r"^location-signed": ("mat-bang", "Mặt bằng ký thành công"),
        r"^location-status": ("mat-bang", "Trạng thái mặt bằng"),
        r"^location-type": ("mat-bang", "Loại mặt bằng"),
        r"^location-action": ("mat-bang", "Hoạt động mặt bằng"),
        r"^contract-status": ("mat-bang", "Tình trạng hợp đồng"),
        r"^leasing-status": ("mat-bang", "Tình trạng cho thuê"),
        r"^place-list": ("mat-bang", "Quản lý mặt bằng"),
        r"^place-add": ("mat-bang", "Thêm mới mặt bằng (v2)"),
        r"^place-edit": ("mat-bang", "Chỉnh sửa mặt bằng (v2)"),
        r"^place-detail": ("mat-bang", "Chi tiết mặt bằng (v2)"),
        r"^place-status": ("mat-bang", "Trạng thái mặt bằng (v2)"),
        r"^place-type": ("mat-bang", "Loại mặt bằng (v2)"),
        r"^population-density": ("mat-bang", "Mật độ dân số khu vực"),
        r"^scope-list": ("mat-bang", "Danh sách phạm vi"),
        r"^scope-add": ("mat-bang", "Thêm mới phạm vi"),
        r"^scope-edit": ("mat-bang", "Chỉnh sửa phạm vi"),
        r"^scope-status$": ("mat-bang", "Trạng thái phạm vi"),
        r"^scope-temp": ("mat-bang", "Phạm vi tạm thời"),

        # Đánh giá & Khảo sát
        r"^scope-review-file": ("danh-gia", "Hồ sơ khảo sát phạm vi"),
        r"^scope-status-file": ("danh-gia", "Hồ sơ trạng thái khảo sát"),
        r"^scope-late-reason": ("danh-gia", "Lý do trễ hạn khảo sát"),
        r"^scope-type-rank": ("danh-gia", "Xếp hạng loại mặt bằng"),
        r"^user-review-rank": ("danh-gia", "Đánh giá năng lực khảo sát"),
        r"^scope-user-report": ("danh-gia", "Báo cáo khảo sát nhân viên"),

        # Phân công nhiệm vụ & KPI mục tiêu
        r"^scope-target-yearly": ("phan-cong", "Mục tiêu phạm vi theo năm"),
        r"^scope-target-monthly": ("phan-cong", "Target nhân viên theo tháng"),
        r"^target-yearly": ("phan-cong", "Target nhân viên theo năm"),
        r"^work-goals-by-month": ("phan-cong", "Kế hoạch mục tiêu theo tháng"),
        r"^quantity-kpi-location-rent": ("phan-cong", "KPI số lượng mặt bằng thuê"),
        r"^quantity-user-target": ("phan-cong", "Chỉ tiêu số lượng nhân viên"),
        r"^province-employee-target": ("phan-cong", "Chỉ tiêu nhân viên theo tỉnh thành"),

        # Phân quyền & Phê duyệt
        r"^place-role-user": ("phan-quyen", "Phân quyền vai trò nhân viên"),
        r"^place-role$": ("phan-quyen", "Phân quyền vai trò mặt bằng"),
        r"^role-list": ("phan-quyen", "Danh sách vai trò"),
        r"^user-authorize": ("phan-quyen", "Phân quyền người dùng & chức năng"),

        # Tuyến đường & Địa danh
        r"^district-summary": ("dia-danh", "Tổng quan quận huyện"),
        r"^ward-detail": ("dia-danh", "Chi tiết phường xã"),
        r"^street-list": ("dia-danh", "Danh sách tuyến đường"),
        r"^route-list": ("dia-danh", "Danh sách tuyến đường khảo sát"),
        r"^route-edit": ("dia-danh", "Thiết lập tuyến đường khảo sát"),

        # Tiện ích
        r"^utility": ("tien-ich", "Tiện ích mở rộng"),
        r"^refer-system": ("tien-ich", "Hệ thống thông tin tham chiếu")
    }
    extract_for_portal('cci-store-location-web', '02_target/CoC.Web.Place/Menu/xmlMenuFiles.xml', place_roots, place_rules, place_allowed)

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
    scm_allowed = {'xuat-hang', 'nhap-hang', 'chuyen-kho', 'dong-tien', 'yctt', 'khuyen-mai', 'tien-ich', 'he-thong'}
    scm_rules = {
        # System screens
        r"^(login|home|cache-storerages|output-caches)": ("he-thong", "Hệ thống"),
        r"^home$": ("he-thong", "Trang chủ Hệ thống SCM"),
        r"^login$": ("he-thong", "Đăng nhập SSO"),
        r"^cache-storerages-create-cache-js": ("he-thong", "Tạo Cache Javascript"),
        r"^cache-storerages": ("he-thong", "Quản lý Cache Storage"),
        r"^output-caches": ("he-thong", "Quản lý Output Cache"),

        # Xuất hàng
        r"^output-orders-create-multi": ("xuat-hang", "Tạo nhiều phiếu xuất"),
        r"^output-orders-create-return-supplier": ("xuat-hang", "Tạo phiếu xuất trả NCC"),
        r"^output-order-destroys-create": ("xuat-hang", "Tạo phiếu xuất hủy hàng"),
        r"^output-order-destroys-edit": ("xuat-hang", "Chi tiết phiếu xuất hủy hàng"),
        r"^output-order-destroys": ("xuat-hang", "Xuất hủy hàng hóa"),
        r"^output-sale-clear-stock4-bdl-ts-edit": ("xuat-hang", "Chi tiết xuất thanh lý hàng tồn"),
        r"^output-sale-clear-stock4-bdl-ts": ("xuat-hang", "Xuất bán thanh lý hàng tồn"),
        r"^output-sale-qr-pays": ("xuat-hang", "Xuất bán thanh toán QR"),
        r"^output-sale-support-requests": ("xuat-hang", "Yêu cầu hỗ trợ bán hàng"),
        r"^output-sales": ("xuat-hang", "Xuất bán hàng"),
        r"^output-types": ("xuat-hang", "Loại phiếu xuất hàng"),
        r"^output-uses-create": ("xuat-hang", "Tạo mục đích xuất hàng"),
        r"^output-uses-edit": ("xuat-hang", "Sửa mục đích xuất hàng"),
        r"^output-uses": ("xuat-hang", "Mục đích sử dụng xuất hàng"),
        r"^bonus-output": ("xuat-hang", "Xuất thưởng NCC"),

        # Chuyển kho & Điều phối
        r"^x-store-changes-create": ("chuyen-kho", "Tạo phiếu chuyển kho"),
        r"^x-store-changes-edit": ("chuyen-kho", "Chỉnh sửa phiếu chuyển kho"),
        r"^x-store-changes": ("chuyen-kho", "Phiếu chuyển kho nội bộ"),
        r"^x-store-change-d-cs-create": ("chuyen-kho", "Tạo phiếu chuyển kho đến DC"),
        r"^x-store-change-d-cs-edit": ("chuyen-kho", "Chỉnh sửa phiếu chuyển kho đến DC"),
        r"^x-store-change-d-cs": ("chuyen-kho", "Phiếu chuyển kho đến DC"),
        r"^err-des-storechanges-create": ("chuyen-kho", "Tạo biên bản lỗi điều chuyển"),
        r"^err-des-storechanges-edit": ("chuyen-kho", "Chỉnh sửa biên bản lỗi điều chuyển"),
        r"^err-des-storechanges": ("chuyen-kho", "Lỗi điều chuyển cửa hàng"),
        r"^confirm-gs-ms": ("chuyen-kho", "Duyệt yêu cầu chuyển kho GSM"),
        r"^confirm-s-cs": ("chuyen-kho", "Duyệt yêu cầu chuyển kho SCS"),

        # Dòng tiền & Đối soát
        r"^e-wallet-debits": ("dong-tien", "Công nợ ví điện tử"),
        r"^payment-collection-accounts": ("dong-tien", "Tài khoản đối tác thu hộ"),
        r"^payment-receipt-partners": ("dong-tien", "Đối tác thanh toán thu chi"),
        r"^voucher-receipt-in-store-reconciles": ("dong-tien", "Đối soát chứng từ voucher tại cửa hàng"),

        # Khuyến mại & Vouchers
        r"^category_store-exclusions": ("khuyen-mai", "Ngành hàng không áp dụng khuyến mại theo shop"),
        r"^cnb-groups": ("khuyen-mai", "Nhóm chương trình khuyến mại CNB"),
        r"^cnb-types": ("khuyen-mai", "Loại hình khuyến mại CNB"),
        r"^customer-clear-stocks": ("khuyen-mai", "Khách hàng mua hàng thanh lý"),
        r"^io-voucher-change-create": ("khuyen-mai", "Đổi voucher khuyến mại"),
        r"^ipos-voucher-histories": ("khuyen-mai", "Lịch sử phát hành voucher IPOS"),
        r"^ipos-voucher-types": ("khuyen-mai", "Loại voucher IPOS"),
        r"^journeys": ("khuyen-mai", "Hành trình mua sắm & Ưu đãi"),
        r"^member-packages": ("khuyen-mai", "Gói thành viên & Ưu đãi"),
        r"^mini-game-details": ("khuyen-mai", "Chương trình minigame ưu đãi"),
        r"^os-lucky-draw-thanks-brands": ("khuyen-mai", "Vòng quay may mắn tri ân nhãn hàng"),
        r"^product-area-exclusions": ("khuyen-mai", "Sản phẩm loại trừ theo khu vực"),
        r"^product-category-g-ms": ("khuyen-mai", "Nhóm ngành hàng khuyến mại GM"),
        r"^product-g-ms": ("khuyen-mai", "Sản phẩm quà tặng GM"),
        r"^product-gift-cn-bs-create": ("khuyen-mai", "Thêm mới quà tặng CNB"),
        r"^product-gift-cn-bs": ("khuyen-mai", "Quà tặng chương trình CNB"),
        r"^product-gift-cnb-categories": ("khuyen-mai", "Danh mục quà tặng CNB"),
        r"^product-gift-cnb-products-create": ("khuyen-mai", "Thêm sản phẩm quà tặng CNB"),
        r"^product-gift-cnb-products": ("khuyen-mai", "Sản phẩm quà tặng CNB"),
        r"^product-gm-error-logs": ("khuyen-mai", "Nhật ký lỗi khuyến mại GM"),
        r"^product-store-size-exclusions": ("khuyen-mai", "Sản phẩm loại trừ theo quy mô shop"),

        # Tiện ích & Báo cáo
        r"^take-inventory-cc-apps-edit": ("chuyen-kho", "Chỉnh sửa kiểm kê kho CC App"),
        r"^take-inventory-cc-apps": ("chuyen-kho", "Kiểm kê kho CC App"),
        r"^output-sale-charities": ("xuat-hang", "Xuất bán hàng từ thiện"),
        r"^popup-action-types": ("tien-ich", "Cửa sổ Loại hoạt động"),
        r"^popup-actions": ("tien-ich", "Cửa sổ Hoạt động"),
        r"^popup-black-list-customers": ("tien-ich", "Cửa sổ Khách hàng hạn chế"),
        r"^popup-bonus-point-types": ("tien-ich", "Cửa sổ Loại điểm thưởng"),
        r"^popup-categories": ("tien-ich", "Cửa sổ Danh mục ngành hàng"),
        r"^popup-customers": ("tien-ich", "Cửa sổ Tra cứu khách hàng"),
        r"^popup-memberships": ("tien-ich", "Cửa sổ Gói thành viên"),
        r"^popup-products": ("tien-ich", "Cửa sổ Tra cứu sản phẩm"),
        r"^popup-promotions": ("tien-ich", "Cửa sổ Chương trình khuyến mại"),
        r"^popups": ("tien-ich", "Cửa sổ tra cứu chung"),
        r"^activities-create": ("tien-ich", "Tạo chương trình hoạt động"),
        r"^activities": ("tien-ich", "Chương trình hoạt động"),
        r"^pos-ms-create-multi": ("tien-ich", "Thêm hàng loạt máy POS"),
        r"^pos-ms-create": ("tien-ich", "Thêm mới máy POS"),
        r"^pos-ms": ("tien-ich", "Danh sách máy POS"),
        r"^product-top-store": ("tien-ich", "Top sản phẩm bán chạy cửa hàng"),
        r"^sale-kpi-store-results": ("tien-ich", "Kết quả KPI bán hàng cửa hàng"),
        r"^sale-kp-is": ("tien-ich", "Chỉ tiêu KPI bán hàng"),
        r"^store-device-i-ps": ("tien-ich", "IP thiết bị cửa hàng"),
        r"^store-i-ps": ("tien-ich", "Địa chỉ IP cửa hàng")
    }
    extract_for_portal('cci-scm-web', '02_target/CoC.Web.SCM/Menu/xmlMenuFiles.xml', scm_roots, scm_rules, scm_allowed)

    # 3. Income Web
    income_roots = {
        "1": "bao-cao-dashboard",
        "2000": "bao-cao-dashboard",
        "3000": "bao-cao-dashboard",
        "4000": "bao-cao-dashboard",
        "5000": "bao-cao-dashboard",
        "6000": "bao-cao-dashboard"
    }
    income_allowed = {'bao-cao-dashboard', 'he-thong'}
    income_rules = {
        r"^dashboards$": ("bao-cao-dashboard", "Dashboard Tổng quan Doanh thu"),
        r"^dashboards-detail-voucher$": ("bao-cao-dashboard", "Chi tiết Voucher Doanh thu"),
        r"^dashboards-detail-voucher-cate$": ("bao-cao-dashboard", "Chi tiết Ngành hàng Voucher"),
        r"^dashboards-monthly-voucher$": ("bao-cao-dashboard", "Voucher Doanh thu theo tháng"),
        r"^dashboards-monthly-voucher-sal-group$": ("bao-cao-dashboard", "Doanh thu theo nhóm bán hàng"),
        r"^dashboards-salary-daily$": ("bao-cao-dashboard", "Thu nhập hàng ngày nhân viên"),
        r"^cache-storerages$": ("he-thong", "Quản lý Cache Storage"),
        r"^error-pages$": ("he-thong", "Trang thông báo lỗi"),
        r"^home$": ("he-thong", "Trang chủ Doanh thu"),
        r"^login$": ("he-thong", "Đăng nhập Hệ thống")
    }
    extract_for_portal('cci-income-web', '02_target/CoC.Web.INC/Menu/xmlMenuFiles.xml', income_roots, income_rules, income_allowed)

if __name__ == '__main__':
    main()
