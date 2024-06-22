#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import g2d

x, y, dx = 40, 40, 4
ARENA_W, ARENA_H = 480, 360

def tick():
    global x, dx
    g2d.clear_canvas()                  # Draw background
    g2d.draw_image("ball.png", (x, y))  # Draw foreground
    ##if g2d.mouse_clicked(): ...
    ##if x + dx > ARENA_W: ...
    x += dx                             # Update ball’s position

g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(tick)  # call tick 30 times/second
