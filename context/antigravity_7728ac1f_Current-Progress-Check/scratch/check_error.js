const { chromium } = require('@playwright/test');
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ storageState: '.auth/state.json' });
  const page = await ctx.newPage();
  await page.goto('https://place-stg10.concung.vn/Home/Index');
  const html = await page.content();
  const match = html.match(/objEx\.Message\s*:\s*([^<]+)/);
  if (match) {
    console.log('FOUND EXCEPTION MESSAGE:', match[1].trim());
  } else {
    console.log('No objEx.Message found. Searching for error text...');
    const bodyText = await page.locator('body').innerText();
    console.log('Body Text snippet:\n', bodyText.slice(0, 500));
  }
  const matchStep = html.match(/objCodeStep\.ErrorMessage\s*:\s*([^<]+)/);
  if (matchStep) {
    console.log('FOUND CODESTEP ERROR:', matchStep[1].trim());
  }
  await browser.close();
})();
