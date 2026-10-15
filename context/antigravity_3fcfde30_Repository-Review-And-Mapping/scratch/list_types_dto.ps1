$bytes = [System.IO.File]::ReadAllBytes('C:\Users\25303_TruongVanTinh\.nuget\packages\cci.core.dto\1.0.5\lib\net8.0\Core.DTO.dll')
$asm = [System.Reflection.Assembly]::Load($bytes)
$asm.GetTypes() | ForEach-Object { $_.FullName }
