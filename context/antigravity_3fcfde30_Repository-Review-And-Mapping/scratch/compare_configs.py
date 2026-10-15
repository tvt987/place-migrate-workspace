import json
import subprocess
import re

def strip_json_comments(text):
    text = re.sub(r'//.*', '', text)
    return text

raw_dev = subprocess.check_output(['git', 'show', 'origin/dev:02_target/CoC.Web.SCM/appsettings.json']).decode('utf-8-sig')
raw_dev_clean = strip_json_comments(raw_dev)
dev_cfg = json.loads(raw_dev_clean, strict=False)

with open('e:/Work/dev-ops/vaults-gitops/stg/cci/scm/scm-web-mssql/configs/appsettings.json', encoding='utf-8-sig') as f:
    gitops_cfg = json.load(f, strict=False)

print("=== Top Level Sections ===")
print("dev:   ", list(dev_cfg.keys()))
print("gitops:", list(gitops_cfg.keys()))

dev_cc = dev_cfg.get("CommonConfig", {})
gitops_cc = gitops_cfg.get("CommonConfig", {})

print("\n=== CommonConfig comparison ===")
print("Keys only in dev CommonConfig:", [k for k in dev_cc if k not in gitops_cc])
print("Keys only in gitops CommonConfig:", [k for k in gitops_cc if k not in dev_cc])

print("\nOauth2ForWeb in dev:", dev_cc.get("Oauth2ForWeb"))
print("Oauth2ForWeb in gitops:", gitops_cc.get("Oauth2ForWeb"))

if "AppSettings" in gitops_cfg:
    print("\nKeys in gitops AppSettings:", list(gitops_cfg["AppSettings"].keys()))

print("\n=== ClientUrl ===")
print("dev ClientUrl:   ", dev_cc.get("ClientUrl"))
print("gitops ClientUrl:", gitops_cc.get("ClientUrl"))
