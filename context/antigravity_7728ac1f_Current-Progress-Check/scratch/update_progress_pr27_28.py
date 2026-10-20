progress_path = r"E:\Work\Place_Migrate\WORKSPACE_PROGRESS.md"

with open(progress_path, "r", encoding="utf-8-sig") as f:
    content = f.read()

# Add PR #27 and PR #28 to store-location section
old_prs = "    - PR #26 (`dev -> staging` - 3D Parity Comparator & Interactive Viewer Matrix): https://bitbucket.org/concung/cci-store-location-web/pull-requests/26\n"
new_prs = old_prs + (
    "    - PR #27 (`dev -> staging10` - Fix renderParityTab ReferenceError): https://bitbucket.org/concung/cci-store-location-web/pull-requests/27\n"
    "    - PR #28 (`dev -> staging` - Fix renderParityTab ReferenceError): https://bitbucket.org/concung/cci-store-location-web/pull-requests/28\n"
)

if old_prs in content:
    content = content.replace(old_prs, new_prs)

content = content.lstrip('\ufeff')
with open(progress_path, "w", encoding="utf-8-sig", newline='\n') as f:
    f.write(content)

print("Updated WORKSPACE_PROGRESS.md successfully with UTF-8 BOM.")
