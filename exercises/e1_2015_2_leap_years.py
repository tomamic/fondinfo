#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

year = int(input("Year? "))
while year != 0:
    if year % 4 == 0 and not(year % 100 == 0 and year % 400 != 0):
        print("Leap")
    else:
        print("Common")
        
##    if year % 400 == 0:
##        print("Leap")
##    elif year % 100 == 0:
##        print("Common")
##    elif year % 4 == 0:
##        print("Leap")
##    else:
##        print("Common")
        
    year = int(input("Year? "))

