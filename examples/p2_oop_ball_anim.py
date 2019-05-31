#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p2_oop_ball import Ball, ARENA_W, ARENA_H

def tick():
    g2d.clear_canvas()  # BG
    b1.move()
    b2.move()
    g2d.fill_rect(b1.position())  # FG
    g2d.fill_rect(b2.position())  # FG

def main():
    global b1, b2
    b1 = Ball((40, 80))
    b2 = Ball((80, 40))
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
