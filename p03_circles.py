#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from random import randrange

def center(x: int, y: int) -> bool:
    return max(abs(x - W/2), abs(y - H/2)) <= 25

def tick():
    if g2d.mouse_clicked():
        x, y = g2d.mouse_pos()
        if center(x, y) and g2d.confirm("Center! Exit?"):
            g2d.close_canvas()
        else:
            g2d.set_color((randrange(256), randrange(256), randrange(256)))
            g2d.draw_circle((x, y), 25)

W, H = 480, 360
g2d.init_canvas((W, H))
g2d.main_loop(tick)
