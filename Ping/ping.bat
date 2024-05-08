@echo off
setlocal enabledelayedexpansion

rem Set the base IP range (APIPA: 169.254.0.0/16)
set "base_ip=169.254."

rem Loop through each possible IP address in the APIPA range
for /L %%i in (1,1,255) do (
    set "ip=!base_ip!%%i"
    echo Pinging !ip!...

    rem Ping the IP address
    ping -n 1 !ip! >nul

    rem Check the error level to determine reachability
    if !errorlevel! equ 0 (
        echo !ip! is reachable.
    ) else (
        echo !ip! is not reachable.
    )
)

endlocal
