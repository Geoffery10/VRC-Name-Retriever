@echo off
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