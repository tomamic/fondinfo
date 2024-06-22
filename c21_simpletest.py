#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from unittest import TestCase, main
from c06_ball import Ball, ARENA_W, ARENA_H, BALL_W, BALL_H

MAX_X, MAX_Y = ARENA_W - BALL_W, ARENA_H - BALL_H

class SimpleTest(TestCase):

    def test_corner(self):
        b = Ball(MAX_X, MAX_Y)  # dx = 4, dy = 4
        b.move()
        self.assertTrue(b.pos() == (MAX_X - 4, MAX_Y - 4))

    def test_move(self):
        test_values = [ (40, 80, 44, 84),
                        (40, MAX_Y - 4, 44, MAX_Y),
                        (40, MAX_Y, 44, MAX_Y - 4),
                        (MAX_X - 4, 80, MAX_X, 84),
                        (MAX_X, 80, MAX_X - 4, 84) ]

        for param in test_values:
            with self.subTest(param=param):
                x0, y0, x1, y1 = param
                b = Ball(x0, y0)
                b.move()
                self.assertTrue(b.pos() == (x1, y1))


if __name__ == "__main__":
    main()
