import subprocess
import urllib.request
import urllib.error
import json

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, _ = p.communicate('protocol=https\nhost=bitbucket.org\n\n')
creds = dict(l.split('=', 1) for l in out.splitlines() if '=' in l)
token = creds.get('password')

# Check default reviewers
req = urllib.request.Request('https://api.bitbucket.org/2.0/repositories/concung/cci-scm-web/default-reviewers')
req.add_header('Authorization', f'Bearer {token}')

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print('Default reviewers:', [r.get('display_name') for r in data.get('values', [])])
except urllib.error.HTTPError as e:
    print('Default reviewers error:', e.code)
