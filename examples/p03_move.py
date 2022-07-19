#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

# way too much global stuff!
x1, y1, dx1, dy1 = 40, 80, 5, 5
x2, y2, dx2, dy2 = 80, 40, 5, 5
ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

# encapsulates behaviour, but exposes data
def move_ball(x: int, y: int,
              dx: int, dy: int) -> (int, int, int, int):
    if not 0 <= x + dx <= ARENA_W - BALL_H:
        dx = -dx
    if not 0 <= y + dy <= ARENA_H - BALL_H:
        dy = -dy
    x += dx
    y += dy
    return (x, y, dx, dy)

def tick():
    global x1, y1, dx1, dy1
    global x2, y2, dx2, dy2
    g2d.clear_canvas()               # Draw background
    g2d.draw_image("ball.png", (x1, y1))  # Draw foreground
    g2d.draw_image("ball.png", (x2, y2))  # Draw foreground
    x1, y1, dx1, dy1 = move_ball(x1, y1, dx1, dy1)
    x2, y2, dx2, dy2 = move_ball(x2, y2, dx2, dy2)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)  # call tick 30 times/second

main()
