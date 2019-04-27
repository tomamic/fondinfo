#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys

##with open("_list.txt", "w") as new_file:
##    print("always second: 35", file=new_file)
##    print("bombastic champion: 40", file=new_file)
##    print("hopeless dud: 10", file=new_file)

records = {}
with open("_list.txt") as infile:
    for line in infile:
        name, points = line.strip().split(": ", 2)
        records[name] = points

for name, points in records.items():
    print(name, points)

for name in sys.stdin:
    name = name.strip()
    if name in records.keys():
        print(records[name])
    else:
        print("Unknown user")
