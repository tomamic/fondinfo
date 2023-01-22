#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena

board = ["#############################",
         "#             #             #",
         "# ------------# ------------#",
         "# -### -#### -# -#### -### -#",
         "# +### -#### -# -#### -### +#",
         "# -    -     -  -     -    -#",
         "# --------------------------#",
         "# -### -# -####### -# -### -#",
         "# -    -# -   #    -# -    -#",
         "# ------# ----# ----# ------#",
         "###### -####  #  #### -######",
         "###### -#           # -######",
         "###### -#           # -######",
         "###### -#  #######  # -######",
         "       -   #######    -      ",
         "       -   #######    -      ",
         "###### -#  #######  # -######",
         "###### -#           # -######",
         "###### -#           # -######",
         "###### -#  #######  # -######",
         "#      -      #       -     #",
         "# ------------# ------------#",
         "# -### -#### -# -#### -### -#",
         "# -  # -     -  -     -#   -#",
         "# +--# -------  -------# --+#",
         "### -# -# -####### -# -# -###",
         "#   -  -# -   #    -# -  -  #",
         "# ------# ----# ----# ------#",
         "# -######### -# -######### -#",
         "# -          -  -          -#",
         "# --------------------------#",
         "#############################"]

tile_w, tile_h = 8, 8  # each char in the map represents a 8×8 block

def in_wall(x, y, w, h) -> bool:
    x0, y0 = x // tile_w, y // tile_h
    x1, y1 = (x + w - 1) // tile_w, (y + h - 1) // tile_h
    return "#" in "".join(line[x0:x1 + 1] for line in board[y0:y1 + 1])
    ##for line in board[y0:y1 + 1]:
    ##    if "#" in line[x0:x1 + 1]: return True
    ##return False

class PacMan(Actor):
    def __init__(self, pos: (int, int)):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._dx, self._dy = 0, 0
        self._speed = 2

    def move(self, arena):
        if self._x % tile_w == 0 and self._y % tile_h == 0:
            # TODO : new dir, only if not leading against a wall
            keys = arena.current_keys()
            if "a" in keys:
                self._dx, self._dy = -self._speed, 0
            elif "d" in keys:
                self._dx, self._dy = +self._speed, 0
            elif "w" in keys:
                self._dx, self._dy = 0, -self._speed
            elif "s" in keys:
                self._dx, self._dy = 0, +self._speed

        if in_wall(self._x + self._dx, self._y + self._dy, self._w, self._h):
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

    arena.tick(g2d.current_keys())
    g2d.draw_image(background, (0, 0))
    for a in arena.actors():
        g2d.draw_image_clip(sprites, a.pos(), a.sprite(), a.size())

def main():
    global arena
    arena = Arena((232, 256))
    arena.spawn(PacMan((112, 184)))
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
