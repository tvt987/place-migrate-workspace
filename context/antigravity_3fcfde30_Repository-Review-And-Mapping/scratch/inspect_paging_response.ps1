Add-Type -AssemblyName System.Reflection
$dllPath = "E:\Work\Place_Migrate\cci-scm-api\01_origin\DLL.API\Core.DTO.dll"
if (Test-Path $dllPath) {
    $bytes = [System.IO.File]::ReadAllBytes($dllPath)
    $asm = [System.Reflection.Assembly]::Load($bytes)
    $t = $asm.GetType("Core.DTO.Response.PagingResponse``1")
    Write-Host "Found PagingResponse: $($t.FullName)"
    $protoAttrs = $t.GetCustomAttributes($false) | ForEach-Object { $_.GetType().FullName }
    Write-Host "Class Attributes: $($protoAttrs -join ', ')"
    foreach ($p in $t.GetProperties()) {
        $pAttrs = $p.GetCustomAttributes($false) | ForEach-Object { $_.GetType().FullName }
        Write-Host "Property: $($p.Name) -> $($pAttrs -join ', ')"
    }
} else {
    Write-Host "File not found: $dllPath"
}
