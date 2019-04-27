#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import randrange

# create two sorted files with random data
for n in (1, 2):
    with open(f"_file{n}.dat", "w") as wf:
        data = sorted(randrange(50) for i in range(randrange(15)))
        print("\n".join(map(str, data)), file=wf, end="")

with open("_file1.dat") as f1, open("_file2.dat") as f2:
    a = f1.readline().strip()
    b = f2.readline().strip()
    while a != "" or b != "":
        if a != "" and (b == "" or float(a) < float(b)):
            print(a)
            a = f1.readline().strip()
        else:
            print(b)
            b = f2.readline().strip()
