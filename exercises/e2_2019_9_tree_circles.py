import g2d
from random import randrange

side = 480
g2d.init_canvas((side, side))
n = int(g2d.prompt("n?"))

d = side // (n + 1)
r = d // 2
start = side // 2

for y in range(1, n + 1):
    for x in range(y):
        g2d.set_color((randrange(256), randrange(256), randrange(256)))
        g2d.fill_circle((start + x * d, y * d - r), r)
    start -= r

g2d.set_color((randrange(256), randrange(256), randrange(256)))
g2d.fill_circle((side // 2, side - r), r)

g2d.main_loop()
