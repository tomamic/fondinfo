#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import unittest

class Ball:
    def __init__(self, x: int, y: int, dx=1, dy=1, w=16, h=12):
        if not (0 <= x < w and 0 <= y < h):
            raise ValueError("Out of bounds")
        if not (dx in (-1, 0, 1) and dy in (-1, 0, 1)):
            raise ValueError("Wrong direction")
        self._x = x
        self._y = y
        self._dx = dx
        self._dy = dy
        self._w = w
        self._h = h
        
    def move(self):
        if not (0 <= self._x + self._dx < self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy < self._h):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    @property
    def position(self) -> (int, int):
        return (self._x, self._y)


class SimpleBallTest(unittest.TestCase):
    test_values = ( (8, 4, 1, 1, 9, 5),
                    (8, 11, 1, 1, 9, 10),
                    (15, 4, 1, 1, 14, 5),
                    (0, 4, -1, 1, 1, 5),
                    (8, 0, 1, -1, 9, 1) )

    def test_move(self):
        w, h = 16, 12
        for param in SimpleBallTest.test_values:
            x0, y0, dx, dy, x1, y1 = param
            b = Ball(x0, y0, dx, dy, w, h)
            b.move()
            self.assertTrue(b.position == (x1, y1))
            
    def test_bounce_down(self):
        b = Ball(8, 11)  # dx = 1, dy = 1, w = 16, h = 12
        b.move()
        self.assertTrue(b.position == (9, 10))

    def test_out_of_arena(self):
        with self.assertRaises(ValueError):
            b = Ball(-1, -1)
        
    def test_wrong_dir(self):
        with self.assertRaises(ValueError):
            b = Ball(8, 6, +2, 0)
        
if __name__ == '__main__':
    unittest.main(exit=False)
