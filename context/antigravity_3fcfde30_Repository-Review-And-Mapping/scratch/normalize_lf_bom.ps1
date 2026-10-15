$filePath = "E:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Permission\UserPrincipal.cs"
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
# Normalize to LF
$content = $content.Replace("`r`n", "`n").TrimEnd("`n") + "`n"
$utf8WithBom = New-Object System.Text.UTF8Encoding($true)
[System.IO.File]::WriteAllText($filePath, $content, $utf8WithBom)
