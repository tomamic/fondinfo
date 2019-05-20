if not "x%PATH:MinGW=%"=="x%PATH%" setx PATH "%PATH%;C:\MinGW\bin"

del _main.exe
g++ *.cpp -o _main.exe -lws2_32 -lwsock32
_main.exe
