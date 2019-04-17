#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

g2d.init_canvas((600, 400))  # width, height

g2d.set_color((255, 255, 0))  # red + green = yellow
g2d.fill_rect((150, 100, 250, 200))  # left, top, width, height

g2d.set_color((0, 255, 0))
g2d.draw_line((150, 100), (400, 300))  # point1, point2

g2d.set_color((0, 0, 255))
g2d.fill_circle((400, 300), 20)  # center, radius

g2d.set_color((255, 0, 0))
g2d.draw_text("Hello", (150, 100), 40)  # text, left-top, font-size

g2d.main_loop()  # manage the window/canvas
