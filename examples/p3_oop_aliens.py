#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p2_oop_alien import Alien

def tick():
    g2d.clear_canvas()
    for a in aliens:
        a.move()
        g2d.fill_rect(a.position())

aliens = [Alien(40, 40), Alien(80, 80), Alien(120, 40)]
g2d.init_canvas((480, 360))
g2d.main_loop(tick)
