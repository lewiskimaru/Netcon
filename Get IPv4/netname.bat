@Echo Off & SetLocal EnableExtensions
Set "Name=" & Set "NetConnectionID="
For /F Delims^= %%G In ('%__APPDIR__%wbem\WMIC.exe NIC Where ^
 "Not NetConnectionStatus Is Null And NetEnabled='TRUE'" ^
 Get Name^,NetConnectionID /Value 2^> NUL') Do Set "%%G" 2> NUL 1>&2
If Not Defined Name GoTo :EOF
Echo You are currently connected to Interface "%NetConnectionID%" on "%Name%"
Pause