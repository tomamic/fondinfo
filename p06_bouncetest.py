import unittest
from p05_bouncegame import Arena, Ball, Ghost, TurtleHero


class BallTest(unittest.TestCase):

    def test_corner(self):
        a = Arena((480, 360))
        b = Ball((460, 340))  # dx = 4, dy = 4
        b.move(a)  # dx = -4, dy = -4
        b.move(a)
        self.assertEqual(b.pos(), (452, 332))

    def test_move(self):
        a = Arena((480, 360))
        test_values = ( (40, 80, 44, 84),
                        (40, 215, 44, 219),
                        (40, 340, 44, 336),
                        (295, 80, 299, 84),
                        (460, 80, 456, 84) )
        for param in test_values:
            x0, y0, x1, y1 = param
            b = Ball((x0, y0))
            b.move(a)
            self.assertEqual(b.pos(), (x1, y1))


class TurtleTest(unittest.TestCase):

    def test_right(self):
        a = Arena((480, 360))
        a.tick(("ArrowRight"))
        t = TurtleHero((230, 170))
        t.move(a)
        t.move(a)
        a.tick()
        t.move(a)  # no effect
        self.assertEqual(t.pos(), (234, 170))

    def test_collide_ball(self):
        a = Arena((480, 360))
        b = Ball((0, 0))
        t = TurtleHero((230, 170))
        t.collide(b, a)
        t.collide(b, a)  # no effect
        self.assertEqual(t.lives(), 2)

    def test_collide_ghost(self):
        a = Arena((480, 360))
        g = Ghost((0, 0))
        t = TurtleHero((230, 170))
        t.collide(g, a)
        self.assertEqual(t.lives(), 3)


if __name__ == '__main__':
    unittest.main()
