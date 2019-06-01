#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from x2_oop_vehicle import Vehicle

def tick():
    g2d.clear_canvas()
    for a in actors:
        a.move()
        g2d.fill_rect(a.position())

actors = [Vehicle((40, 40), 5),
          Vehicle((120, 40), 5),
          Vehicle((80, 80), -5)]
g2d.init_canvas((480, 360))
g2d.main_loop(tick)
