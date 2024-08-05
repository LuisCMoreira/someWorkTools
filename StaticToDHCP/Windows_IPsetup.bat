@echo off
rem Set the network interface name (change this to match your network adapter name)
set INTERFACE_NAME="Ethernet"

rem Set the static IP address, subnet mask, and default gateway
set IP_ADDRESS=10.0.0.10
set SUBNET_MASK=255.255.255.0
set DEFAULT_GATEWAY=10.0.0.254

rem Set the primary and secondary DNS servers
set DNS1=0.0.0.0

rem Apply the static IP configuration
netsh interface ip set address name=%INTERFACE_NAME% static %IP_ADDRESS% %SUBNET_MASK% %DEFAULT_GATEWAY%

rem Apply the DNS server configuration
netsh interface ip set dns name=%INTERFACE_NAME% static %DNS1%
netsh interface ip add dns name=%INTERFACE_NAME% %DNS2% index=2

echo Static IP configuration has been set.