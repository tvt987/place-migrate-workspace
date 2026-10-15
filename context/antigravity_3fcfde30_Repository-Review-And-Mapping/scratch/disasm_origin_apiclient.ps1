Add-Type -AssemblyName System.Reflection
$bytes = [System.IO.File]::ReadAllBytes('e:\Work\Place_Migrate\cci-store-location-web\01_origin\DLL.Web\Core.MVC.dll')
$asm = [System.Reflection.Assembly]::Load($bytes)
$t = $asm.GetType('Core.MVC.APIClient')

foreach ($name in @('Post', 'PostObject', 'Put', 'PutObject')) {
    $m = $t.GetMethods() | Where-Object { $_.Name -eq $name } | Select-Object -First 1
    Write-Host "=== Method $name ==="
    $body = $m.GetMethodBody()
    $il = $body.GetILAsByteArray()
    Write-Host "IL bytes: $(($il | ForEach-Object { $_.ToString('X2') }) -join ' ')"
}
