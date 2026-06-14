$ErrorActionPreference = "Stop"

$taskName = "ResearchSentinel_WeeklyUpdate"
$repoRoot = $PSScriptRoot
$batchPath = Join-Path $repoRoot "run_pipeline.bat"

if (-not (Test-Path -LiteralPath $batchPath)) {
    throw "Pipeline launcher not found: $batchPath"
}

$action = New-ScheduledTaskAction `
    -Execute "$env:SystemRoot\System32\cmd.exe" `
    -Argument "/d /c `"$batchPath`"" `
    -WorkingDirectory $repoRoot

$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Friday -At "21:00"
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2)

Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Description "Fetch and publish the weekly Research Sentinel literature review." `
    -Force | Out-Null

Write-Host "Registered $taskName to run every Friday at 9:00pm."
