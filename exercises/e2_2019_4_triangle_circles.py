import g2d
from random import randrange

side = 480
g2d.init_canvas((side, side))
n = int(g2d.prompt("n?"))

d = side // n
r = d // 2

for y in range(1, n + 1):
    for x in range(1, y + 1):
        g2d.set_color((randrange(256), randrange(256), randrange(256)))
        g2d.fill_circle((x * d - r, y * d - r), r)

g2d.main_loop()
