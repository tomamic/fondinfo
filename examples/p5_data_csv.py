#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

# remove these two lines if file already exists
##with open("_matrix.csv", "w") as wfile:
##    print("5,7,2,11\n1,3,12,9\n4,6,10,8", file=wfile, end="")

matrix = []
cols, rows = 0, 0

with open("_matrix.csv", "r") as rfile:
    for line in rfile:
        splitted = line.split(",")
        vals = [int(i) for i in splitted]
        matrix.append(vals)
        ## matrix += vals  # for a simple list

        cols = len(vals)
        rows += 1

print(rows, "x", cols)
print(matrix)

total = 0
x, y = cols - 1, rows - 1
while x >= 0 and y >= 0:
    total += matrix[y][x]
    ## total += matrix[y * cols + x]  # for a simple list
    x -= 1
    y -= 1
print(total)
