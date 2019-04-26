#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import math

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self._x, self._y = x, y

    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y
    
    @property
    def angle(self) -> float:
        return math.atan2(self._y, self._x) * 180.0 / math.pi
    
    @property
    def radius(self) -> float:
        return math.sqrt(self._x ** 2 + self._y ** 2)
    
    def set_cartesian(self, x: float, y: float):
        self._x, self._y = x, y

    def set_polar(self, angle: float, radius: float):
        self._x = radius * math.cos(angle * math.pi / 180.0)
        self._y = radius * math.sin(angle * math.pi / 180.0)        

    def distance(self, other: 'Point') -> float:
        dx = self._x - other._x
        dy = self._y - other._y
        return math.sqrt(dx ** 2 + dy ** 2);

    def parse(text: str) -> 'Point':
        dat = text.split(',')
        return Point(float(dat[0]), float(dat[1]))

    def __str__(self) -> str:
        return '{}, {}'.format(self._x, self._y)


if __name__ == '__main__':
    NEW_POINT = 1
    DEL_POINT = 2
    DISTANCE = 3
    EXIT = 9

    points = []
    choice = 0
    while choice != EXIT:
        for i, p in enumerate(points):
            print(i, p)

        print('Enter your coice:')
        print('1. Create point (x, y)')
        print('2. Delete point (index)')
        print('3. Calculate distance (index1, index2)')
        print('9. Exit')

        choice = int(input())
        
        if choice == NEW_POINT:
            p = Point.parse(input())
            points.append(p)
        elif choice == DEL_POINT:
            id = int(input())
            if 0 <= id < len(points):
                points.pop(id)
        elif choice == DISTANCE:
            id1 = int(input())
            id2 = int(input())
            if (0 <= id1 < len(points)) and (0 <= id2 < len(points)):
                p1 = points[id1]
                p2 = points[id2]
                print(p1.distance(p2))
