import json
from collections import Counter

with open(r'E:\Work\Place_Migrate\cci-scm-web\03_qa\reports\details\parity-summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

regressions = data.get('regressions', [])

stg10_statuses = Counter(r.get('stg10') for r in regressions)
stg4_statuses = Counter(r.get('stg4') for r in regressions)

failed_cases = [r for r in regressions if r.get('stg10') == 'failed']
timedout_cases = [r for r in regressions if r.get('stg10') == 'timedOut']
skipped_cases = [r for r in regressions if r.get('stg10') == 'skipped']

# Also check origin_fails (failures that occur on both)
origin_fails = data.get('origin_fails', [])

analysis = {
    "total_regressions": len(regressions),
    "stg10_status_counts": dict(stg10_statuses),
    "stg4_status_counts": dict(stg4_statuses),
    "failed_cases_count": len(failed_cases),
    "timedout_cases_count": len(timedout_cases),
    "skipped_cases_count": len(skipped_cases),
    "failed_cases": failed_cases,
    "timedout_sample": timedout_cases[:10],
    "skipped_sample": skipped_cases[:10],
    "total_origin_fails": len(origin_fails),
    "origin_fails_sample": origin_fails[:5]
}

with open(r'C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\scratch\reg_analysis.json', 'w', encoding='utf-8') as out:
    json.dump(analysis, out, indent=2, ensure_ascii=False)

print('Analysis completed.')
