import g2d
from random import randrange

def keydown(key):
    x, y = g2d.mouse_position()
    g2d.set_color((randrange(256), randrange(256), randrange(256)))
    g2d.fill_circle((x, y), 25)
    if x <= 10 and y <= 10:
        g2d.close_canvas()

w = int(g2d.prompt("w? "))
h = int(g2d.prompt("h? "))
g2d.init_canvas((w, h))
g2d.handle_events(None, keydown, None)
g2d.main_loop()
