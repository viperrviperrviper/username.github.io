@echo off
setlocal

set "ROOT=%~dp0."
set "PY=C:\Users\zxc\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if not exist "%PY%" set "PY=python"

cd /d "%ROOT%"
"%PY%" "%ROOT%\start-local-server.py"

pause
