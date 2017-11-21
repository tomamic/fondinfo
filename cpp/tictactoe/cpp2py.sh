#!/bin/bash

## sudo apt install swig g++ python3-dev

swig -python -c++ tictactoe.i
g++ -fPIC -c tictactoe.cpp tictactoe_wrap.cxx -I/usr/include/python3.6m
g++ -shared tictactoe.o tictactoe_wrap.o -o _tictactoe.so
