#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from random import randrange

def tick():
    if g2d.mouse_clicked():
        x, y = g2d.mouse_pos()
        if x <= 25 and y <= 25 and g2d.confirm("Exit?"):
            g2d.close_canvas()
        else:
            g2d.set_color((randrange(256), randrange(256), randrange(256)))
            g2d.fill_circle((x, y), 25)

g2d.init_canvas((480, 360))
g2d.main_loop(tick)
