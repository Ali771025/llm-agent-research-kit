param([string]$Profile='01-openai')
$ErrorActionPreference = 'Stop'
$Root = $PSScriptRoot
$Lock = Join-Path $Root "profiles\$Profile.lock.txt"
if (!(Test-Path $Lock)) { Get-ChildItem (Join-Path $Root 'profiles') -Filter '*.lock.txt' | Select-Object -ExpandProperty BaseName; throw "Unknown profile: $Profile" }
& py -3.13 -c "import sys, platform; assert sys.version_info[:2] == (3,13) and sys.platform == 'win32' and platform.machine().upper() in ('AMD64','X86_64'), 'Requires standard CPython 3.13 Windows x64'"
if ($LASTEXITCODE -ne 0) { throw 'Install standard Python 3.13 x64 with the py launcher first.' }
$EnvPath = Join-Path $Root ".venvs\$Profile"
if (!(Test-Path (Join-Path $EnvPath 'Scripts\python.exe'))) {
 & py -3.13 -m venv $EnvPath
 if ($LASTEXITCODE -ne 0) { throw 'venv creation failed' }
}
$Python = Join-Path $EnvPath 'Scripts\python.exe'
$Wheels = Join-Path $Root 'wheelhouse'
& $Python -m pip install --no-index --find-links $Wheels --upgrade pip
if ($LASTEXITCODE -ne 0) { throw 'Offline pip upgrade failed' }
& $Python -m pip install --no-index --find-links $Wheels --require-hashes -r $Lock
if ($LASTEXITCODE -ne 0) { throw 'Offline installation failed; retain the error output.' }
& $Python -m pip check
if ($LASTEXITCODE -ne 0) { throw 'Dependency check failed' }
Write-Host "Installed $Profile. Python: $Python"
Write-Host "Activate with: & '$EnvPath\Scripts\Activate.ps1'"
