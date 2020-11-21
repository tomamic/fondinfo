from math import sin, cos, atan2, pi, sqrt

def radius(pt: (float, float)) -> float:
    x, y = pt  # ❗ sequence unpacking
    return (x ** 2 + y ** 2) ** 0.5

def angle(pt: (float, float)) -> float:
    x, y = pt
    return atan2(y, x)

def to_polar(pt: (float, float)) -> (float, float):
    r = radius(pt)
    a = angle(pt)
    return (r, a)  # ❗ return a tuple

def from_polar(pol: (float, float)) -> (float, float):
    r, a = pol
    return (r * cos(a), r * sin(a))

def main():
    r1, a1 = to_polar((0.5, 0.866))  # 1, π/3
    x1, y1 = from_polar((1, pi/3))  # 1/2, √3/2
    print(r1, a1)
    print(x1, y1)

#main()