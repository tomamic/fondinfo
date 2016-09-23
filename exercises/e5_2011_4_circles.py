#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import math

from e4_2011_4_points import Point

class Circle:
    def __init__(self, center: Point, radius: float):
        self._center, self._radius = center, radius
        
    @property
    def center(self) -> float:
        return self._center
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

    @property
    def area(self) -> float:
        return math.pi * self._radius ** 2

    def parse(text: str) -> 'Circle':
        dat = text.split(',')
        center = Point(float(dat[0].strip()), float(dat[1].strip()))
        radius = float(dat[3].strip())
        return Circle(center, radius)

    def __str__(self) -> str:
        return '{}, {}'.format(self._center, self._radius)
        
            
if __name__ == '__main__':
    NEW_POINT = 1
    MOVE_POINT = 2
    NEW_CIRCLE = 3
    EXIT = 9

    points = []
    circles = []

    choice = 0
    while choice != EXIT:
        print('Points:')
        for i, p in enumerate(points):
            print(i, p)
            
        print('Circles:')
        for i, c in enumerate(circles):
            print(i, c)
            
        print('Enter your coice:')
        print('1. Create point (x, y)')
        print('2. Move point (point-id, x, y)')
        print('3. Create circle (point-id, radius)')
        print('9. Exit')

        choice = int(input('choice? '))
        if choice == NEW_POINT:
            p = Point.parse(input('x, y? '))
            points.append(p)
        elif choice == MOVE_POINT:
            i = int(input('i? '))
            x = float(input('x? '))
            y = float(input('y? '))
            if 0 <= i < len(points):
                p = points[i]
                p.set_cartesian(x, y)
        elif choice == NEW_CIRCLE:
            i = int(input('i? '))
            r = float(input('r? '))
            if 0 <= i < len(points):
                p = points[i]
                c = Circle(p, r)
                circles.append(c)
