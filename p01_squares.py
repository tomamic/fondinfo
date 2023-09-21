#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

L, l = 500, 200
g2d.init_canvas((L, L))

n = 4        # int(g2d.prompt("N?"))
m_red = 85   # 255 / max(n - 1, 1)
m_pos = 100  # (L - l) / max(n - 1, 1)

for i in range(n):
    pos = i * m_pos
    red = i * m_red
    g2d.set_color((red, 0, 0))
    g2d.draw_rect((pos, pos), (l, l))

g2d.main_loop()
