Add-Type -AssemblyName System.Reflection

# Load protobuf-net first so attributes can resolve
$protoNet = "C:\Users\25303_TruongVanTinh\.nuget\packages\protobuf-net\2.3.2\lib\net40\protobuf-net.dll"
if (Test-Path $protoNet) { [System.Reflection.Assembly]::Load([System.IO.File]::ReadAllBytes($protoNet)) | Out-Null }

$pkgDir = "C:\Users\25303_TruongVanTinh\.nuget\packages\cci.core.dto\1.0.5\lib"
Get-ChildItem -Recurse -Filter "CCI.Core.DTO.dll" $pkgDir | ForEach-Object {
    Write-Host "=== Inspecting $($_.FullName) ==="
    $bytes = [System.IO.File]::ReadAllBytes($_.FullName)
    $asm = [System.Reflection.Assembly]::Load($bytes)
    $t = $asm.GetType("Core.DTO.Response.PagingResponse``1")
    if ($t) {
        Write-Host "Found PagingResponse in $($_.FullName)"
        $attrs = $t.GetCustomAttributes($false) | ForEach-Object { $_.GetType().FullName }
        Write-Host "Class Attributes: $($attrs -join ', ')"
        foreach ($p in $t.GetProperties()) {
            $pAttrs = $p.GetCustomAttributes($false) | ForEach-Object { $_.GetType().FullName }
            Write-Host "Property: $($p.Name) -> $($pAttrs -join ', ')"
        }
    }
}
