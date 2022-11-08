#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

text = "informazioneSEGRETISSIMA"
#with open("p09_scytale.py") as infile:
#    text = infile.read()

with open("_output.txt", "w") as outfile:
    FILLER = ' '
    ROWS = 3
    COLS = 4

    matrix = [FILLER] * (ROWS * COLS)
    i = 0
    while i < len(text):
        for y in range(ROWS):
            for x in range(COLS):
                if i < len(text):
                    matrix[y * COLS + x] = text[i]
                    i += 1
                else:
                    matrix[y * COLS + x] = FILLER

        for x in range(COLS):
            for y in range(ROWS):
                print(matrix[y * COLS + x], end="", file=outfile)
