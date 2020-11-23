#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import cppyy
cppyy.include("ball.cpp")
from cppyy.gbl import Ball

b1 = Ball(140, 180)
b2 = Ball(180, 140)

for i in range(25):
    b1.move()
    b2.move()
    print(b1.pos_x(), b1.pos_y())
    print(b2.pos_x(), b2.pos_y())
