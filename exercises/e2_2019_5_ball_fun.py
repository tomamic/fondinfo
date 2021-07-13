#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d
x, y, dx, dy = 50, 50, 5, 0
ball_w, ball_h, canvas_w, canvas_h = 20, 20, 480, 360

def tick():
    global x, y, dx, dy
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))

    if x + dx > canvas_w - ball_w:
        dx, dy = 0, 5
    elif x + dx < 0:
        dx, dy = 0, -5
    elif y + dy > canvas_h - ball_h:
        dx, dy = -5, 0
    elif y + dy < 0:
        dx, dy = 5, 0
    x += dx
    y += dy


g2d.init_canvas((canvas_w, canvas_h))
g2d.main_loop(tick)
