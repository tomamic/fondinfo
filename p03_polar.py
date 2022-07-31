from math import cos, atan2, pi, sin, sqrt

def radius(pt: (float, float)) -> float:
    x, y = pt
    return (x ** 2 + y ** 2) ** 0.5

def angle(pt: (float, float)) -> float:
    x, y = pt
    return atan2(y, x)  # atan(y/x), correct sign

def to_polar(pt: (float, float)) -> (float, float):
    r = radius(pt)
    a = angle(pt)
    return (r, a)

def from_polar(plr: (float, float)) -> (float, float):
    r, a = plr
    return (r * cos(a), r * sin(a))

def rotate(pt: (float, float), a: float) -> (float, float):
    x, y = pt
    x1 = x * cos(a) - y * sin(a)
    y1 = x * sin(a) + y * cos(a)
    return (x1, y1)

def main():
    pt0 = from_polar((2, pi/4))
    # pt0 = sqrt(2), sqrt(2)  # same point, ∡ π/4
    pt1 = rotate(pt0, pi/12)  # (1, √3) ∡ π/3

    print(pt0, to_polar(pt0))  # (√2, √2) (2, π/4)
    print(pt1, to_polar(pt1))  # (1, √3) (2, π/3)

main()
