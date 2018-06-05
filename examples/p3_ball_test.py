#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import unittest
from p3_ball import Ball


class SimpleBallTest(unittest.TestCase):

    def test_bounce_down(self):
        b = Ball(300, 220)  # dx = 5, dy = 5
        b.move()
        self.assertTrue(b.position() == (295, 215, 20, 20))

    def test_move(self):
        test_values = ( (40, 80, 45, 85),
                        (40, 215, 45, 220),
                        (40, 220, 45, 215),
                        (295, 80, 300, 85),
                        (300, 80, 295, 85) )

        for param in test_values:
            with self.subTest(param=param):
                x0, y0, x1, y1 = param
                b = Ball(x0, y0)
                b.move()
                self.assertTrue(b.position() == (x1, y1, 20, 20))
        
        
if __name__ == '__main__':
    unittest.main()
