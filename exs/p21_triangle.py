#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

def triangle_perimeter(a: float, b: float, c: float) -> float:
    if a > b + c or b > a + c or c > a + b:
        raise ValueError("Not a triangle")
    return a + b + c
    
def main():
    again = True
    while again:
        a = float(input("a? "))
        b = float(input("b? "))
        c = float(input("c? "))
        try:
            print(triangle_perimeter(a, b, c))
        except ValueError as e:
            print(e)
    
        again = input("Continue [Y/N]? ") in "Yy"
        
if __name__ == "__main__":
    main()
    