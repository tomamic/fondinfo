from random import choice, randrange

class Ghost:
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._visible = True

    def move(self):
        arena_w, arena_h = 480, 360
        dx = choice([-4, 0, 4])
        dy = choice([-4, 0, 4])
        self._x = (self._x + dx) % arena_w
        self._y = (self._y + dy) % arena_h

        if randrange(100) == 0:
            self._visible = not self._visible

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        if self._visible:
            return 20, 0
        return 20, 20


def tick():
    g2d.clear_canvas()
    for g in ghosts:
        # Cut an area from a larger image
        g2d.draw_image_clip("sprites.png", g.pos(), g.sprite(), g.size())
        g.move()

def main():
    global g2d, ghosts
    import g2d  # Ghost does not depend on g2d

    ghosts = []
    for i in range(5):
        ghosts.append(Ghost((randrange(480), randrange(360))))

    g2d.init_canvas((480, 360))
    g2d.main_loop(tick)

##main()
