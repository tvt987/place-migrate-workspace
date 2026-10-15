Add-Type -AssemblyName System.Reflection
$bytes = [System.IO.File]::ReadAllBytes('02_target/CoC.Web.Place/bin/Debug/net10.0/CoC.Web.Place.dll')
$asm = [System.Reflection.Assembly]::Load($bytes)
$t = $asm.GetType('CoC.Web.Place.Helpers.APIClient')
$m = $t.GetMethod('PostObject')
$body = $m.GetMethodBody()
$il = $body.GetILAsByteArray()
Write-Host "IL length of PostObject: $($il.Length)"
foreach ($f in $t.GetFields([System.Reflection.BindingFlags]'Static,NonPublic,Public')) {
    Write-Host "Field: $($f.Name), Type: $($f.FieldType.FullName)"
}
