#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

year = int(input("What's your birth year? "))
if (2024 - year) % 12 == 0:
    print("Your sign is Dragon")
else:
    print("Your sign is not Dragon")
