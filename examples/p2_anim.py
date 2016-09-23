from game2d import *

def update():
    global x
    screen_fill(canvas, (255, 255, 255))  # Draw background        
    image_blit(canvas, image, (x, 50))    # Draw foreground
    x = (x + 5) % 320                     # Update ball's position

canvas = screen_set_mode((320, 240))
image = image_load("ball.png")
x = 50

timer.set_interval(update, 30)            # Call update 30 times/second
