import g2d

g2d.init_canvas((300, 300))

for i in range(5):  ## range(0, 5)
    x = i * 40
    y = x
    red = i * 60
    g2d.set_color((red, 0, 0))
    g2d.fill_rect((x, y, 140, 140))

g2d.main_loop()
