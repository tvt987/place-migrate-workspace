$path = 'C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\.system_generated\logs\transcript.jsonl'
$reader = [System.IO.File]::OpenText($path)
while (-not $reader.EndOfStream) {
    $line = $reader.ReadLine()
    if ($line.Contains('"type":"USER_INPUT"')) {
        $json = $line | ConvertFrom-Json
        $content = $json.content
        if ($content -match 'start|server|deploy|place|stg10|refuse|503|lỗi') {
            Write-Host "Step $($json.step_index): $content`n---"
        }
    }
}
$reader.Close()
