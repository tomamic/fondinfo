if not "x%PATH:MinGW=%"=="x%PATH%" setx PATH "%PATH%;C:\MinGW\mingw64\bin"

del _main.exe
cl *.cpp /Fe_main.exe /D WEBVIEW_WINAPI=1 /link ole32.lib comctl32.lib oleaut32.lib uuid.lib gdi32.lib advapi32.lib
_main.exe
