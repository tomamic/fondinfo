import unittest

from p4_ball import Ball

class ParamBallTest(unittest.TestCase):
    TEST_VALUES = ( (40, 80, 45, 85),
                    (40, 215, 45, 220),
                    (40, 220, 45, 215),
                    (295, 80, 300, 85),
                    (300, 80, 295, 85) )

    def test_move(self):
        for param in ParamBallTest.TEST_VALUES:
            with self.subTest(param=param):
                x0, y0, x1, y1 = param
                b = Ball(x0, y0)
                b.move()
                self.assertTrue(b.rect() == (x1, y1, 20, 20))

    def test_corner(self):
        b = Ball(300, 220)  # dx = 5, dy = 5
        b.move()
        self.assertTrue(b.rect() == (295, 215, 20, 20))

if __name__ == '__main__':
    unittest.main(exit=False)

