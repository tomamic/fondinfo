import g2d
from random import randrange

def keydown(key):
    x, y = g2d.mouse_position()
    g2d.set_color((randrange(256), randrange(256), randrange(256)))
    if x <= 25 and y <= 25 and g2d.confirm("Exit?"):
        g2d.close_canvas()
    else:
        g2d.fill_circle((x, y), 25)

g2d.init_canvas((640, 480))
g2d.handle_events(None, keydown, None)
g2d.main_loop()
