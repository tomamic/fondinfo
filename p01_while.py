#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

g2d.init_canvas((400, 400))  # width, height

r = int(g2d.prompt("Radius? [50-99]"))

while r < 50 or r > 99:
    g2d.alert("Out of range!")
    r = int(g2d.prompt("Radius? [50-99]"))

g2d.set_color((0, 0, 255))
g2d.draw_circle((200, 200), r)

g2d.main_loop()  # manage the window/canvas
