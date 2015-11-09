#!/bin/bash
swig -python -c++ board.i
g++ -fPIC -c board.cpp board_wrap.cxx -I/usr/include/python3.4/ -std=c++11
g++ -shared board.o board_wrap.o -o _board.so
