import subprocess
import os

repos = [
    ('cci-timekeeping-web', 'https://tinhkun102@bitbucket.org/concung/cci-timekeeping-web.git'),
    ('cci-supplier-web', 'https://tinhkun102@bitbucket.org/concung/cci-supplier-web.git'),
    ('cci-common-web', 'https://tinhkun102@bitbucket.org/concung/cci-common-web.git')
]

for name, url in repos:
    if not os.path.exists(name):
        print(f"=== Cloning {name} ===")
        res = subprocess.run(['git', 'clone', url, name], capture_output=True, text=True)
        print(res.stdout)
        print(res.stderr)
        if res.returncode == 0:
            print(f"Successfully cloned {name}")
        else:
            print(f"Failed to clone {name} (code {res.returncode})")
    else:
        print(f"=== {name} exists, pulling dev ===")
        subprocess.run(['git', '-C', name, 'fetch', 'origin', 'dev'])
        subprocess.run(['git', '-C', name, 'checkout', 'dev'])
        subprocess.run(['git', '-C', name, 'pull', 'origin', 'dev'])

print("All reference repos processed.")
