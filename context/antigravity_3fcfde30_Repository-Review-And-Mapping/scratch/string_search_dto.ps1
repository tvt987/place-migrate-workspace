$bytes = [System.IO.File]::ReadAllBytes('C:\Users\25303_TruongVanTinh\.nuget\packages\cci.core.dto\1.0.5\lib\net8.0\Core.DTO.dll')
$str = [System.Text.Encoding]::UTF8.GetString($bytes)
Write-Host "Contains PagingResponse: $($str.Contains('PagingResponse'))"
Write-Host "Contains ProtoContract: $($str.Contains('ProtoContract'))"
Write-Host "Contains ProtoMember: $($str.Contains('ProtoMember'))"
