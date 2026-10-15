import subprocess, urllib.request, urllib.error, json

def get_token():
    p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, _ = p.communicate('protocol=https\nhost=bitbucket.org\n\n')
    creds = dict(l.split('=', 1) for l in out.splitlines() if '=' in l)
    return creds.get('password')

def create_pull_request(repo, src, dest, title, description=""):
    token = get_token()
    url = f'https://api.bitbucket.org/2.0/repositories/{repo}/pullrequests'
    payload = {
        "title": title,
        "description": description or f"Merge branch '{src}' into {dest}",
        "source": {"branch": {"name": src}},
        "destination": {"branch": {"name": dest}},
        "close_source_branch": False
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Authorization', f'Bearer {token}')
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req) as resp:
            res_data = json.loads(resp.read().decode('utf-8'))
            pr_id = res_data.get('id')
            html_url = res_data.get('links', {}).get('html', {}).get('href')
            print(f"[SUCCESS] Created PR #{pr_id}: {title}")
            print(f"  URL: {html_url}")
            return res_data
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8')
        print(f"[ERROR {e.code}] Failed to create PR for {src} -> {dest}: {err_msg}")
        return None

if __name__ == '__main__':
    repo = "concung/cci-dc-web"
    print("=== Creating PRs for cci-dc-web ===")
    create_pull_request(repo, "dev", "staging10", "Merge dev into staging10", "fix(qa): update pagerPage2 selector in page objects to target clickable link")
    create_pull_request(repo, "dev", "staging", "Merge dev into staging", "fix(qa): update pagerPage2 selector in page objects to target clickable link")
