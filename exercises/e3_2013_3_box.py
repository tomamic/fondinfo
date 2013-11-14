class Box:
    def __init__(self, w: int, h: int):
        self._w = w
        self._h = h
        
    def area(self) -> int:
        return self._w * self._h

    def perimeter(self) -> int:
        return 2 * (self._w + self._h)

    def dimensions(self) -> (int, int):
        return (self._w, self._h)
    
if __name__ == '__main__':
    width = int(input('width? '))
    height = int(input('height? '))
    while width > 0 and height > 0:
        box = Box(width, height)
        a = box.area()
        p = box.perimeter()
        print('area =', a)
        print('perimeter =', p)
        width = int(input('width? '))
        height = int(input('height? '))
