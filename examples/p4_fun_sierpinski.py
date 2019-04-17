#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

def sierpinski(rect: (int, int, int, int)):
    x, y, w, h = rect
    w3, h3 = w // 3, h // 3
    if w3 < 1 or h3 < 1:
        return
    for row in range(3):
        for col in range(3):
            rect3 = x + col * w3, y + row * h3, w3, h3
            if row == 1 and col == 1:
                g2d.fill_rect(rect3)
            else:
                sierpinski(rect3)

def main():
    g2d.init_canvas((263, 263))
    g2d.set_color((127, 0, 0))
    sierpinski((10, 10, 243, 243))
    g2d.main_loop()

main()
