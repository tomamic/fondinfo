#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, y, dx, count = 40, 40, -2, 0
ARENA_W, ARENA_H = 480, 360

def tick():
    global x, dx, count
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))
    if "LeftButton" in g2d.current_keys() and count == 0:
        count = 10
        dx = -dx
    if count > 0:
        count -= 1
        x += dx

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick, 5)  # call tick 5 times/second

main()
