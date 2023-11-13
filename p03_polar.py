from math import cos, atan2, pi, sin, sqrt

Point = tuple[float, float]  # A point in cartesian coords (x, y)
Polar = tuple[float, float]  # A point in polar coords (r, a)

def radius(pt: Point) -> float:
    x, y = pt
    return sqrt(x ** 2 + y ** 2)

def angle(pt: Point) -> float:
    x, y = pt
    return atan2(y, x)  # atan(y/x), correct sign

def to_polar(pt: Point) -> Polar:
    r = radius(pt)
    a = angle(pt)
    return (r, a)

def from_polar(plr: Polar) -> Point:
    r, a = plr
    return (r * cos(a), r * sin(a))

def rotate(pt: Point, angle: float) -> Point:
    r, a = to_polar(pt)
    return from_polar((r, a + angle))

def move_around(start: Point, length: float, angle: float) -> Point:
    x, y = start
    dx, dy = from_polar((length, angle))
    return x + dx, y + dy

def main():
    pt0 = from_polar((2, pi/4))
    # pt0 = sqrt(2), sqrt(2)  # same point, ∡ π/4
    pt1 = rotate(pt0, pi/12)  # (1, √3) ∡ π/3

    print(pt0, to_polar(pt0))  # (√2, √2) (2, π/4)
    print(pt1, to_polar(pt1))  # (1, √3) (2, π/3)


if __name__ == "__main__":
    main()  # won't run automatically, if the script is imported elsewhere
