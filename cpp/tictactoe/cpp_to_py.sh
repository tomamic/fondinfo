#!/bin/bash

## sudo apt install swig python3-dev

swig -python -c++ tictactoe.i
g++ -fPIC -c tictactoe.cpp tictactoe_wrap.cxx -I/usr/include/python3.6m/ -std=c++11
g++ -shared tictactoe.o tictactoe_wrap.o -o _tictactoe.so
