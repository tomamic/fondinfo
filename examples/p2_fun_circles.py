import g2d
from random import randrange

def tick():
    if g2d.key_pressed("LeftButton"):
        x, y = g2d.mouse_position()
        g2d.set_color((randrange(256), randrange(256), randrange(256)))
        if x <= 25 and y <= 25 and g2d.confirm("Exit?"):
            g2d.close_canvas()
        else:
            g2d.fill_circle((x, y), 25)

g2d.init_canvas((480, 360))
g2d.main_loop(tick)
