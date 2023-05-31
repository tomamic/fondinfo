#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena
import p05_pacmanmap as pmmap

tile = 8

class Wall(Actor):
    def __init__(self, pos, size):
        self._pos = pos
        self._size = size

    def move(self, arena):
        return

    def pos(self):
        return self._pos

    def size(self):
        return self._size

    def sprite(self):
        return


class PacMan(Actor):
    def __init__(self, pos: (int, int)):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._dx, self._dy = 0, 0
        self._speed = 2

    def move(self, arena):
        path_l, path_r, path_u, path_d = True, True, True, True
        for other in arena.collisions():
            if isinstance(other, Wall):
                ox, oy, ow, oh = other.pos() + other.size()
                if oy < self._y + self._h and self._y < oy + oh:  ## | overlap
                    if self._x > ox:
                        path_l = False
                    else:
                        path_r = False
                if ox < self._x + self._w and self._x < ox + ow:  ## — overlap
                    if self._y > oy:
                        path_u = False
                    else:
                        path_d = False

        if self._x % tile == 0 and self._y % tile == 0:
            # new direction, only if not leading against a wall
            keys = arena.current_keys()
            u, l, d, r = "wasd"
            if l in keys and path_l:
                self._dx, self._dy = -self._speed, 0
            elif r in keys and path_r:
                self._dx, self._dy = +self._speed, 0
            elif u in keys and path_u:
                self._dx, self._dy = 0, -self._speed
            elif d in keys and path_d:
                self._dx, self._dy = 0, +self._speed

            # if current direction is blocked, PacMan stops
            if (self._dx < 0 and not path_l or self._dx > 0 and not path_r or
                self._dy < 0 and not path_u or self._dy > 0 and not path_d):
                self._dx, self._dy = 0, 0

        self._y += self._dy
        self._x += self._dx
        self._x %= arena.size()[0]

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return (0, 0)


def tick():
    background = "https://tomamic.github.io/images/sprites/pac-man-bg.png"
    sprites = "https://tomamic.github.io/images/sprites/pac-man.png"
    g2d.draw_image(background, (0, 0))
    for a in arena.actors():
        if a.sprite():
            g2d.draw_image_clip(sprites, a.pos(), a.sprite(), a.size())

    arena.tick(g2d.current_keys())

def main():
    global arena, g2d
    import g2d
    arena = Arena(pmmap.size)
    for x, y, w, h in pmmap.walls:
        arena.spawn(Wall((x, y), (w, h)))
    arena.spawn(PacMan(pmmap.pacman))
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
