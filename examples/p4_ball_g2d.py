#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *
from p4_ball import Ball

def update():
    canvas_fill(canvas, (255, 255, 255))  # BG
    for b in balls:
        b.move()
        draw_rect(canvas, (127, 127, 127), b.rect())  # FG

balls = [Ball(40, 80), Ball(80, 40)]
canvas = canvas_init((Ball.ARENA_W, Ball.ARENA_H))
set_interval(update, 1000 // 30)  # Millis

