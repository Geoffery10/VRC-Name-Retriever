@echo off
setlocal
set "VRCPATH=%USERPROFILE%\AppData\LocalLow\VRChat\vrchat"
python "%VRCPATH%\get_usernames.py"
endlocal
pause