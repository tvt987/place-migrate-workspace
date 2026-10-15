import subprocess
import urllib.request
import urllib.error
import json

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, _ = p.communicate('protocol=https\nhost=bitbucket.org\n\n')
creds = dict(l.split('=', 1) for l in out.splitlines() if '=' in l)

token = creds.get('password')
req = urllib.request.Request('https://api.bitbucket.org/2.0/repositories/concung/cci-scm-web/pullrequests?state=OPEN')
req.add_header('Authorization', f'Bearer {token}')

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print('Bearer SUCCESS! Open PRs count:', len(data.get('values', [])))
        for pr in data.get('values', []):
            print(f"#{pr.get('id')}: {pr.get('title')} ({pr.get('source', {}).get('branch', {}).get('name')} -> {pr.get('destination', {}).get('branch', {}).get('name')})")
            print(f"  URL: {pr.get('links', {}).get('html', {}).get('href')}")
except urllib.error.HTTPError as e:
    print('Bearer HTTP ERROR:', e.code, e.read().decode())
