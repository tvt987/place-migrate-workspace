import subprocess, urllib.request, json
p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, _ = p.communicate('protocol=https\nhost=bitbucket.org\n\n')
creds = dict(l.split('=', 1) for l in out.splitlines() if '=' in l)
token = creds.get('password')

for repo, pr_id in [('concung/cci-scm-web', 6), ('concung/cci-dc-web', 5), ('concung/cci-dc-web', 6), ('concung/cci-store-location-web', 5), ('concung/cci-store-location-web', 6)]:
    req = urllib.request.Request(f'https://api.bitbucket.org/2.0/repositories/{repo}/pullrequests/{pr_id}')
    req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"{repo} #{pr_id}: state={data.get('state')} ({data.get('source', {}).get('branch', {}).get('name')} -> {data.get('destination', {}).get('branch', {}).get('name')})")
    except Exception as e:
        print(f"{repo} #{pr_id} error: {e}")
