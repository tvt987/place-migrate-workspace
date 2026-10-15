import os

# 1. Update ApiHelper.cs in cci-store-location-web
place_apihelper_path = r"E:\Work\Place_Migrate\cci-store-location-web\02_target\CoC.Web.Place\Helpers\ApiHelper.cs"
with open(place_apihelper_path, "rb") as f:
    raw = f.read()
has_bom = raw.startswith(b"\xef\xbb\xbf")
text = raw.decode("utf-8-sig").replace("\r\n", "\n")

old1 = """            _CodeStep.ErrorStep = "Set token";
            _ObjAPIClient.Client.SetBearerToken(CurrentUser.Token);
            if (!_ObjAPIClient.Client.DefaultRequestHeaders.Contains("UserID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("UserID", CurrentUser.Username);
            //AI[MIGRATE_START]: HttpContext.Current.Items / Session.SessionID -> accessor HttpContext.Items / ISession.Id (same header names and values)
            if (httpContext.Items.ContainsKey("ConcungContextID") && !_ObjAPIClient.Client.DefaultRequestHeaders.Contains("ConcungContextID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("ConcungContextID", httpContext.Items["ConcungContextID"].ToString());
            if (!_ObjAPIClient.Client.DefaultRequestHeaders.Contains("SessionID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("SessionID", httpContext.Session.Id);
            //AI[MIGRATE_END]""".replace("\r\n", "\n")

new1 = """            _CodeStep.ErrorStep = "Set token";
            _ObjAPIClient.Client.SetBearerToken(CurrentUser?.Token ?? string.Empty);
            if (!_ObjAPIClient.Client.DefaultRequestHeaders.Contains("UserID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("UserID", CurrentUser?.Username ?? string.Empty);
            //AI[MIGRATE_START]: HttpContext.Current.Items / Session.SessionID -> accessor HttpContext.Items / ISession.Id (same header names and values)
            if (httpContext != null && httpContext.Items != null && httpContext.Items.ContainsKey("ConcungContextID") && !_ObjAPIClient.Client.DefaultRequestHeaders.Contains("ConcungContextID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("ConcungContextID", httpContext.Items["ConcungContextID"].ToString());
            if (httpContext?.Session != null && !_ObjAPIClient.Client.DefaultRequestHeaders.Contains("SessionID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("SessionID", httpContext.Session.Id);
            //AI[MIGRATE_END]""".replace("\r\n", "\n")

old2 = """                            apiClient.Client.SetBearerToken(bgToken);
                            apiClient.Client.DefaultRequestHeaders.Add("UserID", bgUsername);""".replace("\r\n", "\n")

new2 = """                            apiClient.Client.SetBearerToken(bgToken ?? string.Empty);
                            apiClient.Client.DefaultRequestHeaders.Add("UserID", bgUsername ?? string.Empty);""".replace("\r\n", "\n")

old3 = """            System.Text.StringBuilder srtLog = new System.Text.StringBuilder();
            srtLog.Append("CurrentUser.UserID: ").Append(CurrentUser.UserID).Append("\\r\\n");""".replace("\r\n", "\n")

new3 = """            System.Text.StringBuilder srtLog = new System.Text.StringBuilder();
            if (CurrentUser != null)
            {
                srtLog.Append("CurrentUser.UserID: ").Append(CurrentUser.UserID).Append("\\r\\n");
            }""".replace("\r\n", "\n")

assert old1 in text, "old1 not found in place ApiHelper.cs"
assert old2 in text, "old2 not found in place ApiHelper.cs"
assert old3 in text, "old3 not found in place ApiHelper.cs"

text = text.replace(old1, new1, 1).replace(old2, new2, 1).replace(old3, new3, 1)

with open(place_apihelper_path, "wb") as f:
    if has_bom:
        f.write(b"\xef\xbb\xbf")
    f.write(text.encode("utf-8"))
print("Successfully patched place ApiHelper.cs")

# 2. Update UserPrincipal.cs in cci-store-location-web
place_userprincipal_path = r"E:\Work\Place_Migrate\cci-store-location-web\02_target\CoC.Web.Place\Permission\UserPrincipal.cs"
with open(place_userprincipal_path, "rb") as f:
    raw2 = f.read()
has_bom2 = raw2.startswith(b"\xef\xbb\xbf")
text2 = raw2.decode("utf-8-sig").replace("\r\n", "\n")

old_perm = """        public bool IsPermission(string RoleFunctionName)
        {
            if (Username == "0000") return true;
            if (string.IsNullOrWhiteSpace(RoleFunctionName) || _roleIDs == null)
                return false;

            return UserPermission.Any(p => p.RoleFunctionName == RoleFunctionName);
        }""".replace("\r\n", "\n")

new_perm = """        public bool IsPermission(string RoleFunctionName)
        {
            if (Username == "0000") return true;
            if (string.IsNullOrWhiteSpace(RoleFunctionName) || _roleIDs == null || _roleIDs.Count == 0)
                return false;

            try
            {
                var perms = UserPermission;
                if (perms == null || perms.Count == 0) return false;
                return perms.Any(p => p != null && p.RoleFunctionName == RoleFunctionName);
            }
            catch
            {
                return false;
            }
        }""".replace("\r\n", "\n")

assert old_perm in text2, "old_perm not found in place UserPrincipal.cs"
text2 = text2.replace(old_perm, new_perm, 1)

with open(place_userprincipal_path, "wb") as f:
    if has_bom2:
        f.write(b"\xef\xbb\xbf")
    f.write(text2.encode("utf-8"))
print("Successfully patched place UserPrincipal.cs")
