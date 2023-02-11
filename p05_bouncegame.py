#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import randrange
from p05_bounce import Actor, Arena, Ball, Ghost, Turtle

def randpt(w: int, h: int) -> (int, int):
    x, y = randrange(w - 20), randrange(h - 20)
    while (x - w // 2) ** 2 + (y - h // 2) ** 2 < 100 ** 2:
        x, y = randrange(w - 20), randrange(h - 20)
    return x, y

class TurtleHero(Turtle):
    def __init__(self, pos):
        super().__init__(pos)
        self._lives = 3
        self._blinking = 0

    def move(self, arena: Arena):
        super().move(arena)
        if self._blinking > 0:
            self._blinking -= 1

    def hit(self, arena: Arena):
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
    def __init__(self, size=(480, 360), nballs=3, nghosts=2, secs=120):
        super().__init__(size)
        w, h = size
        self.spawn(TurtleHero((w // 2, h // 2)))  # center
        for _ in range(nballs):
            self.spawn(Ball(randpt(w, h)))
        for _ in range(nghosts):
            self.spawn(Ghost(randpt(w, h)))
        self._secs = secs

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
        return self._secs - self.count() // 30


class BounceGui:
    def __init__(self):
        self._game = BounceGame()
        g2d.init_canvas(self._game.size())
        g2d.main_loop(self.tick)

    def tick(self):
        g2d.clear_canvas()
        for a in self._game.actors():
            if a.sprite() != None:
                g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())
            else:
                pass  # g2d.draw_rect(a.pos(), a.size())
        lives, time = self._game.lives(), self._game.time()
        g2d.draw_text(f"Lives: {lives} Time: {time}", (0, 0), 24)

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
