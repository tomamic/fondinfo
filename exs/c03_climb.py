#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randint

TOP = 100              # top of the climb
climb_a = climb_b = 0  # start
win_a = win_b = False  # winner

while not(win_a) and not(win_b):
    climb_a = min(max(climb_a + randint(-1, 3), 0), TOP)
    climb_b = min(max(climb_b + randint(-1, 3), 0), TOP)
    print(climb_a,climb_b)
    if climb_a == TOP:
        win_a = True
    if climb_b == TOP:
        win_b = True
        
if win_a and win_b:
    print("Both climbers win")
elif win_a:
    print("The climber a wins the race")
else:
    print("The climber b wins the race")
