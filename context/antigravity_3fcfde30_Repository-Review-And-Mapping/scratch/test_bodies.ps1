$bodyPascal = '{"ScopeStatusID":[5,4,101],"ScopeIDs":[]}'
$bodyCamel = '{"scopeStatusID":[5,4,101],"scopeIDs":[]}'

try {
    $r1 = Invoke-RestMethod -Uri 'https://place-api-stg4.concung.vn/api/Scopes/GetListMVC' -Method POST -Body $bodyPascal -ContentType 'application/json'
    Write-Host ("PascalCase: SUCCESS count=" + $r1.Count)
} catch {
    Write-Host ("PascalCase FAILED: " + $_.Exception.Message)
    if ($_.ErrorDetails) { Write-Host $_.ErrorDetails.Message }
}

try {
    $r2 = Invoke-RestMethod -Uri 'https://place-api-stg4.concung.vn/api/Scopes/GetListMVC' -Method POST -Body $bodyCamel -ContentType 'application/json'
    Write-Host ("CamelCase: SUCCESS count=" + $r2.Count)
} catch {
    Write-Host ("CamelCase FAILED: " + $_.Exception.Message)
    if ($_.ErrorDetails) { Write-Host $_.ErrorDetails.Message }
}
