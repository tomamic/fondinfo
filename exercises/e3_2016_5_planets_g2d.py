import g2d
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
        return int(x), int(y)

    def move(self):
        self._theta += self._omega

    def diameter(self):
        return self._diameter

    def color(self):
        return self._color


def new_frame():
    center_x, center_y = canvas_w // 2, canvas_h // 2
    g2d.fill_canvas((255, 255, 255))
    g2d.draw_circle((255, 255, 0), (center_x, center_y), 30)
    for p in planets:
        p.move()
        x, y = p.pos()
        radius = p.diameter() // 2
        g2d.draw_circle(p.color(),
                        (center_x + x, center_y + y),
                        p.diameter() // 2)

def main():
    global planets, canvas_w, canvas_h
    
    canvas_w, canvas_h = 600, 600
    planets = []
    for i in range(5):
        p = Planet(100 + i * 40)
        planets.append(p)
    g2d.init_canvas((canvas_w, canvas_h))

    g2d.main_loop(new_frame, 1000 // 30)

main()
