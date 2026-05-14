Write-Host "Running from app specific run.ps1"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$mainPath = Join-Path $scriptDir "main.py"
$pythonCommand = if (Get-Command python -ErrorAction SilentlyContinue) { "python" } else { "python3" }

& $pythonCommand $mainPath
