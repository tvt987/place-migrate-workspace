import subprocess
import urllib.request
import json

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
out, _ = p.communicate('protocol=https\nhost=bitbucket.org\n\n')
token = dict(l.split('=', 1) for l in out.splitlines() if '=' in l).get('password')

url = 'https://api.bitbucket.org/2.0/repositories/concung/cci-scm-web/pullrequests'
payload = {
    'title': 'feat(qa): align activity-types, agent-service-products, and agent-services specs with screen design',
    'description': "Merge dev into staging10: align activity-types, agent-service-products, and agent-services specs with screen design",
    'source': {'branch': {'name': 'dev'}},
    'destination': {'branch': {'name': 'staging10'}},
    'close_source_branch': False
}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), method='POST')
req.add_header('Authorization', f'Bearer {token}')
req.add_header('Content-Type', 'application/json')

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        pr_id = res.get('id')
        html_url = res.get('links', {}).get('html', {}).get('href')
        print(f"[SUCCESS] Created PR #{pr_id}: {html_url}")
except Exception as e:
    print(f"[ERROR] {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())
