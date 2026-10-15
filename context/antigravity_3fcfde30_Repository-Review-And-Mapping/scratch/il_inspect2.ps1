$path = "e:\Work\Place_Migrate\cci-store-location-web\01_origin\DLL.Web\Core.MVC.dll"
$asm = [System.Reflection.Assembly]::Load([System.IO.File]::ReadAllBytes($path))
$t = $asm.GetType("Core.MVC.APIClient")
$m = $t.GetMethod("PostObject")
$module = $m.Module
$body = $m.GetMethodBody()
$il = $body.GetILAsByteArray()
Write-Host "IL bytes: $([System.BitConverter]::ToString($il))"

# Read tokens from IL
for ($i = 0; $i -lt $il.Length; $i++) {
    $b = $il[$i]
    if ($b -eq 0x28 -or $b -eq 0x6f -or $b -eq 0x73) { # call, callvirt, newobj
        $token = [System.BitConverter]::ToInt32($il, $i + 1)
        try {
            $member = $module.ResolveMember($token)
            Write-Host "Opcode: $([string]::Format('{0:X2}', $b)) Token: $([string]::Format('{0:X8}', $token)) -> $($member.DeclaringType.FullName)::$($member.Name)"
        } catch {
            Write-Host "Opcode: $([string]::Format('{0:X2}', $b)) Token: $([string]::Format('{0:X8}', $token)) -> unresolved"
        }
        $i += 4
    }
}
