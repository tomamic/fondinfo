@echo off

set SWIG_HOME=%TMP%\swigwin-3.0.12
set PYTHON_HOME=%LOCALAPPDATA%\Programs\Python\Python36-32
set CODEB_HOME=%PROGRAMFILES(X86)%\CodeBlocks

set PATH=C:\MinGW\bin;%CODEB_HOME%\MinGW\bin;%SWIG_HOME%;%PATH%
setlocal ENABLEDELAYEDEXPANSION
for %%f in (*.i) do (
    set MODULE=%%~nf
    swig -python -c++ !MODULE!.i
    g++ -std=c++14 -D_hypot=hypot -c *.cpp *.cxx -I"%PYTHON_HOME%\include"
    g++ -shared *.o "%PYTHON_HOME%\libs\libpython36.a" -o _!MODULE!.pyd
    del *.o *wrap.cxx
)

pause
