#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, y, dx = 50, 50, 5
ARENA_W, ARENA_H = 320, 240
BALL_W, BALL_H = 20, 20
image = g2d.load_image("ball.png")

def update():
    global x, dx
    g2d.clear_canvas()                 # Draw background
    g2d.draw_image(image, (x, y))      # Draw foreground
##    if x + dx < 0 or x + dx + BALL_W > ARENA_W:
##        dx = -dx
    x = (x + dx) % ARENA_W             # Update ball's position

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.handle_events(update)          # Set update to be called...
    g2d.main_loop()                    # ... at 30 fps

main()
