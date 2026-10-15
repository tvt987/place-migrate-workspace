with open('02_target/CoC.Web.SCM/Controllers/ErrorController.cs', 'rb') as f:
    raw = f.read()

# Strip BOM if present for decoding
if raw.startswith(b'\xef\xbb\xbf'):
    content = raw[3:].decode('utf-8')
else:
    content = raw.decode('utf-8')

target = """        // GET: Error
        public new ActionResult Unauthorized()
        {
            if (!UserSessionStore.Exists(HttpContext.Session))
                return RedirectToAction("index", "home");
            return View();
        }

        public ActionResult Error(string aspxerrorpath = null)
        {
            //if (HttpContext.Session["UserPricinpal"] == null)
            //    return RedirectToAction("index", "home");

            return View();
        }

        public new ActionResult NotFound()
        {
            if (!UserSessionStore.Exists(HttpContext.Session))
                return RedirectToAction("index", "home");
            return View();
        }"""

replacement = """        // GET: Error
        public new ActionResult Unauthorized()
        {
            var user = (User as UserPrincipal) ?? UserSessionStore.Load(HttpContext.Session);
            if (user == null)
                return RedirectToAction("index", "home");
            HttpContext.User = user;
            return View();
        }

        public ActionResult Error(string aspxerrorpath = null)
        {
            var user = (User as UserPrincipal) ?? UserSessionStore.Load(HttpContext.Session);
            if (user != null)
                HttpContext.User = user;

            return View();
        }

        public new ActionResult NotFound()
        {
            var user = (User as UserPrincipal) ?? UserSessionStore.Load(HttpContext.Session);
            if (user == null)
                return RedirectToAction("index", "home");
            HttpContext.User = user;
            return View();
        }"""

target_lf = target.replace('\r\n', '\n')
replacement_lf = replacement.replace('\r\n', '\n')
content_lf = content.replace('\r\n', '\n')

assert target_lf in content_lf, "Target string not found in ErrorController.cs"
new_content = content_lf.replace(target_lf, replacement_lf)

with open('02_target/CoC.Web.SCM/Controllers/ErrorController.cs', 'wb') as f:
    f.write(b'\xef\xbb\xbf' + new_content.encode('utf-8'))

print("Updated ErrorController.cs with LF and UTF-8 BOM successfully")
