#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randrange
from c04_polar import move_around
from c07_bounce import Actor, Arena, Ball, Ghost, Turtle, Point

class TurtleHero(Turtle):
    def __init__(self, pos):
        super().__init__(pos)
        self._lives = 3
        self._blinking = 0

    def move(self, arena):
        super().move(arena)
        if self._blinking > 0:
            self._blinking -= 1

    def hit(self, arena):
        if self._blinking == 0:
            self._blinking = 60
            self._lives -= 1
            if self._lives <= 0:
                arena.kill(self)

    def lives(self) -> int:
        return self._lives

    def sprite(self):
        if self._blinking > 0 and self._blinking % 4 < 2:
            return None
        return super().sprite()


class BounceGame(Arena):
    def __init__(self, size=(500, 500), nballs=3, nghosts=2, time=120*30):
        super().__init__(size)
        w, h = size
        center = w / 2, h / 2
        self.spawn(TurtleHero(center))
        for _ in range(nballs):
            pos = move_around(center, 150, randrange(360))
            self.spawn(Ball(pos))
        for _ in range(nghosts):
            pos = move_around(center, 150, randrange(360))
            self.spawn(Ghost(pos))
        self._time = time

    def game_over(self) -> bool:
        return self.lives() <= 0

    def game_won(self) -> bool:
        return self.time() <= 0

    def lives(self) -> int:
        for a in self.actors():
            if isinstance(a, Turtle):
                return a.lives()
        return 0

    def time(self) -> int:
        return self._time - self.count()


class BounceGui:
    def __init__(self):
        self._game = BounceGame()
        g2d.init_canvas(self._game.size())
        g2d.main_loop(self.tick)

    def tick(self):
        g2d.clear_canvas()
        for a in self._game.actors():
            if a.sprite() != None:
                g2d.draw_image("sprites.png", a.pos(), a.sprite(), a.size())

        lives, time = self._game.lives(), self._game.time() // 30
        g2d.draw_text(f"Lives: {lives} Time: {time}", (250, 12), 24)

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
    gui = BounceGui()
