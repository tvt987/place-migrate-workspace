try {
    $r = Invoke-RestMethod -Uri "https://place-api-stg4.concung.vn/api/Scopes/GetListMVC" -Method POST -Body "{}" -ContentType "application/json"
    Write-Host "Success: $r"
} catch {
    Write-Host "StatusCode: $($_.Exception.Response.StatusCode.value__)"
    Write-Host "Details: $($_.ErrorDetails.Message)"
    Write-Host "Exception: $($_.Exception.Message)"
}
