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

    n = 3  # triangle
    pos, side, angle = (200, 200), 200, 0  # →

    for i in range(n):
        pos = move_pen(pos, side, angle)
        angle += 2 * math.pi / n  # ↻ 120°

    g2d.main_loop()

main()
