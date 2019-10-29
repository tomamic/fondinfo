import g2d
from random import randrange
img = g2d.load_image("ball.png")
canvas_w, canvas_h = 480, 360

class TurningBall:
    def __init__(self):
        self._w, self._h = 20, 20
        self._dx, self._dy = 5, 0
        self._count = 0
        self._x = randrange(canvas_w - self._w)
        self._y = randrange(canvas_h - self._h)
    def move(self):
        self._x += self._dx
        self._y += self._dy
        self._count += 1
        if self._count == 10:
            self._dx, self._dy = self._dy, -self._dx  # rot 90°
            self._count == 0
    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

def tick():
    b.move()
    x, y, w, h = b.position()

    g2d.clear_canvas()
    g2d.draw_image(img, (x, y))

b = TurningBall()
g2d.init_canvas((canvas_w, canvas_h))
g2d.main_loop(tick)
