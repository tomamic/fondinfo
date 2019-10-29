class Box:
    def __init__(self, width: float, height: float):
        self._w = width
        self._h = height
    def area(self) -> float:
        return self._w * self._h
    def perimeter(self) -> float:
        return 2 * (self._w + self._h)

def main():
    w = float(input("w? "))
    h = float(input("h? "))

    b = Box(w, h)
    print(b.area(), b.perimeter())
    
