#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, y, dx = 50, 50, 5
image = g2d.load_image("ball.png")

def tick():
    global x, y, dx
    g2d.clear_canvas()
    g2d.draw_image(image, (x, y))
    if x + dx < 0 or x + dx + 20 > 320:
        y += 5
        dx = -dx
    else:
        x = x + dx

def main():
    g2d.init_canvas((320, 240))
    g2d.main_loop(tick)

main()
