#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

from unittest import TestCase, main
from p31_ball import Ball, ARENA_W, ARENA_H, BALL_W, BALL_H

MAX_X, MAX_Y = ARENA_W - BALL_W, ARENA_H - BALL_H

class SimpleTest(TestCase):

    def test_corner(self):
        b = Ball(MAX_X, MAX_Y)  # dx = 5, dy = 5
        b.move()
        self.assertTrue(b.pos() == (MAX_X - 5, MAX_Y - 5))

    def test_move(self):
        test_values = [ (40, 80, 45, 85),
                        (40, MAX_Y - 5, 45, MAX_Y),
                        (40, MAX_Y, 45, MAX_Y - 5),
                        (MAX_X - 5, 80, MAX_X, 85),
                        (MAX_X, 80, MAX_X - 5, 85) ]

        for param in test_values:
            with self.subTest(param=param):
                x0, y0, x1, y1 = param
                b = Ball(x0, y0)
                b.move()
                self.assertTrue(b.pos() == (x1, y1))


if __name__ == "__main__":
    main()
