#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys

LENGTH = 16

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input('Insert the file name: ')

with open(filename, 'rb') as infile:
    bytes = infile.read()
    line = []
    for b in bytes:
        # print the hex value of each byte
        print('{:02x} '.format(b), end='')

        # remember the corresponding char
        if ord(' ') <= b <= ord('~'):
            line.append(chr(b))
        else:
            line.append(' ')
        
        # collected 16 chars: print them all
        if len(line) == LENGTH:
            print('', ''.join(line))
            line = []

    # end of file: remaining chars to print?
    if len(line) > 0:
        print('   ' * (LENGTH - len(line)), ''.join(line))

