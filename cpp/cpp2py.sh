#!/bin/bash

## sudo apt install swig g++ python3-dev

for file in $(ls *.i); do
    module=$(basename $file .i)
    swig -python -c++ $module.i
    g++ -fPIC -c *.cpp *.cxx -I/usr/include/python3.6m
    g++ -fPIC -shared *.o -o _$module.so
done


