import subprocess
import os

env = os.environ.copy()
env['BASE_URL'] = 'https://place-stg10.concung.vn/'
env['APP_ENV'] = 'NET10_MSSQL'
env['UPLOAD_REPORT'] = '0'

print("=== Starting Targeted Test on cci-store-location-web STG10 ===")
print("Target specs: e2e/home, e2e/login")
print("Target URL: https://place-stg10.concung.vn/")

cmd = ['cmd.exe', '/c', 'npx playwright test e2e/home e2e/login --project=e2e']
res = subprocess.run(cmd, cwd='e:/Work/Place_Migrate/cci-store-location-web/03_qa', env=env, text=True)
print("=== Targeted Test Finished with exit code:", res.returncode)
