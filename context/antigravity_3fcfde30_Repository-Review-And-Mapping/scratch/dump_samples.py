import json

with open(r'E:\Work\Place_Migrate\cci-scm-web\03_qa\reports\details\parity-summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

regressions = data.get('regressions', [])

with open(r'C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\scratch\reg_keys.json', 'w', encoding='utf-8') as out:
    json.dump(regressions[:3], out, indent=2, ensure_ascii=False)

print('Dumped first 3 regressions')
