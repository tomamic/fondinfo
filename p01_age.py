#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from datetime import date

b_year = int(input("Birth year? "))
b_month = int(input("Birth month? "))
b_day = int(input("Birth day? "))
now = date.today()

age = now.year - b_year
if now.month < b_month or (now.month == b_month and now.day < b_day):
    age -= 1

print("Your age is", age)
