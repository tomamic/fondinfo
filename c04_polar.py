#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from math import sin, cos, radians, degrees, hypot, atan2, pi, dist

Point = tuple[float, float]  # Pt in cartesian coords (x, y)
Polar = tuple[float, float]  # Pt in polar coords (r, angle)

def to_polar(pt: Point) -> Polar:
    """
    Convert from cartesian to polar coords
    """
    x, y = pt
    return (hypot(x, y), degrees(atan2(y, x)))

def from_polar(plr: Polar) -> Point:
    """
    Convert from polar to cartesian coords
    """
    r, angle = plr
    return (r * cos(radians(angle)), r * sin(radians(angle)))

def move_around(start: Point, length: float, angle: float) -> Point:
    """
    Move from `start` pt, by given `lenght` and `angle` (direction)
    """
    x0, y0 = start
    dx, dy = from_polar((length, angle))
    return x0 + dx, y0 + dy

def rotate(pt: Point, angle: float) -> Point:
    """
    Rotate a point in cartesian coords by a given angle
    """
    r, a = to_polar(pt)
    return from_polar((r, a + angle))

def main():
    pt0 = from_polar((2, 45))  # (√2, √2) ∡ 45°
    pt1 = rotate(pt0, 15)  # (1, √3) ∡ 60°

    print(pt0, to_polar(pt0))  # (√2, √2) (2, 45°)
    print(pt1, to_polar(pt1))  # (1, √3) (2, 60°)

if __name__ == "__main__":
    main()
