param($file)
$b = [System.IO.File]::ReadAllBytes($file)
$hasBom = ($b.Length -ge 3 -and $b[0] -eq 0xEF -and $b[1] -eq 0xBB -and $b[2] -eq 0xBF)
Write-Host "$file : BOM=$hasBom"
