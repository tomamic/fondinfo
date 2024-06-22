#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

year = int(input("What's your birth year? "))
if (2024 - year) % 12 == 0:
    print("Your sign is Dragon")
else:
    print("Your sign is not Dragon")
