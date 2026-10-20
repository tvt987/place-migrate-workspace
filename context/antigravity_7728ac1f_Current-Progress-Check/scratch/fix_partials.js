const fs = require('fs');
const path = require('path');

const scmRoot = 'e:/Work/Place_Migrate/cci-scm-web/02_target/CoC.Web.SCM/Views/PayForms';

function fixFile(filePath, replacements) {
    const fullPath = path.join(scmRoot, filePath);
    let content = fs.readFileSync(fullPath, 'utf8');
    for (const [target, replacement] of replacements) {
        if (!content.includes(target)) {
            console.error(`Target not found in ${filePath}:`, target);
            process.exit(1);
        }
        content = content.replace(target, replacement);
    }
    // Ensure UTF-8 BOM and LF endings preserved
    const cleanContent = content.replace(/^\ufeff/, '');
    fs.writeFileSync(fullPath, '\ufeff' + cleanContent, 'utf8');
    console.log(`Updated ${filePath} successfully.`);
}

// 1. IndexOutputCache.cshtml
fixFile('IndexOutputCache.cshtml', [
    ['@await Html.PartialAsync("_ConfirmProcessDocUserSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_ConfirmProcessDocUserSearchModal.cshtml")']
]);

// 2. CreateOutputCache.cshtml
fixFile('CreateOutputCache.cshtml', [
    ['@await Html.PartialAsync("_PaymentDetail")', '@await Html.PartialAsync("~/Views/PayForms/_PaymentDetail.cshtml")'],
    ['@await Html.PartialAsync("_PayFormRequestDistributed")', '@await Html.PartialAsync("~/Views/PayForms/_PayFormRequestDistributed.cshtml")'],
    ['@await Html.PartialAsync("_OrderSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_OrderSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_OutputVoucherSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_OutputVoucherSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_AdvanceRequestSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_AdvanceRequestSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_AddDetailOrderModal")', '@await Html.PartialAsync("~/Views/PayForms/_AddDetailOrderModal.cshtml")'],
    ['@await Html.PartialAsync("_SupplierBankSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_SupplierBankSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_AddPaymentRecipient")', '@await Html.PartialAsync("~/Views/PayForms/_AddPaymentRecipient.cshtml")'],
    ['@await Html.PartialAsync("_PaymentAdvanceOrderSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_PaymentAdvanceOrderSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_SupplierObjectSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_SupplierObjectSearchModal.cshtml")']
]);

// 3. EditOutputCache.cshtml
fixFile('EditOutputCache.cshtml', [
    ['@await Html.PartialAsync("_PaymentDetail")', '@await Html.PartialAsync("~/Views/PayForms/_PaymentDetail.cshtml")'],
    ['@await Html.PartialAsync("_PayFormRequestDistributed")', '@await Html.PartialAsync("~/Views/PayForms/_PayFormRequestDistributed.cshtml")'],
    ['@await Html.PartialAsync("_PayFormDistributedModal")', '@await Html.PartialAsync("~/Views/PayForms/_PayFormDistributedModal.cshtml")'],
    ['@await Html.PartialAsync("_OrderSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_OrderSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_OutputVoucherSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_OutputVoucherSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_AdvanceRequestSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_AdvanceRequestSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_AddDetailOrderModal")', '@await Html.PartialAsync("~/Views/PayForms/_AddDetailOrderModal.cshtml")'],
    ['@await Html.PartialAsync("_AddPaymentRecipient")', '@await Html.PartialAsync("~/Views/PayForms/_AddPaymentRecipient.cshtml")'],
    ['@await Html.PartialAsync("_PaymentAdvanceOrderSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_PaymentAdvanceOrderSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_SupplierObjectSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_SupplierObjectSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_SupplierBankSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_SupplierBankSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_ConfirmProcessDocUserSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_ConfirmProcessDocUserSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_ConfirmProcessDocUserModal")', '@await Html.PartialAsync("~/Views/PayForms/_ConfirmProcessDocUserModal.cshtml")']
]);

// 4. EditCCAppOutputCache.cshtml
fixFile('EditCCAppOutputCache.cshtml', [
    ['@await Html.PartialAsync("_PaymentDetail")', '@await Html.PartialAsync("~/Views/PayForms/_PaymentDetail.cshtml")'],
    ['@await Html.PartialAsync("_PayFormRequestDistributed")', '@await Html.PartialAsync("~/Views/PayForms/_PayFormRequestDistributed.cshtml")'],
    ['@await Html.PartialAsync("_PayFormDistributedModal")', '@await Html.PartialAsync("~/Views/PayForms/_PayFormDistributedModal.cshtml")'],
    ['@await Html.PartialAsync("_OrderSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_OrderSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_OutputVoucherSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_OutputVoucherSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_AdvanceRequestSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_AdvanceRequestSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_AddDetailOrderModal")', '@await Html.PartialAsync("~/Views/PayForms/_AddDetailOrderModal.cshtml")'],
    ['@await Html.PartialAsync("_AddPaymentRecipient")', '@await Html.PartialAsync("~/Views/PayForms/_AddPaymentRecipient.cshtml")'],
    ['@await Html.PartialAsync("_ConfirmProcessDocUserSearchModal")', '@await Html.PartialAsync("~/Views/PayForms/_ConfirmProcessDocUserSearchModal.cshtml")'],
    ['@await Html.PartialAsync("_ConfirmProcessDocUserModal")', '@await Html.PartialAsync("~/Views/PayForms/_ConfirmProcessDocUserModal.cshtml")']
]);

console.log('ALL PARTIALS UPDATED CLEANLY!');
