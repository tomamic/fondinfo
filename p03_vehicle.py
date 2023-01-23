#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''
import g2d

x, y, dx = 50, 50, 5
ARENA_W, ARENA_H = 480, 360
XMIN, XMAX = -100, ARENA_W + 100

def tick():
    global x, dx
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))
    if g2d.mouse_clicked():
        dx = -dx
    if x + dx < XMIN:
        x += XMAX - XMIN
    if x + dx > XMAX:
        x -= XMAX - XMIN
    x += dx

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
