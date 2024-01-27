#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from math import sin, cos, radians, hypot, atan2

Point = tuple[float, float]  # Pt in cartesian coords (x, y)
Polar = tuple[float, float]  # Pt in polar coords (r, angle)

def to_polar(pt: Point) -> Polar:
    '''
    Convert from cartesian to polar coords
    '''
    x, y = pt
    return (hypot(x, y), atan2(y, x))

def from_polar(plr: Polar) -> Point:
    '''
    Convert from polar to cartesian coords
    '''
    r, angle = plr
    return (r * cos(angle), r * sin(angle))

def move_around(start: Point, length: float, angle: float) -> Point:
    '''
    Move from `start` pt, by given `lenght` and `angle` (direction)
    '''
    x0, y0 = start
    dx, dy = from_polar((length, angle))
    return x0 + dx, y0 + dy

def rotate(pt: Point, angle: float) -> Point:
    '''
    Rotate a point in cartesian coords by a given angle
    '''
    r, a = to_polar(pt)
    return from_polar((r, a + angle))

def main():
    pt0 = from_polar((2, radians(45)))
    # pt0 = sqrt(2), sqrt(2)  # same point, ∡ 45°
    pt1 = rotate(pt0, radians(15))  # (1, √3) ∡ 60°

    print(pt0, to_polar(pt0))  # (√2, √2) (2, π/4)
    print(pt1, to_polar(pt1))  # (1, √3) (2, π/3)

if __name__ == "__main__":
    main()  # won't run automatically, if script is imported elsewhere
    