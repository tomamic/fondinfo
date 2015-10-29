from math import pi, sqrt

class Shape:

    def perimeter(self):
        raise NotImplementedError("Abstract method")

    def area(self):
        raise NotImplementedError("Abstract method")
    

class Triangle(Shape):

    def __init__(self, side1: float, side2: float, side3: float):
        self._a = side1
        self._b = side2
        self._c = side3

    def perimeter(self) -> float:
        p = self._a + self._b + self._c
        return p

    def area(self) -> float:
        s = (self._a + self._b + self._c) / 2
        a = sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))
        return a

    def __str__(self):
        # give a string representation of this Triangle
        return 'Triangle: {}, {}, {}'.format(self._a, self._b, self._c)


class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self._w = width
        self._h = height

    def perimeter(self) -> float:
        p = 2 * (self._w + self._h)
        return p

    def area(self) -> float:
        a = self._w * self._h
        return a

    def __str__(self):
        # give a string representation of this Rectangle
        return 'Rectangle: {}, {}'.format(self._w, self._h)


class Circle(Shape):

    def __init__(self, radius: float):
        self._r = radius

    def perimeter(self) -> float:
        p = 2 * pi * self._r
        return p

    def area(self) -> float:
        a = pi * self._r ** 2
        return a

    def __str__(self):
        # give a string representation of this Circle
        return 'Circle: {}'.format(self._r)


def main():
    shapes = []  # a list of Shape objects
    
    action_choice = input('A/R/X (Add/Remove/Exit)? ').upper()
    while action_choice != 'X':
        if action_choice == 'A':
            shape_choice = input('C/T/R (Circle/Rectangle/Triangle)? ').upper()
            if shape_choice == 'C':
                r = float(input('radius? '))
                c = Circle(r)
                shapes.append(c)
            elif shape_choice == 'T':
                s1 = float(input('side1? '))
                s2 = float(input('side2? '))
                s3 = float(input('side3? '))
                t = Triangle(s1, s2, s3)
                shapes.append(t)
            elif shape_choice == 'R':
                w = float(input('width? '))
                h = float(input('height? '))
                r = Rectangle(w, h)
                shapes.append(r)
        elif action_choice == 'R':
            i = int(input('index (0-based)? '))
            if 0 <= i < len(shapes):
                shapes.pop(i)

        total_area = 0
        for s in shapes:
            a = s.area()
            p = s.perimeter()
            total_area += a
            print(s)  # Python calls s.__str__()
            print('area:', a)
            print('perimeter:', p)
            print()
            
        print('total area:', total_area)
        action_choice = input('A/R/X (Add/Remove/Exit)? ').upper()
    

if __name__ == '__main__':
    main()
