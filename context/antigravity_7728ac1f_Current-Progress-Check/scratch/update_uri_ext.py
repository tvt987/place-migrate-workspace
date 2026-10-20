path = '02_target/CoC.Web.SCM/Helpers/UriExtension.cs'
content = '''namespace CoC.Web.SCM.Helpers\r
{\r
    public static class UriExtension\r
    {\r
        public static string ToUrl(this string url)\r
        {\r
            if (url.EndsWith("/"))\r
            {\r
                url = url.Remove(url.Length - 1, 1);\r
            }\r
            return $"{url}/";\r
        }\r
\r
        public static string NormalizeUrl(this string url)\r
        {\r
            if (string.IsNullOrEmpty(url)) return url;\r
            return System.Text.RegularExpressions.Regex.Replace(url, "(?<!https?:)/{2,}", "/");\r
        }\r
    }\r
}\r
'''
with open(path, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + content.encode('utf-8'))
print('UriExtension.cs updated with BOM and CRLF')
