#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

ARENA_W, ARENA_H = 320, 240
x, y, dx, dy = 50, 50, 5, 5
image = g2d.load_image("ball.png")

def tick():
    global x, y, dx
    g2d.clear_canvas()
    g2d.draw_image(image, (x, y))
    if 0 <= x + dx <= ARENA_W - 20:
        x += dx
    else:
        y += dy
        dx = -dx

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick, 5)  # 5 fps

main()
