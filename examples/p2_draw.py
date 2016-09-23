from game2d import *

canvas = canvas_init((400, 400))

draw_rect(canvas, (165, 0, 255), (100, 100, 250, 250))
draw_circle(canvas, (255, 0, 0), (100, 100), 20)

draw_text(canvas, "Hello", (0, 255, 0), (0, 0), 60)
