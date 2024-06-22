#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

b_year = int(input("Birth year? "))
b_month = int(input("Birth month? "))
b_day = int(input("Birth day? "))

c_year = int(input("Current year? "))
c_month = int(input("Current month? "))
c_day = int(input("Current day? "))

age = c_year - b_year
if c_month < b_month or (c_month == b_month and c_day < b_day):
    age -= 1

print("Your age is", age)
