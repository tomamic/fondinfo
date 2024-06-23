#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

#with open("_groceries.txt", "w") as outf:
#    print("spam\negg\nbaked beans\nbacon", file=outf)

with open("_groceries.txt") as groceries:
    for line in groceries:
        # process line
        print(line.strip(), ":", len(line))