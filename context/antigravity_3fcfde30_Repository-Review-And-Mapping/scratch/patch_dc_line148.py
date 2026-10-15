path = r'E:\Work\Place_Migrate\cci-dc-web\02_target\CoC.Web.DC\Helpers\ApiHelper.cs'
with open(path, 'rb') as f:
    raw = f.read()
has_bom = raw.startswith(b'\xef\xbb\xbf')
text = raw.decode('utf-8-sig')

old = 'apiClient.Client.DefaultRequestHeaders.Add("UserID", CurrentUser.Username);'
new = 'apiClient.Client.DefaultRequestHeaders.Add("UserID", CurrentUser?.Username ?? string.Empty);'

assert old in text, 'old not found'
text = text.replace(old, new, 1)

with open(path, 'wb') as f:
    if has_bom:
        f.write(b'\xef\xbb\xbf')
    f.write(text.encode('utf-8'))
print('Line 148 patched')
