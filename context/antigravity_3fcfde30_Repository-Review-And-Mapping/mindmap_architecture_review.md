# Đánh Giá Tổng Thể, Kiến Trúc & Sơ Đồ Tư Duy Dự Án `cci-store-location-web`

## 1. Thông Tin Chung
- **Dự án**: `cci-store-location-web` (`CoC.Web.Place`)
- **Repo Git**: `https://tinhkun102@bitbucket.org/concung/cci-store-location-web.git`
- **Vị trí lưu trữ**: [`e:\Work\Place_Migrate\cci-store-location-web`](file:///e:/Work/Place_Migrate/cci-store-location-web)
- **Nhóm chức năng**: Quản lý mặt bằng, điểm thuê và mở rộng chuỗi cửa hàng Con Cung (Group: `4_STORE-LOCATION`).
- **Nền tảng**: Đã được migrate từ **ASP.NET MVC 5 (.NET 4.6.1)** sang **ASP.NET Core (.NET 10)**.

---

## 2. Sơ Đồ Tư Duy (Mindmap)

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

## 3. Kiến Trúc Luồng Dữ Liệu (Data Flow)

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

## 4. Chi Tiết Các Tầng Công Nghệ & Thành Phần

### 4.1 Frontend Layer
- **Framework**: AngularJS 1.x kết hợp MVC Razor Views (220 file `.cshtml`).
- **Tài nguyên tĩnh**: Nằm trong `wwwroot/` với 3 thư mục `script-handler/`, `content/`, `data/`.
- **Thư viện UI**: Bootstrap, jQuery, Angular UI-Select, Leaflet Map (bản đồ trực quan hóa vị trí cửa hàng và mật độ dân cư).
- **Format dữ liệu**: JSON serialization kiểu PascalCase tương thích với client AngularJS ban đầu.

### 4.2 Backend & Web Host (.NET 10)
- **Host**: Kestrel chạy trên `net10.0` với cấu hình SDK Web (`Microsoft.NET.Sdk.Web`).
- **DI Engine**: Autofac `8.3.0` tích hợp sâu qua `AutofacServiceProviderFactory`.
- **Cơ chế Adapter/Shims**:
  - `LegacyDateTimeJsonConverter` & `LegacyTimeSpanJsonConverter`: Xử lý định dạng ngày tháng kiểu cũ `/Date(ms)/` và ISO.
  - `LegacyJsonNetResult` / `BaseController`: Đảm bảo serialization chuẩn `Newtonsoft.Json` mà không làm thay đổi các model cũ.
  - `LegacyHosting`: Giả lập `Server.MapPath` và `HttpRuntime.AppDomainAppPath` thông qua `IWebHostEnvironment.ContentRootPath`.

### 4.3 Xác thực & Ủy quyền (AuthN / AuthZ)
- **SSO Keycloak (IDS1)**: Sử dụng OAuth2 Authorization Code flow (không dùng PKCE, `response_mode=query`).
- **Session**: Session được lưu qua `AddDistributedMemoryCache` với cookie `CC.SID` (`SameSite=Lax`).
- **MDM Permission**: Dịch vụ nền `ClientPermissionWorker` tự động fetch bảng phân quyền từ `MDMUrl/api/Permissions/ReadClient` lúc khởi động và định kỳ.
- **Filter**: `MvcAuthorizeAttribute` kiểm tra quyền theo module và hành động.

### 4.4 Tích hợp Dữ liệu & Caching
- **Không có Database kết nối trực tiếp**: Mọi truy vấn dữ liệu đều thực hiện qua HTTP REST calls đến downstream API `store-location-api` (`ApisUrl`).
- **Multi-Level Cache**:
  - Tầng 1: In-Memory Cache cục bộ (`MemoryCacheManager`).
  - Tầng 2: Distributed Cache qua Redis (`RedisCacheManager`).
  - Đồng bộ Cache: Cơ chế Pub/Sub qua Redis channel (`SubcribeMessageFromRedisSafe`).

---

## 5. Phát Hiện Kỹ Thuật Đáng Lưu Ý (Technical Observation)

> [!NOTE]
> **Cảnh báo NU1605 (Package Downgrade)**:
> Khi chạy `dotnet restore` trên `02_target/CoC.Web.Place.sln`, hệ thống phát hiện lỗi:
> `error NU1605: Warning As Error: Detected package downgrade: EPPlus from 7.2.2 to 5.7.3.`
> **Nguyên nhân**: Bản nâng cấp `CCI.Core.MVC 1.0.60` kéo theo `CCI.Core.Utilities 1.0.5`, gói này phụ thuộc vào `EPPlus >= 7.2.2`. Trong khi đó, `CoC.Web.Place.csproj` vẫn đang ghim cứng `<PackageReference Include="EPPlus" Version="5.7.3" />`.
> **Hướng xử lý đề xuất**: Nâng version EPPlus trong `CoC.Web.Place.csproj` lên `7.2.2` hoặc thêm cấu hình NoWarn thích hợp.
