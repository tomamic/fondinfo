#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, y, dy, count = 40, 40, -4, 0
ARENA_W, ARENA_H = 480, 360

def tick():
    global y, dy, count
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))
    if g2d.mouse_clicked() and count == 0:
        count = 5
        dy = -dy
    if count > 0:
        count -= 1
        y += dy

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick, 10)  # call tick 10 times/second

main()
