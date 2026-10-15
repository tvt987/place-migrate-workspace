const fs = require('fs');

function patch(filePath, target, repl) {
    const b = fs.readFileSync(filePath);
    let s = b.toString('utf8');
    if (!s.includes(target)) {
        console.error(`Target not found in ${filePath}!`);
        return;
    }
    s = s.replace(target, repl);
    const clean = s.replace(/^\ufeff/, '');
    const out = Buffer.concat([Buffer.from([0xef, 0xbb, 0xbf]), Buffer.from(clean, 'utf8')]);
    fs.writeFileSync(filePath, out);
    console.log(`Successfully patched ${filePath}`);
}

patch(
    'e:/Work/Place_Migrate/cci-scm-web/02_target/CoC.Web.SCM/Controllers/PaymentReceiptPartnersController.cs',
    `                if (keySearch != "")
                {
                    result = result.Where(c =>
                        (
                            (c.PartnerTypeID == 1 && (
                                c.BankMasterName.Trim().ToLower().Contains(keySearch.Trim().ToLower()) ||
                                c.BankMasterNameEN.Trim().ToLower().Contains(keySearch.Trim().ToLower()) ||
                                c.BankMasterShortName.Trim().ToLower().Contains(keySearch.Trim().ToLower()))
                            ) ||
                            (c.PartnerTypeID == 2 && c.PaymentReceiptPartnerName.Trim().ToLower().Contains(keySearch.Trim().ToLower()))
                        )).ToList();
                }`,
    `                if (!string.IsNullOrWhiteSpace(keySearch))
                {
                    string trimmedKey = keySearch.Trim().ToLower();
                    result = result.Where(c =>
                        (
                            (c.PartnerTypeID == 1 && (
                                (!string.IsNullOrEmpty(c.BankMasterName) && c.BankMasterName.Trim().ToLower().Contains(trimmedKey)) ||
                                (!string.IsNullOrEmpty(c.BankMasterNameEN) && c.BankMasterNameEN.Trim().ToLower().Contains(trimmedKey)) ||
                                (!string.IsNullOrEmpty(c.BankMasterShortName) && c.BankMasterShortName.Trim().ToLower().Contains(trimmedKey)))
                            ) ||
                            (c.PartnerTypeID == 2 && !string.IsNullOrEmpty(c.PaymentReceiptPartnerName) && c.PaymentReceiptPartnerName.Trim().ToLower().Contains(trimmedKey))
                        )).ToList();
                }`
);

patch(
    'e:/Work/Place_Migrate/cci-scm-web/02_target/CoC.Web.SCM/Controllers/PaymentTypeInStoresController.cs',
    `                if (keySearch != "")
                {
                    result = result.Where(c => c.PaymentTypeName.ToLower().Contains(keySearch)).ToList();
                }`,
    `                if (!string.IsNullOrWhiteSpace(keySearch))
                {
                    string trimmedKey = keySearch.Trim().ToLower();
                    result = result.Where(c => !string.IsNullOrEmpty(c.PaymentTypeName) && c.PaymentTypeName.ToLower().Contains(trimmedKey)).ToList();
                }`
);
