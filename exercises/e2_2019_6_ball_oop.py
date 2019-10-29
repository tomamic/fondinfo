import g2d
from random import randrange
img = g2d.load_image("ball.png")
canvas_w, canvas_h = 480, 360

class Ball:
    def __init__(self):
        self._w, self._h = 20, 20
        self._dx, self._dy = 5, 0
        self._x = randrange(canvas_w - self._w)
        self._y = randrange(canvas_h - self._h)
    def move(self):
        if self._x + self._dx > canvas_w - self._w:
            self._x = canvas_w - self._w
            self._dx, self._dy = 0, 5
        elif self._x + self._dx < 0:
            self._x = 0
            self._dx, self._dy = 0, -5
        elif self._y + self._dy > canvas_h - self._h:
            self._y = canvas_h - self._h
            self._dx, self._dy = -5, 0
        elif self._y + self._dy < 0:
            self._y = 0
            self._dx, self._dy = 5, 0
        self._x += self._dx
        self._y += self._dy
    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

def tick():
    b.move()
    x, y, w, h = b.position()

    g2d.clear_canvas()
    g2d.draw_image(img, (x, y))

b = Ball()
g2d.init_canvas((canvas_w, canvas_h))
g2d.main_loop(tick)
