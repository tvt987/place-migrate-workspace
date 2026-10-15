const https = require('https');

async function getToken() {
  const postData = new URLSearchParams({
    client_id: 'scm.ClientCredential',
    client_secret: '6D9F85',
    scope: 'scm-api',
    grant_type: 'client_credentials'
  }).toString();

  return new Promise((resolve, reject) => {
    const req = https.request('https://ids1-stg.concung.vn/realms/master/protocol/openid-connect/token', {
      method: 'POST',
      rejectUnauthorized: false,
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': Buffer.byteLength(postData)
      }
    }, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          resolve(json.access_token);
        } catch (e) {
          reject(e);
        }
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function callSearch(url, token, body, headers = {}) {
  return new Promise((resolve) => {
    const postData = JSON.stringify(body);
    const parsedUrl = new URL(url);
    const options = {
      hostname: parsedUrl.hostname,
      port: 443,
      path: parsedUrl.pathname,
      method: 'POST',
      rejectUnauthorized: false,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        'UserID': '2741',
        'Content-Length': Buffer.byteLength(postData),
        ...headers
      }
    };

    const req = https.request(options, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        resolve({
          statusCode: res.statusCode,
          headers: res.headers,
          body: data
        });
      });
    });
    req.on('error', err => resolve({ error: err.message }));
    req.write(postData);
    req.end();
  });
}

async function main() {
  console.log('1. Lấy token...');
  const token = await getToken();
  console.log('Token OK, length:', token.length);

  const searchReq = {
    PageIndex: 0,
    PageSize: 20,
    FromDate: '2026-09-01T00:00:00',
    ToDate: '2026-10-12T23:59:59',
    StoreID: 31,
    CustomerID: -1,
    KeySearch: null
  };

  console.log('\n2. Test STG4: https://scm-api-stg4.concung.vn/api/BonusOutputSales/Search');
  const res4 = await callSearch('https://scm-api-stg4.concung.vn/api/BonusOutputSales/Search', token, searchReq, {
    'Accept': 'application/json'
  });
  console.log('STG4 Status:', res4.statusCode);
  console.log('STG4 Headers:', res4.headers);
  console.log('STG4 Body:', res4.body?.substring(0, 500));

  console.log('\n3. Test STG10: https://scm-api-stg10.concung.vn/api/BonusOutputSales/Search');
  const res10 = await callSearch('https://scm-api-stg10.concung.vn/api/BonusOutputSales/Search', token, searchReq, {
    'Accept': 'application/json'
  });
  console.log('STG10 Status:', res10.statusCode);
  console.log('STG10 Headers:', res10.headers);
  console.log('STG10 Body:', res10.body?.substring(0, 500));

  console.log('\n4. Test STG10 với Header Accept Protobuf');
  const res10Proto = await callSearch('https://scm-api-stg10.concung.vn/api/BonusOutputSales/Search', token, searchReq, {
    'Accept': 'application/x-protobuf'
  });
  console.log('STG10 (Accept protobuf) Status:', res10Proto.statusCode);
  console.log('STG10 (Accept protobuf) Body:', res10Proto.body?.substring(0, 500));
}

main().catch(console.error);
