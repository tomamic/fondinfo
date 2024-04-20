#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import random
from actor import Actor, Arena, Point

class Alien(Actor):
    def __init__(self, pos: Point):
        self._x, self._y = pos
        self._w, self._h = 32, 20
        self._pose = 0
        # each alien has its own moving space, e.g. 150px
        self._xmin, self._xmax = self._x, self._x + 150
        self._dx, self._dy = 4, 8

    def move(self, arena: Arena):
        for other in arena.collisions():
            if isinstance(other, Missile):
                arena.kill(self)
        if self._xmin <= self._x + self._dx <= self._xmax:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self._dy
        
        f = 1 + arena.count() // 50
        if random.randrange(500 // f) == 0:
            pos = self._x + self._w / 2, self._y + self._h
            arena.spawn(Bomb(pos))
        self._pose = arena.count() // 8 % 2

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        return 74, 519 if self._pose else 548


class Missile(Actor):
    def __init__(self, pos):
        self._w, self._h = 4, 8
        self._x, self._y = pos
        self._x -= self._w / 2
        self._y -= self._h

    def move(self, arena):
        for other in arena.collisions():
            if isinstance(other, Alien):
                arena.kill(self)

        self._y -= 4
        if self._y < 0:
            arena.kill(self)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 204, 557


class Bomb(Actor):
    def __init__(self, pos):
        self._w, self._h = 4, 8
        self._x, self._y = pos
        self._x -= self._w / 2

    def move(self, arena):
        for other in arena.collisions():
            if isinstance(other, Cannon):
                arena.kill(self)

        aw, ah = arena.size()
        self._y += 4
        if self._y > ah:
            arena.kill(self)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 204, 531


class Cannon(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 28, 16

    def move(self, arena):
        for other in arena.collisions():
            if isinstance(other, Alien):
                arena.kill(self)
            if isinstance(other, Bomb):
                arena.kill(self)


        aw, ah = arena.size()
        keys = arena.current_keys()
        prev = arena.previous_keys()
        if "ArrowUp" in keys and "ArrowUp" not in prev:
            pos = self._x + self._w / 2, self._y
            arena.spawn(Missile(pos))

        if "ArrowLeft" in keys:
            self._x -= 4
        elif "ArrowRight" in keys:
            self._x += 4
        self._x = max(self._x, 0)
        self._x = min(self._x, aw - self._w)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 273, 549

class AlienGame(Arena):
    def __init__(self, size=(480, 360)):
        super().__init__(size)
        for y in range(4):
            for x in range(8):
                self.spawn(Alien((x * 42, y * 24)))
        self.spawn(Cannon((240, 340)))

    def game_over(self) -> bool:
        cannon = False
        for a in self.actors():
            x, y = a.pos()
            if isinstance(a, Alien) and y > 320:
                return True
            if isinstance(a, Cannon):
                cannon = True
        return not cannon

    def game_won(self) -> bool:
        for a in self.actors():
            if isinstance(a, Alien):
                return False
        return True

    def lives(self) -> int:
        for a in self.actors():
            if isinstance(a, Turtle):
                return a.lives()
        return 0

    def time(self) -> int:
        return self._time - self.count()


class AlienGui:
    def __init__(self):
        self._game = AlienGame()
        g2d.init_canvas(self._game.size())
        g2d.main_loop(self.tick)

    def tick(self):
        sprites = "https://tomamic.github.io/images/sprites/invaders.png"
        g2d.clear_canvas()
        for a in self._game.actors():
            if a.sprite():
                g2d.draw_image(sprites, a.pos(), a.sprite(), a.size())
            else:
                g2d.draw_rect(a.pos(), a.size())

        if self._game.game_over():
            g2d.alert("Game over")
            g2d.close_canvas()
        elif self._game.game_won():
            g2d.alert("Game won")
            g2d.close_canvas()
        else:
            self._game.tick(g2d.current_keys())  # Game logic

if __name__ == "__main__":
    import g2d
    gui = AlienGui()
