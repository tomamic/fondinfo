#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d

x, y, dx, dy = 50, 50, 5, 5
count = 0
ARENA_W, ARENA_H, BALL_W, BALL_H = 320, 240, 20, 20

def tick():
    global x, y, count
    if "LeftButton" in g2d.current_keys() and count == 10:
        count = 0
    g2d.clear_canvas()             # Draw background
    g2d.draw_image("ball.png", (x, y))  # Draw foreground
    if count < 10:
        x = (x + dx) % ARENA_W     # Update ball's position
        y = (y + dy) % ARENA_H     # Update ball's position
        count += 1

def main():
    global dx, dy
    g2d.init_canvas((ARENA_W, ARENA_H))
    dx = int(g2d.prompt("dx?"))
    dy = int(g2d.prompt("dy?"))
    g2d.main_loop(tick, 10)  # Call tick 10 times/second

main()
