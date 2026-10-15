$path = "e:\Work\Place_Migrate\cci-store-location-web\01_origin\DLL.Web\Core.MVC.dll"
$asm = [System.Reflection.Assembly]::Load([System.IO.File]::ReadAllBytes($path))
$t = $asm.GetType("Core.MVC.APIClient")
$m = $t.GetMethod("PostObject")
$module = $m.Module
$method = $module.ResolveMethod(0x2B000002)
Write-Host "Resolved: $($method.DeclaringType.FullName)::$($method.Name)"
Write-Host "Generic arguments: $([string]::Join(', ', ($method.GetGenericArguments() | ForEach-Object { $_.FullName })))"
Write-Host "Declaring assembly: $($method.DeclaringType.Assembly.FullName)"
