with open('e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

old_pr_block = """    - PR #15 (`dev -> staging10`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/15 (Auto-merged)
    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/16"""

new_pr_block = """    - PR #15 (`dev -> staging10`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/15 (Auto-merged)
    - PR #16 (`dev -> staging`): https://bitbucket.org/concung/cci-store-location-web/pull-requests/16
    - PR #17 (`dev -> staging10` - Tooling): https://bitbucket.org/concung/cci-store-location-web/pull-requests/17
    - PR #18 (`dev -> staging` - Tooling): https://bitbucket.org/concung/cci-store-location-web/pull-requests/18"""

if old_pr_block in text:
    text = text.replace(old_pr_block, new_pr_block)
    with open('e:/Work/Place_Migrate/WORKSPACE_PROGRESS.md', 'wb') as f:
        f.write(bytes([0xEF, 0xBB, 0xBF]) + text.encode('utf-8'))
    print("WORKSPACE_PROGRESS.md updated with PR #17 & #18")
else:
    print("Could not find old_pr_block")
