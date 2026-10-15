$content = [System.IO.File]::ReadAllText('C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\scratch\step1506.txt')
if ($content -match '(eyJ[a-zA-Z0-9_\-\.]+)') {
    $t = $matches[1]
    Write-Host "Found token length: $($t.Length)"
    [System.IO.File]::WriteAllText('C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\scratch\token.txt', $t)
} else {
    Write-Host "Token not found"
}
