#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import g2d

g2d.init_canvas((500, 500))

for i in range(4):  # (0, 1, 2, 3)
    red = i * 85    # proportional to i
    g2d.set_color((red, 0, 0))

    pos = i * 100   # proportional to i
    g2d.draw_rect((pos, pos), (200, 200))

g2d.main_loop()
