param(
    [Parameter(Mandatory=$true)]
    [string]$FilePath
)

$utf8WithBom = New-Object System.Text.UTF8Encoding($true)
$content = [System.IO.File]::ReadAllText($FilePath, [System.Text.Encoding]::UTF8)
[System.IO.File]::WriteAllText($FilePath, $content, $utf8WithBom)

$b = [System.IO.File]::ReadAllBytes($FilePath)
$hasBom = ($b.Length -ge 3 -and $b[0] -eq 0xEF -and $b[1] -eq 0xBB -and $b[2] -eq 0xBF)
Write-Host "Restored BOM on $FilePath : BOM=$hasBom"
