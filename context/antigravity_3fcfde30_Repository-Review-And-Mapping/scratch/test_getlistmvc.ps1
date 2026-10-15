$token = [System.IO.File]::ReadAllText('C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\scratch\token.txt').Trim()

$headers = @{
    "Authorization" = "Bearer $token"
    "UserID" = "2741"
    "Accept" = "application/json"
}

$tests = @(
    @{ Name = "Empty Object {}"; Body = '{}' },
    @{ Name = "CamelCase"; Body = '{"provinceID":null,"scopeTypeRankID":null,"scopeStatusID":[5,4,101],"userIDFilter":null,"scopeIDs":[],"isAll":false,"isNearStore":false,"referSystemIDs":null,"storeSizeIDs":null}' },
    @{ Name = "PascalCase"; Body = '{"ProvinceID":null,"ScopeTypeRankID":null,"ScopeStatusID":[5,4,101],"UserIDFilter":null,"ScopeIDs":[],"IsAll":false,"IsNearStore":false,"ReferSystemIDs":null,"StoreSizeIDs":null}' }
)

foreach ($t in $tests) {
    Write-Host "`n--- Testing: $($t.Name) ---"
    try {
        $res = Invoke-RestMethod -Uri "https://place-api-stg4.concung.vn/api/Scopes/GetListMVC" -Method Post -Headers $headers -Body $t.Body -ContentType "application/json"
        Write-Host "SUCCESS! Count: $($res.Count)"
    } catch {
        Write-Host "FAILED! Status: $($_.Exception.Response.StatusCode.value__)"
        $stream = $_.Exception.Response.GetResponseStream()
        if ($stream) {
            $reader = New-Object System.IO.StreamReader($stream)
            $body = $reader.ReadToEnd()
            Write-Host "Response body: $body"
        } else {
            Write-Host "Exception: $($_.Exception.Message)"
        }
    }
}
