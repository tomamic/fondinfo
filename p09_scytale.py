#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

COLS, ROWS = 4, 3
text = "informazioneSEGRETISSIMA"
#with open("p09_scytale.py") as infile:
#    text = infile.read()

with open("_output.txt", "w") as outfile:
    matrix = [" "] * (COLS*ROWS)
    i, n = 0, len(text)
    while i < n:
        for x in range(COLS):
            for y in range(ROWS):
                c = text[i] if i < n else " "
                matrix[x + y*COLS] = c
                i += 1
        print("".join(matrix), end="", file=outfile)
