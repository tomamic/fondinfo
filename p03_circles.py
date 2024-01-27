#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from random import randrange
from math import dist

def tick():
    if g2d.mouse_clicked():
        pos = g2d.mouse_pos()
        if dist(pos, center) <= R and g2d.confirm("Center! Exit?"):
            g2d.close_canvas()
        else:
            col = (randrange(256), randrange(256), randrange(256))
            g2d.set_color(col)
            g2d.draw_circle(pos, R)

W, H, R = 480, 360, 25
center = (W / 2, H / 2)
g2d.init_canvas((W, H))
g2d.main_loop(tick)
