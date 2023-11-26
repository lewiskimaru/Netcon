@echo off

for /f "tokens=2 delims=:" %%a in ('ipconfig^|findstr IPv4') do (

set "ip=%%a"

)
for /f "tokens=2 delims=:" %%b in ('ipconfig^|findstr Subnet') do (

set "netmask=%%b"

)

for /f "tokens=2 delims=:" %%c in ('ipconfig^|findstr Default') do (

set "dgw=%%c"

)


echo %ip% %netmask% %dgw% > "C:\Netcon\Get IPv4\IPv4.txt"