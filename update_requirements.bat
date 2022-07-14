@echo Off

rem the below section as well as the :colorEcho function at the end of the script just allows for 
rem multiple lines of different colours. See https://stackoverflow.com/questions/21660249/how-do-i-make-one-particular-line-of-a-batch-file-a-different-color-then-the-oth
rem https://github.com/bndr/pipreqs

SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do     rem"') do (
  set "DEL=%%a"
)

call :colorEcho 0d "Updating requirements.txt! "
echo.
echo.
call :colorEcho 05 "This script utilises pipreqs by Vadim Kravcenko to automatically detect dependencies and generate the file. All credit goes to Vadim and the project contributers."
echo.
echo.
set mypath=%cd%
pipreqs %mypath% --force
echo.
pause
exit

:colorEcho
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1i