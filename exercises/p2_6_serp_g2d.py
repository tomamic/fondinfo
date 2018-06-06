#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d

x, y, dx = 50, 50, 5
image = g2d.load_image("ball.png")

def update():
    global x, y, dx
    g2d.fill_canvas((255, 255, 255))
    g2d.draw_image(image, (x, y))
    if x + dx < 0 or x + dx + 20 > 320:
        y += 5
        dx = -dx
    else:
        x = x + dx

def main():
    g2d.init_canvas((320, 240))
    g2d.main_loop(update, 1000 // 30)    # Call update 30 times/second

main()
