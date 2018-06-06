#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d

x, dx = 50, 5
image = g2d.load_image("ball.png")

def update():
    global x, dx
    g2d.fill_canvas((255, 255, 255))  # Draw background
    g2d.draw_image(image, (x, 50))    # Draw foreground
    if x + dx < 0 or x + dx + 20 > 320:
        dx = -dx
    x = x + dx                        # Update ball's position

def main():
    g2d.init_canvas((320, 240))
    g2d.main_loop(update, 1000 // 30)    # Call update 30 times/second

main()
