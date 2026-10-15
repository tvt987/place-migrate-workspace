import subprocess
import urllib.request
import urllib.error
import base64
import json
import sys

def get_creds():
    p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate('protocol=https\nhost=bitbucket.org\n\n')
    creds = dict(line.split('=', 1) for line in out.splitlines() if '=' in line)
    return creds.get('username'), creds.get('password')

def list_open_prs():
    user, pwd = get_creds()
    auth = base64.b64encode(f'{user}:{pwd}'.encode()).decode()
    url = 'https://api.bitbucket.org/2.0/repositories/concung/cci-scm-web/pullrequests?state=OPEN'
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Basic {auth}')
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print('SUCCESS! Open PRs count:', len(data.get('values', [])))
            for pr in data.get('values', []):
                print(f"  #{pr.get('id')}: {pr.get('title')} ({pr.get('source', {}).get('branch', {}).get('name')} -> {pr.get('destination', {}).get('branch', {}).get('name')})")
                print(f"    URL: {pr.get('links', {}).get('html', {}).get('href')}")
            return data.get('values', [])
    except urllib.error.HTTPError as e:
        print('HTTP ERROR:', e.code, e.read().decode())
        return []

if __name__ == '__main__':
    list_open_prs()
