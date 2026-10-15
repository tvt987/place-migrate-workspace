const fs = require('fs');

const newRep = JSON.parse(fs.readFileSync('E:/Work/Place_Migrate/cci-scm-web/03_qa/reports/details/test-mssql-report-20261012-144036.json', 'utf8'));
const oldRep = JSON.parse(fs.readFileSync('E:/Work/Place_Migrate/cci-scm-web/03_qa/reports/details/test-mssql-report-20261008-192415.json', 'utf8'));
const net4Rep = JSON.parse(fs.readFileSync('E:/Work/Place_Migrate/cci-scm-web/03_qa/reports/details/test-net4-report-latest.json', 'utf8'));

console.log('========================================================');
console.log('1. TỔNG QUAN SUITE TEST:');
console.log('STG4 (Oracle NET4)      : Passed = ' + net4Rep.summary.passed + ' | Failed = ' + net4Rep.summary.failed + ' | Skipped = ' + net4Rep.summary.skipped);
console.log('STG10 CŨ (2026-10-08)   : Passed = ' + oldRep.summary.passed + ' | Failed = ' + oldRep.summary.failed + ' | Skipped = ' + oldRep.summary.skipped);
console.log('STG10 MỚI (2026-10-12)  : Passed = ' + newRep.summary.passed + ' | Failed = ' + newRep.summary.failed + ' | Skipped = ' + newRep.summary.skipped);
console.log('-> Tăng: +' + (newRep.summary.passed - oldRep.summary.passed) + ' Passed | Giảm: -' + (oldRep.summary.failed - newRep.summary.failed) + ' Failed');
console.log('========================================================\n');

console.log('2. CÁC MÀN HÌNH QUẢN LÝ SẢN PHẨM & KHO VỪA ĐƯỢC FIX:');
const checkScreens = [
  'product-category-g-ms',
  'product-category-weights',
  'product-categories',
  'store-change-requests',
  'stores',
  'store-groups',
  'product-group-vouchers'
];

Object.values(newRep.screens).forEach(s => {
  const scKey = s.screen.toLowerCase();
  if (checkScreens.some(k => scKey.includes(k))) {
    const o = Object.values(oldRep.screens).find(x => x.screen === s.screen);
    const n = Object.values(net4Rep.screens).find(x => x.screen === s.screen);
    console.log('[' + s.screen + ']');
    console.log('  STG4 (Oracle) : Pass = ' + (n ? n.passed : 0) + ' / ' + (n ? n.total : 0) + ', Fail = ' + (n ? n.failed : 0));
    console.log('  STG10 Cũ      : Pass = ' + (o ? o.passed : 0) + ' / ' + (o ? o.total : 0) + ', Fail = ' + (o ? o.failed : 0));
    console.log('  STG10 Mới     : Pass = ' + s.passed + ' / ' + s.total + ', Fail = ' + s.failed);
  }
});

console.log('\n========================================================');
console.log('3. TOP CÁC MÀN HÌNH CẢI THIỆN NHIỀU NHẤT TRONG ĐỢT NÀY:');
const improved = [];
Object.values(newRep.screens).forEach(s => {
  const o = Object.values(oldRep.screens).find(x => x.screen === s.screen);
  if (o && s.passed > o.passed) {
    improved.push({
      screen: s.screen,
      diffPass: s.passed - o.passed,
      diffFail: o.failed - s.failed,
      nowPass: s.passed,
      oldPass: o.passed,
      total: s.total
    });
  }
});

improved.sort((a, b) => b.diffPass - a.diffPass);
improved.forEach(item => {
  console.log('  * ' + item.screen + ': +' + item.diffPass + ' passed (' + item.oldPass + ' -> ' + item.nowPass + '/' + item.total + '), fail giảm ' + item.diffFail);
});
