Add-Type -AssemblyName System.Reflection
$bytes = [System.IO.File]::ReadAllBytes('e:\Work\Place_Migrate\cci-store-location-web\01_origin\DLL.Web\Core.MVC.dll')
$asm = [System.Reflection.Assembly]::Load($bytes)
$t = $asm.GetType('Core.MVC.APIClient')
Write-Host "Found type: $($t.FullName)"
foreach ($m in $t.GetMethods([System.Reflection.BindingFlags]'Public,NonPublic,Instance,Static,DeclaredOnly')) {
    $params = ($m.GetParameters() | ForEach-Object { "$($_.ParameterType.Name) $($_.Name)" }) -join ', '
    Write-Host "Method: $($m.Name) ($params)"
}
