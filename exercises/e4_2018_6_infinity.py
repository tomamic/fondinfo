import sys
sys.path.append("../examples")
import g2d

def infinite_circles(x: int, y: int, w: int, h: int,
                     c1: (int, int, int), c2: (int, int, int)):
    w2, h2 = w // 2, h // 2
    if h2 < 1:
        return
    g2d.set_color(c1)
    g2d.fill_circle((x + w2, y + h2), h2)

    infinite_circles(x, y, w, h2, c2, c1)
    infinite_circles(x, y + h2, w, h2, c2, c1)

g2d.init_canvas((600, 600))
infinite_circles(10, 10, 580, 580, (0, 0, 255), (255, 255, 0))
g2d.main_loop()
