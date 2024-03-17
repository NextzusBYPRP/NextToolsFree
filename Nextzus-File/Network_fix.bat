@echo off


cls
echo Optimizing Network Settings...
echo.
echo Please wait...

echo.
echo Clearing Internet Temporary Files...
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8

netsh int tcp set global autotuninglevel=normal


:: Reset Network Stack
cls
echo Resetting Network Stack...
ipconfig /flushdns
netsh int ip reset
netsh winsock reset
netsh winhttp reset proxy
netsh winsock reset
netsh int ip reset
netsh int ipv4 reset
netsh int ipv6 reset






