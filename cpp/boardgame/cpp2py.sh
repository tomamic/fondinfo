#!/bin/bash

## sudo apt install swig g++ python3-dev

swig -python -c++ knightdom.i
g++ -fPIC -c knightdom.cpp knightdom_wrap.cxx -I/usr/include/python3.6m
g++ -shared knightdom.o knightdom_wrap.o -o _knightdom.so
