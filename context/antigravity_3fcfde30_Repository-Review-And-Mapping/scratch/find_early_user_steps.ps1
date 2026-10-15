$path = 'C:\Users\25303_TruongVanTinh\.gemini\antigravity-ide\brain\3fcfde30-4110-403c-8f9f-a4ed95abc9e6\.system_generated\logs\transcript.jsonl'
$reader = [System.IO.File]::OpenText($path)
while (-not $reader.EndOfStream) {
    $line = $reader.ReadLine()
    if ($line.Contains('"type":"USER_INPUT"')) {
        $json = $line | ConvertFrom-Json
        if ($json.step_index -lt 3800) {
            Write-Host "Step $($json.step_index): $($json.content)`n---"
        }
    }
}
$reader.Close()
