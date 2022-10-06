#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, y, dx, dy = 50, 50, 5, 5
ARENA_W, ARENA_H = 480, 360
BALL_W, BALL_H = 20, 20

def tick():
    global x, y, dx
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))
    if not 0 <= x + dx <= ARENA_W - BALL_W:
        dx = -dx
        y += dy
    else:
        x += dx

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)  # call tick 30 times/second

main()
