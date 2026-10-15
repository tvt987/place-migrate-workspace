$path = "e:\Work\Place_Migrate\cci-store-location-web\01_origin\DLL.Web\Core.MVC.dll"
$bytes = [System.IO.File]::ReadAllBytes($path)
# Let's search for string literals or referenced methods in the dll
$str = [System.Text.Encoding]::ASCII.GetString($bytes)
$matches = [System.Text.RegularExpressions.Regex]::Matches($str, "(PostAsJsonAsync|PostAsync|PostObject|JsonConvert|SerializeObject|ObjectContent|MediaTypeFormatter)[a-zA-Z0-9_.]*")
foreach ($m in $matches) {
    Write-Host $m.Value
}
