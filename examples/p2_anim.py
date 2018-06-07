#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, dx = 50, 5
image = g2d.load_image("ball.png")

def update():
    global x
    g2d.fill_canvas((255, 255, 255))  # Draw background
    g2d.draw_image(image, (x, 50))    # Draw foreground
    x = (x + dx) % 320                # Update ball's position

def keydown(code):
    global dx
    if code == "Space":
        dx = -dx

def keyup(code):
    pass

def main():
    g2d.init_canvas((320, 240))
    g2d.handle_keyboard(keydown, keyup)
    g2d.main_loop(update, 1000 // 30)    # Call update 30 times/second

main()
