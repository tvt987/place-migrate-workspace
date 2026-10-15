import subprocess, urllib.request, json

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, _ = p.communicate('protocol=https\nhost=bitbucket.org\n\n')
creds = dict(l.split('=', 1) for l in out.splitlines() if '=' in l)
token = creds.get('password')

for repo in ['concung/cci-scm-web', 'concung/cci-dc-web', 'concung/cci-store-location-web']:
    print(f'=== {repo} ===')
    req = urllib.request.Request(f'https://api.bitbucket.org/2.0/repositories/{repo}/pullrequests?state=OPEN')
    req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            prs = data.get('values', [])
            if not prs:
                print('  No open PRs found.')
            for pr in prs:
                src = pr.get('source', {}).get('branch', {}).get('name')
                dst = pr.get('destination', {}).get('branch', {}).get('name')
                print(f"  #{pr.get('id')}: {pr.get('title')} ({src} -> {dst})")
                print(f"    {pr.get('links', {}).get('html', {}).get('href')}")
    except Exception as e:
        print('  Error:', e)
