import unittest
from p3_oop_bounce import Arena, Ball, Ghost, Turtle


class BallTest(unittest.TestCase):

    def test_corner(self):
        a = Arena((480, 360))
        b = Ball(a, (460, 340))  # dx = 5, dy = 5
        b.move()  # dx = -5, dy = -5
        b.move()
        self.assertTrue(b.position() == (450, 330, 20, 20))

    def test_move(self):
        a = Arena((480, 360))
        test_values = ( (40, 80, 45, 85),
                        (40, 215, 45, 220),
                        (40, 340, 45, 335),
                        (295, 80, 300, 85),
                        (460, 80, 455, 85) )
        for param in test_values:
            x0, y0, x1, y1 = param
            b = Ball(a, (x0, y0))
            b.move()
            self.assertTrue(b.position() == (x1, y1, 20, 20))


class TurtleTest(unittest.TestCase):

    def test_right(self):
        a = Arena((480, 360))
        t = Turtle(a, (230, 170))
        t.go_right(True)
        t.move()
        t.move()
        t.go_right(False)
        t.move()  # no effect
        self.assertTrue(t.position() == (234, 170, 20, 20))

    def test_collide_ball(self):
        a = Arena((480, 360))
        b = Ball(a, (0, 0))
        t = Turtle(a, (230, 170))
        t.collide(b)
        t.collide(b)  # no effect
        self.assertTrue(t.lives() == 2)

    def test_collide_ghost(self):
        a = Arena((480, 360))
        g = Ghost(a, (0, 0))
        t = Turtle(a, (230, 170))
        t.collide(g)
        self.assertTrue(t.lives() == 0)


if __name__ == '__main__':
    unittest.main()
