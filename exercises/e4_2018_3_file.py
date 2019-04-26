#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def generate_file():
    from random import uniform
    with open("values.csv", "w") as csv_out:
        for y in range(20):
            print(uniform(0, 50), uniform(0, 50), sep=",", file=csv_out)

def main():
    max_val, min_val = 0, 0
    total, count = 0, 0
    with open("values.csv", "r") as csv:
        for line in csv:
            for word in line.split(","):
                val = float(word)
                if count == 0 or val > max_val:
                    max_val = val
                if count == 0 or val < min_val:
                    min_val = val
                total += val
                count += 1

    if count > 0:
        print(max_val, min_val, total / count)
