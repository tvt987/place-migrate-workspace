$dllDir = "e:\Work\Place_Migrate\cci-store-location-web\01_origin\DLL.Web"
[System.AppDomain]::CurrentDomain.add_AssemblyResolve({
    param($sender, $args)
    $name = $args.Name.Split(',')[0]
    $candidate = Join-Path $dllDir "$name.dll"
    if (Test-Path $candidate) {
        return [System.Reflection.Assembly]::LoadFrom($candidate)
    }
    $pkgCandidates = Get-ChildItem -Path "e:\Work\Place_Migrate\cci-store-location-web\01_origin\packages" -Filter "$name.dll" -Recurse -ErrorAction SilentlyContinue
    if ($pkgCandidates.Count -gt 0) {
        return [System.Reflection.Assembly]::LoadFrom($pkgCandidates[0].FullName)
    }
    return $null
})

$dllPath = Join-Path $dllDir "Core.MVC.dll"
$asm = [System.Reflection.Assembly]::LoadFrom($dllPath)
$t = $asm.GetType("Core.MVC.APIClient")
if ($t) {
    Write-Host "Found $($t.FullName)"
    $t.GetMethods() | ForEach-Object {
        Write-Host "$($_.ReturnType.Name) $($_.Name) ($([string]::Join(', ', ($_.GetParameters() | ForEach-Object { "$($_.ParameterType.Name) $($_.Name)" }))))"
    }
} else {
    Write-Host "Type Core.MVC.APIClient not found, searching all types:"
    foreach ($type in $asm.GetExportedTypes()) {
        Write-Host $type.FullName
    }
}
