const fs = require('fs');

const stg10 = JSON.parse(fs.readFileSync('E:/Work/Place_Migrate/cci-scm-web/03_qa/reports/details/test-mssql-report-20261012-144036.json', 'utf8'));
const stg4 = JSON.parse(fs.readFileSync('E:/Work/Place_Migrate/cci-scm-web/03_qa/reports/details/test-net4-report-latest.json', 'utf8'));

function isPass(status) { return status === 'passed'; }
function isFail(status) { return status === 'failed' || status === 'timedOut'; }

const stg4Map = new Map();
Object.values(stg4.screens).forEach(screen => {
  (screen.tests || []).forEach(t => {
    const key = t.tc ? `${screen.screen}:::${t.tc}` : `${screen.screen}:::${t.scenario}`;
    stg4Map.set(key, { screen: screen.screen, ...t });
  });
});

const parityFails = []; // STG4 pass -> STG10 fail
const bothFails = [];   // Cả 2 cùng fail
const stg10OnlyFails = [];

Object.values(stg10.screens).forEach(screen => {
  (screen.tests || []).forEach(t => {
    if (isFail(t.status)) {
      const key = t.tc ? `${screen.screen}:::${t.tc}` : `${screen.screen}:::${t.scenario}`;
      const t4 = stg4Map.get(key);
      if (t4) {
        if (isPass(t4.status)) {
          parityFails.push({
            screen: screen.screen,
            tc: t.tc,
            scenario: t.scenario,
            dimension: t.dimension,
            route: t.observedRoute,
            error: t.error || '',
            stg4Status: t4.status,
            stg10Status: t.status
          });
        } else if (isFail(t4.status)) {
          bothFails.push({
            screen: screen.screen,
            tc: t.tc,
            scenario: t.scenario,
            error: t.error || ''
          });
        }
      } else {
        stg10OnlyFails.push({
          screen: screen.screen,
          tc: t.tc,
          scenario: t.scenario,
          error: t.error || ''
        });
      }
    }
  });
});

console.log('========================================================');
console.log(`TỔNG SỐ TEST BỊ FAIL TRÊN STG10: ${parityFails.length + bothFails.length + stg10OnlyFails.length}`);
console.log(`1. PARITY FAILS (STG4 PASS -> STG10 FAIL): ${parityFails.length} tests`);
console.log(`2. CẢ HAI CÙNG FAIL (Lỗi chung của STG): ${bothFails.length} tests`);
console.log(`3. Test chỉ có trên STG10 và FAIL: ${stg10OnlyFails.length} tests`);
console.log('========================================================\n');

// Gom nhóm Parity Fails theo Screen
const parityByScreen = new Map();
parityFails.forEach(item => {
  if (!parityByScreen.has(item.screen)) parityByScreen.set(item.screen, []);
  parityByScreen.get(item.screen).push(item);
});

console.log(`CÓ TỔNG CỘNG ${parityByScreen.size} MÀN HÌNH BỊ PARITY FAIL:`);

const summaryList = [];

for (const [screen, tests] of parityByScreen.entries()) {
  const testDetails = tests.map(t => {
    let cleanErr = (t.error || '').split('\n')[0].trim();
    if (cleanErr.length > 100) cleanErr = cleanErr.substring(0, 100) + '...';
    return {
      tc: t.tc,
      scenario: t.scenario,
      error: cleanErr
    };
  });
  summaryList.push({ screen, count: tests.length, tests: testDetails });
}

// Sắp xếp theo số lượng fail giảm dần
summaryList.sort((a, b) => b.count - a.count);

summaryList.forEach(s => {
  console.log(`\n📌 [${s.screen}] - ${s.count} lỗi:`);
  s.tests.forEach(t => {
    console.log(`   * ${t.tc ? '[' + t.tc + '] ' : ''}${t.scenario}`);
    if (t.error) console.log(`     -> Lỗi: ${t.error}`);
  });
});

fs.writeFileSync('C:/Users/25303_TruongVanTinh/.gemini/antigravity-ide/brain/3fcfde30-4110-403c-8f9f-a4ed95abc9e6/scratch/parity_fails_detailed.json', JSON.stringify(summaryList, null, 2));
