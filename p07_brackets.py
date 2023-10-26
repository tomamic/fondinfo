#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

text = "Python is a <multi-paradigm> <programming language>, meant to be highly <readable>."

selection = []  # collect text, till the mandatory closing bracket
inside = False

for c in text:
    if c == "<" and not inside:
        inside = True
        selection = []
    elif c == ">" and inside:
        inside = False
        print("".join(selection))
    elif inside:
        selection.append(c)
