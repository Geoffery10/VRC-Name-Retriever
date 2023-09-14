@echo off

REM Check if colorama is installed and get its version
for /f "tokens=2 delims= " %%i in ('pip show colorama ^| findstr Version') do set version=%%i

REM Check if version is not empty
if not defined version (
    echo colorama is not installed.
    set /p user_input="Do you want to install colorama? (y/n): "
    if /i "%user_input%"=="y" (
        pip install colorama
    ) else (
        echo Exiting script...
        exit /b
    )
)

setlocal
set "VRCPATH=%USERPROFILE%\AppData\LocalLow\VRChat\vrchat"
if exist "%VRCPATH%\get_usernames.py" (
    python "%VRCPATH%\get_usernames.py"
) else (
    echo "get_usernames.py not found in %VRCPATH%"
    if exist ".\get_usernames.py" (
        echo "get_usernames.py found in the current directory"
        python ".\get_usernames.py"
    ) else (
        echo "get_usernames.py not found in the current directory"
    )
)
endlocal
pause