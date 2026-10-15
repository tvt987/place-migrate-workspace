<#
  git-sync.ps1 - cua vao duy nhat cho pull/push/status/scan trong E:\Work\Place_Migrate
  Mode 1 = PROJECTS (git rieng cua tung cci-*, Bitbucket)
  Mode 2 = CONTEXT  (git cua workspace root, GitHub tvt987)
  Xem GIT_RULES.md
#>
param(
  [ValidateSet('pull','push','status','scan')][string]$Action = 'status',
  [string]$Mode,                       # 1 | 2 | both ; bo trong thi hoi
  [string[]]$Repos,                    # loc cac cci-* cho mode 1
  [string]$Message,                    # commit message cho mode 2
  [string]$RemoteUrl,                  # URL GitHub cho mode 2 (lan dau)
  [string]$Pattern,                    # regex cho -Action scan
  [switch]$PushTags,
  [switch]$Yes
)
$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path "$PSScriptRoot\..").Path
$Protected = 'staging','staging10','staging4','master','main'
$WebTrio = 'cci-scm-web','cci-dc-web','cci-store-location-web'
$ContextDocs = @(
  "$Root\GIT_RULES.md",
  "$Root\cci-dc-web\DEV_GUIDE.md",
  "$Root\cci-dc-web\DEV_HANDBOOK.md",
  "$Root\cci-dc-web\FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md")

function Show-Context {
  Write-Host "`n=== NAP LAI CONTEXT TRUOC KHI THAO TAC GIT ===" -ForegroundColor Yellow
  foreach($d in $ContextDocs){
    if(Test-Path $d){ $i=Get-Item $d; Write-Host ("  [doc] {0}  ({1:N0} B, {2:yyyy-MM-dd HH:mm})" -f $d,$i.Length,$i.LastWriteTime) }
    else { Write-Host "  [THIEU] $d" -ForegroundColor Red }
  }
  Write-Host "  + AGENTS.md / README.md cua project dang lam." -ForegroundColor Yellow
  Write-Host "  Luat: chi sua 02_target/; 1 bug = 1 ma = 1 commit + ho so + tag; khong force-push; khong commit .env." 
  Write-Host "  KHONG merge/push thang staging, staging10 -> chi tao Pull Request dev->staging10 va dev->staging (auto merge + build)."
  Write-Host "  Fix 1 trong 3 web (scm/dc/place) -> quet lai ca 3 (-Action scan -Pattern ...), fix + push cung."
  Write-Host "  Report web: https://report-web-testing-uat.concung.vn ; xem 03_qa/.env de upload qua make test-*`n"
}

function Resolve-Mode {
  if(-not $Mode){
    Write-Host "Chon mode: [1] PROJECTS (Bitbucket cci-*)  [2] CONTEXT (GitHub tvt987)  [both]"
    $script:Mode = Read-Host 'Mode'
  }
  if($Mode -notin '1','2','both'){ throw "Mode phai la 1, 2 hoac both (nhan: '$Mode')" }
}

function Get-ProjectRepos {
  $all = Get-ChildItem $Root -Directory | Where-Object { $_.Name -like 'cci-*' -and (Test-Path "$($_.FullName)\.git") }
  if($Repos){ $Repos = $Repos -split ','; $all =$all | Where-Object { $Repos -contains $_.Name } }
  $all
}

function Git($p){ & git -C $p @args 2>&1 }

function Mode1 {
  Write-Host "`n##### MODE 1 - PROJECTS (Bitbucket) - $Action #####" -ForegroundColor Cyan
  foreach($r in Get-ProjectRepos){
    $p=$r.FullName; $br=(Git $p branch --show-current).Trim()
    $dirty=(Git $p status --porcelain | Out-String).Trim()
    Write-Host "`n[$($r.Name)] nhanh=$br $(if($dirty){'(CO THAY DOI CHUA COMMIT)'}else{'(sach)'})" -ForegroundColor Green
    switch($Action){
      'status' { Git $p status -sb | Select-Object -First 6 }
      'pull' {
        Git $p fetch --all --tags --prune | Out-Null
        if($dirty){ Write-Host "  bo qua pull: working tree dang co thay doi. Commit/stash truoc." -ForegroundColor Yellow; continue }
        Git $p pull --ff-only
        if(Test-Path "$p\03_qa\.env"){ Write-Host "  03_qa/.env: co" } elseif(Test-Path "$p\03_qa"){ Write-Host "  03_qa/.env: THIEU - tao tu .env.example, xin credential tu leader" -ForegroundColor Yellow }
      }
      'push' {
        if($br -in $Protected){
          Write-Host "  TU CHOI push len '$br'. Dung Pull Request:" -ForegroundColor Red
          foreach($d in 'staging10','staging'){ Write-Host "    https://bitbucket.org/concung/$($r.Name)/pull-requests/new?source=dev&dest=$d" }
          continue
        }
        $ahead=(Git $p rev-list --count "@{u}..HEAD" 2>$null)
        if($LASTEXITCODE -ne 0){ $ahead='(chua co upstream)' }
        Write-Host "  commit chua push: $ahead"
        if($dirty){ Write-Host "  luu y: con file chua commit, se KHONG duoc push." -ForegroundColor Yellow }
        if(-not $Yes){ if((Read-Host "  push '$br' len origin? (y/N)") -ne 'y'){ continue } }
        Git $p push -u origin $br
        if($PushTags){ Git $p push origin --tags }
        if($br -eq 'dev'){
          Write-Host "  Tiep theo - tao PR (khong merge tay):" -ForegroundColor Cyan
          foreach($d in 'staging10','staging'){ Write-Host "    https://bitbucket.org/concung/$($r.Name)/pull-requests/new?source=dev&dest=$d" }
        }
      }
    }
  }
}

function Mode2 {
  Write-Host "`n##### MODE 2 - CONTEXT (GitHub tvt987) - $Action #####" -ForegroundColor Cyan
  if(-not (Test-Path "$Root\.git")){ Write-Host "Root chua la git repo. Chay: git -C $Root init -b main" -ForegroundColor Yellow; return }
  switch($Action){
    'status' { Git $Root status -sb | Select-Object -First 30 }
    'pull'   { Git $Root pull --ff-only }
    'push'   {
      if($RemoteUrl){ if(Git $Root remote | Select-String -Quiet '^origin$'){ Git $Root remote set-url origin $RemoteUrl } else { Git $Root remote add origin $RemoteUrl } }
      if(-not (Git $Root remote | Select-String -Quiet '^origin$')){ throw 'Chua co remote origin. Truyen -RemoteUrl https://github.com/tvt987/<repo>.git' }
      $url=(Git $Root remote get-url origin).Trim()
      if($url -notmatch 'github\.com[:/]tvt987/'){ throw "Remote '$url' khong thuoc tvt987. Dung lai." }
      Git $Root add -A | Out-Null
      $staged=(Git $Root diff --cached --name-only) -split "`n" | Where-Object { $_ }
      $bad=$staged | Where-Object { $_ -match '(^|/)\.env$|\.pem$|\.pfx$|\.key$|\.auth/' }
      $big=$staged | Where-Object { (Test-Path "$Root\$_") -and ((Get-Item "$Root\$_").Length -gt 95MB) }
      if($bad){ Git $Root reset -q; throw "Co file nhay cam trong staged: $($bad -join ', ')" }
      if($big){ Git $Root reset -q; throw "Co file >95MB (GitHub chan): $($big -join ', ')" }
      if(-not $staged){ Write-Host 'Khong co gi de commit.'; }
      else {
        if(-not $Message){ $Message="docs(context): cap nhat workspace $(Get-Date -Format 'yyyy-MM-dd HH:mm')" }
        Git $Root commit -m $Message
      }
      if(-not $Yes){ if((Read-Host "push origin main -> $url ? (y/N)") -ne 'y'){ return } }
      Git $Root push -u origin main
    }
  }
}

function Scan {
  if(-not $Pattern){ throw 'Can -Pattern <regex>' }
  Write-Host "`n##### QUET CHEO 3 WEB: $Pattern #####" -ForegroundColor Cyan
  foreach($n in $WebTrio){
    Write-Host "`n[$n]" -ForegroundColor Green
    $dirs=@("$Root\$n\02_target","$Root\$n\03_qa") | Where-Object { Test-Path $_ }
    Get-ChildItem $dirs -Recurse -File -ErrorAction SilentlyContinue |
      Where-Object { $_.FullName -notmatch '\\(node_modules|bin|obj|wwwroot\\lib|playwright-report|test-results|\.auth)\\' -and $_.Extension -in '.cs','.cshtml','.js','.ts','.json','.config','.csproj' } |
      Select-String -Pattern $Pattern -ErrorAction SilentlyContinue | Select-Object -First 40 |
      ForEach-Object { "  {0}:{1}: {2}" -f $_.Path.Substring($Root.Length+1),$_.LineNumber,$_.Line.Trim().Substring(0,[Math]::Min(140,$_.Line.Trim().Length)) }
  }
  Write-Host "`nGhi ket qua (co/khong) vao ho so bug; co thi fix + push cung dot." -ForegroundColor Yellow
}

Show-Context
if($Action -eq 'scan'){ Scan; return }
Resolve-Mode
if($Mode -in '1','both'){ Mode1 }
if($Mode -in '2','both'){ Mode2 }
