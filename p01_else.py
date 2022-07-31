#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

g2d.init_canvas((400, 400))  # width, height

radius = int(g2d.prompt("Radius? [50-99]"))

if 50 <= radius and radius <= 99:
    g2d.set_color((0, 0, 255))
    g2d.fill_circle((200, 200), radius)
else:
    g2d.alert("Out of range!")

g2d.set_color((255, 255, 0))
g2d.fill_circle((200, 200), 25)

g2d.main_loop()  # manage the window/canvas
