import os

APP_JS = r"e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\app.js"
STYLES_CSS = r"e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\styles.css"

with open(APP_JS, "r", encoding="utf-8") as f:
    js_content = f.read()

# Replace findDefectsForTest and renderRegistryTab
new_registry_code = '''
  var CATEGORY_DEFINITIONS = {
    "Auth & Session / Redis Keyring": {
      icon: "🔐",
      whatIsIt: "Quản lý phiên làm việc (Session, Cookie xác thực .PlaceWeb, Antiforgery) trên môi trường phân tán Kubernetes.",
      rootCause: "ASP.NET Core mặc định lưu khóa DataProtection Keyring trong RAM cục bộ từng Pod. Khi K8s scale/rollout Pod mới, khóa giải mã bị mất khiến người dùng bị văng đăng nhập và lỗi 500 CryptographicException.",
      solution: "Lưu trữ DataProtection Keyring tập trung trên Redis Cache (DataProtection-Keys:Place) kèm fallback an toàn sang DistributedMemoryCache."
    },
    "URL Normalization & Double Slash": {
      icon: "🌐",
      whatIsIt: "Chuẩn hóa format URL gọi từ Web sang Backend API, chống lỗi dấu gạch chéo kép (//).",
      rootCause: "Base URL backend kết thúc bằng '/' ghép với route '/api/...' tạo thành '//api/...'. Ingress Controller / NGINX từ chối và trả về HTTP 404 Not Found.",
      solution: "Bổ sung UriExtensions.NormalizeUrl() tự động làm sạch '//' thành '/' trong toàn bộ các phương thức gọi HTTP (Get, Post, Put, Delete)."
    },
    "Routing & Config Fallback": {
      icon: "🔀",
      whatIsIt: "Cấu hình môi trường phân tán (Vault GitOps, AppSettings, IDS SSO Url) và fallback dịch vụ.",
      rootCause: "Môi trường STG10 chưa triển khai đủ API backend (gây 131 ca 404), và AppConfig.cs nạp thiếu section 'AppSettings' làm _iDSUrl bị null, redirect sai sang domain cục bộ.",
      solution: "Trỏ ApisUrl/HRMApisUrl sang STG4 (giải quyết 100% 131 ca 404) và nạp AppSettings kèm chuỗi fallback an toàn Get('IDSUrl') ?? GetRaw('URLConnectionCore:IDSUrl') ?? GetRaw('AppSettings:IDSUrl')."
    },
    "FormOptions & Model Binding": {
      icon: "📝",
      whatIsIt: "Giới hạn số lượng phần tử form dữ liệu lớn khi người dùng chọn lọc hàng loạt (Bulk Selection).",
      rootCause: "ASP.NET Core mặc định giới hạn ValueCountLimit = 1024 để chống HashDoS. Khi chọn 'Tất cả siêu thị' (> 1.380 siêu thị) và submit, server quăng InvalidDataException.",
      solution: "Cấu hình mở rộng ngưỡng services.Configure<FormOptions>(opt => opt.ValueCountLimit = int.MaxValue) trong Startup.cs."
    },
    "File Upload & Directives": {
      icon: "📁",
      whatIsIt: "Xử lý file đính kèm đa phần (Multipart Form Data) trong nghiệp vụ tài liệu / chỉ đạo.",
      rootCause: "Request raw từ client không có multipart boundary hoặc đọc Request.Form.Files khi chưa kiểm tra Request.HasFormContentType làm Kestrel ném lỗi 500.",
      solution: "Thêm guard clause kiểm tra HasFormContentType và multipart boundary trước khi đọc Request.Form.Files, trả về rỗng an toàn nếu request thiếu boundary."
    },
    "Security & Redirection / SSO Callback": {
      icon: "🛡️",
      whatIsIt: "Điều hướng xác thực sau khi đăng nhập qua cổng SSO tập trung Keycloak.",
      rootCause: "Tham số ReturnUrl sau SSO callback nếu không kiểm tra Same-Origin có thể bị kẻ xấu chèn URL độc hại bên ngoài để thực hiện tấn công Open Redirect.",
      solution: "Kiểm tra nghiêm ngặt Url.IsLocalUrl(returnUrl), chỉ cho phép redirect khi URL thuộc cùng domain cục bộ, ngược lại redirect về trang chủ ~/."
    },
    "Linux Compatibility & Static Files": {
      icon: "🐧",
      whatIsIt: "Tương thích hệ điều hành giữa môi trường Windows (IIS) và Linux Container (Docker/K8s).",
      rootCause: "Hệ thống tập tin Linux phân biệt chữ hoa và chữ thường (Case-Sensitive), trong khi Windows (IIS) thì không. Nếu URL gọi tên file tĩnh lệch hoa thường (vd Icons.png vs icons.png) thì Linux trả 404.",
      solution: "Tích hợp middleware UseCaseInsensitiveStaticFiles() tự động đối chiếu và phục vụ file tĩnh không phân biệt hoa thường trên Linux container."
    },
    "EPPlus DataValidation Order": {
      icon: "📊",
      whatIsIt: "Xuất file bảng tính Excel chứa quy tắc kiểm tra dữ liệu (Dropdown Validation) với thư viện EPPlus 5+.",
      rootCause: "EPPlus 5+ thay đổi kiến trúc DOM XML. Nếu gán thuộc tính Formula trước các thuộc tính cấu hình (ShowErrorMessage, AllowBlank) sẽ bị ngoại lệ DataValidationStaleException hoặc file corrupt.",
      solution: "Chuẩn hóa thứ tự gán thuộc tính EPPlus: thiết lập cờ hiển thị lỗi và cho phép rỗng trước, sau đó mới nạp chuỗi công thức ExcelFormula."
    }
  };

  var registryFilterCategory = "ALL";
  function jumpToFix(fixId) {
    registryFilterCategory = "ALL";
    switchTab("registry");
    var p = payloadById(state.pid);
    if (p) renderRegistryTab(p);
    setTimeout(function () {
      var card = document.getElementById("card-fix-" + fixId);
      if (card) {
        card.scrollIntoView({ behavior: "smooth", block: "center" });
        card.classList.add("card-highlight");
        setTimeout(function () { card.classList.remove("card-highlight"); }, 2500);
      }
    }, 60);
  }
  window.__jumpToFix = jumpToFix;

  function jumpToTestByCode(tcCode) {
    switchTab("detail");
    var p = payloadById(state.pid);
    if (!p) return;
    var matchedScreen = null;
    var matchedTest = null;
    allScreens(p).some(function (s) {
      return (s.tests || []).some(function (t) {
        if (t.tc && t.tc.toUpperCase() === tcCode.toUpperCase()) {
          matchedScreen = s;
          matchedTest = t;
          return true;
        }
        return false;
      });
    });
    if (matchedScreen && matchedTest) {
      state.selectedEp = epLabel(matchedScreen);
      state.selectedTest = testKey(matchedTest);
      renderList(p);
      renderDetail(p);
    }
  }

  function renderRegistryTab(p) {
    var panel = document.getElementById("panel-registry");
    if (!panel) return;
    var defects = (defectRegistry && defectRegistry.defects) ? defectRegistry.defects : [];
    var countEl = document.getElementById("defectRegistryCount");
    if (countEl) countEl.textContent = defects.length;

    if (!defects.length) {
      panel.innerHTML = '<section class="registry-tab"><h2 class="dim-section-title">Nhóm Lỗi &amp; So Sánh Code (Defect Registry)</h2>' +
        '<p class="ov-line">Chưa có dữ liệu sổ lỗi (defect-registry.json). Chạy test hoặc cập nhật defect-registry.json để xem.</p></section>';
      return;
    }

    var categories = Array.from(new Set(defects.map(function (d) { return d.category; })));
    var catCounts = {};
    categories.forEach(function (c) { catCounts[c] = 0; });
    defects.forEach(function (d) { catCounts[d.category] = (catCounts[d.category] || 0) + 1; });

    // 1. Build Visual Defect Map Cards
    var mapCardsHtml = Object.keys(CATEGORY_DEFINITIONS).map(function (catName) {
      var catDef = CATEGORY_DEFINITIONS[catName] || { icon: "⚙️", whatIsIt: "", rootCause: "", solution: "" };
      var catDefects = defects.filter(function (d) { return d.category === catName; });
      var count = catDefects.length;
      var isActive = registryFilterCategory === catName;
      var fixBadges = catDefects.map(function (d) {
        return '<span class="map-fix-pill" title="' + esc(d.title) + '">' + esc(d.id) + '</span>';
      }).join(" ");

      return '<div class="cat-map-card' + (isActive ? ' active-card' : '') + '" data-cat="' + esc(catName) + '">' +
        '<div class="cat-map-hdr">' +
          '<div class="cat-map-icon">' + catDef.icon + '</div>' +
          '<div class="cat-map-title-box">' +
            '<div class="cat-map-name">' + esc(catName) + '</div>' +
            '<div class="cat-map-count">' + (count > 0 ? (count + ' lỗi đã fix &amp; verify') : '0 lỗi') + '</div>' +
          '</div>' +
        '</div>' +
        '<div class="cat-map-body">' +
          '<div class="cat-map-row"><span class="cat-map-tag tag-what">Nhóm lỗi là gì:</span> <span class="cat-map-desc">' + esc(catDef.whatIsIt) + '</span></div>' +
          '<div class="cat-map-row"><span class="cat-map-tag tag-cause">Nguyên nhân:</span> <span class="cat-map-desc">' + esc(catDef.rootCause) + '</span></div>' +
          '<div class="cat-map-row"><span class="cat-map-tag tag-sol">Giải pháp:</span> <span class="cat-map-desc">' + esc(catDef.solution) + '</span></div>' +
        '</div>' +
        '<div class="cat-map-footer">' +
          '<div class="cat-map-fixes">' + fixBadges + '</div>' +
          '<button type="button" class="btn-filter-cat" data-cat="' + esc(catName) + '">Xem chi tiết &amp; Code diff &rarr;</button>' +
        '</div>' +
      '</div>';
    }).join("");

    // 2. Build Category Filter Buttons
    var catButtons = '<button type="button" class="cat-chip' + (registryFilterCategory === "ALL" ? " active" : "") + '" data-cat="ALL">Tất cả (' + defects.length + ')</button>' +
      categories.map(function (c) {
        return '<button type="button" class="cat-chip' + (registryFilterCategory === c ? " active" : "") + '" data-cat="' + esc(c) + '">' +
          esc(c) + ' (' + catCounts[c] + ')</button>';
      }).join("");

    // 3. Filter Defect Cards
    var filtered = registryFilterCategory === "ALL" ? defects : defects.filter(function (d) { return d.category === registryFilterCategory; });

    var cardsHtml = filtered.map(function (d) {
      var sevCls = (d.severity || "").toLowerCase();
      var prUrl = d.pr || (d.pullRequests && d.pullRequests[0]) || "";
      var prLinks = "";
      if (prUrl) {
        var num = prUrl.split("/").pop();
        prLinks = '<a href="' + esc(prUrl) + '" target="_blank" rel="noopener" class="pr-link">PR #' + esc(num) + ' &nearr;</a>';
      }
      var commitBadges = (d.commits || []).map(function (cm) {
        return '<span class="commit-tag" title="' + esc(cm.message || "") + '">' + esc(cm.hash ? cm.hash.slice(0, 7) : "-") + '</span>';
      }).join(" ");
      var relatedList = d.relatedTests || d.relatedTestCases || [];
      var tcBadges = relatedList.map(function (tc) {
        return '<button type="button" class="tc-tag" data-tc="' + esc(tc) + '" title="Bấm để chuyển tới chi tiết test case">' + esc(tc) + '</button>';
      }).join(" ");

      var symptomText = d.symptom || d.symptoms || "";
      var rootCauseText = d.rootCause || "";
      var fixedWhatText = d.fixedWhat || "";

      // Support BOTH d.oldCode/d.newCode AND d.codeComparison
      var oldCode = d.oldCode || (d.codeComparison && d.codeComparison.oldCodeSnippet) || "// Không có code cũ";
      var newCode = d.newCode || (d.codeComparison && d.codeComparison.newCodeSnippet) || "// Không có code mới";
      var explanation = (d.codeComparison && d.codeComparison.explanation) || "";

      return '<div class="defect-card" id="card-fix-' + esc(d.id) + '">' +
        '<div class="defect-card-header">' +
          '<div class="defect-header-left">' +
            '<span class="fix-id-badge">' + esc(d.id) + '</span>' +
            '<span class="fix-sev-badge sev-' + esc(sevCls) + '">' + esc(d.severity) + '</span>' +
            '<span class="fix-status-badge">' + esc(d.status) + '</span>' +
            '<h3 class="fix-title">' + esc(d.title) + '</h3>' +
          '</div>' +
          '<span class="fix-cat-tag">' + esc(d.category) + '</span>' +
        '</div>' +
        '<div class="defect-card-body">' +
          '<div class="defect-grid-info">' +
            '<div class="defect-info-item"><span class="info-lbl">Triệu chứng:</span> <span class="info-val">' + esc(symptomText) + '</span></div>' +
            '<div class="defect-info-item"><span class="info-lbl">Nguyên nhân gốc:</span> <span class="info-val">' + esc(rootCauseText) + '</span></div>' +
            '<div class="defect-info-item"><span class="info-lbl">Đã khắc phục:</span> <span class="info-val font-semibold text-pass">' + esc(fixedWhatText) + '</span></div>' +
            '<div class="defect-meta-row">' +
              (tcBadges ? '<div class="meta-item"><span class="meta-lbl">Test Cases:</span> ' + tcBadges + '</div>' : '') +
              (prLinks ? '<div class="meta-item"><span class="meta-lbl">Pull Request:</span> ' + prLinks + '</div>' : '') +
              (commitBadges ? '<div class="meta-item"><span class="meta-lbl">Commits:</span> ' + commitBadges + '</div>' : '') +
            '</div>' +
          '</div>' +
          '<div class="code-diff-box">' +
            '<div class="diff-header-bar">' +
              '<span class="diff-title">So Sánh Code Cũ (Gây Lỗi) vs Code Mới (Đã Fix)</span>' +
            '</div>' +
            '<div class="diff-columns">' +
              '<div class="diff-col diff-col-old">' +
                '<div class="diff-col-hdr">❌ CODE CŨ (GÂY LỖI / ORIGIN)</div>' +
                '<pre class="diff-pre"><code>' + esc(oldCode) + '</code></pre>' +
              '</div>' +
              '<div class="diff-col diff-col-new">' +
                '<div class="diff-col-hdr">✅ CODE MỚI (ĐÃ KHẮC PHỤC / TARGET)</div>' +
                '<pre class="diff-pre"><code>' + esc(newCode) + '</code></pre>' +
              '</div>' +
            '</div>' +
            (explanation ? '<div class="diff-footer-expl"><strong>💡 Rationale:</strong> ' + esc(explanation) + '</div>' : '') +
          '</div>' +
        '</div>' +
      '</div>';
    }).join("");

    panel.innerHTML = '<section class="registry-tab">' +
      '<div class="registry-tab-hdr">' +
        '<div>' +
          '<h2 class="dim-section-title">Nhóm Lỗi Kỹ Thuật Đã Khắc Phục &amp; So Sánh Code Cũ vs Mới</h2>' +
          '<p class="registry-sub">Tổng hợp ' + defects.length + ' lỗi và giải pháp dập khuôn chuẩn hóa trên Store Location Web (' + categories.length + ' nhóm kỹ thuật)</p>' +
        '</div>' +
        '<div class="registry-kpi-summary">' +
          '<div class="reg-kpi"><span class="num">' + defects.length + '</span><span class="lbl">Tổng mã fix</span></div>' +
          '<div class="reg-kpi"><span class="num text-pass">' + defects.length + '</span><span class="lbl">Đã giải quyết</span></div>' +
          '<div class="reg-kpi"><span class="num text-accent">' + categories.length + '</span><span class="lbl">Nhóm lỗi</span></div>' +
        '</div>' +
      '</div>' +
      '<!-- Map Tổng Trực Quan Các Nhóm Lỗi -->' +
      '<div class="defect-map-section">' +
        '<div class="map-section-hdr">' +
          '<h3 class="map-section-title">🗺️ Bản Đồ Tổng Quan Các Nhóm Lỗi Migration &amp; Hạ Tầng (.NET 10)</h3>' +
          '<p class="map-section-sub">Bấm vào bất kỳ nhóm lỗi nào để lọc và xem ngay toàn bộ chi tiết giải pháp &amp; khối so sánh code bên dưới.</p>' +
        '</div>' +
        '<div class="defect-map-grid">' + mapCardsHtml + '</div>' +
      '</div>' +
      '<div class="list-section-hdr" id="detailsAnchor">' +
        '<h3 class="list-section-title">Chi Tiết Giải Pháp &amp; So Sánh Code Cũ vs Mới ' +
          (registryFilterCategory !== "ALL" ? '— Nhóm: <span class="active-cat-name">' + esc(registryFilterCategory) + '</span>' : '') +
        '</h3>' +
        '<div class="cat-filter-bar">' + catButtons + '</div>' +
      '</div>' +
      '<div class="defect-cards-list">' + cardsHtml + '</div>' +
    '</section>';

    // Click handler for cat chips
    panel.querySelectorAll(".cat-chip").forEach(function (btn) {
      btn.addEventListener("click", function () {
        registryFilterCategory = btn.getAttribute("data-cat");
        renderRegistryTab(p);
      });
    });

    // Click handler for map cards and their buttons
    panel.querySelectorAll(".cat-map-card, .btn-filter-cat").forEach(function (el) {
      el.addEventListener("click", function (ev) {
        var cat = el.getAttribute("data-cat") || (el.closest(".cat-map-card") && el.closest(".cat-map-card").getAttribute("data-cat"));
        if (!cat) return;
        registryFilterCategory = cat;
        renderRegistryTab(p);
        var anchor = document.getElementById("detailsAnchor");
        if (anchor) anchor.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });

    // Click handler for tc-tag
    panel.querySelectorAll(".tc-tag").forEach(function (tag) {
      tag.addEventListener("click", function (ev) {
        ev.stopPropagation();
        var tcCode = tag.getAttribute("data-tc");
        if (tcCode) jumpToTestByCode(tcCode);
      });
    });
  }
'''

# Replace from var registryFilterCategory up to renderRegistryTab closing brace
start_marker = "  var registryFilterCategory = \"ALL\";"
end_marker = "  function renderAll() {"

start_idx = js_content.find(start_marker)
end_idx = js_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    js_content = js_content[:start_idx] + new_registry_code + "\n  " + js_content[end_idx:]
    with open(APP_JS, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Updated app.js with Category Definitions & Visual Map successfully.")
else:
    print("Could not find markers in app.js! start_idx:", start_idx, "end_idx:", end_idx)
