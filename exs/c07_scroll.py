#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from random import randrange
from p32_bounce import Ball, Arena

# arena & actors aren't aware of view
ARENA_W, ARENA_H = 500, 250
arena = Arena((ARENA_W, ARENA_H))
for _ in range(10):
    pos = randrange(ARENA_W - 20), randrange(ARENA_H - 20)
    arena.spawn(Ball(pos))

# view size is smaller than arena
VIEW_W, VIEW_H = 300, 200
view_x, view_y = 0, 0

def tick():
    global view_x, view_y
    keys = g2d.current_keys()
    if "ArrowUp" in keys:
        view_y = max(view_y - 10, 0)
    elif "ArrowRight" in keys:
        view_x = min(view_x + 10, ARENA_W - VIEW_W)
    elif "ArrowDown" in keys:
        view_y = min(view_y + 10, ARENA_H - VIEW_H)
    elif "ArrowLeft" in keys:
        view_x = max(view_x - 10, 0)

    # translate background and sprites in view's coords
    g2d.draw_image("viewport.png", (0, 0),
                        (view_x, view_y), (VIEW_W, VIEW_H))
    for a in arena.actors():
        x, y = a.pos()
        g2d.draw_image("ball.png", (x - view_x, y - view_y))
    arena.tick()

def main():
    g2d.init_canvas((VIEW_W, VIEW_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
