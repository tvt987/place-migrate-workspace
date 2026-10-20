import sys

path = '02_target/CoC.Web.SCM/Controllers/BonusPointAccountProductsController.cs'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """            var validation = DataWorksheet.DataValidations.AddListValidation("A2:A1048576");
            validation.Formula.ExcelFormula = "BonusPointTypeList!$A$2:$A$"
                + (objExport.Count() + 1).ToString();
            validation.ShowErrorMessage = true;
            validation.AllowBlank = true;
            validation.Error = "Chọn giá trị từ danh sách";"""

replacement = """            var validation = DataWorksheet.DataValidations.AddListValidation("A2:A1048576");
            validation.ShowErrorMessage = true;
            validation.AllowBlank = true;
            validation.Error = "Chọn giá trị từ danh sách";
            validation.Formula.ExcelFormula = "BonusPointTypeList!$A$2:$A$"
                + (objExport.Count() + 1).ToString();"""

if target in text:
    new_text = text.replace(target, replacement, 1)
    with open(path, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + new_text.encode('utf-8'))
    print("Successfully replaced and wrote UTF-8 BOM")
else:
    print("Target not found in text!")
