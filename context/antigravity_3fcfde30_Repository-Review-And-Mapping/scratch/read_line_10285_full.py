import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\.system_generated\logs\transcript_full.jsonl', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if i == 10285:
            content = json.loads(line).get('content', '')
            print(content)
            break
