#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, y, dx, dy = 50, 50, 5, 5
count = 0
ARENA_W, ARENA_H = 320, 240
BALL_W, BALL_H = 20, 20
image = g2d.load_image("ball.png")

def update():
    global x, y, count
    g2d.clear_canvas()             # Draw background
    g2d.draw_image(image, (x, y))  # Draw foreground
    if count < 5:
        x = (x + dx) % ARENA_W     # Update ball's position
        y = (y + dy) % ARENA_H     # Update ball's position
        count += 1

def keydn(code: str):
    global count
    if count == 5:
        count = 0

def main():
    global dx, dy
    dx = int(g2d.prompt("dx?"))
    dy = int(g2d.prompt("dy?"))
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.handle_events(update, keydn, None)
    g2d.main_loop(5)  # Call update 5 times/second

main()
