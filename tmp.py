import random, g2d

g2d.init_canvas((400, 400))

n = int(g2d.prompt("n? "))

x, y = 0, 0

step = 255 // n

for i in range(n):
    
    r = random.randrange(4)
    if r == 0:
        y -= 10
    elif r == 1:
        y += 10
    elif r == 2:
        x += 10
    else:
        x -= 10
        
    g2d.set_color((i * step, i * step, i * step))

    cx, cy = x + 200, y + 200
    g2d.draw_line((cx - 3, cy), (cx + 3, cy))
    g2d.draw_line((cx, cy - 3), (cx, cy + 3))

g2d.main_loop()

        