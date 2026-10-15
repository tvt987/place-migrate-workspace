$utf8WithBom = New-Object System.Text.UTF8Encoding($true)
$filePath = "E:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Permission\UserPrincipal.cs"
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
[System.IO.File]::WriteAllText($filePath, $content, $utf8WithBom)
