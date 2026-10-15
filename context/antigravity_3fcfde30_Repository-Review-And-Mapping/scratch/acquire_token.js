const { chromium } = require('@playwright/test');
const http = require('http');

(async () => {
  // Setup local redirect receiver
  const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('ok');
  });
  await new Promise(r => server.listen(5104, r));

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const authUrl = 'https://ids1-stg.concung.vn/realms/master/protocol/openid-connect/auth?response_type=token&client_id=CCI.Swagger.ClientCredential&scope=CCI.Swagger&redirect_uri=http://localhost:5104/swagger/oauth2-redirect.html';
  await page.goto(authUrl);
  await page.locator('input[name="username"]').first().fill('2741');
  await page.locator('input[name="password"]').first().fill('Long123456');
  await page.locator('#btnLogin, input[name="login"]').first().click();

  await page.waitForURL(u => u.hash.includes('access_token='), { timeout: 20000 });
  const hash = new URL(page.url()).hash;
  const params = new URLSearchParams(hash.substring(1));
  const token = params.get('access_token');
  console.log('TOKEN_ACQUIRED_SUCCESS, token length:', token ? token.length : 0);
  
  if (token) {
    const fs = require('fs');
    const path = require('path');
    const authDir = 'E:\\Work\\Place_Migrate\\cci-store-location-web\\03_qa\\.auth';
    fs.mkdirSync(authDir, { recursive: true });
    fs.writeFileSync(path.join(authDir, 'token.json'), JSON.stringify({ access_token: token }), 'utf-8');
    console.log('Saved token to 03_qa/.auth/token.json');
  }

  await browser.close();
  server.close();
})().catch(e => {
  console.error('Error:', e);
  process.exit(1);
});
