import sys

path = '02_target/CoC.Web.SCM/Startup.cs'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Add using Microsoft.AspNetCore.DataProtection;
using_target = "using Microsoft.AspNetCore.Authentication.Cookies;\n"
using_replacement = "using Microsoft.AspNetCore.Authentication.Cookies;\nusing Microsoft.AspNetCore.DataProtection;\n"

# Replace session block
session_target = """            //AI[MIGRATE_START]: session store stays IN-PROCESS MEMORY exactly like the origin (Web.config `<sessionState mode="InProc" timeout="60"/>`) — DECISION: Redis-backed session (SessionRedisConfig / AddStackExchangeRedisCache) is DEFERRED, cci.core.json ships SessionRedisConfig.UseSessionRedis=false. Why: production incident on STG10 (mbm-web 06_dead_config_keys_dedup.md §11) — a pod that cannot reach Redis took the whole site down through the session/DataProtection path — and nothing proves an scm-web pod reaches the Redis of app.config (192.168.12.112:6379). Cost: sessions are per process (lost on restart, not shared between replicas -> single replica or sticky routing). Cookie name/SameSite/Secure follow the gold apps (CC.SID = origin CookieNames.Session); holders of the old ASP.NET_SessionId cookie lose the session on deploy (fall through to /accounts/login) — announce at deploy time
            services.AddDistributedMemoryCache();
            services.AddSession(options =>
            {
                options.IdleTimeout = TimeSpan.FromMinutes(60);
                options.Cookie.Name = "CC.SID";
                options.Cookie.HttpOnly = true;
                options.Cookie.IsEssential = true;
                options.Cookie.SameSite = SameSiteMode.None;
                options.Cookie.SecurePolicy = CookieSecurePolicy.Always;
            });
            //AI[MIGRATE_END]"""

session_replacement = """            try
            {
                var redisConnStr = AppConfig.RedisCachingConnectionString;
                if (!string.IsNullOrWhiteSpace(redisConnStr))
                {
                    var redisOptions = StackExchange.Redis.ConfigurationOptions.Parse(redisConnStr);
                    redisOptions.AllowAdmin = true;
                    redisOptions.AbortOnConnectFail = false;
                    redisOptions.ConnectRetry = 1;
                    if (AppConfig.Instance.RedisDbNumber.HasValue)
                    {
                        redisOptions.DefaultDatabase = AppConfig.Instance.RedisDbNumber.Value;
                    }

                    services.AddStackExchangeRedisCache(options =>
                    {
                        options.ConfigurationOptions = redisOptions;
                        options.InstanceName = "SCM:";
                    });

                    var dataProtectionRedis = StackExchange.Redis.ConnectionMultiplexer.Connect(redisOptions);
                    services.AddDataProtection()
                        .SetApplicationName("CoC.Web.SCM")
                        .PersistKeysToStackExchangeRedis(dataProtectionRedis, "DataProtection-Keys:SCM");
                }
                else
                {
                    services.AddDistributedMemoryCache();
                }
            }
            catch
            {
                services.AddDistributedMemoryCache();
            }

            services.AddSession(options =>
            {
                options.IdleTimeout = TimeSpan.FromMinutes(60);
                options.Cookie.Name = "CC.SID";
                options.Cookie.HttpOnly = true;
                options.Cookie.IsEssential = true;
                options.Cookie.SameSite = SameSiteMode.None;
                options.Cookie.SecurePolicy = CookieSecurePolicy.Always;
            });"""

if using_target in text and session_target in text:
    text = text.replace(using_target, using_replacement, 1)
    text = text.replace(session_target, session_replacement, 1)
    clean_text = text.lstrip('\ufeff')
    clean_bytes = clean_text.encode('utf-8')
    with open(path, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + clean_bytes)
    print("Successfully updated Startup.cs with single BOM and LF")
else:
    print("Target strings not found in Startup.cs!")
    if using_target not in text:
        print("using_target missing")
    if session_target not in text:
        print("session_target missing")
