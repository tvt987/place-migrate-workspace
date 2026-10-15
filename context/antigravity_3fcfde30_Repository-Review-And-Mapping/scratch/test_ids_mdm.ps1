try {
    $tokenUrl = "https://ids1-stg.concung.vn/realms/master/protocol/openid-connect/token"
    $body = @{
        client_id = "scm.ClientCredential"
        client_secret = "6D9F85"
        scope = "scm-api"
        grant_type = "client_credentials"
    }
    Write-Host "Testing IDS token..."
    $resp = Invoke-RestMethod -Uri $tokenUrl -Method Post -Body $body -TimeoutSec 10
    Write-Host ("Token obtained successfully. Token length: " + $resp.access_token.Length)
    
    $mdmUrl = "https://mdm-api-stg.concung.vn/api/Permissions/ReadClient?clientName=scm.concung.com&enviroment=STG"
    $headers = @{ Authorization = "Bearer " + $resp.access_token }
    Write-Host "Testing MDM permission API..."
    $permResp = Invoke-RestMethod -Uri $mdmUrl -Method Get -Headers $headers -TimeoutSec 15
    Write-Host ("MDM returned permissions: " + $permResp.Permission.Count)
} catch {
    Write-Host ("Error: " + $_)
}
