#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d
from p3_3_alien_g2d import Alien

def update():
    g2d.fill_canvas((255, 255, 255))
    for a in aliens:
        a.move()
        g2d.draw_rect((127, 127, 127), a.position())

aliens = [Alien(40, 40), Alien(80, 80), Alien(120, 40)]
g2d.init_canvas((320, 240))
g2d.main_loop(update, 1000 // 30)
