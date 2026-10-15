$bytes = [System.IO.File]::ReadAllBytes("E:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Permission\UserPrincipal.cs")
if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    Write-Host "Has UTF-8 BOM: TRUE"
} else {
    Write-Host "Has UTF-8 BOM: FALSE"
}
