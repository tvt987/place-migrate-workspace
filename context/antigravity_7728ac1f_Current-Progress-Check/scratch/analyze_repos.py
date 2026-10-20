import subprocess

repos = ['cci-timekeeping-web', 'cci-supplier-web', 'cci-common-web']

with open('scratch/analysis_report.txt', 'w', encoding='utf-8') as out:
    for r in repos:
        out.write(f"\n{'='*60}\n=== REPO: {r} ===\n{'='*60}\n")
        commits = subprocess.check_output(['git', '-C', r, 'log', '-n', '10', '--oneline', '--', 'app'], text=True, errors='replace').splitlines()
        for c_line in commits:
            cid = c_line.split()[0]
            out.write(f"\n--- Commit {c_line} ---\n")
            stat = subprocess.check_output(['git', '-C', r, 'show', '--stat', '--oneline', cid], text=True, errors='replace')
            out.write(stat + "\n")
            
            # If touching cs or csproj or config
            diff = subprocess.check_output(['git', '-C', r, 'show', cid], text=True, errors='replace')
            # Look for interesting patterns: DataProtection, Redis, Cookie, Json, EpPlus, ChildAction, ViewComponent
            for pattern in ['DataProtection', 'Redis', 'Cookie', 'Json', 'Excel', 'Normalize', 'ChildAction', 'ViewComponent', 'AutoMapper', 'Session']:
                if pattern.lower() in diff.lower():
                    out.write(f"  [Found keyword: {pattern}]\n")

print("Analysis report written to scratch/analysis_report.txt")
