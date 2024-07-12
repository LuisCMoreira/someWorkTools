@echo off
rem Set the network interface name (change this to match your network adapter name)
set INTERFACE_NAME="Ethernet"

rem Reactivate DHCP for IP address and DNS
netsh interface ip set address name=%INTERFACE_NAME% source=dhcp
netsh interface ip set dns name=%INTERFACE_NAME% source=dhcp

echo DHCP has been reactivated.
