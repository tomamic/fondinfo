from game2d import *
import math
import random

class Planet:

    def __init__(self, orbit):
        self._orbit = orbit
        self._theta = random.uniform(0, math.pi * 2)
        self._omega = random.uniform(0.01, 0.04)
        self._diameter = random.randint(10, 20)
        self._color = (random.randrange(256),
                       random.randrange(256),
                       random.randrange(256))

    def pos(self):
        x = self._orbit * math.cos(self._theta)
        y = self._orbit * math.sin(self._theta)
        return x, y

    def move(self):
        self._theta += self._omega

    def diameter(self):
        return self._diameter

    def color(self):
        return self._color


def new_frame():
    center_x, center_y = canvas.width // 2, canvas.height // 2
    canvas_fill(canvas, (255, 255, 255))
    draw_circle(canvas, (255, 255, 0), (center_x, center_y), 30)
    for p in planets:
        p.move()
        x, y = p.pos()
        radius = p.diameter() // 2
        draw_circle(canvas, p.color(),
                    (center_x + x, center_y + y), p.diameter() // 2)

planets = []
for i in range(5):
    p = Planet(100 + i * 40)
    planets.append(p)
canvas = canvas_init((600, 600))

set_interval(new_frame, 1000 // 30)
