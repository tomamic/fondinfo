#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

g2d.init_canvas((400, 400))

i = 0
while i < 10:
    x = i * 25
    y = i * 25
    red = i * 25
    g2d.draw_rect((red, 0, 0), (x, y, 100, 100))
    i += 1

g2d.main_loop()
