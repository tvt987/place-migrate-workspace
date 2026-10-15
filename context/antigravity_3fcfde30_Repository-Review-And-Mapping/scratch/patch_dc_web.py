with open(r'E:\Work\Place_Migrate\cci-dc-web\02_target\CoC.Web.DC\Helpers\ApiHelper.cs', 'rb') as f:
    raw = f.read()
has_bom = raw.startswith(b'\xef\xbb\xbf')
text = raw.decode('utf-8-sig').replace('\r\n', '\n')

old1 = """            _CodeStep.ErrorStep = "Set token";
            if (this.CurrentUser == null)
                throw new InvalidOperationException("No authenticated user in the session (UserPricinpal): cannot call the API without a token");
            _ObjAPIClient.Client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", CurrentUser.Token);
            if (!_ObjAPIClient.Client.DefaultRequestHeaders.Contains("UserID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("UserID", CurrentUser.Username);
            ApplyAccept(_ObjAPIClient.Client.DefaultRequestHeaders);""".replace('\r\n', '\n')

new1 = """            _CodeStep.ErrorStep = "Set token";
            _ObjAPIClient.Client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", CurrentUser?.Token ?? string.Empty);
            if (!_ObjAPIClient.Client.DefaultRequestHeaders.Contains("UserID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("UserID", CurrentUser?.Username ?? string.Empty);
            ApplyAccept(_ObjAPIClient.Client.DefaultRequestHeaders);""".replace('\r\n', '\n')

old2 = """                            IAPIClient apiClient = Engine.ContainerManager.Resolve<IAPIClient>();
                            apiClient.Client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", CurrentUser.Token);""".replace('\r\n', '\n')

new2 = """                            IAPIClient apiClient = Engine.ContainerManager.Resolve<IAPIClient>();
                            apiClient.Client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", CurrentUser?.Token ?? string.Empty);""".replace('\r\n', '\n')

assert old1 in text, "old1 not found"
assert old2 in text, "old2 not found"
text = text.replace(old1, new1, 1).replace(old2, new2, 1)

with open(r'E:\Work\Place_Migrate\cci-dc-web\02_target\CoC.Web.DC\Helpers\ApiHelper.cs', 'wb') as f:
    if has_bom:
        f.write(b'\xef\xbb\xbf')
    f.write(text.encode('utf-8'))
print("DC ApiHelper patched successfully")

with open(r'E:\Work\Place_Migrate\cci-dc-web\02_target\CoC.Web.DC\Permission\UserPrincipal.cs', 'rb') as f:
    raw2 = f.read()
has_bom2 = raw2.startswith(b'\xef\xbb\xbf')
text2 = raw2.decode('utf-8-sig').replace('\r\n', '\n')

old_perm = """        public bool IsPermission(string RoleFunctionName)
        {
            if (this.RoleIDs == null)
            {
                return false;
            }
            if (Username == "0000") return true;
            return (from r in Permission.Data.Permission
                    where this.RoleIDs.Contains(r.RoleID) &&
                      r.RoleFunctionName == RoleFunctionName
                    select r).Count() > 0;
        }""".replace('\r\n', '\n')

new_perm = """        public bool IsPermission(string RoleFunctionName)
        {
            if (Username == "0000") return true;
            if (string.IsNullOrEmpty(RoleFunctionName)) return false;
            if (this.RoleIDs == null || this.RoleIDs.Count == 0) return false;

            try
            {
                var permissions = Permission.Data?.Permission;
                if (permissions == null || permissions.Count == 0) return false;

                return permissions.Any(r => r != null && this.RoleIDs.Contains(r.RoleID) && r.RoleFunctionName == RoleFunctionName);
            }
            catch
            {
                return false;
            }
        }""".replace('\r\n', '\n')

assert old_perm in text2, "old_perm not found"
text2 = text2.replace(old_perm, new_perm, 1)

with open(r'E:\Work\Place_Migrate\cci-dc-web\02_target\CoC.Web.DC\Permission\UserPrincipal.cs', 'wb') as f:
    if has_bom2:
        f.write(b'\xef\xbb\xbf')
    f.write(text2.encode('utf-8'))
print("DC UserPrincipal patched successfully")
