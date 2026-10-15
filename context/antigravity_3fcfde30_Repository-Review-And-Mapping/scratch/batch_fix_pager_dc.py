import glob

files = glob.glob(r'e:\Work\Place_Migrate\cci-dc-web\03_qa\pages\*.page.ts')
matched = []
target = "this.pager().locator('a, button, li, span').filter({ hasText: /^\\s*2\\s*$/ })"
replacement = "this.pager().locator('a, button').filter({ hasText: /^\\s*2\\s*$/ })"

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    if target in content:
        matched.append(f)
        new_content = content.replace(target, replacement)
        with open(f, 'w', encoding='utf-8', newline='') as fp:
            fp.write(new_content)

print(f'Replaced in {len(matched)} files in cci-dc-web.')
