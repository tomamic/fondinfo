#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

text = "Python is a <multi-paradigm> <programming language>, meant to be highly <readable>."

selection = []  # collect text, till the mandatory closing bracket
inside = False

for c in text:
    if c == "<" and not inside:
        inside = True
    elif c == ">" and inside:
        inside = False
        print("".join(selection))
        selection.clear()
    elif inside:
        selection.append(c)
