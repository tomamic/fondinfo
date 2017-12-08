#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d
from p3_ball import Ball, ARENA_W, ARENA_H

def update():
    g2d.canvas_fill((255, 255, 255))  # BG
    for b in balls:
        b.move()
        g2d.draw_rect((127, 127, 127), b.rect())  # FG

balls = [Ball(40, 80), Ball(80, 40)]
g2d.canvas_init((ARENA_W, ARENA_H))
g2d.set_interval(update, 1000 // 30)  # Millis

