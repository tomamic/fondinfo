#!/bin/bash
swig -python -c++ board.i
gcc -fPIC -c board.cpp board_wrap.cxx -I/usr/include/python3.6m/ -std=c++11
gcc -shared board.o board_wrap.o -o _board.so
