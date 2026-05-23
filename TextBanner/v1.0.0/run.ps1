Write-Host "Running TextBanner"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$mainPath = Join-Path $scriptDir "main.py"
$pythonCommand = if (Get-Command python -ErrorAction SilentlyContinue) { "python" } else { "python3" }

& $pythonCommand $mainPath @args
