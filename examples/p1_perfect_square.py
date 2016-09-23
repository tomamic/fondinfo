#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

n = int(input('n? '))
result = 0

i = 1
while i * i <= n:
    if i * i == n:
        result = i
    i += 1

if result == 0:
    print('no')
else:
    print(result)
