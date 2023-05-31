#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

ARENA_W, ARENA_H = 500, 250
VIEW_W, VIEW_H = 300, 200
BALL_W, BALL_H = 20, 20

class FallingBall:
    def __init__(self, pos, speed=(4, 0), gravity=0.4):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = speed
        self._g = gravity

    def move(self):
        if not (0 <= self._x + self._dx <= ARENA_W - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ARENA_H - self._h):
            self._dy = -self._dy
        else:
            self._dy += self._g

        self._x += self._dx
        self._y += self._dy

    def pos(self) -> (int, int):
        return self._x, self._y

    def size(self) -> (int, int):
        return self._w, self._h

    def sprite(self) -> (int, int):
        if self._g == 0:
            return 20, 0
        return 0, 0


balls = [FallingBall((40, 80)), FallingBall((80, 120)),
         FallingBall((60, 60), (3, 0), 0), FallingBall((60, 80), (-3, 0), 0)]
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

    g2d.draw_image_clip("https://raw.githubusercontent.com/tomamic/tomamic.github.io/master/images/oop/viewport.png",
                        (0, 0), (view_x, view_y), (VIEW_W, VIEW_H))
    for a in balls:
        x, y = a.pos()
        g2d.draw_image_clip("sprites.png", (x - view_x, y - view_y), a.sprite(), a.size())
        a.move()

def main():
    g2d.init_canvas((VIEW_W, VIEW_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
