#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, y, dx = 50, 50, 5
ARENA_W, ARENA_H, MARGIN = 480, 360, 100
image = g2d.load_image("ball.png")

def tick():
    global x, dx
    if g2d.key_pressed("Enter"):
        dx = -dx
    if x + dx < -MARGIN:
        x = ARENA_W + MARGIN
    if x + dx > ARENA_W + MARGIN:
        x = -MARGIN
    g2d.clear_canvas()             # Draw background
    g2d.draw_image(image, (x, y))  # Draw foreground
    x += dx                        # Update ball's position

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)  # call tick 30 times/second

main()
