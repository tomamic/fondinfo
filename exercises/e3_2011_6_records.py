#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys

records = {}
with open('list.txt') as infile:
    for line in infile:
        name, points = line.strip().split(': ', 2)
        records[name] = points

for name, points in records.items():
    print(name, points)

for name in sys.stdin:
    name = name.strip()
    if name in records.keys():
        print(records[name])
    else:
        print('Unknown user')
