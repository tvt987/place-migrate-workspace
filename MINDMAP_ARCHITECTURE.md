# Sơ Đồ Tư Duy & Tổng Quan Kiến Trúc — `cci-store-location-web` (CoC.Web.Place)

> **Dự án**: `cci-store-location-web` (Tên mã: `CoC.Web.Place` / `store-location-web`)  
> **Thư mục mã nguồn**: [`cci-store-location-web/`](file:///e:/Work/Place_Migrate/cci-store-location-web)  
> **Tổ chức**: Hệ thống Bán lẻ Con Cung (Nhóm: `4_STORE-LOCATION`)  
> **Mục đích**: Cổng thông tin & Web App Quản lý Mặt bằng, Khảo sát, Đàm phán và Lập kế hoạch Phát triển Chuỗi Cửa hàng Con Cung trên toàn quốc.  
> **Hiện trạng**: Đã hoàn tất nâng cấp từ **ASP.NET MVC 5 (.NET Framework 4.6.1)** sang **ASP.NET Core (.NET 10)**.

---

## 1. Sơ Đồ Tư Duy Tổng Thể (System Mindmap)

```mermaid
mindmap
  root((Store Location Web<br/>CoC.Web.Place))
    Nghiep Vu Cot Loi
      LOC - Quan Ly Mat Bang
        LocationIndex: Tra cuu, tim kiem mat bang
        LocationAdd / Edit / Detail: Ho so mat bang tiem nang
        LocationContract: Hop dong thue, gia thue, thoi han
        LocationComment / History: Nhat ky khao sat, danh gia
        LocationInfo / LocationRefer: Thong tin ky thuat, nguon gioi thieu
        LocationSigned: Mat bang da ky ket
      PLA - Ke Hoach & Pham Vi
        ScopeIndex / Add / Edit: Pham vi mo chuoi theo khu vuc
        ScopeTargetYearly: Chi tieu mo mat bang hang nam
        WorkGoalsByMonth: KPI thang cua chuyen vien mat bang
        ProvinceEmployeeTarget: Phan bo chi tieu theo tinh thanh
        RouteIndex / Edit: Lo trinh tuyen khao sat mat bang
        DistrictSummary: Tong hop mat do quan huyen
        ImportIndex: Import Excel danh sach mat bang
      MAT - Danh Muc & Tham So
        LocationStatus / LeasingStatus: Trang thai mat bang, tien do
        PlaceChainStore: Danh muc chuoi Con Cung, Toycity
        PlaceType: Loai hinh cua hang Standard, Supercenter
        PlaceRole / PlaceRole_User: Vai tro phap ly, thiet ke, PTMB
        ScopeLateReason: Danh muc ly do tre han tien do
        UtilityIndex: Tien ich ngoai khu truong hoc, cho, benh vien
      USR - Phan Quyen Dia Ban
        UserAuthorizeIndex: Ma tran phan quyen nguoi dung
        UserProvince: Phan cong nhan su theo Tinh / Thanh pho
        UserDistrict: Phan cong theo Quan / Huyen
        UserLocation: Phan cong theo Diem mat bang cu the
    Kien Truc Ky Thuat
      Frontend Layer
        AngularJS 1.x SPA
        Razor Views 220 views
        Static Assets: script-handler, content, data
        Bootstrap, jQuery, UI Select, Leaflet Map
      Backend Layer net10.0
        ASP.NET Core MVC Host
        Autofac DI Container
        Custom Compatibility Shims: LegacyJson, LegacyDateTime
        Newtonsoft JsonNetResult Serialization
        Background Service: ClientPermissionWorker
      Bao Mat & Xac Thuc
        SSO Keycloak IDS1 realm master
        OAuth2 / OIDC Authorization Code Flow
        UserSessionStore: Session Distributed Memory Cache
        MDM API: Permission ReadClient
      Du Lieu & Cache
        Khong co Database rieng
        Downstream HTTP: Store Location API ApisUrl
        HRM API: Du lieu nhan su HRMApisUrl
        Multi-Level Cache: MemoryCache + Redis Distributed
        Redis Pub/Sub Cache Invalidation
      Quan Sat & Logging
        Serilog Elasticsearch / Kibana
        NLog Local Backup
        Audit Trail & Request Tracking
    Cau Truc Thu Muc & Monorepo
      01_origin: Snapshot MVC5 net461 goc
      02_target: Ban mig net10.0 hoan thien
      04_critical_change: So issue & gap Gold-Align
      tests: Bo test 4 tang Unit, Integration, Functional, Smoke
      app.config / app.uat.config: Config tap trung Staging / UAT
      scripts: apply-env-config.py, run-origin.ps1
```

---

## 2. Sơ Đồ Kiến Trúc Hệ Thống (Architecture & Data Flow)

```mermaid
flowchart TB
    subgraph Client["Trình duyệt Người Dùng (End-User / Chuyên viên PTMB)"]
        Browser["Desktop Browser / Mobile Web<br/>(AngularJS 1.x + Razor MVC Views)"]
    end

    subgraph Host["Web Host — CoC.Web.Place (.NET 10)"]
        direction TB
        Kestrel["Kestrel Web Server<br/>Port 5305 (STG) / 4784 (UAT)"]
        
        subgraph Pipeline["ASP.NET Core Middleware Pipeline"]
            SecHeaders["Security Headers & CORS<br/>(X-Frame-Options, XSS, HSTS)"]
            StaticF["Static Files Provider<br/>(/wwwroot: script-handler, content, data)"]
            SessionM["Distributed Session<br/>(Cookie CC.SID, Memory Cache)"]
            AuthF["MvcAuthorizeAttribute Filter<br/>(Token Validation & Permission Gate)"]
        end

        subgraph Modules["Tầng Controllers (61 Controllers)"]
            AccountsC["AccountsController<br/>(Login/Callback/Logout)"]
            LocC["LOC Module<br/>(Quản lý Mặt bằng)"]
            PlaC["PLA Module<br/>(Phạm vi & Chỉ tiêu)"]
            MatC["MAT Module<br/>(Danh mục tham số)"]
            UsrC["USR Module<br/>(Phân quyền địa bàn)"]
            DirectC["Directives & Upload<br/>(Template & File Handler)"]
        end

        subgraph CoreServices["Dịch vụ Cốt lõi & Tương thích"]
            ApiH["ApiHelper & APIClient<br/>(HTTP Gateway Proxy)"]
            CacheMgr["MultiLevelCacheManager<br/>(MemoryCache + Redis)"]
            PermWorker["ClientPermissionWorker<br/>(BackgroundService)"]
            SLog["Serilog / SLogger<br/>(Structured Log)"]
        end
    end

    subgraph AuthServer["Hạ tầng Xác thực Tập trung"]
        IDS1["Keycloak IDS1 (Staging / UAT)<br/>OAuth2 / OpenID Connect"]
    end

    subgraph Downstream["Hệ sinh thái Dịch vụ Nội bộ Con Cung"]
        PlaceAPI["Store Location API<br/>(store-location-api: CRUD dữ liệu mặt bằng)"]
        MDM["MDM API<br/>(api/Permissions/ReadClient)"]
        HrmAPI["HRM API<br/>(hrm-api: Dữ liệu chuyên viên & phòng ban)"]
        RedisSrv["Redis Server<br/>(Distributed Cache & Invalidation Pub/Sub)"]
        Kibana["Elasticsearch & Kibana<br/>(Log tập trung)"]
        GCS["Google Cloud Storage / Drive<br/>(Lưu trữ hình ảnh, hồ sơ mặt bằng)"]
    end

    Browser <-->|HTTP / HTTPS| Kestrel
    Kestrel --> Pipeline --> Modules
    Modules --> CoreServices

    AccountsC <-->|OAuth2 Auth Code| IDS1
    PermWorker <-->|Token & Permissions| MDM
    ApiH <-->|JSON over HTTP| PlaceAPI
    ApiH <-->|JSON over HTTP| HrmAPI
    CacheMgr <-->|StackExchange.Redis| RedisSrv
    SLog -->|Elasticsearch Sink| Kibana
    DirectC <-->|Upload file| GCS
```

---

## 3. Bản Đồ Phân Hệ Nghiệp Vụ (Business Domain Matrix)

Hệ thống được tổ chức nhất quán theo **4 phân hệ nghiệp vụ chính**, xuyên suốt từ Frontend (`script-handler/`), Controllers, Request/Response DTO cho đến `ObjectCore`:

| Phân hệ | Tên Đầy Đủ | Nhiệm Vụ Nghiệp Vụ Chính | Các Controller Tiêu Biểu |
|---|---|---|---|
| **LOC** | **Location Management**<br/>(Quản lý Mặt bằng) | Quản lý vòng đời mặt bằng: tìm kiếm, thẩm định kỹ thuật, đàm phán giá thuê, ký hợp đồng, lưu trữ lịch sử khảo sát và đánh giá thực địa. | `LocationIndex`, `LocationAdd`, `LocationEdit`, `LocationDetail`, `LocationContract`, `LocationComment`, `LocationHistory`, `LocationInfo`, `LocationSigned` |
| **PLA** | **Planning & Scope**<br/>(Kế hoạch & Phạm vi) | Lập kế hoạch mở rộng chuỗi cửa hàng, quản lý phạm vi mở mới (Scope), giao chỉ tiêu KPI mở điểm từng tháng cho nhân viên, quản lý lộ trình khảo sát và import Excel hàng loạt. | `ScopeIndex`, `ScopeAdd`, `ScopeEdit`, `ScopeTargetYearly`, `WorkGoalsByMonth`, `ProvinceEmployeeTarget`, `RouteIndex`, `DistrictSummary`, `ImportIndex` |
| **MAT** | **Master Data**<br/>(Danh mục & Tham số) | Quản lý toàn bộ danh mục metadata hỗ trợ vận hành: trạng thái mặt bằng, loại hình cửa hàng (Standard/Supercenter), xếp hạng quy mô, lý do trễ hạn mở điểm, danh mục tiện ích xung quanh. | `LocationStatusIndex`, `LocationTypeIndex`, `PlaceChainStoreIndex`, `PlaceTypeIndex`, `PlaceRoleController`, `ScopeLateReasonController`, `UtilityIndex` |
| **USR** | **User & Territory**<br/>(Phân quyền Địa bàn) | Ma trận phân quyền kiểm soát dữ liệu theo khu vực địa lý: gán chuyên viên phụ trách theo Tỉnh/Thành phố, Quận/Huyện hoặc địa điểm cụ thể. | `UserAuthorizeIndex`, `UserProvince`, `UserDistrict`, `UserLocation` |

---

## 4. Kiến Trúc Migration (.NET Framework 4.6.1 sang .NET 10)

### 4.1 Bố cục Monorepo / Migration Layout
- `01_origin/`: Snapshot nguyên bản từ repo cũ (`coc.web.place.git` branch `master10`, commit `d1299579`). Dùng làm bản đối chiếu chuẩn (Pristine baseline), không chỉnh sửa trực tiếp.
- `02_target/`: Dự án đích chạy trên **ASP.NET Core .NET 10** theo phương pháp **Keep-Structure**:
  - Giữ nguyên cấu trúc thư mục, tên file, namespace gốc (`CoC.Web.Place`).
  - Toàn bộ khối code thay đổi đều được gắn tag tường minh: `//AI[MIGRATE_START]` ... `//AI[MIGRATE_END]`.
  - Giữ lại các file không còn biên dịch dưới dạng `<Compile Remove>` thay vì xóa vật lý khỏi đĩa (quy tắc *Exclude, don't delete*).

### 4.2 Tiến trình Gold-Alignment Mới Nhất
Theo hồ sơ [`04_critical_change/03_gold_align_cci_core_mvc.md`](file:///e:/Work/Place_Migrate/cci-store-location-web/04_critical_change/03_gold_align_cci_core_mvc.md):
1. **Chuyển đổi thư viện nền tảng**: Thay thế các DLL proprietary cũ (`Core.MVC`, `Core.Cache`, `Core.DTO`, `Core.Log`) bằng bộ NuGet chuẩn nội bộ:
   - `CCI.Core.MVC` (1.0.60)
   - `CCI.Core.ClientHelper` (1.0.4)
   - Giữ lại qua HintPath các DLL không có package thay thế: `Core.Helper.dll`, `Core.Infrastructure.dll`, `Libs.dll`, `LinqToExcel.dll`, `Remotion.Data.Linq.dll`, `SM.ItemCore.dll`.
2. **Cấu hình chuẩn hóa (Dual-Configuration)**:
   - `appsettings.json`: Cấu hình phẳng `AppSettings` phục vụ `AppConfig.Instance`.
   - `cci.core.json`: Cấu hình hệ thống chuẩn cho JWT, Redis, Serilog, Session.
   - Nạp lifecycle hooks `HostBuilderItem` (`ConfigurationItem`, `ServiceCollectonItem`, `ContainerBuilderItem`, `ApplicationBuilderItem`).
3. **Cơ chế xác thực**:
   - Tích hợp IdentityServer 1 (Keycloak `master` realm) qua giao thức Authorization Code không PKCE.
   - Lưu session an toàn qua `UserSessionStore` (Cookie `CC.SID` SameSite=Lax).
   - Tự động nạp bảng phân quyền người dùng qua background service `ClientPermissionWorker`.

---

## 5. Chiến Lược Cấu Hình & Môi Trường

Hệ thống sử dụng cơ chế **Cấu hình tập trung một nguồn sự thật (Single Source of Truth)**:
- Nguồn Staging: [`app.config`](file:///e:/Work/Place_Migrate/cci-store-location-web/app.config) (Target port: **5305**, Origin port: **4205**)
- Nguồn UAT: [`app.uat.config`](file:///e:/Work/Place_Migrate/cci-store-location-web/app.uat.config) (Target port: **4784**, Origin port: **4205**)
- Công cụ nạp cấu hình: `scripts/apply-env-config.py` tự động chuyển đổi XML thành:
  - `01_origin/CoC.Web.Place/appSetting.config`
  - `01_origin/CoC.Web.Place/Web.config`
  - `02_target/CoC.Web.Place/appsettings.json`

> [!WARNING]
> Tuyệt đối không sửa tay trực tiếp vào `appsettings.json` hay `appSetting.config` vì lệnh `make config` sẽ ghi đè từ file pristine gốc.

---

## 6. Chiến Lược Kiểm Thử (4-Track Test Suite)

Thư mục `tests/` chứa bộ kiểm thử tự động toàn diện gồm 4 tầng, với **418 bài kiểm tra** đã chạy pass 100%:

```mermaid
graph TD
    TestRoot["Hệ Thống Kiểm Thử (tests/)"]
    TestRoot --> Track1["1. Unit Tests (69 tests)<br/>• JSON Serializer & Converters<br/>• SessionStore & Permission<br/>• Offline MvcAuthorize Logic<br/>• String & Number Helpers"]
    TestRoot --> Track2["2. Integration Tests (6 tests)<br/>• Khám phá OIDC IDS1 Keycloak<br/>• Xác thực client_credentials<br/>• ClientPermissionWorker nạp MDM có GZip"]
    TestRoot --> Track3["3. Functional Tests (230 tests)<br/>• Quét Reflection toàn bộ action [MvcAuthorize]<br/>• Chặn ẩn danh trả về 401 Ajax / 302 Login<br/>• Kiểm tra Header bảo mật, 404, Static assets"]
    TestRoot --> Track4["4. Smoke Tests (113 tests)<br/>• 52 Trang Web GET trả về 200 OK<br/>• 61 Endpoint Ajax đọc trả lời JSON chuẩn<br/>• Chạy với phiên đăng nhập SSO thật"]
```

---

## 7. Các Lệnh Điều Hành Chính (Cheat-sheet)

```bash
# Bơm cấu hình môi trường Staging (mặc định)
make config

# Chuyển đổi môi trường sang UAT
make config ENV=uat

# Khôi phục cấu hình sạch ban đầu
make config ARGS="--restore"

# Biên dịch và kiểm tra trạng thái target (.NET 10)
make -C 02_target build

# Chạy ứng dụng local (.NET 10 Kestrel)
make -C 02_target run

# Chạy xác minh khởi động (Health check cổng 5305/4784)
make -C 02_target verify

# Chạy toàn bộ 4 tầng test suite
make config ENV=uat && make -C 02_target test && make config
```

---

## 8. Ghi Chú Kỹ Thuật Đã Xử Lý (Resolved Technical Items)

> [!TIP]
> **Đã xử lý cảnh báo NU1605 (Package Downgrade)**:
> - Đã nâng cấp `EPPlus` từ `5.7.3` lên **`7.2.2`** trong `02_target/CoC.Web.Place/CoC.Web.Place.csproj` để đồng bộ hoàn toàn với transitive dependency của `CCI.Core.Utilities 1.0.5` (thuộc bộ `CCI.Core.MVC 1.0.60`).
> - Kết quả: `dotnet restore` và `dotnet build` đạt **0 Error(s)** hoàn tất.

