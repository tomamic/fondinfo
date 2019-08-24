#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import cppyy
cppyy.include("ball.cpp")
from cppyy.gbl import Ball

b = Ball(150, 200)
for i in range(10):
    b.move()
    print(b.get_x(), b.get_y())
