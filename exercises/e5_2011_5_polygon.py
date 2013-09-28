import math, sys

from e4_2011_4_points import Point

class Polygon:
    def __init__(self):
        self._points = []

    @property
    def perimeter(self) -> float:
        result = 0
        for i, p in enumerate(self._points):
            q = self._points[(i + 1) % len(self._points)]
            result += p.distance(q)
        return result

    def parse(text: str) -> 'Polygon':
        polygon = Polygon()
        rows = text.strip().split('\n')
        for row in rows:
            p = Point.parse(row)
            polygon._points.append(p)
        return polygon

    def __str__(self) -> str:
        result = []
        for p in self._points:
            result.append(str(p))
        return '\n'.join(result)


if __name__ == '__main__':
    text = sys.stdin.read()  # CTRL+D / CTRL+Z to close the stdin stream
    x = Polygon.parse(text)

    print(x.perimeter)

    with open('polygon.txt', 'w') as outfile:
        print(x, file=outfile)
