Add-Type -AssemblyName System.Net.Http
Add-Type -AssemblyName System.Net.Http.Json

$t = [string]
$jc = [System.Net.Http.Json.JsonContent]::Create("hello", [string], $null, $null)
Write-Host "Before buffering:"
Write-Host "  Content-Length: $($jc.Headers.ContentLength)"
Write-Host "  Transfer-Encoding chunked: $($null -eq $jc.Headers.ContentLength)"

$jc.LoadIntoBufferAsync().Wait()
Write-Host "After buffering:"
Write-Host "  Content-Length: $($jc.Headers.ContentLength)"
