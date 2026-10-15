const fs = require('fs');

const stg10 = JSON.parse(fs.readFileSync('E:/Work/Place_Migrate/cci-scm-web/03_qa/reports/details/test-mssql-report-20261012-144036.json', 'utf8'));
const stg4 = JSON.parse(fs.readFileSync('E:/Work/Place_Migrate/cci-scm-web/03_qa/reports/details/test-net4-report-latest.json', 'utf8'));

// Map stg4 tests
const stg4Map = new Map();
Object.values(stg4.screens).forEach(screen => {
  (screen.tests || []).forEach(t => {
    const key = `${screen.screen}:::${t.tc || ''}:::${t.scenario || ''}`;
    stg4Map.set(key, t);
  });
});

const parityFails = []; // STG4 pass, STG10 fail
const bothFails = [];   // Cả 2 cùng fail

Object.values(stg10.screens).forEach(screen => {
  (screen.tests || []).forEach(t => {
    if (t.status === 'failed') {
      const key = `${screen.screen}:::${t.tc || ''}:::${t.scenario || ''}`;
      const t4 = stg4Map.get(key);
      if (t4 && t4.status === 'passed') {
        parityFails.push({
          screen: screen.screen,
          tc: t.tc,
          scenario: t.scenario,
          dimension: t.dimension,
          error: t.error || '',
          stg4Status: t4.status,
          stg10Status: t.status
        });
      } else if (t4 && t4.status === 'failed') {
        bothFails.push({
          screen: screen.screen,
          tc: t.tc,
          scenario: t.scenario,
          error: t.error || ''
        });
      }
    }
  });
});

console.log(`TỔNG SỐ PARITY FAILS (STG4 PASS -> STG10 FAIL): ${parityFails.length}`);
console.log(`TỔNG SỐ CẢ 2 CÙNG FAIL (Lỗi môi trường/Data chung): ${bothFails.length}\n`);

// Phân nhóm Parity Fails theo lỗi
const categorized = {
  titleDiff: [],       // Lệch title/khoảng trắng
  autoSearchDiff: [],  // Lệch cờ auto-search (origin không tự search khi mở index)
  visibility: [],      // Element/grid không hiển thị
  apiDiff: [],         // Lệch API / POST / HTTP response
  validation: [],      // Lỗi form validation
  other: []
};

parityFails.forEach(item => {
  const err = item.error || '';
  if (err.includes('title=') || err.includes('page.title')) {
    categorized.titleDiff.push(item);
  } else if (err.includes('không tự Search khi mở Index') || err.includes('auto-search')) {
    categorized.autoSearchDiff.push(item);
  } else if (err.includes('toBeVisible') || err.includes('not visible')) {
    categorized.visibility.push(item);
  } else if (err.includes('kỳ vọng POST') || err.includes('API') || err.includes('SearchStore') || err.includes('response')) {
    categorized.apiDiff.push(item);
  } else if (err.includes('validation') || err.includes('chặn ghi')) {
    categorized.validation.push(item);
  } else {
    categorized.other.push(item);
  }
});

console.log('=== PHÂN LOẠI PARITY FAIL THEO BẢN CHẤT LỖI ===');
console.log(`1. Lệch Auto-Search khi mở Index: ${categorized.autoSearchDiff.length} tests`);
console.log(`2. Lỗi Element / Grid Visibility (Chưa render hoặc lệch selector): ${categorized.visibility.length} tests`);
console.log(`3. Lệch Tiêu đề trang (Title mismatch - thừa dấu cách/chữ): ${categorized.titleDiff.length} tests`);
console.log(`4. Lệch API / Endpoint POST/GET: ${categorized.apiDiff.length} tests`);
console.log(`5. Lệch Form Validation / Chặn ghi: ${categorized.validation.length} tests`);
console.log(`6. Các lỗi khác: ${categorized.other.length} tests`);

fs.writeFileSync('C:/Users/25303_TruongVanTinh/.gemini/antigravity-ide/brain/3fcfde30-4110-403c-8f9f-a4ed95abc9e6/scratch/parity_fails_full.json', JSON.stringify({
  totalParityFails: parityFails.length,
  categorized,
  parityFails
}, null, 2));

console.log('\nĐã xuất file chi tiết: scratch/parity_fails_full.json');
