#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import urllib.request
import urllib.error
import json
import sys
import argparse

def get_bitbucket_token():
    try:
        p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, _ = p.communicate('protocol=https\nhost=bitbucket.org\n\n')
        creds = dict(l.split('=', 1) for l in out.splitlines() if '=' in l)
        return creds.get('password')
    except Exception as e:
        print(f"[ERROR] Failed to get git credentials: {e}", file=sys.stderr)
        return None

def create_pull_request(repo, src="dev", dest="staging10", title=None, description=""):
    token = get_bitbucket_token()
    if not token:
        print("[ERROR] No Bitbucket token available from git credential", file=sys.stderr)
        return None

    if not title:
        title = f"Merge branch '{src}' into {dest}"

    url = f"https://api.bitbucket.org/2.0/repositories/{repo}/pullrequests"
    payload = {
        "title": title,
        "description": description or f"Merge branch '{src}' into {dest}",
        "source": {"branch": {"name": src}},
        "destination": {"branch": {"name": dest}},
        "close_source_branch": False
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req) as resp:
            res_data = json.loads(resp.read().decode("utf-8"))
            pr_id = res_data.get("id")
            html_url = res_data.get("links", {}).get("html", {}).get("href")
            print(f"[SUCCESS] Created PR #{pr_id}: {src} -> {dest}")
            print(f"  URL: {html_url}")
            return {"id": pr_id, "url": html_url, "data": res_data}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        # Check if already exists
        if e.code == 400 and "There is already an open pull request" in err_msg:
            print(f"[INFO] PR {src} -> {dest} already exists. Finding existing PR...")
            existing = find_existing_pr(repo, src, dest, token)
            if existing:
                return existing
        print(f"[ERROR {e.code}] Failed to create PR {src} -> {dest}: {err_msg}", file=sys.stderr)
        return None

def find_existing_pr(repo, src, dest, token=None):
    if not token:
        token = get_bitbucket_token()
    url = f"https://api.bitbucket.org/2.0/repositories/{repo}/pullrequests?state=OPEN"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req) as resp:
            res_data = json.loads(resp.read().decode("utf-8"))
            for pr in res_data.get("values", []):
                s = pr.get("source", {}).get("branch", {}).get("name")
                d = pr.get("destination", {}).get("branch", {}).get("name")
                if s == src and d == dest:
                    pr_id = pr.get("id")
                    html_url = pr.get("links", {}).get("html", {}).get("href")
                    print(f"  Existing PR #{pr_id}: {html_url}")
                    return {"id": pr_id, "url": html_url, "data": pr}
    except Exception as e:
        print(f"[WARN] Error finding existing PR: {e}", file=sys.stderr)
    return None

def list_open_prs(repo):
    token = get_bitbucket_token()
    url = f"https://api.bitbucket.org/2.0/repositories/{repo}/pullrequests?state=OPEN"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        res_data = json.loads(resp.read().decode("utf-8"))
        prs = res_data.get("values", [])
        print(f"=== Open PRs for {repo} ({len(prs)}) ===")
        for pr in prs:
            pr_id = pr.get("id")
            s = pr.get("source", {}).get("branch", {}).get("name")
            d = pr.get("destination", {}).get("branch", {}).get("name")
            title = pr.get("title")
            url = pr.get("links", {}).get("html", {}).get("href")
            print(f"- #{pr_id}: {title} ({s} -> {d})\n  {url}")
        return prs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bitbucket PR Manager")
    parser.add_argument("--repo", required=True, help="Repo in format concung/cci-xxx")
    parser.add_argument("--action", choices=["create", "create-pair", "list"], default="create-pair")
    parser.add_argument("--src", default="dev")
    parser.add_argument("--dest", default="staging10")
    parser.add_argument("--title", default=None)
    parser.add_argument("--desc", default="")

    args = parser.parse_args()

    if args.action == "list":
        list_open_prs(args.repo)
    elif args.action == "create":
        create_pull_request(args.repo, args.src, args.dest, args.title, args.desc)
    elif args.action == "create-pair":
        print(f"=== Creating pair of PRs (dev -> staging10 and dev -> staging) for {args.repo} ===")
        pr1 = create_pull_request(args.repo, args.src, "staging10", args.title, args.desc)
        pr2 = create_pull_request(args.repo, args.src, "staging", args.title, args.desc)
