if not "x%PATH:MinGW=%"=="x%PATH%" setx PATH "%PATH%;C:\MinGW\mingw64\bin"

del _main.exe
g++ *.cpp -std=c++14 -DWEBVIEW_WINAPI=1 -lole32 -lcomctl32 -loleaut32 -luuid -mwindows -o _main.exe
_main.exe
