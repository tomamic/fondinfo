#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p2_oop_alien import Alien

def update():
    g2d.fill_canvas()
    for a in aliens:
        a.move()
        g2d.fill_rect(a.position())

aliens = [Alien(40, 40), Alien(80, 80), Alien(120, 40)]
g2d.init_canvas((320, 240))
g2d.handle_events(update)
g2d.main_loop()
