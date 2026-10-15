$path = "e:\Work\Place_Migrate\cci-store-location-web\01_origin\DLL.Web\Core.MVC.dll"
# Using System.Reflection.Metadata or IL to inspect
Add-Type -AssemblyName System.Reflection
$asm = [System.Reflection.Assembly]::Load([System.IO.File]::ReadAllBytes($path))
$t = $asm.GetType("Core.MVC.APIClient")
if ($t) {
    foreach ($m in $t.GetMethods([System.Reflection.BindingFlags]"Public,NonPublic,Instance,Static,DeclaredOnly")) {
        $body = $m.GetMethodBody()
        Write-Host "Method: $($m.Name), IL Length: $(if ($body) { $body.GetILAsByteArray().Length } else { 'none' })"
    }
}
