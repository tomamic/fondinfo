#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import choice, randrange

ARENA_W, ARENA_H = 400, 400

class Ghost:
    def __init__(self):
        self._w, self._h = 20, 20
        self._x, self._y = ARENA_W // 2, ARENA_H // 2
        self._visible = True

    def move(self):
        dx = choice([-4, 0, 4])
        dy = choice([-4, 0, 4])
        self._x = (self._x + dx) % ARENA_W
        self._y = (self._y + dy) % ARENA_H

        if randrange(100) == 0:
            self._visible = not self._visible

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        if self._visible:
            return 20, 0
        return 20, 20


def tick():
    g2d.clear_canvas()
    for g in ghosts:
        # Cut an area from a larger image
        g2d.draw_image("sprites.png", g.pos(), g.sprite(), g.size())
        g.move()

def main():
    global g2d, ghosts
    import g2d  # Ghost does not depend on g2d

    ghosts = []
    for i in range(5):
        ghosts.append(Ghost())

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
