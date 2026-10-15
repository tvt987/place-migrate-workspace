import glob
import os

repo_dir = r"e:\Work\Place_Migrate\cci-scm-web"
pages_dir = os.path.join(repo_dir, "03_qa", "pages", "*.page.ts")
files = glob.glob(pages_dir)

target = "this.page.locator('#content input[type=\"text\"]').first()"
replacement = "this.page.locator('#content input[type=\"text\"]:not([readonly])').first()"

matched = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    if target in content:
        matched.append(f)
        new_content = content.replace(target, replacement)
        with open(f, 'w', encoding='utf-8', newline='') as fp:
            fp.write(new_content)

print(f"Replaced {len(matched)} files.")
