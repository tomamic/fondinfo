#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d, math

g2d.init_canvas((400, 400))  # width, height

r = 100
for i in range(5):
    angle = i * (math.pi / 18)  # 10°
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    g2d.draw_circle((x, y), 5)

g2d.main_loop()  # manage the window/canvas
