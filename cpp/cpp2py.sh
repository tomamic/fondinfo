#!/bin/bash

## sudo apt install swig g++ python3-dev

for file in $(ls *.i); do
    module=$(basename $file .i)
    swig -python -c++ $module.i
    g++ -fPIC -shared *.cpp *.cxx -I/usr/include/python3.6m -o _$module.so
    rm $module\_wrap.cxx
done


