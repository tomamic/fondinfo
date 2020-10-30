import g2d_pygame as g2d
import math

def move_pen(start: (float, float), length: float, angle: float) -> (float, float):
    x, y = start
    x1 = x + math.cos(angle) * length
    y1 = y + math.sin(angle) * length
    g2d.draw_line((int(x), int(y)), (int(x1), int(y1)))
    return (x1, y1)


def main():
    g2d.init_canvas((600, 600))

    pos, side, angle = (100, 127), 400, 0  # →

    for i in range(3):
        pos = move_pen(pos, side, angle)
        angle += math.pi * 2/3  # ↻ 120°

    g2d.main_loop()

main()
