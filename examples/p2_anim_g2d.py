#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d

def update():
    global x
    game2d.canvas_fill((255, 255, 255))  # Draw background        
    game2d.image_blit(image, (x, 50))    # Draw foreground
    x = (x + dx) % 320                    # Update ball's position

def keydown(code):
    global dx
    if code == "Space":
        dx = -dx

game2d.canvas_init((320, 240))
image = game2d.image_load("ball.png")
x = 50
dx = 5

game2d.handle_keyboard(keydown, None)
game2d.set_interval(update, 1000 // 30)    # Call update 30 times/second
