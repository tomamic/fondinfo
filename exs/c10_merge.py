#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randrange

# create two sorted files with random data
for n in (1, 2):
    with open(f"_file{n}.dat", "w") as wf:
        rows = randrange(15)
        for x in sorted(randrange(50) for i in range(rows)):
            print(x, file=wf)

with open("_file1.dat") as f1, open("_file2.dat") as f2:
    a = f1.readline()
    b = f2.readline()
    while a or b:
        if a and (not b or float(a) < float(b)):
            print(a.strip())
            a = f1.readline()
        else:
            print(b.strip())
            b = f2.readline()
