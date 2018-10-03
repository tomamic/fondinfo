#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p2_oop_ball import Ball, ARENA_W, ARENA_H

def update():
    g2d.fill_canvas((255, 255, 255))  # BG
    b1.move()
    b2.move()
    g2d.draw_rect((127, 127, 127), b1.position())  # FG
    g2d.draw_rect((127, 127, 127), b2.position())  # FG

def main():
    global b1, b2
    b1 = Ball(40, 80)
    b2 = Ball(80, 40)
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(update, 1000 // 30)  # Millis

main()
