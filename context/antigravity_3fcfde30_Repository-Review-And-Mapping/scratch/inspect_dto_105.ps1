Add-Type -AssemblyName System.Reflection

$dllPath = "C:\Users\25303_TruongVanTinh\.nuget\packages\cci.core.dto\1.0.5\lib\net8.0\Core.DTO.dll"
$bytes = [System.IO.File]::ReadAllBytes($dllPath)
$asm = [System.Reflection.Assembly]::Load($bytes)
$t = $asm.GetType("Core.DTO.Response.PagingResponse``1")
Write-Host "Found PagingResponse in $dllPath"
$attrs = $t.GetCustomAttributesData() | ForEach-Object { $_.AttributeType.FullName }
Write-Host "Class Attributes: $($attrs -join ', ')"
foreach ($p in $t.GetProperties()) {
    $pAttrs = $p.GetCustomAttributesData() | ForEach-Object { $_.AttributeType.FullName }
    Write-Host "Property: $($p.Name) -> $($pAttrs -join ', ')"
}
