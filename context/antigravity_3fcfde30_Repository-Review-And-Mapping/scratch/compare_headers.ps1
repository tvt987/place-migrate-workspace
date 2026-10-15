Add-Type -AssemblyName System.Net.Http
Add-Type -AssemblyName System.Net.Http.Json

$sc = New-Object System.Net.Http.StringContent('{"a":1}', [System.Text.Encoding]::UTF8, 'application/json')
$jc = [System.Net.Http.Json.JsonContent]::Create([PSCustomObject]@{ a = 1 })

Write-Host "StringContent Content-Type: $($sc.Headers.ContentType)"
Write-Host "StringContent Content-Length: $($sc.Headers.ContentLength)"
Write-Host "JsonContent Content-Type: $($jc.Headers.ContentType)"
Write-Host "JsonContent Content-Length: $($jc.Headers.ContentLength)"
